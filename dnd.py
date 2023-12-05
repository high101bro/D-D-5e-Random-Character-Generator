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

import random
import numpy as np
from dnd_lists import *
from dnd_races import *
from dnd_classes import *
from dnd_backgrounds import *

debug = []

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
item_list = [generate_item_list() for _ in range(10)]


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

# Generate 10 unique weapons with all specified properties
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
        self.spells = {}
        self.items = []
        self.weapons = []


padding_value = 35

def customize_character(dictionary, spaces=2):
    try:
        for key, value in dictionary.items():
            if isinstance(value, dict):
                print(f"{' ' * spaces}{key}:")
                print_character(value, spaces + 2)
            else:
                padding = padding_value - spaces
                characters[1].profile[key] = input(f"{' ' * spaces}{f'{key:<{padding}}'} : ")
    except:
        pass


def print_character(dictionary, spaces=2):
    try:
        for key, value in dictionary.items():
            if isinstance(value, dict):  # Check if value is a nested dictionary
                print(f"{' ' * spaces}{key} :")
                print_character(value, spaces + 2)  # recursively call the function to handle nested dictionary
            else:
                padding = padding_value - spaces
                print(f"{' ' * spaces}{f'{key:<{padding}}'} : {value}")  # print key-value pair if value is not a nested dictionary
    except:
        print(f"{' ' * spaces}None")


def print_inventory(dictionary, name):
    for index, item in enumerate(dictionary):
        print(f"  {name} #{index + 1}:")
        for value in item.keys():
            print(f"    {f'{value:<{padding_value - 4}}'} : {item[value]}")


def generate_random_item():
    random_item = random.choice(item_list)
    return random_item


def generate_random_weapon():
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


character_number = int(input(f"Enter number of characters to generate: "))
character_level = int(input(f"Enter character level [1-20]: "))
character_race = input(f"Enter human: ")
character_class = input(f"Enter paladin: ")

characters = []
for _ in range(character_number):
    character = Character()
    characters.append(character)


# # Create manual character
# characters[0].profile['name']['first'] = 'Gallows'
# characters[0].profile['name']['last'] = 'of the Trees'
# characters[0].items.append(generate_random_item())
# characters[0].items.append({
#         "name": "Ring of Fortune",
#         "owner": "Tiefling Warlock",
#         "type": "Potion",
#         "amount": "1",
#         "rarity": "Uncommon",
#         "material_components": "Various",
#         "cost": "500 gp",
#         "weight": "4 lb",
#         "mundane_properties": ['Ancient'],
#         "is_magical": True,
#         "magical_type": "Cursed",
#         "magical_properties": [None],
#         "description": 'Covered in strange runes and symbols',
#         "notes": "This ring was found in a well"
# })
# characters[0].weapons.append(generate_random_weapon())
# characters[0].weapons.append({
#     "name" : "Flame Tongue Sword",
#     "damage_amount" : "1d8",
#     "damage_type" : "Bludgeoning",
#     "weapon_type" : "Martial",
#     "attack_type" : "Melee",
#     "attack_bonus" : "+1",
#     "is_ranged" : "False",
#     "range_low" : "None",
#     "range_high" : "None",
#     "owner" : "Halfling Rouge",
#     "amount" : "1",
#     "rarity" : "Common",
#     "material_components" : "Various",
#     "cost" : "100 gp",
#     "weight" : "10 lb",
#     "mundane_properties" : "['Heavy']",
#     "is_magical" : "False",
#     "magical_type" : "None",
#     "magical_properties" : "[]",
#     "description" : "Covered in strange runes and symbols",
#     "notes" : "This sword was pass down to you from your father"
# })


# Create random character
for character in characters:
    character.profile['name'] = {}
    character.profile['name']['first'] = random.choice(first_names)
    character.profile['name']['last'] = random.choice(last_names)
    character.profile['level'] = character_level
    character.profile['proficiency bonus'] = dnd_proficiency_bonus.get(character_level, '1')
    character.profile['experience'] = dnd_levels_exp.get(character_level, '1')    

    character.profile['race'] = {}
    # if character_race.lower() == 'human':
    character.profile['race']['name'] = 'Human'    
    # else:
    #     character.profile['race']['name'] = random.choice(list(dnd_races.keys()))
    character_race = character.profile['race']['name']
    character.profile['race'] = dnd_races[character_race]

    character.profile['class'] = {}
    # if character_class.lower() == 'paladin':
    character.profile['class']['name'] = 'Paladin'
    # else:
    #     character.profile['class']['name'] = random.choice(list(dnd_classes.keys()))
    character_class = character.profile['class']['name']


    character.profile['class'] = dnd_classes[character_class]
 
    character.profile['background'] = {}
    character.profile['background']['name'] = random.choice(list(dnd_backgrounds.keys()))
    character.profile['background'] = dnd_backgrounds[character.profile['background']['name']]

    
    character.profile['traits'] = {}
    character.profile['traits']['personality'] = []
    character.profile['traits']['feats'] = []
    character.profile['traits']['ideals'] = []
    character.profile['traits']['bonds'] = []
    character.profile['traits']['flaws'] = []

    character.profile['alignment'] = random.choice(list(dnd_alignments))

    # probably not needed, it really just duplicates the info
    # character.profile['all_armor_proficiencies'] = []
    # character.profile['all_weapon_proficiencies'] = []
    # character.profile['all_tools_proficiencies'] = []
    # character.profile['all_languages'] = list(character.profile['race']['Proficiencies']['languages']) + list(character.profile['class']['Proficiencies']['Languages'])


    #!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!
    # character.spells['attack modifier'] = 'answer' #need to calculate, need to get stat attribtes first
    # character.spells['save dc'] = 0 #need to calculate, need to get stat attribtes first
    # character.spells['known'] = 0 #need to script cal autogen
    # character.spells['prepared'] = 0 #need to script cal autogen
    # character.spells['spellcasting ability'] = 'answer' #need to calculate, need to get stat attribtes first
    # character.spells['spellcasting focus'] = 'answer' #need to calculate, need to get stat attribtes first
    #!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!

    if character_class != 'Paladin' and character_class != 'Ranger' :
        character.spells['number known'] = \
        dnd_classes[character_class]['Level Chart'][character.profile['level']]['1st Level Spell Slots'],
        dnd_classes[character_class]['Level Chart'][character.profile['level']]['2nd Level Spell Slots'],
        dnd_classes[character_class]['Level Chart'][character.profile['level']]['3rd Level Spell Slots'],
        dnd_classes[character_class]['Level Chart'][character.profile['level']]['4th Level Spell Slots'],
        dnd_classes[character_class]['Level Chart'][character.profile['level']]['5th Level Spell Slots'],
        dnd_classes[character_class]['Level Chart'][character.profile['level']]['6th Level Spell Slots'],
        dnd_classes[character_class]['Level Chart'][character.profile['level']]['7th Level Spell Slots'],
        dnd_classes[character_class]['Level Chart'][character.profile['level']]['8th Level Spell Slots'],
        dnd_classes[character_class]['Level Chart'][character.profile['level']]['9th Level Spell Slots']
    else:
        dnd_classes[character_class]['Level Chart'][character.profile['level']]['1st Level Spell Slots'],
        dnd_classes[character_class]['Level Chart'][character.profile['level']]['2nd Level Spell Slots'],
        dnd_classes[character_class]['Level Chart'][character.profile['level']]['3rd Level Spell Slots'],
        dnd_classes[character_class]['Level Chart'][character.profile['level']]['4th Level Spell Slots'],
        dnd_classes[character_class]['Level Chart'][character.profile['level']]['5th Level Spell Slots']

    character.spells['slots'] = {}
    
    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['1st Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['1st Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']['Available']['1st Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['1st Level Spell Slots']
            }
    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['2nd Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['2nd Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']['Available']['2nd Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['2nd Level Spell Slots']
            }
    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['3rd Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['3rd Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']['Available']['3rd Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['3rd Level Spell Slots']
            }

    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['4th Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['4th Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']['Available']['4th Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['4th Level Spell Slots']
            }

    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['5th Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['5th Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']['Available']['5th Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['5th Level Spell Slots']
            }

    if character_class != 'Paladin' and character_class != 'Ranger' :
        if dnd_classes[character_class]['Level Chart'][character.profile['level']]['6th Level Spell Slots'] != '-':
            character.spells['slots']['6th Level'] = dnd_classes[character_class]['Spells']['Available']['6th Level']

        if dnd_classes[character_class]['Level Chart'][character.profile['level']]['7th Level Spell Slots'] != '-':
            character.spells['slots']['7th Level'] = dnd_classes[character_class]['Spells']['Available']['7th Level']

        if dnd_classes[character_class]['Level Chart'][character.profile['level']]['8th Level Spell Slots'] != '-':
            character.spells['slots']['8th Level'] = dnd_classes[character_class]['Spells']['Available']['8th Level']

        if dnd_classes[character_class]['Level Chart'][character.profile['level']]['9th Level Spell Slots'] != '-':
            character.spells['slots']['9th Level'] = dnd_classes[character_class]['Spells']['Available']['9th Level']

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

        if attribute == str(dnd_classes[character_class]['Features']["Proficiencies"]["Spellcasting Modifier"]).lower():
            character.capabilities['attributes'][attribute]['spellcasting modifier'] = True
        else:
            character.capabilities['attributes'][attribute]['spellcasting modifier'] = False
        character.capabilities['attributes'][attribute]['total'] =  character.capabilities['attributes'][attribute]['base'] + character.capabilities['attributes'][attribute]['race_bonus']
        character.capabilities['attributes'][attribute]['modifier'] = (character.capabilities['attributes'][attribute]['total'] - 10) // 2
        for saving_throw in dnd_classes[character_class]['Features']["Proficiencies"]["Saving Throws"]:
            if attribute in str(saving_throw).lower():
                character.capabilities['attributes'][attribute]['saving_throw'] = character.capabilities['attributes'][attribute]['modifier'] + character.profile['proficiency bonus']


    # character.capabilities['physical'] = {}
    # character.capabilities['physical']['carry_capacity'] = character.capabilities['attributes']['strength']['total'] * 15
    # character.capabilities['physical']['push_pull_lift'] = character.capabilities['attributes']['strength']['total'] * 30
    # character.capabilities['physical']['speed'] = dnd_races[character_race]['Traits']['Speed']['Ground']
    # character.capabilities['physical']['vision'] = dnd_races[character_race]['Vision']
    # character.capabilities['physical']['dark_vision'] = dnd_races[character_race]['Dark Vision']
    # character.capabilities['physical']['passive_perception'] = 10 + character.capabilities['skills']['perception']['total']

