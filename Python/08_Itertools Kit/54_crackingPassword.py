'''
You've been trying to crack the password from your friend's laptop (just to prank him, malicious intent!), but with no luck. However, looks like you're finally up to something: you checked the keyboard with the "little detective" game set and determined that the password consists of a limited set of digits.

You've seen your friend typing the password quite a few times, and are now sure that it consists of k digits. You also know that he is very superstitious and believes in the power of number d, so the password is apt to be divisible by it.

Given the digits that comprise the password, its length k and the number d by which it is divisible, return a sorted list of strings that should be tried as passwords.

Example

For digits = [1, 5, 2], k = 2, and d = 3,
the output should be
crackingPassword(digits, k, d) = ["12", "15", "21", "51"].

Here are all the numbers of length 2: 11, 15, 12, 51, 55, 52, 21, 25 and 22. Only four of them are divisible by 3, and they comprise the answer.
'''
from itertools import product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return [i for i in sorted([createNumber(i) for i in set(list(product(createNumber(digits), repeat = k)) ) ]) if ((int(i) % d == 0) or int(i.lstrip("0")) % d == 0)  ]

# return sorted(product(createNumber(digits), repeat = k))
# return sorted(x for x in map(createNumber,product(digits,repeat=k)) if int(x)%d==0)
# return list(filter(lambda x: int(x) % d == 0, map(createNumber, product(sorted(digits), repeat = k))))
# return sorted(ifilter(lambda n: int(n) % d == 0, imap(createNumber, product(digits, repeat=k)))) 

'''
Product('ABCD', repeat=2) -> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD: 
    -This tool computes the cartesian product of input iterables. To compute the product of an iterable with itself, we use the optional repeat keyword argument to specify the number of repetitions. The output of this function are tuples in sorted order.
'''

def crackingPassword2(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))
    
    result =[]
    possible_pass = list(product(createNumber(digits), repeat = k))

    for i in possible_pass:
        num = createNumber(i)
        if int(num) % d ==0:
            result.append(str(num))

    return sorted(result)
print(crackingPassword2([1, 5, 2], 2, 3))