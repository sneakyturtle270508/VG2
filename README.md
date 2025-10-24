# My_python_journey

A collection of Python exercises and projects from my programming course, showcasing fundamental programming concepts and problem-solving skills.

**Author:** William Berge Groensberg  
**Course:** Python Programming Fundamentals

---

## 📁 Project Structure

```
📦 Python-School-Projects
├── 01-ovelser/           # Basic exercises and concepts
├── 02-oppgaver/          # Core assignments
├── 03-ekstraoppgaver/    # Extra challenges and games
└── 04-egen_ovelse/       # Self-practice and advanced projects
```

---

## 🎯 Learning Objectives

This repository demonstrates proficiency in:

- **Variables and Data Types** - Working with strings, integers, floats, lists, and dictionaries
- **User Input/Output** - Interactive programs with `input()` and `print()`
- **Conditional Logic** - `if`, `elif`, `else` statements and complex decision trees
- **Type Conversion** - Converting between different data types
- **Loops** - `for` and `while` loops for repetitive tasks and game mechanics
- **Random Numbers** - Using the `random` module for games and simulations
- **Functions** - Creating reusable code blocks and modular programming
- **Data Structures** - Working with lists, sets, and dictionaries
- **ASCII Art** - Creating visual representations and enhanced user interfaces
- **Game Development** - Complete interactive games with win conditions
- **Algorithm Design** - Implementing game logic and win detection systems

---

## 📚 Project Highlights

### 🔄 **01-ovelser** - Foundation Exercises
- **Hello World** (`hello.py`) - First Python program with variables and output
- **If Statements** (`if-setninger.py`) - Age verification with conditional logic
- **User Input** (`bruker-input.py`) - Interactive age checking program
- **Type Conversion** (`konvertering.py`) - Converting between strings, integers, and floats
- **Increment Operations** (`inkrement.py`) - Variable manipulation and increment operators
- **Loops** (`for_loop.py`, `while_loop.py`) - Mastering repetitive operations
- **Mathematical Operations** (`pseudokode_regning.py`) - Arithmetic and operator precedence

### 📋 **02-oppgaver** - Core Assignments
- **Cup Swap** (`kopp.py`) - Variable swapping algorithm with temporary storage
- **Age Comparison** (`opg.py`) - Compare ages of two people (Henrik and Kari)
- **Interactive Quiz** (`opg.py`) - 10-question quiz with scoring system and feedback
- **Multiplication Tables** (`opg_for_loops.py`) - Dynamic table generation using loops
- **Number Guessing Game** (`opg.py`) - Random number guessing with hints and attempt tracking
- **Currency Exchange** (`opg.py`) - Bill denomination calculator using modulo operations

### 🎮 **03-ekstraoppgaver** - Interactive Games & Challenges
- **Math Quiz Game** (`OPG.PY`) - 10-question multiplication quiz with scoring system
- **Dice Roll Challenge** (`terning.py`) - Keep rolling until you get a 6
- **Double Dice Game** (`opg.py`) - Roll two dice until you get matching numbers
- **Yatzy Challenge** (`opg.py`) - Roll 5 dice until all show the same number
  - Includes enhanced version with ASCII art dice visualization
  - Statistical analysis version for probability calculations

### 🧪 **04-egen_ovelse** - Advanced Self-Practice
- **🎯 Tic Tac Toe** (`ticTacToe.py`) - Complete two-player game with win detection
- **🃏 Blackjack** (`blackjack.py`) - Card game with ASCII art and proper Ace handling
- **Data Types Reference** (`cheatsheet.py`) - Comprehensive Python syntax guide

---

## 🎲 Featured Projects

### 🃏 Blackjack Card Game
A fully functional Blackjack game with professional features:
- **Complete 52-card deck** with proper shuffling
- **Beautiful ASCII art cards** with suits (♠ ♥ ♦ ♣)
- **Smart Ace handling** - automatically adjusts between 1 and 11
- **Realistic card values** - Face cards worth 10, Aces flexible
- **Interactive gameplay** - Hit or Stand decisions
- **Bust detection** - Automatic game over when exceeding 21
- **Visual hand display** - See your cards laid out beautifully

