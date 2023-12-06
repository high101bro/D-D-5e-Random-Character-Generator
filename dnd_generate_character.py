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
#         'money' : {
#             'cp' : 0,
#             'sp' : 0,
#             'ep' : 0,
#             'gp' : 0,
#             'pp' : 0
#         }
#     },
# }
# print(character)

import random, os, datetime
from dnd_lists import *
from dnd_races import *
from dnd_classes import *
from dnd_backgrounds import *
from dnd_random_generation import *
from dnd_character_print import *


# Clear the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

debug = []

item_list = [generate_item_list() for _ in range(10)]
weapon_list = [generate_weapon_list() for _ in range(10)]


class Character():
    def __init__(self):
        self.profile = {}
        #         'description' : {
        #             'age' : 0,
        #             'height' : 0,
        #             'weight' : 0,
        #             'skin_color' : None,
        #             'description' : None,
        #             'eye_color' : None,
        #             'ear_type' : None

        #         'traits' : {
        #             'personality' : [],
        #             'feats' : [],
        #             'ideals' : [],
        #             'bonds' : [],
        #             'flaws' : []
        #         },
        #         'all_proficiencies' : [],
        #         'all_languages' : []

        self.capabilities = {}
        self.spells = {
            "spellcasting" : "",
            "preparation" : "",
            "spellcasting modifier" : "",
            "attack modifier" : 0,
            "save dc" : 0,
            'slots' : {}
        }
        self.items = []
        self.weapons = []


