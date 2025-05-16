from abc import ABC, abstractmethod


# Product
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}, GPU: {self.gpu}"


# Builder Interface
class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self): pass

    @abstractmethod
    def set_ram(self): pass

    @abstractmethod
    def set_storage(self): pass

    @abstractmethod
    def set_gpu(self): pass

    @abstractmethod
    def get_computer(self): pass


# Concrete Builder: Gaming PC
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self):
        self.computer.cpu = "Intel i9"

    def set_ram(self):
        self.computer.ram = "32GB"

    def set_storage(self):
        self.computer.storage = "1TB SSD"

    def set_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"

    def get_computer(self):
        return self.computer


# Concrete Builder: Office PC
class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self):
        self.computer.cpu = "Intel i5"

    def set_ram(self):
        self.computer.ram = "16GB"

    def set_storage(self):
        self.computer.storage = "512GB SSD"

    def set_gpu(self):
        self.computer.gpu = "Integrated Graphics"

    def get_computer(self):
        return self.computer


# Director (optional)
class Director:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def build_computer(self):
        self.builder.set_cpu()
        self.builder.set_ram()
        self.builder.set_storage()
        self.builder.set_gpu()
        return self.builder.get_computer()


# Client code
def client():
    # Build a Gaming PC
    gaming_builder = GamingComputerBuilder()
    director = Director(gaming_builder)
    gaming_pc = director.build_computer()
    print("Gaming PC:")
    print(gaming_pc)

    # Build an Office PC
    office_builder = OfficeComputerBuilder()
    director = Director(office_builder)
    office_pc = director.build_computer()
    print("\nOffice PC:")
    print(office_pc)


if __name__ == "__main__":
    client()
