from Modele.Board import Board
from Modele.Player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.board.initboard()
        self.whitePlayer = Player("White")
        self.blackPlayer = Player("Black")
        self.whitePlayer.listPiece = self.board.whitePieces
        self.blackPlayer.listPiece = self.board.blackPieces
        self.play()

    def play(self):
        p = 0
        players = [self.whitePlayer, self.blackPlayer]
        while True:
            piece, move = players[p].play(self.board)
            print(piece, move, piece.pos)
            y, x = list(piece.pos)
            x = int(x)
            letter = ["A", "B", "C", "D", "E", "F", "G", "H"]
            y = letter.index(y)
            self.board.grid[8-x][y].piece = None
            y, x = list(move)
            x = int(x)
            y = letter.index(y)
            self.board.grid[8-x][y].piece = piece
            piece.pos = move
            self.board.showgrid()
            p = (p+1) % 2


game = Game()
