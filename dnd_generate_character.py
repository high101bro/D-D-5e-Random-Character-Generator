#! /usr/bin/env python3

# character = {
#     'profile' : {
        # 'name' : {
        #     'first' : "",
        #     'last' : ""

#     'items' : {
#         'armor' : {
#             'name' : "",
#             'class' : 0,
#             'type' : "",
#             'stealth' : "",
#             'strength' : 0,
#             'properties' : [],
#             'description' : "",
#         },
#         'tools' : [],
#         'items' : [],
#     },
# }
# print(character)

import random, os, datetime
from dnd_lists import *
from dnd_races import *
from dnd_classes import *
from dnd_backgrounds import *
from dnd_helper import *
from dnd_spells import *
from chatgpt_dall_e import *
from dnd_towns_and_cities import *

item_list = [generate_item_list() for _ in range(10)]
weapon_list = [generate_weapon_list() for _ in range(10)]


class Character():
    def __init__(self):
        self.profile = {}
        self.memory = {}
        self.character_race = {}
        self.character_class = {}
        self.description = {}
        self.background = {}
        self.level_chart = {}
        self.attributes = {
            'strength' : {},
            'dexterity' : {},
            'constitution' : {},
            'intelligence' : {},
            'wisdom' : {},
            'charisma' : {}
        }
        self.capabilities = {}
        self.skills = {}
        self.features = {}
        self.money = {
            'cp' : 0,
            'sp' : 0,
            'ep' : 0,
            'gp' : 0,
            'pp' : 0
        }
        self.items = []
        self.armor = []
        self.weapons = {}
        self.combat = {}
        self.spells = {
            "Spellcasting" : "",
            "Preparation" : "",
            "Spellcasting Modifier" : "",
            "Attack Modifier" : 0,
            "Save DC" : 0,
            "Spells Known" : {
                "Slots" : {},
            },
            "Selected Spells" : []
        }
    def to_dict(self):
        return {
            'profile' : self.profile,
            'character_race' : self.character_race,
            'character_class' : self.character_class,
            'description' : self.description,
            'background' : self.background,
            'level_chart' : self.level_chart,
            'attributes' : self.attributes,
            'capabilities' : self.capabilities,
            'skills' : self.skills,
            'features' : self.features,
            'money' : self.money,
            'items' : self.items,
            'armor' : self.armor,
            'weapons' : self.weapons,
            'combat' : self.combat,
            'spells' : self.spells,
        }



def create_character(all_characters,character_number_tracker,only_one=False):
    characters_to_create = []
    continue_char_number = True
    while continue_char_number:
        # Number of characters_to_create
        clear()
        if only_one == True:
            character_number = 1
            character_number_selected = 1
        elif only_one == False:
            print('\033[91mHow many characters do you want to create? \033[0m\n')
            dnd_choose_character_number = ['Random Number','1','2','3','4','5','6','7','8','9','10','Exit']
            character_number_menu = TerminalMenu(dnd_choose_character_number)
            character_number_index = character_number_menu.show()
            character_number_selected = dnd_choose_character_number[character_number_index]
            dnd_choose_character_number.remove('Random Number')
            dnd_choose_character_number.remove('Exit')

        if character_number_selected == 'Exit':
            continue_char_number = False
            continue_guide_or_automated = False
            continue_guided = False
            break

        elif character_number_selected == 'Random Number':
            character_number = int(random.choice(dnd_choose_character_number))
            continue_char_number = False
            continue_guide_or_automated = True
            continue_guided = True

        else: # The chosen number of characters_to_create
            character_number = int(character_number_selected)
            continue_char_number = False
            continue_guide_or_automated = True
            continue_guided = True

        while continue_guide_or_automated:
            if character_number > 0:
                # Create the characters_to_create
                for _ in range(character_number):
                    character = Character()
                    characters_to_create.append(character)

                clear()
                if int(character_number) > 1 :
                    print(f"Great. Each character will be created one a time. Let's start with Character \033[92m1 of {character_number}\033[0m.\n")
                else:
                    print(f"Great. Let's create a new character.\n")

                print('\033[91mDo you want to guide the character generation or have it completely automated? \033[0m\n')
                dnd_choose_character_number = ['Automated','Guided','Manual','Go Back','Exit']
                generation_menu = TerminalMenu(dnd_choose_character_number)
                generation_menu_index = generation_menu.show()
                generation_menu_selected = dnd_choose_character_number[generation_menu_index]


                if generation_menu_selected == 'Exit':
                    continue_char_number = False
                    continue_guide_or_automated = False
                    break

                elif generation_menu_selected == 'Go Back':
                    continue_char_number = True
                    continue_guide_or_automated = True
                    break

                elif generation_menu_selected == 'Automated':
                    for index, character in enumerate(characters_to_create):

                        clear()
                        character_number_tracker = max((char.profile['character number'] for char in all_characters), default=0) + 1
                        # character_number_tracker += 1
                        all_characters.append(
                            generate_characters(
                                character,
                                character_number_tracker,
                                character_level = random.randint(1,20),
                                character_race = random.choice(list(dnd_races.keys())),
                                character_class = random.choice(list(dnd_classes.keys())),
                                method='Automated',
                            )
                        )
                        pickle_handler.save_dnd_state('characters', all_characters)
                        clear()

                    continue_char_number = False
                    continue_guide_or_automated = False
                    break


                elif generation_menu_selected == 'Guided':
                    for index, character in enumerate(characters_to_create):

                        clear()
                        character_number_tracker = max((char.profile['character number'] for char in all_characters), default=0) + 1
                        # character_number_tracker += 1

                        character, character_level, character_race, character_class = create_character_guided_or_manual(character, character_number_tracker)
                        all_characters.append(
                            generate_characters(
                                character,
                                character_number_tracker,
                                character_level,
                                character_race,
                                character_class,
                                method='Guided',
                            )
                        )
                        pickle_handler.save_dnd_state('characters', all_characters)                            
                        clear()

                    continue_char_number = False
                    continue_guide_or_automated = False                            
                    break


                elif generation_menu_selected == 'Manual':
                    for index, character in enumerate(characters_to_create):

                        clear()
                        character_number_tracker = max((char.profile['character number'] for char in all_characters), default=0) + 1
                        # character_number_tracker += 1
                        character, character_level, character_race, character_class = create_character_guided_or_manual(character, character_number_tracker)
                        all_characters.append(
                            generate_characters(
                                character,
                                character_number_tracker,
                                character_level,
                                character_race,
                                character_class,
                                method='Manual'
                            )
                        )
                        pickle_handler.save_dnd_state('characters', all_characters)                            
                        clear()

                    continue_char_number = False
                    continue_guide_or_automated = False                            
                    break
                

