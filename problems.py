def concatenationsSum(a):
    t=sum(a)
    t1=t*len(a)
    t2=sum([t*[len(str(x))-1 for x in a].count(j)*10**(j+1) for j in range(7)])
    return t1+t2


def mutateTheArray(n, a):
    return [a[0]+a[1]]+[sum(a[x-1:x+2])for x in range(1,len(a))]if n>1 else a

def countTinyPairs(a, b, k):
    return sum([1 if int(str(x)+str(y))<k else 0for x,y in zip(a,b[::-1])])


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

            



 
 
 
