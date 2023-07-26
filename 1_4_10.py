class Translator():
    dict = {}

    def add(self, eng, rus):
        if eng in self.dict:
            if rus in self.dict[eng]:
                return
            self.dict[eng].append(rus)
            return
        self.dict[eng] = [rus]

    def remove(self, eng):
        self.dict.pop(eng)

    def translate(self, eng):
        return self.dict[eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove('car')
print(*tr.translate('go'))