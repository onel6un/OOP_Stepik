class StackObj:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    top = None
    tail = None
    count = 0

    def _check_indx(self, indx):
        if not isinstance(indx, int) or (indx < 0 or self.count <= indx):
            raise IndexError('неверный индекс')

    def push_back(self, obj):
        if not self.top:
            self.top = self.tail = obj
            self.count += 1
        else:
            self.tail.next = obj
            self.tail = obj
            self.count += 1

    def push_front(self, obj):
        if not self.top:
            self.top = self.tail = obj
            self.count += 1
        else:
            obj.next = self.top
            self.top = obj
            self.count += 1

    def pop(self):
        if self.top and self.top != self.tail:
            node = self.top
            while node.next != self.tail:
                node = node.next
            self.tail = node
            pop_obj = node.next
            node.next = None
            self.count -= 1
            return pop_obj
        else:
            self.top = self.tail = None
            self.count = 0
            return None

    def _get_obj(self, indx):
        self._check_indx(indx)
        if indx == self.count - 1:
            return self.tail
        i = 0
        node = self.top
        while i != indx:
            node = node.next
            i += 1
        return node

    def __getitem__(self, indx):
        if indx == self.count - 1:
            return self.tail.data
        return self._get_obj(indx).data

    def __setitem__(self, indx, value):
        node = self._get_obj(indx)
        node.data = value

    def __iter__(self):
        self.ret = self.top
        return self

    def __next__(self):
        if self.ret:
            obj = self.ret
            self.ret = self.ret.next
            return obj
        else:
            raise StopIteration