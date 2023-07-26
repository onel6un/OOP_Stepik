class Record:
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.fields = list(kwargs.keys())

    def _check_item(self, item):
        if not isinstance(item, int) and item > len(self.fields) - 1:
            raise IndexError('неверный индекс поля')

    def __getitem__(self, item):
        self._check_item(item)
        key = self.fields[item]
        return getattr(self, key)

    def __setitem__(self, item, value):
        self._check_item(item)
        key = self.fields[item]
        setattr(self, key, value)

r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.__dict__)