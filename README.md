# Snake Water Gun Game

This is a Python implementation of the classic "Snake, Water, Gun" game, similar to Rock-Paper-Scissors. The game is played between the user and the computer.

## Game Rules:
- **Snake** beats **Water**
- **Water** beats **Gun**
- **Gun** beats **Snake**

If both the player and the computer choose the same, it results in a draw.

## How to Play:
1. The player chooses either `snake`, `water`, or `gun`.
2. The computer randomly selects its choice.
3. The program compares both choices and determines the winner based on the rules.

## Code Overview:
The program uses Python's `random` module to make the computer's choice. The player's input is matched against predefined values for `snake`, `water`, or `gun`. After both choices are made, the game logic determines the winner or if it's a draw.

Here’s a simplified breakdown:
- **1 for Snake**, **-1 for Water**, and **0 for Gun**.
- The game compares the player's choice and the computer's choice to decide the outcome.
- If both choose the same, the game is a draw. Otherwise, the predefined logic determines the winner.

## How to Run the Code:
1. Clone the repository or download the code.
2. Ensure you have Python 3.x installed on your system.
3. Run the program from the terminal or command prompt:

    ```bash
    python snake_water_gun.py
    ```

4. Follow the instructions to enter your choice and see the result.
