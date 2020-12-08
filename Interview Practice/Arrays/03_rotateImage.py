'''
You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
Example
For
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

                    rotateImage(a) =
                        [[7, 4, 1],
                        [8, 5, 2],
                        [9, 6, 3]]
     
'''
def rotateImage(a):
    return list(zip(*a[::-1]))
    # return list(list(x)[::-1] for x in zip(*a))

def rotateImage2(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a


def rotateImage3(a):
    for j in range(len(a)//2):
        for i in range(j, len(a)-1-j):
            temp = a[j][i]
            a[j][i]  = a[-1-i][j]
            a[-1-i][j] = a[-1-j][-1-i]
            a[-1-j][-1-i] = a[i][-1-j]
            a[i][-1-j] = temp
    return a

def rotateImage4(a):
    n = len(a)
    
    for i in range(n):
        for j in range(i+1,n):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    
    print(a)   
    for i in range(n):
        for j in range(n//2):
            a[i][j], a[i][n-j-1]  = a[i][n-j-1], a[i][j]
    
    return a 