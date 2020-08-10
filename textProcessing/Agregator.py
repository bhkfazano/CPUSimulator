
class Agregator:

    def __init__(self):
        self.wordlist = {}

    def eventHandler(self, eventType, payload):
        if eventType == "GET_WORD_LIST":
            return self.agregate(payload)
    
    def dispatchEvent(self, eventType, payload):
        return eventType, payload
    
    def agregate(self, word):
        if word == False:
            return self.dispatchEvent("GET_CROSS_REFERENCE_TABLE", self.wordlist)
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

        return self.dispatchEvent("GET_CHAR", 0)