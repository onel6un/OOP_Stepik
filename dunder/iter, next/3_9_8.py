class IterColumn:
    def __init__(self, lst, column) -> None:
        self.lst = lst
        self.column = column

    def __iter__(self):
        self.__indx = 0
        return self

    def __next__(self):
        if self.__indx < len(self.lst):
            ret_row = self.__indx
            self.__indx += 1
            return self.lst[ret_row][self.column]
        else:
            raise StopIteration

lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

it = IterColumn(lst, 0)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)