def create_character_guided_or_manual(character, character_number):
    continue_guided = True
    while continue_guided:
        # Character Level
        clear()
        print(f"\033[92mCharacter {character_number}\033[0m will be a level \033[91m[#]\033[0m, [race] [class].\n")
        print("\033[91mSelect Character Level:\033[0m\n")
        level_menu_list = ['Random Level'] + dnd_menu_level + ['Go Back','Exit']
        level_menu_menu = TerminalMenu(level_menu_list)
        level_menu_index = level_menu_menu.show()
        level_menu_selected = level_menu_list[level_menu_index]

        if level_menu_selected == "Exit":
            continue_char_number = False
            continue_guide_or_automated = False
            continue_guided = False
            continue_race = False
            break

        elif level_menu_selected == 'Go Back':
            continue_char_number = True
            continue_guide_or_automated = True
            continue_guided = False
            continue_race = False
            break

        elif level_menu_selected == "Random Level": 
            character_level = random.randint(1,20)
            continue_char_number = False
            continue_guide_or_automated = False
            continue_guided = False
            continue_race = True

        else: # The chosen level of the character
            character_level = int(level_menu_list[level_menu_index][:8][-3:])
            continue_char_number = False
            continue_guide_or_automated = False
            continue_guided = False
            continue_race = True

        while continue_race:
            # Character Race
            clear()
            print(f"\033[92mCharacter {character_number}\033[0m will be a level \033[92m{character_level}\033[0m, \033[91m[race]\033[0m [class].\n")
            print("\033[91mSelect Character Race:\033[0m\n")
            char_race_list = ['Random Race'] + dnd_race_list + ["Go Back","Exit"]
            char_race_menu = TerminalMenu(char_race_list)
            char_race_index = char_race_menu.show()
            char_race_selected = char_race_list[char_race_index]

            if char_race_selected == 'Exit':
                continue_char_number = False
                continue_guide_or_automated = False
                continue_guided = False
                continue_race = False
                continue_class = False
                continue_create_character = False
                break
            elif char_race_selected == 'Go Back':
                continue_char_number = True
                continue_guide_or_automated = True
                continue_guided = True
                continue_race = False
                continue_class = False
                # continue_create_character = False
                break
            elif char_race_selected == 'Random Race':
                character_race = random.choice(list(dnd_races.keys()))
                continue_char_number = False
                continue_guide_or_automated = False
                continue_guided = False
                continue_race = False
                continue_class = True
                # continue_create_character = False
            else: # The chosen race of the character
                character_race = char_race_list[char_race_index].split()[0]
                continue_char_number = False
                continue_guide_or_automated = False
                continue_guided = False
                continue_race = False
                continue_class = True
                # continue_create_character = False


            while continue_class:
                # Character Class
                clear()
                print(f"\033[92mCharacter {character_number}\033[0m will be a level \033[92m{character_level}\033[0m, \033[92m{character_race}\033[0m \033[91m[class]\033[0m.\n")
                print("\033[91mSelect Character Class:\033[0m\n")
                char_class_list = ["Random Class"] + dnd_class_list + ["Go Back","Exit"]
                char_class_menu = TerminalMenu(char_class_list)
                char_class_index = char_class_menu.show()
                char_class_selected = char_class_list[char_class_index]

                if char_class_selected == "Exit":
                    continue_char_number = False
                    continue_guide_or_automated = False
                    continue_guided = False
                    continue_race = False
                    continue_class = False
                    continue_create_character = False
                    break
                if char_class_selected == "Go Back":
                    continue_char_number = True
                    continue_guide_or_automated = True
                    continue_guided = True
                    continue_race = True
                    continue_class = False
                    continue_create_character = False
                    break
                elif char_class_selected == "Random Class":
                    character_class = random.choice(list(dnd_classes.keys()))
                    continue_char_number = False
                    continue_guide_or_automated = False
                    continue_guided = False
                    continue_race = False
                    continue_class = False
                    continue_create_character = True
                else: # The chosen class of the character
                    character_class = char_class_list[char_class_index].split()[0]
                    continue_char_number = False
                    continue_guide_or_automated = False
                    continue_guided = False
                    continue_race = False
                    continue_class = False
                    continue_create_character = True


                while continue_create_character:
                    # Proceed with character creation or not
                    clear()
                    print(f"\033[92mCharacter {character_number} will be a level {character_level}, {character_race} {character_class}.\033[0m\n")
                    print(f"\033[91mWould you like to proceed with creating this character? \033[0m\n")
                    create_character_list = ["Yes","No","Go Back","Exit"]
                    create_character_menu = TerminalMenu(create_character_list)
                    create_character_index = create_character_menu.show()
                    create_character_selected = create_character_list[create_character_index]

                    if create_character_selected == "Exit":
                        continue_char_number = False
                        continue_guide_or_automated = False
                        continue_guided = False
                        continue_race = False
                        continue_class = False
                        continue_create_character = False
                        break
                    elif create_character_selected == "Go Back":
                        continue_char_number = True
                        continue_guide_or_automated = True
                        continue_guided = True
                        continue_race = True
                        continue_class = True
                        continue_create_character = False
                        break
                    elif create_character_selected == "Yes":
                        clear()
                        character_number += 1

                        continue_char_number = False
                        continue_guide_or_automated = False
                        continue_guided = False
                        continue_race = False
                        continue_class = False
                        continue_create_character = False

                        return character, character_level, character_race, character_class

                    elif create_character_selected == "No":
                        continue_char_number = False
                        continue_guide_or_automated = False
                        continue_guided = False
                        continue_race = False
                        continue_class = False
                        continue_create_character = False
                        break



