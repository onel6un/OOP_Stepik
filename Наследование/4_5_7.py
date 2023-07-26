from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    _id = 1

    def __init__(self, login, password) -> None:
        self._login = login
        self._password = password
        self._id = self.__create_id() 

    @classmethod
    def __create_id(cls):
        id = cls._id
        cls._id += 1
        return id

    def get_pk(self):
        return self._id
