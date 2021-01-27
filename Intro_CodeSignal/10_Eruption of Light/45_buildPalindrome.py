'''
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
'''
def buildPalindrome(st):
    if st == st[::-1]:
        return st
        
    ends=[]
    for i in range(1, len(st)):
        ends.append(st[:i])
    
    for i in range(len(ends)):
        print(ends[i][::-1])
        new_st= st + ends[i][::-1]
        print(f"new_str: {new_st} ---{new_st[::-1]}")
        if new_st == new_st[::-1]:
            return(new_st)


def buildPalindrome2(st):
    for i in range(0,len(st)):
        if(st[i:len(st)] == st[i:len(st)][::-1]):
            return st[0:i] + st[i:len(st)] + st[0:i][::-1]
            