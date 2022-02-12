import re
from .FileHandler import FileHandler
from .WordleLetter import WordleLetter
from .WordleWord import WordleWord


class WordleSolver:
    # TODO: Tighten data integrity
    # TODO: Add getters and setters

    def __init__(self, dictionary = None, reset = False):
        # TODO: Normalize class variables; each of them works and behaves differently, but naming is similar
        self.words = []
        self.misLetters = [
            [],
            [],
            [],
            [],
            []
        ]
        self.wrongLetters = []
        self.correctLetters = WordleWord([
            WordleLetter("", -1),
            WordleLetter("", -1),
            WordleLetter("", -1),
            WordleLetter("", -1),
            WordleLetter("", -1)
        ])
        self.fh = FileHandler(dictionary, reset)
    
    def addGuess(self, word):
        self.words.append(word)

        # TODO: Extend checking
        # For instance, in Wordle if a given word has only one letter 'r' and the user puts in a word with two 'r', then only one of them will be labeled as misplaced (0) or correct (1) - the rest is going to be wrong (-1), which would break the script at it's current state
        i = 0
        for wLetter in word.letters:
            if wLetter.match == 1 and not self.correctLetters.letters[i].letter:
                self.correctLetters.letters[i] = wLetter
            elif wLetter.match == 0 and wLetter.letter not in self.misLetters[i]:
                self.misLetters[i].append(wLetter.letter)
            elif wLetter.match == -1 and wLetter.letter not in self.wrongLetters:
                self.wrongLetters.append(wLetter.letter)
            i += 1

    def getBestFirstWord(self):
        return self.fh.bestFirstWord
    
    def getRegExp(self):
        reg = ""
        wrongLettersStr = "".join(self.wrongLetters)

        for i in range(5):
            if self.correctLetters.letters[i].match == 1:
                reg += self.correctLetters.letters[i].letter
            elif len(self.misLetters[i]) > 0:
                # TODO: Check if there are only unique letters in the joined string
                reg += "[^" + "".join(self.misLetters[i]) + wrongLettersStr + "]"
            else:
                reg += "[^" + wrongLettersStr + "]"

        return reg

    def getMissedLetters(self):
        misLetters = []
        for letters in self.misLetters:
            for letter in letters:
                if letter not in misLetters:
                    misLetters.append(letter)
        return misLetters

    def getGuesses(self):
        list = self.fh.getProcessedWords()
        results = []

        for line in list:
            isValid = re.search(self.getRegExp(), line)

            if isValid is None:
                continue

            # TODO: Maybe this could also be implemented as a lookahead within the first regex check?
            for letter in self.getMissedLetters():
                if letter not in line:
                    isValid = None
                    break

            if isValid is not None:
                results.append(line)

        letterRanking = dict(self.fh.getLetterRanking())
        wordRanking = []
        for word in results:
            sum = 0

            for letter in word:
                sum += letterRanking[letter]

            wordRanking.append((word, sum))
        wordRanking.sort(key=lambda tup: tup[1], reverse=True)

        self.fh.saveResults(wordRanking)
        return wordRanking

    def getBestGuess(self):
        guess = ""
        try:
            guess = self.getGuesses()[0]
        except:
            print("No results found")
        return guess