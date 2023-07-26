class DataBase:
    def __init__(self, path) -> None:
        self.dict_db = {}
        self.path = path

    def write(self, record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        for lst_obj in self.dict_db.values():
            if len(lst_obj) == 1:
                return lst_obj[0]
            else:
                return list(filter(lambda x: x.pk == pk, lst_obj))[0]


class Record:
    count = 1

    def __init__(self, fio, descr, old) -> None:
        self.pk = Record.count
        self.fio = fio
        self.descr = descr
        self.old = old
        Record.count += 1

    def __hash__(self) -> int:
        return hash((self.fio, self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)

lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'Балакирев С.М.; преподаватель; 33'
          ]
#lst_in = list(map(str.strip, sys.stdin.readlines()))

db = DataBase('1')
for str in lst_in:
    args = list(map(lambda x: x.strip(), str.split(';')))
    args[-1] = int(args[-1])
    print(args[0])
    db.write(Record(*args))
