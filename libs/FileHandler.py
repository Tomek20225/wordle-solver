import os.path
import re
from typing import List, Tuple
import os


# TODO: Try/Except when opening files
# TODO: Util for file reading and caching
# TODO: Add saving a hash of the read dictionary for auto detection of changed dictionary vs. processed data in /temp

class FileHandler():
    def __init__(self, dictionary = None, reset_dictionary = False):
        if dictionary is None:
            self.dict = "default.txt"
        else:
            self.dict = dictionary

        self.dict_path = "dictionaries/"
        self.temp_path = "temp/"
        
        self.processed_words_filename = "words-processed.txt"
        self.excluded_words_filename = "words-excluded.txt"
        self.ranking_filename = "words-processed-ranking.txt"
        self.results_filename = "words-results.txt"

        self.best_first_word = ""

        if not os.path.exists(self.temp_path):
            os.makedirs(self.temp_path)

        if reset_dictionary:
            self._parse_dictionary()
        else:
            self._find_best_first_word()

    def _is_created(self, path: str, filename: str) -> bool:
        return os.path.isfile(path + filename)

    def _get_excluded_words(self) -> List[str]:
        excluded_words: List[str] = []
        
        if not self._is_created(self.dict_path, self.excluded_words_filename):
            return excluded_words

        list = open(self.dict_path + self.excluded_words_filename, "r", encoding="utf-8")

        for line in list:
            line = line.strip()
            if line:
                excluded_words.append(line)

        return excluded_words
    
    def _parse_dictionary(self) -> None:
        list = open(self.dict_path + self.dict, "r", encoding="utf-8")
        excluded_words = self._get_excluded_words()

        found = []
        found_letters = []
        found_letters_count = []
        for line in list:
            if re.search(r"^\s*$", line):
                continue

            line = line.split()[0].strip().lower()

            if re.fullmatch(r"^[^\s\d\W]{5}$", line):
                if line not in found and line not in excluded_words:
                    found.append(line)
                else:
                    continue

                for letter in line:
                    if letter not in found_letters:
                        found_letters.append(letter)
                        found_letters_count.append(1)
                    else:
                        found_letters_count[found_letters.index(letter)] += 1

        # TODO: Find a better way to rank words
        # For now the words are ranked by frequency of their individual letters in the parsed dictionary
        # In most cases that's good enough to solve a Wordle game in 4-5 tries, but the intention for the Solver is for it to be as efficient and effective as possible
        # Been thinking about popularity of the words in Google Search, but that will most likely be even less reliable
        letter_ranking = []
        i = 0
        for letter in found_letters:
            letter_ranking.append((letter, found_letters_count[i]))
            i += 1
        letter_ranking.sort(key=lambda tup: tup[1], reverse=True)

        letter_ranking_final = []
        i = len(letter_ranking)
        for letter_tup in letter_ranking:
            letter_ranking_final.append(letter_tup[0] + "-" + str(i))
            i -= 1

        list.close()

        print(f"Found {len(found)} possible words")
        self._write_to_file(found, self.processed_words_filename)
        self._write_to_file(letter_ranking_final, self.ranking_filename)

        self._find_best_first_word()

    def get_letter_ranking(self) -> List[Tuple[str, int]]:
        if not self._is_created(self.temp_path, self.ranking_filename):
            self._parse_dictionary()

        list = open(self.temp_path + self.ranking_filename, "r", encoding="utf-8")
        letter_ranking: List[Tuple[str, int]] = []

        for line in list:
            line = line.strip()
            if line:
                line = line.split("-")
                letter_ranking.append((line[0], int(line[1])))

        list.close()
        return letter_ranking

    def get_processed_words(self) -> List[str]:
        if not self._is_created(self.temp_path, self.processed_words_filename):
            self._parse_dictionary()

        list = open(self.temp_path + self.processed_words_filename, "r", encoding="utf-8")
        words: List[str] = []

        for line in list:
            line = line.strip()
            if line:
                words.append(line)
        
        list.close()
        return words
    
    def _find_best_first_word(self) -> None:
        list = self.get_processed_words()
        ranking = self.get_letter_ranking()

        max = 5
        while self.best_first_word == "":
            best_letters = []
            for i in range(max):
                best_letters.append(ranking[i][0])
            
            for line in list:
                is_match = True
                for letter in line:
                    if letter not in best_letters:
                        is_match = False
                if is_match == True:
                    if len(set(line)) == len(line):
                        self.best_first_word = line
                        break
            
            max += 1
    
    def _write_to_file(self, tab: List[str], filename: str) -> None:
        new_list = open(self.temp_path + filename, "w", encoding="utf-8")

        for word in tab:
            if word != tab[len(tab) - 1]:
                new_list.write(word + "\n")
            else:
                new_list.write(word)

        new_list.close()

    def save_results(self, results: List[Tuple[str, int]]) -> None:
        parsed_results = []

        for result in results:
            parsed_results.append(result[0])

        self._write_to_file(parsed_results, self.results_filename)