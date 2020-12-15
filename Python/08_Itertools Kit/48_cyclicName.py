'''
You've come up with a really cool name for your future startup company, and already have an idea about its logo. This logo will represent a circle, with the prefix of a cyclic string formed by the company name written around it.

The length n of the prefix you need to take depends on the size of the logo. You haven't yet decided on it, so you'd like to try out various options. Given the name of your company, return the prefix of the corresponding cyclic string containing n characters.

Example

For name = "nicecoder" and n = 15, the output should be
cyclicName(name, n) = "nicecoderniceco".
'''
from itertools import cycle
# Itertools is a module that provides various functions that work on iterators to produce complex iterators.
def cyclicName(name, n):
    gen = cycle(name) # defining iterator 
    res = [next(gen) for _ in range(n)]  # Using next function to take the first n char
    return ''.join(res) 

'''  Infinite iterators
        - count(start, step): This iterator starts printing from the “start” number and prints infinitely. If steps are mentioned, the numbers are skipped else step is 1 by default.
        
'''
