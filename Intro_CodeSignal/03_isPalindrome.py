'''
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
'''
def checkPalindrome(inputString):
    new = inputString[::-1]
    if inputString == new:
        return True
    else:
        return False

    # return inputString == inputString[::-1]

    # checkPalindrome = lambda s: s[::-1] == s

# cheking the first half with the reversed second half 
def checkPalindrome(inputString):
    for i in range(len(inputString) // 2):
        if inputString[i] != inputString[-i - 1]:
            return False
    return True