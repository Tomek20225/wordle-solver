import os.path
import re

# TODO: Try/Except when opening files
# TODO: Add saving a hash of the read dictionary for auto detection of changed dictionary vs. processed data in /temp

class FileHandler():
    def __init__(self, dictionary = None, reset = False):
        if dictionary is None:
            self.dict = "default.txt"
        else:
            self.dict = dictionary

        self.dictPath = "dictionaries/"
        self.tempPath = "temp/"
        
        self.pWords = "words-processed.txt"
        self.pExWords = "words-excluded.txt"
        self.pRanking = "words-processed-ranking.txt"
        self.pResults = "words-results.txt"

        self.bestFirstWord = ""

        if reset:
            self.parseDictionary()
        else:
            self.findBestFirstWord()

    def isCreated(self, path, filename):
        return os.path.isfile(path + filename)

    def getExcludedWords(self):
        excludedWords = []
        
        if not self.isCreated(self.dictPath, self.pExWords):
            return excludedWords

        list = open(self.dictPath + self.pExWords, "r", encoding="utf-8")

        for line in list:
            line = line.strip()
            if line:
                excludedWords.append(line)

        return excludedWords
    
    def parseDictionary(self):
        list = open(self.dictPath + self.dict, "r", encoding="utf-8")
        excludedWords = self.getExcludedWords()

        found = []
        foundLetters = []
        foundLettersCount = []
        for line in list:
            isInvalid = re.search("^\s*$", line)
            if isInvalid is not None:
                continue

            line = line.split()[0].strip().lower()

            isValid = re.search("^[^\s\d!-\/:-@[-`{-~]{5}$", line)
            # isValid = re.search("^[a-z]{5}$", line)
            if isValid is not None:
                if line not in found and line not in excludedWords:
                    found.append(line)
                else:
                    continue

                for letter in line:
                    if letter not in foundLetters:
                        foundLetters.append(letter)
                        foundLettersCount.append(1)
                    else:
                        foundLettersCount[foundLetters.index(letter)] += 1

        # TODO: Find a better way to rank words
        # For now the words are ranked by frequency of their individual letters in the parsed dictionary
        # In most cases that's good enough to solve a Wordle game in 4-5 tries, but the intention for the Solver is for it to be as efficient and effective as possible
        # Been thinking about popularity of the words in Google Search, but that will most likely be even less reliable
        letterRanking = []
        i = 0
        for letter in foundLetters:
            letterRanking.append((letter, foundLettersCount[i]))
            i += 1
        letterRanking.sort(key=lambda tup: tup[1], reverse=True)

        letterRankingFinal = []
        i = len(letterRanking)
        for letterTup in letterRanking:
            letterRankingFinal.append(letterTup[0] + "-" + str(i))
            i -= 1

        list.close()

        print(len(found))
        self.writeToFile(found, self.pWords)
        self.writeToFile(letterRankingFinal, self.pRanking)

        self.findBestFirstWord()

    def getLetterRanking(self):
        if not self.isCreated(self.tempPath, self.pRanking):
            self.parseDictionary()

        list = open(self.tempPath + self.pRanking, "r", encoding="utf-8")
        letterRanking = []

        for line in list:
            line = line.strip()
            if line:
                line = line.split("-")
                letterRanking.append((line[0], int(line[1])))

        list.close()
        return letterRanking

    def getProcessedWords(self):
        if not self.isCreated(self.tempPath, self.pWords):
            self.parseDictionary()

        list = open(self.tempPath + self.pWords, "r", encoding="utf-8")
        words = []

        for line in list:
            line = line.strip()
            if line:
                words.append(line)
        
        list.close()
        return words
    
    def findBestFirstWord(self):
        list = self.getProcessedWords()
        ranking = self.getLetterRanking()

        max = 5
        while self.bestFirstWord == "":
            bestLetters = []
            for i in range(max):
                bestLetters.append(ranking[i][0])
            
            for line in list:
                isMatch = True
                for letter in line:
                    if letter not in bestLetters:
                        isMatch = False
                if isMatch == True:
                    if len(set(line)) == len(line):
                        self.bestFirstWord = line
                        break
            
            max += 1
    
    def writeToFile(self, tab, file):
        newList = open(self.tempPath + file, "w", encoding="utf-8")

        for word in tab:
            if word != tab[len(tab) - 1]:
                newList.write(word + "\n")
            else:
                newList.write(word)

        newList.close()

    def saveResults(self, results):
        parsedResults = []

        for result in results:
            parsedResults.append(result[0])

        self.writeToFile(parsedResults, self.pResults)