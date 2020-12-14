 '''
 implementing a function that will replace all multiple space characters 
 in the given line of your code with single ones.
 In addition, all leading and trailing whitespaces should be removed.

Example
For
line = "def      m   e  gaDifficu     ltFun        ction(x):"
the output should be
catWalk(line) = "def m e gaDifficu ltFun ction(x):".
'''
def catWalk(code):
    return ' '.join(code.split())
