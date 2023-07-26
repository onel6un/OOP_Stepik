class Factory():
    @staticmethod
    def build_sequence():
        return []

    @staticmethod
    def build_number(string):
        return float(string.strip())


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq