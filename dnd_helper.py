#! /usr/bin/env python3

import readline
import os
import random, sys, time
from simple_term_menu import TerminalMenu
import pickle_handler 
from dnd_spells import *
from dnd_lists import *
import numpy as np
from dnd_classes import *
import textwrap
from dnd_npc_conversation import *


def debug(show):
    print(f"[Debug] Type: {type(show)} == Value: {show}")
    input("\nPress Enter to Continue...")
    return 


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def text_wrap(long_text,line_length=100, initial_indent="", padding_value=35, spaces=2):

    subsequent_indent = ' ' * (padding_value + spaces + 1)  # The + 1 accounts for the :

    # Use textwrap to format the string with an initial indent
    wrapped_text = textwrap.fill(long_text, width=line_length, initial_indent=initial_indent)

    # Manually add subsequent indent to the wrapped lines
    formatted_text = '\n'.join([initial_indent + line if i == 0 else subsequent_indent + line for i, line in enumerate(wrapped_text.splitlines())])

    return formatted_text


def choose_random_spell(character, spell_list, chosen_temp_list):
    random_spell = random.choice(spell_list)
    if random_spell == None:
        choose_random_spell(character, spell_list, chosen_temp_list)
    elif random_spell in chosen_temp_list:
        choose_random_spell(character, spell_list, chosen_temp_list)
    elif random_spell not in chosen_temp_list:
        # return random_spell, chosen_temp_list
        chosen_temp_list.append(random_spell)
        character.spells["Selected Spells"].append(random_spell)


