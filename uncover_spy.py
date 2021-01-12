'''
In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.

The spy, if it exists:

Does not trust anyone else.
Is trusted by everyone else (he's good at his job).
Works alone; there are no other spies in the city-state.
You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.

If the spy exists and can be found, return their identifier. Otherwise, return -1.

Example 1:

Input: n = 2, trust = [[1, 2]]
Output: 2
Explanation: Person 1 trusts Person 2, but Person 2 does not trust Person 1, so Person 2 is the spy.
Example 2:

Input: n = 3, trust = [[1, 3], [2, 3]]
Output: 3
Explanation: Person 1 trusts Person 3, and Person 2 trusts Person 3, but Person 3 does not trust either Person 1 or Person 2. Thus, Person 3 is the spy.
Example 3:

Input: n = 3, trust = [[1, 3], [2, 3], [3, 1]]
Output: -1
Explanation: Person 1 trusts Person 3, Person 2 trusts Person 3, and Person 3 trusts Person 1. Since everyone trusts at least one other person, there is no spy.
Example 4:

Input: n = 3, trust = [[1, 2], [2, 3]]
Output: -1
Explanation: Person 1 trusts Person 2, and Person 2 trusts Person 3. However, in this situation, we don't have any one person who is trusted by everyone else. So we can't determine who the spy is in this case.
Example 5:

Input: n = 4, trust = [[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]]
Output: 3
Explanation: Person 1 trusts Person 3 and Person 4, Person 2 trusts Person 3 and Person 4, Person 4 trusts Person 3. Everyone trusts Person 3 but Person 3 does not trust anyone, so they are the spy.
'''
def uncover_spy(n, trust):
    table = {}
    count = 0
    possible_spy = []
    for pair in trust:
        if pair[0] not in table:
            table[pair[0]]= pair[1]
    print(table)
    print(list(table.values()))
    for k, v in table.items():
        if v not in table:
            count+=1
            possible_spy.append(v)
            print('possible spy')
            
    myset=set(possible_spy)
    d = []
    if len(possible_spy)==1:
        d.append(possible_spy[0])
    for x in possible_spy:
        if x in myset:
            myset.remove(x)
        else:
            d.append(x)
    print(f"d: {d}")
    
    if n-count == 1 and len(d)!=0:
        return d[0]
        print("there is a spy")
    else:
        return -1




'''Given a non-empty integer array numbers, you may perform increment operations, each of which increases one of the values of the array by 1. Your task is to find the minimum number of increment operations required to make all the array elements unique.

Note: You can increment the same array element multiple times.

Example

For numbers = [5, 1, 2, 4, 5, 2], the output should be obtainUniqueSequence(numbers) = 2.

Explanation:

One way to make all the elements unique is to increment numbers[0] and numbers[2], after which the array will look like numbers = [6, 1, 3, 4, 5, 2]. Because 2 increment operations were performed, the answer is 2.
'''


''''
You are given a matrix of characters representing a big box. Each cell of the matrix contains one of three characters:

'.', which means that the cell is empty;
'*', which means that the cell contains an obstacle;
'#', which means that the cell contains a small box.
You decide to rotate the big box clockwise to see how the small boxes will fall under the gravity. After rotating, each small box falls down until it lands on an obstacle, another small box, or the bottom of the big box.

Given box, a matrix representation of the big box, your task is to return the state of the box after rotating it clockwise.

Example

For
box = [['#', '#', '.', '.', '.', '.', '.'],
       ['#', '#', '#', '.', '.', '.', '.'],
       ['#', '#', '#', '.', '.', '#', '.']]
the output should be

rotateAndFall(box) = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.'],
                      ['#', '.', '.'],
                      ['#', '#', '.'],
                      ['#', '#', '#'],
                      ['#', '#', '#']]
example1

For
box = [['#', '#', '.', '.', '.', '#', '.'],
       ['#', '#', '#', '.', '.', '*', '.'],
       ['#', '#', '#', '*', '.', '#', '.']]
the output should be

rotateAndFall(box) = [['#', '.', '.'],
                      ['#', '.', '.'],
                      ['#', '#', '.'],
                      ['*', '#', '.'],
                      ['.', '#', '#'],
                      ['.', '*', '#'],
                      ['#', '.', '#']]
example2

''''
'''
You are given numbers, an array of non-negative integers. Your task is to perform the following algorithm on this array:

Step 1. Find the index i of the leftmost non-zero element numbers[i] = x ≠ 0. If there is no such element, finish the algorithm.
Step 2. Starting at index i and going to the right, attempt to subtract x from each element
If the element is strictly less than x, move on to step 3;
Otherwise, subtract x from the element and move on to the next element;
If you reach the end of the array, move on to step 3.
Step 3. Add x to the final result.
Step 4. Go back to step 1.
Return the resulting sum obtained from step 3. It is guaranteed that the algorithm is finite and will finish at some point.

Example

For numbers = [3, 3, 5, 2, 3], the output should be sumOfFirsts(numbers) = 6.

example 1

On the first iteration you find the leftmost non-zero element numbers[0] = 3 and subtract 3 from numbers[0] = 3, numbers[1] = 3, and numbers[2] = 5. You obtain new array [0, 0, 2, 2, 3] and add 3 to the final result.
Going back to step 1, array is now [0, 0, 2, 2, 3]. The leftmost non-zero element is numbers[2] = 2, so you subtract it from numbers[2] = 2, numbers[3] = 2, and numbers[4] = 3. You obtain new array [0, 0, 0, 0, 1] and add 2 to the final result.
For the remaining array [0, 0, 0, 0, 1], the leftmost non-zero element is numbers[4] = 1. You decrease this last non-zero element by 1, add 1 to the final result and finish the algorithm.
The answer is 3 + 2 + 1 = 6.

For numbers = [5, 5, 5, 5], the output should be sumOfFirsts(numbers) = 5.

example 2

On the first step you find the leftmost non-zero element numbers[0] = 5.
On the second step you decrease all array elements by 5, because there is no element strictly less than 5.
The array now contain only zeros, non-zero element doesn't exist, so the algorithm finishes its work.
'''

def sumOfFirsts(numbers):
    result_sum =0
    for x in range(len(numbers)):
        if numbers[x] > 0:
            print("not zero")
            for i in range(len(numbers)):
                if numbers[i]< numbers[x]:
                    result_sum +=numbers[x]
                else:
                    
                    numbers[i] -=numbers[x]
                    i+=1
                    print(numbers)
        else:
            return numbers[x]
    return(result_sum)




"""
Given an integer n, your task is to calculate the alternating sum of its digits. In other words, add up all the digits, alternating between positive and negative.

For example, if n = 52134, the answer should be 5 - 2 + 1 - 3 + 4 = 5.

Example

For n = 52134, the output should be numberSigningSum(n) = 5.

5 - 2 + 1 - 3 + 4 = 5

For n = 12345, the output should be numberSigningSum(n) = 3.

1 - 2 + 3 - 4 + 5 = 3

For n = 104956, the output should be numberSigningSum(n) = -5.

1 - 0 + 4 - 9 + 5 - 6 = -5
"""

def numberSigningSum(n):
    str_num = str(n)
    total_sum = int(str_num[0])
    for i in range(1,len(str_num)):
        if i %2 == 0:
            total_sum = total_sum + int(str_num[i])
        else:
            total_sum = total_sum - int(str_num[i])
        print(total_sum)
    return total_sum