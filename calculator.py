# Type Conversion
# Nesting of functions int(input())

"""
x=int(input("Enter x : "))  #int() is itself a function that converts any string or number passed to it in INT
y=int(input("Enter y : "))

print(x+y)

x=float(input("Enter x : "))  
y=float(input("Enter y : "))

z=round(x+y)

print(z)
print(f"{z:,}") #Adding commas in numbers as we do in decimal system

print(x/y)
print(round(x/y,2))    #Second parameter adds precision of rounding
print(f"{x/y:.2f}")    #Rounding can be done in this way too

"""

def square(n):
    #return x**2
    return pow(n,2)

def main():
    n=int(input("Enter any number : "))
    print(square(n))

main()