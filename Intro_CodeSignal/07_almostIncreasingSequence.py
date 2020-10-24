'''
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 105,
-105 ≤ sequence[i] ≤ 105.

[output] boolean

Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.
'''


# it works but not in all cases 
# def almostIncreasingSequence(sequence):
#     not_in_sequence =[]
#     for i in range(len(sequence)-1):
#         if sequence[i] == (sequence[i+1])-1:
#             print(sequence[i])
#             i=i+1
#         else:
#             print(f'else:{sequence[i+1]}')
#             if sequence[i+1] in not_in_sequence:
#                 i=i+1
#             else:
#                 not_in_sequence.append(sequence[i+1])
#                 i=i+1
#     print(not_in_sequence)
#     return len(not_in_sequence)-1 >= 1       
          
# myarr = [1, 1, 2, 3, 4, 4]#[10, 1, 2, 3, 4, 5]  #[1, 1, 2, 3, 4, 4]
# print(almostIncreasingSequence(myarr))



def almostIncreasingSequence(list):
  removedIdx = []                   #Indexes that need to be removed

  for idx, item in enumerate(list):
    print(f"{idx, item}")
    tmp = []                        #Indexes between current index and 0 that break the increasing order
    for i in range(idx-1, -1, -1):
        if list[idx]<=list[i]:        #Add index to tmp if number breaks order
            tmp.append(i)
    if len(tmp)>1:                  #If more than one of the former numbers breaks order  
        removedIdx.append(idx)        #Add current index to removedIdx
    else:
        if len(tmp)>0:                #If only one of the former numbers breaks order
            removedIdx.append(tmp[0])   #Add it to removedIdx
  return len(set(removedIdx))<=1 

myarr = [1, 1, 2, 3, 4, 4]#[10, 1, 2, 3, 4, 5]  #[1, 1, 2, 3, 4, 4]
print(almostIncreasingSequence(myarr))



# VVVVVVVVVVVVVVVVVV
# This version passes all the tests on codesignal
def almostIncreasingSequence(sequence):

    #Take out the edge cases
    if len(sequence) <= 2:
        return True

    #Set up a new function to see if it's increasing sequence
    def IncreasingSequence(test_sequence):
        if len(test_sequence) == 2:
            if test_sequence[0] < test_sequence[1]:
                return True
        else:
            for i in range(0, len(test_sequence)-1):
                if test_sequence[i] >= test_sequence[i+1]:
                    return False
                else:
                    pass
            return True

    for i in range (0, len(sequence) - 1):
        if sequence[i] >= sequence [i+1]:
            #Either remove the current one or the next one
            test_seq1 = sequence[:i] + sequence[i+1:]
            test_seq2 = sequence[:i+1] + sequence[i+2:]
            if IncreasingSequence(test_seq1) == True:
                return True
            elif IncreasingSequence(test_seq2) == True:
                return True
            else:
                return False
