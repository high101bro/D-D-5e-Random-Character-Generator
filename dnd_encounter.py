#! /usr/bin/env python3

from simple_term_menu import TerminalMenu
import pickle_handler
from menu import *


# # Option to load previous save files
# all_characters = pickle_handler.select_and_load_pkl()
# if all_characters is not None:
#     print("Characters loaded")
# else:
#     print("No Characters loaded")
#     all_characters = []
# print()

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
    char_in_battle.attacks    = []


    return char_in_battle


encounter_menu_options = [
    "Automated",
    "Guided"
]
encounter_menu_selected = TerminalMenu(encounter_menu_options)
encounter_menu_selected_index = encounter_menu_selected.show()

# Characters entering the battlefield
if encounter_menu_options[encounter_menu_selected_index] == 'Automated':
    clear()
    print(f"Make Inititative Rolls:")
    for index, character in enumerate(all_characters):
        characters_in_battle.append(character_enters_the_battle(character))

    battle_in_initiative_order = sorted(characters_in_battle, key=lambda char: char.initiative, reverse=True)

    clear()
    print()
    print(f"Turn Order [Initiative]:")
    for index, character in enumerate(battle_in_initiative_order):
        display_name = f"{character.name} the {character.char_race} {character.char_class}"
        print(f"  Turn {index + 1} [{character.initiative:>2}] {display_name:<50}  HP: {character.hp_current}/{character.hp_total}")



    battle_tasks = [
        'Attack an Opponent',
        'Add an Opponent',
        'Change Turn Order',
        'Remove from Battle',
    ]

    while True:
        print(f"\nBattle Actions:")
        battle_task_menu = TerminalMenu(battle_tasks)
        battle_task_menu_index = battle_task_menu.show()
        battle_task_menu_selected = battle_tasks[battle_task_menu_index]


        print(battle_task_menu_selected)
        ##################################
        ##################################
        ##################################
        ##################################
        ##################################
        ##################################
        ##################################
        if battle_task_menu_selected == 'Add an Opponent':
            monster_menu_list = []
            from dnd_monsters import *
            for monster in dnd_monsters.items():
                monster_menu_list.append(f"{monster['Name']:<20} {monster['Challenge Ratting']:<5} {monster['Description']}")


            pass
        elif battle_task_menu_selected == 'Change Turn Order':
            def move_character_down(objects, display_attr='name'):
                menu_options = [getattr(obj, display_attr, "Unknown") for obj in objects]
                menu = TerminalMenu(menu_options, title="\nSelect an item to move down:")

                selected_index = menu.show()

                if selected_index is not None and selected_index < len(objects) - 1:
                    objects[selected_index], objects[selected_index + 1] = objects[selected_index + 1], objects[selected_index]

            while True:
                print("\nCurrent character order:")
                for index, character in enumerate(battle_in_initiative_order):
                    print(f"#{index} [{character.initiative:<2}]  {character.name} the {character.char_race} {character.char_class}")

                move_character_down(battle_in_initiative_order)

                if input("\nSwap another character? (y/n): ").lower() != 'y':
                    break

            print("\nFinal character order:")
            for index, character in enumerate(battle_in_initiative_order):
                print(f"  Turn {index + 1} [{character.initiative:>2}]  {character.name} the {character.char_race} {character.char_class}")

            input("\nPress Enter to Continue...")        


        ##################################
        ################################## GO UP
        ##################################
        ##################################

        elif battle_task_menu_selected == 'Attack an Opponent':

            print(battle_task_menu_selected)

            input("\nPress Enter to Continue...")        


        elif battle_task_menu_selected == 'Remove from Battle':
            print('ddddddddddddddddd')
            print(battle_task_menu_selected)

            input("\nPress Enter to Continue...")   


        else:
            print('eeeeeeeeeeeeeeeeeeeee')


elif encounter_menu_options[encounter_menu_selected_index] == 'Guided':
    pass









# print(
#     xp_thresholds[1]
# )