def terminalmenu_quick_select(list,title):
    terminal_menu = TerminalMenu(list,title=title)
    terminal_menu_index = terminal_menu.show()
    return list[terminal_menu_index]


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
            # Define the desired line length and indent
            # initial_indent = ""  # 4 spaces for initial indent
            # subsequent_indent = ' ' * (padding_value + spaces + 1)  # The + 1 accounts for the :

            # Use textwrap to format the string with an initial indent
            # wrapped_text = textwrap.fill(value, width=100, initial_indent=initial_indent)

            # Manually add subsequent indent to the wrapped lines
            # formatted_text = '\n'.join([initial_indent + line if i == 0 else subsequent_indent + line for i, line in enumerate(wrapped_text.splitlines())])
            # value = formatted_text

            if isinstance(value, dict):  # Check if value is a nested dictionary
                print(f"\n{' ' * spaces}{key} :")
                print_character(value, spaces + 2)  # recursively call the function to handle nested dictionary
            elif isinstance(value, list):  
                print(f"{' ' * spaces}{key} :")
                list_space = spaces -1
                for v in value:
                    print(f"{' ' * (padding_value + list_space)}- {v}")
                print_character(value, spaces + 2)  # recursively call the function to handle nested dictionary
            else:
                padding = padding_value - spaces
                print(f"{' ' * spaces}{f'{key:<{padding}}'} : {value}")  # print key-value pair if value is not a nested dictionary
    except:
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
            break
        elif character_list[characters_menu_index] == 'Delete Character':

            while True:
                clear()
                print("Delete a Character from the Game.")
                character_management_banner()

                character_remove_list = []
                for character in all_characters:
                    character_remove_list.append(f"Character {character.profile['character number']:<7} {character.profile['level']:<10} {character.character_race['Name']:<15} {character.character_class['Name']:<14} {character.profile['name']['first'] + ' ' + character.profile['name']['last']:<34} {character.profile['created']:<20}")
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
            dnd_menu_character_class_section_selection = ["Chat with the Character","Profile","Description","Background","Features","Spells","Attributes","Skills","Capabilities","Money","Items","Weapons","Armor","Combat","Race Details","Class Details","Level Chart","Exit"] 
 
            dnd_menu_character_class_section_selection_menu = TerminalMenu(dnd_menu_character_class_section_selection)
            dnd_menu_character_class_section_selection_menu_index = dnd_menu_character_class_section_selection_menu.show()


            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Chat with the Character':
                character_names = [f"{character.profile['name']['first']} {character.profile['name']['last']} the {character.character_race['Name']} {character.character_class['Name']}" for character in all_characters]
                character_names.append('Exit')
                npc_description = all_characters[characters_menu_index].background.copy()
               
               
                conversation_with_npc(
                    character_names = character_names,
                    npc_name  = all_characters[characters_menu_index].profile['name']['full'],
                    npc_race  = all_characters[characters_menu_index].character_race["Name"],
                    npc_class = all_characters[characters_menu_index].character_class["Name"],
                    npc_description = npc_description,
                    # npc_salutations=,
                    # npc_follow_up_statements=
                )
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Profile':
                print_character(all_characters[characters_menu_index].profile)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Race Details':
                print_character(all_characters[characters_menu_index].character_race)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Class Details':
                print_character(all_characters[characters_menu_index].character_class)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Description':
                print_character(all_characters[characters_menu_index].description)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Background':
                print_character(all_characters[characters_menu_index].background)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Level Chart':
                print_character(all_characters[characters_menu_index].level_chart)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Attributes':
                print_character(all_characters[characters_menu_index].attributes)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Capabilities':
                print_character(all_characters[characters_menu_index].capabilities)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Skills':
                print_character(all_characters[characters_menu_index].skills)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Features':
                print_character(all_characters[characters_menu_index].features)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Money':
                print_character(all_characters[characters_menu_index].money)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Items':
                print_character(all_characters[characters_menu_index].items)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Armor':
                print_character(all_characters[characters_menu_index].armor)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Weapons':
                print_character(all_characters[characters_menu_index].weapons)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Combat':
                print_character(all_characters[characters_menu_index].combat)
                input("\nPress Enter to Continue...")
            if dnd_menu_character_class_section_selection[dnd_menu_character_class_section_selection_menu_index] == 'Spells':


                # if all_characters[characters_menu_index].character_class['Name'] in half_magic_classes:
                #     if all_characters[characters_menu_index].character_class['Name'] == "Paladin":
                #         pass
                #     if all_characters[characters_menu_index].character_class['Name'] == "Ranger":
                #         pass
                #     if all_characters[characters_menu_index].character_class['Name'] == "Warlock":
                #         pass

                # el
                if all_characters[characters_menu_index].character_class['Name'] in magic_classes or all_characters[characters_menu_index].character_class['Name'] in half_magic_classes:
                    spell_level_list = list(all_characters[characters_menu_index].spells['Spells Known']['Slots'])
                    spell_level_list.insert(0,'Details')
                    spell_level_list.append('Exit')

                    # These magic classes don't have Cantrips
                    if all_characters[characters_menu_index].character_class['Name'] == 'Paladin' or \
                       all_characters[characters_menu_index].character_class['Name'] == "Ranger":
                       spell_level_list.remove('Cantrips')
                       
                    while True:
                        clear()
                        def spell_menu_banner():
                            print(f"  ========================================================================================================================================================================================================")
                            print(f"  {spell_level_title:<35} {'SEL':<5} {'School':<20} {'Damage':<10} {'Saving Throw':<15} {'Range':<22} {'Duration':<32} {'Casting Time':<25} {'Components':<12}")
                            print(f"  ========================================================================================================================================================================================================")
                        spell_menu_banner
                        line_length=100

                        #example: Cantrips, 1st, 2nd...                        
                        spell_level_menu = TerminalMenu(spell_level_list, title="Select Level")
                        spell_level_index = spell_level_menu.show()
                        spell_level_selected = list(spell_level_list)[spell_level_index]

                        if spell_level_selected == 'Exit':
                            break
                        if spell_level_selected == 'Details':
                            print(f"""
Spellcasting Ability   : {text_wrap(dnd_classes[all_characters[characters_menu_index].character_class['Name']]["Spells"]["Spellcasting"],line_length=line_length,padding_value=22)}

Spellcasting Modifier  : {text_wrap(dnd_classes[all_characters[characters_menu_index].character_class['Name']]["Spells"]["Spellcasting Modifier"],line_length=line_length,padding_value=22)}

Spell Attack Modifier  : {text_wrap(dnd_classes[all_characters[characters_menu_index].character_class['Name']]["Spells"]["Spell Attack Modifier"],line_length=line_length,padding_value=22)}

Spell DC Save          : {text_wrap(dnd_classes[all_characters[characters_menu_index].character_class['Name']]["Spells"]["Spell DC Save"],line_length=line_length,padding_value=22)}

Preparation            : {text_wrap(dnd_classes[all_characters[characters_menu_index].character_class['Name']]["Spells"]["Preparation"],line_length=line_length,padding_value=22)}

Recovery               : {text_wrap(dnd_classes[all_characters[characters_menu_index].character_class['Name']]["Spells"]["Recovery"],line_length=line_length,padding_value=22)}

Spell Slots            : {text_wrap(dnd_classes[all_characters[characters_menu_index].character_class['Name']]["Spells"]["Spell Slots"],line_length=line_length,padding_value=22)}

Spells Known           : {text_wrap(dnd_classes[all_characters[characters_menu_index].character_class['Name']]["Spells"]["Spells Known"],line_length=line_length,padding_value=22)}

Change Up              : {text_wrap(dnd_classes[all_characters[characters_menu_index].character_class['Name']]["Spells"]["Change Up"],line_length=line_length,padding_value=22)}

Progression            : {text_wrap(dnd_classes[all_characters[characters_menu_index].character_class['Name']]["Spells"]["Progression"],line_length=line_length,padding_value=22)}

Requirements           : {text_wrap(dnd_classes[all_characters[characters_menu_index].character_class['Name']]["Spells"]["Requirements"],line_length=line_length,padding_value=22)}

Key Differences        : {text_wrap(dnd_classes[all_characters[characters_menu_index].character_class['Name']]["Spells"]["Key Difference"],line_length=line_length,padding_value=22)}

Uniqueness             : {text_wrap(dnd_classes[all_characters[characters_menu_index].character_class['Name']]["Spells"]["Uniqueness"],line_length=line_length,padding_value=22)}

Magic Lore             : {text_wrap(dnd_classes[all_characters[characters_menu_index].character_class['Name']]["Spells"]["Magic Lore"],line_length=line_length,padding_value=22)}

""")
                            input("\nPress Enter to Continue...")
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
                                spell_name_menu2 = TerminalMenu(spell_list_formatted)
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

                            # input("\nPress Enter to Continue...")
            # input("\nPress Enter to Continue...")



