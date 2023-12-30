#! /usr/bin/env python3

from simple_term_menu import TerminalMenu
import pickle_handler
from dnd_monsters import *
from dnd_helper import *
from dnd_generate_character import *
# from menu import *
import random, os, re
from dnd_lists import *
import battlefield



class Character_in_battle():
    def __init__(self):
        self.name = ''
        self.display_name = ''
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
        self.skills = {}
        self.attacks = {}
        self.attack_number = 1
    def to_dict(self):
        return {
            'name' : self.name,
            'display_name' : self.display_name,
            'cr' : self.cr,
            'char_race' : self.char_race,
            'char_class' : self.char_class,
            'type' : self.type,
            'ac' : self.ac,
            'hp' : self.hp,
            'speed' : self.speed,
            'initiative' : self.initiative,
            'str' : self.str,
            'dex' : self.dex,
            'con' : self.con,
            'int' : self.int,
            'wis' : self.wis,
            'cha' : self.cha,
            'skills' : self.skills,
            'attacks' : self.attacks,
            'attack_number' : self.attack_number,
        }


def main(all_characters):


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

    def character_enters_the_battle(character):
        char_in_battle              = Character_in_battle()
        char_in_battle.name         = f"{character.profile['name']['first']} {character.profile['name']['last']}"
        char_in_battle.display_name = f"{character.profile['name']['first']} {character.profile['name']['last']}"
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
        char_in_battle.str        = int(character.attributes['strength']['modifier'])
        char_in_battle.dex        = int(character.attributes['constitution']['modifier'])
        char_in_battle.con        = int(character.attributes['dexterity']['modifier'])
        char_in_battle.int        = int(character.attributes['intelligence']['modifier'])
        char_in_battle.wis        = int(character.attributes['wisdom']['modifier'])
        char_in_battle.cha        = int(character.attributes['charisma']['modifier'])
        while True:
            user_roll = input(f"  Roll for {char_in_battle.display_name} the {char_in_battle.char_race} {char_in_battle.char_class}: ")
            if user_roll == None or user_roll == "":
                initiative_calc = dnd_roll_dice(dice_number=1,dice_sides=20,roll_modifier=char_in_battle.dex)
                break
            else:
                try:
                    user_roll = int(user_roll)
                    initiative_calc = int(character.attributes['dexterity']['modifier']) + user_roll
                    break
                except:
                    print(f"Error, please input a number")
        char_in_battle.initiative = initiative_calc
        char_in_battle.attacks    = character.weapons
        char_in_battle.skills     = character.skills
        char_in_battle.effects    = []
        char_in_battle.friendly   = True

        return char_in_battle

    def monster_enters_the_battle(monster):
        mon_in_battle              = Character_in_battle()
        mon_in_battle.name         = monster['Name']
        mon_in_battle.display_name = f"[{monster['Name']}] {random.choice(monster['5 Common First Names'])} {random.choice(monster['5 Common Last Names'])}"
        mon_in_battle.cr           = monster["Challenge Rating"]
        mon_in_battle.level        = 0
        mon_in_battle.pb           = 0
        mon_in_battle.char_race    = monster["Race"]
        mon_in_battle.char_class   = monster["Class"]
        mon_in_battle.type         = monster["Type"]
        mon_in_battle.size         = monster['Size']
        mon_in_battle.ac           = monster["Armor Class"].split()[0]

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
        mon_in_battle.skills    = {
            'acrobatics' : {
                'Related Attribute' : 'dexterity',
                'proficiency' : False,
                'total' : mon_in_battle.dex,
                'description' : "Performing physical feats, maintaining balance, and tumbling."
            },
            'animal handling' : {
                'Related Attribute' : 'wisdom',
                'proficiency' : False,
                'total' : mon_in_battle.wis,
                'description' : "Calming, controlling, or understanding the intentions of animals."
            },
            'arcana' : {
                'Related Attribute' : 'intelligence',
                'proficiency' : False,
                'total' : mon_in_battle.int,
                'description' : "Knowledge of magic, magical creatures, mystical lore, and magical traditions."
            },
            'athletics' : {
                'Related Attribute' : 'strength',
                'proficiency' : False,
                'total' : mon_in_battle.str,
                'description' : "Performing physical activities like climbing, jumping, and swimming."
            },
            'deception' : {
                'Related Attribute' : 'charisma',
                'proficiency' : False,
                'total' : mon_in_battle.cha,
                'description' : "Your ability to convincingly hide the truth, either verbally or through actions."
            },
            'history' : {
                'Related Attribute' : 'intelligence',
                'proficiency' : False,
                'total' : mon_in_battle.int,
                'description' : "Recalling information about historical events, legendary people, ancient kingdoms, and recent wars."
            },
            'insight' : {
                'Related Attribute' : 'wisdom',
                'proficiency' : False,
                'total' : mon_in_battle.wis,
                'description' : "Determining the true intentions of a creature, such as when searching out a lie or predicting someone’s next move."
            },
            'intimidation' : {
                'Related Attribute' : 'charisma',
                'proficiency' : False,
                'total' : mon_in_battle.cha,
                'description' : "Influencing someone through overt threats, hostile actions, and physical intimidation."
            },
            'investigation' : {
                'Related Attribute' : 'intelligence',
                'proficiency' : False,
                'total' : mon_in_battle.int,
                'description' : "Looking for clues and making deductions based on those clues."
            },
            'medicine' : {
                'Related Attribute' : 'wisdom',
                'proficiency' : False,
                'total' : mon_in_battle.wis,
                'description' : "Ability to diagnose and treat injuries and diseases."
            },
            'nature' : {
                'Related Attribute' : 'intelligence',
                'proficiency' : False,
                'total' : mon_in_battle.int,
                'description' : "Knowledge about terrain, plants and animals, the weather, and natural cycles."
            },
            'perception' : {
                'Related Attribute' : 'wisdom',
                'proficiency' : True,
                'total' : mon_in_battle.wis,
                'description' : "Noticing or sensing things, typically based on Wisdom. It’s the skill you’d use to hear a conversation through a door, spot something hidden under a rock, or notice someone sneaking up on you."
            },
            'performance' : {
                'Related Attribute' : 'charisma',
                'proficiency' : False,
                'total' : mon_in_battle.cha,
                'description' : "Delighting an audience with music, dance, acting, storytelling, or some other form of entertainment."
            },
            'persuasion' : {
                'Related Attribute' : 'charisma',
                'proficiency' : False,
                'total' : mon_in_battle.cha,
                'description' : "Influencing someone with tact, social graces, or good nature."
            },
            'religion' : {
                'Related Attribute' : 'intelligence',
                'proficiency' : False,
                'total' : mon_in_battle.int,
                'description' : "Knowledge about deities, rites and prayers, religious hierarchies, holy symbols, and the practices of secret cults."
            },
            'sleight of hand' : {
                'Related Attribute' : 'dexterity',
                'proficiency' : False,
                'total' : mon_in_battle.dex,
                'description' : "Executing tricks of dexterity or misdirection, like picking pockets or conjuring objects."
            },
            'stealth' : {
                'Related Attribute' : 'dexterity',
                'proficiency' : False,
                'total' : mon_in_battle.dex,
                'description' : "Concealing yourself from enemies, slinking past guards, slipping away without being noticed."
            },
            'survival' : {
                'Related Attribute' : 'wisdom',
                'proficiency' : False,
                'total' : mon_in_battle.wis,
                'description' : "Following tracks, hunting wild game, guiding your group through frozen wastelands, identifying signs that owlbears live nearby, predicting the weather, or avoiding quicksand and other natural hazards."
            }


        }
        mon_in_battle.effects    = []
        mon_in_battle.friendly   = False

        return mon_in_battle



    battle_in_initiative_order = []
    monsters_on_the_battlefield = []
    temporary_battle_characters = []
    original_battle_characters = []

    def print_turn_banner():
        print(f"  ======================================================================================================================================================")
        print(f"  {'Turn':<3}   {'Init':>4}   {'Character':<65}  {'Hit Points':>7}    {'Effects':<8}")
        print(f"  ======================================================================================================================================================")


    def get_hp_color(current, total):
        hp_percentage = (int(current) / int(total)) * 100

        if hp_percentage > 75:
            return "\033[92m"  # Green
        elif hp_percentage > 50:
            return "\033[93m"  # Yellow
        elif hp_percentage > 25:
            return "\033[91m"  # Orange
        else:
            return "\033[91m"  # Red


    def print_turn_order():
        for index, character in enumerate(battle_in_initiative_order):
            display_name = f"{character.display_name} the {character.char_race} {character.char_class}"

            current_hp = character.hp_current
            total_hp = character.hp_total
            hp_color = get_hp_color(current_hp, total_hp)

            if character.friendly == True:
                if len(character.effects) == 0:
                    print(f"  {index + 1:>4}   [{character.initiative:>2}]   \033[92m{display_name:<65}\033[0m  {hp_color}{character.hp_current:>4} /{character.hp_total:>4}\033[0m    {'None':<8}")
                else:
                    print(f"  {index + 1:>4}   [{character.initiative:>2}]   \033[92m{display_name:<65}\033[0m  {hp_color}{character.hp_current:>4} /{character.hp_total:>4}\033[0m    {', '.join(character.effects):<8}")
            elif character.friendly == False:
                if len(character.effects) == 0:
                    print(f"  {index + 1:>4}   [{character.initiative:>2}]   \033[91m{display_name:<65}\033[0m  {hp_color}{character.hp_current:>4} /{character.hp_total:>4}\033[0m    {'None':<8}")
                else:
                    print(f"  {index + 1:>4}   [{character.initiative:>2}]   \033[91m{display_name:<65}\033[0m  {hp_color}{character.hp_current:>4} /{character.hp_total:>4}\033[0m    {', '.join(character.effects):<8}")



    def select_character_menu(character_list,from_battle=False):
        for index, character in enumerate(battle_in_initiative_order):
            display_name = f"{character.display_name} the {character.char_race} {character.char_class}"
            if from_battle == False:
                if len(character.effects) == 0:
                    character_list.append(f"{index + 1:>4}   [{character.initiative:>2}]   {display_name:<65} {character.hp_current:>4} /{character.hp_total:>4}    {'None':<8}")
                else:
                    character_list.append(f"{index + 1:>4}   [{character.initiative:>2}]   {display_name:<65} {character.hp_current:>4} /{character.hp_total:>4}    {', '.join(character.effects):<8}")
            # The purpose of the below is to show just those characters who are not already a member of the party, so we can add them if desired
            elif from_battle == True:
                is_name_present = any(char.profile['name']['full'] in display_name for char in all_characters)
                if not is_name_present:
                    if len(character.effects) == 0:
                        character_list.append(f"{index + 1:>4}   [{character.initiative:>2}]   {display_name:<65} {character.hp_current:>4} /{character.hp_total:>4}    {'None':<8}")
                    else:
                        character_list.append(f"{index + 1:>4}   [{character.initiative:>2}]   {display_name:<65} {character.hp_current:>4} /{character.hp_total:>4}    {', '.join(character.effects):<8}")


        character_list.append('Exit')

        characters_menu = TerminalMenu(
            character_list,
            multi_select=False,
            show_multi_select_hint=False,
            accept_keys=("enter", "alt-d", "ctrl-i"),
            title=None,
            # preview_command='',
        )
        character_menu_index = characters_menu.show()
        return character_list[character_menu_index], character_menu_index, character_menu_index



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
            load_pickle = ['Load previous battle','Start new battle']
            print("\n\033[91mDo you want to load it?\033[0m\n")
            load_pickle_menu = TerminalMenu(load_pickle)
            load_pickle_menu_index = load_pickle_menu.show()
            load_pickle_menu_selected = load_pickle[load_pickle_menu_index]
            if load_pickle_menu_selected == 'Load previous battle':
                for pickle_file in pickle_files:
                    # print(f"Previous save stated detected: {pickle_file}")
                    if pickle_file == "battle.pkl":
                        battle_in_initiative_order = pickle_handler.load_pkl_file(pickle_file, directory_path)
                    if pickle_file == "temporary_battle_characters.pkl":
                        temporary_battle_characters = pickle_handler.load_pkl_file(pickle_file, directory_path)
                    if pickle_file == "monsters_on_the_battlefield.pkl":
                        monsters_on_the_battlefield = pickle_handler.load_pkl_file(pickle_file, directory_path)
                    if pickle_file == "original_battle_characters.pkl":
                        original_battle_characters = pickle_handler.load_pkl_file(pickle_file, directory_path)
                        

            elif load_pickle_menu_selected == 'Start new battle':
                clear()
                print(f"\n\033[91mMake Inititative Rolls:\033[0m\n")
                print(f"Leave blank and press [Enter] for auto-roll, or enter a value manually.")
                print()
                for index, character in enumerate(all_characters):
                    char_to_add = character_enters_the_battle(character)
                    characters_in_battle.append(char_to_add)
                    original_battle_characters.append(char_to_add)

                pickle_handler.save_dnd_state('original_battle_characters', original_battle_characters, "./save_states/battles")


                battle_in_initiative_order = sorted(characters_in_battle, key=lambda char: char.initiative, reverse=True)
                pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")
        else:
            clear()
            print("No pickle files found in the directory.")
            print(f"\nMake Inititative Rolls:")
            for index, character in enumerate(all_characters):
                char_to_add = character_enters_the_battle(character)
                characters_in_battle.append(char_to_add)
                original_battle_characters.append(char_to_add)

            pickle_handler.save_dnd_state('original_battle_characters', original_battle_characters, "./save_states/battles")

            battle_in_initiative_order = sorted(characters_in_battle, key=lambda char: char.initiative, reverse=True)
            pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")

    battle_tasks = [
        'Inspect Character',
        'Attack a Character',
        'Fumble Generator',
        'Heal a Character',
        'Resurrect a Character',
        'Apply an Effect to a Character',
        'Remove an Effect from a Character',
        'Modify the Turn Order',
        'Swap Friendly/Enemy Status',
        'Add a Character to the Battle',
        'Add a Monster to the Battle',
        'Remove a Character from the Battle',
        'Have a Character Join To Party',
        'Generate Battlefield',
        'Character Management',
        'Roll Dice',
        'Exit',
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


        if battle_task_menu_selected == 'Inspect Character':
            clear()
            print(battle_task_menu_selected)
            print_turn_banner()

            character_list = []
            selected_character, selected_index, character_menu_index = select_character_menu(character_list)


            def character_inspection():
                pass

            if selected_character == 'Exit':
                break                

            else:
                print_character(battle_in_initiative_order[selected_index].to_dict())

                input("\nPress Enter to Continue...")



        elif battle_task_menu_selected == 'Swap Friendly/Enemy Status':
            clear()
            print(battle_task_menu_selected)
            print_turn_banner()

            character_list = []
            selected_character, selected_index, character_menu_index = select_character_menu(character_list)

            if selected_character == 'Exit':
                break                

            else:
                if battle_in_initiative_order[selected_index].friendly == True:
                    battle_in_initiative_order[selected_index].friendly = False
                elif battle_in_initiative_order[selected_index].friendly == False:
                    battle_in_initiative_order[selected_index].friendly = True


            # for index, character in enumerate(battle_in_initiative_order):
            #     display_name = f"{character.display_name} the {character.char_race} {character.char_class}"

            #     current_hp = character.hp_current
            #     total_hp = character.hp_total
            #     hp_color = get_hp_color(current_hp, total_hp)

            #     if character.friendly == True:
            #         if len(character.effects) == 0:
            #             print(f"  {index + 1:>4}   [{character.initiative:>2}]   \033[92m{display_name:<65}\033[0m  {hp_color}{character.hp_current:>4} /{character.hp_total:>4}\033[0m    {'None':<8}")
            #         else:
            #             print(f"  {index + 1:>4}   [{character.initiative:>2}]   \033[92m{display_name:<65}\033[0m  {hp_color}{character.hp_current:>4} /{character.hp_total:>4}\033[0m    {', '.join(character.effects):<8}")
            #     elif character.friendly == False:
            #         if len(character.effects) == 0:
            #             print(f"  {index + 1:>4}   [{character.initiative:>2}]   \033[91m{display_name:<65}\033[0m  {hp_color}{character.hp_current:>4} /{character.hp_total:>4}\033[0m    {'None':<8}")
            #         else:
            #             print(f"  {index + 1:>4}   [{character.initiative:>2}]   \033[91m{display_name:<65}\033[0m  {hp_color}{character.hp_current:>4} /{character.hp_total:>4}\033[0m    {', '.join(character.effects):<8}")

        elif battle_task_menu_selected == 'Add a Character to the Battle':
            clear()
            print(battle_task_menu_selected)
            print_turn_banner()
            print_turn_order()

            character_number_tracker = max((char.profile['character number'] for char in all_characters), default=0) + 1
            create_character(all_characters,character_number_tracker,only_one=True)
            new_character_in_battle = all_characters[-1]
            temporary_battle_characters.append(new_character_in_battle)
            all_characters.pop()
            pickle_handler.save_dnd_state('characters', all_characters)
            pickle_handler.save_dnd_state('temporary_battle_characters', temporary_battle_characters, "./save_states/battles")

            print(f"\n\033[91mMake an Inititative Roll:\033[0m\n")
            print(f"Leave blank and press [Enter] for auto-roll, or enter a value manually.")

            char_to_add = character_enters_the_battle(new_character_in_battle)

            battle_in_initiative_order.append(char_to_add)
            pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")

            original_battle_characters.append(char_to_add)
            pickle_handler.save_dnd_state('original_battle_characters', original_battle_characters, "./save_states/battles")


        elif battle_task_menu_selected == 'Add a Monster to the Battle':
            clear()
            print(battle_task_menu_selected)
            print_turn_banner()
            print_turn_order()

            def autocomplete_monster(text, state):
                text_lower = text.lower()
                options = [key for key in dnd_monsters.keys() if text_lower in key.lower()]
                if state < len(options):
                    return options[state]
                else:
                    return None
                
            readline.set_completer(autocomplete_monster)
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

                        num_mon_to_add = ['1','2','3','4','5','6','7','8','9','10']
                        num_mon_to_add_menu = TerminalMenu(
                            num_mon_to_add,
                            title=f"Number of {matching_key} to add: "
                        )
                        num_mon_to_add_index = num_mon_to_add_menu.show()
                        num_mon_to_add_selected = num_mon_to_add[num_mon_to_add_index]


                        options=['Yes','No']
                        menu = TerminalMenu(options,title=f"Do you want to add {num_mon_to_add_selected} {matching_key}s this to the battle? ")
                        index = menu.show()
                        selected = options[index]

                        if selected == 'Yes':
                            for _ in range(int(num_mon_to_add_selected)):
                                monsters_on_the_battlefield.append(monster_enters_the_battle(dnd_monsters[matching_key]))
                                battle_in_initiative_order.append(monster_enters_the_battle(dnd_monsters[matching_key]))

                            pickle_handler.save_dnd_state('monsters_on_the_battlefield', monsters_on_the_battlefield, "./save_states/battles")
                            pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")

                        elif selected == 'No':
                            break

                        break
                    else:
                        print(f"[-] {user_input} is monster does not exist. Please enter a valid name.")


        elif battle_task_menu_selected == 'Modify the Turn Order':
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
                    print("Modify the Turn Order - Select Charater To Move:")
                    print_turn_banner()

                    character_list = []
                    selected_character, selected_index, character_menu_index = select_character_menu(character_list)

                    if selected_character == 'Exit':
                        break
                    else:
                        if change_turn_order_selected == 'Move Selected Up':
                            if character_menu_index is not None and character_menu_index > 0:
                                battle_in_initiative_order[character_menu_index], battle_in_initiative_order[character_menu_index - 1] = battle_in_initiative_order[character_menu_index - 1], battle_in_initiative_order[character_menu_index]
                        elif change_turn_order_selected == 'Move Selected Down':
                            if character_menu_index is not None and character_menu_index < len(battle_in_initiative_order) - 1:
                                battle_in_initiative_order[character_menu_index], battle_in_initiative_order[character_menu_index + 1] = battle_in_initiative_order[character_menu_index + 1], battle_in_initiative_order[character_menu_index]
                        pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")
            elif change_turn_order_selected == 'Exit':
                break

        elif battle_task_menu_selected == 'Attack a Character':
            clear()
            print(battle_task_menu_selected)
            print_turn_banner()

            character_list = []
            selected_character, selected_index, character_menu_index = select_character_menu(character_list)

            if selected_character == 'Exit':
                pass
            else:
                while True:
                    clear()
                    print(battle_task_menu_selected)
                    print_turn_banner()
                                        
                    if selected_character == 'Exit':
                        pass
                    else:
                        damage_selection_list = ['Roll Dice', 'Enter Manually', 'Exit']
                        damage_selection_menu = TerminalMenu(damage_selection_list)
                        damage_selection_index = damage_selection_menu.show()
                        damage_selection_selected = damage_selection_list[damage_selection_index]
                        if damage_selection_selected == 'Exit':
                            pass
                        else:
                            while True:
                                try:
                                    if damage_selection_selected == 'Roll Dice':
                                        damage_to_character = dnd_roll_dice()

                                        input("\nPress Enter to Continue...")

                                    elif damage_selection_selected == 'Enter Manually':
                                        damage_to_character = int(input(f"  {character_list[character_menu_index]}\n\nEnter damage: "))
                                    
                                    # subtracts damage
                                    battle_in_initiative_order[character_menu_index].hp_current = battle_in_initiative_order[character_menu_index].hp_current - damage_to_character

                                    # does not go below 0
                                    if battle_in_initiative_order[character_menu_index].hp_current < 0:
                                        battle_in_initiative_order[character_menu_index].hp_current = 0

                                    if battle_in_initiative_order[character_menu_index].hp_current <= 0:
                                        if 'Unconscious' not in battle_in_initiative_order[character_menu_index].effects and 'Instant Death' not in battle_in_initiative_order[character_menu_index].effects and 'Death' not in battle_in_initiative_order[character_menu_index].effects:
                                            battle_in_initiative_order[character_menu_index].effects.append('Unconscious')

                                    # if you take massive damage equal to you total hp... instant death
                                    if damage_to_character >= battle_in_initiative_order[character_menu_index].hp_total:
                                        if 'Unconscious' in battle_in_initiative_order[character_menu_index].effects:
                                            battle_in_initiative_order[character_menu_index].effects.remove('Unconscious')
                                        if 'Instant Death' not in battle_in_initiative_order[character_menu_index].effects:
                                            battle_in_initiative_order[character_menu_index].effects.append('Instant Death')

                                    # This just makes sense, no need to track how many revives in battle
                                    if 'Revived' in battle_in_initiative_order[character_menu_index].effects:
                                        battle_in_initiative_order[character_menu_index].effects.remove('Revived')


                                    pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")

                                    break
                                except:
                                    print(f"Ensure to enter a number")
                        break


        elif battle_task_menu_selected == 'Fumble Generator':
            clear()

            fumble_types = ['Melee Attack', 'Ranged Attack', 'Spell Attack', 'Skills Checks', 'Saving Throws']
            fumble_types_menu = TerminalMenu(fumble_types,title=f"Select a fumble type to generate: ")
            fumble_types_index = fumble_types_menu.show()
            fumble_types_selected = fumble_types[fumble_types_index]

            if fumble_types_selected == 'Melee Attack':
                print(random.choice(dnd_fumbles_melee))
                print()
                input(f"Press enter to continue")

            elif fumble_types_selected == 'Ranged Attack':
                print(random.choice(dnd_fumbles_ranged))
                print()
                input(f"Press enter to continue")

            elif fumble_types_selected == 'Spell Attack':
                print(random.choice(dnd_fumbles_spells))
                print()
                input(f"Press enter to continue")

            elif fumble_types_selected == 'Skills Checks':
                dnd_fumbles_skills_list = list(dnd_fumbles_skills.keys())
                fumble_menu = TerminalMenu(dnd_fumbles_skills_list)
                fumble_menu_index = fumble_menu.show()
                fumble_menu_selected = dnd_fumbles_skills_list[fumble_menu_index]
                print(random.choice(dnd_fumbles_skills.get(fumble_menu_selected)))
                print()
                input(f"Press enter to continue")

            elif fumble_types_selected ==  'Saving Throws':
                dnd_fumble_attribute_saves_list = list(dnd_fumble_attribute_saves.keys())
                fumble_menu = TerminalMenu(dnd_fumble_attribute_saves_list)
                fumble_menu_index = fumble_menu.show()
                fumble_menu_selected = dnd_fumble_attribute_saves_list[fumble_menu_index]
                print(random.choice(dnd_fumble_attribute_saves.get(fumble_menu_selected)))
                print()
                input(f"Press enter to continue")


        elif battle_task_menu_selected == 'Heal a Character':
            clear()
            print(battle_task_menu_selected)
            print_turn_banner()

            character_list = []
            selected_character, selected_index, character_menu_index = select_character_menu(character_list)

            if selected_character == 'Exit':
                pass
            else:
                while True:
                    clear()
                    print(battle_task_menu_selected)
                    print_turn_banner()
                                        
                    if selected_character == 'Exit':
                        pass
                    else:
                        heal_selection = ['Roll Dice', 'Enter Manually', 'Exit']
                        heal_selection_menu = TerminalMenu(heal_selection)
                        heal_selection_index = heal_selection_menu.show()
                        heal_selection_selected = heal_selection[heal_selection_index]
                        if heal_selection_selected == 'Exit':
                            pass
                        else:
                            while True:
                                try:
                                    if heal_selection_selected == 'Roll Dice':
                                        heal_character = dnd_roll_dice()

                                        input("\nPress Enter to Continue...")

                                    elif heal_selection_selected == 'Enter Manually':
                                        heal_character = int(input(f"  {character_list[character_menu_index]}\n\nEnter healing amount: "))

                                    # add heath
                                    if battle_in_initiative_order[character_menu_index].hp_current < battle_in_initiative_order[character_menu_index].hp_total: 
                                        battle_in_initiative_order[character_menu_index].hp_current = battle_in_initiative_order[character_menu_index].hp_current + heal_character
                                    # can't over heal them, only to max hp
                                    if battle_in_initiative_order[character_menu_index].hp_current > battle_in_initiative_order[character_menu_index].hp_total:
                                        battle_in_initiative_order[character_menu_index].hp_current = battle_in_initiative_order[character_menu_index].hp_total

                                    if battle_in_initiative_order[character_menu_index].hp_current > 0:
                                        if 'Instant Death' in battle_in_initiative_order[character_menu_index].effects:
                                            battle_in_initiative_order[character_menu_index].hp_current = 0
                                        if 'Death' in battle_in_initiative_order[character_menu_index].effects:
                                            battle_in_initiative_order[character_menu_index].hp_current = 0
                                        if 'Unconscious' in battle_in_initiative_order[character_menu_index].effects:
                                            battle_in_initiative_order[character_menu_index].effects.remove('Unconscious')

                                    pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")

                                    break
                                except:
                                    print(f"Ensure to enter a number")
                            break


        elif battle_task_menu_selected == 'Resurrect a Character':
            clear()
            print(battle_task_menu_selected)
            print_turn_banner()

            character_list = []
            selected_character, selected_index, character_menu_index = select_character_menu(character_list)

            if selected_character == 'Exit':
                pass
            else:
                while True:
                    clear()
                    print(battle_task_menu_selected)
                    print_turn_banner()
                                        
                    if selected_character == 'Exit':
                        pass
                    else:
                        revive_selection = ['Roll Dice', 'Enter Manually', 'Exit']
                        revive_selection_menu = TerminalMenu(revive_selection)
                        revive_selection_index = revive_selection_menu.show()
                        revive_selection_selected = revive_selection[revive_selection_index]
                        if revive_selection_selected == 'Exit':
                            pass
                        else:
                            while True:
                                try:
                                    if revive_selection_selected == 'Roll Dice':
                                        heal_character = dnd_roll_dice()

                                        input("\nPress Enter to Continue...")

                                    elif revive_selection_selected == 'Enter Manually':
                                        heal_character = int(input(f"  {character_list[character_menu_index]}\n\nEnter healing amount: "))

                                    # add heath
                                    if battle_in_initiative_order[character_menu_index].hp_current < battle_in_initiative_order[character_menu_index].hp_total: 
                                        battle_in_initiative_order[character_menu_index].hp_current = battle_in_initiative_order[character_menu_index].hp_current + heal_character
                                    # can't over heal them, only to max hp
                                    if battle_in_initiative_order[character_menu_index].hp_current > battle_in_initiative_order[character_menu_index].hp_total:
                                        battle_in_initiative_order[character_menu_index].hp_current = battle_in_initiative_order[character_menu_index].hp_total


                                    if 'Instant Death' in battle_in_initiative_order[character_menu_index].effects:
                                        battle_in_initiative_order[character_menu_index].effects.remove('Instant Death')
                                        if 'Revived' not in battle_in_initiative_order[character_menu_index].effects:
                                            battle_in_initiative_order[character_menu_index].effects.insert(0,'Revived')
                                    if 'Death' in battle_in_initiative_order[character_menu_index].effects:
                                        battle_in_initiative_order[character_menu_index].effects.remove('Death')
                                        if 'Revived' not in battle_in_initiative_order[character_menu_index].effects:
                                            battle_in_initiative_order[character_menu_index].effects.insert(0,'Revived')
                                    if 'Unconscious' in battle_in_initiative_order[character_menu_index].effects:
                                        battle_in_initiative_order[character_menu_index].effects.remove('Unconscious')
                                    # pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")

                                    break

                                except:
                                    print(f"Ensure to enter a number")
                            break


        elif battle_task_menu_selected == 'Apply an Effect to a Character':
            clear()
            print(battle_task_menu_selected)
            print_turn_banner()

            character_list = []
            selected_character, selected_index, character_menu_index = select_character_menu(character_list)

            if selected_character == 'Exit':
                pass
            else:
                while True:
                    clear()
                    print(battle_task_menu_selected)
                    print_turn_banner()
                    print_turn_order()

                    def autocomplete_condition_status(text, state):
                        text_lower = text.lower()
                        options = [key for key in conditions_and_effects if text_lower in key.lower()]
                        if state < len(options):
                            return options[state]
                        else:
                            return None
                        
                    readline.set_completer(autocomplete_condition_status)
                    readline.parse_and_bind("tab: complete")

                    while True:
                        print(f"\nType 'Exit' to exit search.")
                        user_input = input("\nSearch for a condition or status to add to the character: [Supports Tab Completion] ")
                        user_input = user_input.lower()
                        
                        if user_input.lower() == 'exit':
                            break
                        else:
                            # Check if the entered item (in lowercase) is in the inventory
                            lowercase_keys = [key.lower() for key in conditions_and_effects]
                            if user_input in lowercase_keys:
                                # Find the original key with matching lowercase version
                                matching_key = conditions_and_effects[lowercase_keys.index(user_input)]
                                # print(f"[+] You have {conditions_and_effects[matching_key]} {matching_key}(s) in your inventory.")
                                if user_input not in [item.lower() for item in battle_in_initiative_order[character_menu_index].effects]:
                                    battle_in_initiative_order[character_menu_index].effects.append(user_input.title())                                    
                                break
                            else:
                                print(f"[-] {user_input} is condition or status does not exist.")
                    pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")
                    break


        elif battle_task_menu_selected == 'Remove an Effect from a Character':
            clear()
            print(battle_task_menu_selected)
            print_turn_banner()

            character_list = []
            selected_character, selected_index, character_menu_index = select_character_menu(character_list)

            if selected_character == 'Exit':
                pass
            else:
                while True:
                    clear()
                    print(battle_task_menu_selected)
                    print_turn_banner()
                    print_turn_order()

                    while True:
                        print("Select a condition or status from a character:")
                        battle_in_initiative_order[character_menu_index].effects.append('Exit')
                        character_effects_menu = TerminalMenu(battle_in_initiative_order[character_menu_index].effects)
                        character_effects_index = character_effects_menu.show()
                        character_effects_selected = battle_in_initiative_order[character_menu_index].effects[character_effects_index]

                        if character_effects_selected == 'Exit':
                            battle_in_initiative_order[character_menu_index].effects.pop()
                            break
                        else:
                            battle_in_initiative_order[character_menu_index].effects.pop()
                            battle_in_initiative_order[character_menu_index].effects.remove(character_effects_selected)
                            break
                    pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")
                    break



        elif battle_task_menu_selected == 'Remove a Character from the Battle':
            while True:
                clear()
                print(battle_task_menu_selected)
                print_turn_banner()
                
                character_list = []
                selected_character, selected_index, character_menu_index = select_character_menu(character_list)
                
                if selected_character == 'Exit':
                    pass
                else:
                    character_remove_confirm = input(f"  {character_list[character_menu_index]}\n\nEnter 'd' to confirm deletion: ")
                    if character_remove_confirm.lower() == 'd':
                        del character_list[character_menu_index]
                        del battle_in_initiative_order[character_menu_index]
                        pickle_handler.save_dnd_state('battle', battle_in_initiative_order, "./save_states/battles")

                    else:
                        pass  
                break


        elif battle_task_menu_selected == 'Have a Character Join To Party':
            clear()
            print(battle_task_menu_selected)
            print_turn_banner()

            character_list = []
            selected_character, selected_index, character_menu_index = select_character_menu(character_list, from_battle=True)

            print(f"\n  Note: You can only have Character join a party - monsters are not supported.\n")
            if selected_character == 'Exit':
                break                
            else:
                for character_in_battle in temporary_battle_characters:
                    if character_in_battle.profile['name']['full'] in selected_character:
                        all_characters.append(character_in_battle)
                        pickle_handler.save_dnd_state('characters', all_characters)
                        print(f"  {character_in_battle.profile['name']['full']} the {character_in_battle.character_race['Name']} {character_in_battle.character_class['Name']} has joined the party.\n")
                    # else:
                    #     print(f"\n  This is currently not permitted. {character_in_battle.profile['name']['full']} is a monster can not join the party.\n")

                input(f"  Press enter to continue.")



        elif battle_task_menu_selected == 'Generate Battlefield':

            # Convert the monsters_on_the_battlefield to be compatible with the battlefield map generator
            monster_counts = {}
            for monster in monsters_on_the_battlefield:
                # if monster.name 
                if monster.name not in monster_counts:
                    monster_counts[monster.name] = 1
                elif monster.name in monster_counts:
                    monster_counts[monster.name] += 1

            # debug(len(monsters_on_the_battlefield)) # too many, inclues char, temp char, and mon
            # debug(temporary_battle_characters) #too few
            # debug(characters_in_battle) #none?
            map_these_characters = {}
            for index, char in enumerate(original_battle_characters):
                # print(
                #     char.name,
                #     char.char_race,
                #     char.char_class,
                #     index +1,
                #     "'Color': 'Magenta_BG'",
                # )
                map_these_characters[char.name] = {
                    'Marker': f"{index +1:02d}",
                    'Color': 'Magenta_BG',
                }

            battlefield_grid_display = battlefield.main(
                grid_size = 50,
                monster_counts = monster_counts,
                map_these_characters = map_these_characters,
            )

            input(f"Press enter to continue")


        elif battle_task_menu_selected == 'Character Management':
            character_management(all_characters)


        elif battle_task_menu_selected == 'Roll Dice':
            dnd_roll_dice()
            input("\nPress Enter to Continue...")


        elif battle_task_menu_selected == 'Exit':
            break

        else:
            print('What the F is this error...')




if __name__ == '__main__':
    # Option to load previous save files
    all_characters = pickle_handler.select_and_load_pkl()
    if all_characters is not None:
        print("Characters loaded")
    else:
        print("No Characters loaded")
        all_characters = []
    print()

    main(all_characters)


