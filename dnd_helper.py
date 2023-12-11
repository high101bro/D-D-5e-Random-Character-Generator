#! /usr/bin/env python3

import readline
import os
import random, sys, time
from simple_term_menu import TerminalMenu
import pickle_handler 

def debug(show):
    print(f"[Debug] Type: {type(show)} == Value: {show}")
    input("\nPress Enter to Continue...")
    return 


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


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




def print_character(dictionary, spaces=2, padding_value=35):
    try:
        for key, value in dictionary.items():
            if isinstance(value, dict):  # Check if value is a nested dictionary
                print(f"{' ' * spaces}{key} :")
                print_character(value, spaces + 2)  # recursively call the function to handle nested dictionary
            elif isinstance(value, list):  
                print(f"{' ' * spaces}{key} :")
                list_space = spaces + 2
                for v in value:
                    print(f"{' ' * list_space}{v} :")
                print_character(value, spaces + 2)  # recursively call the function to handle nested dictionary
            else:
                padding = padding_value - spaces
                print(f"{' ' * spaces}{f'{key:<{padding}}'} : {value}")  # print key-value pair if value is not a nested dictionary
    except:
        # print(f"{' ' * spaces}None")
        print(f"{' ' * spaces}")


def print_inventory(dictionary, name, padding_value=35):
    for index, item in enumerate(dictionary):
        print(f"  {name} #{index + 1}:")
        for value in item.keys():
            print(f"    {f'{value:<{padding_value - 4}}'} : {item[value]}")




def inspect_character(all_characters):
    while True:
        clear()
        print('Character Management')
        print(f"  ===============================================================================================================")
        print(f"  Character {'#':<7} {'Level':<10} {'Race':<15} {'Class':<14} {'Name':<34} {'Created':<20} ")
        print(f"  ===============================================================================================================")

        character_list = []
        for index, character in enumerate(all_characters):
            character_list.append(f"Character {character.profile['character number']:<7} {character.profile['level']:<10} {character.character_race['Name']:<15} {character.character_class['Name']:<14} {character.profile['name']['first'] + ' ' + character.profile['name']['last']:<34} {character.profile['created']:<20}")
        character_list.append('Delete Character')
        character_list.append('Exit')

        characters_menu = TerminalMenu(character_list)
        characters_menu_index = characters_menu.show()
        
        if character_list[characters_menu_index] == 'Exit':
            character_list.pop()
            character_list.pop()
            break
        elif character_list[characters_menu_index] == 'Delete Character':
            character_list.pop()
            character_list.pop()

            while True:
                clear()
                print("Delete a Character from the Game.")
                print(f"  ====================================================================================================")
                print(f"  Character {'#':<7} {'Race':<15} {'Class':<14} {'Name':<34} {'Created':<20} ")
                print(f"  ====================================================================================================")

                character_remove_list = []
                for character in all_characters:
                    character_remove_list.append(f"Character {character.profile['character number']:<7} {character.character_race['Name']:<15} {character.character_class['Name']:<14} {character.profile['name']['first'] + ' ' + character.profile['name']['last']:<34} {character.profile['created']:<20}")
                character_remove_list.append('Exit')

                characters_menu = TerminalMenu(character_remove_list)
                characters_menu_index = characters_menu.show()
                
                if character_remove_list[characters_menu_index] == 'Exit':
                    character_remove_list.pop()
                    break
                else:
                    character_remove_list.pop()
                    character_remove_confirm = input(f"Are you sure you want to delete the following?\n\n  {character_remove_list[characters_menu_index]}\n\nEnter 'd' to confirm deletion: ")
                    if character_remove_confirm.lower() == 'd':
                        del character_remove_list[characters_menu_index]
                        del all_characters[characters_menu_index]
                        pickle_handler.save_dnd_state('characters', all_characters)
                    else:
                        pass  
            
        else: 
            # dnd_menu_level.pop()
            # dnd_menu_level.pop()

            clear()
            print(f"You selected {character_list[characters_menu_index]}")
            # dnd_choose_character_number = dir(Character())
            # Gets all the attributues of Character() and removes all the attributes that start with '__'
            # dnd_menu_character_class_section_selection = [attr for attr in dir(Character()) if not attr.startswith("__")]
            dnd_menu_character_class_section_selection = ["armor","attributes","background","capabilities","character_class","character_race","combat","description","features","items","level_chart","money","profile","skills","spells","weapons"] 
 
            dnd_menu_character_class_section_selection_menu = TerminalMenu(dnd_menu_character_class_section_selection)
            dnd_menu_character_class_section_selection_menu_index = dnd_menu_character_class_section_selection_menu.show()

            
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'profile':
                print_character(all_characters[characters_menu_index].profile)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'character_race':
                print_character(all_characters[characters_menu_index].character_race)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'character_class':
                print_character(all_characters[characters_menu_index].character_class)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'description':
                print_character(all_characters[characters_menu_index].description)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'background':
                print_character(all_characters[characters_menu_index].background)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'level_chart':
                print_character(all_characters[characters_menu_index].level_chart)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'attributes':
                print_character(all_characters[characters_menu_index].attributes)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'capabilities':
                print_character(all_characters[characters_menu_index].capabilities)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'skills':
                print_character(all_characters[characters_menu_index].skills)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'featuers':
                print_character(all_characters[characters_menu_index].feautres)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'money':
                print_character(all_characters[characters_menu_index].money)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'items':
                print_character(all_characters[characters_menu_index].items)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'armor':
                print_character(all_characters[characters_menu_index].armor)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'weapons':
                print_character(all_characters[characters_menu_index].weapons)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'combat':
                print_character(all_characters[characters_menu_index].combat)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'spells':
                print_character(all_characters[characters_menu_index].spells)
          
            input("\nPress Enter to Continue...")



