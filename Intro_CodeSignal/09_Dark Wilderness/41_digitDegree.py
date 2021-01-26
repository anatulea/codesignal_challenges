"""Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
digitDegree(n) = 0;
For n = 100, the output should be
digitDegree(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
digitDegree(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1."""
def digitDegree(n):

    c = 0
    while (n >= 10):
        n = sum(int(d) for d in str(n))
        c += 1
    return c


def digitDegree2(n):
    count = 0
    
    while True:
        if n <= 9:
            return count
        else:
            sum1=0
            while n:
                sum1+= n%10
                n=n//10
            n = sum1
            count+=1
            
    #return count