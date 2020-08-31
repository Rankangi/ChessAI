from Modele.Pieces.Pieces import Pieces


class Rook(Pieces):
    def __init__(self, color, pos):
        Pieces.__init__(self, "R", color, pos)

    def move(self, board):
        possiblemove = [self]
        col, raw = list(self.pos)
        raw = int(raw)
        indexsum = [1, 2, 3, 4, 5, 6, 7]
        i = 0
        while i < 7 and raw + indexsum[i] <= 8:
            if board.isempty(col + str(raw + indexsum[i])):
                possiblemove.append(col + str(raw + indexsum[i]))
            else:
                break
            i += 1
        i = 0
        while i < 7 and raw - indexsum[i] >= 1:
            if board.isempty(col + str(raw - indexsum[i])):
                possiblemove.append(col + str(raw - indexsum[i]))
            else:
                break
            i += 1
        i = 0
        letter = ["A", "B", "C", "D", "E", "F", "G", "H"]
        col = letter.index(col) + 1
        raw = str(raw)
        while i < 7 and col + indexsum[i] <= 8:
            if board.isempty(letter[col + indexsum[i] - 1] + raw):
                possiblemove.append(letter[col + indexsum[i] - 1] + raw)
            else:
                break
            i += 1
        i = 0
        while i < 7 and col - indexsum[i] >= 1:
            if board.isempty(letter[col - indexsum[i] - 1] + raw):
                possiblemove.append(letter[col - indexsum[i] - 1] + raw)
            else:
                break
            i += 1

        return possiblemove