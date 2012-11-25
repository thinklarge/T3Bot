board = [["o","o","x"],
         ["o","x","o"],
         ["x","",""]]

heuristic = [[2,1,2],
            [1,3,1],
            [2,1,2]]

corner = [["x","","x"],
         ["","",""],
         ["x","","x"]]

side = [["","x",""],
         ["x","","x"],
         ["","x",""]]


def check3s(xo):
    print("check for 3s")
    if xo == "x":
        op = "o"
    elif xo == "o":
        op = "x"
    else:
        return ("Error, your input was bad")

    angela = 0
    angelb = 0

    for ii in range(0,3):
        row = 0
        col = 0

        if (board[ii][ii] == xo):
            angela += 1
        elif (board[ii][ii] == op):
            angela = -99
        else: 
            misxa = ii
            misya = ii 

        if (board[ii][2-ii] == xo):
            angelb += 1
        elif (board[ii][2-ii] == op):
            angelb = -99
        else: 
            misxb = 2-ii
            misyb = ii 

        for jj in range(0,3):
            if (board[ii][jj] == xo):
                row += 1
            elif (board[ii][jj] == op):
                row = -99
            else: 
                misx = jj
                misy = ii   

        if row == 2:       
            return [misx, misy]
               
        for jj in range(0,3):                   
            if (board[jj][ii] == xo):
                col += 1
            elif (board[jj][ii] == op):
                col = -99
            else: 
                misx = ii
                misy = jj
                
        if col == 2:        
            return [misx, misy] 
        


        elif row == 3 or col == 3 or angela == 3 or angelb == 3:
            return xo+" wins!"

    if angela == 2:
        print("a")
        return [misxa, misya]
        
    if angelb == 2:
        print("b")
        return [misxb, misyb]        

def human_move():
    x = input("what is x: ")
    y = input("what is y: ")
    x = int(x)
    y = int(y)
    calc_heuristic(x,y,1)

    board[y][x] = "x"

def computer_move():
    x = 1
    y = 1

def calc_heuristic(x, y, val):
    heuristic[y][x] = -99
    if not (val != -1 and val != 1):
        if is_side(x,y):
            print("side")
            heuristic[y][x]+=1
            for ii in range(1,3):
                if (x+ii < 3):
                    heuristic[y][x+ii] += 1
                if (x-ii > -1):
                    heuristic[y][x-ii] += 1
                if (y+ii < 3):
                    heuristic[y+ii][x] += 1
                if (y-ii > -1):
                    heuristic[y-ii][x] += 1
        elif is_corner(x,y):
            print("corner")
            for ii in range(1,3):
                if (x+ii < 3):
                    if (y+ii < 3):
                        heuristic[y+ii][x+ii] += 1
                    if (y-ii > -1):
                        heuristic[y-ii][x+ii] += 1
                    heuristic[y][x+ii] += 1
                if (x-ii > -1):
                    if (y+ii < 3):
                        heuristic[y+ii][x-ii] += 1
                    if (y-ii > -1):
                        heuristic[y-ii][x-ii] += 1
                    heuristic[y][x-ii] += 1
                if (y+ii < 3):
                    heuristic[y+ii][x] += 1
                if (y-ii > -1):
                    heuristic[y-ii][x] += 1
        elif is_center(x,y):
            print("center")
            for ii in range(0,3):
                for jj in range(0,3):
                    heuristic[ii][jj] += 1

def is_corner(x,y):
    if corner[y][x] == "x":
        ret = True
    else:
        ret = False
    return ret

def is_side(x,y):
    if side[y][x] == "x":
        ret = True
    else:
        ret = False
    return ret

def is_center(x,y):
    if x == 1 and y == 1:
        return True
    else:
        return False
    return corner

def print_array(ar):
    for ii in range(len(ar[0])):
        print ar[ii]

print(check3s("x"))
s=1
while s < 9:
    print_array(heuristic)
    human_move()
    s += 1
