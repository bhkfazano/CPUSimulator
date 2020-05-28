from Classificator import *

class Delimiter:

    def __init__(self, classificator):
        self.word = ""
        self.data = ["", "", False]
        self.classificator = classificator
    
    def delimit(self):

        self.data = ["", "", False]
        while True:
        
            char = self.classificator.extract()
            if char == False:
                return False
            if char[1] == False:
                # if len(self.word) == 0:
                #     self.word = char[0]
                self.data[0] = char[3]
                self.data[1] = self.word.lower()
                data = self.data
                self.word = ""
                return self.data
            else:
                if char[2] == True:
                    self.data[2] = True
                self.word += char[0]