from math import isclose


class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def _get_m(self):
        return self.ro * self.volume

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            other = other._get_m()
        return isclose(self._get_m(), other)

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            other = other._get_m()
        return self._get_m() < other
