class SellItem:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class House(SellItem):
    def __init__(self, name, price, material, square) -> None:
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name, price, size, rooms) -> None:
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name, price, square) -> None:
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name) -> None:
        self.name = name
        self.slots = []

    def add_object(self, obj):
        self.slots.append(obj)

    def remove_object(self, obj):
        self.slots.remove(obj)

    def get_objects(self):
        return self.slots
