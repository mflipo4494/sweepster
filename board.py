
board = {y:{x+1:{} for x in range(8)} for y in range(8)}

for row in board:
    print(board[row])
