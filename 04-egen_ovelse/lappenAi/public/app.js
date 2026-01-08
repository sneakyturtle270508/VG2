const API_URL = window.location.origin;

let currentUser = null;
let currentNoteId = null;
let authToken = null;

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    // Load saved theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-theme', savedTheme);
    const themeSelect = document.getElementById('theme-select');
    if (themeSelect) {
        themeSelect.value = savedTheme;
    }

    authToken = localStorage.getItem('token');
    if (authToken) {
        // Decode token to get user info
        try {
            const payload = JSON.parse(atob(authToken.split('.')[1]));
            currentUser = { id: payload.id, username: payload.username };
            updateUserDisplay();
        } catch (e) {
            console.error('Error decoding token:', e);
        }
        showApp();
        loadNotes();
    } else {
        showAuth();
    }

    // Tab switching
    document.querySelectorAll('.tab').forEach(tab => {
        tab.addEventListener('click', () => {
            const tabName = tab.dataset.tab;
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.auth-form').forEach(f => f.classList.remove('active'));
            tab.classList.add('active');
            document.getElementById(`${tabName}-form`).classList.add('active');
        });
    });

    // Close user menu when clicking outside
    document.addEventListener('click', (e) => {
        const userMenu = document.getElementById('user-menu');
        const userIconBtn = document.getElementById('user-icon-btn');
        if (userMenu && !userMenu.contains(e.target) && !userIconBtn.contains(e.target)) {
            userMenu.classList.add('hidden');
        }
    });
});

function showAuth() {
    document.getElementById('auth-screen').classList.remove('hidden');
    document.getElementById('app-screen').classList.add('hidden');
}

function showApp() {
    document.getElementById('auth-screen').classList.add('hidden');
    document.getElementById('app-screen').classList.remove('hidden');
}

async function register() {
    const username = document.getElementById('register-username').value;
    const password = document.getElementById('register-password').value;
    const errorEl = document.getElementById('register-error');

    if (!username || !password) {
        errorEl.textContent = 'Please fill in all fields';
        return;
    }

    try {
        const response = await fetch(`${API_URL}/api/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            authToken = data.token;
            localStorage.setItem('token', authToken);
            currentUser = data.user;
            updateUserDisplay();
            showApp();
            loadNotes();
        } else {
            errorEl.textContent = data.error || 'Registration failed';
        }
    } catch (error) {
        errorEl.textContent = 'Connection error. Please try again.';
    }
}

async function login() {
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
    const errorEl = document.getElementById('auth-error');

    if (!username || !password) {
        errorEl.textContent = 'Please fill in all fields';
        return;
    }

    try {
        const response = await fetch(`${API_URL}/api/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            authToken = data.token;
            localStorage.setItem('token', authToken);
            currentUser = data.user;
            updateUserDisplay();
            showApp();
            loadNotes();
        } else {
            errorEl.textContent = data.error || 'Login failed';
        }
    } catch (error) {
        errorEl.textContent = 'Connection error. Please try again.';
    }
}

function logout() {
    authToken = null;
    localStorage.removeItem('token');
    currentUser = null;
    showAuth();
}

