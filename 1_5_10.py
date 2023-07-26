import sys


class ListObject():
    def __init__(self, data) -> None:
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))


tail_obj = None
head_obj = None
for i, data in enumerate(lst_in):
    if i == 0:
        tail_obj = ListObject(data)
        head_obj = tail_obj
        continue
    node_obj = ListObject(data)
    tail_obj.link(node_obj)
    tail_obj = node_obj

print(head_obj.next_obj.next_obj.data)
lst_in = ['1. Первые шаги в ООП',
          '1.1 Как правильно проходить этот курс',
          '1.2 Концепция ООП простыми словами',
          '1.3 Классы и объекты. Атрибуты классов и объектов',
          '1.4 Методы классов. Параметр self',
          '1.5 Инициализатор init и финализатор del',
          '1.6 Магический метод new. Пример паттерна Singleton',
          '1.7 Методы класса (classmethod) и статические методы (staticmethod)']