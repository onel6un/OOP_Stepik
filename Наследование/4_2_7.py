class Tuple(tuple):
    def __add__(self, other):
        new_lst = [*self]
        for i in other:
            new_lst.append(i)
        return Tuple(new_lst)
