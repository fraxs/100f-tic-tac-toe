

def read(board, square):
  square -= 1
  if board[square] == "X":
    return "X"
  if board[square] == "O":
    return "O"
  if board[square] == 0:
    return None



  return None

def write(square,board,player):

  square -= 1
  if board[square] == 0:
    board.pop(square)#removes the 0 at the index given
    board.insert(square,player)#inserts X or O at the given index
    return board
  else:
    return board

def mainRead():
  board = [ 0, 'X', 0, 'X', 'O', 'O', 0 , 0, 0]
  assert read(board, 3) == None
  assert read(board, 2) == 'X'
  assert read(board, 5) == 'O'

def mainWrite():
  board = [ 0,0,0,0,0,0,0,0,0,0]
  assert write(1,board,'X') == ['X',0,0,0,0,0,0,0,0,0]
  assert write(5,board,'O') == ['X',0,0,0,'O',0,0,0,0,0]
  #next command should not do anything because square #5 is already occupied by an 'O'
  assert write(5,board,'X') == ['X',0,0,0,'O',0,0,0,0,0]
 
  
  
if __name__ == "__main__" :
  mainRead()
  mainWrite()