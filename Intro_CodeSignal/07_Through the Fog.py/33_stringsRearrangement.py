'''
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false.

There are 6 possible arrangements for these strings:

["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]
None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.
'''
import itertools

def stringsRearrangement(inputArray):
    permutations = itertools.permutations(inputArray)
    for array in permutations:
        if testArrangement(array):
            return True
    return False

def testArrangement(array):
    for i in range(len(array) - 1):
        if sum([a != b for a, b in zip(array[i], array[i + 1])]) != 1:
            return False
    return True


from itertools import permutations as p
def stringsRearrangement1(inputArray):
    for ia in p(inputArray):
        c = 0
        for i in range(len(ia) - 1):
            for j in range(len(ia[i])):
                if ia[i][j] != ia[i+1][j]: c += 1
            if ia[i] == ia[i+1]: c += 10
        if c == len(ia) - 1: return True
    return False