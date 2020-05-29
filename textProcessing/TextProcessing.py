from Classificator import *
from Delimiter import *
from Agregator import *
from Sorter import *
from Output import *

class TextProcessing:
    
    def __init__(self, filePath):

        self.crossReferenceTable = []
        self.char = ""
        self.word = ""
        self.data = []
        self.step = 0
        self.event = ""

        self.classificator = Classificator(filePath)
        self.delimiter = Delimiter(self.classificator)
        self.agregator = Agregator(self.delimiter)
        self.sorter = Sorter(self.agregator)
        self.output = Output()

    def enventHandler(self, eventType):

        if eventType == "START":
            self.crossReferenceTable = self.dispatchEvent("GET_CROSS_REFERENCE_TABLE", 0)
            self.dispatchEvent("OUTPUT_TABLE", self.crossReferenceTable)
    
    def dispatchEvent(self, eventType, payload):
        if eventType == "GET_CROSS_REFERENCE_TABLE":
            return self.sorter.eventHandler(eventType)
        elif eventType == "OUTPUT_TABLE":
            return self.output.eventHandler(eventType, payload)

        
