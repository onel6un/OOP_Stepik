class Array:
    def __init__(self, max_length, cell) -> None:
        self.max_lenght = max_length
        self.cell = cell
        self.values = [cell(0) for i in range(max_length)]

    def _check_indx(self, indx):
        if not isinstance(indx, int) or (indx < 0 or self.max_lenght <= indx):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, indx):
        self._check_indx(indx)
        return self.values[indx].value

    def __setitem__(self, indx, value):
        self._check_indx(indx)
        self.values[indx].value = value

    def __str__(self):
        return ' '.join(map(lambda x: str(x.value), self.values))


class Integer:
    def __init__(self, start_value) -> None:
        self.value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')
        self.__value = value
