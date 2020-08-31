class Pieces:

    def __init__(self, type, color, pos):
        self.type = type
        self.color = color
        self.pos = pos

    def __repr__(self):
        return self.type