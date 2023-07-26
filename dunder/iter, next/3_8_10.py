class Cell:
    def __init__(self, data) -> None:
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class TableValues:
    def __init__(self, rows, cols, type_data=int) -> None:
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[Cell(0) for i in range(cols)] for i in range(rows)]

    def _check_indx(self, indx):
        i, j = indx
        if not all((isinstance(i, int), isinstance(j, int), i < self.rows, j < self.cols)):
            raise IndexError('неверный индекс')

    def _check_value(self, value):
        if self.type_data != type(value):
            raise TypeError('неверный тип присваиваемых данных')

    def __getitem__(self, indx):
        self._check_indx(indx)
        i, j = indx
        return self.table[i][j].data

    def __setitem__(self, indx, value):
        self._check_indx(indx)
        self._check_value(value)
        i, j = indx
        self.table[i][j].data = value

    def __iter__(self):
        self.__row_indx = 0
        self.__col_indx = 0
        return self

    def __next__(self):
        if self.__row_indx < self.rows:
            lst_obj = self.table[self.__row_indx]
            self.__row_indx += 1
            return map(lambda x: x.data, lst_obj)
        else:
            raise StopIteration


tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"
        
assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"


tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"


try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"


try:
    a = tb[2, 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"