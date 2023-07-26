class Box:
    def __init__(self) -> None:
        self.lst_obj = []

    def add_thing(self, obj):
        self.lst_obj.append(obj)

    def get_things(self):
        return self.lst_obj

    def __eq__(self, other) -> bool:

        if len(self.lst_obj) != len(other.lst_obj):
            return False
        return all(map(lambda x: x in other.lst_obj, self.lst_obj))


class Thing:
    def __init__(self, name, mass) -> None:
        self.name = name
        self.mass = mass

    def __eq__(self, other) -> bool:
        return (self.name.lower() == other.name.lower()
                and self.mass == other.mass)

    def __lt__(self, other):
        return self.mass < other.mass

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('доска', 2000))
b2.add_thing(Thing('доска', 2000))


res = b1 == b2 # True
print(res)