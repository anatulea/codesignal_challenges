'''
Determine if the given character is a digit or not.

Example

For symbol = '0', the output should be
isDigit(symbol) = true;
For symbol = '-', the output should be
isDigit(symbol) = false.
'''
def isDigit(symbol):
    nums = '1234567890'
    return (symbol in nums)
    # return symbol.isdigit()