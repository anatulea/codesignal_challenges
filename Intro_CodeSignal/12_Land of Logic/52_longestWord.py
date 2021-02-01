'''
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".'''
import string
def longestWord(text):
  
  for char in string.punctuation:
    text = text.replace(char,' ')
  text = text.split()
  text.sort(key = lambda x: len(x))
  
  return text[-1]

import re
def longestWord2(text):
    return max(re.split('[^a-zA-Z]', text), key=len)