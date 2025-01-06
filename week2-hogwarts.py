#students=["Hermione", "Harry", "Ron"]

"""print(students[0])
print(students[1])
print(students[2])
"""
"""for student in students:
    print(student)

for i in range(len(students)):  #len(object) function provides length of the object(sequence or collection)
    print(students[i])"""

# Dictionary(dict):

"""students={
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin",
}

print(students["Hermione"])

print(students["Draco"])

# Iterating over dictionary

for student in students:
    print(student, students[student])"""


# List of Dictionaries

students=[
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},

    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},

    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russel Terrier"},

    {"name":"Draco", "house":"Slytherin", "patronus":None}
]

# "None" is a keyword in python that officially depicts "no value specified"

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=": ")