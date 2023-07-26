def log_decorater(func, list):
    def wrapper(*args, **kwargs):
        list.append(func.__name__)
        return func(*args, **kwargs)
    return wrapper


def class_log(log):
    def wrapper(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, log_decorater(v, log))
        return cls

    return wrapper


vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
print(v[0])
print(vector_log)
