class Thing:
    def __init__(self, name, price, weight) -> None:
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self) -> int:
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    def __init__(self, dict={}):
        self._check_dict(dict)
        self._check_thing(dict)
        super().__init__(dict)

    @staticmethod
    def _check_dict(value):
        if not isinstance(value, dict):
            raise TypeError('аргумент должен быть словарем')

    def _check_thing(self, value):
        for key in value.keys():
            self._check_key(key)

    @staticmethod
    def _check_key(key):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')

    def __setitem__(self, key, value):
        self._check_key(key)
        super().__setitem__(key, value)


th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)
