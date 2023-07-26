class BookStudy:
    def __init__(self, name, author, year) -> None:
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self) -> int:
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]

lst_bs = []

for l in lst_in:
    args = list(map(str.strip, l.split(';')))
    args[-1] = int(args[-1])
    lst_bs.append(BookStudy(*args))

unique_books = len(set(lst_bs))
