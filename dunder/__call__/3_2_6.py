class DigitRetrieve:
    def __call__(self, str):
        try:
            i = int(str)
        except ValueError:
            i = None
        return i
