# pylint: disable=C0103, C0114, C0116, C0301, W0106, W0611, W0614, W0401, C0200, R0913, R0911, R0912
import random
import string
from util import *
from constants import *

ON = True
board = Board()
print('At any point, enter Ctrl + C to quit.\n')

def menu():
    valid = False
    while valid is False:
        options = input('\n1: Play a move\n2: Pass turn\n3: Exchange tiles\n4: Show board\n\t')
        if options == '1':
            # Play a move
            user_input()
        elif options == '2':
            # Pass turn, give turn to opponent
            print('Placeholder. Returning to menu.')
            # valid = True
        elif options == '3':
            # Exchange tiles in hand for new tiles in the bag.
            print('Placeholder. Returning to menu.')
            # valid = True
        elif options == '4':
            board.show()
            # valid = True
        else:
            print('Invalid option selected.')

def user_input():
    valid = False
    while not valid:
        play = input('Input the word you would like to play:\t')
        coords = input('Enter two integers seperated by a space (formatted \'row col\'):\t')
        r, c = coords.split()
        direction = input('1: HORI\n2: VERT:\n\t')
        if direction == '1':
            board.placeWord(board, play, int(r), int(c), HORI)
            valid = True
        elif direction == '2':
            board.placeWord(board, play, int(r), int(c), VERT)
            valid = True
        else:
            print('Invalid direction.')

while ON:
    print('\n\n\n')
    board.show()
    menu()
