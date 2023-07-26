class Vector:
    def __init__(self, *args) -> None:
        self.coords = args

    def _check_vector(self, vector):
        if len(self.coords) != len(vector.coords):
            raise TypeError('размерности векторов не совпадают')

    def __add__(self, other):
        self._check_vector(other)
        self_vctr = list(self.coords)
        for i, value in enumerate(other.coords):
            self_vctr[i] = self_vctr[i] + value
        return Vector(*self_vctr)

    def __sub__(self, other):
        self._check_vector(other)
        self_vctr = list(self.coords)
        for i, value in enumerate(other.coords):
            self_vctr[i] = self_vctr[i] - value
        return Vector(*self_vctr)

    def get_coords(self):
        return self.coords


class VectorInt(Vector):
    def __init__(self, *args) -> None:
        self._check_int_cord(args)
        super().__init__(*args)

    @staticmethod
    def _check_int_cord(coords):
        for cord in coords:
            if not isinstance(cord, int):
                raise ValueError('координаты должны быть целыми числами')

    def __add__(self, other):
        try:
            self._check_int_cord(other.coords)
        except ValueError:
            return super().__add__(other)

        self._check_vector(other)
        self_vctr = list(self.coords)
        for i, value in enumerate(other.coords):
            self_vctr[i] = self_vctr[i] + value
        return VectorInt(*self_vctr)

    def __sub__(self, other):
        try:
            self._check_int_cord(other)
        except ValueError:
            return super().__sub__(other)

        self._check_vector(other)
        self_vctr = list(self.coords)
        for i, value in enumerate(other.coords):
            self_vctr[i] = self_vctr[i] - value
        return VectorInt(*self_vctr)


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
#v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
print(v.coords)