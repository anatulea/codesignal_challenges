'''Given the string, check if it is a palindrome.

Example
For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;

For inputString = "abac", the output should be
checkPalindrome(inputString) = false;

For inputString = "a", the output should be
checkPalindrome(inputString) = true.
'''

def checkPalindrome(inputString):
    # return word == word[::-1] # one line solution
    new = inputString[::-1]
    if inputString == new:
        return True
    else:
        return False
