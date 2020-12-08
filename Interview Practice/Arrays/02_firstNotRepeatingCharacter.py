'''
Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.
'''
def firstNotRepeatingCharacter(s):
    single = []
    double = []
    for i in range(len(s)):
        if s[i] in single:
            single.remove(s[i])
            double.append(s[i])
        elif s[i] in double:
            continue
        else:
            single.append(s[i])
    if len(single) == 0:
        return "_"
    else:
        return single[0]


def firstNotRepeatingCharacter2(s):
    for c in s:
        if s.index(c) == s.rindex(c): #The rindex() method returns the highest index of the substring inside the string (if found). If the substring is not found, it raises an exception.
            return c
    return '_'

def firstNotRepeatingCharacter3(s):
    chk = []
    for i in range(len(s)): 
        if s[i] not in s[i+1:] and s[i] not in chk:
            return s[i]
        chk.append(s[i])
    return '_'