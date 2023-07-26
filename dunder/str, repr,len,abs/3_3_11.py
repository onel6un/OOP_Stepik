class PolyLine(object):
    def __init__(self, start_coord, *args) -> None:
        self.line = [start_coord]
        if args:
            for arg in args:
                self.line.append(arg)

    def add_coord(self, x, y):
        self.line.append((x, y))

    def remove_coord(self, indx):
        self.line.pop(indx)

    def get_coords(self):
        return self.line