class WordleLetter:
    # TODO: Zabezpieczajki, private, gettery, settery
    
    def __init__(self, letter, match):
        self.letter = letter
        self.match = match

    def __str__(self):
        return self.letter