# List of items
def generate_item_list():
    # Lists of item properties
    names = ["Elixir of Health", "Scroll of Knowledge", "Ring of Fortune", "Amulet of Protection",
             "Wand of Wonder", "Cloak of Invisibility", "Boots of Speed", "Gloves of Thievery"]
    item_types = ["Potion", "Scroll", "Ring", "Amulet", "Wand", "Cloak", "Boots", "Gloves"]
    rarities = ["Common", "Uncommon", "Rare", "Very Rare", "Legendary"]
    weights = ["1 lb", "2 lb", "3 lb", "4 lb", "5 lb"]
    mundane_properties = ["Fragile", "Glowing", "Ancient", "Ornate", "Simple"]
    magical_types = [None, "Enchanted", "Cursed", "Blessed"]
    magical_properties = [
        None, "Glow in the dark", "Emit a faint musical tone", "Change color based on the holder's mood",
        "Levitate when not in use", "Speak a random phrase in an unknown language periodically"
    ]
    descriptions = [
        "An ancient-looking item with an aura of mystery",
        "A finely crafted item, glittering with a faint magical essence",
        "Appears mundane but has an inexplicable allure",
        "Radiates a warmth that is comforting to hold",
        "Covered in intricate patterns and symbols"
    ]

    # Rarity based cost calculation
    rarity_costs = {
        "Common": 100,
        "Uncommon": 500,
        "Rare": 5000,
        "Very Rare": 50000,
        "Legendary": 250000
    }

    # Rarity probabilities
    probabilities = [0.50, 0.25, 0.15, 0.08, 0.02]

    # Select rarity based on probability
    rarity = np.random.choice(rarities, p=probabilities)
    cost = rarity_costs[rarity]

    # Select random properties for the item
    name = random.choice(names)
    owner = random.choice(["Human Fighter", "Elf Ranger", "Halfling Rouge", "Tiefling Warlock", "Tabaxi Druid"])
    item_type = random.choice(item_types)
    amount = random.randint(1, 3)  # Random amount between 1 and 3
    weight = random.choice(weights)
    mundane_property = random.choice(mundane_properties)
    magical = random.choice([False, True])
    magical_type = None if not magical else random.choice(magical_types)
    magical_property = None if not magical else random.choice(magical_properties)
    description = random.choice(descriptions)
    notes = None

    return {
        "name": name,
        "owner": owner,
        "type": item_type,
        "amount": amount,
        "rarity": rarity,
        "material_components": "Various",
        "cost": f"{cost} gp",
        "weight": weight,
        "mundane_properties": [mundane_property],
        "is_magical": magical,
        "magical_type": magical_type,
        "magical_properties": [magical_property] if magical_property else [],
        "description": description,
        "notes": notes
    }


