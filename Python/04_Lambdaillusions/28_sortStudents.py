'''
You are given a list of students who want to apply to the internship at CodeSignal. For the ith student you know their full name students[i], which can consist of up to 5 words (where a word is a set of consecutive letters). It is guaranteed that the surname is always the last name of student's full name.

Your task is to sort the students lexicographically by their surnames. If two students happen to have the same surname, their order in the result should be the same as in the original list.

Example
For
students = ["John Smith", "Jacky Mon Simonoff", 
            "Lucy Smith", "Angela Zimonova"]
the output should be

sortStudents(students) = ["Jacky Mon Simonoff", "John Smith", 
                          "Lucy Smith", "Angela Zimonova"]
'''

def sortStudents(students):
    students.sort(key=lambda name: name.split(' ')[-1])
    return students

'''
To complete the sort, we will combine three operations:

- lambda x: x.split(" "), which is a function that takes a string x and breaks it up along each blank space. This outputs a list.
- [-1], which takes the last element of a list.
- sorted(), which sorts a list.

# Sort a variable called 'commander_names' by the last elements of each name.
sorted(commander_names, key=lambda x: x.split(" ")[-1])
'''