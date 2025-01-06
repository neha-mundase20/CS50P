# Printing N*N brick wall

n=int(input("Enter the size : "))

"""for i in range(n):
    for j in range(n):
        print("#",sep="\t",end=" ")
    print() # introduces newline character after each row"""

"""for i in range(n):
    for j in range(n):
        print("#\t",end=" ")
    print()"""

for i in range(n):
    print("#\t"*n,end="\n")