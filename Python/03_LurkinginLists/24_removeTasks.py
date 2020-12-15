'''
Today is a good day: it's the kth year since you started to work at the company, which means you have to have a party today. In order to get home earlier and prepare for the jamboree, you need to get home early. You decided to remove each kth tasks from your toDo list, since today is your day and you can do whatever you please.

Given the list of task ids in your toDo list, remove each kth task from it and return the list of remaining tasks.

Example

For k = 3 and toDo = [1237, 2847, 27485, 2947, 1, 247, 374827, 22],
the output should be
removeTasks(k, toDo) = [1237, 2847, 2947, 1, 374827, 22].
'''
def removeTasks(k, toDo):
    del toDo[k-1:len(toDo):k] # specify step as [start:stop:step].  removes the elements of s[i:j:k] from the list
    # del s[i:j] same as s[i:j] = []
    return toDo
    '''del d[key]
    Remove d[key] from d. Raises a KeyError if key is not in the map.
    '''

def removeTasks2(k, toDo):
    del toDo[k - 1::k]
    return toDo