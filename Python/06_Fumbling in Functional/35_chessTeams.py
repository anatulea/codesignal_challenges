'''
A grand Team Chess Tournament will be held at your University. Two teams, smarties and cleveries, will clash to determine whose chess skills are better. The teams have the same number of members, and the ith member of smarties will play against the ith member of cleveries in the ith game for each valid i

Given the names of the players of both smarties and cleveries, return the games in the order they will be played.

Example

For smarties = ["Jane", "Bob", "Peter"] and
cleveries = ["Oscar", "Lidia", "Ann"], the output should be

chessTeams(smarties, cleveries) = [["Jane",  "Oscar"],
                                   ["Bob",   "Lidia"],
                                   ["Peter", "Ann"]]
'''
def chessTeams(smarties, cleveries):
    return list(zip(smarties, cleveries))
''' 
    The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it.
            -If we do not pass any parameter, zip() returns an empty iterator
            -If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
            -If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements from all the iterables.
'''
    # return [[a,b] for a,b in zip(smarties,cleveries)]
    # return list(map(lambda x1,x2: list([x1, x2]), smarties, cleveries))
    # return map(list, zip(smarties, cleveries))