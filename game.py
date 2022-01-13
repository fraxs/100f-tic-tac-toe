from x01_data import *
from x02_display import *
from x03_winner import *

if __name__ == "__main__":
    board = [0,0,0,0,0,0,0,0,0]
    while True:
        p1input = int(input("X, input the square you want to play: "))
        if read(board,p1input) == None:
            board = write(p1input,board,"X")
            print( displayString(board))
        if whoWins(board) != None:
            print(f"Congrats {whoWins(board)}! You win!")
            break
        p2input = int(input("O, input the square you want to play: "))
        if read(board,p2input) == None:
            board = write(p2input,board,"O")
            print( displayString(board))
        if whoWins(board) != None:
            print(f"Congrats {whoWins(board)}! You win!")
            break

