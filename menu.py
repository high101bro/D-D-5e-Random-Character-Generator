#! /usr/bin/env python3

import re, time, sys
from simple_term_menu import TerminalMenu
from dnd_generate_character import *
from dnd_helper import *
from dnd_lists import *
from dnd_cities import *
from dnd_spells import *
from dnd_monsters import *
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
    'Spells and Cantrips',
    'Monster Manual',
    'Locations, Cities, and Towns',
    'Manage Battle',
    'Roll Dice',
    'ChatGPT'
]

all_characters = []
character_number_tracker = 0





def print_dnd_menu(items_dictionary,pad=30):

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
        menu_formatted.append(f"{first_element.strip():<{pad}}{second_element.strip()}")
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
            # debug(random_selection)
        return random_selections
    elif menu_formatted[menu_index] == 'Exit':
        # debug(menu_formatted[menu_index])
        return None
    else: # prints the selection
        del menu_formatted[0]
        del menu_formatted[-1]
        # debug(menu_formatted[menu_index - 1])
        return menu_formatted[menu_index - 1]
    




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
        characters_on_the_battlefield = []
        number_of_characters = int(input(f"How many characters? "))
        class Character_in_battle():
            def __init__(self):
                self.name = ''
                self.cr = 0
                self.char_race = ''
                self.char_class = ''
                self.type = ''
                self.ac = 0
                self.hp = 0
                self.speed = 0
                self.initiative = 0
                self.str = 0
                self.dex = 0
                self.con = 0
                self.int = 0
                self.wis = 0
                self.cha = 0
                self.attacks = {}
                self.attack_number = 1
        dan = Character_in_battle()
        dan.name = 'Elowen'
        dan.cr = 2
        dan.level = 2
        dan.pb = 2
        dan.char_race = 'elf'
        dan.char_class = 'ranger'
        dan.type = 'character'
        dan.ac = 12+5+1
        dan.hp = 20
        dan.speed = 25
        dan.initiative = '1d20 + dex'
        dan.str = 2
        dan.dex = 5
        dan.con = 1
        dan.int = 0
        dan.wis = 2
        dan.cha = -1
        dan.attacks = {
            'long bow' : '1d20 + 1d8 + dex + pb',
            'rapier' : '1d20 + 1d8 + dex + pb',
        }
        dan.attack_number = 1

        while True:
            # input(f"Enter the character name: ")
            dan = Character_in_battle()
            dan.name = 'dan'
            dan.ac = 17
            break
        print(
            dan.name,
            dan.ac
        )
        debug(dan)


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
                print_dnd_menu(dnd_items)
            elif stuff_category[stuff_category_menu_index] == 'Equipment':
                print_dnd_menu(dnd_equipment)
            elif stuff_category[stuff_category_menu_index] == 'Weapons':
                print_dnd_menu(dnd_weapons)
            elif stuff_category[stuff_category_menu_index] == 'Armor':
                print_dnd_menu(dnd_armor)

        input("\nPress Enter to Continue...")


    elif re.compile("^Spells").match(optionsMenu [selectedMenuOption]):
    
        dnd_menu_spells = {
            "Cantrips": "Simple, low-level spells that can be cast at will for minor magical effects.",
            "1st Level": "Basic magical abilities for novice spellcasters with various effects.",
            "2nd Level": "Slightly more powerful than 1st-level spells, offering improved or new abilities.",
            "3rd Level": "Significant spells with a noticeable increase in power and versatile effects.",
            "4th Level": "Potent and versatile spells with a wide range of magical effects.",
            "5th Level": "Powerful spells that can have game-changing effects in combat or utility.",
            "6th Level": "High-level magic with incredible feats, reshaping battles and providing advantages.",
            "7th Level": "Among the most powerful magic accessible to adventurers, affecting regions.",
            "8th Level": "Exceedingly rare and potent spells, capable of bending reality and shaping epic adventures.",
            "9th Level": "The pinnacle of magical power, granting god-like abilities to alter reality itself.",
        }


        dnd_menu_spell_selection = print_dnd_menu(dnd_menu_spells)
        # debug(dnd_menu_spell_selection)
        if dnd_menu_spell_selection.split()[0] == "Cantrips":
            dnd_menu_spell_formated_list = []
            dnd_menu_spell_formated_dict = {}
            for index, spell in enumerate(dnd_spells[dnd_menu_spell_selection.split()[0]]):
                spell_formatted = f"{spell:<20} {dnd_spells['Cantrips'][spell]['School']:<18} {dnd_spells['Cantrips'][spell]['Components']:<11} {dnd_spells['Cantrips'][spell]['Casting Time']:<13} {dnd_spells['Cantrips'][spell]['Range']:<21} {dnd_spells['Cantrips'][spell]['Duration']:<20}"
                dnd_menu_spell_formated_list.append(spell_formatted)
                dnd_menu_spell_formated_dict[index] = spell
            dnd_menu_spell_selected = TerminalMenu(dnd_menu_spell_formated_list)
            dnd_menu_spell_selected_index = dnd_menu_spell_selected.show()
            print(dnd_menu_spell_formated_dict[dnd_menu_spell_selected_index])
            print_character(dnd_spells['Cantrips'][dnd_menu_spell_formated_dict[dnd_menu_spell_selected_index]],2)

        else:
            dnd_menu_spell_level_selection = dnd_menu_spell_selection.split()[0][0]
            dnd_menu_spell_formated_list = []
            dnd_menu_spell_formated_dict = {}

            for index, spell in enumerate(dnd_spells[int(dnd_menu_spell_level_selection)]):
                spell_formatted = f"{spell:<20} {dnd_spells[int(dnd_menu_spell_level_selection)][spell]['School']:<18} {dnd_spells[int(dnd_menu_spell_level_selection)][spell]['Components']:<11} {dnd_spells[int(dnd_menu_spell_level_selection)][spell]['Casting Time']:<21} {dnd_spells[int(dnd_menu_spell_level_selection)][spell]['Range']:<21} {dnd_spells[int(dnd_menu_spell_level_selection)][spell]['Duration']:<20}"
                dnd_menu_spell_formated_list.append(spell_formatted)
                dnd_menu_spell_formated_dict[index] = spell
            dnd_menu_spell_selected = TerminalMenu(dnd_menu_spell_formated_list)
            dnd_menu_spell_selected_index = dnd_menu_spell_selected.show()
            print(dnd_menu_spell_formated_dict[dnd_menu_spell_selected_index])
            print_character(dnd_spells[int(dnd_menu_spell_level_selection)][dnd_menu_spell_formated_dict[dnd_menu_spell_selected_index]],2)
        
        input("\nPress Enter to Continue...")


    elif re.compile("^Locations").match(optionsMenu [selectedMenuOption]):

        dnd_locations_menu = {
            "Cities and Towns" : 'Various places where civilization has taken root.',
            "Ohter Locations" : 'An assortment of bespoke places to possibly explore.',
            "Merchant Shops" : "Planes where you can purchase and sell goods.",
        }
        selected_location = print_dnd_menu(dnd_locations_menu)

        if re.compile("^Cities and Towns").match(selected_location):
            dnd_cities_formated = {}
            for city in dnd_cities.items():
                dnd_cities_formated[city[0]] = city[1]['description']

            dnd_city_selected = print_dnd_menu(dnd_cities_formated)
            print(f"You selected: {dnd_city_selected}")
            print_character(dnd_cities[dnd_city_selected.split()[0]], padding_value = 50)


        if re.compile("^Ohter Locations").match(selected_location):
            dnd_locations_formated = {}
            for location in dnd_locations.items():
                dnd_locations_formated[location[0]] = location[1]

            dnd_location_selected = print_dnd_menu(dnd_locations_formated)
            print(f"You selected: {dnd_location_selected}")
            print_character(dnd_locations[dnd_location_selected.split()[0]], padding_value = 50)
            
            
        if re.compile("^Merchant Shops").match(selected_location):
            print(f"Dan... Added some show generation")
            # print_character(selected_location)
                    
        input("\nPress Enter to Continue...")
        
    elif re.compile("^Monster Manual").match(optionsMenu [selectedMenuOption]):
        print_character(dnd_monsters)
        input("\nPress Enter to Continue...")


    elif re.compile("^ChatGPT").match(optionsMenu [selectedMenuOption]):
        user_query = input(f"Ask ChatGPT: ")
        chatgpt_response = query_chatgpt(openai_key,user_query)
        print(chatgpt_response)
        input("\nPress Enter to Continue...")
    

    elif re.compile("^Roll Dice").match(optionsMenu [selectedMenuOption]):
        dnd_roll_dice()
        input("\nPress Enter to Continue...")


# if __name__ == '__main__':
#     menu()