# Wordle Solver

Solver for Wordle and it's equvalents written in Python.



## How does it work?

The logic is quite simple:
**Once the word is added to the Solver, it generates a regular expression that describes the rules for finding words that comply with the game's requirements**. Then it suggests the best word to try out next. When other words are added, the expression is updated and extended, and by doing so it narrows down the list of plausible words.

**The best word for the current iteration is based on the score of the word**:
During processing of the dictionary, the script also counts the occurrences of each letter within it. Each letter is assigned a score, with the most frequent letter having the highest score. Then for each plausible word a score is calculated as the sum of the scores of its letters. The word with the highest score is considered to be the best.

**The script also suggests the first guess.** After processing of the dictionary, it searches for the word that has the highest amount of most frequent letters. That approach maximizes the chances of getting as many correct or misplaced letters as possible.

**Usually 3-5 tries are needed to win the game** *(at least in original Wordle)*, but the effectiveness is highly based on the first guess.



## How to use it?

The script doesn't autoplay Wordle *at the moment* and it doesn't have a CLI. You have to edit the script every time you want to get another guess.

1. Clone the repository.
2. Edit `wordle.py`:
   1. The `WordleSolver` accepts two parameters: the dictionary file name and a boolean implying whether you want to process the dictionary again or use the previously generated files. **In the first run you have to generate the files.**
   2. When you run the script for the first time, it'll print the first suggested word to put in the game. You may use that suggestion or put in the word you prefer - *the choice is yours*.
   3. Once you have an answer from Wordle or it's equivalent, you create a `WordleWord` variable, which requires an array of 5 `WordleLetter` objects. Each `WordleLetter` object requires a character and it's score (`1` for the correct placement of the letter, `0` for the correct letter but wrong placement and `-1` for wrong letter). **The order of `WordleLetter` objects in an array meant for `WordleWord` is important.**
   4. Then you add it to the Solver by using `add_guess` method. At last, you print out the quess with `get_best_guess` method.
   5. Repeat steps 2.3 and 2.4 until you win!

And please remember to ***read comments in the script***.



## Is my language supported?

Any language is supported by the program if it's dictionary can be found in `dictionaries` directory.

The requirements for the dictionary to be parsed without issues are:

1. The file should be in a raw format, like .txt
2. There is only one word intended to be parsed in each line. There can be multiple words in line, but only the first one will be read.

By default, Solver has 2 good dictionaries included - for English (the default language) and for Polish.



## Can I contribute?

Yes, of course! Any help is welcome.

This project was originally made purely: for fun, to learn Python better (since I've never used it before) and to get good at data processing. I am also passionate about Open Source Software and always wanted to contribute to the community. Creating this is project is my way of doing these things at once.

The major steps I've planned for the project are to:

- [x] Create a dictionary parser
- [x] Create a Solver that guesses based on a single word
- [x] Extend the Solver to guess based on multiple words
- [x] Make it #OOP
- [ ] Tighten data integrity in classes
- [ ] Find a better way to rank words in results
- [ ] Refactor and normalize the code
- [ ] Create a CLI
- [ ] Create a GUI
- [ ] Create a computer-vision bot to play the game by itself

If you are in a position similar to mine or you simply feel you could help in pushing the project further, then feel free to give a hand! And remember - have fun!



## Project structure

    .
    ├── wordle.py               # The main script
    ├── libs                    # Classes and handlers for the script
    │   ├── FileHandler.py      # Handles file read/write operations
    │   ├── WordleLetter.py     # Individual letter with its score
    │   ├── WordleWord.py       # Word built of WordleLetters
    │   ├── WordleSolver.md     # The main Solver logic
    ├── dictionaries            # Directory with dictionaries meant for parsing
    │   ├── default.txt         # Default English dictionary
    │   ├── words-excluded.txt  # Words that are in dictionaries, but not in Wordle
    │   ├── en.txt              # Same as default
    │   ├── en2.txt             # Another English dictionary (not as good)
    │   ├── pl.txt              # Polish dictionary
    │   └── ...                 # other dictionaries (TBA)
    ├── temp                    # Dictionary for temporary files with results of parsing
    │   ├── words-processed.txt # Processed dictionary for further reading
    │   ├── words-processed-ranking.txt  # Letter frequency ranking
    │   ├── word-results.txt    # Results of the current search



## Credits

- @github/sujithps [for the default dictionary used in the Solver](https://github.com/sujithps/Dictionary/) 
- @github/dwyl [for the backup English word list](https://github.com/dwyl/english-words)
- [sjp.pl](https://sjp.pl/slownik/growy/) for Polish dictionary



Thanks for stopping by! **Have a nice day and good luck! :heartpulse::sparkles:**

Please let me know what you think about the code! It helps a lot!