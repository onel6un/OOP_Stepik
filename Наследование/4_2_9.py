class IteratorAttrs:
    def __iter__(self):
        return ((key, value) for key, value in self.__dict__.items())


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory) -> None:
        self.model = model
        self.size = size
        self.memory = memory

phone = SmartPhone(5, (3, 4), 2)

for value in phone:
    print(value)