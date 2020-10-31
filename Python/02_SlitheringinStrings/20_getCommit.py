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


def getCommit(commit):
    return commit.lstrip('0?+!')


def getCommit(commit):
    return re.sub('[0?+!]', '', commit)


def getCommit(commit):
    return "".join(filter(lambda x: x not in "0?+!", commit))


def getCommit(commit):
    return re.match(r"^[0\?\+!]*(.*)$", commit).group(1)