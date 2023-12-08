#! /usr/bin/env python3

import re, time, sys
from simple_term_menu import TerminalMenu
from dnd_generate_character import *
from dnd_lists import *
from dnd_cities import *
from chatgpt import *
from my_secrets import *


# def menu():
#     click.echo('Hello, World!')

dnd_dungeon_master = """
 _____        _____              _____                                        __  __           _            
|  __ \      |  __ \            |  __ \                                      |  \/  |         | |           
| |  | |_ __ | |  | |   _____   | |  | |_   _ _ __   __ _  ___  ___  _ __    | \  / | __ _ ___| |_ ___ _ __ 
| |  | | '_ \| |  | |  |_____|  | |  | | | | | '_ \ / _` |/ _ \/ _ \| '_ \   | |\/| |/ _` / __| __/ _ \ '__|
| |__| | | | | |__| |           | |__| | |_| | | | | (_| |  __/ (_) | | | |  | |  | | (_| \__ \ ||  __/ |   
|_____/|_| |_|_____/(5e)        |_____/ \__,_|_| |_|\__, |\___|\___/|_| |_|  |_|  |_|\__,_|___/\__\___|_|(DM)  
                                                     __/ |                                                  
                                                    |___/                                                   
"""
optionsMenu  = [
    'Create Character',
    'Character Management',
    'Items, Weapons, Armor, Equipment',
    'Locations',
    'Manage Battle',
    'Roll Dice',
    'ChatGPT'
]

all_characters = []
character_number_tracker = 0

def debug(show):
    ts = input(f"{show}")
    return print(ts)


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
    input("\nPress Enter to Continue...")
    return dice_roll_total


def display_dnd_menu(items_dictionary):

    # Convert the dictionary into a list
    menu_items = [f"{key} - {value}" for key, value in items_dictionary.items()]

    # Function to split text into two elements
    def split_two_elements(text):
        split_text = text.split('-', 1)
        return split_text[0], split_text[1]

    # Format the list to be pretty in the menu
    menu_formatted = []
    for item in menu_items:
        first_element, second_element = split_two_elements(item)
        menu_formatted.append(f"{first_element.strip():<30}{second_element.strip()}")
    menu_formatted = sorted(menu_formatted)

    # The menu
    print(f"Select from {len(menu_formatted)} options: ")
    menu_formatted.insert(0, 'Random Selection(s)')
    menu_formatted.append('Exit')
    terminal_menu = TerminalMenu(menu_formatted)
    menu_index = terminal_menu.show()

    # Handling menu selections
    if menu_formatted[menu_index] == 'Random Selection(s)':
        del menu_formatted[0]
        del menu_formatted[-1]
        while True:
            try:
                number_of_random_selections = int(input(f"How many selections? "))
                break
            except ValueError:
                print(f"Error: Enter a number.")
                input("\nPress Enter to Continue...")
        random_selections = []
        for _ in range(number_of_random_selections):
            random_selection = random.choice(menu_formatted)
            random_selections.append(random_selection)
            print(random_selection)
            input("\nPress Enter to Continue...")
            return random_selection
    elif menu_formatted[menu_index] == 'Exit':
        pass
        return None
    else:
        del menu_formatted[0]
        del menu_formatted[-1]
        print(menu_formatted[menu_index - 1])
        return None
    
    input("\nPress Enter to Continue...")




