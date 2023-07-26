class TriangleListIterator:
    def __init__(self, lst) -> None:
        self.lst = lst
        self.__rows = 0
        self.__cols = 0

    def __iter__(self):
        self.__rows = 0
        self.__cols = 0
        return self

    def __next__(self):
        if self.__rows < len(self.lst):
            ret_rows = self.__rows
            ret_cols = self.__cols
            if self.__rows + 1 != self.__cols:
                self.__cols += 1
                if self.__rows + 1 == self.__cols:
                    self.__rows += 1
                    self.__cols = 0
                return self.lst[ret_rows][ret_cols]
        else:
            raise StopIteration


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32']]

it = TriangleListIterator(lst)

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)