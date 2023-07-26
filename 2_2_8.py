class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0) -> None:
        self.x = self.y = 0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def check_value(cls, value):
        return (type(value) in (int, float)
                and cls.MIN_COORD <= value <= cls.MAX_COORD)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.check_value(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.check_value(y):
            self.__y = y

    @staticmethod
    def norm2(vector):
        return vector.x**2 + vector.y**2


r1 = RadiusVector2D()
r2 = RadiusVector2D(1)
r3 = RadiusVector2D(4, 5)

