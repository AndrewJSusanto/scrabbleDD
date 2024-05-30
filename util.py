import random
import string

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
blank = '?'

BOARD_HEIGHT = BOARD_WIDTH = 15


LETTER_VALUES = {
    '?': 1, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# word list is queried on every action to check validity and value
# word list will be a GADDAG of Naspa Word List 2023 consisting of all valid words in modern Scrabble
WORD_LIST = {}


class Board():
    """Standard Scrabble Board, empty when initialized"""
    def __init__(self):
        self.board_cols = BOARD_WIDTH
        self.board_rows = BOARD_HEIGHT
        self.board_Board = [ [BoardSpace((y, x)) for x in range(self.board_cols)] for y in range(self.board_rows) ]
        self.board_Tiles = [ [Tile() for _ in range(self.board_cols)] for _ in range(self.board_rows) ]
    def show(self):
        for i in range(self.board_cols):
            for j in range(self.board_rows):
                #self.board_Board[i][j].show()
                if j == BOARD_WIDTH - 1:
                    print(getattr(self.board_Board[i][j], 'letter'))
                else:
                    print(getattr(self.board_Board[i][j], 'letter'), end='')
    def placeTile(self, tile, row, col):
        space = (row, col)
        if not isinstance(tile, Tile):
            raise ValueError('Tile passed is of an invalid typing')
        self.board_Board[row][col].occupied((row, col))
        self.board_Tiles[row][col] = tile

class BoardSpace():
    BONUSES = [
        '2W',
        '2L',
        '3W',
        '3L',
        'None'
    ] 
    def __init__(self, coords = (None, None), occupied = False, bonus = 'None'):
        if not isinstance(coords, (int, int)):
            raise ValueError('Tile space invalid')
        self.coords = coords
        self.occupied = occupied
        if bonus not in BONUSES:
            raise ValueError('Bonus invalid')
        self.bonus = bonus
    def is_occupied(self):
        return self.occupied
    def get_bonus(self):
        return self.bonus
    def get_coords(self):
        return self.coords
    
    def occupy(self, coords):
        self.occupied = True
        print("BoardSpace at tile [" + coords[0] + "][" + coords[1] + "] has been occupied")
    


class Bag():
    """Scrabble Word Bag, containing playable tiles and blanks"""


class Tile():
    """Scrabble Tiles of letter, blank, or None, and its associated value"""
    def __init__(self, letter = None):
        self.letter = letter
        if not isinstance(self.letter, (str , type(None))):
            raise ValueError('Proposed tile is not valid: '  + self.letter)
        if self.letter is None:
            self.letter = '_'
    def show(self):
        print(self.letter)

board = Board()
tileA = Tile('A')
tileA.show()