class Aircraft:
    def __init__(self, model, mass, speed, top) -> None:
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, name, value) -> None:
        if name in ("_mass", "_speed", "_top"):
            if not isinstance(value, (int, float)) or value <= 0:
                raise TypeError('неверный тип аргумента')
        if name == '_model':
            if not isinstance(value, str):
                raise TypeError('неверный тип аргумента')
        super().__setattr__(name, value)


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs) -> None:
        super().__init__(model, mass, speed, top)
        self._chairs = chairs

    def __setattr__(self, name, value) -> None:
        if name == "_chairs":
            if not isinstance(value, int) or value <= 0:
                raise TypeError('неверный тип аргумента')
        return super().__setattr__(name, value)


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons) -> None:
        super().__init__(model, mass, speed, top)
        self._weapons = weapons

    def __setattr__(self, name, value) -> None:
        if name == "_weapons":
            if not isinstance(value, dict):
                raise TypeError('неверный тип аргумента')
        return super().__setattr__(name, value)


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]