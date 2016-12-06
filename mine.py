import utils

###setup inputs###

symbols = {' ': False, '*': True}
  
BOARD_SIZE = 8
board = utils.board(BOARD_SIZE)

#symbol_data = []
print utils.show_board(utils.show_bombs(board))

helpmessage = ("Type the column followed by the row (eg. 1,5)"
               "complete this until all 10 bombs are found,"
               "Have Fun! May the odds be ever in your favor!!!") 

choice = raw_input(helpmessage)
utils.check_choice(choice)


