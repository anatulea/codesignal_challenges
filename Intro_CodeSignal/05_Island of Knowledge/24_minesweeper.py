'''
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
'''
def minesweeper(matrix):
    result = []
    for row in range(len(matrix)):
        # print(f'row: {row}')
        
        result.append([])
        # print(f'result: {result}')
        
        for col in range(len(matrix[0])):
            # print(f'col: {col}')
            bomb_count = -matrix[row][col] # true == 1    ==>   -true == -1 false == 0    =>  -false ==0
            # print(f'l: {l}, {matrix[row][col]}')
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if 0 <= row + x < len(matrix) and 0 <= col + y < len(matrix[0]):
                        
                       bomb_count += matrix[row + x][col + y]

            result[row].append(bomb_count)
    return result


def minesweeper2(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    
    conv = lambda i , j : 1 if 0 <= i < rows and 0 <= j < cols and matrix[i][j] else 0
    
    nbs = lambda i, j : sum(conv(ii, jj) for ii in range(i-1, i+2) for jj in range(j-1, j+2)) - conv(i, j)
    
    return [[nbs(i, j) for j in range(cols)]for i in range(rows)]
