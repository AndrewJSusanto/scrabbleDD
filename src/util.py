# pylint: disable=C0103, C0114, C0115, C0116, C0301, W0106, W0611, W0614, W0401, C0200, R0913, R0911, R0912
import random
import string
import gaddag
from constants import *

class Board():
    """Standard Scrabble Board, empty when initialized"""
    def __init__(self):
        self.turn_count = 0
        self.board_cols = BOARD_WIDTH
        self.board_rows = BOARD_HEIGHT
        self.board_Board = [ [BoardSpace((y, x)) for x in range(self.board_cols)] for y in range(self.board_rows) ]
        self.board_Tiles = [ [Tile() for _ in range(self.board_cols)] for _ in range(self.board_rows) ]
    def show(self):
        print('     ', end='')
        for index in range(len(col_labels)):
            print(col_labels[index] + ' ', end='')
        print('\n')
        for i in range(self.board_rows):
            for j in range(self.board_cols):
                if j == BOARD_WIDTH - 1:
                    print(getattr(self.board_Tiles[i][j], 'letter'))
                elif j == 0:
                    print(row_labels[i] + '   ', end='')
                    print(getattr(self.board_Tiles[i][j], 'letter') + ' ', end='')  
                else:
                    print(getattr(self.board_Tiles[i][j], 'letter') + ' ', end='')
    def get_cardinal_neighbors(self, board, row, col):
        """
            Takes a coordinate position on board and returns a list of cardinal-neighboring Tile objects
        """
        neighbors = [] # NSEW
        neighbors.append(getattr(board.board_Tiles[row - 1][col], 'letter')) if row > 0 else neighbors.append(NONE)
        neighbors.append(getattr(board.board_Tiles[row + 1][col], 'letter')) if row < BOARD_HEIGHT - 1 else neighbors.append(NONE)
        neighbors.append(getattr(board.board_Tiles[row][col + 1], 'letter')) if col < BOARD_WIDTH - 1 else neighbors.append(NONE)
        neighbors.append(getattr(board.board_Tiles[row][col - 1], 'letter')) if col > 0 else neighbors.append(NONE)

        return neighbors if any(isinstance(item, str) and item.isalpha() for item in neighbors) else []

    def valid(self, board, word, row, col, direction):
        """
            Takes current board state, word, coords, and direction of desired play and determines
            the validity of the move.
            1. Check if valid word, row, col, dir
            2. Check if valid available space
            3. Check if valid intersect between previous play and current play
                - Valid intersect if:
                    - Input contains one or more tiles already in play (letter, coord)
                    - Input connects to a neighbor one or more times
                        - Call neighbors function; if neighbors neighbors returns [] then false 
        """
        input = word.upper()
        input_space = []
        length = len(word)

        # valid word: extend, but for now if word is all alpha
        # valid row, col: if row, col exists within 0 and BOARD_WIDTH, BOARD_HEIGHT
        # valid dir: HORI or VERT (building towards the right or downwards)

        if not word.isalpha():
            print('Submitted word is not valid (Non-alphabetical)')
            return False
        if not (0 <= row < BOARD_HEIGHT and 0 <= col < BOARD_WIDTH):
            print('Submitted coordinates out of bounds.')
            return False
        if direction is HORI:
            if col + len(input) > BOARD_WIDTH:
                # raise ValueError('Board not wide enough for play')
                print('Board not wide enough for play')
                return False
            for i in range(length):
                input_space.append(getattr(board.board_Tiles[row][col + i], 'letter'))
            # print(input_space)
            # After on-tiles are determined, we want to see if the played word has letters in the right spots.
            # Crosscheck input space and input word to see if it matches.
            for i in range(length):
                if input_space[i] is not NONE:
                    if input_space[i] != input[i]:
                        # if the input space is filled and the letters do not match, return
                        print('Tile present \'' + input_space[i] +
                              '\' conflicts with user input \'' + input[i] +
                              '\' at ' + '[' + str(row) + ']' + '[' + str(col + i) + ']')
                        return False
            # Check if play has neighbors; play is valid if neighbors exist at least once for all tiles being played
            list_of_neighbors = []
            for i in range(length):
                list_of_neighbors.append(board.get_cardinal_neighbors(board, row, col + i))
            if all(sublist == [] for sublist in list_of_neighbors) and board.turn_count != 0: # if all tiles have no neighbors, isolated.
                print('All tiles attempted have no neighbors')
                return False
            return True
        elif direction is VERT:
            if row + len(input) > BOARD_HEIGHT:
                # raise ValueError('Board not tall enough for play')
                print('Board not tall enough for play')
                return False
            for i in range(length):
                input_space.append(getattr(board.board_Tiles[row + i][col], 'letter'))
            # print(input_space)
            # After on-tiles are determined, we want to see if the played word has letters in the right spots.
            # Crosscheck input space and input word to see if it matches.
            for i in range(length):
                if input_space[i] is not NONE:
                    if input_space[i] != input[i]:
                        # if the input space is filled and the letters do not match, return
                        print('Tile present \'' + input_space[i] +
                              '\' conflicts with user input \'' + input[i] +
                              '\' at ' + '[' + str(row + i) + ']' + '[' + str(col) + ']') 
                        print('Invalid input, conflicting tiles from submission')
                        return False
            # Check if play has neighbors; play is valid if neighbors exist at least once for all tiles being played
            list_of_neighbors = []
            for i in range(length):
                list_of_neighbors.append(board.get_cardinal_neighbors(board, row + i, col))
            if all(sublist == [] for sublist in list_of_neighbors) and board.turn_count != 0: # if all tiles have no neighbors, isolated.
                print('All tiles attempted have no neighbors')
                return False
            return True
        else:
            # raise ValueError('Direction not Valid')
            print('Direction not valid. Play HORI or VERT.')
            return False

    def placeTile(self, letter, row, col):
        space = (row, col)
        tile = letter.lower()
        if tile not in LETTER_VALUES:
            raise ValueError('Tile Contents invalid')
        self.board_Board[row][col].occupy((row, col))
        self.board_Tiles[row][col] = Tile(letter.upper())

    def placeWord(self, board, word, row, col, dir):
        space = (row, col)
        word = word.lower()
        print('Attempting to play ' + word.upper())
            # if word not in word list value error
            # call valid. If valid is true, play the word. if valid is not true, return False.
        if not self.valid(board, word, row, col, dir): # if invalid, end
            print('Play was invalid. Gamestate unchanged.')
            return

        if dir is HORI:
            if col + len(word) > BOARD_WIDTH: # if board does not fit
                raise ValueError('Board not wide enough for play')
            for index in range(len(word)):
                letter = word[index]
                board.placeTile(letter, row, col + index)
        elif dir is VERT:
            if row + len(word) > BOARD_HEIGHT: # if board does not fit
                raise ValueError('Board not tall enough for play')
            for index in range(len(word)):
                letter = word[index]
                board.placeTile(letter, row + index, col)

        if self.turn_count == 0:
            print('First play of the game! ( ˶°ㅁ°)')
        self.turn_count += 1
        print('User ' + str(self.turn_count % 2) + ' has played ' + word +
              ' from [' + str(row) + ']' + '[' + str(col) + ']')
        print('New game state:\n')
        board.show()
        # take into account present game state
        # take letters and present board tiles and build word from user input
        # if letter is * use tile present

class BoardSpace():
    def __init__(self, coords = (None, None), occupied = False, bonus = 'None'):
        # Raise a value error if the instance is not a tuple, or if any of the coords are not ints.
        if not isinstance(coords, tuple) and len(coords) == 2 and all(isinstance(i, int) for i in coords):
            raise ValueError('Tile space invalid')
        self.coords = coords
        self.occupied = occupied
        self.bonuses = ['2W', '2L', '3W', '3L', 'None'] 
        if bonus not in self.bonuses:
            raise ValueError('Bonus invalid')
        self.bonus = bonus
    def is_occupied(self):
        return self.occupied
    def get_bonus(self):
        return self.bonus
    def get_coords(self):
        return self.coords
    def show(self):
        print(self.coords)
    def occupy(self, coords):
        self.occupied = True
        # print("BoardSpace at [" + str(coords[0]) + "][" + str(coords[1]) + "] has been occupied")


class Bag():
    """Scrabble Word Bag, containing playable tiles and blanks"""


class Tile():
    """Scrabble Tiles of letter, blank, or None, and its associated value"""
    def __init__(self, letter = None, value = None):
        self.letter = letter
        self.value = LETTER_VALUES.get(self.letter.lower()) if self.letter.lower() in LETTER_VALUES else 0
        if not isinstance(self.letter, (str , type(None))):
            raise ValueError('Proposed tile is not valid: '  + self.letter)
        if self.letter is None:
            self.letter = NONE
    def show(self):
        print(self.letter, end='')
    def show_value(self):
        print(self.value)

tileA = Tile('A')
tileA.show_value()
