class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0) -> None:
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell=None) -> None:
        if not cell:
            raise ValueError('параметр cell не указан')
        self.cells = tuple([tuple([cell() for i in range(cols)]) for i in range(rows)])

    def __getitem__(self, indx):
        i = indx[0]
        j = indx[1]
        return self.cells[i][j].value

    def __setitem__(self, indx, value):
        i = indx[0]
        j = indx[1]
        self.cells[i][j].value = value
