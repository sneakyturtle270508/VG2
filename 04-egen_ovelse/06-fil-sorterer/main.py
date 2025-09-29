# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-26 13:25:57
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-26 18:18:08
import os
import re
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

class CourseFileOrganizer(FileSystemEventHandler):
    def __init__(self, watch_directory):
        self.watch_directory = Path(watch_directory)
        # This will store known courses - dynamically updated
        self.known_courses = set()
        
        # Initialize by scanning existing files and folders
        self._discover_existing_courses()
    
    def _discover_existing_courses(self):
        """Discover existing courses from folder names and organize files by date"""
        print("Discovering existing courses...")
        
        # Find existing course folders
        for item in self.watch_directory.iterdir():
            if item.is_dir():
                course_name = item.name.lower()
                self.known_courses.add(course_name)
                print(f"Found existing course: {course_name}")
        
        # Reorganize all files by creation date
        self._reorganize_all_files()
    
    def _extract_course_from_filename(self, filename):
        """Extract course name from filename (everything before first underscore or space)"""
        filename_lower = filename.lower()
        
        # Remove file extension
        name_without_ext = Path(filename_lower).stem
        
        # Remove existing number prefix if present
        name_without_prefix = re.sub(r'^\d{2}_', '', name_without_ext)
        
        # Extract course name (first word or everything before underscore)
        if '_' in name_without_prefix:
            course = name_without_prefix.split('_')[0]
        elif ' ' in name_without_prefix:
            course = name_without_prefix.split(' ')[0]
        else:
            # If no separator, take first few characters or whole name if short
            course = name_without_prefix[:8] if len(name_without_prefix) > 8 else name_without_prefix
        
        # Clean up course name (remove special characters, keep only letters and numbers)
        course = re.sub(r'[^a-z0-9]', '', course)
        
        return course if course else "ukjent"
    
    def _get_file_creation_time(self, file_path):
        """Get file creation time"""
        try:
            return file_path.stat().st_ctime
        except:
            return time.time()
    
    def _reorganize_course_files(self, course):
        """Reorganize all files in a course folder by creation date"""
        course_folder = self.watch_directory / course
        
        if not course_folder.exists():
            return
        
        # Get all files in the course folder
        files = [f for f in course_folder.iterdir() if f.is_file()]
        
        if not files:
            return
        
        # Sort files by creation time (oldest first)
        files_with_time = [(f, self._get_file_creation_time(f)) for f in files]
        files_with_time.sort(key=lambda x: x[1])
        
        print(f"Reorganizing {len(files)} files in {course} folder by creation date...")
        
        # Rename files temporarily to avoid conflicts
        temp_names = []
        for i, (file_path, _) in enumerate(files_with_time):
            temp_name = course_folder / f"temp_{i}_{file_path.name}"
            file_path.rename(temp_name)
            temp_names.append(temp_name)
        
        # Rename with proper numbering
        for i, temp_file in enumerate(temp_names):
            # Remove old number prefix if it exists
            original_name = re.sub(r'^temp_\d+_\d{2}_', '', temp_file.name)
            original_name = re.sub(r'^temp_\d+_', '', original_name)
            
            new_name = f"{i:02d}_{original_name}"
            final_path = course_folder / new_name
            temp_file.rename(final_path)
            
        print(f"Reorganized {course} folder with files numbered 00-{len(files)-1:02d}")
    
    def _reorganize_all_files(self):
        """Reorganize all files in all course folders and loose files in main directory"""
        print("Reorganizing all files by creation date...")
        
        # First, handle loose files in main directory
        loose_files = [f for f in self.watch_directory.iterdir() if f.is_file()]
        
        for file_path in loose_files:
            course = self._extract_course_from_filename(file_path.name)
            self._add_course_and_move_file(course, file_path)
        
        # Then reorganize each course folder
        for course in self.known_courses:
            self._reorganize_course_files(course)
    
    def _add_course_and_move_file(self, course, file_path):
        """Add a new course if needed and move file to appropriate folder"""
        if course not in self.known_courses:
            self.known_courses.add(course)
            print(f"Added new course: {course}")
        
        # Create course folder if it doesn't exist
        course_folder = self.watch_directory / course
        course_folder.mkdir(exist_ok=True)
        
        # Move file to course folder (temporarily without number prefix)
        temp_filename = f"{file_path.name}"
        temp_path = course_folder / temp_filename
        
        try:
            file_path.rename(temp_path)
            print(f"Moved {file_path.name} to {course} folder")
            
            # Reorganize the entire course folder to maintain date order
            self._reorganize_course_files(course)
            
        except Exception as e:
            print(f"Error moving file {file_path}: {e}")
    
    def on_created(self, event):
        """Handle file creation events"""
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        
        # Skip temporary files and system files
        if (file_path.name.startswith('temp_') or 
            file_path.name.startswith('.') or 
            file_path.name.startswith('~') or
            file_path.suffix in ['.tmp', '.temp']):
            return
        
        print(f"\nNew file detected: {file_path.name}")
        print("⏳ Waiting for you to finish creating/editing the file...")
        
        # Wait longer to ensure file is completely written and user is done editing
        time.sleep(3)
        
        # Check if file still exists (might have been deleted/renamed by user)
        if not file_path.exists():
            print("❌ File no longer exists, skipping...")
            return
        
        # Check if file is still being written to (file size changing)
        initial_size = file_path.stat().st_size if file_path.exists() else 0
        time.sleep(1)
        current_size = file_path.stat().st_size if file_path.exists() else 0
        
        if initial_size != current_size:
            print("⏳ File still being modified, waiting longer...")
            time.sleep(30)
        
        print(f"✅ Processing file: {file_path.name}")
        
        # Extract course name from filename
        course = self._extract_course_from_filename(file_path.name)
        print(f"📚 Detected course: {course}")
        
        # Add course and move file
        self._add_course_and_move_file(course, file_path)
    
    def on_moved(self, event):
        """Handle file move events (like drag and drop)"""
        if event.is_directory:
            return
        
        file_path = Path(event.dest_path)
        
        # Skip if file is already in a course folder
        parent_folder = file_path.parent.name.lower()
        if parent_folder in self.known_courses:
            return
        
        # Skip temporary files and system files
        if (file_path.name.startswith('temp_') or 
            file_path.name.startswith('.') or 
            file_path.name.startswith('~') or
            file_path.suffix in ['.tmp', '.temp']):
            return
        
        print(f"\nFile moved to directory: {file_path.name}")
        print("⏳ Waiting to ensure file transfer is complete...")
        
        # Wait to ensure file operation is complete
        time.sleep(2)
        
        # Check if file still exists
        if not file_path.exists():
            print("❌ File no longer exists, skipping...")
            return
        
        print(f"✅ Processing moved file: {file_path.name}")
        
        # Extract course name from filename
        course = self._extract_course_from_filename(file_path.name)
        print(f"📚 Detected course: {course}")
        
        # Add course and move file
        self._add_course_and_move_file(course, file_path)

