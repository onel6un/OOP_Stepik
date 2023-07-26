class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    __id = 0
    __attrs = {'id': (int,), 'name': (str,), 'weight': (int, float),
               'price': (int, float)}

    def __new__(cls, *args, **kwargs):
        cls.__id += 1
        return super().__new__(cls)

    def __init__(self, name, weight, price):
        self.id = self.__id
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key in self.__attrs and type(value) in self.__attrs[key]:
            if key in ('weight', 'price') and value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
            super().__setattr__(key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(item)

