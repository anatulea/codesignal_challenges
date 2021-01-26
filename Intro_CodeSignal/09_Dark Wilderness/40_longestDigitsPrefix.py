'''
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
longestDigitsPrefix(inputString) = "123".
'''
def longestDigitsPrefix(inputString):
    prefix =[]
    for i in inputString:
        if i.isdigit():
            prefix.append(i)
        else:
            break
    
    return ''.join(prefix)

import re
def longestDigitsPrefix2(inputString):
    return re.findall('^\d*',inputString)[0]


def longestDigitsPrefix3(inputString):
    digit = ''
    for x in inputString:
        if x.isdigit():
            digit+=x
        else:
            break
    return digit
