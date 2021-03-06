'''
You've recently read "The Gold-Bug" by Edgar Allan Poe, and was so impressed by the cryptogram in it that decided to try and decipher an encrypted text yourself. You asked your friend to encode a piece of text using a substitution cipher, and now have an encryptedText that you'd like to decipher.

The encryption process in the story you read involves frequency analysis: it is known that letter 'e' is the most frequent one in the English language, so it's pretty safe to assume that the most common character in the encryptedText stands for 'e'. To begin with, implement a function that will find the most frequent character in the given encryptedText.

Example

For encryptedText = "$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ",
the output should be
frequencyAnalysis(encryptedText) = 'C'.

Letter 'C' appears in the text more than any other character (4 times), which is why it is the answer.

'''
from collections import Counter
import operator

def frequencyAnalysis(encryptedText):
    return max(Counter(encryptedText), key= Counter(encryptedText).get)
    # return Counter(encryptedText).most_common(1)[0][0]
    # return sorted(encryptedText, key=encryptedText.count, reverse=True)[0]
''' Counter() returns a dictionary data structure which contains characters of input as key and their frequencies as it's corresponding value.
   Counter objects support three methods beyond those available for all dictionaries:
        - elements():  Return an iterator over elements repeating each as many times as its count.
        - most_common([n]):  Return a list of the n most common elements and their counts from the most common to the least. 
        - subtract([iterable-or-mapping]):  Elements are subtracted from an iterable or from another mapping (or counter). 
'''