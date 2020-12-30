'''
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
'''
def arrayMaximalAdjacentDifference(inputArray):
    max_num = 0
    for i in range(len(inputArray)-1):
        adj_diff= abs(inputArray[i]- inputArray[i+1])
        if max_num < adj_diff:
            max_num = adj_diff
    return max_num

def arrayMaximalAdjacentDifference2(a):
    diffs=[abs(a[i]-a[i+1]) for i in range(len(a)-1)]
    return max(diffs)


def arrayMaximalAdjacentDifference3(inputArray):
    return max([abs(i - j) for i, j in zip(inputArray, inputArray[1:])])