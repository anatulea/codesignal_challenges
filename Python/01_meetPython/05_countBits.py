#Implement a function that, given an integer n, will return the number of bits in its binary representation.

#Example

#For n = 50, the output should be
#countBits(n) = 6.

# 50(base_10) = 110010(base_2), a number that consists of 6 digits. Thus, the output should be 6.

def countBits(n):
    return n.bit_length()

n= 1000000000
print(countBits(n)) # 30
n2= 237487384
print(countBits(n2)) # 28