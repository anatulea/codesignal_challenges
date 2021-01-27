'''
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

Example

For inputString = "00-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = false;
For inputString = "not a MAC-48 address", the output should be
isMAC48Address(inputString) = false.'''
import string
def isMAC48Address(inputString):
    
    acceptable= string.hexdigits
    new_string = inputString.split('-')
    print(new_string)
    
    if len(inputString) != 17:
        return False
    else:
        for i in new_string:
            if len(new_string)!=6:
                return False
            for j in i:
                if j  in acceptable:
                    continue
                else:
                    return False
        return True
    
import re
def isMAC48Address2(s):
    return bool(re.match(('^' + '[\dA-F]{2}-' * 6)[:-1] + '$', s))
