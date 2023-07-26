class StringDigit(str):
    def __init__(self, str) -> None:
        self._check_str(str)
        super().__init__()

    @staticmethod
    def _check_str(str):
        for i in str:
            try:
                int(i)
            except ValueError:
                raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        self._check_str(other)
        return StringDigit(super().__add__(other))

    def __radd__(self, other):
        return StringDigit(other) + self


sd = StringDigit("123")
print(sd)       # 123
sd = "456" + sd # StringDigit: 123456
print(sd)