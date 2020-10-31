#Implement a function that, given an integer n, will return the number of bits in its binary representation.

#Example

#For n = 50, the output should be
#countBits(n) = 6.

# 50_10 = 110010_2, a number that consists of 6 digits. Thus, the output should be 6.

def countBits(n):
    return n.bit_length()