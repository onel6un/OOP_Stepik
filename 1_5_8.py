class CPU():
    def __init__(self, name, fr) -> None:
        self.name = name
        self.fr = fr


class Memory():
    def __init__(self, name, volume) -> None:
        self.name = name
        self.volume = volume


class MotherBoard():
    def __init__(self, name, cpu, *mem_slots) -> None:
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = list(mem_slots)[:self.total_mem_slots]

    def _connectation(self, obj):
        return f'{obj.name}-{obj.volume};'

    def get_config(self):
        mem_conf = " ".join(map(self._connectation, self.mem_slots)).strip(';')
        return [
            f'Материнская плата: {self.name}',
            f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
            f'Слотов памяти: {self.total_mem_slots}',
            f'Память: {mem_conf}'
        ]


cpu1 = CPU('intel core i5', '3,6mhz')
mem1 = Memory('name1', '512')
mem2 = Memory('name1', '512')
mb = MotherBoard('mother', cpu1, mem1, mem2)
print(mb.get_config())