# 'physical' : {
#     'carry_capacity' : 0,
#     'push_pull_lift' : 0,
#     'speed' : 0,
#     'vision' : None,
#     'dark_vision' : 0,
#     'passive_perception' : 0
# },




    character.capabilities['skills'] = dnd_skills
    def choose_random_proficiency_skill():
        randomly_chosen_proficiency_skills = []
        class_proficiency_choices = list(dnd_classes[character_class]['Features']["Proficiencies"]["Skills"]["Choose From"])
        for i in range(0, int(dnd_classes[character_class]['Features']["Proficiencies"]["Skills"]["Choose Number"])):
            randomly_chosen_skill = random.choice(class_proficiency_choices)
            if randomly_chosen_skill not in randomly_chosen_proficiency_skills:
                randomly_chosen_proficiency_skills.append(randomly_chosen_skill)
                class_proficiency_choices.remove(randomly_chosen_skill)
        return randomly_chosen_proficiency_skills


    randomly_chosen_skills = choose_random_proficiency_skill()
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

        for choose_skill in randomly_chosen_skills: 
            if skill == choose_skill:
                character.capabilities['skills'][skill]['proficiency'] = True
                character.capabilities['skills'][skill]['total'] += character.profile['proficiency bonus']

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
        character.items.append(generate_random_item())
    for i in range(1, random.randint(1,4)):
        character.weapons.append(generate_random_weapon())



# Print Character to screen
for index, character in enumerate(characters):
    print(f"==================================================")
    print(f"Character #{index + 1}")
    print(f"==================================================")
    print(f"Profile :")
    print_character(character.profile)

    print(f"Weapons :")
    print_inventory(character.weapons, 'Weapon')

    print(f"Items :")
    print_inventory(character.items, 'Item')

    print(f"Spells :")
    print_character(character.spells)

    print(f"Capabilities :")
    print_character(character.capabilities)

print(
    debug
)


