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
        self.memory.store()


    def assemble(self, path):

        objectCode = self.assembler.assemble(path)
        return objectCode

    def load(self, path):
        
        file = open('./userFiles/' + path, 'r')
        lines = [line.split()[0] for line in file]
    
        insert = []
        for i in range(len(lines)):
            if i < 3:
                insert.append(lines[i])
            else:
                insert.append(lines[i][0:2])
                insert.append(lines[i][2:])
        
        return insert

    def run(self, path):

        program = self.load(path)

    def jump(self, add):
        self.CI = int(add, 16)
    
    def jumpIfZero(self, add):
        if self.ACC == 0:
            self.CI = int(add, 49)
        else:
            self.CI += 2

    def jumpIfNegative(self, add):
        if self.ACC < 0:
            self.CI = int(add, 49)
        else:
            self.CI += 2

    def loadValue(self, value):
        self.ACC = int(value, 16)
        self.CI += 2

    def sum(self, add):
        self.ACC += int(self.memory.read(add), 16)
        self.CI += 2

    def sub(self, add):
        self.ACC -= int(self.memory.read(add), 16)
        self.CI += 2

    def mult(self, add):
        self.ACC *= int(self.memory.read(add), 16)
        self.CI += 2

    def div(self, add):
        self.ACC = self.ACC/int(self.memory.read(add), 16)
        self.CI += 2

    def loadMM(self, add):
        self.ACC = int(self.memory.read(add), 16)

    def storeMM(self, add):
        self.memory.write(hex(int(add, 16) + 1), hex(self.ACC))
        self.CI += 2

    def srCall(self, add):
        address = self.parseAddress(add)
        operand = self.parseCI(hex(self.CI + 2))
        self.memory.write(address[0], operand[0])
        self.memory.write(address[1], operand[1])
        self.CI = int(add, 16) + 2

    def srReturn(self, add):
        self.CI = int(add, 16)

    def halt(self, add):
        option = ""
        option = input("\n MVNSimulator $ Pressione qualquer tecla para continuar")
        while len(option) == 0:
            continue
        self.CI = int(add, 16)

    def getData(self, value):
        self.ACC = value
        self.CI += 2

    def putData(self):
        print(self.ACC)
        self.CI += 2

    def osCall(self):
        self.CI += 2

    def parseAddress(self, address):
        add = address
        if "x" in add:
            add = x.split("x")[1]
        if len(add) == 1:
            add = "000" + add
        elif len(add) == 2:
            add = "00" + add
        elif len(add) == 3:
            add = "0" + add
        return [add[0:2], add[2:]]
    
    def parseCI(self, ci):
        add = ci
        if "x" in add:
            add = x.split("x")[1]
        if len(add) == 1:
            return ["00", "0" + add]
        elif len(add) == 2:
            return ["00", add]
        elif len(add) == 3:
            return ["0" + add[0], add[-2:]]
        return [add[0:2], add [2:]]
    