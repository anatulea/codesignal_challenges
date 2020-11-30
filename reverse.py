# Given a string , we need to reverse it using recursion (and iteration)
# For example, input = "Zero To Mastery", output = "yretsaM oT oreZ"

# First we will implement the iterative solution
# Here we use a second string to store the reversed version. Time and Space complexity = O(n)
def iterative_reverse(string):
    reversed_string = ''
    for i in range(len(string)):
        reversed_string = reversed_string + string[len(string)-i-1]
    return reversed_string


print(iterative_reverse("Zero To Mastery"))
'''
Here we append the string backwards into the original string itself and then slice it to contain only the 2nd half,i.e.,the reversed part.
Time complexity = O(n). Space complexity = O(n)
'''

def second_iterative_reverse(string):
    original_length = len(string)
    for i in range(original_length):
        string = string + string[original_length - i - 1]
        print(string)
    string = string[original_length:] #Zero To MasteryyretsaM oT oreZ
    return string


print(second_iterative_reverse("Zero To Mastery"))



def recursive_reverse(string):
    print(string)
    if len(string) == 0:
        return string
    else:
        return recursive_reverse(string[1:]) + string[0]


print(recursive_reverse("Zero To Mastery"))