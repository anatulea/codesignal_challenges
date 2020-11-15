'''
You're organizing murder mystery games for your coworkers, and came up with a lot of ideas for various groups of participants. The ith 0-based game can be played only if there are at least i people registered for it. Game number 0 is a beta that you will try out with your friends, so there's no need for participants.

You're expecting a full house, since a lot of participants signed up already. Not too many, unfortunately: looks like some games can't be played, because too few people registered for them. Given the list of participants, your task is to return the list of games for which too few people signed up.

Example

For participants = [0, 1, 1, 5, 4, 8], the output should be
checkParticipants(participants) = [2].

For the game number 2 (0-based) 2 people are required, but only one person has registered.
'''
def checkParticipants(participants):
   return [idx for idx, num in enumerate(participants) if num < idx]
   # return filter (lambda i:i>participants[i],range(len(participants)))

participants = [0, 1, 1, 5, 4, 8]

def checkParticipants2(participants):
   result = [] # will store the game index of the games that too few people sighnd for
   for idx, num in enumerate(participants):
      if idx > num: #if the index is grater than the value means not enough people signed
         result.append(idx) # add the index to the result array 
   return result
      
print(checkParticipants2(participants)) # [2]

participants2 = [3, 3, 3, 3, 3, 3, 3, 3]
print(checkParticipants2(participants2)) # [4, 5, 6, 7]
