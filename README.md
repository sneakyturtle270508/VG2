# VG2 IT - Python Programming Portfolio

A comprehensive collection of Python exercises and projects from my programming course, showcasing progression from fundamental concepts to advanced applications including games, networking, and automation.

**Author:** William Berge Groensberg  
**Course:** Programming (VG2) 

---

## Project Structure

```
VG2-IT-Python-Projects
├── 02-oppgaver/              # Core curriculum assignments (9 projects)
├── 03-ekstraoppgaver/        # Extra challenges and games (8 projects)
├── 04-egen_ovelse/           # Self-practice and advanced projects (8 projects)
└── README.md                 # This file
```

---

## Learning Objectives

This repository demonstrates comprehensive proficiency in:

### Core Programming Concepts
- **Variables and Data Types** - Strings, integers, floats, lists, dictionaries, sets
- **User Input/Output** - Interactive programs with validation and error handling
- **Conditional Logic** - Complex decision trees with if/elif/else statements
- **Type Conversion** - Dynamic type handling and casting
- **Loops** - For loops, while loops, nested iterations, and break/continue
- **Functions** - Modular programming with parameters and return values
- **File Operations** - Reading/writing files, CSV parsing, file monitoring

### Advanced Topics
- **Data Structures** - Lists, dictionaries, sets, tuples for efficient data management
- **Algorithm Design** - Sorting, searching, optimization, game logic
- **Database Management** - Relational databases, table design, normalization
- **Network Programming** - Client-server architecture, UDP broadcasting, TCP connections
- **Threading** - Concurrent operations for real-time applications
- **Game Development** - Complete game loops, state management, AI opponents
- **ASCII Art** - Visual programming and enhanced user interfaces
- **Random Numbers** - Probability, simulations, and procedural generation
- **Mathematical Operations** - Formulas, calculations, statistical analysis
- **Automation** - File organization, monitoring systems, scheduled tasks

---

## Detailed Project Overview

### **02-oppgaver** - Core Curriculum (10 Projects)

#### 1. **Cup Swap** (`01 - Bytt kopper/`)
Variables and value swapping using temporary storage
```python
blakopp = "bla_tusj"
rodkopp = "rod_tusj"
# Swap using temporary variable
```

#### 2. **Age Comparison** (`02-hvem-er-eldst/`)
Conditional logic comparing two people's ages
- User input validation
- If/elif/else decision making
- Clear output formatting

#### 3. **Interactive Quiz** (`03-quiz/`)
10-question quiz system with scoring
- Input validation
- Score tracking
- Multiple implementations (basic and enhanced with ASCII boxes)
- Feedback system

#### 4. **Multiplication Tables** (`04-Gangetabell/`)
Dynamic multiplication table generator
- For loop implementation
- User-defined ranges
- Formatted output display

#### 5. **Number Guessing Game** (`05-tippespill/`)
Random number guessing with hints
- Random number generation
- While loop implementation
- Attempt counter
- Two versions: with and without True in condition

#### 6. **Currency Exchange** (`06-veksleren/`)
Bill denomination calculator using dictionaries
- Modulo operations for change calculation
- Dictionary data structure
- Efficient denomination breakdown

#### 7. **Box Volume Optimizer** (`07-volum_paa_eske/`)
Mathematical optimization problem
- Function creation
- While loop optimization
- Formula implementation (volume calculation)
- Finding maximum value through iteration

#### 8. **Order Management** (`08-bestillinger-med-lister/`)
Weekly order tracking system
- List operations (append, index, max)
- Statistical calculations (sum, average)
- Data analysis and reporting
- Multiple list manipulation

#### 9. **Database Management** (Access DB)
Employee database system using Microsoft Access
- Table design with multiple data types
- Fields: ansattID, fornavn, etternavn, dato_startet, loensnivaa
- Primary key implementation
- Data entry and validation
- Query design and filtering
- Relational database concepts
- Database normalization principles

**Skills Demonstrated:**
- SQL fundamentals
- Database schema design
- Data types (AutoNumber, Text, Date, Currency)
- Table relationships
- Query creation

