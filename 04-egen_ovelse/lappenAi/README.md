# Lappen AI - Learning Notes App

A minimalistic note-taking application with AI-powered flashcard and question generation using Ollama.

## Features

- **User Authentication**: Multiple user support with secure login/registration
- **Note Taking**: Clean, minimalistic interface for writing and organizing notes
- **AI-Powered Flashcards**: Generate flashcards from your notes using Ollama
- **AI-Powered Questions**: Generate practice questions from your notes
- **Minimalistic Design**: Clean, distraction-free interface

## Requirements

- Node.js (v14 or higher)
- Ollama with llama3.2 model installed
- FTP server for deployment

## Setup

1. Install dependencies:
```bash
npm install
```

2. Configure environment variables:
```bash
cp .env.example .env
```

Edit `.env` and set:
- `PORT`: Server port (default: 3000)
- `JWT_SECRET`: Secret key for JWT tokens (change this!)
- `OLLAMA_URL`: URL of your Ollama server (default: http://localhost:11434)

3. Make sure Ollama is running and has the llama3.2 model:
```bash
ollama pull llama3.2
```

4. Start the server:
```bash
npm start
```

5. Open your browser and navigate to `http://localhost:3000`

## Deployment to FTP Server

1. Upload all files to your FTP server
2. Make sure Node.js is installed on the server
3. Install dependencies on the server: `npm install`
4. Set up environment variables on the server
5. Run the server (consider using PM2 or similar for production):
```bash
npm start
```

## Usage

1. **Register/Login**: Create an account or login with existing credentials
2. **Create Notes**: Click "New Note" to start writing
3. **Save Notes**: Click "Save" to save your notes
4. **Generate Flashcards**: After saving a note, click "Generate Flashcards" to create flashcards
5. **Generate Questions**: Click "Generate Questions" to create practice questions
6. **Review**: Use the Flashcards and Questions tabs to review your learning materials

## Database

The app uses SQLite database (`lappen.db`) which is automatically created on first run. The database stores:
- Users
- Notes
- Flashcards
- Questions

## Notes

- Make sure Ollama is accessible from your server
- The Ollama URL should be accessible from where the Node.js server is running
- For production, use a strong JWT_SECRET
- Consider using HTTPS in production

