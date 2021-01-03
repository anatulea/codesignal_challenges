'''
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.



For cell1 = "A1" and cell2 = "H3", the output should be
chessBoardCellColor(cell1, cell2) = false.
'''
def chessBoardCellColor(cell1, cell2):
    alph=['A','B','C','D','E','F','G','H']
    table ={}
    
    for i in range(1,9,2):
        for j in range(0,7, 2):
            table[(i,alph[j])]='black'
    for i in range(2,9,2):
        for j in range(1,8, 2):
            table[(i,alph[j])]='black'
    print(table)
    if (int(cell1[1]), cell1[0]) in table and (int(cell2[1]), cell2[0]) in table:
        return True
    if (int(cell1[1]), cell1[0])  not in table and (int(cell2[1]), cell2[0]) not in table:
        return True
    else:
        return False

def chessBoardCellColor2(cell1, cell2):
    
    return (ord(cell1[0])+int(cell1[1])+ord(cell2[0])+int(cell2[1]))%2==0

def chessBoardCellColor3(cell1, cell2):
    return (sum(map(ord,cell1+cell2)))%2 == 0