def whoWins(board):
  if board[0] == board[1] == board[2] and board[0] != 0:
    return str(board[0])

board = [0,0,0,0,0,0,0,0,0,0]
print(whoWins(board))