'''
Your friend has been doodling during the lecture and wrote down several digits in a circle. You're wondering if these digits might form the password to your friend's computer. You're planning to prank him some time in the future, and hacking into his computer will definitely help. If the digits written in the clockwise order indeed form a password, all you need to do is figure out which digit comes in it first.

Given a list of digits as they are written in the clockwise order, find all other combinations the password could possibly have.

Example

For digits = [1, 2, 3, 4, 5], the output should be

doodledPassword(digits) = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2],
                           [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
'''
from collections import deque

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    print(res) # [deque([1, 2, 3, 4, 5]), deque([1, 2, 3, 4, 5]), deque([1, 2, 3, 4, 5]), deque([1, 2, 3, 4, 5]), deque([1, 2, 3, 4, 5])]

    deque(map(lambda x: res[x].rotate(-x), range(n)), 0)
    print(res) #[deque([1, 2, 3, 4, 5]), deque([2, 3, 4, 5, 1]), deque([3, 4, 5, 1, 2]), deque([4, 5, 1, 2, 3]), deque([5, 1, 2, 3, 4])]

    return [list(d) for d in res]

digits = [1, 2, 3, 4, 5]
print(doodledPassword(digits))
'''
class collections.deque([iterable[, maxlen]])
    - Returns a new deque object initialized left-to-right (using append()) with data from iterable.

Let’s see various Operations on deque :
    - append() :- This function is used to insert the value in its argument to the right end of deque.
    - appendleft() :- This function is used to insert the value in its argument to the left end of deque.
    - pop() :- This function is used to delete an argument from the right end of deque.
    - popleft() :- This function is used to delete an argument from the left end of deque.   
    - index(ele, beg, end) :- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
    - insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
    - remove() :- This function removes the first occurrence of value mentioned in arguments.
    - count() :- This function counts the number of occurrences of value mentioned in arguments.
    - extend(iterable) :- This function is used to add multiple values at the right end of deque. The argument passed is an iterable.
    - extendleft(iterable) :- This function is used to add multiple values at the left end of deque. The argument passed is an iterable. Order is reversed as a result of left appends.
    - reverse() :- This function is used to reverse order of deque elements.
    - rotate() :- This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to left. Else rotation is to right.

'''