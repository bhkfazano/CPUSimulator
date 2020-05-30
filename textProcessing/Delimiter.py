from Classificator import *

class Delimiter:

    def __init__(self):
        self.word = ""
        self.data = ["", "", False]

    def eventHandler(self, eventType, payload):
        if eventType == "GET_WORDS":
            return self.delimit(payload)
        
    def dispatchEvent(self, eventType, payload):
        return eventType, payload
    
    def delimit(self, char):
        if char == False:
            data = 0
            if self.word != "":
                self.data[1] = self.word.lower()
                data = self.data
                self.word = ""
                self.data = ["", "", False]
            return self.dispatchEvent("GET_WORD_LIST", data)
        if char[1] == False:
            self.data[0] = char[3]
            self.data[1] = self.word.lower()
            data = self.data
            self.word = ""
            self.data = ["", "", False]
            return self.dispatchEvent("GET_WORD_LIST", data)
        else:
            if char[2] == True:
                self.data[2] = True
            self.data[0] = char[3]
            self.word += char[0]
            return self.dispatchEvent("GET_CHAR", 0)