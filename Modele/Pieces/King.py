from Modele.Pieces.Pieces import Pieces


class King(Pieces):
    def __init__(self, color, pos):
        Pieces.__init__(self,"K",color, pos)

    def move(self, board):
        possiblemove = [self]
        col, raw = list(self.pos)
        raw = int(raw)
        letter = ["A", "B", "C", "D", "E", "F", "G", "H"]
        col = letter.index(col) + 1
        sumindex = [-1, 0, 1]
        for j in sumindex:
            for i in sumindex:
                if (col == 1 and j == -1) or (col == 8 and j == 1) or (raw == 1 and i == -1) or (raw == 8 and i == 1) or (i == 0 and j == 0):
                    continue
                elif board.isempty(letter[col + j - 1] + str(raw + i)):
                    possiblemove.append(letter[col + j - 1] + str(raw + i))
        return possiblemove