from Modele.Pieces.Pieces import Pieces


class Bishop(Pieces):
    def __init__(self, color, pos):
        Pieces.__init__(self,"B",color, pos)

    def move(self, board):
        possiblemove = [self]
        col, raw = list(self.pos)
        raw = int(raw)
        letter = ["A", "B", "C", "D", "E", "F", "G", "H"]
        col = letter.index(col) + 1
        indexsum = [1, 2, 3, 4, 5, 6, 7]
        i = 0
        while i < 7 and raw + indexsum[i] <= 8 and col + indexsum[i] <= 8:
            if board.isempty(letter[col + indexsum[i] - 1] + str(raw + indexsum[i])):
                possiblemove.append(letter[col + indexsum[i] - 1] + str(raw + indexsum[i]))
            else:
                break
            i += 1
        i = 0
        while i < 7 and raw - indexsum[i] >= 1 and col - indexsum[i] >= 1:
            if board.isempty(letter[col - indexsum[i] - 1] + str(raw - indexsum[i])):
                possiblemove.append(letter[col - indexsum[i] - 1] + str(raw - indexsum[i]))
            else:
                break
            i += 1
        i = 0
        while i < 7 and raw + indexsum[i] <= 8 and col - indexsum[i] >= 1:
            if board.isempty(letter[col - indexsum[i] - 1] + str(raw + indexsum[i])):
                possiblemove.append(letter[col - indexsum[i] - 1] + str(raw + indexsum[i]))
            else:
                break
            i += 1
        i = 0
        while i < 7 and raw - indexsum[i] >= 1 and col + indexsum[i] <= 8:
            if board.isempty(letter[col + indexsum[i] - 1] + str(raw - indexsum[i])):
                possiblemove.append(letter[col + indexsum[i] - 1] + str(raw - indexsum[i]))
            else:
                break
            i += 1

        return possiblemove