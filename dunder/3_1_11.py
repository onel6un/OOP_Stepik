import time


class Date:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if hasattr(instance, self.name):
            return  # атрибут уже есть

        if type(value) in (int, float):
            setattr(instance, self.name, value)


class Mechanical:
    date = Date()

    def __init__(self, date):
        self.date = date


class Aragon:
    date = Date()

    def __init__(self, date):
        self.date = date


class Calcium:
    date = Date()

    def __init__(self, date):
        self.date = date


class GeyserClassic:
    MAX_DATE_FILTER = 100
    numb_slots = {1: 'slot_1', 2: 'slot_2', 3: 'slot_3'}
    type_slots = {1: Mechanical, 2: Aragon, 3: Calcium}

    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def add_filter(self, slot_num, filter):
        numb_slot = self.numb_slots[slot_num]
        type_slot = self.type_slots[slot_num]
        if type_slot == type(filter) and getattr(self, numb_slot) is None:
            setattr(self, numb_slot, filter)

    def remove_filter(self, slot_num):
        numb_slot = self.numb_slots[slot_num]
        setattr(self, numb_slot, None)

    def get_filters(self):
        return (self.slot_1, self.slot_2, self.slot_3)

    def water_on(self):
        return (
            None not in self.get_filters()
            and all(list(map(lambda x: True if (time.time() - x.date) <= self.MAX_DATE_FILTER else False, self.get_filters())))
        )


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
print(w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
print(w)