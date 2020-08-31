import numpy as np
from Pieces import Pieces


class Board:

    def __init__(self):
        self.grid = np.array([
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"]
        ])

    def showGrid(self):
        print(self.grid)

    def initBoard(self):
        """ Black pieces """
        self.grid[0][0] = Pieces("R", "Black", "A8")
        self.grid[0][1] = Pieces("N", "Black", "B8")
        self.grid[0][2] = Pieces("B", "Black", "C8")
        self.grid[0][3] = Pieces("Q", "Black", "D8")
        self.grid[0][4] = Pieces("K", "Black", "E8")
        self.grid[0][5] = Pieces("B", "Black", "F8")
        self.grid[0][6] = Pieces("N", "Black", "G8")
        self.grid[0][7] = Pieces("R", "Black", "H8")
        self.grid[1][0] = Pieces("P", "Black", "A7")
        self.grid[1][1] = Pieces("P", "Black", "B7")
        self.grid[1][2] = Pieces("P", "Black", "C7")
        self.grid[1][3] = Pieces("P", "Black", "D7")
        self.grid[1][4] = Pieces("P", "Black", "E7")
        self.grid[1][5] = Pieces("P", "Black", "F7")
        self.grid[1][6] = Pieces("P", "Black", "G7")
        self.grid[1][7] = Pieces("P", "Black", "H7")

        """ White pieces """
        self.grid[7][0] = Pieces("R", "White", "A1")
        self.grid[7][1] = Pieces("N", "White", "B1")
        self.grid[7][2] = Pieces("B", "White", "C1")
        self.grid[7][3] = Pieces("Q", "White", "D1")
        self.grid[7][4] = Pieces("K", "White", "E1")
        self.grid[7][5] = Pieces("B", "White", "F1")
        self.grid[7][6] = Pieces("N", "White", "G1")
        self.grid[7][7] = Pieces("R", "White", "H1")
        self.grid[6][0] = Pieces("P", "White", "A2")
        self.grid[6][1] = Pieces("P", "White", "B2")
        self.grid[6][2] = Pieces("P", "White", "C2")
        self.grid[6][3] = Pieces("P", "White", "D2")
        self.grid[6][4] = Pieces("P", "White", "E2")
        self.grid[6][5] = Pieces("P", "White", "F2")
        self.grid[6][6] = Pieces("P", "White", "G2")
        self.grid[6][7] = Pieces("P", "White", "H2")

board = Board()
board.initBoard()
board.showGrid()