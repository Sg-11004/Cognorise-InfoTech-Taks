import random

def roll_dice(sides, rolls):
    print(f"Rolling a {sides}-sided dice {rolls} times:")
    for roll in range(rolls):
        result = random.randint(1, sides)
        print(f"Roll {roll + 1}: {result}")

def dice_simulator():
    while True:
        try:
            sides = int(input("Enter the number of sides on the dice: "))
            rolls = int(input("Enter the number of rolls: "))

            if sides <= 0 or rolls <= 0:
                print("Please enter positive values for sides and rolls.")
                continue

            roll_dice(sides, rolls)
            break

        except ValueError:
            print("Invalid input. Please enter valid numbers for sides and rolls.")
dice_simulator()
