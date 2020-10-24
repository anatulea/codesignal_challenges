'''
Implement a function that will change the very first symbol of the given message to uppercase, and make all the other letters lowercase.

Example

For message = "you'll NEVER believe what that 'FrIeNd' of mine did!!1",
the output should be
fixMessage(message) = "You'll never believe what that 'friend' of mine did!!1".
'''
def fixMessage(message):
    return message[0].upper() + message[1:].lower()