---

### **03-ekstraoppgaver** - Extra Challenges (8 Projects)

#### 1. **Math Quiz Game** (`01-Ekstra/`)
Interactive multiplication quiz
- 10 random multiplication problems
- Score tracking
- Time delays for better UX
- Performance feedback based on score

#### 2. **Dice Roll Challenge** (`02-Ekstra/`)
Keep rolling until you get a 6
- Random dice simulation
- Attempt counting
- User interaction (press Enter)

#### 3. **Double Dice Game** (`03-Ekstra/`)
Roll two dice until matching numbers
- Multiple random variables
- Comparison logic
- Visual feedback

#### 4. **Yatzy Challenge** (`04-Ekstra/`)
Roll 5 dice until all match
- **Three versions:**
  1. Basic version with attempt counter
  2. Enhanced with ASCII art dice visualization
  3. Statistical probability calculator version
- Advanced comparison logic (5-way equality)

#### 5. **Party Planner** (`05-Ekstra/`)
Calculate hot dogs and buns needed
- Mathematical calculations
- `math.ceil()` for rounding up
- Practical problem solving

#### 6. **Geometry Calculator** (`07-Ekstra/`)
Calculate areas of various shapes
- Functions for each shape
- Circle calculations with `math.pi`
- Multiple return values
- Formulas: square, rectangle, triangle, parallelogram, rhombus, trapezoid, circle

#### 7. **Pixel Art Creator** (`08-Exstra/`)
Create pixel art using turtle graphics
- Turtle graphics library
- Coordinate system
- Color management
- Pattern creation

---

### **04-egen_ovelse** - Advanced Self-Practice (8 Projects)

#### 1. **Tic Tac Toe** (`01-tic-tac-toe/`)
Complete two-player strategy game
- Dynamic 3x3 game board
- Win detection (8 possible combinations)
- Input validation and illegal move prevention
- Turn management system
- Set-based win condition checking
- Real-time position tracking

```python
# Game board display
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

#### 2. **Blackjack** (`02-Blackjack/`)
Professional casino card game
- Complete 52-card deck implementation
- Beautiful ASCII art cards with suits (♠ ♥ ♦ ♣)
- Smart Ace handling (1 or 11)
- Realistic card values
- Dealer AI with strategy
- Flip animation for dealer's hidden card
- Virtual money system with betting
- Hit/Stand mechanics

```python
┌───────┐  ┌───────┐
|K♠     |  |A♥     |
|   ♠   |  |   ♥   |
|     ♠K|  |     ♥A|
└───────┘  └───────┘
Total: 21 - BLACKJACK!
```

#### 3. **LAN Chat System** (`03-chat-system/`)
Advanced networked chat application
- **Server Features:**
  - UDP broadcast for automatic discovery
  - TCP connections for chat
  - Room-based chat with PIN codes
  - Server administration dashboard
  - User kick/ban capabilities
  - Activity logging
  - Server states (active/standby/stopped)
- **Client Features:**
  - Automatic server discovery
  - Multiple server selection
  - Reconnection handling
  - Clean disconnect
- Complete documentation included

#### 4. **Even Number Checker** (`04-sjekke-partall/`)
Simple modulo operation example
- Input validation
- Modulo arithmetic (% 2)
- Even/odd determination

#### 5. **Number System Converter** (`05-hex-to-bin/`)
Multi-format number converter
- 6 conversion modes:
  1. Binary → Hexadecimal
  2. Hexadecimal → Binary
  3. Integer → Binary
  4. Binary → Integer
  5. Integer → Hexadecimal
  6. Hexadecimal → Integer
- Menu-driven interface
- Input validation

#### 6. **Smart File Organizer** (`06-fil-sorterer/`)
Automated file organization system
- Automatic course folder detection
- File monitoring with `watchdog` library
- Date-based file numbering
- Dynamic reorganization
- Prevents conflicts during editing
- Course name extraction from filenames
- Real-time file system monitoring

#### 7. **Matrix Effect** (`07-matrix/`)
Classic Matrix digital rain effect
- Random character generation
- Terminal color formatting
- Continuous animation loop
- Visual programming demonstration

#### 8. **CSV to ICS Converter** (`08-csv-to-ice/`)
School schedule converter
- CSV parsing
- ICS (iCalendar) format generation
- Date/time formatting
- Multi-event handling
- Import into calendar applications

---

## Featured Advanced Projects

### LAN Chat System - Multi-User Networking
A production-ready chat system with enterprise features:

**Server Capabilities:**
- Automatic discovery via UDP broadcast
- Multi-room support with PIN-based access
- Real-time user management
- Administrative controls (kick, ban, close rooms)
- Activity logging with configurable history
- Three operational states: active, standby, stopped
- Thread-safe operations with locking mechanisms
- Graceful shutdown and cleanup

**Client Features:**
- Zero-configuration server discovery
- Multi-server support (choose from discovered servers)
- Automatic reconnection after network issues
- Clean disconnect with `/stop` command
- Real-time message delivery
- Connection status monitoring

**Technical Implementation:**
```python
# Server broadcasts presence
sock.sendto(b"SERVER_HERE", addr)

