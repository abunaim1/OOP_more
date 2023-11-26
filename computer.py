# inheritance vs comppsition
class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores
    
class RAM:
    def __init__(self, size) -> None:
        self.size = size

class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity

#computer has a CPU
#computer has a RAM
#computer has a hardDrive
class Computer:
    def __init__(self, cores, ram_size, disk_capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hardDrive = HardDrive(disk_capacity)

c1 = Computer(4, 32, '1T')
