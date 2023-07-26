class SoftList(list):
    def __getitem__(self, indx):
        try:
            return super().__getitem__(indx)
        except IndexError:
            return False