# Create random character
def generate_characters(character, character_number, character_level=1, character_race='Human', character_class='Fighter', method='Automated'):

    character.profile['character number'] = character_number
    character.profile['created'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%S"))
    character.profile['name'] = {}
    character.profile['name']['first'] = random.choice(first_names)
    character.profile['name']['last'] = random.choice(last_names)
    character.profile['name']['full'] = f"{character.profile['name']['first']} {character.profile['name']['last']}"
    character.profile['level'] = character_level
    character.profile['proficiency bonus'] = dnd_proficiency_bonus.get(character_level, '1')
    character.profile['experience'] = dnd_levels_exp.get(character_level, '1')    
    character.profile['alignment'] = random.choice(list(dnd_alignments))



    # Locations
    character.profile['born and raised'] = random.choice(list(dnd_towns_and_cities.keys()))
    character.profile['current residence'] = character.profile['born and raised'] # We'll assume this person hasn't moved... yet
    character.profile['places visited'] = [character.profile['born and raised']] # The person has at least visited where they were rasied

    def will_character_travel(chance_to_move):        
        random_number = random.randint(1, 100) # Generate a random number between 1 and 100
        if random_number <= chance_to_move:
            return True   # The character will move
        else:
            return False  # The character will not move

    hometown_population = dnd_towns_and_cities[character.profile['born and raised']]["Population"]
    if hometown_population < 3000:
        move_percentage = 10 # This one is small as we'll assume small town people may never leave
        for i in range(0,random.randint(0,3)): # May have visited from 0 to 3 places
            random_location_visited = random.choice(list(dnd_towns_and_cities.keys()))
            if random_location_visited not in character.profile['places visited']:
                character.profile['places visited'].append(random_location_visited)
    elif hometown_population < 10000:
        move_percentage = 75 # large because people are potentially moving to get the hell out of town
        for i in range(0,random.randint(0,3)): # May have visited from 0 to 3 places
            random_location_visited = random.choice(list(dnd_towns_and_cities.keys()))
            if random_location_visited not in character.profile['places visited']:
                character.profile['places visited'].append(random_location_visited)
    elif hometown_population < 20000:
        move_percentage = 50 # 50/50 on moving, some people like to travel
        for i in range(0,random.randint(2,5)): # May have visited from 2 to 5 places
            random_location_visited = random.choice(list(dnd_towns_and_cities.keys()))
            if random_location_visited not in character.profile['places visited']:
                character.profile['places visited'].append(random_location_visited)
    else:
        move_percentage = 25 # For larger cities, people may never have the need to move
        for i in range(0,random.randint(3,10)): # May have visited from 3 to 10 places
            random_location_visited = random.choice(list(dnd_towns_and_cities.keys()))
            if random_location_visited not in character.profile['places visited']:
                character.profile['places visited'].append(random_location_visited)

    if character.profile['current residence'] != character.profile['born and raised']:
        character.profile['places visited'].append(character.profile['current residence'])

    # Determine if the character will move
    character_will_move = will_character_travel(move_percentage)
    if character_will_move:
        character.profile['current residence'] = random.choice(list(dnd_towns_and_cities.keys()))



    character.character_race = dnd_races[character_race]


    character.character_class["ASCII Art"] = dnd_classes[character_class]["ASCII Art"]
    character.character_class["Name"] = dnd_classes[character_class]["Name"]
    character.character_class["Description"] = dnd_classes[character_class]["Description"]
    character.character_class["Requirements"] = dnd_classes[character_class]["Requirements"]
    character.character_class["Hit Die"] = dnd_classes[character_class]["Hit Die"]
    character.character_class["Current Level Chart"] = {}
    character.character_class["Current Level Chart"][character_level] = dnd_classes[character_class]["Level Chart"][int(character_level)]
    character.character_class["Features"] = dnd_classes[character_class]["Features"]
    character.character_class["Attribute Priority"] = dnd_classes[character_class]["Attribute Priority"]
    character.character_class["Spells"] = dnd_classes[character_class]["Spells"]

    character.description = {}

    character.description['race'] = str(character_race)

    character.description['class'] = str(character_class)
    

    # Age
    character_age_ranges = {
        'Elf': (18, 701),
        'Dwarf': (18, 401),
        'Dragonborn': (18, 81),
        'Gnome': (18, 351),
        'Half-Elf': (18, 181),
        'Half-Orc': (18, 71),
        'Halfling': (18, 151),
        'Human': (18, 81),
        'Tiefling': (18, 81),
    }
    if method == 'Automated' or method == 'Guided':
        character.description['age'] = random.randint(character_age_ranges[character_race][0], character_age_ranges[character_race][1])
    elif method == 'Manual':
        character.description['age'] = terminalmenu_quick_select([str(num) for num in range(character_age_ranges[character_race][0], character_age_ranges[character_race][1])], f'[{character_race}] Select an age:')


    # Gender
    if method == 'Automated' or method == 'Guided':
        character.description['gender'] = str(random.choice(list(['Male','Female','Unknown'])))
    elif method == 'Manual':
        character.description['gender'] = terminalmenu_quick_select(['Male', 'Female', 'Hermaphrodite', 'Non-Binary', 'Transgender', 'Unknown', 'Other', 'None'], f'[{character_race}] Select a gender:')


    # Height
    character_height_ranges = {
        'Elf': (60, 73),
        'Dwarf': (48, 59),
        'Dragonborn': (66, 79),
        'Gnome': (35, 43),
        'Half-Elf': (62, 75),
        'Half-Orc': (58, 73),
        'Halfling': (18, 151),
        'Human': (56, 79),
        'Tiefling': (57, 74),
    }
    if method == 'Automated' or method == 'Guided':
        character.description['height'] = random.randint(character_height_ranges[character_race][0], character_height_ranges[character_race][1])
    elif method == 'Manual':
        character.description['height'] = terminalmenu_quick_select([str(num) for num in range(character_height_ranges[character_race][0], character_height_ranges[character_race][1])], f'[{character_race}] Select a height in inches:')


    # Weight
    character_weight_ranges = {
        'Elf': (100, 146),
        'Dwarf': (130, 181),
        'Dragonborn': (220, 321),
        'Gnome': (35, 43),
        'Half-Elf': (110, 161),
        'Half-Orc': (140, 251),
        'Halfling': (35, 46),
        'Human': (155, 241),
        'Tiefling': (110, 191),
    }
    if method == 'Automated' or method == 'Guided':
        character.description['weight'] = random.randint(character_weight_ranges[character_race][0], character_weight_ranges[character_race][1])
    elif method == 'Manual':
        character.description['weight'] = terminalmenu_quick_select([str(num) for num in range(character_weight_ranges[character_race][0],character_weight_ranges[character_race][1])], f'[{character_race}] Select a weight in pounds:')


    # Skin variations
    if method == 'Automated' or method == 'Guided':
        character.description['skin_type'] = random.choice(character_skin_type_variations[character_race])
    elif method == 'Manual':
        character.description['skin_type'] = terminalmenu_quick_select(character_skin_type_variations[character_race], f'[{character_race}] Select a skin type variation:')


    if method == 'Automated' or method == 'Guided':
        character.description['skin_color'] = random.choice(character_skin_color_variations[character_race])
    elif method == 'Manual':
        character.description['skin_color'] = terminalmenu_quick_select(character_skin_color_variations[character_race], f'[{character_race}] Select a skin color variation:')








    # Facial Features
    if method == 'Automated' or method == 'Guided':
        character.description['facial_features'] = random.choice(character_race_facial_features[character_race])
    elif method == 'Manual':
        character.description['facial_features'] = terminalmenu_quick_select(character_race_facial_features[character_race], f'[{character_race}] Select a facial feature:')


    # Eye Brows
    if method == "Automated" or method == "Guided":
        character.description["Eye Brows"] = random.choice(['None','Short','Medium','Long', 'Thin', 'Bushy', 'Other'])
    elif method == "Manual":
        character.description["Eye Brows"] = terminalmenu_quick_select(['Short','Medium','Long', 'Thin', 'Bushy', 'Other'], f"[{character_race}] Select an eye brow style:")


    # Eye Description
    if method == "Automated" or method == "Guided":
        character.description["Eye Description"] = random.choice(character_eye_shape_variations[character_race])
    elif method == "Manual":
        character.description["Eye Description"] = terminalmenu_quick_select(character_eye_shape_variations[character_race], f"[{character_race}] Select an eye description:")


    # Eye Features
    if method == "Automated" or method == "Guided":
        character.description["Eye Feature"] = random.choice(character_eye_feature_variations)
    elif method == "Manual":
        selected_feature = terminalmenu_quick_select(character_eye_feature_variations, f"[{character_race}] Select an eye feature or sight condition:")
        character.description["Eye Feature"] = selected_feature
    

    # Eye Color
    if method == "Automated" or method == "Guided":
        character.description["Eye Color"] = random.choice(character_eye_color_variations[character_race])
    elif method == "Manual":
        character.description["Eye Color"] = terminalmenu_quick_select(character_eye_color_variations[character_race], f"[{character_race}] Select an eye color:")


    # Nose
    if method == "Automated" or method == "Guided":
        character.description["Nose Description"] = random.choice(character_race_nose_variations[character_race])
    elif method == "Manual":
        character.description["Nose Description"] = terminalmenu_quick_select(character_race_nose_variations[character_race], f"[{character_race}] Select a nose feature:")


    # Hair Style
    if method == 'Automated' or method == 'Guided':
        character.description['Hair Style'] = random.choice(character_race_hair_style[character_race])
    elif method == 'Manual':
        character.description['Hair Style'] = terminalmenu_quick_select(character_race_hair_style[character_race], f'[{character_race}] Select a hair style:')


    # Hair Color
    if method == 'Automated' or method == 'Guided':
        character.description['Hair Color'] = random.choice(character_race_hair_colors[character_race])
    elif method == 'Manual':
        character.description['Hair Color'] = terminalmenu_quick_select(character_race_hair_colors[character_race], f'[{character_race}] Select a hair color:')


    # Ear Description
    if method == "Automated" or method == "Guided":
        character.description["Ear Description"] = random.choice(character_race_ear_features[character_race])
    elif method == "Manual":
        character.description["Ear Description"] = terminalmenu_quick_select(character_race_ear_features[character_race], f"[{character_race}] Select an ear description:")


    # Chin Features
    if method == "Automated" or method == "Guided":
        character.description["Chin Description"] = random.choice(character_race_chin_descriptions[character_race])
    elif method == "Manual":
        character.description["Chin Description"] = terminalmenu_quick_select(character_race_chin_descriptions[character_race], f"[{character_race}] Select a chin feature:")


    # Facial Hair Style
    if method == 'Automated' or method == 'Guided':
        character.description['Facial Hair'] = random.choice(character_race_facial_hair[character_race])
    elif method == 'Manual':
        character.description['Facial Hair'] = terminalmenu_quick_select(character_race_facial_hair[character_race], f'[{character_race}] Select a facial hair style:')


    # Body Type
    if method == 'Automated' or method == 'Guided':
        character.description['Body Type'] = random.choice(character_race_body_types[character_race])
    elif method == 'Manual':
        character.description['Body Type'] = terminalmenu_quick_select(character_race_body_types[character_race], f'[{character_race}] Select a body type:')


    # Tattoo Locations
    if method == 'Automated' or method == 'Guided':
        character.description['Tatoo Location'] = random.choice(character_race_tattoo_locations[character_race])
    elif method == 'Manual':
        character.description['Tatoo Location'] = terminalmenu_quick_select(character_race_tattoo_locations[character_race], f'[{character_race}] Select a tattoo location:')


    # Scent
    if method == "Automated" or method == "Guided":
        character.description["Scent"] = random.choice(character_scent_variations[character_race])
    elif method == "Manual":
        character.description["Scent"] = terminalmenu_quick_select(character_scent_variations[character_race], f"[{character_race}] Select a scent:")


    # Skin
    if method == "Automated" or method == "Guided":
        character.description["skin_defect"] = random.choice(character_skin_defect_variations[character_race])
    elif method == "Manual":
        character.description["skin_defect"] = terminalmenu_quick_select(character_skin_defect_variations[character_race], f"[{character_race}] Select a skin defect:")




    # Clothing Style
    if method == 'Automated' or method == 'Guided':
        character.description['Clothing Sytle'] = random.choice(character_race_clothing_styles[character_race])
    elif method == 'Manual':
        character.description['Clothing Sytle'] = terminalmenu_quick_select(character_race_clothing_styles[character_race], f'[{character_race}] Select a clothing style:')


    # Accessories
    if method == 'Automated' or method == 'Guided':
        character.description['Accessories'] = random.choice(character_race_accessories[character_race])
    elif method == 'Manual':
        character.description['Accessories'] = terminalmenu_quick_select(character_race_accessories[character_race], f'[{character_race}] Select an accessory:')
    

    # Voice
    if method == 'Automated' or method == 'Guided':
        character.description['Voice'] = random.choice(character_race_voices[character_race])
    elif method == 'Manual':
        character.description['Voice'] = terminalmenu_quick_select(character_race_voices[character_race], f'[{character_race}] Select a voice:')


    # Manerism
    if method == 'Automated' or method == 'Guided':
        character.description['Mannerisms'] = random.choice(character_race_mannerisms[character_race])
    elif method == 'Manual':
        character.description['Mannerisms'] = terminalmenu_quick_select(character_race_mannerisms[character_race], f'[{character_race}] Select mannerisms:')


    # Personaltiy Trait
    if method == 'Automated' or method == 'Guided':
        character.description['personality'] = random.choice(character_race_personalities[character_race])
    elif method == 'Manual':
        character.description['personality'] = terminalmenu_quick_select(character_race_personalities[character_race], f'[{character_race}] Select a personality trait:')


    # Background
    character.background = {}
    if method == 'Automated':
        character_automated_background_selected = terminalmenu_quick_select(["Use random pre-built template","Create random background from others"], f'[{character_race}] Select a background:')
        if character_automated_background_selected == "Use random pre-built template":
            character.background['name'] = random.choice(list(dnd_backgrounds.keys()))
            character.background = dnd_backgrounds[character.background['name']]    
        elif character_automated_background_selected == "Create random background from others":
            randomly_generated_background = generate_random_background(dnd_backgrounds)
            character.background['name'] = randomly_generated_background["Name"]
            character.background = randomly_generated_background
    elif method == 'Guided':
        character.background['name'] = terminalmenu_quick_select(sorted(list(dnd_backgrounds.keys())), f'[{character_race}] Select a background:')
        character.background = dnd_backgrounds[character.background['name']]
    elif method == 'Manual':
        character.background = {}
        character.background['Name']                = terminalmenu_quick_select(sorted(list(set(dnd_backgrounds.keys()))), f'[{character_race}] Select a background name:')
        character.background['Source']              = "Manually Selected"
        character.background['Details']             = terminalmenu_quick_select(sorted(list(set([dnd_backgrounds[background]["Details"]  for background in dnd_backgrounds]))), f'[{character_race}] Select background details:')
        character.background['Features']            = terminalmenu_quick_select(sorted(list(set([dnd_backgrounds[background]["Features"] for background in dnd_backgrounds]))), f'[{character_race}] Select background features:')
        character.background['Skill Proficiencies'] = terminalmenu_quick_select(sorted(list(set([', '.join(dnd_backgrounds[background]["Skill Proficiencies"]).lower() for background in dnd_backgrounds]))), f'[{character_race}] Select background skill proficiencies:')
        character.background['Tool Proficiencies']  = terminalmenu_quick_select(sorted(list(set([', '.join(dnd_backgrounds[background]["Tool Proficiencies"])  for background in dnd_backgrounds]))), f'[{character_race}] Select background tool proficiencies:')
        character.background['Languages']           = terminalmenu_quick_select(sorted(list(set([', '.join(dnd_backgrounds[background]["Languages"]) for background in dnd_backgrounds]))), f'[{character_race}] Select background languages:')
        character.background['Equipment']           = terminalmenu_quick_select(sorted(list(set([dnd_backgrounds[background]["Equipment"] for background in dnd_backgrounds]))), f'[{character_race}] Select background equipment:')
        character.background['Roleplaying Suggestions'] = {}

        character_background_persontality_trait_list = []
        for background in dnd_backgrounds:
            character_background_persontality_trait_list.append(dnd_backgrounds[background]["Roleplaying Suggestions"]["Personality Trait"])
        character_background_persontality_trait_list = list(set(character_background_persontality_trait_list))
        character.background['Roleplaying Suggestions']["Personality Trait"] = terminalmenu_quick_select(sorted(list(character_background_persontality_trait_list)), f'[{character_race}] Select a background suggested roleplaying ideal:')
        
        character_background_ideal_list = []
        for background in dnd_backgrounds:
            character_background_ideal_list.append(dnd_backgrounds[background]["Roleplaying Suggestions"]["Ideal"])
        character_background_ideal_list = list(set(character_background_ideal_list))
        character.background['Roleplaying Suggestions']["Ideal"] = terminalmenu_quick_select(sorted(list(character_background_ideal_list)), f'[{character_race}] Select a background suggested roleplaying ideal:')
        
        character_background_bond_list = []
        for background in dnd_backgrounds:
            character_background_bond_list.append(dnd_backgrounds[background]["Roleplaying Suggestions"]["Bond"])
        character_background_bond_list = list(set(character_background_bond_list))
        character.background['Roleplaying Suggestions']["Bond"]  = terminalmenu_quick_select(sorted(list(character_background_bond_list)), f'[{character_race}] Select a background suggested roleplaying ideal:')
        
        character_background_flaw_list = []
        for background in dnd_backgrounds:
            character_background_flaw_list.append(dnd_backgrounds[background]["Roleplaying Suggestions"]["Flaw"])
        character_background_flaw_list = list(set(character_background_flaw_list))
        character.background['Roleplaying Suggestions']["Flaw"]  = terminalmenu_quick_select(sorted(list(character_background_flaw_list)), f'[{character_race}] Select a background suggested roleplaying ideal:')
            
        
    # Level Chart
    character.level_chart = dnd_classes[character_class]["Level Chart"]

    # character.profile['all_armor_proficiencies'] = []
    # character.profile['all_weapon_proficiencies'] = []
    # character.profile['all_tools_proficiencies'] = []
    # character.profile['all_languages'] = list(character.character_race['Proficiencies']['languages']) + list(character.character_class['Proficiencies']['Languages'])


    # Spellcasting
    if character_class == "Barbarian":
        # Not a native spell caster
        character.spells['Cantrips Known'] = "None"
        character.spells['Spells Known'] = "None"


    elif character_class == "Fighter":
        # Not a native spell caster
        character.spells['Cantrips Known'] = "None"
        character.spells['Spells Known'] = "None"


    elif character_class == "Monk":
        # Not a native spell caster
        character.spells['Cantrips Known'] = "None"
        character.spells['Spells Known'] = "None"


    elif character_class == "Rogue":
        # Not a native spell caster
        character.spells['Cantrips Known'] = "None"
        character.spells['Spells Known'] = "None"   


    elif character_class == "Bard":
        spell_levels = ['Cantrips','1st','2nd','3rd','4th','5th','6th','7th','8th','9th']

        character.spells['Cantrips Known'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']
        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Spells Known']
        character.spells['Spells Known']["Slots"] = {}

        for spell_level in spell_levels:
            if spell_level == 'Cantrips':
                
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : f"Can cast {character.spells['Cantrips Known']} known Cantrips unlimiited times",
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)
                
                chosen_temp_list = []
                for each in range(1,character.spells['Cantrips Known'] + 1):
                    choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)

            else:
                if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                    character.spells['Spells Known']["Slots"][spell_level] = {
                        "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                        "Known Spells" : {}
                    }
                    for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                        character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                    chosen_temp_list = []
                    for each in range(1,int(dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level]) + 1):
                        choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


    elif character_class == "Cleric":
        spell_levels = ['Cantrips','1st','2nd','3rd','4th','5th','6th','7th','8th','9th']

        character.spells['Cantrips Known'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']
        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = "Clerics have access to all their spells, but can change them daily with preparation"
        character.spells['Spells Known']["Slots"] = {}

        for spell_level in spell_levels:
            if spell_level == 'Cantrips':
                
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : f"Can cast {character.spells['Cantrips Known']} known Cantrips unlimiited times",
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)
                
                chosen_temp_list = []
                for each in range(1,character.spells['Cantrips Known'] + 1):
                    choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)

            else:
                if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                    character.spells['Spells Known']["Slots"][spell_level] = {
                        "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                        "Known Spells" : {}
                    }
                    for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                        character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                    chosen_temp_list = []
                    for each in range(1,int(dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level]) + 1):
                        choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


    elif character_class == "Druid":
        spell_levels = ['Cantrips','1st','2nd','3rd','4th','5th','6th','7th','8th','9th']

        character.spells['Cantrips Known'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']
        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = "Clerics have access to all their spells, but can change them daily with preparationXXXXXXXXXXXXXXXXXXXXXXXXXX"
        character.spells['Spells Known']["Slots"] = {}

        for spell_level in spell_levels:
            if spell_level == 'Cantrips':
                
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : f"Can cast {character.spells['Cantrips Known']} known Cantrips unlimiited times",
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)
                
                chosen_temp_list = []
                for each in range(1,character.spells['Cantrips Known'] + 1):
                    choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


            else:
                if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                    character.spells['Spells Known']["Slots"][spell_level] = {
                        "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                        "Known Spells" : {}
                    }
                    for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                        character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                    chosen_temp_list = []
                    for each in range(1,int(dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level]) + 1):
                        choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


    elif character_class == "Sorcerer":
        spell_levels = ['Cantrips','1st','2nd','3rd','4th','5th','6th','7th','8th','9th']

        character.spells['Cantrips Known'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']
        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Spells Known']
        character.spells['Spells Known']["Slots"] = {}

        for spell_level in spell_levels:
            if spell_level == 'Cantrips':
                
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : f"Can cast {character.spells['Cantrips Known']} known Cantrips unlimiited times",
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)
                
                chosen_temp_list = []
                for each in range(1,character.spells['Cantrips Known'] + 1):
                    choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


            else:
                if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                    character.spells['Spells Known']["Slots"][spell_level] = {
                        "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                        "Known Spells" : {}
                    }
                    for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                        character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                    chosen_temp_list = []
                    for each in range(1,int(dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level]) + 1):
                        choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


    elif character_class == "Wizard":
        spell_levels = ['Cantrips','1st','2nd','3rd','4th','5th','6th','7th','8th','9th']

        character.spells['Cantrips Known'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']
        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = "Clerics have access to all their spells, but can change them daily with preparationXXXXXXXXXXXXXXXXXXXXXXXXXX"
        character.spells['Spells Known']["Slots"] = {}

        for spell_level in spell_levels:
            if spell_level == 'Cantrips':
                
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : f"Can cast {character.spells['Cantrips Known']} known Cantrips unlimiited times",
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)
                
                chosen_temp_list = []
                for each in range(1,character.spells['Cantrips Known'] + 1):
                    choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)

            else:
                if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                    character.spells['Spells Known']["Slots"][spell_level] = {
                        "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                        "Known Spells" : {}
                    }
                    for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                        character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                    chosen_temp_list = []
                    for each in range(1,int(dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level]) + 1):
                        choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


    elif character_class == "Paladin":
        spell_levels = ['1st','2nd','3rd','4th','5th']

        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = "Clerics have access to all their spells, but can change them daily with preparationXXXXXXXXXXXXXXXXXXXXXXXXXX"
        character.spells['Spells Known']["Slots"] = {}

        character.spells['Cantrips Known'] = "None"
        character.spells['Spells Known']["Slots"]["Cantrips"] = {
            "Able To Cast" : "None",
            "Known Spells" : "None"
        }

        for spell_level in spell_levels:
            if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                chosen_temp_list = []
                for each in range(1,int(dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level]) + 1):
                    choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


    elif character_class == "Ranger":
        spell_levels = ['1st','2nd','3rd','4th','5th']

        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = "Clerics have access to all their spells, but can change them daily with preparationXXXXXXXXXXXXXXXXXXXXXXXXXX"
        character.spells['Spells Known']["Slots"] = {}

        character.spells['Cantrips Known'] = "None"
        character.spells['Spells Known']["Slots"]["Cantrips"] = {
            "Able To Cast" : "None",
            "Known Spells" : "None"
        }

        for spell_level in spell_levels:
            if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                chosen_temp_list = []
                for each in range(1,int(dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level]) + 1):
                    choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


    elif character_class == "Warlock":
        # Warlock's primary ranged spell is Eldritch Blast, which they get for free at level 1
        character.spells["Selected Spells"].append('Eldritch Blast')
        character.spells['Cantrips Known'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']
        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = "Clerics have access to all their spells, but can change them daily with preparationXXXXXXXXXXXXXXXXXXXXXXXXXX"
        character.spells['Spells Known']["Slots"] = {}

        spell_level = 'Cantrips'
        character.spells['Spells Known']["Slots"][spell_level] = {
            "Able To Cast" : f"Can cast {character.spells['Cantrips Known']} known Cantrips unlimiited times",
            "Known Spells" : {}
        }
        for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
            character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)
        
        chosen_temp_list = ['Eldritch Blast']
        for each in range(1,character.spells['Cantrips Known'] + 1):
            choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)

        #This is how many spells a warlock knows at at each level of any given spell level
        # Coincidently, the number of 1st level spells you can ever now is also your total number of known spells...
        # level : [5th, 4th, 3rd, 2nd, 1st]
        # warlock_known_vs_slot_level = {
        #     20 : [12, 14, 15, 15, 15],
        #     19 : [11, 13, 15, 15, 15],
        #     18 : [10, 12, 14, 15, 14],
        #     17 : [ 9, 11, 13, 15, 14],
        #     16 : [ 8, 10, 12, 14, 13],
        #     15 : [ 7,  9, 11, 13, 13],
        #     14 : [ 6,  8, 10, 12, 12],
        #     13 : [ 5,  7,  9, 11, 12],
        #     12 : [ 4,  6,  8, 10, 11],
        #     11 : [ 3,  5,  7,  9, 11],
        #     10 : [ 2,  4,  6,  8, 10],
        #      9 : [ 1,  3,  5,  7, 10],
        #      8 : [ 0,  2,  4,  6,  9],
        #      7 : [ 0,  1,  3,  5,  8],
        #      6 : [ 0,  0,  2,  4,  7],
        #      5 : [ 0,  0,  1,  3,  6],
        #      4 : [ 0,  0,  0,  2,  5],
        #      3 : [ 0,  0,  0,  1,  4],
        #      2 : [ 0,  0,  0,  0,  3],
        #      1 : [ 0,  0,  0,  0,  2],
        # }
        # This dictionary is an even distribution of the spells that a Warlock is able to know per each level - not the max.
        # This is purely used to generate a relatively "balanced" character when auto creating characters.
        # level : [1st, 2nd, 3rd, 4th, 5th]
        warlock_slots_generic_distribution = {
            20 : [ 3,  3,  3,  3,  3],
            19 : [ 3,  3,  3,  3,  3],
            18 : [ 2,  3,  3,  3,  3],
            17 : [ 2,  3,  3,  3,  3],
            16 : [ 2,  2,  3,  3,  3],
            15 : [ 2,  2,  3,  3,  3],
            14 : [ 2,  2,  2,  3,  3],
            13 : [ 2,  2,  2,  3,  3],
            12 : [ 2,  2,  2,  2,  3],
            11 : [ 2,  2,  2,  2,  3],
            10 : [ 2,  2,  2,  2,  2],
             9 : [ 2,  2,  2,  3,  1],
             8 : [ 2,  2,  3,  2,  0],
             7 : [ 2,  2,  3,  1,  0],
             6 : [ 2,  3,  2,  0,  0],
             5 : [ 2,  3,  1,  0,  0],
             4 : [ 3,  2,  0,  0,  0],
             3 : [ 3,  1,  0,  0,  0],
             2 : [ 3,  0,  0,  0,  0],
             1 : [ 2,  0,  0,  0,  0],
        }
        # spells_count_to_learn = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Spells Known'] #ex: returns 6 known for level 5
        for index,spell_index in enumerate(warlock_slots_generic_distribution[character.profile['level']]): #ex: returns 2,3,1,0,0 (for 5th Level)
            if index == 0:
                spell_level = "1st"
            elif index == 1:
                spell_level = "2nd"
            elif index == 2:
                spell_level = "3rd"
            elif index == 3:
                spell_level = "4th"
            elif index == 4:
                spell_level = "5th"

            if spell_index > 0:
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : f"Can cast {dnd_classes[character_class]['Level Chart'][character.profile['level']]['Spell Slots']} from any of their known spells.",
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                warlock_slots_generic_distribution_limit = spell_index # ex: for level 5, [2,3,1,0,0] the first iteration [1st level spells] will have a limit of 2 spells, second iteration [2d level spells] will have 3 spells, etc
                chosen_temp_list = []
                for num in range(1,spell_index + 1):
                    if warlock_slots_generic_distribution_limit > 0:
                        warlock_slots_generic_distribution_limit -= 1                       
                        choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)
                  
                
        print_character(character.spells)

 
    new_roles = {
        'strength' : 0,
        'charisma' : 0,
        'constitution' : 0,
        'dexterity' : 0,
        'wisdom' : 0,
        'intelligence' : 0
    }

    generate_new_roles = generate_attribute_number()
    generate_new_roles = sorted(generate_new_roles, reverse=True)
    # Assigns role values in priority based on that listed in the dnd_classes
    for index, attribute in enumerate(dnd_classes[character_class]['Attribute Priority']):
        new_roles[attribute] = generate_new_roles[index]


    for attribute in character.attributes:
        character.attributes[attribute]['base'] = new_roles[attribute]
        
        try:
            character.attributes[attribute]['race_bonus'] = dnd_races[character_race]['Ability Score Increase'][attribute]
        except:
            character.attributes[attribute]['race_bonus'] = 0

        if attribute == str(dnd_classes[character_class]['Spells']["Spellcasting Modifier"]).lower():
            character.attributes[attribute]["Spellcasting Modifier"] = True
        else:
            character.attributes[attribute]["Spellcasting Modifier"] = False
        
        character.attributes[attribute]['total'] =  character.attributes[attribute]['base'] + character.attributes[attribute]['race_bonus']
        character.attributes[attribute]['modifier'] = (character.attributes[attribute]['total'] - 10) // 2
        
        if attribute.lower() in str(dnd_classes[character_class]["Proficiencies"]["Saving Throws"]).lower():
            character.attributes[attribute]['saving_throw'] = character.attributes[attribute]['modifier'] + character.profile['proficiency bonus']
        else:
            character.attributes[attribute]['saving_throw'] = character.attributes[attribute]['modifier'] #No proficiency bons


    character.capabilities['physical'] = {}
    character.capabilities['physical']['carry capacity'] = character.attributes['strength']['total'] * 15
    character.capabilities['physical']['push pull lift'] = character.attributes['strength']['total'] * 30
    character.capabilities['physical']['speed'] = dnd_races[character_race]['Traits']['Speed']['Ground']
    character.capabilities['physical']['vision'] = dnd_races[character_race]['Traits']['Vision']
    character.capabilities['physical']['dark vision'] = dnd_races[character_race]['Traits']['Vision']['Darkvision']["Possesses"]

    # Passive Perception is added after the skills section, as it's value depends on perception proficiency
    character.capabilities['physical']['passive perception'] = 0



    character.spells["Spellcasting"] = dnd_classes[character_class]['Spells']["Spellcasting"]
    character.spells["Preparation"] = dnd_classes[character_class]['Spells']["Preparation"]
    character.spells["Spellcasting Modifier"] = dnd_classes[character_class]['Spells']["Spellcasting Modifier"]

    if character_class not in non_magic_classes:
        # This needs to be beneath the spells and attributes section
        # Spell Attack Modifier = Your Spellcasting Ability Modifier + Your Proficiency Bonus
        character.spells["Attack Modifier"] = character.attributes[str(dnd_classes[character_class]['Spells']["Spellcasting Modifier"]).lower()]['modifier'] + character.profile['proficiency bonus']

        # Spell Save DC = 8 + Your Spellcasting Ability Modifier + Your Proficiency Bonus
        character.spells["Save DC"] = 8 + character.spells["Attack Modifier"]

    # character.spells['spellcasting focus'] = 'answer' #need to calculate, need to get stat attribtes first




    # Class Features
    # character_feautres = []
    for Level in range(1,character_level + 1):
        for Feature in dnd_classes[character_class]["Level Chart"][Level]["Features"]:
            if Feature == "-":
                pass
            else:
                character.features[Feature] = dnd_classes[character_class]["Features"][Feature]


    # Skills
    character.skills = dnd_skills
    randomly_chosen_skills = choose_random_proficiency_skill(dnd_classes,character_class)
    
    # Assigns proficiency to skills based on the randomly chosen skills list
    for skill in dnd_skills:
        if character.skills[skill]['Related Attribute'] == 'strength':
            character.skills[skill]['total'] = character.attributes['strength']['modifier']
        elif character.skills[skill]['Related Attribute'] == 'dexterity':
            character.skills[skill]['total'] = character.attributes['dexterity']['modifier']
        elif character.skills[skill]['Related Attribute'] == 'constitution':
            character.skills[skill]['total'] = character.attributes['constitution']['modifier']
        elif character.skills[skill]['Related Attribute'] == 'intelligence':
            character.skills[skill]['total'] = character.attributes['intelligence']['modifier']
        elif character.skills[skill]['Related Attribute'] == 'wisdom':
            character.skills[skill]['total'] = character.attributes['wisdom']['modifier']
        elif character.skills[skill]['Related Attribute'] == 'charisma':
            character.skills[skill]['total'] = character.attributes['charisma']['modifier']

        # Randomly adds proficiency to a skill if it is in the randomly chosen proficiency skills list
        for choose_skill in randomly_chosen_skills: 
            if skill == choose_skill:
                character.skills[skill]['proficiency'] = True
                character.skills[skill]['total'] += character.profile['proficiency bonus']

        # Calculates passive perception
        if skill == 'perception':
            if character.skills[skill]['proficiency'] == True:
                character.capabilities['physical']['passive perception'] = 10 + character.skills['perception']['total'] + character.profile['proficiency bonus']
            else:
                character.capabilities['physical']['passive perception'] = 10 + character.skills['perception']['total']





    character.capabilities['combat'] = {}
    character.capabilities['combat']['initiative'] = {}
    character.capabilities['combat']['initiative']['normal'] = character.attributes['dexterity']['modifier']
    character.capabilities['combat']['initiative']['temporary'] = 0 #placeholder
    character.capabilities['combat']['initiative']['total'] = character.capabilities['combat']['initiative']['normal'] + character.capabilities['combat']['initiative']['temporary']
    character.capabilities['combat']['armor_class'] = 10 + character.attributes['dexterity']['modifier']
    character.capabilities['combat']['hit_points'] = {}
    character.capabilities['combat']['hit_points']['damage_resistence'] = 0
    character.capabilities['combat']['hit_points']['false_life'] = 0
    character.capabilities['combat']['hit_points']['temp_hit_points'] = 0


    character_hp_calc_total = 0
    # add full level 1 hit die hp
    character_hp_calc_total += int(character.character_class["Hit Die"].split('d')[1]) + int(character.attributes['constitution']['modifier'])
    for level in range(2,int(character.profile['level'] + 1)): # starts at level 2, because level 1 is added in full up above
        val = random.randint(1, int(character.character_class["Hit Die"].split('d')[1])) + int(character.attributes['constitution']['modifier'])
        character_hp_calc_total += val
    character.capabilities['combat']['hit_points']['total'] = character_hp_calc_total
    character.capabilities['combat']['hit_points']['current'] = character.capabilities['combat']['hit_points']['total']