def organize_existing_files(directory):
    """Organize files that already exist in the directory"""
    organizer = CourseFileOrganizer(directory)
    return organizer

def start_monitoring(directory):
    """Start monitoring a directory for new files"""
    # First organize existing files
    organizer = organize_existing_files(directory)
    
    # Set up file system watcher
    observer = Observer()
    observer.schedule(organizer, directory, recursive=False)
    
    print(f"\n🔍 Starting file monitor for: {directory}")
    print("📚 Courses will be automatically detected from filenames")
    print("📅 Files will be numbered by creation date (oldest = 00)")
    print("⏰ Script waits 3+ seconds after file creation before organizing")
    print("⏹️  Press Ctrl+C to stop monitoring")
    print("-" * 60)
    
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n⏹️  Stopping file monitor...")
    
    observer.join()

if __name__ == "__main__":
    # Configuration - Your specific school folder path
    WATCH_DIRECTORY = r"C:\Users\WilliamBergeGrønsber\OneDrive - Telemark fylkeskommune\vg2"
    
    # Create directory if it doesn't exist
    Path(WATCH_DIRECTORY).mkdir(parents=True, exist_ok=True)
    
    print("🎓 Smart Course File Organizer")
    print("=" * 50)
    print(f"📁 Monitoring directory: {WATCH_DIRECTORY}")
    print("\n🤖 How it works:")
    print("  • Automatically detects course names from filenames")
    print("  • Creates course folders as needed")
    print("  • Numbers files by creation date (oldest first)")
    print("  • Reorganizes when older files are added")
    print("\n📝 Examples:")
    print("  'matte_oppgave.pdf' → matte/00_oppgave.pdf")
    print("  'engelsk_essay.docx' → engelsk/00_essay.docx")
    print("  'historie_notater.txt' → historie/00_notater.txt")
    
    # Start monitoring
    start_monitoring(WATCH_DIRECTORY)