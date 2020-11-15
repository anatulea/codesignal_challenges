'''
You are working on a revolutionary video game. In this game the player will be able to collect several types of bonuses on each level, and his total score for the level is equal to the sum of the first n bonuses he collected. However, if he collects less than n bonuses, his score will be equal to 0.

Given the bonuses the player got, your task is to return his final score for the level.

Example

For bonuses = [4, 2, 4, 5] and n = 3,
the output should be
calcBonuses(bonuses, n) = 10.

4 + 2 + 4 = 10.

For bonuses = [4, 2, 4, 5] and n = 5,
the output should be
calcBonuses(bonuses, n) = 0.

The player has collected only 4 bonuses, so his final score is 0.

'''
def calcBonuses(bonuses, n):
    it = iter(bonuses) 
    '''   
     The iter() function creates an object which can be iterated one element at a time.These objects are useful when coupled with loops like for loop, while loop.
     
     The iter() function takes two parameters:
        - object - object whose iterator has to be created (can be sets, tuples, etc.)
        - sentinel (optional) - special value that is used to represent the end of a sequence

    We can use the iter() method with the sentinel parameter to stop the iteration. If the value returned from __next__() is equal to sentinel, StopIteration will be raised, otherwise, the value will be returned.
    '''
    # it = (b for b in bonuses)
    # it = [(yield x) for x in bonuses]
    # it = (x for x in bonuses if len(bonuses) >= n)
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res