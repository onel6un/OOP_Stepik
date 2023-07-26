class NewList():
    def __init__(self, lst=[]):
        self.lst = lst

    def _sub(self, min_lst, sub_lst):
        for sub in sub_lst:
            for i, min in enumerate(min_lst):
                if sub == min and type(sub) == type(min):
                    min_lst.pop(i)
                    break
        return min_lst

    def __sub__(self, other):
        if not isinstance(other, (self.__class__, list)):
            raise ValueError('второй операнд должен быть NewList')
        sub_lst = other
        if isinstance(other, self.__class__):
            sub_lst = other.lst
        return NewList(self._sub(self.lst.copy(), sub_lst))

    def __rsub__(self, other):
        return NewList(self._sub(other, self.lst.copy()))

    def __isub__(self, other):
        return self - other

    def get_list(self):
        return self.lst



lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"
res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2

assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
#assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"