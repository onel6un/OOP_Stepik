class Item:
    def __init__(self, name, money) -> None:
        self.name = name
        self.money = money

    def __add__(self, other):
        add = other.money if isinstance(other, self.__class__) else other
        return self.money + add

    def __radd__(self, other):
        return self + other


class Budget:
    items = []

    def add_item(self, it):
        self.items.append(it)

    def remove_item(self, indx):
        self.items.pop(indx)

    def get_items(self):
        return self.items


item1 = Item('1', 1)
item2 = Item('1', 2)
item3 = Item('1', 3)

s = item1 + item2 + item3
print(s)
