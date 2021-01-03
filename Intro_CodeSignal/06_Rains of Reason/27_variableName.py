'''
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
variableName(name) = true;
For name = "qq-q", the output should be
variableName(name) = false;
For name = "2w2", the output should be
variableName(name) = false.
'''
def variableName(name):
    if name[0].isnumeric():
        return False
    alph = string.ascii_lowercase
    big= string.ascii_uppercase
    
    nums = ['0','1','2','3','4','5','6','7','8','9','_']
    for i in name:
        if i not in alph and i not in nums and i not in big:
            return False
            print('not letter')
    return True 


def variableName2(name):
    return name.isidentifier()

def variableName3(name):

    if re.match('[a-z_][0-9_a-z]*$', name,re.IGNORECASE):
        return True
    return False

def variableName4(name):
    if not name[0].isdigit():
        for n in name:
            if n != '_' and not n.isalpha() and not n.isdigit():
                return False
        return True
    return False