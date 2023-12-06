#! /usr/bin/env python3


first_names = [
    'Grog', "Vax'ildan", 'Keyleth', 'Percy', 'Scanlan', "Vex'ahlia", 'Pike', 'Tiberius', 'Percival', 'Aric', 
    'Elowen', 'Thrain', 'Isolde', 'Kael', 'Seraphina', 'Grom', 'Elira', 'Finnian', 'Eilif', 'Lyria', 
    'Thalwin', 'Oona', 'Idris', 'Brigid', 'Dagfinn', 'Ysolde', 'Sylas', 'Maelis', 'Linnea', 'Thorne', 
    'Keldan', 'Elysia', 'Thora', 'Erling', 'Nerys', 'Aldric', 'Fianna', 'Varin', 'Seren', 'Ailin', 
    'Eilin', 'Alaric', 'Gwendolyn', 'Leif', 'Elowyn', 'Caelan', 'Aislinn', 'Einar', 'Imogen', 'Gavric', 
    'Elara', 'Freyr', 'Aislyn', 'Eolande', 'Lachlan', 'Tamsin', 'Rowan', 'Fiore', 'Magnus', 'Seraphim', 
    'Yrsa', 'Nolin', 'Ulfric', 'Ilyana', 'Kaelan', 'Eirik', 'Thalia', 'Sigurd', 'Gwyneira', 'Emrys', 
    'Idunn', 'Ulrik', 'Aislin', 'Thane', 'Eilwen', 'Orin', 'Lyra', 'Rhiannon', 'Soren', 'Lirael', 
    'Eldric', 'Daelin', 'Freya', 'Taran', 'Ysolt', 'Iolande'
]


last_names = [
    'Strongjaw', 'De Rolo', 'of the Air Ashari', 'Fredrickstein', 'Shorthalt', 'of Syngorn', 'Trickfoot', 'Stormwind', 'de Rolo', 'Brightwood', 
    'Ironheart', 'Fireforge', 'Stonefist', 'Wildwalker', 'Stormbringer', 'Doomhammer', 'Lionheart', 'Dragonslayer', 'Darkbane', 'Moonshadow', 
    'Blackthorn', 'Stormrage', 'Duskwalker', 'Battlehammer', 'Ironfist', 'Hammersmith', 'Wyrmslayer', 'Thundershield', 'Hawkwing', 'Bloodrider', 
    'Skyblade', 'Frostwolf', 'Snowfall', 'Windrider', 'Darkthorn', 'Nighthunter', 'Shadowstalker', 'Grimtotem', 'Stonemaul', 'Blackhand', 
    'Stormreaver', 'Bloodhoof', 'Ravencrest', 'Firebeard', 'Hellscream', 'Whisperwind', 'Blackrock', 'Thornsong', 'Swiftstrike', 'Warbringer', 
    'Thundertotem', 'Mistrunner', 'Rockseeker', 'Ironfoot', 'Braveforge', 'Mossbeard', 'Goldvein', 'Silvershield', 'Darkhammer', 'Stormbeard', 
    'Bronzebeard', 'Thrainsson', 'Dwarfbane', 'Silveraxe', 'Mountainheart', 'Stonesmith', 'Goreblade', 'Sureshot', 'Braveheart', 'Winterfall', 
    'Stormswift', 'Hawkmoon', 'Nightslayer', 'Redfist', 'Gorehammer', 'Hammerheart', 'Bronzeforge', 'Flintbeard', 'Dragonbane', 'Trollbane', 
    'Frostbeard', 'Whitestone', 'Dragonfist', 'Runeheart', 'Swiftaxe', 'Silentstrike', 'Brightblade', 'Gorehoof', 'Thunderaxe', 'Nightsong', 
    'Flintforge', 'Mountainaxe', 'Darkbeard', 'Waraxe', 'Silentstorm', 'Ironhorn', 'Stonehammer', 'Stoneguard', 'Hawkeye', 'Stormwalker', 
    'Darkfist', 'Ironclaw', 'Gorehelm', 'Stormshield', 'Hammerfall', 'Darkblade', 'Runeaxe'
]


