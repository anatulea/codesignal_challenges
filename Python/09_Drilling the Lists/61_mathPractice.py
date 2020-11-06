'''
Little Billy is not too good with numbers and having trouble even multiplying and adding them. He needs some practice, and you are the one helpful fellow who can give him a list of numbers to practice on. Given a list of numbers, Billy should calculate the following value:

(((...(a[0] + a[1]) * a[2] + a[3]) * a[4] + ...)
Unfortunately you yourself are not too good with math, but you know how to code. Implement a function that, given a list of numbers, will return the result of the operation Billy has to perform.

Example

For numbers = [1, 2, 3, 4, 5, 6], the output should be
mathPractice(numbers) = 71.

Here's how the answer is obtained: ((1 + 2) * 3 + 4) * 5 + 6 = 71.
'''
# reduce(function, iterable, initializer=None)
def mathPractice(numbers):
    return functools.reduce(lambda x,y: (x+y[1]) if y[0]%2 else x*y[1], enumerate(numbers), 1)
    # return reduce(lambda x, (i,y): x+y if i%2 else x*y, enumerate(numbers), 1)
    # return reduce(lambda z,(x,y):z*x+y, zip(numbers[::2],numbers[1::2]+[0]), 1)
    # return functools.reduce(lambda s, a: s+numbers[a] if a%2==1 else s*numbers[a], range(1, len(numbers)), numbers[0])
