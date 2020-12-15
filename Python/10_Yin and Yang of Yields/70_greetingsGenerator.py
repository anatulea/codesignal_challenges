'''
The web application service you're working on is supposed to be used by developers teams. To make the service more friendly, you'd like to implement a feature that will greet each person in a group.

Given a list of people in a team, return an array of greetings that should be printed out, where each greeting is in the format "Hello, <team[i]>!".

Example

For team = ["Athos", "Porthos", "Aramis"],
the output should be

greetingsGenerator(team) = ["Hello, Athos!",
                            "Hello, Porthos!",
                            "Hello, Aramis!"]
                            '''
class Greeter(object):
    def __init__(self, names):
        self.count = 0
        self.names = names

    def __iter__(self):
        return self
    '''
    The __iter__() function returns an iterator for the given object (array, set, tuple etc. or custom objects). It creates an object that can be accessed one element at a time using __next__() function, which generally comes in handy when dealing with loops.
    '''

    def __next__(self):
        if self.count < len(self.names):
            self.count += 1
            return 'Hello, {}!'.format(self.names[self.count - 1])
        else:
            raise StopIteration


def greetingsGenerator(team):
    return list(Greeter(team))