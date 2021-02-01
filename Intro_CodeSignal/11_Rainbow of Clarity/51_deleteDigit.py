'''
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
deleteDigit(n) = 52;
For n = 1001, the output should be
deleteDigit(n) = 101.
'''
def deleteDigit(n):
    str_num = str(n)
    nums = []
    
    for i in range(len(str_num)):
        nums.append(str_num[:i]+str_num[i+1:])
    return max([int(x) for x in nums])


def deleteDigit2(n):
    n = str(n)
    return max(int(''.join(n[:i]+n[i+1:])) for i in range(len(n)))