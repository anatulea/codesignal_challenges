'''
 Implement a function that will turn the old-style string formating s into a new one so that the following two strings have the same meaning:

s % (*args)
s.format(*args)
Example

For s = "We expect the %f%% growth this week", the output should be
newStyleFormatting(s) = "We expect the {}% growth this week".
'''

def newStyleFormatting(s):
    s = s.split('%%') 
    print(s)# s = ["We expect the %f", "growth this week"]
    for i in range(len(s)):
        while '%' in s[i]:
            idx = s[i].find('%') # find the % index
            # modify string "We expect the " + {} + the rest of string
            s[i] = s[i][:idx] + '{}' + s[i][idx + 2:]
    return '%'.join(s)


import re
def newStyleFormatting2(s):
    return re.sub('%\w','{}', s.replace('%%','{%}')).replace('{%}','%')


def newStyleFormatting3(s):
    s = re.sub('%%', '{%}', s) 
    #  re.sub(pattern we look for, replacement, string, count=0, flags=0)

    s = re.sub('%[dfFgeEGnnxXodcbs]', '{}', s)
    return re.sub('{%}','%',s)


import re
def newStyleFormatting4(s):
    return "%".join([re.sub("%([bcdeEfFgGnosxX])","{}",S) for S in s.split("%%")])

def newStyleFormatting5(s):
    return '%'.join(re.sub('%\w', '{}', part) for part in s.split('%%'))