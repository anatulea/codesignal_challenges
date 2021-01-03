'''
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.
'''
def evenDigitsOnly(n):
    num= str(n)
    for i in num:
        if int(i) % 2 !=0:
            return False
    return True
    

def evenDigitsOnly2(n):
    return all([int(i)%2==0 for i in str(n)])
    # return sum([int(i)%2 for i in str(n)])==0