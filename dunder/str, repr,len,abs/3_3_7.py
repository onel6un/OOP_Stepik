from math import sqrt


class Complex:
    def __init__(self, real, img) -> None:
        self.real = real
        self.img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, x):
        if type(x) in (int, float):
            self.__real = x
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, x):
        if type(x) in (int, float):
            self.__img = x
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return sqrt(self.real**2 + self.img**2)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)