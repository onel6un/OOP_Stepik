import time


class DeltaClock:
    def __init__(self, clock1, clock2) -> None:
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        return time.strftime("%H: %M: %S", time.gmtime(time.mktime(self.clock1.time) - time.mktime(self.clock2.time)))


class Clock:
    def __init__(self, hours, minutes, seconds) -> None:
        self.time = time.strptime(f'{hours}: {minutes}: {seconds}', "%H: %M: %S")


cl = DeltaClock(Clock(10, 10, 30), Clock(10, 10, 20))
#print(str(cl))
cl = Clock(0, 0, 30)
cl2 = Clock(0, 0, 20)
print(cl.time-cl2.time)