function getAuthHeaders() {
    return {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authToken}`
    };
}

// Notes functions
async function loadNotes() {
    try {
        const response = await fetch(`${API_URL}/api/notes`, {
            headers: getAuthHeaders()
        });

        if (response.ok) {
            const notes = await response.json();
            displayNotes(notes);
        }
    } catch (error) {
        console.error('Error loading notes:', error);
    }
}

function displayNotes(notes) {
    const notesList = document.getElementById('notes-list');
    
    if (notes.length === 0) {
        notesList.innerHTML = '<div class="empty-state"><h3>No notes yet</h3><p>Create your first note to get started</p></div>';
        return;
    }

    notesList.innerHTML = notes.map(note => `
        <div class="note-card" onclick="openNote(${note.id})">
            <div class="note-preview">${escapeHtml(note.content.substring(0, 200))}</div>
            <div class="note-date">${new Date(note.updated_at).toLocaleDateString()}</div>
        </div>
    `).join('');
}

function createNewNote() {
    currentNoteId = null;
    document.getElementById('note-content').value = '';
    
    // Hide all views
    document.querySelectorAll('.view').forEach(v => {
        v.classList.remove('active');
        v.classList.add('hidden');
    });
    
    // Show editor - remove hidden and add active
    const editor = document.getElementById('note-editor');
    editor.classList.remove('hidden');
    editor.classList.add('active');
    
    // Focus on textarea
    setTimeout(() => {
        document.getElementById('note-content').focus();
    }, 100);
}

function openNote(id) {
    currentNoteId = id;
    fetch(`${API_URL}/api/notes`, {
        headers: getAuthHeaders()
    })
    .then(res => res.json())
    .then(notes => {
        const note = notes.find(n => n.id === id);
        if (note) {
            document.getElementById('note-content').value = note.content;
            
            // Hide all views
            document.querySelectorAll('.view').forEach(v => {
                v.classList.remove('active');
                v.classList.add('hidden');
            });
            
            // Show editor
            const editor = document.getElementById('note-editor');
            editor.classList.remove('hidden');
            editor.classList.add('active');
            
            // Focus on textarea
            setTimeout(() => {
                document.getElementById('note-content').focus();
            }, 100);
        }
    });
}

function closeEditor() {
    // Hide editor
    const editor = document.getElementById('note-editor');
    editor.classList.remove('active');
    editor.classList.add('hidden');
    
    // Show notes view
    const notesView = document.getElementById('notes-view');
    notesView.classList.remove('hidden');
    notesView.classList.add('active');
    
    currentNoteId = null;
    loadNotes();
}

async function saveNote() {
    const content = document.getElementById('note-content').value;

    if (!content.trim()) {
        alert('Note cannot be empty');
        return;
    }

    try {
        const url = currentNoteId 
            ? `${API_URL}/api/notes/${currentNoteId}`
            : `${API_URL}/api/notes`;
        
        const method = currentNoteId ? 'PUT' : 'POST';

        const response = await fetch(url, {
            method,
            headers: getAuthHeaders(),
            body: JSON.stringify({ content })
        });

        if (response.ok) {
            const data = await response.json();
            if (!currentNoteId) {
                currentNoteId = data.id;
            }
            alert('Note saved!');
        } else {
            alert('Failed to save note');
        }
    } catch (error) {
        alert('Error saving note');
    }
}

async function generateFlashcards() {
    if (!currentNoteId) {
        alert('Please save the note first');
        return;
    }

    const btn = event.target;
    const originalText = btn.textContent;
    btn.textContent = 'Generating...';
    btn.disabled = true;

    try {
        const response = await fetch(`${API_URL}/api/notes/${currentNoteId}/flashcards`, {
            method: 'POST',
            headers: getAuthHeaders()
        });

        const data = await response.json();

        if (response.ok) {
            alert(`Generated ${data.count} flashcards! Check the Flashcards tab.`);
            // Refresh flashcards view if it's currently open
            if (document.getElementById('flashcards-view').classList.contains('active')) {
                showFlashcards();
            }
        } else {
            let errorMsg = data.error || 'Failed to generate flashcards';
            if (errorMsg.includes('Ollama') || errorMsg.includes('connect')) {
                errorMsg += '\n\nDon\'t worry! The app used a fallback method to create flashcards from your notes.';
            }
            alert(errorMsg);
        }
    } catch (error) {
        alert('Error generating flashcards. The app will use a fallback method to create flashcards from your notes.');
    } finally {
        btn.textContent = originalText;
        btn.disabled = false;
    }
}

async function generateQuestions() {
    if (!currentNoteId) {
        alert('Please save the note first');
        return;
    }

    const btn = event.target;
    const originalText = btn.textContent;
    btn.textContent = 'Generating...';
    btn.disabled = true;

    try {
        const response = await fetch(`${API_URL}/api/notes/${currentNoteId}/questions`, {
            method: 'POST',
            headers: getAuthHeaders()
        });

        const data = await response.json();

        if (response.ok) {
            alert(`Generated ${data.count} questions! Check the Questions tab.`);
            // Refresh questions view if it's currently open
            if (document.getElementById('questions-view').classList.contains('active')) {
                showQuestions();
            }
        } else {
            let errorMsg = data.error || 'Failed to generate questions';
            if (errorMsg.includes('Ollama') || errorMsg.includes('connect')) {
                errorMsg += '\n\nDon\'t worry! The app used a fallback method to create questions from your notes.';
            }
            alert(errorMsg);
        }
    } catch (error) {
        alert('Error generating questions. The app will use a fallback method to create questions from your notes.');
    } finally {
        btn.textContent = originalText;
        btn.disabled = false;
    }
}

// Navigation
function showNotes() {
    setActiveView('notes');
    loadNotes();
}

async function showFlashcards() {
    setActiveView('flashcards');
    
    try {
        const response = await fetch(`${API_URL}/api/flashcards`, {
            headers: getAuthHeaders()
        });

        if (response.ok) {
            const flashcards = await response.json();
            displayFlashcards(flashcards);
        }
    } catch (error) {
        console.error('Error loading flashcards:', error);
    }
}

async function showQuestions() {
    setActiveView('questions');
    
    try {
        const response = await fetch(`${API_URL}/api/questions`, {
            headers: getAuthHeaders()
        });

        if (response.ok) {
            const questions = await response.json();
            displayQuestions(questions);
        }
    } catch (error) {
        console.error('Error loading questions:', error);
    }
}

function setActiveView(viewName) {
    // Hide all views
    document.querySelectorAll('.view').forEach(v => {
        v.classList.remove('active');
        v.classList.add('hidden');
    });
    
    // Hide settings if open
    document.getElementById('settings-view').classList.remove('active');
    document.getElementById('settings-view').classList.add('hidden');
    
    // Show the requested view
    const targetView = document.getElementById(`${viewName}-view`);
    if (targetView) {
        targetView.classList.remove('hidden');
        targetView.classList.add('active');
    }
    
    // Update nav buttons
    document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
    const navBtn = document.querySelector(`[data-view="${viewName}"]`);
    if (navBtn) {
        navBtn.classList.add('active');
    }
}

function updateUserDisplay() {
    if (currentUser) {
        const usernameDisplay = document.getElementById('username-display');
        const userMenuUsername = document.getElementById('user-menu-username');
        const settingsUsername = document.getElementById('settings-username');
        
        if (usernameDisplay) usernameDisplay.textContent = currentUser.username;
        if (userMenuUsername) userMenuUsername.textContent = currentUser.username;
        if (settingsUsername) settingsUsername.textContent = currentUser.username;
    }
}

function toggleUserMenu() {
    const menu = document.getElementById('user-menu');
    menu.classList.toggle('hidden');
}

async function showUserSettings() {
    document.getElementById('user-menu').classList.add('hidden');
    
    // Hide all views
    document.querySelectorAll('.view').forEach(v => {
        v.classList.remove('active');
        v.classList.add('hidden');
    });
    
    // Show settings
    const settingsView = document.getElementById('settings-view');
    settingsView.classList.remove('hidden');
    settingsView.classList.add('active');
    
    // Load user data
    if (currentUser) {
        document.getElementById('settings-username').textContent = currentUser.username;
        
        // Load available contexts and populate dropdown
        try {
            const contextsResponse = await fetch(`${API_URL}/api/contexts`, {
                headers: getAuthHeaders()
            });
            if (contextsResponse.ok) {
                const contexts = await contextsResponse.json();
                const contextSelect = document.getElementById('context-select');
                
                // Clear and populate context select
                if (contextSelect) {
                    contextSelect.innerHTML = contexts.map(ctx => 
                        `<option value="${ctx.id}">${ctx.name}</option>`
                    ).join('');
                }
            }
            
            // Load user preferences
            const response = await fetch(`${API_URL}/api/preferences`, {
                headers: getAuthHeaders()
            });
            if (response.ok) {
                const prefs = await response.json();
                const contextSelect = document.getElementById('context-select');
                const contextDesc = document.getElementById('context-description');
                
                if (contextSelect) {
                    contextSelect.value = prefs.ai_context || 'car-theory';
                }
                
                // Update description
                const contextsResponse2 = await fetch(`${API_URL}/api/contexts`, {
                    headers: getAuthHeaders()
                });
                if (contextsResponse2.ok) {
                    const contexts = await contextsResponse2.json();
                    const selectedContext = contexts.find(c => c.id === (prefs.ai_context || 'car-theory'));
                    if (selectedContext && contextDesc) {
                        contextDesc.textContent = selectedContext.description;
                    }
                }
            }
        } catch (error) {
            console.error('Error loading preferences:', error);
        }
    }
}

function closeSettings() {
    const settingsView = document.getElementById('settings-view');
    settingsView.classList.remove('active');
    settingsView.classList.add('hidden');
    showNotes();
}

function changeTheme() {
    const theme = document.getElementById('theme-select').value;
    document.body.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
}

async function changeContext() {
    const contextSelect = document.getElementById('context-select');
    const contextDesc = document.getElementById('context-description');
    const selectedContext = contextSelect.value;
    
    if (!selectedContext) return;
    
    try {
        // Update description
        const response = await fetch(`${API_URL}/api/contexts`, {
            headers: getAuthHeaders()
        });
        if (response.ok) {
            const contexts = await response.json();
            const context = contexts.find(c => c.id === selectedContext);
            if (context && contextDesc) {
                contextDesc.textContent = context.description;
            }
        }
        
        // Save preference
        const saveResponse = await fetch(`${API_URL}/api/preferences`, {
            method: 'PUT',
            headers: getAuthHeaders(),
            body: JSON.stringify({ ai_context: selectedContext })
        });
        
        if (saveResponse.ok) {
            // Show success message
            const desc = contextDesc || document.createElement('div');
            const originalText = desc.textContent;
            desc.textContent = '✓ Context updated!';
            desc.style.color = 'var(--primary-color)';
            setTimeout(() => {
                desc.textContent = originalText;
                desc.style.color = '';
            }, 2000);
        } else {
            alert('Failed to update context preference');
        }
    } catch (error) {
        console.error('Error updating context:', error);
        alert('Error updating context preference');
    }
}

function exportData() {
    // Export all notes as JSON
    fetch(`${API_URL}/api/notes`, {
        headers: getAuthHeaders()
    })
    .then(res => res.json())
    .then(notes => {
        const dataStr = JSON.stringify(notes, null, 2);
        const dataBlob = new Blob([dataStr], { type: 'application/json' });
        const url = URL.createObjectURL(dataBlob);
        const link = document.createElement('a');
        link.href = url;
        link.download = `lappen-notes-${new Date().toISOString().split('T')[0]}.json`;
        link.click();
        URL.revokeObjectURL(url);
    })
    .catch(err => {
        alert('Error exporting data');
    });
}

function displayFlashcards(flashcards) {
    const container = document.getElementById('flashcards-list');
    
    if (flashcards.length === 0) {
        container.innerHTML = '<div class="empty-state"><h3>No flashcards yet</h3><p>Generate flashcards from your notes</p></div>';
        return;
    }

    container.innerHTML = flashcards.map((card, index) => `
        <div class="flashcard" onclick="flipCard(${index})" id="flashcard-${index}">
            <div class="flashcard-label">Front</div>
            <div class="flashcard-front">${escapeHtml(card.front)}</div>
            <div class="flashcard-back">${escapeHtml(card.back)}</div>
        </div>
    `).join('');
}

function flipCard(index) {
    const card = document.getElementById(`flashcard-${index}`);
    card.classList.toggle('flipped');
}

function displayQuestions(questions) {
    const container = document.getElementById('questions-list');
    
    if (questions.length === 0) {
        container.innerHTML = '<div class="empty-state"><h3>No questions yet</h3><p>Generate questions from your notes</p></div>';
        return;
    }

    container.innerHTML = questions.map(q => `
        <div class="question-card">
            <h3>${escapeHtml(q.question)}</h3>
            <div class="answer">${escapeHtml(q.answer)}</div>
        </div>
    `).join('');
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

