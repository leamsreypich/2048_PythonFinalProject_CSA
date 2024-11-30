# 2048_PythonFinalProject_CSA
---

---

## Project Issue / Problem to Be Solved

The goal of this project is to implement a 2048 game with a persistent high score system. The game needs to store the highest score a player achieves and provide functionality for playing the game with smooth animations and responsive design. The challenge is to ensure that the game mechanics, including tile movements, merges, and game-over detection, function correctly, while integrating a backend database to save and retrieve high scores.

---

## Current Progress (PDLC: Problem Analysis, Design, etc.)

### Problem Analysis:
- Identified the need for a game that tracks the highest score over multiple sessions.
- Needed to optimize the tile merging mechanics and add smooth animations for a better user experience.

### Design:
- Designed a 4x4 grid to represent the game board.
- Decided on the use of arrow keys to control tile movements.
- Database schema for storing the highest score was planned.

### Implementation:
- Developed the basic game logic (tile movement, merging, game-over conditions).
- Implemented front-end (HTML/CSS) for displaying the game and handling user input.
- Built the back-end (using a simple database) to store the highest score.

---

## Project Functions / Features

- **Save Data**: The game stores the highest score achieved in a database.
- **Search**: The game can retrieve the highest score from the database.
- **Delete**: The user can reset the game and remove the current high score.
- **Update**: The game updates the highest score whenever a new record is achieved.
- **Tile Movement and Merging**: Tiles move smoothly in any direction (left, right, up, down), merging when necessary.
- **Game Over**: The game detects when no further moves or merges are possible, triggering a game-over state.

---

## Expected Number of Pages

1. **Home Page**: The main game interface where the player can play the game.
2. **Game Over Page**: A page that displays the final score and asks the player to start a new game or view the high score.
3. **High Score Page**: A page displaying the highest score stored in the database.

---

## Database Applied

The project uses a simple database to store the highest score. The database consists of the following:

- **Players Table**:
  - `player_id` (VARCHAR): A unique identifier for the player.
  - `highest_score` (INT): The highest score achieved by the player.
  
The game retrieves and updates the highest score from this table whenever the player finishes a game.

---

## Project Reference / Source

- YouTube tutorial: [Make 2048 In Python | Full Python Game Tutorial](https://youtu.be/6ZyylFcjfIg?si=98Yc8nJhN8P-MX-8) YT Channel: Tech With Tim
- Code reference: [2048-In-Python] (https://github.com/techwithtim/2048-In-Python) by Tim Ruscica.

---

