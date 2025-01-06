"""
count=3
while count>0:
    print("meow")
    count=count-1

for i in [0,1,2]:
    print("meow")

for i in range(3):
    print("meow")

print("meow"*3)

print("meow\n"*3,end="")
"""

while True:
    n=int(input("Enter the value of n : "))

    if(n>0):
        break
    else:
        continue

for i in range(1,n+1):    #range(start,end,stepsize), if not specified, the stepsize is by default 1
    print("*\t"*i)

