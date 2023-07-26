class Track:
    def __init__(self, start_x, start_y) -> None:
        self.start = (start_x, start_y)
        self.track = []

    def add_point(self, x, y, speed):
        self.track.append([x, y, speed])

    def _check_indx(self, indx):
        if not isinstance(indx, int) and 0 <= indx <= len(self.fields) - 1:
            raise IndexError('некорректный индекс')

    def __getitem__(self, indx):
        self._check_indx(indx)
        point = tuple(self.track[indx][:2])
        speed = self.track[indx][2:][0]
        return point, speed

    def __setitem__(self, indx, value):
        self._check_indx(indx)
        self.track[indx][2] = value
