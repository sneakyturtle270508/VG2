const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const cors = require('cors');
const axios = require('axios');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key-change-this';
const OLLAMA_URL = process.env.OLLAMA_URL || 'http://localhost:11434';
const OLLAMA_MODEL = process.env.OLLAMA_MODEL || 'llama3.2';

app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Initialize database
const db = new sqlite3.Database('./lappen.db');

// Create tables
db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  )`);

  db.run(`CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
  )`);

  db.run(`CREATE TABLE IF NOT EXISTS flashcards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    note_id INTEGER,
    front TEXT NOT NULL,
    back TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (note_id) REFERENCES notes(id)
  )`);

  db.run(`CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    note_id INTEGER,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (note_id) REFERENCES notes(id)
  )`);
});

// Middleware to verify JWT token
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({ error: 'Access token required' });
  }

  jwt.verify(token, JWT_SECRET, (err, user) => {
    if (err) {
      return res.status(403).json({ error: 'Invalid or expired token' });
    }
    req.user = user;
    next();
  });
};

// Helper function to call Ollama
async function callOllama(prompt, systemPrompt = '') {
  try {
    const response = await axios.post(`${OLLAMA_URL}/api/generate`, {
      model: 'llama3.2',
      prompt: systemPrompt ? `${systemPrompt}\n\n${prompt}` : prompt,
      stream: false
    });
    return response.data.response;
  } catch (error) {
    console.error('Ollama error:', error.message);
    throw new Error('Failed to connect to Ollama. Make sure Ollama is running and the model is available.');
  }
}

// Auth routes
app.post('/api/register', async (req, res) => {
  const { username, password } = req.body;

  if (!username || !password) {
    return res.status(400).json({ error: 'Username and password required' });
  }

  try {
    const hashedPassword = await bcrypt.hash(password, 10);
    
    db.run('INSERT INTO users (username, password) VALUES (?, ?)', 
      [username, hashedPassword], 
      function(err) {
        if (err) {
          if (err.message.includes('UNIQUE constraint')) {
            return res.status(400).json({ error: 'Username already exists' });
          }
          return res.status(500).json({ error: 'Database error' });
        }

        const token = jwt.sign({ id: this.lastID, username }, JWT_SECRET);
        res.json({ token, user: { id: this.lastID, username } });
      }
    );
  } catch (error) {
    res.status(500).json({ error: 'Server error' });
  }
});

app.post('/api/login', (req, res) => {
  const { username, password } = req.body;

  if (!username || !password) {
    return res.status(400).json({ error: 'Username and password required' });
  }

  db.get('SELECT * FROM users WHERE username = ?', [username], async (err, user) => {
    if (err) {
      return res.status(500).json({ error: 'Database error' });
    }

    if (!user) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const validPassword = await bcrypt.compare(password, user.password);
    if (!validPassword) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const token = jwt.sign({ id: user.id, username: user.username }, JWT_SECRET);
    res.json({ token, user: { id: user.id, username: user.username } });
  });
});

// Notes routes
app.get('/api/notes', authenticateToken, (req, res) => {
  db.all('SELECT * FROM notes WHERE user_id = ? ORDER BY updated_at DESC', 
    [req.user.id], 
    (err, notes) => {
      if (err) {
        return res.status(500).json({ error: 'Database error' });
      }
      res.json(notes);
    }
  );
});

app.post('/api/notes', authenticateToken, (req, res) => {
  const { content } = req.body;

  if (!content) {
    return res.status(400).json({ error: 'Content required' });
  }

  db.run('INSERT INTO notes (user_id, content) VALUES (?, ?)', 
    [req.user.id, content], 
    function(err) {
      if (err) {
        return res.status(500).json({ error: 'Database error' });
      }
      res.json({ id: this.lastID, user_id: req.user.id, content, created_at: new Date().toISOString(), updated_at: new Date().toISOString() });
    }
  );
});

app.put('/api/notes/:id', authenticateToken, (req, res) => {
  const { content } = req.body;
  const noteId = req.params.id;

  if (!content) {
    return res.status(400).json({ error: 'Content required' });
  }

  db.run('UPDATE notes SET content = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ? AND user_id = ?', 
    [content, noteId, req.user.id], 
    function(err) {
      if (err) {
        return res.status(500).json({ error: 'Database error' });
      }
      if (this.changes === 0) {
        return res.status(404).json({ error: 'Note not found' });
      }
      res.json({ success: true });
    }
  );
});

app.delete('/api/notes/:id', authenticateToken, (req, res) => {
  const noteId = req.params.id;

  db.run('DELETE FROM notes WHERE id = ? AND user_id = ?', 
    [noteId, req.user.id], 
    function(err) {
      if (err) {
        return res.status(500).json({ error: 'Database error' });
      }
      if (this.changes === 0) {
        return res.status(404).json({ error: 'Note not found' });
      }
      res.json({ success: true });
    }
  );
});

// Generate flashcards from note
app.post('/api/notes/:id/flashcards', authenticateToken, async (req, res) => {
  const noteId = req.params.id;

  db.get('SELECT * FROM notes WHERE id = ? AND user_id = ?', 
    [noteId, req.user.id], 
    async (err, note) => {
      if (err) {
        return res.status(500).json({ error: 'Database error' });
      }
      if (!note) {
        return res.status(404).json({ error: 'Note not found' });
      }

      try {
        const systemPrompt = 'You are a helpful assistant that creates educational flashcards. Generate flashcards in JSON format: [{"front": "question", "back": "answer"}, ...]. Only return the JSON array, no other text.';
        const prompt = `Create flashcards from the following notes about car theory:\n\n${note.content}\n\nGenerate 5-10 flashcards that help with learning.`;
        
        const response = await callOllama(prompt, systemPrompt);
        
        // Try to extract JSON from response
        let flashcards;
        try {
          const jsonMatch = response.match(/\[[\s\S]*\]/);
          if (jsonMatch) {
            flashcards = JSON.parse(jsonMatch[0]);
          } else {
            throw new Error('No JSON found');
          }
        } catch (parseError) {
          // Fallback: create simple flashcards
          const lines = note.content.split('\n').filter(l => l.trim());
          flashcards = lines.slice(0, 5).map((line, i) => ({
            front: `Question ${i + 1}`,
            back: line.trim()
          }));
        }

        // Save flashcards to database
        const stmt = db.prepare('INSERT INTO flashcards (user_id, note_id, front, back) VALUES (?, ?, ?, ?)');
        flashcards.forEach(flashcard => {
          stmt.run([req.user.id, noteId, flashcard.front, flashcard.back]);
        });
        stmt.finalize();

        res.json({ flashcards, count: flashcards.length });
      } catch (error) {
        res.status(500).json({ error: error.message });
      }
    }
  );
});

// Generate questions from note
app.post('/api/notes/:id/questions', authenticateToken, async (req, res) => {
  const noteId = req.params.id;

  db.get('SELECT * FROM notes WHERE id = ? AND user_id = ?', 
    [noteId, req.user.id], 
    async (err, note) => {
      if (err) {
        return res.status(500).json({ error: 'Database error' });
      }
      if (!note) {
        return res.status(404).json({ error: 'Note not found' });
      }

      try {
        const systemPrompt = 'You are a helpful assistant that creates educational questions. Generate questions in JSON format: [{"question": "question text", "answer": "answer text"}, ...]. Only return the JSON array, no other text.';
        const prompt = `Create practice questions from the following notes about car theory:\n\n${note.content}\n\nGenerate 5-10 questions that test understanding.`;
        
        const response = await callOllama(prompt, systemPrompt);
        
        // Try to extract JSON from response
        let questions;
        try {
          const jsonMatch = response.match(/\[[\s\S]*\]/);
          if (jsonMatch) {
            questions = JSON.parse(jsonMatch[0]);
          } else {
            throw new Error('No JSON found');
          }
        } catch (parseError) {
          // Fallback: create simple questions
          const lines = note.content.split('\n').filter(l => l.trim());
          questions = lines.slice(0, 5).map((line, i) => ({
            question: `What is ${line.split(' ').slice(0, 3).join(' ')}?`,
            answer: line.trim()
          }));
        }

        // Save questions to database
        const stmt = db.prepare('INSERT INTO questions (user_id, note_id, question, answer) VALUES (?, ?, ?, ?)');
        questions.forEach(q => {
          stmt.run([req.user.id, noteId, q.question, q.answer]);
        });
        stmt.finalize();

        res.json({ questions, count: questions.length });
      } catch (error) {
        res.status(500).json({ error: error.message });
      }
    }
  );
});

// Get flashcards
app.get('/api/flashcards', authenticateToken, (req, res) => {
  db.all('SELECT * FROM flashcards WHERE user_id = ? ORDER BY created_at DESC', 
    [req.user.id], 
    (err, flashcards) => {
      if (err) {
        return res.status(500).json({ error: 'Database error' });
      }
      res.json(flashcards);
    }
  );
});

// Get questions
app.get('/api/questions', authenticateToken, (req, res) => {
  db.all('SELECT * FROM questions WHERE user_id = ? ORDER BY created_at DESC', 
    [req.user.id], 
    (err, questions) => {
      if (err) {
        return res.status(500).json({ error: 'Database error' });
      }
      res.json(questions);
    }
  );
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log(`Ollama URL: ${OLLAMA_URL}`);
});

