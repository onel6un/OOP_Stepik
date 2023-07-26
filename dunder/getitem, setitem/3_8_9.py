class TicTacToe:
    def __init__(self) -> None:
        self.clear()

    def clear(self):
        self.pole = [[Cell() for i in range(3)] for i in range(3)]

    def _check_indx(self, indx):
        if not isinstance(indx[0], slice) and not isinstance(indx[1], slice):
            if len(indx) != 2:
                raise IndexError('неверный индекс клетки')
            i, j = indx
            if (not isinstance(i, int) or i > 3) or (not isinstance(j, int) or j > 3):
                raise IndexError('неверный индекс клетки')

    def __getitem__(self, indx):
        self._check_indx(indx)
        if not isinstance(indx[0], slice) and not isinstance(indx[1], slice):
            i, j = indx
            return self.pole[i][j].value
        if isinstance(indx[0], slice):
            cols_indx = indx[1]
            return tuple(map(lambda x: x[cols_indx].value, self.pole))
        if isinstance(indx[1], slice):
            rows_indx = indx[0]
            return tuple(map(lambda x: x.value, self.pole[rows_indx]))

    def __setitem__(self, indx, value):
        self._check_indx(indx)
        if isinstance(indx, tuple):
            i, j = indx
            cell = self.pole[i][j]
            if cell:
                cell.value = value
                cell.is_free = False
            else:
                raise ValueError('клетка уже занята')


class Cell:
    def __init__(self) -> None:
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free

g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

    
try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"


g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"