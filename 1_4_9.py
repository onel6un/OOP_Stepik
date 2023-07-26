import sys

# программу не менять, только добавить два метода
#lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        a, b = int(a), int(b)
        if b > len(self.lst_data):
            return self.lst_data[a:]
        return self.lst_data[a:b+1]

    def insert(self, data):
        for str_values in data:
            dict = {}
            for i, value in enumerate(str_values.split()):
                dict[self.FIELDS[i]] = value
            self.lst_data.append(dict)

lst_in = [
    '1 Сергей 35 120000',
    '2 Федор 23 12000',
    '3 Иван 13 1200'
]

db = DataBase()
db.insert(lst_in)

print(db.lst_data)
print(db.select(1, 15))