class ListInteger(list):
    def __init__(self, *args):
        self._check_args(*args)
        super().__init__(*args)

    @staticmethod
    def _check_args(args):
        for i in args:
            if not isinstance(i, int):
                raise TypeError('можно передавать только целочисленные значения')

    @staticmethod
    def _check_int(value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')

    def __setitem__(self, indx, value):
        self._check_int(value)
        super().__setitem__(indx, value)

    def append(self, value):
        self._check_int(value)
        super().append(value)


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5