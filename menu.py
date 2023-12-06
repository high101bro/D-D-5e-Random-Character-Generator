#! /usr/bin/env python3

import re
from simple_term_menu import TerminalMenu
from dnd_generate_character import *
from dnd_lists import *


# def menu():
#     click.echo('Hello, World!')
clear()

characters = []

optionsMenu  = [
    'Create Character',
    'Manage Character',
    'Manage Battle',
    'Roll Dice'
]


menuMain = TerminalMenu(optionsMenu)
selectedMenuOption = menuMain.show()
if re.compile("^Create Character").match(optionsMenu [selectedMenuOption]):

    # Number of Characters
    clear()
    print('How many characters do you want to create? ')
    dnd_choose_character_number = ['1','2','3','4','5','6','7','8','9','10']
    dnd_choose_character_number.append('Random Number')
    character_number_menu = TerminalMenu(dnd_choose_character_number)
    character_number_index = character_number_menu.show()


    if character_number_index == (len(dnd_choose_character_number)-1): # Which should the 'Random Number' index
        dnd_choose_character_number.pop()
        character_number = int(random.choice(dnd_choose_character_number))
    else: # The chosen number of characters
        character_number = int(dnd_choose_character_number[character_number_index])

    for _ in range(character_number):
        character = Character()
        characters.append(character)

    
    for character in characters:

        # Character Level
        clear()
        print("Select Character Level:")
        dnd_menu_level.append('Random Level')
        character_level_menu = TerminalMenu(dnd_menu_level)
        character_level_index = character_level_menu.show()
        
        if character_level_index == (len(dnd_menu_level)-1): # Which should the 'Random Level' index
            dnd_menu_level.pop()
            character_level = random.randint(1,21) #random int instead of parsing the menu string
            int(random.choice(dnd_choose_character_number))
        else: # The chosen level of the character
            character_level = int(dnd_menu_level[character_level_index][:8][-3:])


        # Character Race
        clear()
        print("Select Character Race:")
        dnd_menu_race.append('Random Race')
        character_race_menu = TerminalMenu(dnd_menu_race)
        character_race_index = character_race_menu.show()

        if character_race_index == (len(dnd_menu_race)-1): # Which should the 'Random Race' index
            dnd_menu_race.pop()
            character_race = random.choice(list(dnd_races.keys()))
            # Alternative method
            # character_race = random.choice(dnd_menu_race).split()[0]
        else: # The chosen race of the character
            character_race = dnd_menu_race[character_race_index].split()[0]


        # Character Class
        clear()
        print("Select Character Class:")
        dnd_menu_class.append('Random Class')
        character_class_menu = TerminalMenu(dnd_menu_class)
        character_class_index = character_class_menu.show()

        if character_class_index == (len(dnd_menu_class)-1): # Which should the 'Random Class' index
            dnd_menu_class.pop()
            character_class = random.choice(list(dnd_classes.keys()))
            # Alternative method
            # character_class = random.choice(dnd_menu_class).split()[0] 
        else: # The chosen class of the character
            character_class = dnd_menu_class[character_class_index].split()[0]
        character_class='Paladin'


        clear()
        generate_characters(
            character,
            character_level,
            character_race,
            character_class
        )
        display_character(characters)

elif re.compile("^Manage Character").match(optionsMenu [selectedMenuOption]):
    print('Managing a character is under deverlopment...')
elif re.compile("^Manage Battle").match(optionsMenu [selectedMenuOption]):
    print('Managing the Battle is under deverlopment...')
elif re.compile("^Roll Dice").match(optionsMenu [selectedMenuOption]):
    print('Rolling dice is under deverlopment...')
    

# if __name__ == '__main__':
#     menu()