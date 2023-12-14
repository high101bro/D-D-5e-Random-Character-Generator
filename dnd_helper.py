#! /usr/bin/env python3

import readline
import os
import random, sys, time
from simple_term_menu import TerminalMenu
import pickle_handler 
from dnd_spells import *
from dnd_lists import *


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



def character_management_banner():
        print(f"  ===============================================================================================================")
        print(f"  Character {'#':<7} {'Level':<10} {'Race':<15} {'Class':<14} {'Name':<34} {'Created':<20} ")
        print(f"  ===============================================================================================================")

def character_management(all_characters):
    while True:
        clear()
        print('Character Management')
        character_management_banner()
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
                    # character_remove_list.pop()
                    break
                else:
                    # character_remove_list.pop()
                    character_remove_confirm = input(f"Are you sure you want to delete the following?\n\n  {character_remove_list[characters_menu_index]}\n\nEnter 'd' to confirm deletion: ")
                    if character_remove_confirm.lower() == 'd':
                        del character_remove_list[characters_menu_index]
                        del all_characters[characters_menu_index]
                        pickle_handler.save_dnd_state('characters', all_characters)
                        break
                    else:
                        pass  
            
        else: 
            clear()
            character_management_banner()
            print(f"  {character_list[characters_menu_index]}")
            print(f"")

            # dnd_choose_character_number = dir(Character())
            # Gets all the attributues of Character() and removes all the attributes that start with '__'
            # dnd_menu_character_class_section_selection = [attr for attr in dir(Character()) if not attr.startswith("__")]
            dnd_menu_character_class_section_selection = ["Armor","attributes","background","capabilities","character_class","character_race","combat","description","features","items","level_chart","money","profile","skills","spells","weapons"] 
 
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
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Armor':
                print_character(all_characters[characters_menu_index].armor)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'weapons':
                print_character(all_characters[characters_menu_index].weapons)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'combat':
                print_character(all_characters[characters_menu_index].combat)
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'spells':


                if all_characters[characters_menu_index].character_class['Name'] in half_magic_classes:
                    if all_characters[characters_menu_index].character_class['Name'] == "Paladin":
                        pass
                    if all_characters[characters_menu_index].character_class['Name'] == "Ranger":
                        pass
                    if all_characters[characters_menu_index].character_class['Name'] == "Warlock":
                        pass

                elif all_characters[characters_menu_index].character_class['Name'] in magic_classes:
                    spell_level_list = list(all_characters[characters_menu_index].spells['Spells Known']['Slots'])
                    spell_level_list.append('Exit')
                    while True:
                        clear()
                        def spell_menu_banner():
                            print(f"  ========================================================================================================================================================================================================")
                            print(f"  {spell_level_title:<35} {'SEL':<5} {'School':<20} {'Damage':<10} {'Saving Throw':<15} {'Range':<22} {'Duration':<32} {'Casting Time':<25} {'Components':<12}")
                            print(f"  ========================================================================================================================================================================================================")
                        spell_menu_banner


                        #example: Cantrips, 1st, 2nd...
                        spell_level_menu = TerminalMenu(spell_level_list, title="Select Level")
                        spell_level_index = spell_level_menu.show()
                        spell_level_selected = list(spell_level_list)[spell_level_index]

                        if spell_level_selected == 'Exit':
                            break
                        else:
                            while True:
                                spells_in_level_list = list(all_characters[characters_menu_index].spells['Spells Known']["Slots"][spell_level_selected]['Known Spells'].keys())
                                spell_list_formatted = []
                                if spell_level_selected == 'Cantrips':
                                    spell_level_title = spell_level_selected.rstrip('s') + " Spells"
                                else:
                                    spell_level_title = spell_level_selected + " Level Spells"

                                spell_menu_banner()
                                spells_not_found = []
                                error_messages = []
                                for spell in spells_in_level_list:
                                    try:
                                        School = dnd_spells[spell_level_selected][spell]['School']
                                        # Damage = dnd_spells[spell_level_selected][spell]['Damage'] # Dan update this
                                        Range = dnd_spells[spell_level_selected][spell]['Range']
                                        Duration = dnd_spells[spell_level_selected][spell]['Duration']
                                        try:
                                            DC_Saving_Throw = dnd_spells[spell_level_selected][spell]['DC Saving Throw']
                                        except:
                                            DC_Saving_Throw = "None"
                                        Casting_Time = dnd_spells[spell_level_selected][spell]['Casting Time']
                                        Components = dnd_spells[spell_level_selected][spell]['Components']

                                        if spell in all_characters[characters_menu_index].spells["Selected Spells"]:
                                            spell_list_formatted.append(f"{spell:<35} {'[X]':<5} {School:<20} {'Damage':<10} {DC_Saving_Throw:<15} {Range:<22} {Duration:<32} {Casting_Time:<25} {Components:<12}")
                                        elif spell not in all_characters[characters_menu_index].spells["Selected Spells"]:
                                            spell_list_formatted.append(f"{spell:<35} {'[ ]':<5} {School:<20} {'Damage':<10} {DC_Saving_Throw:<15} {Range:<22} {Duration:<32} {Casting_Time:<25} {Components:<12}")

                                    except Exception as err:
                                        spells_not_found.append(spell)
                                if len(spells_not_found) > 0:
                                    print(f"[!] Error loading spell: {spells_not_found}")
                                    input("\nPress Enter to Continue...")


                                spell_list_formatted.append('Exit')

                                clear()
                                spell_menu_banner()
                                spell_name_menu2 = TerminalMenu(spell_list_formatted, title='Select Spell')
                                spell_name_index2 = spell_name_menu2.show()
                                spell_name_selected2 = spell_list_formatted[spell_name_index2]
                                spell_name_selected2 = spell_name_selected2.split('[')[0].strip()

                                if spell_name_selected2 == 'Exit':
                                    break
                                else:
                                    while True:
                                        spell_selection_list = ["Get Details","Select","Unselect", "Exit"]
                                        spell_selection_menu = TerminalMenu(spell_selection_list, title="Select what to do with the spell:")
                                        spell_selection_index = spell_selection_menu.show()
                                        spell_selection_selected = spell_selection_list[spell_selection_index]

                                        if spell_selection_selected == "Exit":
                                            break

                                        elif spell_selection_selected == "Get Details":
                                            clear()
                                            print(f"======================================================================================================================================================")
                                            print(f"{spell_level_title.rstrip('s')} : {spell_name_selected2}")
                                            print(f"======================================================================================================================================================")
                                            print_character(dnd_spells[spell_level_selected][spell_name_selected2])
                                            input("\nPress Enter to Continue...")
                                            break
                                        elif spell_selection_selected == "Select":
                                            try:
                                                if spell_selection_selected not in all_characters[characters_menu_index].spells["Selected Spells"]:
                                                    all_characters[characters_menu_index].spells["Selected Spells"].append(spell_name_selected2)
                                                    pickle_handler.save_dnd_state('characters', all_characters)
                                            except:
                                                pass
                                            break
                                        elif spell_selection_selected == "Unselect":
                                            try:
                                                all_characters[characters_menu_index].spells["Selected Spells"].remove(spell_name_selected2)
                                                pickle_handler.save_dnd_state('characters', all_characters)
                                            except:
                                                pass
                                            break
                                        debug(all_characters[characters_menu_index].spells["Selected Spells"])

                            # input("\nPress Enter to Continue...")
            # input("\nPress Enter to Continue...")



