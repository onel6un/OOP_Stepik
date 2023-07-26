from abc import ABC, abstractmethod


class CountryInterface(ABC):
    @abstractmethod
    def get_info(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass


class Country(CountryInterface):
    def __init__(self, name, population, square) -> None:
        self.name = name
        self.population = population
        self.square = square

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        if isinstance(population, int) and population >= 0:
            self.__population = population

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, square):
        if isinstance(square, (float, int)) and square >= 0:
            self.__square = square

    def get_info(self):
        return f"{self.name}: {self.square}, {self.population}"
