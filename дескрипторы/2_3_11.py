class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for i, tl in enumerate(self.items):
            if tl.uid == indx:
                self.items.pop(i)
                return


class Telecast:
    def __init__(self, id, name, duration):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, id):
        if type(id) is int:
            self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) is str:
            self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        if type(duration) is int:
            self.__duration = duration
