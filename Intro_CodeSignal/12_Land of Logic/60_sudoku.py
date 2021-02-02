'''
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Example

For
grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
sudoku(grid) = true;

For
grid = [[1, 3, 2, 5, 4, 6, 9, 2, 7],
        [4, 6, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
sudoku(grid) = false.

The output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.'''
def sudoku(grid):
    d1 = []
    d2 = []
    for i in range(0,9):
        if len(set(grid[i]))!=9:
            return False
        if len(set([row[i] for row in grid]))!=9:
            return False
        
    for i in range(0,9,3):
        for j in range(0,9,3): 
            box = grid[i][j:j+3]+grid[i+1][j:j+3]+grid[i+2][j:j+3]
            if len(set(box))!=9:
                return False
            
    return True


def sudoku2(grid):

    def r(i):
        return sorted(grid[i]) != list(range(1,10))
    
    def c(i):
        return sorted([grid[x][i] for x in range(9)]) != list(range(1,10))
    
    def g(x,y):
        return sorted([grid[i][j] for i in range(x,x+3) for j in range(y,y+3)]) != list(range(1,10))

    for i in range(9):
        if r(i) or c(i):
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            if g(i,j):
                return False
    return True
            