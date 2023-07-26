class Player:
    def __init__(self, name, old, score) -> None:
        self.name = name
        self.old = old
        self.score = score

    def __setattr__(self, key, value):
        if (
            (key in ('old', 'score') and isinstance(value, int))
            or (key == 'name' and isinstance(value, str))
        ):
            super().__setattr__(key, value)

    def __bool__(self):
        return self.score > 0


lst_in = ['Балакирев; 34; 2048',
          'Mediel; 27; 0',
          'Влад; 18; 9012',
          'Nina P; 33; 0']

players = []

for l in lst_in:
    args = list(map(str.strip, l.split(';')))
    args[-1] = int(args[-1])
    args[-2] = int(args[-2])
    players.append(Player(*args))

players_filtered = list(filter(lambda x: bool(x), players))