# 'combat' : {
#     'initiative' : {
#         'modifier' : 0,
#         'total' : 0
#     },
#     'armor_class' : {
#         'temporary' : 0,
#         'total' : 0
#     },
#     'hit_points' : {
#         'damage_resistance' : 0,
#         'false_life' : 0,
#         'temp_hit_points' : 0,
#         'total' : 0
#     },
# }



    for i in range(1, random.randint(1,6)):
        character.items.append(generate_random_item(item_list))

    for i in range(1, random.randint(1,4)):
        ##### old way, when i just used a weapons_list
        # generated_weapon = generate_random_weapon(weapon_list)
        # character.weapons[generated_weapon['name']] = {}
        # character.weapons[generated_weapon['name']]['description'] = generated_weapon['description']
        # character.weapons[generated_weapon['name']]['damage_amount'] = generated_weapon['damage_amount']
        # character.weapons[generated_weapon['name']]['weapon_type'] = generated_weapon['damage_type']
        # character.weapons[generated_weapon['name']]['attack_type'] = generated_weapon['attack_type']
        # character.weapons[generated_weapon['name']]['attack_bonus'] = generated_weapon['attack_bonus']
        # character.weapons[generated_weapon['name']]['is_ranged'] = generated_weapon['is_ranged']
        # character.weapons[generated_weapon['name']]['range_low'] = generated_weapon['range_low']
        # character.weapons[generated_weapon['name']]['range_high'] = generated_weapon['range_high']
        # character.weapons[generated_weapon['name']]['amount'] = generated_weapon['amount']
        # character.weapons[generated_weapon['name']]['rarity'] = generated_weapon['rarity']
        # character.weapons[generated_weapon['name']]['material_components'] = generated_weapon['material_components']
        # character.weapons[generated_weapon['name']]['cost'] = generated_weapon['cost']
        # character.weapons[generated_weapon['name']]['weight'] = generated_weapon['weight']
        # character.weapons[generated_weapon['name']]['mundane_properties'] = generated_weapon['mundane_properties']
        # character.weapons[generated_weapon['name']]['is_magical'] = generated_weapon['is_magical']
        # character.weapons[generated_weapon['name']]['magical_type'] = generated_weapon['magical_type']

        #### new way, basing it off actual dnd_weapons list
        generated_weapon = random.choice(list(dnd_weapons.keys()))
        character.weapons[generated_weapon] = dnd_weapons.get(generated_weapon)


    create_chatgpt_dall_e_image = terminalmenu_quick_select(['No','Yes'], f"[{character_race}] Have ChatGTP use DALL-E to generate a character image? ")
    if create_chatgpt_dall_e_image == 'No':
        pass
    elif create_chatgpt_dall_e_image == 'Yes':
        while True:
            verify = input(f"Let's verify this request as it costs money. Type 'yes' to submit, 'no' to abort. ")
            if verify == 'yes':
                image_size = terminalmenu_quick_select(['1024x1024', '1024x1792', '1792x1024'], f'[{character_race}] Select an image size:')
                image_style = terminalmenu_quick_select(['Abstract Art','Anime', 'Cartoon', 'Impressionism', 'Oil Painting', 'Pixel Art', 'Realistic', 'Sketch ', 'Surrealism','Watercolor'], f'[{character_race}] Select an image style:')
                dall_e_model = terminalmenu_quick_select(['dall-e-2','dall-e-3'], f'[{character_race}] Select an DALLE-E modle:')
                if dall_e_model == 'dall-e-2':
                    number_of_images = terminalmenu_quick_select([1,2,3,4,5,6,7,8,9,10], f'[{character_race}] DALL-E 2 supports mulipli images:')
                else:
                    number_of_images = 1


