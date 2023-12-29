#! /usr/bin/env python3

import re, time, sys
from simple_term_menu import TerminalMenu
from dnd_helper import *
from dnd_generate_character import *
from dnd_lists import *
from dnd_towns_and_cities import *
from dnd_spells import *
from dnd_monsters import *
from chatgpt import *
from my_secrets import *
import pickle_handler
import readline
import dnd_encounter

dnd_dungeon_master = """
\033[93m _____        _____    \033[0m         \033[92m _____                                        __  __           _            
\033[93m|  __ \      |  __ \   \033[0m         \033[92m|  __ \                                      |  \/  |         | |           
\033[93m| |  | |_ __ | |  | |  \033[0m _____   \033[92m| |  | |_   _ _ __   __ _  ___  ___  _ __    | \  / | __ _ ___| |_ ___ _ __ 
\033[93m| |  | | '_ \| |  | |  \033[0m|_____|  \033[92m| |  | | | | | '_ \ / _` |/ _ \/ _ \| '_ \   | |\/| |/ _` / __| __/ _ \ '__|
\033[93m| |__| | | | | |__| |  \033[0m         \033[92m| |__| | |_| | | | | (_| |  __/ (_) | | | |  | |  | | (_| \__ \ ||  __/ |   
\033[93m|_____/|_| |_|_____/\033[94m(5e)\033[0m        \033[92m|_____/ \__,_|_| |_|\__, |\___|\___/|_| |_|  |_|  |_|\__,_|___/\__\___|_|\033[94m(DM)  
\033[93m                                       \033[92m              __/ |                                                  
\033[93m                                       \033[92m             |___/                                                   
"""


main_menu_list  = [
    'Character Management',
    'Manage Encounter',
    'Items, Weapons, Armor, Equipment',
    'Spells and Cantrips',
    'Monster Manual',
    'Locations, Cities, and Towns',
    'Roll Dice',
    'Create Character',
    'Ask ChatGPT a question',
    'Exit DnD Dungeon Master'
]

    # '🎭 Character Management',
    # '⚔️ Manage Encounter',
    # '🛡️ Items, Weapons, Armor, Equipment',
    # '🪄 Spells and Cantrips',
    # '🐉 Monster Manual',
    # '🏰 Locations, Cities, and Towns',
    # '🎲 Roll Dice',
    # '✍️ Create Character',
    # '❓ Ask ChatGPT a question',
    # '🚪 Exit DnD Dungeon Master'




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
    menu_formatted = ["Random Selections(s)"] + menu_formatted + ["Exit"] 

    # The menu
    print(f"Select from {len(menu_formatted)} options: ")
    # menu_formatted.insert(0, 'Random Selection(s)')
    # menu_formatted.append('Exit')
    terminal_menu = TerminalMenu(menu_formatted)
    menu_index = terminal_menu.show()
    # del menu_formatted[0]
    # del menu_formatted[-1]

    # Handling menu selections
    if menu_formatted[menu_index] == 'Random Selection(s)':
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
        return random_selections
    elif menu_formatted[menu_index] == 'Exit':
        return None
    else: # prints the selection
        del menu_formatted[0]
        del menu_formatted[-1]
        return menu_formatted[menu_index - 1]


# Option to load previous save files
all_characters = pickle_handler.select_and_load_pkl()
if all_characters is not None:
    print("Characters loaded")
else:
    print("No Characters loaded")
    all_characters = []




