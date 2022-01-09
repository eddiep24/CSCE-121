from init import *
from pieces import *

def getinput(boardtranslation, board):
    start = input("From: ")
    end = input("To: ")
    return boardtranslation[start[1]], boardtranslation[start[0]], boardtranslation[end[1]], boardtranslation[end[0]]

def gamestate():
    return True



while gamestate():
    for i in board: print(i)
    startrow, startcol, endrow, endcol = getinput(boardtranslation, board)
    currentpiece = board[startrow][startcol]
    print(super().board[7][1])
    
    temp = board[startrow][startcol]
    board[startrow][startcol] = "---"
    board[endrow][endcol] = temp

    

# bool too represent whether a picece is alive or dead
# color variable
# position variable
#       Knights
#   White   Black
# K1   K2   K3  K4

# define a .getColor method so that when I capture I can identify whether I can or not
