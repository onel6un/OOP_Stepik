class RadiusVector:
    def __init__(self, *args) -> None:
        self.coords = list(args)

    def __getitem__(self, indx):
        vl = self.coords[indx]
        if isinstance(vl, (int, float)):
            return self.coords[indx]
        return tuple(self.coords[indx])

    def __setitem__(self, indx, value):
        self.coords[indx] = value
