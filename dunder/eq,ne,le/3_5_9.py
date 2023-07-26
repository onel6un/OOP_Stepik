class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls


class MoneyR:
    def __init__(self, volume=0):
        self.cb = None
        self.volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @staticmethod
    def _volume_to_rub(other):
        rate_r = other.cb.rates.get('rub')
        rate_e = other.cb.rates.get('euro')
        if isinstance(other, MoneyR):
            return other.volume
        if isinstance(other, MoneyD):
            rub = other.volume * rate_r
            return rub
        if isinstance(other, MoneyE):
            doll = other.volume * rate_e
            rub = doll * rate_r
            return rub

    def __eq__(self, other):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        other_rub = self._volume_to_rub(other)
        return round(self.volume, 1) == round(other_rub, 1)

    def __gt__(self, other):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        other_rub = self._volume_to_rub(other)
        return round(self.volume, 1) > round(other_rub, 1)

    def __ge__(self, other):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        other_rub = self._volume_to_rub(other)
        return round(self.volume, 1) >= round(other_rub, 1)


class MoneyD:
    def __init__(self, volume=0):
        self.cb = None
        self.volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @staticmethod
    def _volume_to_rub(other):
        rate_r = other.cb.rates.get('rub')
        rate_e = other.cb.rates.get('euro')
        if isinstance(other, MoneyR):
            return other.volume
        if isinstance(other, MoneyD):
            rub = other.volume * rate_r
            return rub
        if isinstance(other, MoneyE):
            doll = other.volume * rate_e
            rub = doll * rate_r
            return rub

    def __eq__(self, other):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        self_rub = self._volume_to_rub(self)
        other_rub = self._volume_to_rub(other)
        return round(self_rub, 1) == round(other_rub, 1)

    def __gt__(self, other):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        self_rub = self._volume_to_rub(self)
        other_rub = self._volume_to_rub(other)
        return round(self_rub, 1) > round(other_rub, 1)

    def __ge__(self, other):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        self_rub = self._volume_to_rub(self)
        other_rub = self._volume_to_rub(other)
        return round(self_rub, 1) >= round(other_rub, 1)


class MoneyE:
    def __init__(self, volume=0):
        self.cb = None
        self.volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @staticmethod
    def _volume_to_rub(other):
        rate_r = other.cb.rates.get('rub')
        rate_e = other.cb.rates.get('euro')
        if isinstance(other, MoneyR):
            return other.volume
        if isinstance(other, MoneyD):
            rub = other.volume * rate_r
            return rub
        if isinstance(other, MoneyE):
            doll = other.volume * rate_e
            rub = doll * rate_r
            return rub

    def __eq__(self, other):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        self_rub = self._volume_to_rub(self)
        other_rub = self._volume_to_rub(other)
        return round(self_rub, 1) == round(other_rub, 1)

    def __gt__(self, other):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        self_rub = self._volume_to_rub(self)
        other_rub = self._volume_to_rub(other)
        return round(self_rub, 1) > round(other_rub, 1)

    def __ge__(self, other):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        self_rub = self._volume_to_rub(self)
        other_rub = self._volume_to_rub(other)
        return round(self_rub, 1) >= round(other_rub, 1)

CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyD(45000)
d = MoneyE(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")

print(r.cb.rates)