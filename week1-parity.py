# Function that returns boolean values
def isEven(number):
    """
    if number%2==0:
        return True

    else:
        return False
    """

    """
    #Pythonic Expression i.e. condensed format
    return True if number%2==0 else False
    """

    return (number%2==0)  #coz ultimately this returns either True or False 



def main():
    number=int(input("Enter any number: "))
    
    if(isEven(number)):
        print("This is an even number.")
    else:
        print("This is a odd number.")

main()