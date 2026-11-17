# with open("students.csv","a") as file:
#     flag=False

#     while(flag==False):
#         name=input("Enter student's name:")
#         file.write(f"{name},")
#         house=input("Enter student's house:")
#         file.write(f"{house}\n")
#         choice=input("Do you want to continue? (Y/N)")
#         choice=choice.strip().upper()
#         if choice=="N":
#             flag=True

# with open("students.csv","r") as file :
#     for line in file:
#         data = line.rstrip().split(",")
#         print(f"{data[0]} is in house {data[1]}")

# with open("students.csv","r") as file :
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in house {house}")


# def get_name(student):
#     return student["name"]

# students=[]
# with open("students.csv","r") as file :
#     for line in file:
#         name,house = line.rstrip().split(",")
#         student={"name":name,"house":house}
#         students.append(student)

#     for student in sorted(students, key=get_name):
#         print(f"{student['name']} is in {student['house']}")


# students=[]
# with open("students.csv","r") as file :
#     for line in file:
#         name,house = line.rstrip().split(",")
#         student={"name":name,"house":house}
#         students.append(student)

#     # A lambda function is a function that has no name i.e. anonymous, so instead of explicitly
#     # defining the get_name function, lambda function is directly passed to it.
#     for student in sorted(students, key=lambda student:student["name"]):    
#         print(f"{student['name']} is in {student['house']}")


# import csv

# students=[]

# with open("homes.csv","r") as file :
#     reader=csv.reader(file)
#     for row in reader:
#         student={"name":row[0],"home":row[1]}    # reader returns each row as lists
#         students.append(student)

#     # A lambda function is a function that has no name i.e. anonymous, so instead of explicitly
#     # defining the get_name function, lambda function is directly passed to it.
#     for student in sorted(students, key=lambda student:student["name"]):    
#         print(f"{student['name']} is from {student['home']}")

import csv

students=[]

with open("homes.csv","r") as file :
    reader=csv.DictReader(file)
    for row in reader:
        # DictReader returns each row as a dictionary
        students.append({"name":row["name"], "home":row["home"] })

    # A lambda function is a function that has no name i.e. anonymous, so instead of explicitly
    # defining the get_name function, lambda function is directly passed to it.
    for student in sorted(students, key=lambda student:student["name"]):    
        print(f"{student['name']} is from {student['home']}")