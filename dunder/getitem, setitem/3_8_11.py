class SparseTable:
    def __init__(self) -> None:
        self.rows = 0
        self.cols = 0
        self.table = {}

    def add_data(self, row, col, data):
        if self.rows < row + 1:
            self.rows = row + 1
        if self.cols < col + 1:
            self.cols = col + 1
        self.table[(row, col)] = data

    def remove_data(self, row, col):
        if (row, col) not in self.table:
            raise IndexError('ячейка с указанными индексами не существует')
        del self.table[(row, col)]
        rows_value = []
        cols_value = []
        for key in self.table.keys():
            rows_value.append(key[0])
            cols_value.append(key[1])
        self.rows = max(rows_value) + 1
        self.cols = max(cols_value) + 1

    def __getitem__(self, indx):
        if indx not in self.table:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.table[indx].value

    def __setitem__(self, indx, value):
        self.add_data(*indx, Cell(value))


class Cell:
    def __init__(self, value) -> None:
        self.value = value


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
    
try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"