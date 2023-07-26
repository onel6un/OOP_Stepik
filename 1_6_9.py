TYPE_OS = 1 # 1 - Windows; 2 - Linux


class DialogWindows():
    name_class = "DialogWindows"

    def __init__(self, name) -> None:
        self.name = name


class DialogLinux():
    name_class = "DialogLinux"

    def __init__(self, name) -> None:
        self.name = name


class Dialog():
    def __new__(cls, *args):
        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)
            DialogWindows.__init__(obj, *args)
            return obj
        if TYPE_OS != 1:
            obj = super().__new__(DialogLinux)
            DialogLinux.__init__(obj, *args)
            return obj

cl1 = Dialog('1223')
print(cl1.name)