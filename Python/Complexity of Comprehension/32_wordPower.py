'''
You've heard somewhere that a word is more powerful than an action. You decided to put this statement at a test by assigning a power value to each action and each word. To begin somewhere, you defined a power of a word as the sum of powers of its characters, where power of a character is equal to its 1-based index in the plaintext alphabet.

Given a word, calculate its power.

Example

For word = "hello", the output should be
wordPower(word) = 52.

Letters 'h', 'e', 'l' and 'o' have powers 8, 5, 12 and 15, respectively. Thus, the total power of the word is 8 + 5 + 12 + 12 + 15 = 52.
'''

def wordPower(word):
    num = {char: ord(char)-96 for char in word.lower()}

    # zip() is to map the similar index of multiple containers so that they can be used just using as single entity.
    # num = dict(zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))) # {'h': 8, 'e': 5, 'l': 12, 'o': 15}
    # num = dict(zip(list(string.ascii_lowercase), range(1,27)))

    # num = {char: index+1 for (index, char) in enumerate(string.ascii_letters)}
    print(num)
    return sum([num[ch] for ch in word])
myword ='hello'
print(wordPower(myword))

# The ord() function in Python accepts a string of length 1 as an argument and returns the unicode code point representation of the passed argument. 
# ord("a")= 97 | to have "a" equal to 1 will substact  96

def forLoopWordList(word):
    sum = 0
    num = {}
    for char in word.lower():
        num[char] = ord(char)-96 # {'h': 8, 'e': 5, 'l': 12, 'o': 15}
    for character in word:
        sum = sum+num[character] # 8+5+12+12+15 = 52
    return sum


myword ='hello'
print(forLoopWordList(myword))
