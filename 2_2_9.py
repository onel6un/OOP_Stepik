class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @classmethod
    def check_node(cls, node):
        return type(node) is cls

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        if self.check_node(left):
            self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        if self.check_node(right):
            self.__right = right


class DecisionTree:
    root = None

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if cls.root is None:
            cls.root = obj
            return obj
        if left:
            node.left = obj
        else:
            node.right = obj
        return obj

    @classmethod
    def predict(cls, root, x):
        node = root
        while node.left is not None and node.right is not None:
            if x[node.indx] == 1:
                node = node.left
            else:
                node = node.right
        return node.value


root = DecisionTree.add_obj(TreeObj(0, 'любит python'))
v_11 = DecisionTree.add_obj(TreeObj(1, 'понимает ООП'), root)
v_12 = DecisionTree.add_obj(TreeObj(2, 'Panda'), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [0, 1, 0]
res = DecisionTree.predict(root, x)
print(res)
