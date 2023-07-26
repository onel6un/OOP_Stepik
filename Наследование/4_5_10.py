class Track:
    def __init__(self, *args) -> None:
        if len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            self.__points = (PointTrack(*args))
        else:
            self.__points = list(args)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        add_list = [pt]
        self.__points = add_list.extend(self.__points)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


class PointTrack:
    def __init__(self, x, y) -> None:
        self._check_value(x)
        self._check_value(y)
        self.x = x
        self.y = y

    @staticmethod
    def _check_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError('координаты должны быть числами')

    def __setattr__(self, name: str, value) -> None:
        self._check_value(value)
        super().__setattr__(name, value)

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"

tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)