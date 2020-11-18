def concatenationsSum(a):
    t=sum(a)
    t1=t*len(a)
    t2=sum([t*[len(str(x))-1 for x in a].count(j)*10**(j+1) for j in range(7)])
    return t1+t2


def mutateTheArray(n, a):
    return [a[0]+a[1]]+[sum(a[x-1:x+2])for x in range(1,len(a))]if n>1 else a



def countTinyPairs(a, b, k):
    return sum([1 if int(str(x)+str(y))<k else 0 for x,y in zip(a,b[::-1])])



def meanGroups(a):
    d,e=[],[]
    for i,j in enumerate(a):
        if sum(j)/len(j)not in e:
            e+=[sum(j)/len(j)]
            d+=[[i]]
        else:
            d[e.index(sum(j)/len(j))]+=[i]
    return d



def alternatingSort(a):
    c,l=0,a[0]
    while c!=(len(a)-1)//2:
        c=-c if c<0 else -c-1
        if a[c]<=l:
            return False
        l=a[c]
    return True



def mergeStrings(s1, s2):
    s,o1,o2='',s1,s2
    while len(s1)*len(s2)!=0:
        if o1.count(s1[0])>o2.count(s2[0]) or (o1.count(s1[0])==o2.count(s2[0]) and s1[0]>s2[0]):
            s+=s2[0]
            s2=s2[1:]
        else:
            s+=s1[0]
            s1=s1[1:]
    return s+s1+s2



def hashMap(queryType, query):
    d,s,c1,c2={},0,0,0
    for i,j in zip(queryType,query):
        if i == 'insert':
            d[j[0]-c1]=j[1]-c2
        elif i == 'addToValue':
            c2+=j[0]
        elif i == 'addToKey':
            c1+=j[0]
        elif i== 'get':
            s+=d[j[0]-c1]+c2
    return s



def hashMap(queryType, queryType):
    hash_dict= {}
    get_total = 0
    for i, prompt in enumerate(queryType):
        if prompt == 'insert':
            hash_dict[query[i][0]] == query[i][1]
        elif prompt =='addValue':
            hash_dict= {key:val + query[i][0] for key, val in hash_dict.items()}
        elif prompt == 'addToKey':
            hash_dict= {key + query[i][0]: val for key, val in hash_dict.items()}
        elif prompt == 'get':
            get_total += hash_dict[query[i][0]]
    return get_total
        


def centuryFromYear(year):
    if year % 100 == 0:
        return year/100
    else:
        return int(year/100)+1



def firstDuplicate(a):
    s=set()
    for x in a:
        if x in s:
            return x
        else:
            s.add(x)
    return -1



def firstNonRepeatingCharacters(s):
    res ="_"
    d ={}
    for i, c in enumerate(s):
        if c in d.keys():
            d[c] =-1
        else:
            d[c] = i
    min_key = len(s)+1
    for k in d.keys():
        if d[k]>=0:
            min_key=min(min_key, d[k])
            res = s[min_key]
    return res



def mergeStrings(s1, s2):
    count1 = {}
    for i in s1:
        try:
            count1[i]+=1
        except:
            count1[i]=1
    count2 ={}
    for i in s2:
        try:
            count2[i]+=1
        except:
            count2[i]=1
    res =''
    while True:
        if s1 =='':
            return res+s2
        if s2 =='':
            return res+s1
        if count1[s1[0]]==count2[s2[0]]:
            if s1[0]==s2[0]:
                res+=s1[0]
                s1=s1[1:]
            elif s1[0]<s2[0]:
                res +=s1[0]
                s1=s1[1:]
            else:
                res+=s2[0]
                s2=s2[1:]
            continue
        else:
            if count1[s1[0]] < count2[s2[0]]:
                res+=s1[0]
                s1=s1[1:]
            else:
                res+=s2[0]
                s2=s2[1:]
            continue
    return res



def meanGrups(a):
    d, e = [], []
    for i, j in enumerate(a):
        if sum(j)/len(j) not in e:
            e+=[sum(j)/len(j)]
            d+=[[i]]
        else:
            d[e.index(sum(j)/len(j))]+=[i]
    return d



def checkPalindrome(inputString):
    return inputString == inputString[-1::-1]



def adjacetElementProduct(inputArray):
    size = len(inputArray)
    for x in range(1, size):
        prod = inputArray[x-1]*inputArray[x]
        if x == 1:
            maxprod = prod
        if prod>maxprod:
            maxprod = prod
    return maxprod


def shapeArea(n):
    area = 1
    for i in range(1, n+1):
        area = area + ((i-1)*4)
    return area


def makeArrayConsecutive2(statues):
    return len([i for i in range(min(statues), max(statues)) if i not in statues])



def almostIncreasingSequence(sequence):
    numFail = 0
    prev =sequence[0]
    for i in range(len(sequence)-1):
        if sequence[i+1]<=prev:
            numFail+=1
            if i == 0:
                prev = sequence[i+1]
            elif i<= len(sequence)-3 and sequence[i+2]<=sequence[i]:
                if sequence[i+1]>sequence[i-1]:
                    prev = sequence[i+1]
                else:
                    prev = sequence[i]
                if sequence[i+2]<=prev:
                    numFail+=1
            else:
                prev= sequence[i]
            if numFail>1:
                return False
        else:
            prev = sequence[i+1]
    return True


def matrixElementsSum(matrix):
    matrix_copy = matrix.copy()
    total = 0

    #loop over the rows
    for row in matrix:
        #loop over columns
        for col_idx in range(len(row)):
            if row[col_idx] == 0:
                #replace all 0's in the matrix under current 0 to 0s
                for i in range(matrix.index(row), len(matrix)):
                    matrix_copy[i][col_idx] = 0
    
    #find sum of all remaining numbers in matrix
    for row_copy in matrix_copy:
        total+= sum(row_copy)
    return total






 
 
 
