# 🎮 Tic Tac Toe – Python + NumPy  

## 📝 Overview  
This project is a fully functional **Tic Tac Toe** game (X-O) built in **Python** using **NumPy** to handle the game board as a 3×3 array. It demonstrates how to structure game logic, take user input, and check winning conditions in real time.  

The code was designed to be simple, clean, and easy to extend. It currently supports **player vs. player** mode on the console and shows how to implement a full game loop with minimal code.  

---

## 🗂 Features  
- **Game Board Setup:** Uses a 3×3 NumPy array filled with blank spaces to represent the board.  
- **Player Turns:** Tracks which player’s turn it is (`X` or `O`) and switches automatically after each valid move.  
- **Winner Check:** Implements a function to check rows, columns, and diagonals for winning conditions.  
- **Draw Detection:** Declares a draw if the board is full and no winner is found.  
- **Console Display:** Prints the board state in a clean, easy-to-read format after each move.  

---

## 📜 Game Rules  
1. Two players take turns placing their symbols (`X` or `O`) on an empty cell.  
2. The goal is to form a line of three symbols horizontally, vertically, or diagonally.  
3. The first player to form a line wins the game.  
4. If all cells are filled with no winner, the game ends in a draw.  

---

## ⚙️ How It Works  
- **`board`**: NumPy array holding the game state.  
- **`turn`**: Tracks the current player (`X` or `O`).  
- **`show_board()`**: Prints the board to the console.  
- **`winner()`**: Checks whether the current player has won.  
- **Game Loop**: Keeps asking for moves until there’s a winner or a draw.  

---

## ▶️ How to Run  
1. Make sure you have **Python 3.x** and **NumPy** installed.  
2. Save the code to a file, e.g., `tic_tac_toe.py`.  
3. Run the file:  
   ```bash
   python tic_tac_toe.py

.

📝 Future Enhancements
AI Opponent: Add a simple algorithm to allow the computer to play against a human.

Improved UI: Use a graphical interface (e.g., Tkinter or Pygame) for a richer user experience.

Input Validation: Enhance error handling for invalid inputs.

📚 Learning Outcomes
Using NumPy arrays for game state management.

Building a game loop and validating user input.

Checking winning conditions with array operations.

Understanding the fundamentals of Python’s control flow.


**“Developed by Basel Felemban”**
