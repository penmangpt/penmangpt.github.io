#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = 10

def genNnextMoveDict(N):
    N += (N %2)
    out_dict = {}
    for i in range(N+1):
        temp_list_can_move = []
        len_list = 0
        for j in range(2+i):
            if j <= 3:
                len_list += 1
            else:break
        if i <= N-2:
            if i<3:
                for j in range(len_list+1):
                    if i != j:

                        temp_list_can_move.append( j )
            else:
                for j in range(i-2,len_list+i-1):
                    if i != j:

                        temp_list_can_move.append( j )
        else:
            for j in range(i-2,len_list+i-1):
                if i != j and j <=N:

                    temp_list_can_move.append( j )

        out_dict[i] = temp_list_can_move
    return out_dict

nextMoveDict = genNnextMoveDict(N)

def cfToNum(x):
    out = []
    for i in range(len(x)):
        if x[i] == "cow":
            out.append(0)
        elif x[i] == "farmer":
            out.append(1)
        else:
            out.append(-1)
    return out

def numToCF(x):
    out = []
    for i in range(len(x)):
        if x[i] == 0:
            out.append("cow")
        elif x[i] == 1:
            out.append("farmer")
        else:
            out.append("")
    return out

def indexOfHaveChess(chessList):
    index = -1
    return [index for index, item in enumerate(chessList) if item != ""]

def nextCanMove(focusChess, chessList):
    numList = cfToNum(chessList)
    canMoveList = []
    haveChessList = indexOfHaveChess(chessList)

    if chessList[ focusChess ] == "cow":
        for x in nextMoveDict[focusChess]:
            if x not in haveChessList:
                canMoveList.append(x)
    else:
        for x in nextMoveDict[focusChess]:
            if x not in haveChessList:
                if focusChess % 2 == 0 and x < focusChess:
                    canMoveList.append(x)
                elif focusChess % 2 != 0:
                    if x < focusChess or x == focusChess + 1:
                        canMoveList.append(x)
    return canMoveList


