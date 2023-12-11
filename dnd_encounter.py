#! /usr/bin/env python3

from simple_term_menu import TerminalMenu
import pickle_handler
from dnd_monsters import *
from dnd_helper import *
# from menu import *
import random, os, re

# Option to load previous save files
all_characters = pickle_handler.select_and_load_pkl()
if all_characters is not None:
    print("Characters loaded")
else:
    print("No Characters loaded")
    all_characters = []
print()

xp_thresholds = {
    # xp thresholds by character level
    # indice 0 = easy, 1 = medium, 2 = hard, 3 = deadly
    1: [25, 50, 75, 100], 
    2: [50, 100, 150, 200], 
    3: [75, 150, 225, 400],
    4: [125, 250, 375, 500], 
    5: [250, 500, 750, 1100], 
    6: [300, 600, 900, 1400],
    7: [350, 750, 1100, 1700], 
    8: [450, 900, 1400, 2100], 
    9: [550, 1100, 1600, 2400],
    10: [600, 1200, 1900, 2800], 
    11: [800, 1600, 2400, 3600], 
    12: [1000, 2000, 3000, 4500],
    13: [1100, 2200, 3400, 5100], 
    14: [1250, 2500, 3800, 5700], 
    15: [1400, 2800, 4300, 6400],
    16: [1600, 3200, 4800, 7200], 
    17: [2000, 3900, 5900, 8800], 
    18: [2100, 4200, 6300, 9500],
    19: [2400, 4900, 7300, 10900], 
    20: [2800, 5700, 8500, 12700]
}

encounter_multipliers = {
    1 : 1,
    2 : 1.5,
    3 : 2,
    4 : 2,
    5 : 2,
    6 : 2,
    7 : 2.5,
    8 : 2.5,
    9 : 2.5,
    10 : 2.5,
    11 : 3,
    12 : 3,
    13 : 3,
    14 : 3,
    15 : 4,
    # 15 or higher is x4
}

encounter_difficulty = ['easy','medium','hard','deadly']

characters_in_battle = []

# number_of_characters = int(input(f"How many characters? "))

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


def character_enters_the_battle(character):
    char_in_battle            = Character_in_battle()
    char_in_battle.name       = f"{character.profile['name']['first']} {character.profile['name']['last']}"
    # char_in_battle.cr         = character.profile['level']
    char_in_battle.level      = character.profile['level']
    char_in_battle.pb         = character.profile['proficiency bonus']
    char_in_battle.char_race  = character.description['race']
    char_in_battle.char_class = character.description['class']
    char_in_battle.type       = 'Humanoid'
    char_in_battle.size       = character.character_race['Traits']['Size']
    char_in_battle.ac         = 17 #dan, update me
    char_in_battle.hp_total   = character.capabilities['combat']['hit_points']['total']
    char_in_battle.hp_current = character.capabilities['combat']['hit_points']['current']
    char_in_battle.speed      = character.capabilities['physical']['speed']
    while True:
        try:
            user_roll = int(input(f"  {char_in_battle.name} the {char_in_battle.char_race} {char_in_battle.char_class}: "))
            initiative_calc = int(character.capabilities['attributes']['dexterity']['modifier']) + user_roll
            break
        except:
            print(f"Error, please input a number")
    char_in_battle.initiative = initiative_calc
    char_in_battle.str        = int(character.capabilities['attributes']['strength']['modifier'])
    char_in_battle.dex        = int(character.capabilities['attributes']['constitution']['modifier'])
    char_in_battle.con        = int(character.capabilities['attributes']['dexterity']['modifier'])
    char_in_battle.int        = int(character.capabilities['attributes']['intelligence']['modifier'])
    char_in_battle.wis        = int(character.capabilities['attributes']['wisdom']['modifier'])
    char_in_battle.cha        = int(character.capabilities['attributes']['charisma']['modifier'])
    char_in_battle.attacks    = character.weapons
    char_in_battle.effects     = []

    return char_in_battle

def monster_enters_the_battle(monster):
    mon_in_battle            = Character_in_battle()
    mon_in_battle.name       = f"[{monster['Name']}] {random.choice(monster['5 Common First Names'])} {random.choice(monster['5 Common Last Names'])}"
    mon_in_battle.cr         = monster["Challenge Rating"]
    mon_in_battle.level      = 0
    mon_in_battle.pb         = 0
    mon_in_battle.char_race  = monster["Race"]
    mon_in_battle.char_class = monster["Class"]
    mon_in_battle.type       = monster["Type"]
    mon_in_battle.size       = monster['Size']
    mon_in_battle.ac         = monster["Armor Class"].split()[0]

    # Calculate dynamic hp base of ex: "350 (20d20 + 140)"
    match = re.search(r'(\d+) \((\d+)d(\d+) \+ (\d+)\)', monster["Hit Points"])
    if match:
        remove    = int(match.group(1))
        die_num   = int(match.group(2))
        die_sides = int(match.group(3))
        base_con  = int(match.group(4))
        roll_total = 0
        for roll in range(0,die_num):
            roll_total += random.randint(1,die_sides)
        total_hp  = roll_total + base_con
    else:
        # if above calucation fails, like from formatting, just grab the average hp
        total_hp = monster["Hit Points"].split()[0]

    mon_in_battle.hp_total   = total_hp
    mon_in_battle.hp_current = mon_in_battle.hp_total # placeholder
    mon_in_battle.speed      = monster["Speed"]
    mon_in_battle.str        = int(monster["STR"].split()[1].replace('(','').replace(')',''))
    mon_in_battle.dex        = int(monster["DEX"].split()[1].replace('(','').replace(')',''))
    mon_in_battle.con        = int(monster["CON"].split()[1].replace('(','').replace(')',''))
    mon_in_battle.int        = int(monster["INT"].split()[1].replace('(','').replace(')',''))
    mon_in_battle.wis        = int(monster["WIS"].split()[1].replace('(','').replace(')',''))
    mon_in_battle.cha        = int(monster["CHA"].split()[1].replace('(','').replace(')',''))
    mon_in_battle.initiative = random.randint(1,20) + mon_in_battle.dex
    mon_in_battle.attacks    = monster["Actions"]
    mon_in_battle.effects    = []

    return mon_in_battle

encounter_menu_options = [
    "Automated",
    "Guided"
]
encounter_menu_selected = TerminalMenu(encounter_menu_options)
encounter_menu_selected_index = encounter_menu_selected.show()

battle_in_initiative_order = []

def print_turn_banner():
    print(f"  ======================================================================================================================================================")
    print(f"  {'Turn':<3}   {'Init':>4}   {'Character':<65}  {'Hit Points':>7}    {'Effects':<8}")
    print(f"  ======================================================================================================================================================")

def print_turn_order():
    for index, character in enumerate(battle_in_initiative_order):
        display_name = f"{character.name} the {character.char_race} {character.char_class}"
        if len(character.effects) == 0:
            print(f"  {index + 1:>4}   [{character.initiative:>2}]   {display_name:<65}  {character.hp_current:>4} /{character.hp_total:>4}    {'None':<8}")
        else:
            print(f"  {index + 1:>4}   [{character.initiative:>2}]   {display_name:<65}  {character.hp_current:>4} /{character.hp_total:>4}    {character.effects:<8}")


