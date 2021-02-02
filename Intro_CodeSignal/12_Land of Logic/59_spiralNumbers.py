'''
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]'''

def spiralNumbers(n):

    def nextdir (left,right,down,up):
        #rotate direction clockwise
        if left:
            return False,False,False,True
        elif right:
            return False,False,True,False
        elif down:
            return True,False,False,False
        elif up:
            return False,True,False,False
        
    switchseq = [n]
    for i in range(1,n):
        switchseq.append(n-i)
        switchseq.append(n-i)
    
    matrix = [[0 for x in range(n)]for x in range(n)]
    
    x = 1
    y = 1
    num = 1
    
    left = False
    right = True
    down = False
    up = False
    
    for i in range(len(switchseq)):
        steps = switchseq[i]

        while steps > 0:
            matrix[y-1][x-1] = num 

            steps = steps - 1 
            num = num + 1

            if steps == 0:
                left,right,down,up = nextdir(left,right,down,up)

            if left:
                x = x-1
            
            if right:
                x = x+1
            
            if up:
                y = y-1
            
            if down:
                y = y+1
    return matrix


def spiralNumbers2(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for _ in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m