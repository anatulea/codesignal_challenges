'''
CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

Example

For inputString = "2 apples, 12 oranges", the output should be
sumUpNumbers(inputString) = 14.'''
def sumUpNumbers(inputString):
    num = ''
    all_nums =[]
    
    for i in range(len(inputString)):
        if inputString[i].isnumeric():
            num+=inputString[i]
        else:
            if num != '':
                all_nums.append(num)
                num =''
                
    if num != '':
        all_nums.append(num)
        
    if len(all_nums) ==0:
        return 0
    
    return sum([int(num) for num in all_nums])


import re
def sumUpNumbers2(inputString):
    l = re.findall(r"\d+",inputString)
    return sum([int(i) for i in l])


def sumUpNumbers3(s):
    return sum(map(int,"".join([i if i.isdigit() else " " for i in s]).split()))