def nextCanMoveFarmer(focusChess, focusChess2, chessList, chessCombDict, level=100):
    nextCanMoveList = nextCanMove(focusChess, chessList)
    nextCanMoveList2 = nextCanMove(focusChess2, chessList)

    if True:

        try:
            if chessList.index("cow") == 0 and chessList[chessList.index("cow") + 3] == "farmer" and chessList[chessList.index("cow") + 4] == "farmer":
                nextMove = focusChess - 1
                if nextMove in nextCanMoveList:
                    return [focusChess, nextMove]
                return [focusChess if nextCanMoveList else focusChess2, nextCanMoveList[0] if nextCanMoveList else nextCanMoveList2[0]]
        except:
            pass

        try:
            if chessList[chessList.index("cow") + 2] == "farmer" and chessList[chessList.index("cow") + 5] == "farmer":
                nextMove = focusChess + 1
                if nextMove in nextCanMoveList:
                    return [focusChess, nextMove]
                return [focusChess if nextCanMoveList else focusChess2, nextCanMoveList[0] if nextCanMoveList else nextCanMoveList2[0]]
        except:
            pass

        try:
            if chessList.index("cow") == 0 and chessList[chessList.index("cow") + 4] == "farmer" and chessList[chessList.index("cow") + 6] == "farmer":
                nextMove = focusChess - 1
                if nextMove in nextCanMoveList:
                    return [focusChess, nextMove]
                return [focusChess if nextCanMoveList else focusChess2, nextCanMoveList[0] if nextCanMoveList else nextCanMoveList2[0]]
        except:
            pass

        try:
            if chessList[chessList.index("cow") + 2] == "farmer" and chessList[chessList.index("cow") + 3] == "farmer":
                nextMove = focusChess2 - 2
                if nextMove in nextCanMoveList2:
                    return [focusChess2, nextMove]
                return [focusChess if nextCanMoveList else focusChess2, nextCanMoveList[0] if nextCanMoveList else nextCanMoveList2[0]]
        except:
            pass

        try:
            if chessList[chessList.index("cow") + 3] == "farmer" and chessList[chessList.index("cow") + 4] == "farmer":
                nextMove = focusChess - 1
                if nextMove in nextCanMoveList:
                    return [focusChess, nextMove]
                return [focusChess if nextCanMoveList else focusChess2, nextCanMoveList[0] if nextCanMoveList else nextCanMoveList2[0]]
        except:
            pass

        try:
            if chessList[chessList.index("cow") + 1] == "farmer" and chessList[chessList.index("cow") + 3] == "farmer":
                nextMove = focusChess2 - 1
                if nextMove in nextCanMoveList2:
                    return [focusChess2, nextMove]
                return [focusChess if nextCanMoveList else focusChess2, nextCanMoveList[0] if nextCanMoveList else nextCanMoveList2[0]]
        except:
            pass

        try:
            if chessList.index("cow") % 2 == 0 and chessList[chessList.index("cow") + 4] == "farmer" and chessList[chessList.index("cow") + 5] == "farmer":
                nextMove = focusChess - 1
                if nextMove in nextCanMoveList:
                    return [focusChess, nextMove]
                return [focusChess if nextCanMoveList else focusChess2, nextCanMoveList[0] if nextCanMoveList else nextCanMoveList2[0]]
        except:
            pass

        try:
            if chessList.index("cow") % 2 != 0 and chessList[chessList.index("cow") + 2] == "farmer" and chessList[chessList.index("cow") + 4] == "farmer":
                nextMove = focusChess2 + 1
                if nextMove in nextCanMoveList2:
                    return [focusChess2, nextMove]
                return [focusChess if nextCanMoveList else focusChess2, nextCanMoveList[0] if nextCanMoveList else nextCanMoveList2[0]]
        except:
            pass

        try:
            if chessList.index("cow") % 2 != 0 and chessList[chessList.index("cow") + 3] == "farmer" and chessList[chessList.index("cow") + 5] == "farmer":
                nextMove = focusChess - 1
                if nextMove in nextCanMoveList:
                    return [focusChess, nextMove]
                return [focusChess if nextCanMoveList else focusChess2, nextCanMoveList[0] if nextCanMoveList else nextCanMoveList2[0]]
        except:
            pass

        try:
            if chessList.index("cow") % 2 != 0 and chessList[chessList.index("cow") + 4] == "farmer" and chessList[chessList.index("cow") + 5] == "farmer":
                nextMove = focusChess - 2
                if nextMove in nextCanMoveList:
                    return [focusChess, nextMove]
                return [focusChess if nextCanMoveList else focusChess2, nextCanMoveList[0] if nextCanMoveList else nextCanMoveList2[0]]
        except:
            pass

        try:
            if chessList.index("cow") % 2 == 0 and chessList[chessList.index("cow") + 3] == "farmer" and chessList[chessList.index("cow") + 6] == "farmer":
                nextMove = focusChess2 - 1
                if nextMove in nextCanMoveList2:
                    return [focusChess2, nextMove]
                return [focusChess if nextCanMoveList else focusChess2, nextCanMoveList[0] if nextCanMoveList else nextCanMoveList2[0]]
        except:
            pass

    smallest_diff = 999+N
    smallest_diff_focus_chess = -1
    next_move = -1
    for x in nextCanMoveList:
        if focusChess2 - x < smallest_diff:
            smallest_diff = focusChess2 - x
            smallest_diff_focus_chess = focusChess
            next_move = x
    for x in nextCanMoveList2:
        if x - focusChess < smallest_diff:
            smallest_diff = x - focusChess
            smallest_diff_focus_chess = focusChess2
            next_move = x
    return [smallest_diff_focus_chess, next_move]

def nextCanMoveCow(focusChess, chessList, chessCombDict, level = 100):

    nextCanMoveList = nextCanMove(focusChess, chessList)

    if True:
        try:
            if chessList[chessList.index("cow") + 3] == "farmer" and chessList[chessList.index("cow") + 4] == "farmer":
                nextMove = focusChess + 2
                if nextMove in nextCanMoveList:
                    return nextMove
        except:
            pass
        try:
            if chessList.index("cow") % 2 == 0 and chessList[chessList.index("cow") + 1] == "farmer" and chessList[chessList.index("cow") + 2] == "farmer":
                nextMove = focusChess - 2
                if nextMove in nextCanMoveList:
                    return nextMove
        except:
            pass
        try:
            if chessList[chessList.index("cow") + 2] == "farmer" and chessList[chessList.index("cow") + 4] == "farmer":
                nextMove = focusChess - 1
                if nextMove in nextCanMoveList:
                    return nextMove
        except:
            pass
        try:
            if chessList[chessList.index("cow") + 1] == "farmer" and chessList[chessList.index("cow") + 4] == "farmer":
                nextMove = focusChess + 2
                if nextMove in nextCanMoveList:
                    return nextMove
        except:
            pass
        try:
            if chessList[chessList.index("cow") + 2] == "farmer" and chessList[chessList.index("cow") + 5] == "farmer":
                nextMove = focusChess - 1
                if nextMove in nextCanMoveList:
                    return nextMove
        except:
            pass
    if focusChess + 1 in nextCanMoveList:
        return focusChess + 1

    return nextCanMoveList[-1]

