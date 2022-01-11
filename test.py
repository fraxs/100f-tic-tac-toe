board = [ 'O' , 0 , 0 , 'X' , 'O' , 0 , 0 , 0 , 'X' ] 
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
    if count%3 == 0:
        b1.append("\n")
b1[0], b1[2], b1[4], b1[14], b1[16], b1[18] = b1[14], b1[16], b1[18], b1[0], b1[2], b1[4]
b2 = ''.join(b1)
print(b2)
print("- - X\nX O -\nO - -")

