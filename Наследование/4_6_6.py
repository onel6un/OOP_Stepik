class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __repr__(self) -> str:
        lst_attrs = []
        for attr, value in self.__dict__.items():
            lst_attrs.append(f"{attr}: {value}")
        return '\n'.join(lst_attrs)


class ShopUserView:
    def __str__(self) -> str:
        lst_attrs = []
        for attr, value in self.__dict__.items():
            if attr == "_id":
                continue
            lst_attrs.append(f"{attr}: {value}")
        return '\n'.join(lst_attrs)


class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)
