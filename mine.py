import random

import utils

###setup inputs###

symbols = {' ': False, '*': True}
  
BOARD_SIZE = 8
board = utils.board(BOARD_SIZE)

#symbol_data = []
print utils.show_board(utils.show_bombs(board))

play = True
print("Welcome to sweepster!")
while play is True:
    helpmessage = ("Type the column followed by the row (eg. 1,5)"
                   "complete this until all 10 bombs are found,"
                   "Have Fun! May the odds be ever in your favor!!!") 

    choice = raw_input(helpmessage)
    if not utils.check_format(choice):
        continue
    print("Valid!")
    coords = utils.extract_coords(choice)
    if not utils.check_within(coords, BOARD_SIZE):
        print("Coords not within the board!")
        continue

    
