"""
Implement a function that, given a feedback and the size of the screen, splits the feedback into lines so that:
    - each token (i.e. sequence of non-whitespace characters) belongs to one of the lines entirely;
    - each line is at most size characters long;
    - no line has trailing or leading spaces;
    - each line should have the maximum possible length, assuming that all lines before it were also the longest possible.

Example:
For feedback = "This is an example feedback" and size = 8,
the output should be

feedbackReview(feedback, size) = ["This is", 
                                  "an", 
                                  "example", 
                                  "feedback"]

"""
import textwrap

def feedbackReview(feedback, size):
    return textwrap.TextWrapper(size).wrap(feedback)
    ''' wrap(text): 
    Wraps the single paragraph in text (a string) so every line is at most width characters long. All wrapping options are taken from instance attributes of the TextWrapper instance. Returns a list of output lines, without final newlines. '''

# def feedbackReview(feedback, size):
# return textwrap.wrap(feedback, size)

import re
def feedbackReview(feedback, size):
    return re.compile(r"[^ ].{0," + str(size - 2) + r"}[^ ](?= |\Z)").findall(feedback)
''' re.compile(pattern, flags=0)
Compile a regular expression pattern into a regular expression object, which can be used for matching using findall(pattern, string, flags=0) '''

def feedbackReview(feedback, size):
    return re.compile('\S.{,' + `size - 2` + '}\S(?=\s|$)').findall(feedback)
