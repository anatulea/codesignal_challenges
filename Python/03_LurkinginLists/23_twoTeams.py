'''
There are some students standing in a row, each has some number written on their back. The students are about to divide into two teams by counting off by twos: those standing at the even positions (0-based) will go to team A, and those standing at the odd position will join the team B.

Your task is to calculate the difference between the sums of numbers written on the backs of the students that will join team A, and those written on the backs of the students that will join team B.

Example

For students = [1, 11, 13, 6, 14], the output should be
twoTeams(students) = 11.

Students with numbers 1, 13 and 14 will join team A, and students with numbers 11 and 6 will join team B. Thus, the answer is (1 + 13 + 14) - (11 + 6) = 11.
'''
from functools import reduce
def twoTeams(students):
    return sum(students[0::2])- sum(students[1::2])

def twoTeams2(students):
    return sum( (-1)**i*I for i,I in enumerate(students))


def twoTeams3(students):
    return sum([students[i] if i % 2 == 0 else -students[i] for i in range(0, len(students))])

def twoTeams4(students):
    return reduce(lambda x,y:x+y[1] if y[0]%2==0 else x-y[1],enumerate(students),0)
    '''functools.reduce(function, iterable[, initializer]):
    Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value. '''

def twoTeams5(students):
    return sum([s for index,s in enumerate(students) if index%2==0])-sum([s for index,s in enumerate(students) if index%2!=0])