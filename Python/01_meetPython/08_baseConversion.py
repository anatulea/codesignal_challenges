
'''
Implement a function that, given an integer number n and a base x, converts n from base x to base 16.

Example

For n = "1302" and x = 5, the output should be
baseConversion(n, x) = "ca".

Here's why:
13025 = 20210 = ca16.

'''
# hex(x)
# Convert an integer number (of any size) to a lowercase hexadecimal string prefixed with “0x”, for example:

# >>> hex(255)
# '0xff'
# >>> hex(-42)
# '-0x2a'
# >>> hex(1L)
# '0x1L'


def baseConversion(n, x):
    # hex is a function to  convert an integer number into it’s corresponding hexadecimal form.
    return hex(int(n,x))[2:] # [2:] is used to remove the prefix "0x"
    # return format(int(n,x), 'x')
    # return '{0:x}'.format(int(n,x))

def baseConversion2(n, x):
    return hex(sum((int(n[i]) if n[i] <= '9' else ord(n[i]) - ord('a') + 10) * x ** (len(n) - 1 - i) for i in range(len(n))))[2:]