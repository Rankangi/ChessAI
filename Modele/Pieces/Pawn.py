from Modele.Pieces.Pieces import Pieces


class Pawn(Pieces):
    def __init__(self, color, pos):
        Pieces.__init__(self, "P", color, pos)

    def move(self, board):
        possiblemove = [self]
        col, raw = list(self.pos)
        if self.color == "White":
            if raw == "2" and board.isempty(col+str(3)):
                possiblemove.append(col + str(3))
            if int(raw) + 1 <= 8 and board.isempty(col + str(int(raw) + 1)):
                possiblemove.append(col + str(int(raw) + 1))
        else:
            if raw == "7" and board.isempty(col + str(5)):
                possiblemove.append(col + str(5))
            if int(raw) - 1 >= 1 and board.isempty(col + str(int(raw) - 1)):
                possiblemove.append(col + str(int(raw) - 1))

        return possiblemove
