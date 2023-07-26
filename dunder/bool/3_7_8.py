class Ellipse:
    def __init__(self, *args) -> None:
        if args and len(args) == 4:
            self.x1, self.y1, self.x2, self.y2 = args

    def __setattr__(self, key, value) -> None:
        if isinstance(value, (int, float)):
            super().__setattr__(key, value)

    def __bool__(self):
        return all((hasattr(self, 'x1'), hasattr(self, 'x2'),
                   hasattr(self, 'y1'), hasattr(self, 'y2')))

    def get_coords(self):
        if not self:
            raise AttributeError('нет координат для извлечения')
        return (self.x1, self.y1, self.x2, self.y2)


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
for obj in lst_geom:
    if obj:
        obj.get_coords()

el2 = Ellipse(1, 2, 3, 4)
