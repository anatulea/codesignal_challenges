'''
Don Corletwo, local Mafia boss, asked you for a favor, and you, naturally, cannot say no. An yahtzee championship will be held soon enough, and Don needs to make sure that his player has a decent chance to win. You are assigned with the task of writing the dice interface for the game. As a Python programmer, you can use the random module to generate random numbers that will determine the result of throwing an n-sides die.

Of course, random module can get predictable results if given a proper seed value. Your task is to implement a function that, given the seed for random module and the number of sides on the die n, will return the value on the die using the following formula: int(random.random() * n) + 1.

Example

For seed = 37237 and n = 5, the output should be
createDie(seed, n) = 3.
'''
import random

def createDie(seed, n):
    class Die(object):
        def __new__(*args):
            return int(random.Random(seed).random()*n)+1

    class Game(object):
        die = Die(seed, n)

    return Game.die

'''
import random

def createDie(seed, n):
    class Die(object):
        def __init__(self, seed, n):
            """To meet the expected API we need a class instance that, when refrenced as an
            attribute of another class, looks like an int.
            
            One approach to making behavior look like data is the @property decorator.
            That's not a good fit here, it makes funcitons look like data, but we need
            to write a class.  We can't change the way the attribute is defined, either.
            
            However, properties are implemented using something called descriptors,
            which are class based.  The special methods __get__(), __set__() and __delete__()
            make a class behave like an @property when an instance is a property of another class.
            
    """
            self.seed = seed
            self.n = n
            random.seed(self.seed)
            self.value = int(random.random() * self.n + 1)
        
        def __get__(self, instance, owner):
            return self.value

    class Game(object):
        die = Die(seed, n)

    return Game.die
    '''