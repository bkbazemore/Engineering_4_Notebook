# Automatic Dice roller
# Written by Jamez and Bethany

from random import randint

print ("Automatic Dice roller")
min = 1
max = 6


roll_again = "yes"


while roll_again == "yes" or roll_again == "x":
    print ("Rolling the dice...")
    print ("The values are...")
    print (randint(min,max))
    print (randint(min,max))

    roll_again = input("Roll the dice again") 