# Client discovers servers
data, addr = client.recvfrom(1024)
if data.decode("utf-8") == "SERVER_HERE":
    servers.append(addr[0])
```

### Smart File Organizer - Automation System
Intelligent file organization with real-time monitoring:

**Features:**
- Automatic course folder creation from filenames
- Date-based file numbering (oldest = 00)
- Real-time file system monitoring with `watchdog`
- Smart waiting to avoid conflicts during file creation
- Batch reorganization when old files are added
- Prefix extraction and cleanup
- Cross-platform compatibility

**Use Case:**
```
Input: "matte_oppgave.pdf" (created Sept 1)
       "matte_test.pdf" (created Sept 15)
       "matte_notater.pdf" (created Sept 5)

Output: matte/
        ├── 00_oppgave.pdf (Sept 1)
        ├── 01_notater.pdf (Sept 5)
        └── 02_test.pdf (Sept 15)
```

### Blackjack - Professional Game Development
Casino-quality card game with all features:

**Advanced Features:**
- Proper deck management with shuffling
- Visual card representations with Unicode suits
- Dealer flip animation (card reveal effect)
- Smart Ace logic (automatic 1/11 switching)
- Betting system with virtual currency
- Dealer AI following house rules
- Multiple game states (betting, playing, dealer turn, results)
- Clean game loop with replay option

---

## Programming Patterns & Best Practices

### Code Organization
```python
# Modular design with functions
def create_deck():
    """Generate and shuffle a 52-card deck"""
    suits = ['♠', '♥', '♦', '♣']
    values = ['2','3',...,'A']
    return [v + s for v in values for s in suits]

# Clear separation of concerns
# - Game logic in functions
# - Display logic separate
# - Input validation isolated
```

### Error Handling
```python
# Robust input validation
try:
    choice = int(input("Choose: "))
    if 1 <= choice <= 6:
        return choice
except ValueError:
    print("Invalid input!")
```

### Data Structures
```python
# Efficient win detection in Tic Tac Toe
winning_combo = [
    {1,2,3}, {4,5,6}, {7,8,9},  # Rows
    {1,4,7}, {2,5,8}, {3,6,9},  # Columns
    {1,5,9}, {3,5,7}            # Diagonals
]
# Check win with set operations
if any(combo.issubset(player1) for combo in winning_combo):
    return True
```

---

## How to Run

### Basic Programs
```bash
# Clone the repository
git clone <repository-url>
cd vg2-it-python

# Run any basic program
python "02-oppgaver/03-quiz/opg.py"
```

### Featured Games
```bash
# Play Blackjack (requires terminal with Unicode support)
python "04-egen_ovelse/02-Blackjack/blackjack.py"

# Play Tic Tac Toe
python "04-egen_ovelse/01-tic-tac-toe/ticTacToe.py"

