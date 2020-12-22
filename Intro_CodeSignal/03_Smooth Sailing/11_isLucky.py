'''
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
'''

def isLucky(n):
    arr = str(n)
    mid = len(arr)//2
    first = arr[:mid]
    second = arr[mid:]
    return sum(map(int, first)) == sum(map(int, second))


def isLucky2(n):
    n = [int(i) for i in str(n)]
    n_slice = len(n) // 2

    if sum(n[:n_slice]) == sum(n[n_slice : ]):
        return True
    else:
        return False