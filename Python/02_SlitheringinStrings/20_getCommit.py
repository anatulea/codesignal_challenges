'''
The Abanamama Version System (AVS) is a software versioning and revision control system used in highly secure environments. In this system, each commit is assigned a unique name, the first part of which consists of the username encrypted in the base-4 system using symbols '0', '?', '+', and '!', and the second part consists of symbols of English alphabet.

Given such commit, your task is go remove the username part from it and return the second part as an answer.

Example

For commit = "0??+0+!!someCommIdhsSt", the output should be
getCommit(commit) = "someCommIdhsSt".


'''
import re
def getCommit(commit):
    return "".join(re.split('[0?+!]', commit))
    ''' re.split(pattern, string, maxsplit=0, flags=0)
    Split string by the occurrences of pattern. If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list'''

def getCommit2(commit):
    return commit.lstrip('0?+!')
    '''str.lstrip([chars])¶
    Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed.'''


def getCommit3(commit):
    return re.sub('[0?+!]', '', commit)


def getCommit4(commit):
    return "".join(filter(lambda x: x not in "0?+!", commit))


def getCommit5(commit):
    return re.match(r"^[0\?\+!]*(.*)$", commit).group(1)