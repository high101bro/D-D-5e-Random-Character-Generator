#! /usr/bin/env python3

import readline

def debug(show):
    print(f"[Debug] Type: {type(show)} == Value: {show}")
    input("\nPress Enter to Continue...")
    return 



def dnd_roll_dice():
    def roll_dice(sides):
        def roll(sides):
            roll = str(random.randint(1, sides))
            return str(roll)
        for _ in range(15):  # The number of iterations determines the length of the animation
            time.sleep(0.1)  # Pause for a short period to create the animation effect
            the_roll = roll(sides)
            sys.stdout.write(f"\r{'['+ the_roll + ']':<6}")  # Random number between 1 and 6
            sys.stdout.flush()
        final_roll = the_roll
        return final_roll

    while True:
        try:
            dice_number = int(input(f"Enter the number of dice: "))
            break
        except:
            print(f"Enter a number!")
    while True:
        try:
            dice_sides = int(input(f"Enter the dice size/number of sides: "))
            break
        except:
            print(f"Enter a number!")
    while True:
        try:
            roll_modifier = int(input(f"Enter your total modifier to add to each roll: "))
            break
        except:
            print(f"Enter a number!")

    clear()
    print("==================================================")
    print(f"Going to roll {dice_number}d{dice_sides} + {roll_modifier}.")
    print("==================================================")

    dice_roll_total = 0 
    for index,roll in enumerate(range(1,dice_number + 1)):
        # dice_roll = random.randint(1,dice_sides + 1)
        dice_roll = int(roll_dice(dice_sides))
        roll_total = dice_roll + roll_modifier
        dice_roll_total += roll_total
        print(f"  Roll #{(index + 1):<3}    {dice_roll:<3} + {roll_modifier:<3} = {roll_total:<3}")
    print(f"\nTotal rolled value is {dice_roll_total}.")
    return dice_roll_total

