class WordString:
    def __init__(self, string=''):
        self.string = string

    def __call__(self, indx):
        return self.get_list()[indx]

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string):
        self.__string = string

    def get_list(self):
        return self.string.split()

    def __len__(self):
        return len(self.get_list())



words = WordString()
words.string = "Курс по Python ООП"
print(words(0))
