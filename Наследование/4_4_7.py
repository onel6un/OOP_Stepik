class Furniture:
    def __init__(self, name, weight) -> None:
        self.__verify_name(name)
        self.__verify_weight(weight)
        self._name = name
        self._weight = weight

    def __verify_name(self, name):
        if type(name) != str:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, weight):
        if not isinstance(weight, (int, float)) and weight <= 0:
            raise TypeError('вес должен быть положительным числом')

    def __setattr__(self, name, value) -> None:
        if name == '_name':
            self.__verify_name(value)
        if name == '_weight':
            self.__verify_weight(value)
        super().__setattr__(name, value)


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors) -> None:
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return self.__dict__.values()


class Chair(Furniture):
    def __init__(self, name, weight, height) -> None:
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return self.__dict__.values()


class Table(Furniture):
    def __init__(self, name, weight, height, square) -> None:
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return self.__dict__.values()
