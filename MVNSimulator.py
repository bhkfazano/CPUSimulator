from Loader import *
from Assembler import *
from memory.Memory import *

class MVNSimulator:

    def __init__(self):

        self.memory = Memory()
        self.loader = Loader(self.memory)
        self.assembler = Assembler()
        self.CI = 0    # 12 bits
        self.ACC = 0   # 8 bits

    def start(self):

        objectCode = self.assemble('./userFiles/loader.asm')
        file = open('./userFiles/loader.hex', 'r')
        lines = [line[:-1].split() for line in file]
        self.loader.load(lines)
        self.memory.burn()


    def assemble(self, path):

        objectCode = self.assembler.assemble(path)
        return objectCode
    