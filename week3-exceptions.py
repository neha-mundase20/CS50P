"""try:
    n=int(input("Enter the number: "))

except ValueError:
    print("Please enter a valid number.")

print(f"The number is: {n}")"""    
#This will give error : 'n' is not defined, coz due to incorrect input 'n' isn't assigned a value 
#So when this line will execute after 'except' block, it will throw error
#So try-except is supported with 'else' block

"""try:
    n=int(input("Enter the number: "))

except ValueError:
    print("Please enter a valid number.")

else:
    print(f"The number is: {n}")  """  
    #If everything goes correct without exceptions then do this instead of 'except' block


# Prompting user continuously unless and until a proper input is received

def get_int(prompt):
    while True:
        try:
            n=int(input(prompt))

        except ValueError:
            #print("Please enter a valid number.")
            pass    #'pass' catches the error but this silently ignores the exception occured i.e. rather do nothing

        else:
            #print(f"The number is: {n}")
            #break
            return n

    

def main():
    n=get_int("Enter the number: ")
    print(f"The number is: {n}")


main()