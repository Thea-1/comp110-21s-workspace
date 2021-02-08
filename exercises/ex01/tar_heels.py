"""An exercise in remainders and boolean logic."""

__author__ = "730432480"


# Begin your solution here...
how_much: int = int(input("pick a number between 0-100:"))
x = int
if how_much % 2 == 0 or how_much % 7 == 0:
    if how_much % 2 != 0:
        print("HEELS")
    if how_much % 7 != 0:
        print("TAR")
    if how_much % int(2) == 0 and how_much % int(7) == 0:     
        print('TAR HEELS')      
else:
    print("CAROLINA")    


