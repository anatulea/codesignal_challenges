'''
Not long ago a young Christmas elf asked you to implement a function that creates Christmas trees made of asterisks ('*') similar to the one below:

    *    
    *    
   ***   
  *****  
 ******* 
*********
   ***   
Unfortunately because of the extreme coldness the tree that you sent over was corrupted: although its lines are given in the correct order, but are not aligned properly. Now your task is to fix the given tree by centering the asterisks in each line.

Example

For

tree = [
  "      *  ", 
  "    *    ", 
  "***      ", 
  "    *****", 
  "  *******", 
  "*********", 
  " ***     "
]
the output should be

fixTree(tree) = [
  "    *    ", 
  "    *    ", 
  "   ***   ", 
  "  *****  ", 
  " ******* ", 
  "*********", 
  "   ***   "
]
'''
def fixTree(tree):
    return list(map(lambda s: s.strip().center(len(s)), tree))

#   The .strip() method without any arguement removes the spaces from the string
#   Then the .center() method takes the */s and centers them 
# 
# Other solutions:

#   return [x.strip().center(len(x))for x in tree]

#   return [" "*int((len(x) - len(x.strip()))/2) + x.strip() + " "*int((len(x) - len(x.strip()))/2) for x in tree]
#   return map(lambda x: ' ' * (x.count(' ') / 2) + '*' * x.count('*') + ' ' * (x.count(' ') / 2), tree)


def fixTree2(tree):
    theNewTree = []
    for s in tree:
        # stars = s.strip() # remove spaces
        # stars = s.replace(" ", "") # remove spaces
        stars = "".join(s.split()) # remove spaces

        centered = stars.center(len(s)," ") # .center method takes 2 params,  -len : The width of string to expand it. and  fillchr (optional): The character to fill in remaining space , if the second param is missing it takes space as default 

        theNewTree.append(centered)
    return theNewTree

tree = [
  "      *  ", 
  "    *    ", 
  "***      ", 
  "    *****", 
  "  *******", 
  "*********", 
  " ***     "
]
print(fixTree2(tree))
# [
# '    *    ',
# '    *    ', 
# '   ***   ', 
# '  *****  ',
# ' ******* ',
# '*********', 
# '   ***   ']