# Characters entering the battlefield
if encounter_menu_options[encounter_menu_selected_index] == 'Automated':
    if len(all_characters) == 0:
        print(f"There are not character available to enter battle.")
    else:
        directory_path = "./save_states/battles"
        file_extension = ".pkl"

        files_in_directory = os.listdir(directory_path)

        # Check if any file in the directory has the specified file extension
        pickle_files = [file for file in files_in_directory if file.endswith(file_extension)]

        if pickle_files:
            clear()
            for pickle_file in pickle_files:
                print(f"Previous save stated detected: {pickle_file}")
            load_pickle = ['Load previous battle','Start new battle']
            load_pickle_menu = TerminalMenu(load_pickle, title="\nDo you want to load it?")
            load_pickle_menu_index = load_pickle_menu.show()
            load_pickle_menu_selected = load_pickle[load_pickle_menu_index]
            if load_pickle_menu_selected == 'Load previous battle':
                battle_in_initiative_order = pickle_handler.load_pkl_file(pickle_file, directory_path)
            elif load_pickle_menu_selected == 'Start new battle':
                clear()
                print("No pickle files found in the directory.")
                print(f"\nMake Inititative Rolls:")
                for index, character in enumerate(all_characters):
                    characters_in_battle.append(character_enters_the_battle(character))
                battle_in_initiative_order = sorted(characters_in_battle, key=lambda char: char.initiative, reverse=True)
                pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")
        else:
            clear()
            print("No pickle files found in the directory.")
            print(f"\nMake Inititative Rolls:")
            for index, character in enumerate(all_characters):
                characters_in_battle.append(character_enters_the_battle(character))
            battle_in_initiative_order = sorted(characters_in_battle, key=lambda char: char.initiative, reverse=True)
            pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")

    battle_tasks = [
        'Attack an Opponent',
        'Add an Opponent',
        'Change Turn Order',
        'Remove from Battle',
        'Character Management',
        'Exit'
    ]

    while True:
        clear()
        print('Turn Order:')
        print_turn_banner()
        print_turn_order()

        print(f"\nBattle Actions:")
        battle_task_menu = TerminalMenu(battle_tasks)
        battle_task_menu_index = battle_task_menu.show()
        battle_task_menu_selected = battle_tasks[battle_task_menu_index]

        print(battle_task_menu_selected)

        if battle_task_menu_selected == 'Add an Opponent':
            clear()
            print(battle_task_menu_selected)
            print_turn_banner()
            print_turn_order()

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
                print(f"\nType 'Exit' to exit search.")
                user_input = input("\nSearch for a monster to add to the battle: [Supports Tab Completion] ")
                user_input = user_input.lower()  # Convert user input to lowercase
                
                if user_input.lower() == 'exit':
                    break
                else:
                    # Check if the entered item (in lowercase) is in the inventory
                    lowercase_keys = [key.lower() for key in dnd_monsters.keys()]
                    if user_input in lowercase_keys:
                        # Find the original key with matching lowercase version
                        matching_key = list(dnd_monsters.keys())[lowercase_keys.index(user_input)]
                        # print(f"[+] You have {dnd_monsters[matching_key]} {matching_key}(s) in your inventory.")
                        print_character(dnd_monsters[matching_key])

                        options=['Yes','No']
                        menu = TerminalMenu(options,title='Do you want to add this to the battle?')
                        index = menu.show()
                        selected = options[index]

                        if selected == 'Yes':
                            battle_in_initiative_order.append(monster_enters_the_battle(dnd_monsters[matching_key]))
                            pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")

                        elif selected == 'No':
                            break

                        break
                    else:
                        print(f"[-] {user_input} is not in your inventory. Please enter a valid item.")


        elif battle_task_menu_selected == 'Character Management':
            inspect_character(all_characters)

        elif battle_task_menu_selected == 'Exit':
            break

        elif battle_task_menu_selected == 'Change Turn Order':
            change_turn_order_list = ['Sort by Initiative','Move Selected Up','Move Selected Down','Exit']
            change_turn_order_menu = TerminalMenu(change_turn_order_list)
            change_turn_order_index = change_turn_order_menu.show()
            change_turn_order_selected = change_turn_order_list[change_turn_order_index]

            if change_turn_order_selected == 'Sort by Initiative':
                battle_in_initiative_order = sorted(battle_in_initiative_order, key=lambda char: char.initiative, reverse=True)
                pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")

            elif change_turn_order_selected == 'Move Selected Up' or change_turn_order_selected == 'Move Selected Down':
                while True:
                    clear()
                    print("Change Turn Order - Select Charater To Move:")
                    print_turn_banner()


                    character_remove_list = []
                    for index, character in enumerate(battle_in_initiative_order):
                        display_name = f"{character.name} the {character.char_race} {character.char_class}"
                        character_remove_list.append(f"Turn {index + 1:<3} [{character.initiative:>2}]   {display_name:<56}  HP: {character.hp_current:>3}/{character.hp_total:>3} {'Effects:':>11} {character.effects}")

                    character_remove_list.append('Exit')

                    characters_menu = TerminalMenu(character_remove_list)
                    characters_menu_index = characters_menu.show()
                    
                    if character_remove_list[characters_menu_index] == 'Exit':
                        character_remove_list.pop()
                        break
                    else:
                        character_remove_list.pop()

                        if change_turn_order_selected == 'Move Selected Up':
                            if characters_menu_index is not None and characters_menu_index > 0:
                                battle_in_initiative_order[characters_menu_index], battle_in_initiative_order[characters_menu_index - 1] = battle_in_initiative_order[characters_menu_index - 1], battle_in_initiative_order[characters_menu_index]
                        elif change_turn_order_selected == 'Move Selected Down':
                            if characters_menu_index is not None and characters_menu_index < len(battle_in_initiative_order) - 1:
                                battle_in_initiative_order[characters_menu_index], battle_in_initiative_order[characters_menu_index + 1] = battle_in_initiative_order[characters_menu_index + 1], battle_in_initiative_order[characters_menu_index]
                        pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")
            elif change_turn_order_selected == 'Exit':
                break

        elif battle_task_menu_selected == 'Attack an Opponent':

            print(battle_task_menu_selected)

            input("\nPress Enter to Continue...")


        elif battle_task_menu_selected == 'Remove from Battle':
            while True:
                clear()
                print("Remove a Character from Battle.")
                print_turn_banner()
                
                character_remove_list = []
                for index, character in enumerate(battle_in_initiative_order):
                    display_name = f"{character.name} the {character.char_race} {character.char_class}"
                    character_remove_list.append(f"Turn {index + 1:<3} [{character.initiative:>2}]   {display_name:<56}  HP: {character.hp_current:>3}/{character.hp_total:>3} {'Effects:':>11} {character.effects}")

                character_remove_list.append('Exit')

                characters_menu = TerminalMenu(character_remove_list)
                characters_menu_index = characters_menu.show()
                
                if character_remove_list[characters_menu_index] == 'Exit':
                    character_remove_list.pop()
                    break
                else:
                    character_remove_list.pop()
                    character_remove_confirm = input(f"Are you sure you want to remove the following?\n\n  {character_remove_list[characters_menu_index]}\n\nEnter 'd' to confirm deletion: ")
                    if character_remove_confirm.lower() == 'd':
                        del character_remove_list[characters_menu_index]
                        del battle_in_initiative_order[characters_menu_index]
                        pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")

                    else:
                        pass  
                break


        else:
            print('eeeeeeeeeeeeeeeeeeeee')


elif encounter_menu_options[encounter_menu_selected_index] == 'Guided':
    pass









# print(
#     xp_thresholds[1]
# )



