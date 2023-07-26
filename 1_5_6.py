# здесь объявите класс TriangleChecker
class TriangleChecker():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if (not (type(self.a) == int or type(self.a) == float) or self.a <= 0
            or not (type(self.b) == int or type(self.b) == float) or self.b <= 0
            or not (type(self.c) == int or type(self.c) == float) or self.c <= 0):
            return 1
        a, b, c = self.a, self.b, self.c
        if (a + b <= c
            or b + c <= a
            or a + c <= b):
            return 2
        return 3
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран

a, b, c = map(int, input().split()) # эту строчку не менять

tr = TriangleChecker(a, b, c)

print(tr.is_triangle())