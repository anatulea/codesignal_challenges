'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.'''
def palindromeRearranging(inputstring):
    char = set(inputstring)
    print(char)
    t = False
    for x in char:
        print(f'inputstring.count(x): {inputstring.count(x)%2}')
        if inputstring.count(x)%2==1 and t == True:
            return False
        elif inputstring.count(x)%2==1 and t == False:
            t= True
    return True



def palindromeRearranging2(inputString):
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1


def palindromeRearranging3(inputString):
    # count the number of each individual character
    # can form a palindrome only if:
    #   at most one of the character counts is odd, all others must be even
    l = list(inputString)
    chars = set(l)
    counts = sum([l.count(x) % 2 for x in chars])
    return counts <= 1


def palindromeRearranging4(inputString):
    s = set()
    for c in inputString:
        if c in s:
            s.remove(c)
        else:
            s.add(c)
    
    return len(s) <= 1
