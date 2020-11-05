'''
There is a great technique that allows finding sums of consecutive elements in the given array extremely fast. It is based on the usage of prefix sums. Given array a, your task is to calculate all its prefix sums.

Example

For a = [1, 2, 3], the output should be
prefSum(a) = [1, 3, 6].

Here's how the prefix sums can be calculated: [1, 1 + 2, 1 + 2 + 3] = [1, 3, 6].
'''
from itertools import accumulate 
# This iterator takes two arguments, iterable target and the function which would be followed at each iteration of value in target. If no function is passed, addition takes place by default. If the input iterable is empty, the output iterable will also be empty.

# Syntax
# itertools.accumulate(iterable[, func]) –> accumulate object
def prefSum(a):
    return list(accumulate(a)) # no second argument so it does addition


    # Other solutions:
    # return list(functools.reduce(lambda memory, y: memory + [memory[-1]+ y], a[1:], [a[0]]))

    # The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along

# Using numpy
# from numpy import cumsum

# def prefSum2(a):
#     return cumsum(a)

def prefSum3(a):

    result = []
    # result = [sum(a[ : i + 1]) for i in range(len(a))] 
    for i in range(len(a)):
        sum2 = sum(a[:i+1]) # 
        result.append(sum2)  

    print(result)
prefSum3([1, 2, 3]) #[1, 3, 6]