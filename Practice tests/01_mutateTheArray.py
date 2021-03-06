'''
Given an integer n and an array a of length n, your task is to apply the following mutation to a:

Array a mutates into a new array b of length n.
For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].
Example

For n = 5 and a = [4, 0, 1, -2, 3], the output should be mutateTheArray(n, a) = [4, 5, -1, 2, 1].

b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
So, the resulting array after the mutation will be [4, 5, -1, 2, 1].
'''
def mutateTheArray(n, a):
    # [a[0]+a[1]]+[sum(a[x-1:x+2])for x in range(1,len(a))]if n>1 else a # one line solution
    if n <= 1:
        return a
    mylist =[a[0]+a[1]]
    for x in range(1,len(a)):
        print(x)
        if n>1:
           mylist.append(sum(a[x-1:x+2]))
        else:
          mylist = a
    return mylist

n = 5 
a = [4, 0, 1, -2, 3]
print(mutateTheArray(n, a)) #[4, 5, -1, 2, 1]
n = 1 
a = [4]
print(mutateTheArray(n, a))#[4]
n = 0 
a = []
print(mutateTheArray(n, a))#[]
n = 2 
a = [9,3]
print(mutateTheArray(n, a))#[12,12]
n = 3 
a = [3,3,3]
print(mutateTheArray(n, a))# [6, 9, 6]


# let b = a.map( (e, i, arr) => (arr[i-1] || 0)+arr[i]+(arr[i+1] || 0) ); javascript