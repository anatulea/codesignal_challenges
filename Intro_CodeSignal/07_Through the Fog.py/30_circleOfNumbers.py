'''
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
circleOfNumbers(n, firstNumber) = 7.'''
def circleOfNumbers(n, firstNumber):
    if n//2+firstNumber >= n:
        return (firstNumber - n//2)
    else:
        return (n//2+firstNumber)
        

def circleOfNumbers2(n, firstNumber):

    return (firstNumber + n/2)%n

def circleOfNumbers3(n, f):
    return f-n/2 if (f-n/2)>=0 else (f-n/2)+n