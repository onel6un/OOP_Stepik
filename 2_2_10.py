from math import sqrt


class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.list_point = []
        if len(args) != 0:
            for line in args:
                self.list_point.append(line)

    def get_path(self):
        return self.list_point

    def add_line(self, line):
        self.x += 1
        self.list_point.append(line)

    def get_length(self):
        L = 0
        for i, line in enumerate(self.list_point):
            if i == 0:
                L += sqrt((line.x-0)**2 + (line.y-0)**2)
            else:
                prev_line = self.list_point[i-1]
                L += sqrt((line.x-prev_line.x)**2 + (line.y-prev_line.y)**2)
        return L
