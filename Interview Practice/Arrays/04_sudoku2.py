'''
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.
Example
For
grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
the output should be
sudoku2(grid) = true;
For
grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
the output should be
sudoku2(grid) = false.

The given grid is not correct because there are two 1s in the second column. Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.
'''
def sudoku2(grid):
    rows = grid
    cols = zip(*grid)
    subs = [] # 3x3 grids
    
    # create the 3x3 matrix 
    for i in range(0,7,3):
        for j in range(0,7,3):
            subs.append([grid[r][c] for r in range(i,i+3) for c in range(j,j+3)])
    
    def isvalid(arr):
        nums = [x for x in arr if str.isdigit(x)] # create an array of all the numbers in sudoku
        return len(nums) == len(set(nums)) # if the len of the set is smaller than the arr len means there are duplicates
    
    # The all() method returns True when all elements in the given iterable are true. If not, it returns False.
    return all([
        all(map(isvalid, rows)),
        all(map(isvalid, cols)),
        all(map(isvalid, subs))
    ])




# helper function
def check_unique(nums):
    s = set()
    for num in nums:
        if num == '.':
            continue 
            
        if num in s:
            return False
        s.add(num)
    return True
        

def sudoku22(grid):
    for line in grid:
        if not check_unique(line):
            return False
    
    for i in range(9):
        if not check_unique([line[i] for line in grid]):
            return False
        
    for i in range(0,9,3):
        for j in range(0, 9, 3):
            if not check_unique(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]):
                return False
            
    return True



def sudoku23(grid):
    def dup_in_list(lst):
        numbers_only = [n for n in lst if n != '.']
        print(numbers_only)
        return len(numbers_only) > len(set(numbers_only))
        
    dups_in_rows = any(dup_in_list(row) for row in grid)
    dups_in_cols = any(dup_in_list([grid[r][c] for r in range(0,9)]) for c in range(9))
    subgrids = [[] for i in range(9)]
    for r in range(9):
        for c in range(9):
            subgrids[3 * (r // 3) + c // 3].append(grid[r][c])
    dups_in_subgrids = any(dup_in_list(s) for s in subgrids)
    
    return not (dups_in_rows or dups_in_cols or dups_in_subgrids)