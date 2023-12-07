#! /usr/bin/env python3

import re
from simple_term_menu import TerminalMenu
from dnd_generate_character import *
from dnd_lists import *


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
    'Manage Battle',
    'Roll Dice'
]

all_characters = []
character_number_tracker = 0

def debug(show):
    ts = input(f"{show}")
    return print(ts)

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

                input('Press Enter to Continue...')

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

                input('Press Enter to Continue...')
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

            input('Press Enter to Continue...')
    
    
    elif re.compile("^Manage Battle").match(optionsMenu [selectedMenuOption]):
        print('Managing the Battle is under deverlopment...')
        input('Press Enter to Continue...')
    
    
    elif re.compile("^Roll Dice").match(optionsMenu [selectedMenuOption]):
        print('Rolling dice is under deverlopment...')
        input('Press Enter to Continue...')
    

# if __name__ == '__main__':
#     menu()