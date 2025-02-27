from typing import List
from .WordleLetter import WordleLetter


class WordleWord:
    # TODO: Tighten the class

    def __init__(self, letters: List[WordleLetter]):
        self.letters = letters

    def __str__(self):
        str = ""
        for w_letter in self.letters:
            str += w_letter.letter
        return str

    def get_letters_with_status(self, status_num: int) -> List[str]:
        letters: List[str] = []
        for w_letter in self.letters:
            if w_letter.match == status_num:
                letters.append(w_letter.letter)
        return letters