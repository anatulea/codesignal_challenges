'''
Here's how permutation cipher works: the key to it consists of all the letters of the alphabet written up in some order. All occurrences of letter 'a' in the encrypted text are substituted with the first letter of the key, all occurrences of letter 'b' are replaced with the second letter from the key, and so on, up to letter 'z' replaced with the last symbol of the key.
Given the password you always use, your task is to encrypt it using the permutation cipher with the given key.

Example
For password = "iamthebest" and
key = "zabcdefghijklmnopqrstuvwxy", the output should be
permutationCipher(password, key) = "hzlsgdadrs".

Here's a table that can be used to encrypt the text:

abcdefghijklmnopqrstuvwxyz
||  |  ||   |     || 
vv  v  vv   v     vv
zabcdefghijklmnopqrstuvwxy
'''
def permutationCipher(password, key):
    ''' string.maketrans - Returns a translation table usable for str.translate()'''
    
    table = str.maketrans(string.ascii_lowercase, key) 
    '''string.ascii_lowercase is Concatenation of lowercase letters'''
    # https://www.programiz.com/python-programming/methods/string/maketrans
    
    return password.translate(table)


# import string library function 
import string 

# Ascii_letters is a pre-initialized string used as string constant. 
# Storing the value in variable result 
result = string.ascii_letters 
  
# Printing the value 
print(result) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