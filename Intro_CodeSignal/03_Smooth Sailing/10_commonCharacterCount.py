'''
Given two strings, find the number of common characters between them.

Example
For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
'''
def commonCharacterCount(s1, s2):
    count = 0
    commons = set(s1) & set(s2)
    for i in commons:
        count += min(s1.count(i), s2.count(i))
    return count

# ##method 2
def commonCharacterCount2(s1, s2):
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return sum(com)

def commonCharacterCount3(s1, s2):
    return sum(min(s1.count(x), s2.count(x)) for x in set(s1))