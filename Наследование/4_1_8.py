class Singleton:
    _instance = None
    _instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if not cls._instance_base:
                cls._instance_base = object.__new__(cls)
            cls._instance_base

        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance


class Game(Singleton):
    def __init__(self, name) -> None:
        if 'name' not in self.__dict__:
            self.name = name


game = Game("name")
game1 = Game("name1")

print(game1.name)