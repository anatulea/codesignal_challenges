'''
You're given two integers, n and m. Find position of the rightmost bit in which they differ in their binary representations (it is guaranteed that such a bit exists), counting from right to left.

Return the value of 2position_of_the_found_bit (0-based).

Example

For n = 11 and m = 13, the output should be
differentRightmostBit(n, m) = 2.

1110 = 10112, 1310 = 11012, the rightmost bit in which they differ is the bit at position 1 (0-based) from the right in the binary representations.
So the answer is 21 = 2.

For n = 7 and m = 23, the output should be
differentRightmostBit(n, m) = 16.

710 = 1112, 2310 = 101112, i.e.

00111
10111
So the answer is 24 = 16.
'''
def differentRightmostBit(n, m):
    return -~((~(n^m))^((~(n^m))+1))/2

'''
The Explanation
The question essentially requires us to find it using bitwise opetations. Although there are numerous other ways to find it, I will explain the bitwise solution I had.
To solve this problem, first, we need to find the different bits. It is not as hard as it sounds. A simple XOR operation gives us what we need.
1110 = 10112, 1310 = 11012,
1110 XOR 1310 = 01102
Now, we need to find first occurence of 1 here. However, it is easier to find first occurrence of zero. The operation we use becomes XNOR (if you have, otherwise, just get NOT)
1110 XNOR 1310 = 10012
The code to do this:
(~(n^m))
Now, how do we find the first occurrence of zero in a number?
I’d like to get your attention to another operation.
What happens when we add 1 to a number (in binary representation)?
The number gets 1 added to the rightmost bit. If it was already 1, converts it to zero and it creates a carry to the next bit until it reaches to a zero. This means that, each bit until a zero bit (including that zero bit) gets converted to its complement and the remaining bits are unchanged.
So, if we can find the first unchanged bit, we find our last changed bit, which is our first zero bit. (To go from first unchanged bit to last changed bit, we can divide the number by two.)
You can test it with a couple sample numbers. Or, you can see it in my previous post HERE.
To do this, we can XNOR the number with +added number. (q XNOR (q+1)).
Our solution becomes,
q = (~(n^m))
return -~(q^(q+1))/2
You probably noticed the – sign in the answer, that is because the integers are signed according to their most significant bit in computing world and NOT operation reverses that bit too. So, we need to put – sign to get it back to positive numbers’ territory.
Because the problem wants us to give a one-liner, we replace q‘s with it’s value.
And, we get,

   return -~((~(n^m))^((~(n^m))+1))/2''
   '''


def differentRightmostBit2(n, m):
    return (n ^ m) & -(n ^ m)

def differentRightmostBit3(n, m):
    return 1 if n % 2 != m % 2 else 2 * differentRightmostBit3(n // 2, m // 2)

def differentRightmostBit4(n, m):
    return 2**skb(n,m)
def skb(a,b):
    sa=bin(a)[2:len(bin(a))].zfill(max(len(bin(a)),len(bin(b)))-2)[::-1]
    sb=bin(b)[2:len(bin(b))].zfill(len(sa))[::-1]
    i=0
    while i<len(sb):
        if sb[i]!=sa[i]:return i
        i+=1
    return i+1   