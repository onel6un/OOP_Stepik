class Digit:
    def __init__(self, value) -> None:
        self.value = value

    @staticmethod
    def _check_digit(value):
        if not isinstance(value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):
    def __init__(self, value) -> None:
        self._check_int(value)
        super().__init__(value)

    @staticmethod
    def _check_int(value):
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def __init__(self, value) -> None:
        self._check_float(value)
        super().__init__(value)

    @staticmethod
    def _check_float(value):
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def __init__(self, value) -> None:
        self._check_positive(value)
        super().__init__(value)

    @staticmethod
    def _check_positive(value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, value) -> None:
        self._check_negative(value)
        super().__init__(value)

    @staticmethod
    def _check_negative(value):
        if value > 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5),
          FloatPositive(9.2), FloatPositive(6.5), FloatPositive(3.5),
          FloatPositive(8.9)]


lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
