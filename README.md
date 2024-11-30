# 2048_PythonFinalProject_CSA
---
## Instruction on how to run the code application :




---

## Project Issue 

This project aims to recreate the popular "2048" game with an interactive interface, scoring mechanism, and custom features like animations and sound effects. The game needs to store the highest score of a player and provide functionality for playing the game with smooth animations and responsive design. The challenge is to ensure that the game mechanics, including tile movements, merges, and game-over detection, function correctly, while including a database to save and retrieve the highest score of the player.

---

## Current Progress 

### Problem Analysis:
- Understanding the mechanics of the original 2048 game.
- Identifying requirements like grid size, tile mechanics, and scoring, etc.

### Design:
- Designed a 4x4 grid to represent the game board.
- Designed a GUI using Pygame with animations and color-coded tiles.
  
### Implementation:
- Core game logic: Tile movement, tile merging, random tile generation, game-over conditions .
- User interface: Start screen, game screen, and game-over screen.
- Sound effects and music integration.
- Built a simple database to store and retrieve the highest score of the player.
  
### Testing:
- Functional testing of tile movement and scoring.
- Validated database interactions for high scores.

### Future Steps:
- Optimization of game mechanics.
- Adding advanced animations and additional modes/levels for the game.
- Implementing a more advanced database that allows players to input their usernames and compete with each other.

---

## Project Functions / Features

### Core Features:
- Move tiles in all four directions (Up, Down, Left, Right).
- Merge tiles with the same value to create higher numbers.
- Random tile generation with values 2 or 4.
- Game-over detection based on tile positions.

### Additional Features:
- Save the highest score in a local database.
- Display "Game Over" and retry option.
- Animated start screen and loading effects.
- Background music and sound effects.

---

## Expected Pages

1.**Home Page**: Start screen with "Start" button.
2.**Game Screen**: Main 2048 grid and gameplay.
3.**Game Over Screen**: Displays current and highest scores with a retry button.

---

## Database Applied
The project uses a simple database to store the highest score. 
- Type: SQLite (local database).
- High Scores Table: Stores the highest score for the player.
- Records: Tracks the maximum tile value that the player had reached.

---

## Project Reference / Source

- YouTube tutorial: [Make 2048 In Python | Full Python Game Tutorial](https://youtu.be/6ZyylFcjfIg?si=98Yc8nJhN8P-MX-8) YT Channel: Tech With Tim
- Code reference: [2048-In-Python] (https://github.com/techwithtim/2048-In-Python) by Tim Ruscica.

---

