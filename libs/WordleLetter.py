class WordleLetter:
    # TODO: Tighten the class
    
    def __init__(self, letter: str, match: int):
        self.letter = letter
        self.match = match

    def __str__(self):
        return self.letter