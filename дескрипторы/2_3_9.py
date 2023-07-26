class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if thing.weight + self.get_total_weight() < self.max_weight:
            self.things.append(thing)

    def remove_thing(self, indx):
        self.things.pop(indx)

    def get_total_weight(self):
        weight = 0
        for thing in self.things:
            weight += thing.weight
        return weight


class Thing:
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight
