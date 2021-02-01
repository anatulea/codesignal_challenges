'''
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.



Example

For cell = "a1", the output should be
chessKnight(cell) = 2.



For cell = "c2", the output should be
chessKnight(cell) = 6.
'''
def chessKnight(cell):
    row = ord(cell[1]) - ord('0')
    # row = int(cell[1]) - 0
    # treansform letters to numbers from 1 to 8
    column = ord(cell[0]) - ord('a') + 1
   
    steps = [
            [-2, -1], [-1, -2], [1, -2], [2, -1],
            [2, 1], [1, 2], [-1, 2], [-2, 1]
            ]
    answer = 0

    for i in range(len(steps)):
        tmpRow = row + steps[i][0]
        tmpColumn =  column + steps[i][1]
        # check if the moves goes out the board
        if (tmpRow >= 1 and tmpRow <= 8 and
            tmpColumn >= 1 and tmpColumn <= 8):
            answer += 1

    return answer


def chessKnight2(c):
    x,y = ord(c[0])-96, int(c[1])
    return sum([1<=(x+i)<=8 and 1<=(y+j)<=8 for i in [-2,-1,1,2] for j in [-2,-1,1,2]])//2