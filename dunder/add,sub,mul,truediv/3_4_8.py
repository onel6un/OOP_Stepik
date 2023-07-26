class Book:
    def __init__(self, title, author, year):
        self.title = title if type(title) == str else None
        self.author = author if type(author) == str else None
        self.year = year if type(year) == int else None


class Lib:
    def __init__(self) -> None:
        self.book_list = []

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, Book):
            self.book_list.remove(other)
        else:
            self.book_list.pop(other)
        return self

    def __len__(self):
        return len(self.book_list)
