def hello(name="world"):    #default value passed as "world" to the name parameter
    print("Hello",name)

#hello() #no parameter passed for name so the default value will be used

def main(): 
    #convention to wrap main part of program in main function & then call the main function 
    # to start execution of program
    name = input("Enter your name : ")
    hello(name)

main()