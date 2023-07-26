class Table():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class TV():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Notebook():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Cup():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Cart():
    goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(int(indx))

    def get_list(self):
        return list((map(lambda x: f'{x.name}: {x.price}', self.goods)))


cart = Cart()
tv1 = TV("samsung", 1111)
tv2 = TV("LG", 1234)
table = Table("ikea", 2345)
n1 = Notebook("msi", 5433)
n2 = Notebook("apple", 542)
c = Cup("keepcup", 43)

cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(n1)
cart.add(n2)
cart.add(c)

print(cart.get_list())