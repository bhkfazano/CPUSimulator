from memory.Memory import *

class Loader:

    def __init__(self, memory):

        self.memory = memory

    def load(self, loader):
        insert = []
        for i in range(len(loader)):
            if i < 3:
                insert.append(loader[i][0])
            elif len(loader[i][0]) < 3:
                insert.append(loader[i][0][0:2])
            else:
                insert.append(loader[i][0][0:2])
                insert.append(loader[i][0][2:])
        add = int(insert[0] + insert[1], 16)

        for i in insert[3:]:
            self.memory.write(hex(add), i)
            add += 1
        self.memory.burn()