def main():
    # Used for tracking purposes as to not re-use character numbers when new ones are created
    if len(all_characters) > 0:
        character_number_tracker = max((char.profile['character number'] for char in all_characters), default=0)
    else:
        character_number_tracker = 0


    while True:
        clear()
        print(dnd_dungeon_master)
        print(f"\033[91mAlmighty Dungeon Master, what do you want to do?\033[0m\n")
        menuMain = TerminalMenu(main_menu_list)
        menu_main_index = menuMain.show()
        main_menu_selected = main_menu_list[menu_main_index]

        if re.compile("^Exit").match(main_menu_selected):
            #exit the script DnD DM
            break

        elif re.compile("^Create Character").match(main_menu_selected):
            
            create_character(all_characters,character_number_tracker,only_one=False)


        elif re.compile("^Character Management").match(main_menu_selected):            
            character_management(all_characters)
        
        elif re.compile("^Manage Encounter").match(main_menu_selected):
            dnd_encounter.main(all_characters)

        elif re.compile("^Items").match(main_menu_selected):
            # TODO: under deverlopment..

            stuff_category = ['Items','Equipment','Weapons','Armor','Exit']
            print(f"\033[91mSelect one of the following:\033[0m\n")
            # stuff_category.append('Exit')
            stuff_category_menu = TerminalMenu(stuff_category)
            stuff_category_menu_index = stuff_category_menu.show()
            # del stuff_category[-1]
        
            if stuff_category[stuff_category_menu_index] == 'Exit':
                break
            else:
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


        elif re.compile("^Spells").match(main_menu_selected):
        
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


        elif re.compile("^Locations").match(main_menu_selected):

            dnd_locations_menu = {
                "Cities and Towns" : 'Various places where civilization has taken root.',
                "Ohter Locations" : 'An assortment of bespoke places to possibly explore.',
                "Merchant Shops" : "Planes where you can purchase and sell goods.",
            }
            selected_location = print_dnd_menu(dnd_locations_menu)

            if re.compile("^Cities and Towns").match(selected_location):
                clear()
                dnd_towns_and_cities_formated = {}
                for city in dnd_towns_and_cities.items():
                    dnd_towns_and_cities_formated[city[0]] = city[1]['Description']

                dnd_city_selected = print_dnd_menu(dnd_towns_and_cities_formated)
                print(f"You selected: {dnd_city_selected}")
                print_character(dnd_towns_and_cities[dnd_city_selected.split()[0]], padding_value = 50)


            if re.compile("^Ohter Locations").match(selected_location):
                clear()
                dnd_locations_formated = {}
                for location in dnd_locations.items():
                    dnd_locations_formated[location[0]] = location[1]

                dnd_location_selected = print_dnd_menu(dnd_locations_formated)
                print(f"You selected: {dnd_location_selected}")
                print_character(dnd_locations[dnd_location_selected.split()[0]], padding_value = 50)
                
                
            if re.compile("^Merchant Shops").match(selected_location):
                clear()
                print(f"Dan... Added some show generation")
                # print_character(selected_location)
                        
            input("\nPress Enter to Continue...")
            
        elif re.compile("^Monster Manual").match(main_menu_selected):
            # print_character(dnd_monsters)

            # # Set the autocomplete function
            # readline.set_completer(autocomplete_inventory(dnd_monsters))
            # readline.parse_and_bind("tab: complete")

            # while True:
            #     user_input = input("Enter an item from your inventory: ")
            #     user_input = user_input.lower()  # Convert user input to lowercase
                
            #     # Check if the entered item (in lowercase) is in the inventory
            #     if user_input in dnd_monsters:
            #         print(f"You have {dnd_monsters[user_input]} {user_input}(s) in your inventory.")
            #         break
            #     else:
            #         print(f"{user_input} is not in your inventory. Please enter a valid item.")

            def autocomplete_inventory(text, state):
                text_lower = text.lower()
                options = [key for key in dnd_monsters.keys() if text_lower in key.lower()]
                if state < len(options):
                    return options[state]
                else:
                    return None
                
            readline.set_completer(autocomplete_inventory)
            readline.parse_and_bind("tab: complete")

            while True:
                user_input = input("Enter an item from your inventory: ")
                user_input = user_input.lower()  # Convert user input to lowercase
                
                # Check if the entered item (in lowercase) is in the inventory
                lowercase_keys = [key.lower() for key in dnd_monsters.keys()]
                if user_input in lowercase_keys:
                    # Find the original key with matching lowercase version
                    matching_key = list(dnd_monsters.keys())[lowercase_keys.index(user_input)]
                    print(f"[+] You have {dnd_monsters[matching_key]} {matching_key}(s) in your inventory.")
                    break
                else:
                    print(f"[-] {user_input} is not in your inventory. Please enter a valid item.")


            input("\nPress Enter to Continue...")


        elif re.compile("^Ask ChatGPT a question").match(main_menu_selected):
            user_query = input(f"Ask ChatGPT: ")
            chatgpt_response = query_chatgpt(openai_key,user_query)
            print(chatgpt_response)
            input("\nPress Enter to Continue...")
        

        elif re.compile("^Roll Dice").match(main_menu_selected):
            dnd_roll_dice()
            input("\nPress Enter to Continue...")


if __name__ == '__main__':
    main()