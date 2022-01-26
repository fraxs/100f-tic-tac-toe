from x01_data import *
from x02_display import *
from x03_winner import *
import os
import time as t

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
if __name__ == "__main__":
    board = [0,0,0,0,0,0,0,0,0]
    while True:
        try:
            p1input = int(input("X, input the square you want to play: "))
            if read(board,p1input) == None:
                clearConsole()
                board = write(p1input,board,"X")
                print( displayString(board))
                
            if whoWins(board) != None:
                print(f"Congrats {whoWins(board)}! You win!")
                break
            p2input = int(input("O, input the square you want to play: "))
            if read(board,p2input) == None:
                clearConsole()
                board = write(p2input,board,"O")
                print( displayString(board))
                
            if 0 not in board:
                print("Its a tie!")
                break
            if whoWins(board) != None:
                print(f"Congrats {whoWins(board)}! You win!")
                break 
        except:
            print("Invalid input.")

