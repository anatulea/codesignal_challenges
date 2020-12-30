'''
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

Example

For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = false.'''

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft == friendsLeft and yourRight == friendsRight:
        return True
    elif yourLeft == friendsRight and yourRight == friendsLeft:
        return True
    else:
        return False


def areEquallyStrong2(yourLeft, yourRight, friendsLeft, friendsRight):
    return {yourLeft, yourRight} == {friendsLeft, friendsRight}


def areEquallyStrong3(yourLeft, yourRight, friendsLeft, friendsRight):
    return sorted([yourLeft,yourRight])==sorted([friendsLeft,friendsRight])

def areEquallyStrong4(ul, ur, fl, fr):
     return max(ul,ur)==max(fl,fr) and min(ul,ur)==min(fl,fr)