from abc import ABC , abstractmethod
# 1. Define a product

class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return (f"Computer Specifications: \n"
                f"CPU : {self.cpu} \n"
                f"GPU : {self.gpu} \n"
                f"RAM : {self.ram} \n"
                f"Storage: {self.storage}")


# 2. Define a Builder Interface


class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self,cpu):
        pass

    @abstractmethod
    def set_gpu(self,gpu):
        pass
    @abstractmethod
    def set_ram(self,ram):
        pass
    
    @abstractmethod
    def set_storage(self,storage):
        pass
    @abstractmethod
    def get_computer(self):
        pass


# 3. Define Concrete Builder

class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self,cpu):
        self.computer.cpu = cpu

    def set_gpu(self,gpu):
        self.computer.gpu = gpu
    def set_ram(self,ram):
        self.computer.ram = ram

    def set_storage(self,storage):
        self.computer.storage = storage

    def get_computer(self):
        return self.computer

class WorkstationComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self,cpu):
        self.computer.cpu = cpu

    def set_gpu(self,gpu):
        self.computer.gpu = gpu

    def set_ram(self,ram):
        self.computer.ram = ram 

    def set_storage(self,storage):
        self.computer.storage = storage

    def get_computer(self):
        return self.computer


# 4. Define the Director


class ComputerDirector:
    def __init__(self,builder):
        self.builder = builder

    def construct_gaming_computer(self):
        self.builder.set_cpu("Intel i9")
        self.builder.set_gpu("NVIDIA RTX 3080")
        self.builder.set_ram("32GB DDR4")
        self.builder.set_storage("1TB SSD")

    def construct_workstation_computer(self):
        self.builder.set_cpu("AMD Ryzen Threadripper")
        self.builder.set_gpu("NVIDIA Quadro RTX 8000")
        self.builder.set_ram("128GB DDR4")
        self.builder.set_storage("4TB NVMe SSD")



# 5. Client Code 


if __name__ == "__main__":

    #Create a buider for a gaming computer
    gaming_builder = GamingComputerBuilder()
    director = ComputerDirector(gaming_builder)
    director.construct_gaming_computer()
    gaming_computer = gaming_builder.get_computer()
    print("Gaming Computer:\n",gaming_computer)


    #Create a builder for a workstation computer

    workstation_builder = WorkstationComputerBuilder()
    director = ComputerDirector(workstation_builder)
    director.construct_workstation_computer()
    workstation_computer = workstation_builder.get_computer()
    
    print("\n Workstation Computer:\n",workstation_computer)
