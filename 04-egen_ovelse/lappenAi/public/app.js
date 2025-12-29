const API_URL = window.location.origin;

let currentUser = null;
let currentNoteId = null;
let authToken = null;

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    authToken = localStorage.getItem('token');
    if (authToken) {
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
    document.getElementById('notes-view').classList.remove('active');
    document.getElementById('note-editor').classList.add('active');
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
            document.getElementById('notes-view').classList.remove('active');
            document.getElementById('note-editor').classList.add('active');
        }
    });
}

function closeEditor() {
    document.getElementById('note-editor').classList.remove('active');
    document.getElementById('notes-view').classList.add('active');
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
        } else {
            alert(data.error || 'Failed to generate flashcards');
        }
    } catch (error) {
        alert('Error generating flashcards. Make sure Ollama is running.');
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
        } else {
            alert(data.error || 'Failed to generate questions');
        }
    } catch (error) {
        alert('Error generating questions. Make sure Ollama is running.');
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
    document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
    document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById(`${viewName}-view`).classList.add('active');
    document.querySelector(`[data-view="${viewName}"]`).classList.add('active');
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

