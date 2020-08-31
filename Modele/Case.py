class Case:

    def __init__(self, piece, pos):
        self.piece = piece
        self.pos = pos

    def isempty(self):
        return self.piece is None
