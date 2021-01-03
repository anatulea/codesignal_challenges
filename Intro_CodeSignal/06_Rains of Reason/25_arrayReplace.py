'''
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
'''
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    # new_list = []
    # for i in inputArray:
    #     if i == elemToReplace:
    #         new_list.append(substitutionElem)
    #     else:
    #         new_list.append(i)
    
    # return new_list
    return [i  if i != elemToReplace else substitutionElem for i in inputArray ]
  