def makeArrayConsecutive2(statues):
    count = 0
    statues.sort()
    for i in range(len(statues)-1):
        if statues[i] == statues[i+1]:
            i+=1
        else:
            count+=1
            i+=1
    return count

myarr=[0, 3]
print(makeArrayConsecutive2(myarr))