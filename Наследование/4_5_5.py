class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    __id = 1

    def __init__(self, name, weight, price) -> None:
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.__create_id()

    @classmethod
    def __create_id(cls):
        id = cls.__id
        cls.__id += 1
        return id

    def get_id(self):
        return self.__id
