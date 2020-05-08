class Memory:

    def __init__(self):

        file = open('./memory/memory.txt', 'w')
        for i in range (4096):
            file.write(hex(i) + "    " + "00\n")
        file.close()

        file = open('./memory/memory.txt', 'r')
        self.mem = dict(line.split() for line in file)

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
        print("MM: ", address, insert)
        self.mem[address]  = insert
        return 1

    def burn(self):
        file = open('./memory/memory.txt', 'w')
        for i in range(4069):
            file.write(hex(i) + "    " + self.mem[hex(i)] + "\n")

    def store(self):
    
        file = open('./memory/memory.txt', 'r')
        self.mem = dict(line.split() for line in file)

