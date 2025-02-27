from libs.WordleLetter import WordleLetter
from libs.WordleWord import WordleWord
from libs.WordleSolver import WordleSolver


# TODO: Add CLI interface

# If you put in two identical letters as an answer (for instance: 'a'),
# and Wordle says that one of these letters is correct (1) or misplaced (0),
# then Wordle will label the second letter as wrong (-1).
# To not break the script, you should label the second letter as misplaced (0) and everything will work correctly

solver = WordleSolver(dictionary="default.txt", reset_dictionary=True)
print(f"Best first word: {solver.get_best_first_word()}")

word1 = WordleWord([
    WordleLetter("b", 1),
    WordleLetter("u", 0),
    WordleLetter("t", -1),
    WordleLetter("t", -1),
    WordleLetter("s", 1)
])
solver.add_guess(word1)
print(f"Guess for second word: {solver.get_best_guess()[0]}")

# word2 = WordleWord([
#     WordleLetter("m", -1),
#     WordleLetter("o", -1),
#     WordleLetter("o", -1),
#     WordleLetter("n", -1),
#     WordleLetter("a", 1)
# ])
# solver.addGuess(word2)
# print(f"Guess for third word: {solver.get_best_guess()[0]}")

# word3 = WordleWord([
#     WordleLetter("s", 1),
#     WordleLetter("a", 0),
#     WordleLetter("a", 1),
#     WordleLetter("b", -1),
#     WordleLetter("a", 1)
# ])
# solver.addGuess(word3)
# print(f"Guess for foruth word: {solver.get_best_guess()[0]}")

# word4 = WordleWord([
#     WordleLetter("s", 1),
#     WordleLetter("p", -1),
#     WordleLetter("a", 1),
#     WordleLetter("s", 0),
#     WordleLetter("a", 1)
# ])
# solver.addGuess(word4)
# print(f"Guess for fifth word: {solver.get_best_guess()[0]}")

# word5 = WordleWord([
#     WordleLetter("s", 1),
#     WordleLetter("s", 0),
#     WordleLetter("a", 1),
#     WordleLetter("w", -1),
#     WordleLetter("a", 1)
# ])
# solver.addGuess(word5)
# print(f"Guess for sixth, final word: {solver.get_best_guess()[0]}")