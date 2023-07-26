class Track:
    def __init__(self, start_x=0, start_y=0):
        self.lst_trck = [(TrackLine(start_x, start_y))]

    def add_track(self, tr):
        self.lst_trck.append(tr)

    def get_tracks(self):
        return tuple(self.lst_trck)

    def _get_lenght_track(self):
        lenght = 0
        tuple = self.get_tracks()
        for i, tr in enumerate(tuple):
            if i == len(tuple) - 1:
                break
            lenght += ((tuple[i+1].to_x - tr.to_x)**2 + (tuple[i+1].to_y - tr.to_y)**2) ** 0.5
        return lenght

    def __len__(self):
        return int(self._get_lenght_track())

    def __eq__(self, other) -> bool:
        return len(self) == len(other)

    def __gt__(self, other):
        return len(self) > len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed=0):
        self.to_x = to_x if type(to_x) in (int, float) else None
        self.to_y = to_y if type(to_y) in (int, float) else None
        self.max_speed = max_speed if type(max_speed) == int else None


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
