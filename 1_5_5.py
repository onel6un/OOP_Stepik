import random


class Line():
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect():
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse():
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


lst = [Line, Rect, Ellipse]

elements = []

for i in range(217):
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    c = random.randint(1, 1000)
    d = random.randint(1, 1000)
    cls = random.choice(lst)
    elements.append(cls(a, b, c, d))

for obj in elements:
    if type(obj) == Line:
        obj.sp = (0, 0)
        obj.ep = (0, 0)
