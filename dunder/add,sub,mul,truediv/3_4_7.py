class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

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
        self.__next = next


class Stack:
    top = None
    tail = None

    def push_back(self, obj):
        if not self.top:
            self.top = self.tail = obj
        self.tail.next = obj
        self.tail = obj

    def pop_back(self):
        if self.top and self.top != self.tail:
            node = self.top
            while node.next != self.tail:
                node = node.next
            self.tail = node
            node.next = None
        else:
            self.top = self.tail = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        if type(other) != list:
            raise ArithmeticError('Обект умножения должен иметь тип list')
        list_obj = [StackObj(i) for i in other]
        for i in list_obj:
            self.push_back(i)
        return self


st = Stack()
st.push_back(StackObj(0))
st.push_back(StackObj(1))
st.push_back(StackObj(2))
st.push_back(StackObj(3))
st.push_back(StackObj(4))
st = st * [5, 6, 7, 8]
print(st.tail.data)
