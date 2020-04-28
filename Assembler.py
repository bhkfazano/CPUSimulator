from constants import *

class Assembler:

    def __init__(self):

        self.objectCode = []
        self.mnemonic = mnemonic
        self.pseudo = pseudo
        self.symbolsTable = {}
        self.instructions = []
        self.CI = 0
        self.step = 1
        self.mounted = False

    # Remove comments in lines
    def removeComments(self, line):

        for i in line:
            if line[i] == ";":
                return line[0:i]
        return line

    # Get list of instructions. Each instruction is [label, mnemonic, value]
    def getInstructionsList(self, filePath):

        file = open(filePath, 'r')
        lines = [line.split() for line in file]

        for line in lines:
            if len(line) < 3:
                line.insert(0, False)

        self.instructions = lines

    def buildSymbolsTable(self):

        instr = self.instructions

        for i in instr:
            if i[1] not in self.mnemonic and i[1] not in self.pseudo:
                raise Exception('[Error] Invalid instruction: {}'.format(i[1]))
            elif i[1] == "@":
                self.CI = int(i[2].split("/")[1], 16)
            elif i[1] == "#":
                self.step = 2
                self.CI = 0
                return
            else:
                if i[0]:
                    if i[0] not in self.symbolsTable:
                        value = ""
                        if not i[2].isalpha() and not i[2].lower().islower():
                            value = "0x" + i[2]

                        self.symbolsTable[i[0]] = {
                            "defined" : True, 
                            "address" : hex(self.CI),
                            "value"   : value or i[2]
                        }
                    else:
                        raise Exception('[Error] Double definition of value: {}'.format(i[0]))
                self.CI = self.CI + 2
        self.CI = 0
        self.step = 2

    def assemble(self):
        
        instr = self.instructions

        for i in instr:
            if i[1] == "#":
                print("Montagem finalizada")
                return self.objectCode
            elif i[1] == "@":
                self.CI = int(i[2].split("/")[1], 16)
            elif i[1] in self.mnemonic:
                instruction = "0x" + self.mnemonic[i[1]]["code"]
                operand = 0
                if i[2] in self.symbolsTable:
                    operand = self.symbolsTable[i[2]]["value"]
                    if operand in self.symbolsTable:
                        operand = self.symbolsTable[operand]["value"]
                    if len(operand.split("x")[1]) > 3:
                        print(operand)
                        raise Exception('[Error] Operand cannot have more than 12 bits')  
                else:
                    operand = i[2].split("/")[1]
                    if len(operand) > 3:
                        if operand[0] == "0":
                            operand = operand[1:]
                        else:
                            raise Exception('[Error] Operand cannot have more than 12 bits')  
                    operand = "0x" + operand
                if len(operand) == 4:
                    operand = "0x0" + operand.split("x")[1]
                instruction = instruction + operand.split("x")[1]
                self.objectCode.append([hex(self.CI), instruction])
                self.CI += self.mnemonic[i[1]]["size"]

        return self.objectCode



a = Assembler()
a.getInstructionsList('./userFiles/test.asm')
a.buildSymbolsTable()
c = a.assemble()
print(c)
