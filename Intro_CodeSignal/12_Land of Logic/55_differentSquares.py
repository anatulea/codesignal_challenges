'''
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1'''
def differentSquares(matrix):
    row = len(matrix)
    col = len(matrix[0])
    uniqueMatrix = []
    
    for i in range(0,row-1):
        for j in range(0,col-1):
            matrix2 = [[matrix[i][j],matrix[i][j+1]],[matrix[i+1][j],matrix[i+1][j+1]]]
            if matrix2 not in uniqueMatrix:
                uniqueMatrix.append(matrix2)
    
    return len(uniqueMatrix)



def differentSquares2(matrix):
    s = set()
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
                s.add((matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]))
    return len(s)