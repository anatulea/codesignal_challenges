'''
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
lineEncoding(s) = "2a3bc".'''
def lineEncoding(s):
    char_repeating = []
    substring = ''
    first = s[0]
    
    for idx, let in enumerate(s):
        if let == first:
           substring= substring+let
        else:
            char_repeating.append(substring)
            substring = ''
            first = let
            substring += first
    char_repeating.append(substring)
    
    
    result_list= []
    for pair in char_repeating:
        if len(pair) != 1:
            result_list.append(str(len(pair)))
            result_list.append(pair[0])
        else:
            result_list.append(pair[0])
   
    return ''.join(result_list)


from itertools import groupby
def lineEncoding2(s):
    x = ''
    for k,g in groupby(s):
        y = len((list(g)))
        if y==1:
            x += k
        else:
            x += str(y) + k
    return x