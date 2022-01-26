#!python3

def displayString(board):
  b1 = []
  count = 0
  for i in board:
    if i == "O":
      b1.append("O")
    elif i == "X":
      b1.append("X")
    elif i == 0:
      b1.append("-")
    count += 1
    if count%1 == 0:
      b1.append(" ")
    if count %3 == 0:
      b1.append("\n")
  b1 = b1[:-1]
  b1[0], b1[2], b1[4], b1[14], b1[16], b1[18] = b1[14], b1[16], b1[18], b1[0], b1[2], b1[4]
  b2 = "".join(b1)
  return b2.strip() 

def main():
  board = [ 'O' , 0 , 0 , 'X' , 'O' , 0 , 0 , 0 , 'X'] 
  assert displayString(board) == "- - X \nX O - \nO - -"
  board = [ 0 , 'O' , 'X' , 'O' , 'O' , 0 , 'X' , 0 , 'X' ] 
  assert displayString(board) == "X - X \nO O - \n- O X"

if __name__ == "__main__":
  board = [ 'O' , 0 , 0 , 'X' , 'O' , 0 , 0 , 0 , 'X'] 
  print(displayString(board))