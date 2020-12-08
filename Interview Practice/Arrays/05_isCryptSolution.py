'''
A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.

You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits, solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], which should be interpreted as the word1 + word2 = word3 cryptarithm.

If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. If it does not become a valid arithmetic solution, the answer is false.

Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).

Example

For crypt = ["SEND", "MORE", "MONEY"] and

solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
the output should be
isCryptSolution(crypt, solution) = true.

When you decrypt "SEND", "MORE", and "MONEY" using the mapping given in crypt, you get 9567 + 1085 = 10652 which is correct and a valid arithmetic equation.

For crypt = ["TEN", "TWO", "ONE"] and

solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
the output should be
isCryptSolution(crypt, solution) = false.

Even though 054 + 091 = 145, 054 and 091 both contain leading zeroes, meaning that this is not a valid solution.
'''
def isCryptSolution(crypt, solution):
    # a + b = c
    a = crypt[0]
    b = crypt[1]
    c = crypt[2]
    ch_dict = {}

    for s in solution:
        ch_dict[s[0]] = int(s[1])
    hasLeadingZeros = False

    if ch_dict[a[0]] == 0 or ch_dict[b[0]] == 0 or ch_dict[c[0]] == 0:
        hasLeadingZeros =  True
    
    n1 = ''.join([str(ch_dict[i]) for i in a])
    n2 = ''.join([str(ch_dict[i]) for i in b])
    n3 = ''.join([str(ch_dict[i]) for i in c])

    if int(n1)+int(n2) == int(n3):
        if hasLeadingZeros and int(n3) == 0 and len(n3) == len(str(int(n3))):
            return True
        elif hasLeadingZeros:
            return False
        else:
            return True
    else:
        return False



def isCryptSolution2(crypt, solution):
    dic = {ord(c): d for c, d in solution}
    *v, = map(lambda x: x.translate(dic), crypt)
    return not any(x != "0" and x.startswith("0") for x in v) and \
        int(v[0]) + int(v[1]) == int(v[2])


def isCryptSolution3(crypt, solution):
    table = str.maketrans(dict(solution))
    t = tuple(s.translate(table) for s in crypt)
    zeroes = any(s[0] == '0' for s in t if len(s) > 1)
    return not zeroes and int(t[0]) + int(t[1]) == int(t[2])


def isCryptSolution4(crypt, solution):
    crypt_s = crypt
    for i in range(0, 3):
        for s in solution:
            crypt_s[i] = crypt_s[i].replace(s[0], s[1])
        
        if crypt_s[i] != '0' and crypt_s[i][0] == '0':
            return False
        
    if int(crypt_s[0]) + int(crypt_s[1]) != int(crypt_s[2]):
        return False
    
    return True

def isCryptSolution5(crypt, solution):
    sol = dict(solution)
    adds = [int("".join([sol[c] for c in word])) for word in crypt]
    return all([sol[word[0]] != "0" or len(word) == 1 for word in crypt]) and adds[0] + adds[1] == adds[2]