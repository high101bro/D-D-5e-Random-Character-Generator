#! /usr/bin/env python3

import numpy as np
import random

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
