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
        self.wordlist = {}
        self.payload = []
        self.eventStack = ["GET_CHAR"]
        self.run = True

        self.classificator = Classificator(filePath)
        self.delimiter = Delimiter()
        self.agregator = Agregator()
        self.sorter = Sorter()
        self.output = Output()

    def engine(self):

        while self.run == True:
            nextEvent = self.eventStack[-1]
            del self.eventStack[-1]
            res = self.eventHandler(nextEvent)

    def eventHandler(self, eventType):

        if eventType == "GET_CHAR":
            nextEvent, self.char = self.classificator.eventHandler(eventType)
            self.eventStack.append(nextEvent)

        if eventType == "GET_WORDS":
            nextEvent, res = self.delimiter.eventHandler(eventType, self.char)
            self.eventStack.append(nextEvent)
            self.word = res
            
        if eventType == "GET_WORD_LIST":
            nextEvent, res = self.agregator.eventHandler(eventType, self.word)
            self.eventStack.append(nextEvent)
            self.wordlist = res

        if eventType == "GET_CROSS_REFERENCE_TABLE":
            nextEvent, res = self.sorter.eventHandler(eventType, self.wordlist)
            self.eventStack.append(nextEvent)
            self.crossReferenceTable = res
            
        if eventType == "OUTPUT_TABLE":
            self.output.eventHandler(eventType, self.crossReferenceTable)
            self.run = False