dnd_menu_level = [
    "Level  1          0 Exp    You're just starting your adventuring journey, full of potential.",
    "Level  2        300 Exp    Now, you have a battle or two under your belt, gaining some confidence.",
    "Level  3        900 Exp    Your abilities are Expanding, and you're starting to specialize.",
    "Level  4      2,700 Exp    More powerful, you face greater challenges and choices.",
    "Level  5      6,500 Exp    A significant milestone, with access to new spells and abilities.",
    "Level  6     14,000 Exp    You're honing your skills, becoming a formidable force.",
    "Level  7     23,000 Exp    A master of your class, you can tackle complex encounters.",
    "Level  8     34,000 Exp    Your character is well-rounded, capable in various situations.",
    "Level  9     48,000 Exp    You're pushing the boundaries of your power.",
    "Level 10     64,000 Exp    A true Expert, you excel in your chosen path.",
    "Level 11     82,000 Exp    You've achieved greatness, your legend beginning to spread.",
    "Level 12    102,000 Exp    Your character is a force to be reckoned with.",
    "Level 13    125,000 Exp    Mastery of your abilities grants you confidence.",
    "Level 14    151,000 Exp    Few can match your Expertise and power.",
    "Level 15    180,000 Exp    You're on the verge of becoming legendary.",
    "Level 16    212,000 Exp    Your character's name is known far and wide.",
    "Level 17    247,000 Exp    You're considered a living legend, your deeds celebrated.",
    "Level 18    285,000 Exp    Nearly unparalleled in your mastery.",
    "Level 19    326,000 Exp    You're a true hero, capable of incredible feats.",
    "Level 20    370,000 Exp    At the pinnacle of power, you're virtually untouchable."
]

dnd_menu_race = [
    "Dwarf         Known for their craftsmanship, mining skills, and resilience in battle. They often live in mountain strongholds and value honor and tradition." ,
    "Elf           Graceful and long-lived, with a deep connection to nature and magic. They are known for their agility, keen senses, and affinity for archery." ,
    "Halfling      Small and nimble, often living peaceful lives in rural communities. They are known for their love of good food, simple pleasures, and luck." ,
    "Human         Adaptable and diverse, found in all corners of the world. They are known for their ambition, versatility, and ability to excel in various roles." ,
    "Dragonborn    Draconic ancestry with distinctive scales. They often have breath weapons tied to their dragon heritage and are known for their honor and strength." ,
    "Gnome         Curious inventors and tinkerers, known for their intellect and humor. They have a deep affinity for illusions and a love of pranks." ,
    "Half-Elf      The result of human and elf unions, inheriting qualities of both races. They are often charismatic, adaptable, and skilled diplomats." ,
    "Half-Orc      Strong and hardy, with orc and human ancestry. They are known for their endurance, combat prowess, and resilience." ,
    "Tiefling      Infernal bloodlines with fiendish features. They are tied to dark forces but can use their unique abilities for good or ill."
]

dnd_menu_class = [
    "Barbarian     Barbarians are fierce warriors from untamed lands, known for their rage and primal strength. They excel in melee combat and are often linked to nature.",
    "Bard          Bards are versatile performers and spellcasters, using their art and magic to inspire allies and hinder foes. They are charismatic and adaptable adventurers.",
    "Cleric        Clerics are divine spellcasters and servants of gods, channeling their power to heal or smite. They provide spiritual guidance and support in battle.",
    "Druid         Druids are protectors of nature, with the ability to shape-shift and cast spells tied to the natural world. They seek to maintain balance and harmony.",
    "Fighter       Fighters are masterful combatants with a wide range of fighting styles and weapon mastery. They excel in physical combat and tactics.",
    "Monk          Monks are disciplined martial artists with incredible agility and supernatural abilities. They harness ki energy and excel in unarmed combat.",
    "Paladin       Paladins are holy knights, sworn to uphold justice and righteousness. They combine martial prowess with divine spellcasting to protect the innocent.",
    "Ranger        Rangers are skilled hunters and trackers, at home in the wilderness. They excel in archery, survival, and protecting the natural world.",
    "Rogue         Rogues are cunning thieves, spies, and assassins, known for their agility and stealth. They excel in sneaking, lock-picking, and subterfuge.",
    "Sorcerer      Sorcerers have innate magical abilities, drawing power from their bloodline or inner potential. They cast spells with raw magical energy.",
    "Warlock       Warlocks forge pacts with otherworldly beings for magical powers. They have a unique set of spells and eldritch invocations.",
    "Wizard        Wizards are studious spellcasters who learn magic through rigorous study and spellbooks. They can cast a wide variety of spells and specialize in arcane knowledge."
]

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
        'proficiency' : True,
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

