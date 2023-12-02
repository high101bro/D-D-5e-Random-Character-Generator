#! /usr/bin/env python3

# character = {
#     'profile' : {
        # 'name' : {
        #     'first' : "",
        #     'last' : ""
#     'spells' : {
#         'attack_modifier' : 0,
#         'save_dc' : 0,
#         'number_known' : {
#             'level_0' : 0,
#             'level_1' : 0,
#             'level_2' : 0,
#             'level_3' : 0,
#             'level_4' : 0,
#             'level_5' : 0,
#             'level_6' : 0,
#             'level_7' : 0,
#             'level_8' : 0,
#             'level_9' : 0
#         },
#         'slots' : {
#             'level_0' : 0,
#             'level_1' : 0,
#             'level_2' : 0,
#             'level_3' : 0,
#             'level_4' : 0,
#             'level_5' : 0,
#             'level_6' : 0,
#             'level_7' : 0,
#             'level_8' : 0,
#             'level_9' : 0
#         },
#         'known' : {
#             'name': "",
#             'level' : 0,
#             'damage' : 0,
#             'type' : "",
#             'casting_time' : "",
#             'range' : 0,
#             'components' : [],
#             'duration' : 0,
#             'description' : ""
#         },
#         'availabe' : [],
#     },
#     'items' : {
#         'weapons' : {
#             'name' : "",
#             'class' : 0,
#             'type' : "",
#             'damage' : 0,
#             'damage_type' : "",
#             'attack_bonus' : 0,
#             'range_low' : 0,
#             'range_high' : 0,
#             'properties' : [],
#             'description' : ""
#         },
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

# List of random names
first_names = ["Grog", "Vax'ildan", "Keyleth", "Percy", "Scanlan", "Vex'ahlia", "Pike", "Tiberius", "Pike", "Percival"]
last_names = ["Strongjaw", "De Rolo", "of the Air Ashari", "Fredrickstein", "Shorthalt", "of Syngorn", "Trickfoot", "Stormwind", "Trickfoot", "de Rolo"]
# name_list = []
# for i in range(10):
#     full_name = {
#         "first": random.choice(first_names),
#         "last": random.choice(last_names)
#     }
#     name_list.append(full_name)

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
        self.profile = {
            'name': {
                'first' : None,
                'last' : None
            },
            'level' : 0,
            'proficiency_bonus' : 0,
            'experience' : 0,
            'race' : {
                'name' : None,
                'bonuses' : [],
                'proficiencies' : [],
                'languages' : [],
                'features' : []
            },
            'class' : {
                'name' : None,
                'level' : 0,
                'bonuses' : [],
                'proficiencies' : [],
                'languages' : [],
                'features' : []
            },
            'background' : {
                'name' : None,
                'features' : [],
                'description' : None      
            },
            'traits' : {
                'personality' : [],
                'feats' : [],
                'ideals' : [],
                'bonds' : [],
                'flaws' : []
            },
            'moral_alignment' : None,
            'ethical_alignment' : None,
            'all_proficiencies' : [],
            'all_languages' : []
        }            
        self.items = []
        self.weapons = []
        self.physical = {
            'description' : {
                'age' : 0,
                'height' : 0,
                'weight' : 0,
                'skin_color' : None,
                'description' : None,
                'eye_color' : None,
                'ear_type' : None
            },
            'capabilities' : {
                'carry_capacity' : 0,
                'push_pull_lift' : 0,
                'speed' : 0,
                'vision' : None,
                'dark_vision' : 0,
                'passive_perception' : 0
            },
            'attributes' : {
                'strength' : {
                    'base' : 0,
                    'race_bonus' : 0,
                    'class_proficiency' : 0,
                    'total' : 0,
                    'modifier' : 0,
                    'saving_throw' : 0
                },
                'dexterity' : {
                    'base' : 0,
                    'race_bonus' : 0,
                    'class_proficiency' : 0,
                    'total' : 0,
                    'modifier' : 0,
                    'saving_throw' : 0
                },
                'constitution' : {
                    'base' : 0,
                    'race_bonus' : 0,
                    'class_proficiency' : 0,
                    'total' : 0,
                    'modifier' : 0,
                    'saving_throw' : 0
                },
                'inteligence' : {
                    'base' : 0,
                    'race_bonus' : 0,
                    'class_proficiency' : 0,
                    'total' : 0,
                    'modifier' : 0,
                    'saving_throw' : 0
                },
                'wisdom' : {
                    'base' : 0,
                    'race_bonus' : 0,
                    'class_proficiency' : 0,
                    'total' : 0,
                    'modifier' : 0,
                    'saving_throw' : 0
                },
                'charisma' : {
                    'base' : 0,
                    'race_bonus' : 0,
                    'class_proficiency' : 0,
                    'total' : 0,
                    'modifier' : 0,
                    'saving_throw' : 0
                },
            },
            'skills' : {
                'acrobatics' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'animal_handling' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'arcana' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'athletics' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'deception' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'history' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'insight' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'intimidation' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'investigation' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'medicine' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'nature' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'perception' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'performance' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'persuasion' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'religion' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'sleight_of_hand' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'stealth' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                },
                'survival' : {
                    'related_attribute' : None,
                    'proficiency' : False,
                    'total' : 0,
                    'description' : None
                }
            },
            'combat' : {
                'initiative' : {
                    'modifier' : 0,
                    'total' : 0
                },
                'armor_class' : {
                    'temporary' : 0,
                    'total' : 0
                },
                'hit_points' : {
                    'damage_resistance' : 0,
                    'false_life' : 0,
                    'temp_hit_points' : 0,
                    'total' : 0
                },
            }
        }
        # End def
    # End class

def add_item(item):
    item.name = None
    item.owner = None
    item.type = None
    item.amount = None
    item.cost = None
    item.weight = None
    item.mundane_properties = None
    item.is_magical = None
    item.magical_type = None
    item.magical_properties = None
    item.description = None
    item.notes = None
    return item


# @add_item
# class Weapon:
#     def __init__(self, name, damage_amount, damage_type, attack_type, attack_bonus, is_ranged, range_low, range_high):
#         self.name = name
#         self.damage_amount = damage_amount
#         self.damage_type = damage_type
#         self.attack_type = attack_type
#         self.attack_bonus = attack_bonus
#         self.is_ranged = is_ranged
#         self.range_low = range_low
#         self.range_high = range_high

padding_value = 30

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
                print(f"{' ' * spaces}{key}:")
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


number_of_characters = int(input(f"Enter number of characters to generate: "))
characters = []
for _ in range(number_of_characters):
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
    character.profile['name']['first'] = random.choice(first_names)
    character.profile['name']['last'] = random.choice(last_names)
    for i in range(1, random.randint(1,6)):
        character.items.append(generate_random_item())
    for i in range(1, random.randint(1,4)):
        character.weapons.append(generate_random_weapon())



for character in characters:
    print(f"==================================================")
    print(f"Character")
    print_character(character.profile)

    print(f"Items:")
    print_inventory(character.items, 'Item')

    print(f"Weapons:")
    print_inventory(character.weapons, 'Weapon')

    print(f"Physical:")
    print_character(character.physical)







