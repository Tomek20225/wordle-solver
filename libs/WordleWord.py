class WordleWord:
    # TODO: Zabezpieczajki, private, gettery, settery

    def __init__(self, letters):
        self.letters = letters

    def __str__(self):
        str = ""
        for wLetter in self.letters:
            str += wLetter.letter
        return str

    def getLettersWithStatus(self, statusNum):
        letters = []
        for wLetter in self.letters:
            if wLetter.match == statusNum:
                letters.append(wLetter.letter)
        return letters