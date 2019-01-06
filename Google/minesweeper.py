# https://techdevguide.withgoogle.com/resources/coding-question-minesweeper/#!
# The Challenge
#
# Implement Minesweeper
#
# Minesweeper is a game where the objective is correctly identify the location of all mines in a given grid.
# You are given a uniform grid of gray squares in the beginning of the game.
# Each square contains either a mine (indicated by a value of 9), or an empty square. Empty squares have a number indicating the count of mines in the adjacent squares. Empty squares can have counts from zero (no adjacent mines) up to 8 (all adjacent squares are mines).

import random
class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.matrix = [[0 for i in range(rows)] for j in range(cols)]
        self.rows = rows
        self.cols = cols
        self.mines = mines

        mines_placed = 0
        while mines_placed < mines:
            r = random.randint(0,rows-1)
            c = random.randint(0,cols-1)
            if self.matrix[r][c] == 9:
                continue
            mines_placed += 1
            for i in range(max(0, r-1), min(r+2, self.rows)):
                for j in range(max(0, c-1), min(c+2, self.cols)):
                    if i == r and j == c:
                        self.matrix[i][j] = 9
                    elif self.matrix[i][j] != 9:
                        self.matrix[i][j] += 1
    def printf(self):
        for r in range(self.rows):
            print(self.matrix[r])
            print('\n')

mine = Minesweeper(8,8,3)
mine.printf()
