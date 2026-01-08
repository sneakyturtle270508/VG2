# Quick Setup Guide

## Step 1: Create .env file

Create a file named `.env` in the project root with this content:

```
PORT=3000
JWT_SECRET=local-dev-secret-key-change-in-production
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

## Step 2: Install Dependencies (if not done)

```bash
npm install
```

## Step 3: Ollama Setup (Optional but Recommended)

### Option A: Install Ollama for AI Features

1. **Download Ollama:**
   - Visit https://ollama.ai
   - Download and install Ollama for Windows

2. **Pull a model:**
   ```bash
   ollama pull llama3.2
   ```
   Or use a smaller/faster model:
   ```bash
   ollama pull llama3.1
   ollama pull mistral
   ```

3. **Start Ollama:**
   - Ollama usually runs automatically after installation
   - Or start it manually from the Start menu

4. **Verify it's working:**
   ```bash
   ollama list
   ```

### Option B: Use Without Ollama

The app will work without Ollama! It will use a simple fallback method to generate flashcards and questions from your notes. The AI-generated ones will be smarter, but the fallback works fine for basic learning.

## Step 4: Start the Server

```bash
npm start
```

You should see:
```
Server running on port 3000
Ollama URL: http://localhost:11434
Ollama Model: llama3.2
✓ Ollama is available
```
or
```
⚠ Ollama is not available - AI features will use fallback mode
```

## Step 5: Open in Browser

Go to: http://localhost:3000

## Troubleshooting

### If Ollama is not found:
- Make sure Ollama is installed
- Check if it's running (look for Ollama in your system tray)
- Try restarting your computer after installing Ollama

### If you get connection errors:
- Check that `OLLAMA_URL` in `.env` matches where Ollama is running
- Default is `http://localhost:11434`
- If Ollama is on another computer, use that computer's IP address

### The app still works!
Even if Ollama isn't working, you can:
- ✅ Create and save notes
- ✅ Generate flashcards (using fallback method)
- ✅ Generate questions (using fallback method)
- ✅ Review your learning materials

The fallback method splits your notes into flashcards/questions automatically.

