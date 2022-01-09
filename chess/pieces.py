class Piece:
    def __init__(self, string, color):
        self.string = string
        self.color = color

    def getColor(self):
        return "{}".format(self.color)

class Knight(Piece):
    def __init__(self, string, color):
        super().__init__(string, color)

    def __str__(self):
        return "{}".format(self.string)
    
class Pawn(Piece):
    def __init__(self, string, color):
        super().__init__(string, color)

    def move(self, startrow, startcol, endrow, endcol):
        pass

    def __str__(self):
        return "{}".format(self.string)

class King(Piece):
    def __init__(self, string, color):
        super().__init__(string, color)

    def __str__(self):
        return "{}".format(self.string)

class Queen(Piece):
    def __init__(self, string, color):
        super().__init__(string, color)

    def __str__(self):
        return "{}".format(self.string)

class Bishop(Piece):
    def __init__(self, string, color):
        super().__init__(string, color)

    def __str__(self):
        return "{}".format(self.string)

class Rook(Piece):
    def __init__(self, string, color):
        super().__init__(string, color)

    def __str__(self):
        return "{}".format(self.string)


class WhitePawn(Pawn):
    
    def __init__(self, string, position):
        super().__init__(string)
        self.position = position

    def move(self, startrow, startcol, endrow, endcol):
        pass
        # if startrow != endrow:
        #     if startrow
class BlackPawn(Pawn):
    pass
