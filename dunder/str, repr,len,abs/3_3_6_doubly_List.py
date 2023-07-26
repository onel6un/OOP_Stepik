class ObjL:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, name):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == type(instance) or value is None:
            setattr(instance, self.name, value)


class ObjList:
    prev = ObjL()
    next = ObjL()

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class LinkedList:
    head = None
    tail = None

    def _get_obj(self, indx):
        i = 0
        node = self.head
        while i != indx:
            node = node.next
            i += 1
        return node

    def add_obj(self, obj):
        if not self.head and not self.tail:
            self.head = self.tail = obj
        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj

    def remove_obj(self, indx):
        if self.head:
            node = self._get_obj(indx)
            if self.head == self.tail:
                self.head = self.tail = None
            elif node == self.head:
                r_node = node.next
                r_node.prev = None
                self.head = r_node
            elif node == self.tail:
                l_node = node.prev
                l_node.next = None
                self.tail = l_node
            else:
                l_node = node.prev
                r_node = node.next
                l_node.next = r_node
                r_node.prev = l_node

    def __len__(self):
        len = 0
        node = self.head
        while node is not None:
            len += 1
            node = node.next
        return len

    def __call__(self, indx):
        return self._get_obj(indx).data

linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))

linked_lst.remove_obj(0)


