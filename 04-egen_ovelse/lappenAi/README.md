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
- `OLLAMA_MODEL`: Model name to use (default: llama3.2)

3. Make sure Ollama is running and has the model installed:
```bash
# Install Ollama if you haven't already
# Visit https://ollama.ai for installation instructions

# Pull the model (you can use any model you prefer)
ollama pull llama3.2

# Or use a different model like:
# ollama pull llama3.1
# ollama pull mistral
# etc.
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

## Troubleshooting

### Ollama Connection Issues

If you get errors when generating flashcards or questions:

1. **Check if Ollama is running:**
   ```bash
   # On Windows/Mac/Linux
   ollama list
   ```
   If this command works, Ollama is running.

2. **Verify the model is installed:**
   ```bash
   ollama list
   ```
   Make sure your model (e.g., `llama3.2`) appears in the list.

3. **Test Ollama connection:**
   ```bash
   curl http://localhost:11434/api/tags
   ```
   This should return a list of available models.

4. **Check your `.env` file:**
   - Make sure `OLLAMA_URL` matches where Ollama is running
   - If Ollama is on a different machine, use the full URL: `http://your-server-ip:11434`
   - Make sure `OLLAMA_MODEL` matches a model you have installed

5. **Fallback Mode:**
   - If Ollama is not available, the app will use a simple fallback method to generate flashcards/questions
   - This works but won't be as smart as AI-generated content

### Common Errors

- **"Cannot connect to Ollama"**: Ollama is not running or URL is incorrect
- **"Model not found"**: The model name in `.env` doesn't match an installed model
- **"Timeout"**: Ollama is taking too long to respond (check if model is too large for your system)

## Notes

- Make sure Ollama is accessible from your server
- The Ollama URL should be accessible from where the Node.js server is running
- For production, use a strong JWT_SECRET
- Consider using HTTPS in production
- The app includes fallback generation if Ollama is unavailable, so basic functionality will still work

