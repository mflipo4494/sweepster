import random

import utils

###setup inputs###

symbols = {' ': False, '*': True}
  
BOARD_SIZE = 8
board = utils.board(BOARD_SIZE)

#symbol_data = []
print utils.show_board(utils.show_bombs(board))

alive = True
print("Welcome to sweepster!")
print("""Type the column followed by the row (eg. 1,5)
complete this until all 10 bombs are found,
Have Fun! May the odds be ever in your favor!!!""")
while alive is True:
    helpmessage = "Select coordinate: " 
    choice = raw_input(helpmessage)
    if not utils.check_format(choice):
        continue
    coords = utils.extract_coords(choice)
    if not utils.check_within(coords, BOARD_SIZE):
        print("Coords not within the board!")
        continue
    if not utils.bomb_check(coords, board):
        print("space is clear, try another space.")
    else:
        print("oh no! you found a bomb.")
        alive = False
    

    
