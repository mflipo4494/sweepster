import random

###creates a viewer friendly minesweeper board###
def flatten(board):
    flat = []
    for row in board:
        for column in board[row]:
            flat.append(board[row][column])
    return flat

###uses probability in random to add bombs to the board###

def bomb(board):
    bomb_count = 0
    while bomb_count < 10:  
        for row in board:
            for column in board[row]:                        
                if random.random() < 0.05 and board[row][column]['bomb'] == False and bomb_count < 10 :
                    board[row][column]['bomb'] = True
                    bomb_count += 1
    return board


symbols = {' ': False, '*': True}
 



board = {y+1:{x+1:{'bomb': False} for x in range(8)} for y in range(8)}

##board[3][3]['bomb'] = True

data = flatten(bomb(board))


###creates board seen on screen####


symbol_data = []
for cell in data:
    if cell['bomb'] == True:
        symbol_data.append('*')
    else:
        symbol_data.append(' ')
        
print("""
_|12345678
1|{}{}{}{}{}{}{}{}
2|{}{}{}{}{}{}{}{}
3|{}{}{}{}{}{}{}{}
4|{}{}{}{}{}{}{}{}
5|{}{}{}{}{}{}{}{}
6|{}{}{}{}{}{}{}{}
7|{}{}{}{}{}{}{}{}
8|{}{}{}{}{}{}{}{}
""".format(*symbol_data))
