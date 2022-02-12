from libs.WordleLetter import WordleLetter
from libs.WordleWord import WordleWord
from libs.WordleSolver import WordleSolver


# TODO: Add CLI interface
# TODO: Add GUI interface
# TODO: Implement autoplay on website by the script

# If you put in two identical letters as an answer (for instance: 'a'), and Wordle says that one of these letters is correct (1) or misplaced (0), then Wordle will label the second letter as wrong (-1). To not break the script, you should label the second letter as misplaced (0) and everything will work correctly

solver = WordleSolver("default.txt", True)
print(solver.getBestFirstWord())

word1 = WordleWord([
    WordleLetter("b", 1),
    WordleLetter("u", 0),
    WordleLetter("t", -1),
    WordleLetter("t", -1),
    WordleLetter("s", 1)
])
solver.addGuess(word1)
print(solver.getBestGuess())

# word2 = WordleWord([
#     WordleLetter("m", -1),
#     WordleLetter("o", -1),
#     WordleLetter("o", -1),
#     WordleLetter("n", -1),
#     WordleLetter("a", 1)
# ])
# solver.addGuess(word2)
# print(solver.getBestGuess())

# word3 = WordleWord([
#     WordleLetter("s", 1),
#     WordleLetter("a", 0),
#     WordleLetter("a", 1),
#     WordleLetter("b", -1),
#     WordleLetter("a", 1)
# ])
# solver.addGuess(word3)
# print(solver.getBestGuess())

# word4 = WordleWord([
#     WordleLetter("s", 1),
#     WordleLetter("p", -1),
#     WordleLetter("a", 1),
#     WordleLetter("s", 0),
#     WordleLetter("a", 1)
# ])
# solver.addGuess(word4)
# print(solver.getBestGuess())

# word5 = WordleWord([
#     WordleLetter("s", 1),
#     WordleLetter("s", 0),
#     WordleLetter("a", 1),
#     WordleLetter("w", -1),
#     WordleLetter("a", 1)
# ])
# solver.addGuess(word5)
# print(solver.getBestGuess())