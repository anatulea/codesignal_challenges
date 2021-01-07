'''
Given a sorted array of integers a, your task is to determine which element of a is closest to all other values of a. In other words, find the element x in a, which minimizes the following sum:

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
(where abs denotes the absolute value)

If there are several possible answers, output the smallest one.

Example

For a = [2, 4, 7], the output should be absoluteValuesSumMinimization(a) = 4.

for x = 2, the value will be abs(2 - 2) + abs(4 - 2) + abs(7 - 2) = 7.
for x = 4, the value will be abs(2 - 4) + abs(4 - 4) + abs(7 - 4) = 5.
for x = 7, the value will be abs(2 - 7) + abs(4 - 7) + abs(7 - 7) = 8.
The lowest possible value is when x = 4, so the answer is 4.

For a = [2, 3], the output should be absoluteValuesSumMinimization(a) = 2.

for x = 2, the value will be abs(2 - 2) + abs(3 - 2) = 1.
for x = 3, the value will be abs(2 - 3) + abs(3 - 3) = 1.
Because there is a tie, the smallest x between x = 2 and x = 3 is the answer.
'''
def absoluteValuesSumMinimization(a):
    result_table= {}
    total_sum = 0
    
    for num in a:
        for i in range(len(a)):
            total_sum = total_sum + abs(a[i]-num)
        result_table[num]=total_sum
        total_sum=0
    min_output = min(result_table.values())
    
    
    return(list(result_table.keys())[list(result_table.values()).index(min_output)])


def absoluteValuesSumMinimization2(A):
    return A[(len(A)-1)//2]
    # return A[len(A)//2-(len(A)%2==0)]


import statistics
def absoluteValuesSumMinimization3(a):
    return statistics.median_low(a)