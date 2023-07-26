# Здесь объявляется класс Factory
class Factory():
    def build_sequence(self):
        return []

    def build_number(self, string):
        return float(string.strip())


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
res = Loader.parse_format("1, 2, 3, -5, 10", Factory)