while True:
    clear()
    print(dnd_dungeon_master)


    characters = []
    menuMain = TerminalMenu(optionsMenu)
    selectedMenuOption = menuMain.show()
    if re.compile("^Create Character").match(optionsMenu [selectedMenuOption]):

        # Number of Characters
        clear()
        print('How many characters do you want to create? ')
        dnd_choose_character_number = ['1','2','3','4','5','6','7','8','9','10']
        dnd_choose_character_number.insert(0,'Random Number')
        dnd_choose_character_number.append('Exit')
        character_number_menu = TerminalMenu(dnd_choose_character_number)
        character_number_index = character_number_menu.show()
        

        if dnd_choose_character_number[character_number_index] == 'Random Number': # Which should be the 'Random Number' index
            # dnd_choose_character_number.pop()
            del dnd_choose_character_number[0]
            del dnd_choose_character_number[-1]
            character_number = int(random.choice(dnd_choose_character_number))
        elif dnd_choose_character_number[character_number_index] == 'Exit': # Which should be the 'Exit' index
            # dnd_choose_character_number.pop()
            del dnd_choose_character_number[0]
            del dnd_choose_character_number[-1]
            character_number = 0
        else: # The chosen number of characters
            # dnd_choose_character_number.pop()
            del dnd_choose_character_number[0]
            del dnd_choose_character_number[-1]
            character_number = int(dnd_choose_character_number[character_number_index -1])


        if character_number > 0:
            # Create the characters
            for _ in range(character_number):
                character = Character()
                characters.append(character)


            clear()
            print(f"A total of {character_number} character(s) will be created.")
            print('Do you want to guide the character generation or have it copmletely automated? ')
            dnd_choose_character_number = ['Automated','Guided','Exit']
            generation_menu = TerminalMenu(dnd_choose_character_number)
            generation_menu_index = generation_menu.show()
            if dnd_choose_character_number[generation_menu_index] == 'Guided':
                for index, character in enumerate(characters):
                    character_number = index + 1
                    # Character Level
                    clear()
                    print("Select Character Level:")
                    dnd_menu_level.append('Random Level')
                    character_level_menu = TerminalMenu(dnd_menu_level)
                    character_level_index = character_level_menu.show()
                    
                    if character_level_index == (len(dnd_menu_level)-1): # Which should be the 'Random Level' index
                        dnd_menu_level.pop()
                        character_level = random.randint(1,21) #random int instead of parsing the menu string
                    else: # The chosen level of the character
                        dnd_menu_level.pop()
                        character_level = int(dnd_menu_level[character_level_index][:8][-3:])


                    # Character Race
                    clear()
                    print("Select Character Race:")
                    dnd_menu_race.append('Random Race')
                    character_race_menu = TerminalMenu(dnd_menu_race)
                    character_race_index = character_race_menu.show()

                    if character_race_index == (len(dnd_menu_race)-1): # Which should be the 'Random Race' index
                        dnd_menu_race.pop()
                        character_race = random.choice(list(dnd_races.keys()))
                        # Alternative method
                        # character_race = random.choice(dnd_menu_race).split()[0]
                    else: # The chosen race of the character
                        dnd_menu_race.pop()
                        character_race = dnd_menu_race[character_race_index].split()[0]


                    # Character Class
                    clear()
                    print("Select Character Class:")
                    dnd_menu_class.append('Random Class')
                    character_class_menu = TerminalMenu(dnd_menu_class)
                    character_class_index = character_class_menu.show()

                    if character_class_index == (len(dnd_menu_class)-1): # Which should be the 'Random Class' index
                        dnd_menu_class.pop()
                        character_class = random.choice(list(dnd_classes.keys()))
                        # Alternative method
                        # character_class = random.choice(dnd_menu_class).split()[0] 
                    else: # The chosen class of the character
                        dnd_menu_class.pop()
                        character_class = dnd_menu_class[character_class_index].split()[0]
                    character_class='Paladin'


                    clear()
                    character_number_tracker += 1
                    all_characters.append(
                        generate_characters(
                            character,
                            character_number_tracker,
                            character_level,
                            character_race,
                            character_class
                        )
                    )
                    display_character(characters)

                input("\nPress Enter to Continue...")

            elif dnd_choose_character_number[generation_menu_index] == 'Automated':
                for index, character in enumerate(characters):

                    clear()
                    character_number_tracker += 1
                    all_characters.append(
                        generate_characters(
                            character,
                            character_number_tracker,
                            character_level = 1, #random.randint(1,21),
                            character_race = random.choice(list(dnd_races.keys())),
                            character_class = 'Paladin' #random.choice(list(dnd_classes.keys()))
                        )
                    )
                    display_character(characters)

                input("\nPress Enter to Continue...")
            else:
                pass


    elif re.compile("^Character Management").match(optionsMenu [selectedMenuOption]):
        
        while True:
            clear()
            print('Character Management')
            print(f"  ====================================================================================================")
            print(f"  Character {'#':<7} {'Race':<15} {'Class':<14} {'Name':<34} {'Created':<20} ")
            print(f"  ====================================================================================================")

            character_list = []
            for index, character in enumerate(all_characters):
                character_list.append(f"Character {character.profile['character number']:<7} {character.character_race['Name']:<15} {character.character_class['Name']:<14} {character.profile['name']['first'] + ' ' + character.profile['name']['last']:<34} {character.profile['created']:<20}")
            character_list.append('Remove Character')
            character_list.append('Exit')

            characters_menu = TerminalMenu(character_list)
            characters_menu_index = characters_menu.show()
            
            if character_list[characters_menu_index] == 'Exit':
                character_list.pop()
                character_list.pop()
                break
            elif character_list[characters_menu_index] == 'Remove Character':
                character_list.pop()
                character_list.pop()

                while True:
                    clear()
                    print("Remove a Character.")
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
                        else:
                            pass  
                break
            else: 
                dnd_menu_level.pop()
                dnd_menu_level.pop()

                clear()
                print(f"You selected {character_list[characters_menu_index]}")
                # dnd_choose_character_number = dir(Character())
                # Gets all the attributues of Character() and removes all the attributes that start with '__'
                dnd_menu_character_class_section_selection = [attr for attr in dir(Character()) if not attr.startswith("__")]

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
    
    
    elif re.compile("^Manage Battle").match(optionsMenu [selectedMenuOption]):
        print('Managing the Battle is under deverlopment...')
        input("\nPress Enter to Continue...")


    elif re.compile("^Items").match(optionsMenu [selectedMenuOption]):
      


        print('Managing the Battle is under deverlopment...')

        stuff_category = ['Items','Equipment','Weapons','Armor']
        print(f"Select one of the following: ")
        stuff_category.append('Exit')
        stuff_category_menu = TerminalMenu(stuff_category)
        stuff_category_menu_index = stuff_category_menu.show()
        
        if stuff_category[stuff_category_menu_index] == 'Exit':
            del stuff_category[-1]
            pass
        else:
            del stuff_category[-1]
            print(stuff_category[stuff_category_menu_index])

            if stuff_category[stuff_category_menu_index] == 'Items':
                display_dnd_menu(dnd_items)
            elif stuff_category[stuff_category_menu_index] == 'Equipment':
                display_dnd_menu(dnd_equipment)
            elif stuff_category[stuff_category_menu_index] == 'Weapons':
                display_dnd_menu(dnd_weapons)
            elif stuff_category[stuff_category_menu_index] == 'Armor':
                display_dnd_menu(dnd_armor)

        input("\nPress Enter to Continue...")


    elif re.compile("^Locations").match(optionsMenu [selectedMenuOption]):

        dnd_locations_menu = {
            "Cities and Towns" : 'Various places where civilization has taken root.',
            "Other Locations" : 'An assortment of bespoke places to possibly explore.',
            "Merchant Shops" : "Planes where you can purchase and sell goods.",
        }
        display_dnd_menu(dnd_locations_menu)
        
        # if re.compile("^Roll Dice").match(optionsMenu [selectedMenuOption]):

            # display_dnd_menu(dnd_locations)
                                        # clear()
                                        # print('Select a location: ')

                                        # # Convert the dicionary into a list
                                        # dnd_locations_menu = []
                                        # for key, value in dnd_locations.items():
                                        #     dnd_locations_menu.append(f"{key} - {value}")


                                        # # Format the list to be pretty in the menu
                                        # def split_two_elements(text):
                                        #     split_text = text.split('-',1)
                                        #     return split_text[0], split_text[1]

                                        # dnd_locations_menu_formatted = []
                                        # for item in dnd_locations_menu:
                                        #     first_element, second_element = split_two_elements(item)
                                        #     dnd_locations_menu_formatted.append(f"{first_element.strip():<30}{second_element.strip()}")
                                        # dnd_locations_menu_formatted = sorted(dnd_locations_menu_formatted)


                                        # # The menu
                                        # print(f"Select from {len(dnd_locations_menu_formatted)} locations: ")
                                        # dnd_locations_menu_formatted.insert(0,'Random Location(s)')
                                        # dnd_locations_menu_formatted.append('Exit')
                                        # locations_menu = TerminalMenu(dnd_locations_menu_formatted)
                                        # dnd_locations_menu_index = locations_menu.show()
                                        
                                        # if dnd_locations_menu_formatted[dnd_locations_menu_index] == 'Random Location(s)':
                                        #     del dnd_locations_menu_formatted[0]
                                        #     del dnd_locations_menu_formatted[-1]
                                        #     while True:
                                        #         try:
                                        #             number_of_random_locations = int(input(f"How many locations? "))
                                        #             break
                                        #         except:
                                        #             print(f"Error: Enter an number.")
                                        #     random_locations = []
                                        #     for location in range(0,number_of_random_locations):
                                        #         random_location = random.choice(dnd_locations_menu_formatted)
                                        #         random_locations.append(random_location)
                                        #         print(random_location)
                                        #     #print(random_locations)  
                                    
                                        # elif dnd_locations_menu_formatted[dnd_locations_menu_index] == 'Exit':
                                        #     del dnd_locations_menu_formatted[0]
                                        #     del dnd_locations_menu_formatted[-1]
                                        #     pass
                                        # else:
                                        #     del dnd_locations_menu_formatted[0]
                                        #     del dnd_locations_menu_formatted[-1]
                                        #     print(dnd_locations_menu_formatted[dnd_locations_menu_index])

                                        # input("\nPress Enter to Continue...")

    elif re.compile("^Roll Dice").match(optionsMenu [selectedMenuOption]):

        dnd_roll_dice()


    elif re.compile("^ChatGPT").match(optionsMenu [selectedMenuOption]):
        user_query = input(f"Ask ChatGPT: ")
        chatgpt_response = query_chatgpt(openai_key,user_query)
        print(chatgpt_response)
        input("\nPress Enter to Continue...")
    

# if __name__ == '__main__':
#     menu()