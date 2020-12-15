'''
No time to explain! The World Government made contact with intelligent alien life, and needs you to send a message to the outer space. The aliens only receive messages that are stored in a sequence of lists of sizes 0, 1, 1, 2, 3, 5, ..., in other words those whose length increase according to the Fibonacci sequence.

The Government is too busy composing the message, and needs you to prepare the list in which the message should be sent. Given an integer n, return a list of n lists, where the first element consists is empty (consists of 0 zeros), the second element consists of 1 zero, and so on.

Example

For n = 6, the output should be

fibonacciList(n) = [[], 
                    [0], 
                    [0], 
                    [0, 0], 
                    [0, 0, 0], 
                    [0, 0, 0, 0, 0]]
                    '''
import functools
def fibonacciList(n):
    return [[0] * x for x in functools.reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0,1])]


from functools import reduce
'''
---> functools.reduce(function, iterable[, initializer]) <---
Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). The left argument, x, is the accumulated value and the right argument, y, is the update value from the iterable. If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. If initializer is not given and iterable contains only one item, the first item is returned.
'''

def fibonacciList2(n):
    result = []
    
    value = reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0,1])
     # calculates the n fibonacci numbers 
     # as we know that the first and second numbers are 1 we start the range from the third  
    # print(value) # [0, 1, 1, 2, 3, 5]

    for i in value:
        result.append([0]*i)
    return result

print(fibonacciList2(6))