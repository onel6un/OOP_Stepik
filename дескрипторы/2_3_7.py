class FloatValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)

    @staticmethod
    def check_value(value):
        if type(value) is not float:
            raise TypeError("Присваивать можно только вещественный тип данных.")


class Cell:
    value = FloatValue()

    def __init__(self, value) -> None:
        self.value = value


class TableSheet:
    def __init__(self, N, M) -> None:
        self.cells = [[Cell(0.0) for i in range(M)] for i in range(N)]

    def fall_cells(self, start, step):
        i = start
        for filed in self.cells:
            for cell in filed:
                cell.value = i
                i += step
