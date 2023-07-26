class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return list(map(self.render, func().split()))
        return wrapper


class RenderDigit():
    def __call__(self, str):
        try:
            i = int(str)
        except ValueError:
            i = None

        return i


class RenderFloat():
    def __call__(self, str):
        try:
            i = float(str)
        except ValueError:
            i = None

        return i


rend_int = RenderDigit()
rend_fl = RenderFloat()


@InputValues(render=rend_fl)
def input_dg():
    return input()


res = input_dg()
print(res)
