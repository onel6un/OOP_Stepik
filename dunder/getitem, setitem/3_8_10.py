class Bag:
    def __init__(self, max_weight) -> None:
        self.max_weight = max_weight
        self.things = []

    def _check_indx(self, indx):
        if not isinstance(indx, int) or (0 > indx or indx > len(self.things) - 1):
            raise IndexError('неверный индекс')

    def _check_weight(self, thing):
        if self.things:
            totl_weight = sum(map(lambda x: x.weight, self.things))
            if (totl_weight + thing.weight) < self.max_weight:
                return

            raise ValueError('превышен суммарный вес предметов')

        if thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def add_thing(self, thing):
        self._check_weight(thing)
        self.things.append(thing)

    def __getitem__(self, indx):
        self._check_indx(indx)
        return self.things[indx]

    def __setitem__(self, indx, value):
        self._check_indx(indx)
        if self.things:
            totl_weight = sum(map(lambda x: x.weight, self.things))
            if (totl_weight + value.weight - self[indx].weight) > self.max_weight:
                raise ValueError('превышен суммарный вес предметов')

        if value.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.things[indx] = value

    def __delitem__(self, indx):
        self._check_indx(indx)
        del self.things[indx]


class Thing:
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight


b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

    
b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"