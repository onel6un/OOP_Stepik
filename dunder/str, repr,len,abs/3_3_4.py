class Model:
    def query(self, *args, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        str = 'Model:'
        for key, value in self.__dict__.items():
            str = str + f' {key} = {value},'
        if str == 'Model:':
            return 'Model'
        return str.rstrip(',')


model = Model()
#model.query(id=1, fio='Sergey', old=33)
print(model)