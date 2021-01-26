'''
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement.
Example

For bishop = "a1" and pawn = "c3", the output should be
bishopAndPawn(bishop, pawn) = true.
For bishop = "h1" and pawn = "h3", the output should be
bishopAndPawn(bishop, pawn) = false.'''

def bishopAndPawn(bishop, pawn):
    board ={'a':1,'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7,'h':8}
    bishopX = board[bishop[0]]
    bishopY= int(bishop[1])

    pawnX = board[pawn[0]]
    pawnY = int(pawn[1])

    if bishopX + bishopY == pawnX+pawnY  or bishopX + pawnY == bishopY+pawnX:
        return True
    return False

def bishopAndPawn2(bishop, pawn):
    return abs(ord(bishop[0])-ord(pawn[0]))==abs(int(pawn[1])-int(bishop[1]))

def bishopAndPawn3(b, p):
    b=[ord(b[0]),int(b[1])]
    p=[ord(p[0]),int(p[1])]
    return b[1]-b[0]==p[1]-p[0] or sum(b)==sum(p)


def bishopAndPawn4(bishop, pawn):
    cols = {'a': 1, 'b': 2, 'c':3 ,'d':4, 'e':5,'f':6,'g':7,'h':8 }
    if(abs(cols[bishop[0]] - cols[pawn[0]]) == abs(int(bishop[1]) - int(pawn[1]))):
        return True
    return False
    