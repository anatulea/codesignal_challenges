'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example
For
picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
'''
def addBorder(picture):
    starts = (len(picture[0])+2)*'*'
    
    for i in range(len(picture)):
        picture[i] = '*'+ picture[i] + '*'
    picture.insert(0,starts)
    picture.insert(len(picture), starts)   

    return picture



def addBorder2(picture):
    l=len(picture[0])+2
    return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]



def addBorder3(picture):

    r = ['*'*(len(picture[0])+2)]
    for i in picture:
        r.append('*' + i + '*')
    r.append(r[0])
    return r