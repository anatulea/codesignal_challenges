'''
You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. Calculate how many distinct ways you can climb to the top of the staircase.

Example

For n = 1, the output should be
climbingStairs(n) = 1;

For n = 2, the output should be
climbingStairs(n) = 2.

You can either climb 2 steps at once or climb 1 step two times.
'''
#Time complexity O(n)  space complexity O(n)
def climbingStairs(n):
    steps = {}
    steps[0] = 1
    steps[1]= 1
    
    for i in range(2, n+1):
        steps[i]= steps[i-1] + steps[i-2]
    return steps[n]


# BETTER SPACE COMPLEXITY
def climbingStairs2(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = a + b, a
    return a

def climbingStairs3(n):
    if n == 1:
        return 1
    first = 1
    second = 2
    n -= 2
    while n > 0:
        t = first
        first = second
        second = first + t
        n -= 1
    return second

print(climbingStairs(7))