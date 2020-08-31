from Modele.Pieces.Pieces import Pieces


class Knight(Pieces):
    def __init__(self, color, pos):
        Pieces.__init__(self,"N",color, pos)

    def move(self, board):
        possiblemove = [self]
        col, raw = list(self.pos)
        raw = int(raw)
        letter = ["A", "B", "C", "D", "E", "F", "G", "H"]
        col = letter.index(col) + 1
        bigindexsum = [-2, 2]
        littleindexsum = [-1, 1]
        for big in bigindexsum:
            for little in littleindexsum:
                if 1 <= col + big <= 8 and 1 <= raw + little <= 8:
                    if board.isempty(letter[col + big - 1] + str(raw + little)):
                        possiblemove.append(letter[col + big - 1] + str(raw + little))
                if 1 <= col + little <= 8 and 1 <= raw + big <= 8:
                    if board.isempty(letter[col + little - 1] + str(raw + big)):
                        possiblemove.append(letter[col + little - 1] + str(raw + big))
        return possiblemove