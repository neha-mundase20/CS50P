#This is a single line comment

"""
This is a multi-line comment
"""

print("Harvard CS50P")

name=input("What is your name? ")

print("I am "+ name)    # Concatenation of strings

print("I am ", name)    # Two separate arguements passed to the function to print
# When you pass multiple arguements to a print function
# it automatically inserts space inbetween the parameters that are printed

print("I am", name, sep='\t', end='????')

print(end="\n")

#Formatted Strings

print(f"I am {name}")

"""
#Built-In String Methods

name=name.strip()   #Removes all leading and trailing whitespaces
name=name.capitalize()   #Capitalizes the string i.e. first character upper-case and rest lower-case
name=name.title()   #All words in the string will have their first character upper-case

"""

#We can also chain these functions together
name=name.strip().title()

print("I am", name)

first, last=name.split(" ")
print("I am", first)

