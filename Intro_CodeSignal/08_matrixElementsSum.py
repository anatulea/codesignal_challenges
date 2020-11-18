# def matrixElementsSum(matrix):
#     count = sum(matrix[0])
#     for i in range(len(matrix)-1):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == 0:
#                 print('whwhhw')
#                 # print(f'matrix[i][j]: {matrix[i][j]})'
#                 # return
#             else:
#                 print(f'matrix[i+1][j]:{matrix[i+1][j]}')
#                 count = count+ matrix[i+1][j]
#     return count

# def matrixElementsSum(matrix):
#     count = 0
#     for i in range(len(matrix)):
#         print(f'i:{i}')
#         for idx, num in enumerate(matrix[i]):
#             # print(f'idx:{idx} num{num}')
#             if num == 0 :
#                  for(int k=i;k<matrix.length;k++){
#                     matrix[k][j]=0;
#                 }
#                 continue;
#                 # print(f'idx:{idx} num{num}')
#                 # print(f'matrix[i+1][idx]:{matrix[i+1][idx]}')
#                 # # matrix[i+1][idx] = 0
#             else:
#                 # print(f'num:{num}')
#                 count = count + num
                
#     return count

# def matrixElementsSum(matrix):
#     count = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == 0:
#                 k = i+1
#                 for k in range(len(matrix)):
#                     matrix[k][j] = 0
#     for x in range(len(matrix)):
#         for y in range(len(matrix[x])):
#             count += matrix[x][k]         
#     return count
def matrixElementsSum(m):
    r = len(m)
    c = len(m[0])
    total=0
    for j in range(c):
        for i in range(r): 
            if m[i][j]!=0:
                total+=m[i][j]
            else:
                break
    return total

mymatrix =[ [1,1,1,0], 
            [0,5,0,1], 
            [2,1,3,10]]
print(matrixElementsSum(mymatrix))


def matrixElementsSum(matrix):
    matrix_copy = matrix.copy()
    total = 0

    #loop over the rows
    for row in matrix:
        #loop over columns
        for col_idx in range(len(row)):
            if row[col_idx] == 0:
                #replace all 0's in the matrix under current 0 to 0s
                for i in range(matrix.index(row), len(matrix)):
                    matrix_copy[i][col_idx] = 0
    
    #find sum of all remaining numbers in matrix
    for row_copy in matrix_copy:
        total+= sum(row_copy)
    return total