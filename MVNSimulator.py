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
        self.output = []

    def start(self):

        objectCode = self.assemble('./userFiles/loader.asm')
        file = open('./userFiles/loader.hex', 'r')
        lines = [line[:-1].split() for line in file]
        lines.remove(["||"])
        self.loader.load(lines)
        self.memory.store()


    def assemble(self, path):

        objectCode = self.assembler.assemble(path)
        return objectCode

    def init(self, path):
        
        file = open('./userFiles/' + path, 'r')
        lines = [line.split()[0] for line in file]
        block = []
        insert = []

        for i in lines:
            if i != "||":
                block.append(i)
            else:
                insert.append(block)
                block = []

        return insert

    def load(self, program):
        op = ""
        counter = 0
        self.CI = 0
        while True:
            
            instr = self.memory.readInstruction(hex(self.CI))
            #print("CI | instr | ACC : ", hex(self.CI), instr, hex(self.ACC), program[counter])
            if counter == len(program):
                self.CI = 0
                break
            if instr[0] == "D":
                self.handleInstruction(instr, program[counter])
                counter += 1
                if counter == len(program):
                    self.CI = 0
                    break
            else:
                self.handleInstruction(instr, 0)   

        
    def run(self, path):
        self.output = []
        program = self.init(path)

        for i in program:
            self.load(i)
        self.memory.burn()
        self.CI = int(program[0][0] + program[0][1], 16)
        self.ACC = 0
        while True:
            instr = self.memory.readInstruction(hex(self.CI))
            #print("DEBUG:   ", "Instr: ", instr, "ACC: ", hex(self.ACC), "CI: ", hex(self.CI))
            if instr[0] == "F" or instr[0] == "f":
                self.CI = 0
                break
            self.handleInstruction(instr, 0) 
        
        print("ACC: ", self.ACC)
        print("Output: ", self.output)
        self.store()

    def jump(self, add):
        self.CI = int(add, 16)
    
    def jumpIfZero(self, add):
        if self.ACC == 0:
            self.CI = int(add, 16)
        else:
            self.CI += 2

    def jumpIfNegative(self, add):
        if self.ACC < 0:
            self.CI = int(add, 16)
        else:
            self.CI += 2

    def loadValue(self, value):
        self.ACC = int(value, 16)
        self.CI += 2

    def addition(self, add):
        self.ACC = self.ACC + int(self.memory.readByte(add)[-2:], 16)
        self.CI += 2

    def sub(self, add):
        self.ACC -= int(self.memory.readByte(add)[-2:], 16)
        self.CI += 2

    def mult(self, add):
        self.ACC *= int(self.memory.readByte(add)[0:2], 16)
        self.CI += 2

    def div(self, add):
        self.ACC = self.ACC//int(self.memory.readByte(add)[0:2], 16)
        self.CI += 2

    def loadMM(self, add):
        self.ACC = int(self.memory.readByte(add), 16)
        self.CI += 2

    def storeMM(self, add):
        self.memory.write(add, self.parseByte(hex(self.ACC).split("x")[1]))
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
        self.memory.burn()
        option = ""
        print("STATUS: ")
        print("NUSP + CODIGO: ")
        aux = 1536
        end = 1536 + 16
        while aux != end:
            print(self.memory.readByte(hex(aux)), " ", end = " ")
            aux += 1
        option = input("\n MVNSimulator $ Pressione qualquer tecla + enter para continuar: ")
        while len(option) == 0:
            continue
        self.CI = int(add, 16)

    def getData(self, value):
        self.ACC = int(value, 16)
        self.CI += 2

    def putData(self):
        self.output.append(hex(self.ACC).split("x")[1])
        self.CI += 2

    def osCall(self):
        self.CI += 2

    def handleInstruction(self, instr, value):
        opcode = instr[0]
        if opcode == "0":
            self.jump(instr[1:])
        elif opcode == "1":
            self.jumpIfZero(instr[1:])
        elif opcode == "2":
            self.jumpIfNegative(instr[1:])
        elif opcode == "3":
            self.loadValue(instr[2:])
        elif opcode == "4":
            self.addition(instr[1:])
        elif opcode == "5":
            self.sub(instr[1:])
        elif opcode == "6":
            self.mult(instr[1:])
        elif opcode == "7":
            self.div(instr[1:])
        elif opcode == "8":
            self.loadMM(instr[1:])
        elif opcode == "9":
            self.storeMM(instr[1:])
        elif opcode.upper() == "A":
            self.srCall(instr[1:])
        elif opcode.upper() == "B":
            self.srReturn(instr[1:])
        elif opcode.upper() == "C":
            self.halt(instr[1:])
        elif opcode.upper() == "D":
            self.getData(value)
        elif opcode.upper() == "E":
            self.putData()
        elif opcode.upper() == "F":
            self.osCall()



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
    
    def parseByte(self, byte, left=False):
        if len(byte) == 1:
            if left:
                return byte + "0"
            else:
                return "0" +  byte
        return byte

    def store(self):
        file = open("output.hex", 'w')

        for line in self.output:
            file.write(line + "\n") 
        file.close()

