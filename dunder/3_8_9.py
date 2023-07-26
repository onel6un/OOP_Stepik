# Первым при инициализации вызываеться андер сеттер, далее сеттер из проперти, который назначает атрибут приватным, и вызывает андер сеттер с приватным именем
#print()
# __setattr__ x 1
# property for x setter
# __setattr___Circle__x:1

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self.__radius = radius

    def __setattr__(self, key, value):
        if type(value) in (int, float):
            super().__setattr__(key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, key):
        return False
