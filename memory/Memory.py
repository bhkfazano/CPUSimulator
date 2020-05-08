class Memory:

    def __init__(self):

        file = open('./memory/memory.txt', 'w')
        for i in range (4096):
            file.write(hex(i) + "    " + "00\n")
        file.close()

        file = open('./memory/memory.txt', 'r')
        self.mem = dict(line.split() for line in file)
        file.close()

    def readInstruction(self, address):
        address  = hex(int(address, 16))
        address2 = hex(int(address, 16) + 1)
        data = self.mem[address] + self.mem[address2]
        return data

    def readByte(self, address):
        address  = hex(int(address, 16))
        data = self.mem[address]
        return data


    def write(self, address, insert):
        self.mem[hex(int(address, 16))]  = insert
        #print("MMW: ", hex(int(address, 16)), insert, self.mem[hex(int(address, 16))])
        return 1

    def burn(self):
        file = open('./memory/memory.txt', 'w')
        for i in range(4069):
            file.write(hex(i) + "    " + self.mem[hex(i)] + "\n")

    def store(self):
    
        file = open('./memory/memory.txt', 'r')
        self.mem = dict(line.split() for line in file)

