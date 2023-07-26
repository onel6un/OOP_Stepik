class Morph:
    def __init__(self, *args) -> None:
        self.__lst_wrds = [w for w in args if self._check_value(w)]

    @staticmethod
    def _check_value(word):
        return isinstance(word, str)

    def add_word(self, word):
        if self._check_value(word):
            self.__lst_wrds.append(word)

    def get_words(self):
        return tuple(self.__lst_wrds)

    def __eq__(self, other):
        return other.lower() in self.get_words()


text = 'Мы будем устанавливать связь завтра днем.'

s = """- связь, связи, связью, связи, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях
"""

dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in s.splitlines()]

lst_w = map(lambda x: x.strip('., !?').lower(), text.split())

res = list(filter(lambda word: True if any(morph == word for morph in dict_words) else False, lst_w))
print(res)