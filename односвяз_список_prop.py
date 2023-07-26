class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if type(next) is StackObj or next is None:
            self.__next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            node = self.top
            while node.next is not None:
                node = node.next
            node.next = obj

    def pop(self):
        if self.top is None:
            return None
        elif self.top.next is None:
            pop_obj = self.top
            self.top = None
            return pop_obj
        else:
            node = self.top
            while node.next is not None:
                if node.next.next is None:
                    pop_obj = node.next
                    node.next = None
                    return pop_obj
                node = node.next

    def get_data(self):
        if self.top is None:
            return []
        else:
            list_data = []
            node = self.top
            while node.next is not None:
                list_data.append(node.data)
                node = node.next
            list_data.append(node.data)
            return list_data
