from Modele.Case import Case
from Modele.Pieces.Bishop import Bishop
from Modele.Pieces.King import King
from Modele.Pieces.Knight import Knight
from Modele.Pieces.Pawn import Pawn
from Modele.Pieces.Queen import Queen
from Modele.Pieces.Rook import Rook


class Board:

    def __init__(self):
        letter = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.grid = [[Case(None, letter[col] + str(8-raw)) for col in range(8)] for raw in range(8)]
        self.whitePieces = []
        self.blackPieces = []

    def showgrid(self):
        for raw in range(8):
            newRaw = []
            for col in range(8):
                if self.grid[raw][col].isempty():
                    newRaw.append("-")
                else :
                    newRaw.append(self.grid[raw][col].piece.type)
            print(newRaw)

    def initboard(self):

        """ Black pieces """
        self.grid[0][0].piece = Rook("Black", "A8")
        self.grid[0][1].piece = Knight("Black", "B8")
        self.grid[0][2].piece = Bishop("Black", "C8")
        self.grid[0][3].piece = Queen("Black", "D8")
        self.grid[0][4].piece = King("Black", "E8")
        self.grid[0][5].piece = Bishop("Black", "F8")
        self.grid[0][6].piece = Knight("Black", "G8")
        self.grid[0][7].piece = Rook("Black", "H8")
        self.grid[1][0].piece = Pawn("Black", "A7")
        self.grid[1][1].piece = Pawn("Black", "B7")
        self.grid[1][2].piece = Pawn("Black", "C7")
        self.grid[1][3].piece = Pawn("Black", "D7")
        self.grid[1][4].piece = Pawn("Black", "E7")
        self.grid[1][5].piece = Pawn("Black", "F7")
        self.grid[1][6].piece = Pawn("Black", "G7")
        self.grid[1][7].piece = Pawn("Black", "H7")
        for i in range(2):
            for j in range(8):
                self.blackPieces.append(self.grid[i][j].piece)


        """ White pieces """
        self.grid[7][0].piece = Rook("White", "A1")
        self.grid[7][1].piece = Knight("White", "B1")
        self.grid[7][2].piece = Bishop("White", "C1")
        self.grid[7][3].piece = Queen("White", "D1")
        self.grid[7][4].piece = King("White", "E1")
        self.grid[7][5].piece = Bishop("White", "F1")
        self.grid[7][6].piece = Knight("White", "G1")
        self.grid[7][7].piece = Rook("White", "H1")
        self.grid[6][0].piece = Pawn("White", "A2")
        self.grid[6][1].piece = Pawn("White", "B2")
        self.grid[6][2].piece = Pawn("White", "C2")
        self.grid[6][3].piece = Pawn("White", "D2")
        self.grid[6][4].piece = Pawn("White", "E2")
        self.grid[6][5].piece = Pawn("White", "F2")
        self.grid[6][6].piece = Pawn("White", "G2")
        self.grid[6][7].piece = Pawn("White", "H2")
        for i in range(2):
            for j in range(8):
                self.whitePieces.append(self.grid[i+6][j].piece)

    def isempty(self,pos):
        y,x = list(pos)
        x = int(x)
        letter = ["A", "B", "C", "D", "E", "F", "G", "H"]
        y = letter.index(y)
        return self.grid[8-x][y].isempty()
