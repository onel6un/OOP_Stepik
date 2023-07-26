class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def pt_clone(self):
        return Point(self.x, self.y)

pt = Point(1, 2)
pt.pt_clone()