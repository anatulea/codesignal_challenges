'''
You need to sum up a bunch of fractions that have different denominators. In order to do this, you need to find the least common denominator of all the fractions. As a professional programmer, you know that the least common denominator is in fact their LCM.

For the given list of denominators, find the least common denominator by finding their LCM.

Example

For denominators = [2, 3, 4, 5, 6], the output should be
leastCommonDenominator(denominators) = 60.
'''
# from fractions import gcd
import math
import functools

def leastCommonDenominator(denominators):
    return functools.reduce(lambda x,y:x*y//math.gcd(x,y), denominators)
'''
math.gcd(*integers)
    Return the greatest common divisor of the specified integer arguments. If any of the arguments is nonzero, then the returned value is the largest positive integer that is a divisor of all arguments. If all arguments are zero, then the returned value is 0. gcd() without arguments returns 0.

reduce(fun,seq)
    The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
'''
denominators = [2, 3, 4, 5, 6]
print(leastCommonDenominator(denominators)) # 60
