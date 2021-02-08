"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730432480"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
x: int = int(randint(1,4))
if x < 3:
    if x < 2:
        print("A beautiful, smart, and loving person will be coming into your life.")
    else:
        print("YOur life will be happy and peaceful")
else:
    if x > 2: 
        if x == 4:
            print("Soon life will become more interesting.")
        else:
            print("Today is gonna be a good one.")    
print("Now, go spread positive vibes!")
