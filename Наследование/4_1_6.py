class Thing:
    id = 1

    def __init__(self, name, price) -> None:
        self.id = self._get_id()
        self.name = name
        self.price = price
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None

    @classmethod
    def _get_id(cls):
        id = cls.__base__.id
        cls.__base__.id += 1
        return id

    def get_data(self):
        return (self.id, self.name, self.price, self.weight, self.dims,
                self.memory, self.frm)


class Table(Thing):
    def __init__(self, name, price, weight, dims) -> None:
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm) -> None:
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm

table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(table.id)
print(book.id)