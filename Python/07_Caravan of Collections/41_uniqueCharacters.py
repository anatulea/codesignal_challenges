'''
You need to compress a large document that consists of a small number of different characters. To choose the best encoding algorithm, you would like to look closely at the characters that comprise this document.

Given a document, return an array of all unique characters that appear in it sorted by their ASCII codes.

Example
For document = "Todd told Tom to trot to the timber",
the output should be
uniqueCharacters(document) = [' ', 'T', 'b', 'd', 'e', 'h', 'i', 'l', 'm', 'o', 'r', 't'].
'''
def uniqueCharacters(document):
    return sorted(set({ch for ch in document}))
    # return sorted(set(document))
    # return sorted(list(set(document)))
    # return sorted([char for index, char in enumerate(document) if char not in document[0:index]])
    '''
    The sorted() function sorts the elements of a given iterable in a specific order (either ascending or descending) and returns the sorted iterable as a list.
        - The syntax of the sorted() function is:
        - sorted(iterable, key=None, reverse=False)'''