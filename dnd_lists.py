#! /usr/bin/env python3


first_names = ["Grog", "Vax'ildan", "Keyleth", "Percy", "Scanlan", "Vex'ahlia", "Pike", "Tiberius", "Pike", "Percival"]


last_names = ["Strongjaw", "De Rolo", "of the Air Ashari", "Fredrickstein", "Shorthalt", "of Syngorn", "Trickfoot", "Stormwind", "Trickfoot", "de Rolo"]


dnd_races = [
    "Human",
    "Elf",
    "Dwarf",
    "Halfling",
    "Dragonborn",
    "Gnome",
    "Half-Elf",
    "Half-Orc",
    "Tiefling"
]

dnd_classes = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard"
]

dnd_skills = {
    "Strength": ["Athletics"],
    "Dexterity": ["Acrobatics", "Sleight of Hand", "Stealth"],
    "Intelligence": ["Arcana", "History", "Investigation", "Nature", "Religion"],
    "Wisdom": ["Animal Handling", "Insight", "Medicine", "Perception", "Survival"],
    "Charisma": ["Deception", "Intimidation", "Performance", "Persuasion"]
}

dnd_levels_exp = {
    1: 0,
    2: 300,
    3: 900,
    4: 2700,
    5: 6500,
    6: 14000,
    7: 23000,
    8: 34000,
    9: 48000,
    10: 64000,
    11: 85000,
    12: 100000,
    13: 120000,
    14: 140000,
    15: 165000,
    16: 195000,
    17: 225000,
    18: 265000,
    19: 305000,
    20: 355000
}

dnd_proficiency_bonus = {
    1: 2, 2: 2, 3: 2, 4: 2, 5: 3,
    6: 3, 7: 3, 8: 3, 9: 4, 10: 4,
    11: 4, 12: 4, 13: 5, 14: 5, 15: 5,
    16: 5, 17: 6, 18: 6, 19: 6, 20: 6
}

# Python dictionary representing the bonuses for each D&D 5e base race

dnd_race_bonuses = {
    "Human": {
        "Ability Score Increase": "All ability scores increase by 1"
    },
    "Elf": {
        "Ability Score Increase": "Dexterity score increases by 2",
        "Traits": ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance"]
    },
    "Dwarf": {
        "Ability Score Increase": "Constitution score increases by 2",
        "Traits": ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Stonecunning"]
    },
    "Halfling": {
        "Ability Score Increase": "Dexterity score increases by 2",
        "Traits": ["Lucky", "Brave", "Halfling Nimbleness"]
    },
    "Dragonborn": {
        "Ability Score Increase": "Strength score increases by 2, Charisma score by 1",
        "Traits": ["Draconic Ancestry", "Breath Weapon", "Damage Resistance"]
    },
    "Gnome": {
        "Ability Score Increase": "Intelligence score increases by 2",
        "Traits": ["Darkvision", "Gnome Cunning"]
    },
    "Half-Elf": {
        "Ability Score Increase": "Charisma score increases by 2, two other ability scores of choice increase by 1",
        "Traits": ["Darkvision", "Fey Ancestry", "Skill Versatility"]
    },
    "Half-Orc": {
        "Ability Score Increase": "Strength score increases by 2, Constitution score by 1",
        "Traits": ["Darkvision", "Relentless Endurance", "Savage Attacks"]
    },
    "Tiefling": {
        "Ability Score Increase": "Charisma score increases by 2, Intelligence score by 1",
        "Traits": ["Darkvision", "Hellish Resistance", "Infernal Legacy"]
    }
}





