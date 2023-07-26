class ItemAttrs:
    def __getitem__(self, indx):
        name = list(self.__dict__.keys())[indx]
        return getattr(self, name)

    def __setitem__(self, indx, value):
        name = list(self.__dict__.keys())[indx]
        setattr(self, name, value)


class Point(ItemAttrs):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
print(x, y)