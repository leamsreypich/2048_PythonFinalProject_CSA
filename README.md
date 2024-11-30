# 2048_PythonFinalProject_CSA

## How to Run the Application: 
### Prerequisites
1. **Install Python**:
   - Ensure Python 3.8+ is installed. Download it [here](https://www.python.org/).

2. **Install Dependencies**:
   - Use the following command to install the required libraries:
     ```bash
     pip install pygame
     ```

3. **Required Files**:
   - Ensure the following files are in the project directory:
     - `2048game.py`
     - `database.py` 
     - Required assets:
       - `start_screen_background.jpg`
       - `sound_effect.wav`
       - `game_over_sound.wav`
       - `Backgroundmusic.mp3`
4. **Run the Game**
   - Run the `2048game.py` file to play the game
     
---

## How to Play
1. **Objective**:  
   Combine tiles with the same number to create a tile with the value `2048` (or as high as possible).
   
2. **Gameplay**:  
   - Use the arrow keys (`↑`, `↓`, `←`, `→`) to move the tiles on the grid.
   - Tiles with the same number merge into one tile when they collide.
   - After every move, a new tile (2 or 4) appears randomly on the grid.
   - The game ends when no moves are possible.

3. **Tips**:  
   - Plan your moves to avoid filling up the grid.
   - Focus on merging tiles toward one corner for better control.
   - Think ahead to create opportunities for larger merges.

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

## Expected Number of Pages

1. **Home Page**: Start screen with "Start" button.
2. **Game Screen**: Main 2048 grid and gameplay.
3. **Game Over Screen**: Displays current and highest scores with a retry button.


---

## Database Applied
The project uses a simple database to store the highest score. 
- **Type**: SQLite (local database).
- **Tables**:
  - `high_scores`: Stores player name and highest score.
- **Records**:
  - Tracks the maximum tile value reached for each player.
---

## Project Reference / Source

- YouTube tutorial: [Make 2048 In Python | Full Python Game Tutorial](https://youtu.be/6ZyylFcjfIg?si=98Yc8nJhN8P-MX-8) YT Channel: Tech With Tim
- Code reference: [2048-In-Python] (https://github.com/techwithtim/2048-In-Python) by Tim Ruscica.

---

