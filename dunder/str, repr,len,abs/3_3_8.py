from math import sqrt


class RadiusVector:
    def __init__(self, *args):
        if len(args) > 1:
            i = 1
            for arg in args:
                setattr(self, f'coord_{i}', arg)
                i += 1
        else:
            for i in range(1, args[0]+1):
                setattr(self, f'coord_{i}', 0)

    def set_coords(self, *args):
        i = 1
        for arg in args:
            if hasattr(self, f'coord_{i}'):
                setattr(self, f'coord_{i}', arg)
            i += 1

    def get_coords(self):
        return tuple(self.__dict__.values())

    def __len__(self):
        return len(self.__dict__)

    def __abs__(self):
        return sqrt(sum(map(lambda x: x*x, self.__dict__.values())))

vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D) # res_len = 3
print(vector3D.__dict__)
res_abs = abs(vector3D)
print(res_abs)