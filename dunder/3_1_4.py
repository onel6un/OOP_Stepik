class Book:
    attrs = {'title': str, 'author': str, 'pages': int, 'year': int}

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in self.attrs and self.attrs[key] == type(value):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")


book = Book(author='Сергей Балакирев', title='Python ООП', pages=123,
            year=2022)
