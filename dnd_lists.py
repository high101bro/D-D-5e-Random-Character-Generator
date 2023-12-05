#! /usr/bin/env python3


first_names = ["Grog", "Vax'ildan", "Keyleth", "Percy", "Scanlan", "Vex'ahlia", "Pike", "Tiberius", "Pike", "Percival"]


last_names = ["Strongjaw", "De Rolo", "of the Air Ashari", "Fredrickstein", "Shorthalt", "of Syngorn", "Trickfoot", "Stormwind", "Trickfoot", "de Rolo"]


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

dnd_alignments = [
    'Lawful Good',
    'Neutral Good',
    'Chaotic Good',
    'Lawful Neutral', 
    'True Neutral', 
    'Chaotic Neutral', 
    'Lawful Evil',
    'Neutral Evil',
    'Chaotic evil'
]

dnd_skills_by_attribute = {
    "Strength": ["athletics"],
    "Dexterity": ["acrobatics", "sleight of hand", "stealth"],
    "Intelligence": ["arcana", "history", "investigation", "nature", "religion"],
    "Wisdom": ["animal handling", "insight", "medicine", "perception", "survival"],
    "Charisma": ["deception", "intimidation", "performance", "persuasion"]
}

dnd_skills = {
    'acrobatics' : {
        'related attribute' : 'dexterity',
        'proficiency' : False,
        'total' : 0,
        'description' : "Performing physical feats, maintaining balance, and tumbling."
    },
    'animal handling' : {
        'related attribute' : 'wisdom',
        'proficiency' : False,
        'total' : 0,
        'description' : "Calming, controlling, or understanding the intentions of animals."
    },
    'arcana' : {
        'related attribute' : 'intelligence',
        'proficiency' : False,
        'total' : 0,
        'description' : "Knowledge of magic, magical creatures, mystical lore, and magical traditions."
    },
    'athletics' : {
        'related attribute' : 'strength',
        'proficiency' : False,
        'total' : 0,
        'description' : "Performing physical activities like climbing, jumping, and swimming."
    },
    'deception' : {
        'related attribute' : 'charisma',
        'proficiency' : False,
        'total' : 0,
        'description' : "Your ability to convincingly hide the truth, either verbally or through actions."
    },
    'history' : {
        'related attribute' : 'intelligence',
        'proficiency' : False,
        'total' : 0,
        'description' : "Recalling information about historical events, legendary people, ancient kingdoms, and recent wars."
    },
    'insight' : {
        'related attribute' : 'wisdom',
        'proficiency' : False,
        'total' : 0,
        'description' : "Determining the true intentions of a creature, such as when searching out a lie or predicting someone’s next move."
    },
    'intimidation' : {
        'related attribute' : 'charisma',
        'proficiency' : False,
        'total' : 0,
        'description' : "Influencing someone through overt threats, hostile actions, and physical intimidation."
    },
    'investigation' : {
        'related attribute' : 'intelligence',
        'proficiency' : False,
        'total' : 0,
        'description' : "Looking for clues and making deductions based on those clues."
    },
    'medicine' : {
        'related attribute' : 'wisdom',
        'proficiency' : False,
        'total' : 0,
        'description' : "Ability to diagnose and treat injuries and diseases."
    },
    'nature' : {
        'related attribute' : 'intelligence',
        'proficiency' : False,
        'total' : 0,
        'description' : "Knowledge about terrain, plants and animals, the weather, and natural cycles."
    },
    'perception' : {
        'related attribute' : 'wisdom',
        'proficiency' : False,
        'total' : 0,
        'description' : "Noticing or sensing things, typically based on Wisdom. It’s the skill you’d use to hear a conversation through a door, spot something hidden under a rock, or notice someone sneaking up on you."
    },
    'performance' : {
        'related attribute' : 'charisma',
        'proficiency' : False,
        'total' : 0,
        'description' : "Delighting an audience with music, dance, acting, storytelling, or some other form of entertainment."
    },
    'persuasion' : {
        'related attribute' : 'charisma',
        'proficiency' : False,
        'total' : 0,
        'description' : "Influencing someone with tact, social graces, or good nature."
    },
    'religion' : {
        'related attribute' : 'intelligence',
        'proficiency' : False,
        'total' : 0,
        'description' : "Knowledge about deities, rites and prayers, religious hierarchies, holy symbols, and the practices of secret cults."
    },
    'sleight of hand' : {
        'related attribute' : 'dexterity',
        'proficiency' : False,
        'total' : 0,
        'description' : "Executing tricks of dexterity or misdirection, like picking pockets or conjuring objects."
    },
    'stealth' : {
        'related attribute' : 'dexterity',
        'proficiency' : False,
        'total' : 0,
        'description' : "Concealing yourself from enemies, slinking past guards, slipping away without being noticed."
    },
    'survival' : {
        'related attribute' : 'wisdom',
        'proficiency' : False,
        'total' : 0,
        'description' : "Following tracks, hunting wild game, guiding your group through frozen wastelands, identifying signs that owlbears live nearby, predicting the weather, or avoiding quicksand and other natural hazards."
    }
}

