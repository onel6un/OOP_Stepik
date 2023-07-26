class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, name, value) -> None:
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        super().__setattr__(name, value)

    def __hash__(self) -> int:
        return hash((self.a, self.b, self.c))


inpt = input()

lst_dims = [Dimensions(*list(map(float, l.split()))) for l in inpt.split(';')]

lst_dims.sort(key=lambda x: hash(x))
