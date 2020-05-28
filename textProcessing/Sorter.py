
class Sorter:

    def __init__(self, agregator):
        self.agregator = agregator
        self.data = []
    
    def sort(self):

        wordlist = self.agregator.agregate()

        for key, value in sorted(wordlist.items()):
            entry = [key, value[0], value[2]]
            self.data.append(entry)
        return self.data