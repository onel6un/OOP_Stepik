class Person:
    def __init__(self, fio, job, old, salary, year_job) -> None:
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.__fields = {0: 'fio', 1: 'job', 2: 'old', 3: "salary", 4: 'year_job'}
        self.__key = 0

    def _check_indx(self, indx):
        if indx > len(self.__fields) - 1:
            raise IndexError('неверный индекс')

    def __getitem__(self, indx):
        self._check_indx(indx)
        key = self.__fields[indx]
        return getattr(self, key)

    def __setitem__(self, indx, value):
        self._check_indx(indx)
        key = self.__fields[indx]
        setattr(self, key, value)

    def __iter__(self):
        self.__key = 0
        return self

    def __next__(self):
        if self.__key <= len(self.__fields) - 1:
            ret_value = self.__key
            self.__key += 1
            field = self.__fields[ret_value]
            return getattr(self, field)
        else:
            raise StopIteration

