from math import sqrt


class Line:
    def __init__(self, x1=0, y1=0, x2=0, y2=0) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __setattr__(self, key, value) -> None:
        if isinstance(value, (int, float)):
            super().__setattr__(key, value)

    def __len__(self):
        lenght = sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        if lenght >= 1:
            return lenght
        return 0