# Run Yatzy with probability analysis
python "03-ekstraoppgaver/04-Ekstra/yatsi_med_sansynlighet.py"
```

### Advanced Projects
```bash
# Start LAN Chat Server
python "04-egen_ovelse/03-chat-system/server.py"

# Connect as client (in another terminal)
python "04-egen_ovelse/03-chat-system/client.py"

# Run file organizer (configure path first)
python "04-egen_ovelse/06-fil-sorterer/main.py"
```

---

## Skills Progression Map

| Level | Skills | Projects |
|-------|--------|----------|
| **Beginner** | Variables, I/O, Conditionals | Cup Swap, Age Comparison |
| **Intermediate** | Loops, Functions, Lists | Quiz, Guessing Game, Order Management |
| **Advanced** | Algorithms, Data Structures | Tic Tac Toe, Blackjack, Converters |
| **Expert** | Networking, Threading, Automation | Chat System, File Organizer |

---

## Concepts Mastered

### Fundamental Programming
- ✅ Variables and data types (all types)
- ✅ User input with validation
- ✅ Type conversion and casting
- ✅ Conditional statements (if/elif/else)
- ✅ Loops (for, while, nested)
- ✅ Functions with parameters and returns
- ✅ String manipulation and formatting

### Data Structures
- ✅ Lists (creation, indexing, methods)
- ✅ Dictionaries (key-value pairs)
- ✅ Sets (for unique collections)
- ✅ Tuples (immutable sequences)
- ✅ List comprehensions

### Advanced Techniques
- ✅ File I/O operations
- ✅ Random number generation
- ✅ Mathematical calculations
- ✅ Algorithm implementation
- ✅ Network programming (sockets, TCP/UDP)
- ✅ Multi-threading
- ✅ Event-driven programming
- ✅ File system monitoring
- ✅ ASCII art and visualization

### Software Engineering
- ✅ Modular code organization
- ✅ Error handling and validation
- ✅ Documentation and comments
- ✅ Code reusability
- ✅ Testing and debugging
- ✅ Version control awareness
- ✅ Database design and management
- ✅ SQL and relational databases

---

## Code Quality Standards

All projects demonstrate:

- **Norwegian Comments** - Native language for educational clarity
- **Pseudocode Planning** - Visible in `.txt` files showing thought process
- **Meaningful Names** - Self-documenting variable and function names
- **Consistent Style** - Professional formatting and indentation
- **Modular Design** - Functions and organized code blocks
- **Input Validation** - Robust error handling for user input
- **Teacher Feedback** - Inline comments showing instructor guidance
- **Progressive Complexity** - Each project builds on previous concepts

### Example Code Quality
```python
# Clear function with documentation
def hand_value(hand):
    """
    Calculate the optimal value of a blackjack hand.
    Handles Aces intelligently (1 or 11).
    """
    value = 0
    aces = 0
    
    for card in hand:
        # ... implementation
    
    return value
```

---

## Project Achievements

- **26+ Complete Programs** - From simple exercises to complex applications
- **3 Full Games** - Tic Tac Toe, Blackjack, Yatzy (with variants)
- **Network Application** - Complete client-server chat system
- **Database System** - Employee management with Access
- **Automation Tool** - Real-time file organization system
- **Multiple Algorithms** - Win detection, optimization, conversion
- **Professional UX** - ASCII art, animations, formatted output

---

## Future Enhancements

Potential areas for expansion:
- GUI versions using tkinter or pygame
- Database integration for persistent data
- Web interface for chat system
- AI opponents for games
- Additional file format converters
- Mobile app versions

---

## Contact & Acknowledgments

**William Berge Groensberg**  
VG2 Student - IT Technology and Services  
Telemark fylkeskommune

**Special Thanks:**
- Course instructors for detailed feedback
- ChatGPT for LAN chat system architecture assistance (documented in readme)
- Fellow students for testing and suggestions

---

## License & Usage

This is an educational portfolio. Code is available for learning purposes.  
Feel free to explore, learn from, and adapt these projects!

---

*Last Updated: October 2025*  
*Repository represents continuous learning from basic Python to advanced networking and automation*
