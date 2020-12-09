'''
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
'''
def allLongestStrings(inputArray):
    max_len = 0
    alllongstrings = []
    for string in inputArray:
        if len(string)> max_len:
            max_len = len(string)
    for string in inputArray:
        if len(string) == max_len:
            alllongstrings.append(string)    
    return alllongstrings 

def allLongestStrings1(inputArray):
    result = list()
    max_len = 0
    for _str  in inputArray:
        _len = len(_str)
        if _len>max_len:
            max_len = _len
            result = [_str]
            continue
        if _len == max_len:
            result.append(_str)
            continue
    return result

def allLongestStrings2(inputArray):
    result = list()
    max_str_len = 0
    for i in inputArray:
        if max_str_len < len(i):
            max_str_len = len(i)

    for j in inputArray:
        if len(j) == max_str_len:
            result.append(j)

    return result

def allLongestStrings3(inputArray):
    m = max(len(s) for s in inputArray)
    r = [s for s in inputArray if len(s) == m]
    return r