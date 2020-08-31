import random


class Player:
    def __init__(self, color):
        self.color = color
        self.listPiece = []

    def play(self,board):

        """ On récupère tout les mouvements de toutes les pièces"""
        possiblemove = []
        for piece in self.listPiece:
            piecemove = piece.move(board)
            if len(piecemove) != 1:
                possiblemove.append(piecemove)

        """ On choisit une pièce au hasard """
        choice = random.choice(possiblemove)
        piece = choice[0]
        listmove = choice[1:]
        """ On choisit un déplacement au hasard """
        move = random.choice(listmove)

        return piece, move