```python
# Example card display
┌───────┐  ┌───────┐
|K♠     |  |A♥     |
|   ♠   |  |   ♥   |
|     ♠K|  |     ♥A|
└───────┘  └───────┘

Total verdi: 21
```

### 🎯 Tic Tac Toe Strategy Game
Strategic two-player Tic Tac Toe with advanced features:
- **Dynamic game board** - Visual 3x3 grid with clear position markers
- **Win detection system** - Checks all 8 possible winning combinations
- **Input validation** - Prevents invalid moves and overwrites
- **Turn management** - Alternates between Player 1 (X) and Player 2 (O)
- **Real-time tracking** - Shows each player's chosen positions
- **Smart data structures** - Uses sets for efficient win condition checking

```python
# Game board display
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9

Spiller 1: [1, 5]
Spiller 2: [2, 3]
```

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd python-school-projects
   ```

2. **Run any program:**
   ```bash
   python path/to/file.py
   ```

3. **Featured Games:**
   ```bash
   # Play Blackjack
   python "04-egen_ovelse/02-Blackjack/blackjack.py"
   
   # Play Tic Tac Toe
   python "04-egen_ovelse/01-tic-tac-toe/ticTacToe.py"
   ```

---

## 💡 Programming Concepts Demonstrated

| Concept | Files | Description |
|---------|--------|-------------|
| **Variables & Assignment** | `hello.py`, `kopp.py` | Basic variable creation and manipulation |
| **User Input & Validation** | Most files | Interactive programs with input validation |
| **Conditionals** | `if-setninger.py`, games | Decision making with complex logic |
| **Loops** | `for_loop.py`, `while_loop.py` | For loops, while loops, and game loops |
| **Functions** | `blackjack.py` | Modular programming and code reuse |
| **Data Structures** | `ticTacToe.py` | Lists, sets, and dictionaries |
| **Random Numbers** | Games in `03-ekstraoppgaver/` | Using `random` module for gameplay |
| **Type Conversion** | `konvertering.py` | Converting between data types |
| **String Formatting** | All games | F-strings and string manipulation |
| **ASCII Art** | `blackjack.py`, `nam.py` | Visual programming and user interfaces |
| **Algorithm Design** | `ticTacToe.py` | Win detection and game state management |

---

## 🏆 Skills Developed

- **Problem Solving** - Breaking down complex problems into smaller, manageable steps
- **Algorithm Design** - Creating efficient win detection and game logic systems
- **Code Organization** - Using functions and modular programming principles
- **User Experience** - Creating engaging, visually appealing interactive programs
- **Data Structure Mastery** - Efficient use of lists, sets, and dictionaries
- **Input Validation** - Robust error handling and user input verification
- **Game Development** - Complete game loops, state management, and player interaction
- **Documentation** - Writing clear comments and comprehensive pseudocode
- **Testing & Debugging** - Systematic approach to finding and fixing issues

---

## 📝 Code Style & Comments

All code includes:
- **Norwegian comments** - Written in native language for better understanding
- **Detailed pseudocode** - Planning phase visible in `.txt` files
- **Clear variable names** - Self-documenting code with meaningful identifiers
- **Consistent formatting** - Professional code structure and indentation
- **Modular design** - Functions and organized code blocks
- **Error handling** - Input validation and edge case management

---

## 🎓 Course Progress

This repository represents my journey learning Python programming, from basic "Hello World" to sophisticated games like Blackjack and Tic Tac Toe. Each project builds upon previous concepts while introducing advanced programming techniques like:

- **Object-oriented thinking** through card and game representations
- **Algorithm implementation** for win detection and game logic
- **User interface design** with ASCII art and interactive elements
- **Data structure optimization** for efficient game state management

The progression shows mastery of fundamental concepts and readiness for advanced programming challenges.

---

## 📞 Contact

**William Berge Groensberg**  
Feel free to explore the code and see my progression from basic Python concepts to complete interactive games! 🚀