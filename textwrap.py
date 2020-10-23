"""
 Implement a function that, given a feedback and the size of the screen, splits the feedback into lines so that:

each token (i.e. sequence of non-whitespace characters) belongs to one of the lines entirely;
each line is at most size characters long;
no line has trailing or leading spaces;
each line should have the maximum possible length, assuming that all lines before it were also the longest possible.
Example

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

# def feedbackReview(feedback, size):
# return textwrap.wrap(feedback, size)

import re
def feedbackReview(feedback, size):
    return re.compile(r"[^ ].{0," + str(size - 2) + r"}[^ ](?= |\Z)").findall(feedback)

def feedbackReview(feedback, size):
    return re.compile('\S.{,' + `size - 2` + '}\S(?=\s|$)').findall(feedback)
