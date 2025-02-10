"""import random  #imports all functions in that module

coin=random.choice(["heads","tails"])

print(coin)"""


"""from random import choice   #import only the specific function choice(seq)

coin=choice(["heads","tails"])

print(coin)"""

#import random

"""#Returns a random integer in range [a, b], including both end points.
num=random.randint(1,10)

print(num)"""

"""cards=["Jack", "King", "Queen"]

random.shuffle(cards)   #Shuffles list x in place, and return None.
 
print(cards)"""

"""import statistics

average=statistics.mean([0.25,0.44,0.64,0.86])

print(average)"""

import sys

"""try:
    print("Hello, my name is",sys.argv[1])

except IndexError:
    print("argv[1] not provided.")"""


"""if len(sys.argv)<2:
    print("Too few arguements passed.")
elif len(sys.argv)>2:
    print("Too many arguements passed.")
else:
    print("Hello, my name is",sys.argv[1],".")"""

# Rather than explicitly taking input name and passing it, we passed sys.argv[1] 
# which means the argument vector passed while running program in the command line.
# sys.argv[0]=Name of file that you are running
# sys.argv[1]=The next arguement you pass using command-line


# PS D:\Harvard OCW CS50P> python week4-libraries.py Neha
# Hello, my name is Neha


"""if len(sys.argv)<2:
    sys.exit("Too few arguements passed.")
elif len(sys.argv)>2:
    sys.exit("Too many arguements passed.")

print("Hello, my name is",sys.argv[1],".")
"""

if len(sys.argv)<2:
    sys.exit("Too few arguements passed.")

for arg in sys.argv[1:]:    
    #We sliced the sys.argv vector from index 1 to end so that the file name(sys.argv[0]) 
    # won't be considered during iteration

    print("Hello, my name is",arg,".")
    
    #Iterating over the sys.argv vector inputted using command-line


