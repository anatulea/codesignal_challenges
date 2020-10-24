'''
A 2D list lst of size 2 * n - 1 is called a shell if it is filled with zeros and has the following configuration:

lst[0] contains one element;
lst[1] contains two elements;
...
lst[n - 2] contains n - 1 elements;
lst[n - 1] contains n elements;
lst[n] contains n - 1 elements;
...
lst[2 * n - 3] contains two elements;
lst[2 * n - 2] contains one element.
Given an integer n, return a shell list.

Example

For n = 3, the output should be

constructShell(n) = [[0],
                     [0, 0],
                     [0, 0, 0],
                     [0, 0],
                     [0]]

'''

def constructShell(n):
    return [[0]*(i+1) for i in range(n)] + [[0]*(i) for i in range(n-1,0,-1)]
    # return [[0]*min(i,2*n-i) for i in range(1,2*n)]
    # return [[0] * (n-abs(i)) for i in range(-n+1, n)]
    # return [[0] * (n-abs(n-i-1)) for i in range(2*n - 1)]
    # return [[0]*i for i in range(1,(n+1))] + [[0]*i for i in reversed(range(1,n))]
    # return [[0] * i for i in list(range(1, n)) + list(range(n, 0, -1))]
    # return [[0]*(i if i <= n else 2*n-i) for i in range(1,n*2)]
    # return [[0] * (i - 2 * max(0, i-n) ) for i in range(1, 2 * n)]


# same logic using for loops instead of list comprehension
def longShellConstruct(n):
    mylist = []
    for i in range(n):
        mylist.append([0]*(i+1))

    for i in range(n-1, 0, -1): # starts at the end of the list, stops at the begining, and moves by -1
        mylist.append([0]*(i))

    return mylist

print(longShellConstruct(5))
