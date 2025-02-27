import re
from typing import List, Tuple
from .FileHandler import FileHandler
from .WordleLetter import WordleLetter
from .WordleWord import WordleWord


class WordleSolver:
    # TODO: Tighten data integrity

    def __init__(self, dictionary = None, reset_dictionary = False):
        # TODO: Normalize class variables; each of them works and behaves differently, but naming is similar
        self.words: List[WordleWord] = []
        self.mis_letters: List[List[str]] = [[], [], [], [], []]
        self.wrong_letters: List[str] = []
        self.correct_letters = WordleWord([
            WordleLetter("", -1),
            WordleLetter("", -1),
            WordleLetter("", -1),
            WordleLetter("", -1),
            WordleLetter("", -1)
        ])
        self.fh = FileHandler(dictionary, reset_dictionary)
    
    def add_guess(self, word: WordleWord) -> None:
        self.words.append(word)

        # TODO: Extend checking
        # For instance, in Wordle if a given word has only one letter 'r' and the user puts in a word with two 'r',
        # then only one of them will be labeled as misplaced (0) or correct (1) - the rest is going to be wrong (-1),
        # which would break the script at it's current state
        i = 0
        for w_letter in word.letters:
            if w_letter.match == 1 and not self.correct_letters.letters[i].letter:
                self.correct_letters.letters[i] = w_letter
            elif w_letter.match == 0 and w_letter.letter not in self.mis_letters[i]:
                self.mis_letters[i].append(w_letter.letter)
            elif w_letter.match == -1 and w_letter.letter not in self.wrong_letters:
                self.wrong_letters.append(w_letter.letter)
            i += 1

    def get_best_first_word(self) -> str:
        return self.fh.best_first_word
    
    def _get_regexp(self) -> str:
        reg = ""
        wrong_letters_str = "".join(self.wrong_letters)

        for i in range(5):
            if self.correct_letters.letters[i].match == 1:
                reg += self.correct_letters.letters[i].letter
            elif len(self.mis_letters[i]) > 0:
                # TODO: Check if there are only unique letters in the joined string
                reg += "[^" + "".join(self.mis_letters[i]) + wrong_letters_str + "]"
            else:
                reg += "[^" + wrong_letters_str + "]"

        return reg

    def _get_missed_letters(self) -> List[str]:
        mis_letters: List[str] = []
        for letters in self.mis_letters:
            for letter in letters:
                if letter not in mis_letters:
                    mis_letters.append(letter)
        return mis_letters

    def _get_guesses(self) -> List[Tuple[str, int]]:
        list = self.fh.get_processed_words()
        results: List[str] = []

        for line in list:
            is_valid = re.search(self._get_regexp(), line)

            if is_valid is None:
                continue

            # TODO: Maybe this could also be implemented as a lookahead within the first regex check?
            for letter in self._get_missed_letters():
                if letter not in line:
                    is_valid = None
                    break

            if is_valid is not None:
                results.append(line)

        letter_ranking = dict(self.fh.get_letter_ranking())
        word_ranking: List[Tuple[str, int]] = []
        for word in results:
            sum = 0

            for letter in word:
                sum += letter_ranking[letter]

            word_ranking.append((word, sum))
        word_ranking.sort(key=lambda tup: tup[1], reverse=True)

        self.fh.save_results(word_ranking)
        return word_ranking

    def get_best_guess(self) -> Tuple[str, int]:
        try:
            return self._get_guesses()[0]
        except:
            print("No results found")