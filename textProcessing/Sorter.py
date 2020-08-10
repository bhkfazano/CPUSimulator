
class Sorter:

    def __init__(self):
        self.data = []
    
    def eventHandler(self, eventType, payload):
        if eventType == "GET_CROSS_REFERENCE_TABLE":
            return self.sort(payload)

    def dispatchEvent(self, eventType, payload):
        return eventType, payload
    
    def sort(self, wordlist):

        for key, value in sorted(wordlist.items()):
            entry = [key, value[0], value[2]]
            self.data.append(entry)
        return self.dispatchEvent("OUTPUT_TABLE", self.data)