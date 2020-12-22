'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
'''
def sortByHeight(a):
    b = sorted([i for i in a if i!=-1])
    print(b)
    j = 0
    for i in range(len(a)):
        if a[i] == -1:
            pass
        else:
            a[i]=b[j]
            j+=1
    return a

def sortByHeight2(a):
    people = sorted(filter(lambda x: x != -1, a))
    return [people.pop(0) if i != -1 else -1 for i in a]

def sortByHeight3(a):
    humans = sorted([x for x in a if x != -1])
    output = [humans.pop(0) if a[x]!=-1 else -1 for x in range(0,len(a))]
    return(output)