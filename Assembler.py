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
            if len(line) > 0 and (line[0] in self.mnemonic or line[0] in self.pseudo):
                line.insert(0, False)

        self.instructions = lines

    def buildSymbolsTable(self):

        instr = self.instructions
        
        for i in instr:
            if len(i) == 1:

                self.symbolsTable[i[0]] = {
                    "defined" : True, 
                    "address" : hex(self.CI),
                    "value"   : ""
                }

            elif i[1] not in self.mnemonic and i[1] not in self.pseudo:
                raise Exception('[Error] Invalid instruction: {}'.format(i[1]))
            elif i[1] == "@":
                self.CI = int(i[2].split("/")[1], 16)
            elif i[1] == "#":
                self.step = 2
                self.CI = 0
                return
            else:
                if i[0] and i[0] not in self.symbolsTable:

                    value = False
                    if "/" in i[2]:
                        value = i[2].split("/")[1]
                    self.symbolsTable[i[0]] = {
                        "defined" : True, 
                        "address" : hex(self.CI),
                        "value"   : value or i[2]
                    }

                    if not i[2].isdecimal() and "/" not in i[2]:
                        
                        self.symbolsTable[i[2]] = {
                            "defined" : False, 
                            "address" : "",
                            "value"   : ""
                        }

                elif i[0] and i[0] in self.symbolsTable and not self.symbolsTable[i[0]]["defined"]:
                    
                    self.symbolsTable[i[0]] = {
                        "defined" : True, 
                        "address" : hex(self.CI),
                        "value"   : i[2]
                    }

                    for j in self.symbolsTable:
                        if self.symbolsTable[j]["value"] == i[0]:
                            self.symbolsTable[j]["value"] = hex(self.CI)

                elif not i[0]:
                    
                    if not i[2].isdecimal() and "/" not in i[2]:
                        if i[2] in self.symbolsTable:
                            if not self.symbolsTable[i[2]]["defined"]:
                                self.symbolsTable[i[2]] = {
                                    "defined" : False, 
                                    "address" : "",
                                    "value"   : ""
                                }
                        else:
                            self.symbolsTable[i[2]] = {
                                "defined" : False, 
                                "address" : "",
                                "value"   : ""
                            }

                else:
                    raise Exception('[Error] Double definition of value: {}'.format(i[0]))
                if i[1] in self.pseudo and i[1] == "K":
                    self.CI = self.CI + 1
                else:
                    self.CI = self.CI + 2
        self.CI = 0
        self.step = 2

    def assemble(self, filePath):
        self.reset()
        self.getInstructionsList(filePath)
        self.buildSymbolsTable()
        
        block = []
        instr = self.instructions
        for i in instr:
            if len(i) > 1 and i[1] == "#":
                self.objectCode.append(block)
                self.store(filePath)
                return self.objectCode
            elif len(i) > 1 and i[1] == "@":
                if len(block) != 0:
                    self.objectCode.append(block)
                block = []
                self.CI = int(i[2].split("/")[1], 16)

            elif len(i) > 1 and i[1] == "K":
                operand = i[2]
                if len(i[2]) == 1:
                    operand = "0" + i[2]
                block.append([hex(self.CI).split("x")[1], operand[-2:]])
                self.CI = self.CI + 2

            elif len(i) > 1 and i[1] in self.mnemonic:
                
                operation = i[1]
                operand = i[2]
                if "/" in operand:
                    operand = hex(int(operand.split("/")[1], 16))

                elif not operand.isdecimal():
                    operand = self.symbolsTable[operand]["address"]
                elif operand.isdecimal():
                    operand = hex(int(operand, 16))
                
                operand = self.validateOperand(self.mnemonic[i[1]]["operand"], operand)
                #print(i[0], operation, operand)

                instruction = self.mnemonic[i[1]]["code"] + operand.split("x")[1]
                block.append([hex(self.CI).split("x")[1], instruction])
                self.CI += self.mnemonic[i[1]]["size"]
      
        self.store(filePath)
        return self.objectCode

    def validateOperand(self, type, operand):
        if type == "address":
            if len(operand) > 5:
                raise Exception('[Error] Address should be 12 bits: {}'.format(address))
            elif len(operand) == 3:
                operand = "0x" + "00" + operand.split("x")[1]
            elif len(operand) == 4:
                
                operand = "0x" + "0" + operand.split("x")[1]
        if type == "8bit":
            operand = "0x" + "0" + operand[-2:]
        elif type == "null":
            operand = "0x000"
        return operand

    def reset(self):

        self.objectCode = []
        self.mnemonic = mnemonic
        self.pseudo = pseudo
        self.symbolsTable = {}
        self.instructions = []
        self.CI = 0
        self.step = 1
        self.mounted = False

    def store(self, filePath):
        fileName = filePath[:-3] + "hex"
        file = open(fileName, 'w')

        for block in self.objectCode:
            metadata = self.parseAddress(block.copy()[0][0])
            metadata.append(hex(len(block)).split("x")[1])
            for i in metadata:
                file.write(i + "\n")   

            for i in block:
                file.write(i[1] + "\n")
            file.write("x" + "\n")
        file.close()

    def parseAddress(self, add):
        if len(add) == 1:
            add = "000" + add
        elif len(add) == 2:
            add = "00" + add
        elif len(add) == 3:
            add = "0" + add
        return [add[0:2], add[2:]]