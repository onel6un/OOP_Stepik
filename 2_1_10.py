class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head is None and self.tail is None:
            self.head = obj
            self.tail = obj
        else:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj

    def remove_obj(self):
        if self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            obj_prev = self.tail.get_prev()
            obj_prev.set_next(None)
            self.tail = obj_prev

    def get_data(self):
        list_data = []
        if self.head is None:
            return list_data

        obj = self.head
        while obj.get_next() is not None:
            list_data.append(obj.get_data())
            obj = obj.get_next()
        list_data.append(self.tail.get_data())
        return list_data


class ObjList:
    def __init__(self, data) -> None:
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
