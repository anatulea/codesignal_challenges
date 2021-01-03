'''
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".
'''
import string
def alphabeticShift(inputString):
    alph = string.ascii_lowercase
    result= []
    d = {}
    
    for idx, letter in enumerate(alph):
        if letter != 'z':
            d[letter]= alph[idx+1]
        else:
            d[letter]= alph[0]
    
    for letter in inputString:
        result.append(d[letter])
        
    return ''.join(result)


def alphabeticShift2(s):
    return "".join(chr((ord(i)-96)%26+97) for i in s)


def alphabeticShift3(inputString):
    return ''.join((chr(ord(i)+1) if i!="z" else "a" for i in inputString))


from string import ascii_lowercase as a
def alphabeticShift4(s):
    return "".join([a[a.find(i)-25] for i in s])