class ListMath:
    def __init__(self, lst=None):
        self.lst_math = [i for i in lst if type(i) in (int, float)] if type(lst) == list else []

    def __add__(self, other):
        return ListMath(list(map(lambda x: x + other, self.lst_math)))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.lst_math = list(map(lambda x: x + other, self.lst_math))
        return self

    def __mul__(self, other):
        return ListMath(list(map(lambda x: x * other, self.lst_math)))

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.lst_math = list(map(lambda x: x * other, self.lst_math))
        return self

    def __sub__(self, other):
        return ListMath(list(map(lambda x: x - other, self.lst_math)))

    def __rsub__(self, other):
        return ListMath((list(map(lambda x: other - x, self.lst_math))))

    def __isub__(self, other):
        self.lst_math = list(map(lambda x: x - other, self.lst_math))
        return self

    def __truediv__(self, other):
        return ListMath(list(map(lambda x: x / other, self.lst_math)))

    def __rtruediv__(self, other):
        return ListMath((list(map(lambda x: other / x, self.lst_math))))

    def __itruediv__(self, other):
        self.lst_math = list(map(lambda x: x / other, self.lst_math))
        return self

a = ListMath([1, 2, -5, 7.68])
b = a + 5
a *= 2
print(a.lst_math)
print(b.lst_math)
