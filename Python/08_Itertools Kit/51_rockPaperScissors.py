'''
The greatest ever Rock-Paper-Scissors Championship will take place in your town! The best players will battle each other to see who's the best player in the world. Each player will compete against each other player twice, once home and once away.

Given the list of the players, your task is to come up with the list of all the games between them, and return them sorted lexicographically.

Example

For players = ["trainee", "warrior", "ninja"], the output should be

rockPaperScissors(players) = [["ninja", "trainee"], ["ninja", "warrior"], 
                              ["trainee", "ninja"], ["trainee", "warrior"], 
                              ["warrior", "ninja"], ["warrior", "trainee"]]
                              '''
from itertools import permutations

def rockPaperScissors(players):
    return sorted(set([i[0:2] if len(i) > 2 else i for i in list(permutations(players))]))
    # return list(permutations(sorted(players), 2))
    # return sorted(permutations(players, 2))
    # return list(permutations(sorted(players), 2))
'''
    Permutations():
        - Permutations() as the name speaks for itself is used to generate all possible permutations of an iterable. All elements are treated as unique based on their position and not their values. This function takes an iterable and group_size, if the value of group_size is not specified or is equal to None then the value of group_size becomes length of the iterable.
'''