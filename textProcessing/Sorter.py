
class Sorter:

    def __init__(self, agregator):
        self.agregator = agregator
        self.data = []
    
    def eventHandler(self, eventType):
        if eventType == "GET_CROSS_REFERENCE_TABLE":
            return self.sort()

    def dispatchEvent(self, eventType):
        return self.agregator.eventHandler(eventType)
    
    def sort(self):

        wordlist = self.dispatchEvent("GET_WORD_LIST")

        for key, value in sorted(wordlist.items()):
            entry = [key, value[0], value[2]]
            self.data.append(entry)
        return self.data