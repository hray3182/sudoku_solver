# Sudoku Solver

## Introduction
This program generates a Sudoku puzzle and then attempts to solve it. 

## How to Run
Execute `py main.py` in the terminal to run the program.

## Features
- Generates and solves a Sudoku puzzle, ensuring that the puzzle has a unique solution.


## Known Issues
- The program may experience slower solving speeds if the clues are unevenly distributed across the board. An uneven distribution of clues can make the puzzle computationally more complex to solve.

## How it Works
1. The program starts with an empty 9x9 grid.
2. Random numbers are filled into the grid while maintaining Sudoku rules.
3. Some numbers are then removed, ensuring that the puzzle still has a unique solution.
4. Finally, the program solves the generated puzzle.

## Sudoku Solver Demo
![Sudoku Solver Demo](https://github.com/hray3182/sudoku_solver/blob/master/demo.gif?raw=true)
