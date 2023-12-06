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
                    all_characters.append(
                        generate_characters(
                            character,
                            character_number,
                            character_level,
                            character_race,
                            character_class
                        )
                    )
                    display_character(characters)

                input('Press Enter to Continue...')

            elif dnd_choose_character_number[generation_menu_index] == 'Automated':
                for index, character in enumerate(characters):
                    character_number = index + 1

                    clear()
                    all_characters.append(
                        generate_characters(
                            character,
                            character_number,
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
            for character in all_characters:
                character_list.append(f"Character {character.profile['character number']:<7} {character.profile['race']['Name']:<15} {character.profile['class']['Name']:<14} {character.profile['name']['first'] + ' ' + character.profile['name']['last']:<34} {character.profile['created']:<20}")
            character_list.append('Exit')

            characters_menu = TerminalMenu(character_list)
            characters_menu_index = characters_menu.show()
            
            if character_list[characters_menu_index] == 'Exit':
                character_list.pop()
                break
            else: 
                dnd_menu_level.pop()

                clear()
                print(f"You selected {character_list[characters_menu_index]}")
                # dnd_choose_character_number = dir(Character())
                # Gets all the attributues of Character() and removes all the attributes that start with '__'
                dnd_menu_character_class_section_selection = [attr for attr in dir(Character()) if not attr.startswith("__")]

                # Selecte Character Class()
                # debug(
                #     characters[characters_menu_index].profile['race']['Name']
                # )
                # debug(
                #     characters[characters_menu_index].profile['class']['Name']
                # )
                # debug(
                #     characters[characters_menu_index].profile['name']['first']
                # )

                dnd_menu_character_class_section_selection_menu = TerminalMenu(dnd_menu_character_class_section_selection)
                dnd_menu_character_class_section_selection_menu_index = dnd_menu_character_class_section_selection_menu.show()

                
                # debug(
                #     dnd_menu_character_class_section_selection_menu_index
                # )
                # debug(
                #     dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index]
                # )
                # print_character(characters[characters_menu_index].profile)
                if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'profile':            
                    print_character(characters[characters_menu_index].profile)
                if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'capabilities':            
                    print_character(characters[characters_menu_index].profile)
                if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'items':            
                    print_character(characters[characters_menu_index].profile)
                if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'weapons':            
                    print_character(characters[characters_menu_index].profile)
                if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'spells':            
                    print_character(characters[characters_menu_index].profile)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'stats':
                #     print_character(characters[characters_menu_index].stats)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'inventory':
                #     print_character(characters[characters_menu_index].inventory)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'spells':
                #     print_character(characters[characters_menu_index].spells)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'equipment':
                #     print_character(characters[characters_menu_index].equipment)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'proficiencies':
                #     print_character(characters[characters_menu_index].proficiencies)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'features':
                #     print_character(characters[characters_menu_index].features)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'traits':
                #     print_character(characters[characters_menu_index].traits)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'background':
                #     print_character(characters[characters_menu_index].background)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'alignment':
                #     print_character(characters[characters_menu_index].alignment)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'languages':
                #     print_character(characters[characters_menu_index].languages)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'actions':
                #     print_character(characters[characters_menu_index].actions)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'reactions':
                #     print_character(characters[characters_menu_index].reactions)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'bonus actions':
                #     print_character(characters[characters_menu_index].bonus_actions)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'legendary actions':
                #     print_character(characters[characters_menu_index].legendary_actions)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'hitpoints':
                #     print_character(characters[characters_menu_index].hitpoints)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'armor class':
                #     print_character(characters[characters_menu_index].armor_class)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'initiative':
                #     print_character(characters[characters_menu_index].initiative)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'speed':
                #     print_character(characters[characters_menu_index].speed)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'hitdice':
                #     print_character(characters[characters_menu_index].hitdice)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'level':
                #     print_character(characters[characters_menu_index].level)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'proficiency bonus':
                #     print_character(characters[characters_menu_index].proficiency_bonus)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'experience points':
                #     print_character(characters[characters_menu_index].experience_points)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'inspiration':
                #     print_character(characters[characters_menu_index].inspiration)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'saving throws':
                #     print_character(characters[characters_menu_index].saving_throws)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'skills':
                #     print_character(characters[characters_menu_index].skills)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'personality traits':
                #     print_character(characters[characters_menu_index].personality_traits)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'ideals':
                #     print_character(characters[characters_menu_index].ideals)
                # elif dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] ==

                # if dnd_choose_character_number[character_number_index] == 'Random Number': # Which should be the 'Random Number' index











            input('Press Enter to Continue...')
    
    
    elif re.compile("^Manage Battle").match(optionsMenu [selectedMenuOption]):
        print('Managing the Battle is under deverlopment...')
        input('Press Enter to Continue...')
    
    
    elif re.compile("^Roll Dice").match(optionsMenu [selectedMenuOption]):
        print('Rolling dice is under deverlopment...')
        input('Press Enter to Continue...')
    

# if __name__ == '__main__':
#     menu()