class move(object):
    __x__ = None
    __y__ = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x__

    @property
    def y(self):
        return self.__y__

    @x.setter
    def x(self, value):
        self.__x__ = value

    @y.setter
    def y(self, value):
        self.__y__ = value

    def __str__(self):
        return ("Move [x: " + str(self.x) + ", y: " + str(self.y) + "]")

