
class Agregator:

    def __init__(self, delimiter):
        self.delimiter = delimiter
        self.wordlist = {}

    def eventHandler(self, eventType):
        if eventType == "GET_WORD_LIST":
            return self.agregate()

    def dispatchEvent(self, eventType):
        return self.delimiter.eventHandler(eventType)
    
    def agregate(self):
        
        while True:
            word = self.dispatchEvent("GET_WORDS")
            if word == False:
                break
            if word[2] == True:
                word[0] = str(word[0]) + "*"
            else:
                word[0] = str(word[0])
            if word[1] != '' and word[1] not in self.wordlist:
                self.wordlist[word[1]] = [1, word[2], [word[0]]]
            elif word[1] in self.wordlist:
                temp = self.wordlist[word[1]]
                temp[0] += 1
                temp[2].append(word[0])
                self.wordlist[word[1]] = temp

        return self.wordlist