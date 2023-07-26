import inspect


class Vector:
    def __init__(self, *args) -> None:
        for arg in args:
            if not isinstance(arg, (int, float)):
                return ValueError('Аргуметы должны быть типа int or float')
        self.coords = args

    def __len__(self):
        return len(self.coords)

    def _eq_len(self, other):
        return len(self) == len(other)

    def __add__(self, other):
        lst_add = []
        if isinstance(other, self.__class__):
            if not self._eq_len(other):
                raise ArithmeticError('размерности векторов не совпадают')
            for i, cord in enumerate(self.coords):
                sum_cord = cord + other.coords[i]
                lst_add.append(sum_cord)
        else:
            for cord in self.coords:
                sum_cord = cord + other
                lst_add.append(sum_cord)

        if inspect.currentframe().f_back.f_code.co_name == '__iadd__':
            self.coords = tuple(lst_add)
            return self
        else:
            return Vector(*lst_add)

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        lst_add = []
        if isinstance(other, self.__class__):
            if not self._eq_len(other):
                raise ArithmeticError('размерности векторов не совпадают')
            for i, cord in enumerate(self.coords):
                sum_cord = cord - other.coords[i]
                lst_add.append(sum_cord)
        else:
            for cord in self.coords:
                sum_cord = cord - other
                lst_add.append(sum_cord)

        if inspect.currentframe().f_back.f_code.co_name == '__isub__':
            self.coords = tuple(lst_add)
            return self
        else:
            return Vector(*lst_add)

    def __isub__(self, other):
        return self - other

    def __mul__(self, other):
        lst_add = []
        if isinstance(other, self.__class__):
            if not self._eq_len(other):
                raise ArithmeticError('размерности векторов не совпадают')
            for i, cord in enumerate(self.coords):
                sum_cord = cord * other.coords[i]
                lst_add.append(sum_cord)
        else:
            for cord in self.coords:
                sum_cord = cord * other
                lst_add.append(sum_cord)

        return Vector(*lst_add)

    def __eq__(self, other):
        return self.coords == other.coords

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True