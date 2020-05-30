
class Output:

    def __init__(self):
        self.output = []

    def eventHandler(self, eventType, payload):
        if eventType == "OUTPUT_TABLE":
            return self.show(payload)

    def dispatchEvent(self, eventType, payload):
        return eventType, payload
    
    def show(self, table):
        for i in table:
            print("Sequência:", i[0]  + " "*(20-len(i[0])), "Ocorrências:", str(i[1]) + " "*(10-len(str(i[1]))), "Linhas:", i[2])