from memory.Memory import *

class Loader:

    def __init__(self, memory):

        self.memory = memory

    def load(self, loader):
        insert = []
        for i in range(len(loader)):
            if i < 3:
                insert.append(loader[i][0])
            else:
                insert.append(loader[i][0][0:2])
                insert.append(loader[i][0][2:])
        add = int(insert[0] + insert[1], 16)
        for i in insert[3:]:
            self.memory.write(hex(add), i)
            add += 1

    def test(self, loader):
        add = int(loader[0][0] + loader[1][0], 16)
        for i in range(0, len(loader), 2):
            if i < 6:
                continue
            else:
                self.memory.write(hex(add), loader[i - 3][0][0:2])
                self.memory.write(hex(add + 1), loader[i - 3][0][2:])
            add += 2
        self.memory.burn()

        return 1