# from openai import OpenAI
# client = OpenAI()

# response = client.images.create_variation(
#   image=open("image_edit_original.png", "rb"),
#   n=2,
#   size="1024x1024"
# )

# image_url = response.data[0].url                



                description = description=character.description.copy()
                del description['race']
                del description['class']
                del description['gender']
                del description['age']
                # del description['voice']
                # del description['mannerisms']
                # del description['personality']

                generate_character_image(
                    description=description, 
                    character_race=character_race, 
                    character_class=character_class, 
                    character_name=character.profile['name']['full'],
                    character_gender=character.description['gender'],
                    character_age=character.description['age'],
                    background_name=character.background['Name'],
                    background_features=character.background['Features'],
                    background_equipment=character.background['Equipment'],
                    image_style=image_style, 
                    image_size=image_size,
                    dall_e_model=dall_e_model,
                    number_of_images=number_of_images,
                )
                break
            elif verify == 'no':
                break
            else:
                print(f"Invalid input. Type in exactly 'yes' or 'no' to proceed.")

    return character



# def display_character(characters):
#     # Print Character to screen
#     for index, character in enumerate(characters):
#         print(f"==================================================")
#         print(f"Character #{index + 1}")
#         print(f"==================================================")

#         print(f"Profile :")
#         print_character(character.profile)

#         print(f"Race :")
#         print_character(character.character_race)

#         print(f"Class :")
#         print_character(character.character_class)

#         print(f"Level Chart :")
#         print_character(character.level_chart)

#         print(f"Description :")
#         print_character(character.description)

#         print(f"Background :")
#         print_character(character.background)

#         print(f"Attributes :")
#         print_character(character.attributes)

#         print(f"Capabilties :")
#         print_character(character.capabilities)

#         print(f"Skills :")
#         print_character(character.skills)

#         print(f"Features :")
#         print_character(character.features)

#         print(f"Money :")
#         print_character(character.items)

#         print(f"Items :")
#         print_inventory(character.items, 'Items')

#         print(f"Armor :")
#         print_inventory(character.armor, 'Armor')

#         print(f"Weapons :")
#         print_character(character.weapons)

#         print(f"Combat :")
#         print_character(character.combat)

#         print(f"Spells :")
#         print_character(character.spells)

