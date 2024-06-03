# pylint: disable=C0103, C0114, C0116, C0301, W0106, W0611, W0614, W0401, C0200, R0913, R0911, R0912
import gaddag

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
BLANK = '?'
col_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
row_labels = ['1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', '11', '12', '13', '14', '15']
HORI = 'hori'
VERT = 'vert'
NONE = '_'
NORTH, SOUTH, EAST, WEST = [0, 1, 2, 3]
BOARD_HEIGHT = BOARD_WIDTH = 15
LETTER_VALUES = {
    '?': 1, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
    'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 
    'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# word list is queried on every action to check validity and value
# word list will be a GADDAG of Naspa Word List 2023 consisting of all valid words in modern Scrabble
WORD_LIST = ['foo', 'bar', 'foobar', 'baz']
randomwords = ['hello', 'this', 'is', 'a']
blah = ['blah', 'blah', 'blah', 'blah', 'blah', 'blah']
loaded_words = []


def load_word_list(file_path):
    word_list = []
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                print('Adding word ' + word)
                word_list.append(word)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return word_list

fp = './res/test.txt'
loaded_words = load_word_list(fp)
print(loaded_words)

# gdg1 = gaddag.GADDAG(loaded_words)
# gdg = gaddag.GADDAG(loaded_words) # seg fault ? :()
# gdg = gaddag.GADDAG(loaded_words)