def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def real_move(current_chess, current_chessboard, move_to):
    current_character = current_chessboard[current_chess]
    out_character = ""
    if current_character == "cow":
        out_character = "farmer"
    else:
        out_character = "cow"
    return [swapPositions(current_chessboard, current_chess, move_to) , out_character]

def findFarmerIndex(current_chessboard):
    temp_list = []
    for i in range(len(current_chessboard)):
        if current_chessboard[i] == "farmer":
            temp_list.append(i)
    return temp_list

def findCowIndex(current_chessboard):
    temp_list = []
    for i in range(len(current_chessboard)):
        if current_chessboard[i] == "cow":
            temp_list.append(i)
    return temp_list

def genInitBoard(N):
    N+=1
    temp_list = []
    temp_list.append("cow")
    for i in range(N-3):
        temp_list.append("")
    temp_list.append("farmer")
    temp_list.append("farmer")
    return temp_list




def cowBestMove(temp_struct):

    temp_struct = real_move( current_chess, current_chessboard, nextCanMoveCow(current_chess, current_chessboard, nextMoveDict) )

    return temp_struct

def farmerBestMove(temp_struct):

    current_chessboard = temp_struct[0]
    farmer_index = findFarmerIndex(current_chessboard)
    temp_struct = nextCanMoveFarmer(farmer_index[0], farmer_index[1], current_chessboard, nextMoveDict)
    return real_move( temp_struct[0],current_chessboard, temp_struct[1] )

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def struct2img(x):
    x = [x, ""]
    board = x[0]
    temp_board = []
    j = 0
    for y in board:
        try:
            temp_board.append( color.BOLD+y[0]+color.END)
        except:
            temp_board.append(str(j))
        j+=1
    board = temp_board
    i =0
    while i <= N:
        if i == 0:
            try:
                print(board[i])
            except:
                print(i)
            print("|", " \\")
            i+=1
        else:

            print(board[i],"--",board[i+1])

            if i != N-1:
                print("|", " / \\")
            i+=2

    print('='*30)

def newInitBoard():
    global current_chessboard, current_chess, current_character
    current_chessboard = genInitBoard(N)
    current_chess = 0
    current_character = "cow"



def cowCustomMove(a, b):
    global current_chessboard, current_chess, current_character
    current_character = "farmer"
    step_ = [swapPositions(current_chessboard,a,b), current_character]
    current_chessboard = step_[0]
    current_chess = findFarmerIndex(current_chessboard)

    print(current_chessboard)



def farmerCustomMove(a, b):
    global current_chessboard, current_chess, current_character
    current_character = "cow"
    step_ = [swapPositions(current_chessboard,a,b), current_character]
    current_chessboard = step_[0]
    current_chess = findCowIndex(current_chessboard)[0]
    print(current_chessboard)
    
    
    
def cowMoveBestMove():
    global current_chessboard, current_chess, current_character
    step_ = cowBestMove([current_chessboard , current_character])
    current_character = "farmer"
    current_chessboard = step_[0]
    current_chess = findFarmerIndex(current_chessboard)
    print(current_chessboard)



def farmerMoveBestMove():
    global current_chessboard, current_chess, current_character
    step_ = farmerBestMove([current_chessboard , current_character])
    current_character = "cow"
    current_chessboard = step_[0]
    current_chess = findCowIndex(current_chessboard)[0]
    print(current_chessboard)
    
def nextMoveMatrix():
    global nextMoveDict
    hcdict = nextMoveDict
    out_list = []
    for x in hcdict:
        temp_row = []
        temp_i = 0
        for y in (hcdict[x]):
            temp_row.append(y)
            temp_i += 1
        for y in range(temp_i,4):
            temp_row.append(-1)
        out_list.append(temp_row)
    return out_list


# In[2]:


"""
current_chessboard = genInitBoard(N)
current_chess = 0
current_character = "cow"

flag_img = False

if flag_img:
    struct2img([current_chessboard, ""])

for i in range(50):
    step_ = cowBestMove([current_chessboard , current_character])

    current_character = "farmer"
    current_chessboard = step_[0]
    current_chess = findFarmerIndex(current_chessboard)
    if flag_img:
        struct2img([current_chessboard, ""])
    print(current_chessboard)

    step_ = farmerBestMove([current_chessboard , current_character])

    current_character = "cow"
    current_chessboard = step_[0]
    current_chess = findCowIndex(current_chessboard)[0]
    if flag_img:
        struct2img([current_chessboard, ""])
    print(current_chessboard)

"""


# In[8]:





# In[ ]:




