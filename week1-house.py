# Hogwart's Houses

# 'match' is similar to 'switch' in other programming languages

name=input("Enter your name: ")

"""
match name:
    case "Harry":
        print("Gryffindor")

    case "Hermione":
        print("Gryffindor")

    case "Ron":
        print("Gryffindor")

    case "Draco":
        print("Slytherin")

    case _:                 #Default Case
        print("Who?")
"""

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")

    case "Draco":
        print("Slytherin")

    case _:                 #Default Case
        print("Who?")