# Create random character
def generate_characters(character, character_number, character_level=1, character_race='Human', character_class='Fighter'):

    character.profile['character number'] = character_number
    character.profile['created'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%S"))
    character.profile['name'] = {}
    character.profile['name']['first'] = random.choice(first_names)
    character.profile['name']['last'] = random.choice(last_names)
    character.profile['level'] = character_level
    character.profile['proficiency bonus'] = dnd_proficiency_bonus.get(character_level, '1')
    character.profile['experience'] = dnd_levels_exp.get(character_level, '1')    


    character.profile['race'] = {}
    character.profile['race'] = dnd_races[character_race]
    debug.append(character.profile['race']['Name'])


    character.profile['class'] = {}
    character.profile['class']['name'] = character_class
    debug.append(character.profile['class']['name'])


    # character.profile['class'] = dnd_classes[character_class] # imports everything
    character.profile['class']["ASCII Art"] = dnd_classes[character_class]["ASCII Art"]
    character.profile['class']["Name"] = dnd_classes[character_class]["Name"]
    character.profile['class']["Description"] = dnd_classes[character_class]["Description"]
    character.profile['class']["Level Chart"] = {}
    character.profile['class']["Level Chart"][character.profile['level']] = dnd_classes[character_class]["Level Chart"][character.profile['level']]
    character.profile['class']["Features"] = dnd_classes[character_class]["Features"]
    character.profile['class']["Attribute Priority"] = dnd_classes[character_class]["Attribute Priority"]
    character.profile['class']["Spells"] = dnd_classes[character_class]["Spells"]


    character.profile['background'] = {}
    character.profile['background']['name'] = random.choice(list(dnd_backgrounds.keys()))
    character.profile['background'] = dnd_backgrounds[character.profile['background']['name']]

    character.profile['alignment'] = random.choice(list(dnd_alignments))

    # probably not needed, it really just duplicates the info
    # character.profile['all_armor_proficiencies'] = []
    # character.profile['all_weapon_proficiencies'] = []
    # character.profile['all_tools_proficiencies'] = []
    # character.profile['all_languages'] = list(character.profile['race']['Proficiencies']['languages']) + list(character.profile['class']['Proficiencies']['Languages'])


    # # Adds spell slots by class
    # if character_class != 'Paladin' and character_class != 'Ranger' :
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['1st Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['2nd Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['3rd Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['4th Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['5th Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['6th Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['7th Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['8th Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['9th Level Spell Slots']
    # else:
    #     # character.profile['class']["Level Chart"][character.profile['level']] = dnd_classes[character_class]["Level Chart"][character.profile['level']]

    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['1st Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['2nd Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['3rd Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['4th Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['5th Level Spell Slots']

    character.spells['slots'] = {}
    
    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['1st Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['1st Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']["All Class Spells"]['1st Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['1st Level Spell Slots']
            }
    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['2nd Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['2nd Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']["All Class Spells"]['2nd Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['2nd Level Spell Slots']
            }
    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['3rd Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['3rd Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']["All Class Spells"]['3rd Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['3rd Level Spell Slots']
            }

    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['4th Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['4th Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']["All Class Spells"]['4th Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['4th Level Spell Slots']
            }

    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['5th Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['5th Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']["All Class Spells"]['5th Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['5th Level Spell Slots']
            }

    if character_class != 'Paladin' and character_class != 'Ranger' :
        if dnd_classes[character_class]['Level Chart'][character.profile['level']]['6th Level Spell Slots'] != '-':
            character.spells['slots']['6th Level'] = dnd_classes[character_class]['Spells']["All Class Spells"]['6th Level']

        if dnd_classes[character_class]['Level Chart'][character.profile['level']]['7th Level Spell Slots'] != '-':
            character.spells['slots']['7th Level'] = dnd_classes[character_class]['Spells']["All Class Spells"]['7th Level']

        if dnd_classes[character_class]['Level Chart'][character.profile['level']]['8th Level Spell Slots'] != '-':
            character.spells['slots']['8th Level'] = dnd_classes[character_class]['Spells']["All Class Spells"]['8th Level']

        if dnd_classes[character_class]['Level Chart'][character.profile['level']]['9th Level Spell Slots'] != '-':
            character.spells['slots']['9th Level'] = dnd_classes[character_class]['Spells']["All Class Spells"]['9th Level']










    character.capabilities['attributes'] = {
        'strength' : {},
        'dexterity' : {},
        'constitution' : {},
        'intelligence' : {},
        'wisdom' : {},
        'charisma' : {}
    }

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


    for attribute in character.capabilities['attributes']:
        character.capabilities['attributes'][attribute]['base'] = new_roles[attribute]
        
        try:
            character.capabilities['attributes'][attribute]['race_bonus'] = dnd_races[character_race]['Ability Score Increase'][attribute]
        except:
            character.capabilities['attributes'][attribute]['race_bonus'] = 0

        if attribute == str(dnd_classes[character_class]['Spells']["Spellcasting Modifier"]).lower():
            character.capabilities['attributes'][attribute]['spellcasting modifier'] = True
        else:
            character.capabilities['attributes'][attribute]['spellcasting modifier'] = False
        character.capabilities['attributes'][attribute]['total'] =  character.capabilities['attributes'][attribute]['base'] + character.capabilities['attributes'][attribute]['race_bonus']
        character.capabilities['attributes'][attribute]['modifier'] = (character.capabilities['attributes'][attribute]['total'] - 10) // 2
        for saving_throw in dnd_classes[character_class]["Proficiencies"]["Saving Throws"]:
            if attribute in str(saving_throw).lower():
                character.capabilities['attributes'][attribute]['saving_throw'] = character.capabilities['attributes'][attribute]['modifier'] + character.profile['proficiency bonus']


    character.capabilities['physical'] = {}
    character.capabilities['physical']['carry capacity'] = character.capabilities['attributes']['strength']['total'] * 15
    character.capabilities['physical']['push pull lift'] = character.capabilities['attributes']['strength']['total'] * 30
    character.capabilities['physical']['speed'] = dnd_races[character_race]['Traits']['Speed']['Ground']
    character.capabilities['physical']['vision'] = dnd_races[character_race]['Traits']['Vision']
    character.capabilities['physical']['dark vision'] = dnd_races[character_race]['Traits']['Vision']['Darkvision']["Possesses"]

    # Passive Perception is added after the skills section, as it's value depends on perception proficiency
    character.capabilities['physical']['passive perception'] = 0



    character.spells['spellcasting'] = dnd_classes[character_class]['Spells']["Spellcasting"]
    character.spells['preparation'] = dnd_classes[character_class]['Spells']["Preparation"]
    character.spells['spellcasting modifier'] = dnd_classes[character_class]['Spells']["Spellcasting Modifier"]

    # This needs to be beneath the spells and attributes section
    # Spell Attack Modifier = Your Spellcasting Ability Modifier + Your Proficiency Bonus
    character.spells['attack modifier'] = character.capabilities['attributes'][str(dnd_classes[character_class]['Spells']["Spellcasting Modifier"]).lower()]['modifier'] + character.profile['proficiency bonus']

    # Spell Save DC = 8 + Your Spellcasting Ability Modifier + Your Proficiency Bonus
    character.spells['save dc'] = 8 + character.spells['attack modifier']

    # character.spells['spellcasting focus'] = 'answer' #need to calculate, need to get stat attribtes first
    #!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!



    character.capabilities['skills'] = dnd_skills

    
    randomly_chosen_skills = choose_random_proficiency_skill(dnd_classes,character_class)
    
    # Assigns proficiency to skills based on the randomly chosen skills list
    for skill in dnd_skills:
        if character.capabilities['skills'][skill]['related attribute'] == 'strength':
            character.capabilities['skills'][skill]['total'] = character.capabilities['attributes']['strength']['modifier']
        elif character.capabilities['skills'][skill]['related attribute'] == 'dexterity':
            character.capabilities['skills'][skill]['total'] = character.capabilities['attributes']['dexterity']['modifier']
        elif character.capabilities['skills'][skill]['related attribute'] == 'constitution':
            character.capabilities['skills'][skill]['total'] = character.capabilities['attributes']['constitution']['modifier']
        elif character.capabilities['skills'][skill]['related attribute'] == 'intelligence':
            character.capabilities['skills'][skill]['total'] = character.capabilities['attributes']['intelligence']['modifier']
        elif character.capabilities['skills'][skill]['related attribute'] == 'wisdom':
            character.capabilities['skills'][skill]['total'] = character.capabilities['attributes']['wisdom']['modifier']
        elif character.capabilities['skills'][skill]['related attribute'] == 'charisma':
            character.capabilities['skills'][skill]['total'] = character.capabilities['attributes']['charisma']['modifier']

        # Randomly adds proficiency to a skill if it is in the randomly chosen proficiency skills list
        for choose_skill in randomly_chosen_skills: 
            if skill == choose_skill:
                character.capabilities['skills'][skill]['proficiency'] = True
                character.capabilities['skills'][skill]['total'] += character.profile['proficiency bonus']

        # Calculates passive perception
        if skill == 'perception':
            if character.capabilities['skills'][skill]['proficiency'] == True:
                character.capabilities['physical']['passive perception'] = 10 + character.capabilities['skills']['perception']['total'] + character.profile['proficiency bonus']
            else:
                character.capabilities['physical']['passive perception'] = 10 + character.capabilities['skills']['perception']['total']





    character.capabilities['combat'] = {}
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
        character.weapons.append(generate_random_weapon(weapon_list))

    return character



def display_character(characters):
    # Print Character to screen
    for index, character in enumerate(characters):
        print(f"==================================================")
        print(f"Character #{index + 1}")
        print(f"==================================================")
        print(f"Profile :")
        print_character(character.profile)

        print(f"Capabilities :")
        print_character(character.capabilities)

        print(f"Weapons :")
        print_inventory(character.weapons, 'Weapon')

        print(f"Items :")
        print_inventory(character.items, 'Item')

        print(f"Spells :")
        print_character(character.spells)


    print(
        'Debug :', debug
    )


