'''
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.'''

def areSimilar(a,b):
    count=0
    if sum(a)!= sum(b) or len(a)!= len(b):
        return False
    else:
        for i in range(len(a)):
            if (a[i]!= b[i]):
                count+=1
        return count <= 2 and sorted(a)== sorted(b)



def areSimilar2(A, B):
    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2



from collections import Counter as C
def areSimilar3(A, B):
    return C(A) == C(B) and sum(a != b for a, b in zip(A, B)) < 3



def areSimilar4(A, B):

    r = []
    for i in range(len(A)):
        if A[i] != B[i]:
            r.append([A[i],B[i]])
            
    if len(r) == 0 or len(r) == 2 and r[0]==r[1][::-1]:
        return True
    return False