# List of weapons
def generate_weapon_list():
    # Lists of weapon properties
    names = [
        "Flame Tongue Sword", "Frost Brand Axe", "Thunder Maul", "Vorpal Scimitar",
        "Shadow Dagger", "Arcane Longbow", "Celestial Warhammer", "Dragonbone Staff",
        "Spectral Trident", "Windblade Rapier"
    ]
    damage_amounts = ["1d6", "1d8", "1d10", "2d6", "2d4"]
    damage_types = ["Slashing", "Piercing", "Bludgeoning", "Fire", "Cold", "Lightning", "Necrotic", "Radiant"]
    weapon_types = ["Simple", "Martial", "Exotic"]
    attack_types = ["Melee", "Ranged"]
    attack_bonus = ["+0", "+1", "+2", "+3"]
    mundane_properties = ["Sturdy", "Elegant", "Heavy", "Light", "Balanced"]
    magical_types = [None, "Enchanted", "Cursed", "Blessed"]
    magical_properties = [
        None, "Illuminates area", "Deals extra elemental damage", "Grants wielder advantage on certain checks"
    ]
    descriptions = [
        "An ancient weapon with mysterious powers", "A beautifully crafted weapon with a unique design",
        "Emits a faint, otherworldly glow", "Feels surprisingly light and well-balanced",
        "Covered in strange runes and symbols"
    ]

    # Rarity based cost calculation
    rarity_costs = {
        "Common": 100,
        "Uncommon": 500,
        "Rare": 5000,
        "Very Rare": 50000,
        "Legendary": 250000
    }

    # Rarity probabilities
    rarities = ["Common", "Uncommon", "Rare", "Very Rare", "Legendary"]
    probabilities = [0.50, 0.25, 0.15, 0.08, 0.02]

    # Select random properties for the weapon
    name = random.choice(names)
    damage_amount = random.choice(damage_amounts)
    damage_type = random.choice(damage_types)
    weapon_type = random.choice(weapon_types)
    attack_type = random.choice(attack_types)
    attack_bon = random.choice(attack_bonus)
    ranged = random.choice([False, True])
    range_low = None if not ranged else "30 ft"
    range_high = None if not ranged else "120 ft"
    owner = random.choice(["Human Fighter", "Elf Ranger", "Halfling Rouge", "Tiefling Warlock", "Tabaxi Druid"])
    amount = random.randint(1, 3)  # Random amount between 1 and 3
    rarity = np.random.choice(rarities, p=probabilities)
    cost = rarity_costs[rarity]
    weight = random.choice(["5 lb", "7 lb", "10 lb", "12 lb", "15 lb"])
    mundane_property = random.choice(mundane_properties)
    magical = random.choice([False, True])
    magical_type = None if not magical else random.choice(magical_types)
    magical_property = None if not magical else random.choice(magical_properties)
    description = random.choice(descriptions)
    notes = None

    return {
        "name": name,
        "damage_amount": damage_amount,
        "damage_type": damage_type,
        "weapon_type": weapon_type,
        "attack_type": attack_type,
        "attack_bonus": attack_bon,
        "is_ranged": ranged,
        "range_low": range_low,
        "range_high": range_high,
        "owner": owner,
        "amount": amount,
        "rarity": rarity,
        "material_components": "Various",
        "cost": f"{cost} gp",
        "weight": weight,
        "mundane_properties": [mundane_property],
        "is_magical": magical,
        "magical_type": magical_type,
        "magical_properties": [magical_property] if magical_property else [],
        "description": description,
        "notes": notes
    }



def generate_random_item(item_list):
    random_item = random.choice(item_list)
    return random_item


def generate_random_weapon(weapon_list):
    random_weapon = random.choice(weapon_list)
    return random_weapon


def generate_attribute_number():
    attribute_roles = []
    for atr_role in range(0,7):
        roles = []
        for role in range(0,4):
            roles.append(random.randint(1,6))
        roles.remove(min(roles))
        role_sum = sum(roles)
        attribute_roles.append(role_sum)
        
    attribute_roles.remove(min(attribute_roles))
    return attribute_roles


def choose_random_proficiency_skill(dnd_classes,character_class):
    # Chooses a random number of skills from the class proficiency list
    randomly_chosen_proficiency_skills = []
    class_proficiency_choices = list(dnd_classes[character_class]["Proficiencies"]["Skills"]["Choose From"])
    for i in range(0, int(dnd_classes[character_class]["Proficiencies"]["Skills"]["Choose Number"])):
        randomly_chosen_skill = random.choice(class_proficiency_choices)
        if randomly_chosen_skill not in randomly_chosen_proficiency_skills:
            randomly_chosen_proficiency_skills.append(randomly_chosen_skill)
            class_proficiency_choices.remove(randomly_chosen_skill)
    return randomly_chosen_proficiency_skills

