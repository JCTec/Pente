from Copy import deepCopy

class GameState(object):

    __tile__ = None

    __board__ = []

    __x__ = 0

    __y__ = 0

    __value__ = None

    def __init__(self, board, tile, move, value=None):
        self.tile = tile
        self.board = deepCopy(board)
        self.x = move.x
        self.y = move.y
        self.value = value

    @property
    def tile(self):
        return self.__tile__

    @property
    def value(self):
        return self.__value__

    @property
    def board(self):
        return self.__board__

    @property
    def x(self):
        return self.__x__

    @property
    def y(self):
        return self.__y__

    @tile.setter
    def tile(self, value):
        self.__tile__ = value

    @board.setter
    def board(self, value):
        self.__board__ = value

    @x.setter
    def x(self, value):
        self.__x__ = value

    @y.setter
    def y(self, value):
        self.__y__ = value

    @value.setter
    def value(self, value):
        self.__value__ = value

    def __str__(self):
        return "(Tile:_" + self.tile + " X: " + str(self.x) + " Y: " + str(self.y) + ")"