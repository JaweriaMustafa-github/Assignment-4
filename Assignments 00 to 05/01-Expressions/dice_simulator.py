"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times. Prints
the results of each die roll. This program is used
to show how variable scope works.
"""

# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    dice1 : int = random.randint(1, NUM_SIDES)
    dice2 : int = random.randint(1, NUM_SIDES)
    total : int = dice1 + dice2
    print ("Total of two dice are: ", total)

def main():
    dice1: int = 10 # This dice1 is local to main()
    print("dice1 in main() starts as:", dice1)

    roll_dice()
    roll_dice()
    roll_dice()
    
    print("dice1 in main() is:", dice1)

if __name__ == "__main__":
    main()
