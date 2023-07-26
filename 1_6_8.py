# здесь объявляйте класс SingletonFive
class SingletonFive():
    __instance = None
    __count_obj = 0

    def __new__(cls, *args, **kwargs):
        if cls.__count_obj < 5:
            cls.__instance = super().__new__(cls)
            cls.__count_obj += 1
        return cls.__instance
    
    def __init__(self, name):
        self.name = name
        
        
objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять