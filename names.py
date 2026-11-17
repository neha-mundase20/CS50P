# name = input("What's your name ?")

# file = open("names.txt","w")   
# # Opens a file with the specified name in WRITE mode and returns the stream
# # If file doesn't exists, it will create a new file

# file.write(name)
# # Write content to file

# file.close()
# # Saves and closes the file

# ================================================================================================

# name = input("What's your name ?")

# file = open("names.txt","a")   
# # Opens a file with the specified name in APPEND mode(will not delete existing data everytime) and returns the stream
# # If file doesn't exists, it will create a new file

# file.write(f"{name} \n")
# # Write content to file

# file.close()
# # Saves and closes the file

# ================================================================================================

# name = input("What's your name ?")

# with open("names.txt","a") as file :
#     # When "with" keyword is used, no need to explicitly close the file

#     file.write(f"{name} \n")
#     # Write content to file

# ================================================================================================

# # Reading data from the file

# with open("names.txt","r") as file:
#     lines=file.readlines()  # reads data from file linewise and returns list of lines
#     lines= sorted(lines)

# for line in lines:
#     print(line.rstrip())

# ================================================================================================

# # Reading data from the file

# with open("names.txt","r") as file:
#     for line in file:
#         print(line.rstrip())

# ================================================================================================

