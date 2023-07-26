class DiapValue:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, inctance, value):
        if inctance.MIN_DIMENSION <= value <= inctance.MAX_DIMENSION:
            setattr(inctance, self.name, value)


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000
    a = DiapValue()
    b = DiapValue()
    c = DiapValue()

    def __init__(self, a=10, b=10, c=10):
        self.a = a
        self.b = b
        self.c = c

    def __gt__(self, other) -> bool:
        return (self.a * self.b * self.c) > (other.a * other.b * other.c)

    def __ge__(self, other):
        return (self.a * self.b * self.c) >= (other.a * other.b * other.c)


class ShopItem:
    def __init__(self, name, price, dim) -> None:
        self.name = name
        self.price = price
        self.dim = dim


trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)

print(lst_shop_sorted)
