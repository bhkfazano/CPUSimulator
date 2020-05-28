from Classificator import *
from Delimiter import *
from Agregator import *
from Sorter import *

class TextProcessing:
    
    def __init__(self, filePath):

        self.classificator = Classificator(filePath)
        self.delimiter = Delimiter(self.classificator)
        self.agregator = Agregator(self.delimiter)
        self.sorter = Sorter(self.agregator)
        
        self.req = ["", 0]
        self.res = ["", 0]

    def enventHandler(self, eventType, payload):

        if eventType == "GET_UNPROCESSED_CHAR":
            return self.sorter.sort()

        
