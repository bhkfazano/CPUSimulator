
class Classificator:

    def __init__(self, filePath):

        self.text = ["TEXT"]
        self.counter = 1
        self.first = True

        file = open('../userFiles/' + filePath, 'r')
        self.file = [line for line in file]
        
        counter = 1
        for line in file:
            print(counter, line)
            counter += 1
    
    def extract(self):

        res = []
        if len(self.file) == 0:
            return False

        line = self.file[0]
        if len(line) > 0:
            first = self.first

            if first == True:
                self.first = False
                
            res = [line[0], line[0].isalpha(), first, self.counter]
            if len(self.file[0]) == 1:
                self.file = self.file[1:]
                self.counter += 1
                self.first = True
            else:
                self.file[0] = self.file[0][1:]
            return res