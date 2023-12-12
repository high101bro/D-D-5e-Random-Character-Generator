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
    'Strongjaw', 'De Rolo', 'Fredrickstein', 'Shorthalt', 'of Syngorn', 'Trickfoot', 'Stormwind', 'de Rolo', 'Brightwood', 'Runeaxe',
    'Ironheart', 'Fireforge', 'Stonefist', 'Wildwalker', 'Stormbringer', 'Doomhammer', 'Lionheart', 'Dragonslayer', 'Darkbane', 'Moonshadow', 
    'Blackthorn', 'Stormrage', 'Duskwalker', 'Battlehammer', 'Ironfist', 'Hammersmith', 'Wyrmslayer', 'Thundershield', 'Hawkwing', 'Bloodrider', 
    'Skyblade', 'Frostwolf', 'Snowfall', 'Windrider', 'Darkthorn', 'Nighthunter', 'Shadowstalker', 'Grimtotem', 'Stonemaul', 'Blackhand', 
    'Stormreaver', 'Bloodhoof', 'Ravencrest', 'Firebeard', 'Hellscream', 'Whisperwind', 'Blackrock', 'Thornsong', 'Swiftstrike', 'Warbringer', 
    'Thundertotem', 'Mistrunner', 'Rockseeker', 'Ironfoot', 'Braveforge', 'Mossbeard', 'Goldvein', 'Silvershield', 'Darkhammer', 'Stormbeard', 
    'Bronzebeard', 'Thrainsson', 'Dwarfbane', 'Silveraxe', 'Mountainheart', 'Stonesmith', 'Goreblade', 'Sureshot', 'Braveheart', 'Winterfall', 
    'Stormswift', 'Hawkmoon', 'Nightslayer', 'Redfist', 'Gorehammer', 'Hammerheart', 'Bronzeforge', 'Flintbeard', 'Dragonbane', 'Trollbane', 
    'Frostbeard', 'Whitestone', 'Dragonfist', 'Runeheart', 'Swiftaxe', 'Silentstrike', 'Brightblade', 'Gorehoof', 'Thunderaxe', 'Nightsong', 
    'Flintforge', 'Mountainaxe', 'Darkbeard', 'Waraxe', 'Silentstorm', 'Ironhorn', 'Stonehammer', 'Stoneguard', 'Hawkeye', 'Stormwalker', 
    'Darkfist', 'Ironclaw', 'Ironbeak', 'Gorehelm', 'Stormshield', 'Hammerfall', 'Darkblade', 'of the Air Ashari', "of the Ironclad Keep", "of the Silent Moors", 
    "of the Silvered Glen", "of the Frozen Tundra", "of the Crimson Blades", "of the Hidden Caverns", "of the Lost Isles", "of the Whispering Wind", "of the Enchanted Grove", "of the Mystic Mountains", "of the Emerald Isles", "of the Ancient Ruins", 
    "of the Stormy Seas", "of the Eternal Flame", "of the Misty Veil", "of the Shrouded Peaks", "of the Luminous Sky", "of the Ebon Tower", "of the Whispered Secrets", "of the Obsidian Spire", "of the Celestial Watchers", "of the Forgotten Realms", 
    "of the Fading Sunset", "of the Astral Guardians", "of the Eternal Nightfall", "of the Crystal Caves", "of the Crimson Rose", "of the Starlit Path", "of the Forgotten Woods", "of the Serpent's Fang", "of the Moonlit Meadow", "of the Shattered Shield", 
    "of the Silent Night", "of the Phoenix Feather", "of the Sacred Flame", "of the Silver Serpent", "of the Thundering Hooves", "of the Whistling Winds", "of the Amber Eye", "of the Soaring Eagle", "of the Howling Wolf", "of the Golden Sun", 
    "of the Dragon's Breath", "of the Braveheart", "of the Stormcaller", "of the Iron Fist", "of the Crimson Moon", "of the Feral Cat", "of the Hidden Blade", "of the Swift Arrow", "of the Shadowed Hand", "of the Fiery Heart", 
    "of the Serene Lake", "of the Celestial Dawn", "of the Thunderstrike", "of the Verdant Forest", "of the Silent Song", "of the Silver Lining", "of the Ebon Rose", "of the Glittering Sands", "of the Cursed Blood", "of the Iron Will", 
    "of the Whispering Pines", "of the Crimson Sky", "of the Midnight Hour", "of the Starry Night", "of the Enigmatic Orb", "of the Shining Beacon", "of the Ironclad Resolve", "of the Gilded Throne", "of the Thundersong", "of the Fading Echo", 
    "of the Silent Mirage", "of the Serpent's Kiss", "of the Lunar Eclipse", "of the Solar Flare", "of the Shimmering Veil", "of the Sable Shadow", "of the Emerald Dream", "of the Frozen Heart", "of the Crystalline Shard", "of the Primal Roar", 
    "of the Verdant Valley", "of the Whispers of Fate", "of the Mystic Scroll", "of the Eternal Spring",
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
    "Strength" : ["athletics"],
    "Dexterity" : ["acrobatics", "sleight of hand", "stealth"],
    "Intelligence" : ["arcana", "history", "investigation", "nature", "religion"],
    "Wisdom" : ["animal handling", "insight", "medicine", "perception", "survival"],
    "Charisma" : ["deception", "intimidation", "performance", "persuasion"]
}

conditions_and_effects = [
    "Advantage",
    "Bane",
    "Bless",
    "Blinded",
    "Charmed",
    "Concentration",
    "Confused",
    "Cursed",
    "Deafened",
    "Death",
    "Diseased",
    "Disguised",
    "Entangled",
    "Ethereal",
    "Exhaustion",
    "Fascinated",
    "Falling",
    "False Life",
    "Flying",
    "Frenzy",
    "Frightened",
    "Fumbled",
    "Gaseous Form",
    "Grappled",
    "Hasted",
    "Hidden",
    "Incapacitated",
    "Incorporeal",
    "Instant Death",
    "Invisible",
    "Paralyzed",
    "Petrified",
    "Poisoned",
    "Polymorphed",
    "Prone",
    "Rage",
    "Revived",
    "Restrained",
    "Slowed",
    "Stunned",
    "Turned",
    "Unconscious",
]

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


dnd_items = {
    'torch' : 'light in dark areas',
    'rations' : 'food during the trip',
    'waterskin' : 'drink!'
}

dnd_equipment = {
    "explorer's pack" : "for exporing",
    "adventure's pack" : "for the adventurer",
    "dungeoneer's pack" : "for the dungeons"
}

dnd_armor = {
    "Padded" : {
        "description" : "A light armor made of quilted layers of cloth and batting, it offers basic protection but can be noisy, causing stealth disadvantage.",
        "type" : "Light", 
        "cost" : "5 gp", 
        "ac" : 11,
        "add_dex" : True,
        "dex_mod_max" : 0,
        "strength" : 0, 
        "stealth" : "Disadvantage", 
        "magical_properties" : {},
        "don" : 1,
        "doff" : 1,
        "weight" : 8
    },
    "Leather" : {
        "description" : "Made from tanned animal hide, this light armor is flexible and offers a basic level of protection without impeding stealth.",
        "type" : "Light", 
        "cost" : "10 gp", 
        "ac" : 11,
        "add_dex" : True, 
        "dex_mod_max" : 0,
        "strength" : 0, 
        "stealth" : "None", 
        "magical_properties" : {},
        "don" : 1,
        "doff" : 1,
        "weight" : 10
    },
    "Studded Leather" : {
        "description" : "An enhanced version of leather armor with metal studs or spikes added for extra protection, while still being light and not affecting stealth.",
        "type" : "Light", 
        "cost" : "45 gp", 
        "ac" : 12,
        "add_dex" : True, 
        "dex_mod_max" : 0,
        "strength" : 0, 
        "stealth" : "None", 
        "magical_properties" : {},
        "don" : 1,
        "doff" : 1,
        "weight" : 13
    },
    "Hide" : {
        "description" : "Medium armor made from thick furs and pelts, it provides decent protection and doesn't hinder stealth, but is less effective than more refined armors.",
        "type" : "Medium", 
        "cost" : "10 gp", 
        "ac" : 12,
        "add_dex" : True, 
        "dex_mod_max" : 2,
        "strength" : 0, 
        "stealth" : "None", 
        "magical_properties" : {},
        "don" : 5,
        "doff" : 1,
        "weight" : 12
    },
    "Chain Shirt" : {
        "description" : "A medium armor made of interlocking metal rings, it covers the torso and upper arms, offering good protection without impeding stealth.",
        "type" : "Medium", 
        "cost" : "50 gp", 
        "ac" : 13,
        "add_dex" : True, 
        "dex_mod_max" : 2,
        "strength" : 0, 
        "stealth" : "None", 
        "magical_properties" : {},
        "don" : 5,
        "doff" : 1,
        "weight" : 20
    },
    "Scale Mail" : {
        "description" : "This medium armor consists of overlapping metal scales sewn onto a leather backing, offering good protection but at the cost of stealth.",
        "type" : "Medium", 
        "cost" : "50 gp", 
        "ac" : 14,
        "add_dex" : True, 
        "dex_mod_max" : 2,
        "strength" : 0, 
        "stealth" : "Disadvantage", 
        "magical_properties" : {},
        "don" : 5,
        "doff" : 1,
        "weight" : 45
    },
    "Breastplate" : {
        "description" : "Made of a single large metal piece covering the torso, this medium armor offers solid protection and doesn't impede stealth, but doesn't cover the whole body.",
        "type" : "Medium", 
        "cost" : "400 gp", 
        "ac" : 14,
        "add_dex" : True, 
        "dex_mod_max" : 2,
        "strength" : 0, 
        "stealth" : "None", 
        "magical_properties" : {},
        "don" : 5,
        "doff" : 1,
        "weight" : 20
    },
    "Half Plate" : {
        "description" : "A robust medium armor consisting of shaped metal plates covering key parts of the body. It offers high protection but can hinder stealth.",
        "type" : "Medium", 
        "cost" : "750 gp", 
        "ac" : 15,
        "add_dex" : True, 
        "dex_mod_max" : 2,
        "strength" : 0, 
        "stealth" : "Disadvantage", 
        "magical_properties" : {},
        "don" : 5,
        "doff" : 1,
        "weight" : 40
    },
    "Ring Mail" : {
        "description" : "A heavy armor made of interwoven metal rings, it provides a basic level of heavy armor protection but is noisy, causing stealth disadvantage.",
        "type" : "Heavy", 
        "cost" : "30 gp", 
        "ac" : 14,
        "add_dex" : False, 
        "dex_mod_max" : 0,
        "strength" : 0, 
        "stealth" : "Disadvantage", 
        "magical_properties" : {},
        "don" : 10,
        "doff" : 5,
        "weight" : 40
    },
    "Chain Mail" : {
        "description" : "A heavy armor made of interlocking metal rings covering the body, it offers substantial protection but requires some strength to wear effectively and hinders stealth.",
        "type" : "Heavy", 
        "cost" : "75 gp", 
        "ac" : 16,
        "add_dex" : False, 
        "dex_mod_max" : 0,
        "strength" : 13, 
        "stealth" : "Disadvantage", 
        "magical_properties" : {},
        "don" : 10,
        "doff" : 5,
        "weight" : 55
    },
    "Splint" : {
        "description" : "Made of vertical strips of metal riveted to a backing of leather, this heavy armor provides high protection but requires strength and hinders stealth.",
        "type" : "Heavy", 
        "cost" : "200 gp", 
        "ac" : 17,
        "add_dex" : False, 
        "dex_mod_max" : 0,
        "strength" : 15, 
        "stealth" : "Disadvantage", 
        "magical_properties" : {},
        "don" : 10,
        "doff" : 5,
        "weight" : 60
    },
    "Plate" : {
        "description" : "The most protective heavy armor, consisting of shaped metal plates covering the entire body. It offers excellent protection but requires strength and impairs stealth.",
        "type" : "Heavy", 
        "cost" : "1500 gp", 
        "ac" : 18,
        "add_dex" : False, 
        "dex_mod_max" : 0,
        "strength" : 15, 
        "stealth" : "Disadvantage", 
        "magical_properties" : {},
        "don" : 10,
        "doff" : 5,
        "weight" : 65
    },
    "Shield" : {
        "description" : "Not an armor but an armament, it's a protective device carried in one hand. Shields add to your overall Armor Class (AC) when used.",
        "type" : "Shield", 
        "cost" : "10 gp", 
        "ac" : 2,
        "add_dex" : False, 
        "dex_mod_max" : 0,
        "strength" : 0, 
        "stealth" : "None", 
        "magical_properties" : {},
        "don" : '1 action',
        "doff" : '1 action',
        "weight" : 6
    }
}


dnd_armor_weapon_item_modifiers = {
    "adamantine" : {
        "description of material" : "Ultra-hard metal known for its ability to make weapons and armor particularly effective.",
        "special properties" : ["Magical for overcoming resistance and immunity"],
        "locations" : {
            "raw material" : ["Deep mines", "Dwarven forges", "Ancient ruins"],
            "processed material" : ["Specialty blacksmiths", "High-end markets"],
            "upgraded weapons" : ["Elite warriors", "Royal guards", "Adventurers"]
        },
        "availability and rarity" : {
            "raw material" : "Very rare",
            "processed material" : "Rare",
            "upgraded weapons in town" : "Uncommon in major cities",
            "capable blacksmith in town" : "Rare, skilled blacksmiths only"
        },
        "cost" : {
            "items" : {
                "base" : 500,
                "multiplier" : 2
            },
            "armor" : {
                "base" : 500,
                "multiplier" : 2
            },
            "weapon" : {
                "base" : 500,
                "multiplier" : 2
            },
            "ammunition" : {
                "base" : 60,
                "multiplier" : 2
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "Yes",
                "weight" : "Increased by approximately 10%",
                "glows" : "No",
                "other properties" : "Extremely durable"
            },
            "armor" : {
                "armor class" : "Same as base armor",
                "damage reduction" : "Negates critical hits",
                "magical" : "Yes",
                "weight" : "Increased by approximately 10%",
                "glows" : "No",
                "other properties" : "Durable and tough"
            },
            "weapon" : {
                "overcomes damage reduction" : "Yes",
                "attack modifier" : "Same as base weapon",
                "magical" : "Yes",
                "weight" : "Increased by approximately 10%",
                "glows" : "No",
                "other properties" : "Extremely durable"
            },
            "ammunition" : {
                "overcomes damage reduction" : "Yes",
                "attack modifier" : "Same as base ammunition",
                "magical" : "Yes",
                "weight" : "Increased by approximately 10%",
                "glows" : "No",
                "other properties" : "Harder impact"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : "None",
            "that are weak to material" : "None",
            "that are susceptible to material" : ["Constructs", "Objects", "Some magical barriers"],
            "that can only be hurt by this material" : ["Mythical or very rare creatures as determined by DM"]
        },         
        "disadvantage" : {
            "items" : "Slightly heavier, can be more cumbersome",
            "armor" : "Slightly heavier, may hinder stealth",
            "weapon" : "Slightly heavier, requires more strength to wield effectively",
            "ammunition" : "Slightly heavier, may affect range and accuracy"
        },
        "change in" : {
            "weight" : "Increased by approximately 10%",
            "size" : "Same",
            "durability" : "Increased",
            "appearance" : "Metallic, shiny"
        },
        "time for blacksmith to upgrade" : {
            "items" : "Varies",
            "armor" : "1-2 weeks",
            "weapon" : "1 week",
            "ammunition" : "2-3 days"
        }
    },

    "cold iron" : {
        "description of material" : "A special iron known for its effectiveness against fey creatures and certain types of demons and devils.",
        "special properties" : ["Effective against fey, demons, and devils"],
        "locations" : {
            "raw material" : ["Mystical forests", "Otherworldly realms", "Ancient battlefields"],
            "processed material" : ["Specialized forges", "Sacred temples"],
            "upgraded weapons" : ["Demon hunters", "Fey adversaries", "Religious warriors"]
        },
        "availability and rarity" : {
            "raw material" : "Rare",
            "processed material" : "Uncommon",
            "upgraded weapons in town" : "Rare, mostly found in specialized shops",
            "capable blacksmith in town" : "Uncommon, skilled in arcane blacksmithing"
        },
        "cost" : {
            "items" : {
                "base" : 100,
                "multiplier" : 1.5
            },
            "armor" : {
                "base" : 100,
                "multiplier" : 1.5
            },
            "weapon" : {
                "base" : 100,
                "multiplier" : 1.5
            },
            "ammunition" : {
                "base" : 20,
                "multiplier" : 1.5
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "No",
                "weight" : "Same as standard iron",
                "glows" : "No",
                "other properties" : "Effective against certain supernatural creatures"
            },
            "armor" : {
                "armor class" : "Same as base armor",
                "damage reduction" : "None",
                "magical" : "No",
                "weight" : "Same as standard iron",
                "glows" : "No",
                "other properties" : "Protection against fey, demons, and devils"
            },
            "weapon" : {
                "overcomes damage reduction" : "Yes, for specific creatures",
                "attack modifier" : "Same as base weapon",
                "magical" : "No",
                "weight" : "Same as standard iron",
                "glows" : "No",
                "other properties" : "Especially harmful to fey, demons, and devils"
            },
            "ammunition" : {
                "overcomes damage reduction" : "Yes, for specific creatures",
                "attack modifier" : "Same as base ammunition",
                "magical" : "No",
                "weight" : "Same as standard iron",
                "glows" : "No",
                "other properties" : "Effective against certain supernatural creatures"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : "None",
            "that are weak to material" : ["Fey", "Demons", "Devils"],
            "that are susceptible to material" : "None",
            "that can only be hurt by this material" : ["Certain fey, demons, and devils as determined by DM"]
        },         
        "disadvantage" : {
            "items" : "None specific to the material",
            "armor" : "None specific to the material",
            "weapon" : "None specific to the material",
            "ammunition" : "None specific to the material"
        },
        "change in" : {
            "weight" : "Same as standard iron",
            "size" : "Same",
            "durability" : "Same as standard iron",
            "appearance" : "Darker, more somber than regular iron"
        },
        "time for blacksmith to upgrade" : {
            "items" : "Varies",
            "armor" : "1-2 weeks",
            "weapon" : "1-2 weeks",
            "ammunition" : "1 week"
        }
    },    
    "mithral" : {
        "description of material" : "A light, flexible metal. Mithral armor can be worn under normal clothes and doesn't impose disadvantage on Stealth checks. It also doesn't have a Strength requirement.",
        "special properties" : ["Lightweight", "Does not hinder movement", "Stealth-friendly"],
        "locations" : {
            "raw material" : ["Elven mines", "Ancient ruins", "Magical forges"],
            "processed material" : ["Elven smiths", "High-end armories"],
            "upgraded weapons" : ["Elven warriors", "Stealthy adventurers", "Assassins"]
        },
        "availability and rarity" : {
            "raw material" : "Very rare",
            "processed material" : "Rare",
            "upgraded weapons in town" : "Rare, mostly in elven or high-end markets",
            "capable blacksmith in town" : "Uncommon, mostly elven smiths"
        },
        "cost" : {
            "items" : {
                "base" : 100,
                "multiplier" : 1.5
            },
            "armor" : {
                "base" : 100,
                "multiplier" : 1.5
            },
            "weapon" : {
                "base" : 100,
                "multiplier" : 1.5
            },
            "ammunition" : {
                "base" : 10,
                "multiplier" : 1.5
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "No",
                "weight" : "Reduced by approximately 30%",
                "glows" : "No",
                "other properties" : "Easily concealable under clothing"
            },
            "armor" : {
                "armor class" : "Same as base armor",
                "damage reduction" : "None",
                "magical" : "No",
                "weight" : "Reduced by approximately 30%",
                "glows" : "No",
                "other properties" : "No disadvantage on Stealth, no Strength requirement"
            },
            "weapon" : {
                "overcomes damage reduction" : "No",
                "attack modifier" : "Same as base weapon",
                "magical" : "No",
                "weight" : "Reduced by approximately 20%",
                "glows" : "No",
                "other properties" : "Easier to handle and carry"
            },
            "ammunition" : {
                "overcomes damage reduction" : "No",
                "attack modifier" : "Same as base ammunition",
                "magical" : "No",
                "weight" : "Reduced by approximately 20%",
                "glows" : "No",
                "other properties" : "Lighter, potentially faster"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : ["Creatures resistant to non-magical attacks might not be affected"],
            "that are weak to material" : ["None specifically"],
            "that are susceptible to material" : ["None specifically"],
            "that can only be hurt by this material" : ["Creatures vulnerable to lightweight, stealth attacks"]
        },         
        "disadvantage" : {
            "items" : "Less durable in direct combat compared to heavier materials",
            "armor" : "Provides less protection against heavy crushing blows",
            "weapon" : "May not be as effective in brute force attacks",
            "ammunition" : "Lighter weight might affect long-range accuracy in windy conditions"
        },
        "change in" : {
            "weight" : "Reduced by approximately 20-30%",
            "size" : "Same",
            "durability" : "Same as standard materials",
            "appearance" : "Silvery, lustrous"
        },
        "time for blacksmith to upgrade" : {
            "items" : "Varies",
            "armor" : "2-3 weeks",
            "weapon" : "1-2 weeks",
            "ammunition" : "1 week"
        }
    },
    "silvered" : {
        "description of material" : "Silver coating applied to weapons, known for its effectiveness against certain supernatural creatures like werewolves and other lycanthropes, as well as some undead.",
        "special properties" : ["Effective against lycanthropes and certain undead"],
        "locations" : {
            "raw material" : ["Silver mines", "Treasury vaults"],
            "processed material" : ["Silver smiths", "General blacksmiths"],
            "upgraded weapons" : ["Monster hunters", "Clerics", "Paladins"]
        },
        "availability and rarity" : {
            "raw material" : "Common",
            "processed material" : "Common",
            "upgraded weapons in town" : "Common in areas plagued by lycanthropes or undead",
            "capable blacksmith in town" : "Common"
        },
        "cost" : {
            "items" : {
                "base" : 50,
                "multiplier" : 1
            },
            "armor" : {
                "base" : 0,  # Typically not applied to armor
                "multiplier" : 0
            },
            "weapon" : {
                "base" : 100,  # Additional cost for silvering a weapon
                "multiplier" : 1
            },
            "ammunition" : {
                "base" : 5,  # Additional cost per piece of ammunition
                "multiplier" : 1
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "No",
                "weight" : "Slightly increased due to silver coating",
                "glows" : "No",
                "other properties" : "Effective against certain creatures"
            },
            "armor" : {
                "armor class" : "Same as base armor",
                "damage reduction" : "None",
                "magical" : "No",
                "weight" : "Same as base armor",
                "glows" : "No",
                "other properties" : "Not typically applied to armor"
            },
            "weapon" : {
                "overcomes damage reduction" : "Yes, for specific creatures",
                "attack modifier" : "Same as base weapon",
                "magical" : "No",
                "weight" : "Slightly increased",
                "glows" : "No",
                "other properties" : "Silver shine, effective against lycanthropes and certain undead"
            },
            "ammunition" : {
                "overcomes damage reduction" : "Yes, for specific creatures",
                "attack modifier" : "Same as base ammunition",
                "magical" : "No",
                "weight" : "Slightly increased",
                "glows" : "No",
                "other properties" : "Effective against certain creatures"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : "None",
            "that are weak to material" : ["Lycanthropes", "Certain types of undead"],
            "that are susceptible to material" : "None",
            "that can only be hurt by this material" : ["Some lycanthropes and undead as determined by DM"]
        },         
        "disadvantage" : {
            "items" : "Slightly heavier, more expensive",
            "armor" : "Not typically applied to armor",
            "weapon" : "Additional cost for silvering",
            "ammunition" : "Additional cost per piece"
        },
        "change in" : {
            "weight" : "Increased by approximately 5%",
            "size" : "Same",
            "durability" : "Same as standard materials, but may require more maintenance to prevent tarnish",
            "appearance" : "Silver shine, more ornate"
        },
        "time for blacksmith to upgrade" : {
            "items" : "Varies",
            "armor" : "Not applicable",
            "weapon" : "1-2 days",
            "ammunition" : "Few hours"
        }
    },
 "dragonhide" : {
        "description of material" : "The hide of dragons, known for its toughness and the natural magical properties of dragons. Often sought after for crafting armor.",
        "special properties" : ["Tough and durable", "Resistant to the element of the dragon type"],
        "locations" : {
            "raw material" : ["Dragon lairs", "Battlefields where dragons fell"],
            "processed material" : ["Expert leatherworkers", "Dragon slayers"],
            "upgraded armor" : ["Dragon hunters", "High-ranking knights", "Sorcerers"]
        },
        "availability and rarity" : {
            "raw material" : "Extremely rare",
            "processed material" : "Very rare",
            "upgraded armor in town" : "Rare, typically custom-made",
            "capable craftsman in town" : "Very rare, specialized artisans"
        },
        "cost" : {
            "items" : {
                "base" : 0,  # Typically not applied to regular items
                "multiplier" : 0
            },
            "armor" : {
                "base" : 500,  # Additional cost for using dragonhide
                "multiplier" : 2
            },
            "weapon" : {
                "base" : 0,  # Not typically used for weapons
                "multiplier" : 0
            },
            "ammunition" : {
                "base" : 0,  # Not typically used for ammunition
                "multiplier" : 0
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "Varies (depending on dragon type)",
                "weight" : "Comparable to leather",
                "glows" : "No",
                "other properties" : "Resistant to specific elemental damage"
            },
            "armor" : {
                "armor class" : "Same as base armor made from the hide",
                "damage reduction" : "Resistance to specific elemental damage (based on dragon type)",
                "magical" : "Varies",
                "weight" : "Lighter than metal armor, heavier than standard leather",
                "glows" : "No",
                "other properties" : "Durable, often with magical properties"
            },
            "weapon" : {
                "overcomes damage reduction" : "Not applicable",
                "attack modifier" : "Not applicable",
                "magical" : "Not applicable",
                "weight" : "Not applicable",
                "glows" : "Not applicable",
                "other properties" : "Not applicable"
            },
            "ammunition" : {
                "overcomes damage reduction" : "Not applicable",
                "attack modifier" : "Not applicable",
                "magical" : "Not applicable",
                "weight" : "Not applicable",
                "glows" : "Not applicable",
                "other properties" : "Not applicable"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : "None",
            "that are weak to material" : "None",
            "that are susceptible to material" : "None",
            "that can only be hurt by this material" : "None"
        },         
        "disadvantage" : {
            "items" : "Difficult to work with, requiring specialized skills",
            "armor" : "Expensive, requires maintenance to keep its properties",
            "weapon" : "Not typically used",
            "ammunition" : "Not typically used"
        },
        "change in" : {
            "weight" : "Lighter than typical metal armor, increased by approximately 10-20% compared to standard leather",
            "size" : "Custom-fitted",
            "durability" : "Highly durable, retains magical properties of the dragon",
            "appearance" : "Varies with dragon type, often striking and unique"
        },
        "time for craftsman to upgrade" : {
            "items" : "Varies",
            "armor" : "Several weeks to months",
            "weapon" : "Not applicable",
            "ammunition" : "Not applicable"
        }
    },
    "darkwood" : {
        "description of material" : "A magical wood known for its strength and lightness, used for creating light but sturdy armor and shields, often utilized by characters who prefer stealth or need to move quickly.",
        "special properties" : ["Lightweight", "Strong as steel"],
        "locations" : {
            "raw material" : ["Enchanted forests", "Druid groves"],
            "processed material" : ["Expert woodworkers", "Elven craftsmen"],
            "upgraded items" : ["Rangers", "Druids", "Elven warriors"]
        },
        "availability and rarity" : {
            "raw material" : "Rare",
            "processed material" : "Uncommon",
            "upgraded items in town" : "Uncommon, especially in regions near forests",
            "capable craftsman in town" : "Rare, skilled in magical woodworking"
        },
        "cost" : {
            "items" : {
                "base" : 50,
                "multiplier" : 1.5
            },
            "armor" : {
                "base" : 100,
                "multiplier" : 2
            },
            "weapon" : {
                "base" : 50,
                "multiplier" : 1.5
            },
            "ammunition" : {
                "base" : 2,  # Additional cost per piece of ammunition
                "multiplier" : 1.5
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "No",
                "weight" : "Reduced by approximately 50%",
                "glows" : "No",
                "other properties" : "As strong as steel but much lighter"
            },
            "armor" : {
                "armor class" : "Same as base armor",
                "damage reduction" : "None",
                "magical" : "No",
                "weight" : "Reduced by approximately 50%",
                "glows" : "No",
                "other properties" : "Ideal for stealth, does not hinder movement"
            },
            "weapon" : {
                "overcomes damage reduction" : "No",
                "attack modifier" : "Same as base weapon",
                "magical" : "No",
                "weight" : "Reduced by approximately 20-30%",
                "glows" : "No",
                "other properties" : "Lightweight, easy to handle"
            },
            "ammunition" : {
                "overcomes damage reduction" : "No",
                "attack modifier" : "Same as base ammunition",
                "magical" : "No",
                "weight" : "Reduced by approximately 20-30%",
                "glows" : "No",
                "other properties" : "Lighter, potentially faster"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : "None",
            "that are weak to material" : "None",
            "that are susceptible to material" : "None",
            "that can only be hurt by this material" : "None"
        },         
        "disadvantage" : {
            "items" : "Less durable against heavy crushing force",
            "armor" : "Might provide less protection against heavy or blunt attacks",
            "weapon" : "Not suited for heavy, brute-force combat",
            "ammunition" : "Lighter weight might affect long-range accuracy in windy conditions"
        },
        "change in" : {
            "weight" : "Reduced by approximately 20-50%",
            "size" : "Same",
            "durability" : "High durability but not ideal for heavy impact",
            "appearance" : "Rich, dark hue, often with natural patterns"
        },
        "time for craftsman to upgrade" : {
            "items" : "Varies",
            "armor" : "1-2 weeks",
            "weapon" : "1 week",
            "ammunition" : "Few hours to a day"
        }
    },
    "ironwood" : {
        "description of material" : "A magically altered wood that matches or exceeds the strength of steel, often used by druids and other nature-aligned characters for armor and weapons.",
        "special properties" : ["As strong as steel", "Magically enhanced"],
        "locations" : {
            "raw material" : ["Sacred groves", "Areas of strong natural magic"],
            "processed material" : ["Druid enclaves", "Magical workshops"],
            "upgraded items" : ["Druids", "Nature paladins", "Forest guardians"]
        },
        "availability and rarity" : {
            "raw material" : "Rare",
            "processed material" : "Uncommon",
            "upgraded items in town" : "Rare, often custom-made or found in druidic communities",
            "capable craftsman in town" : "Rare, artisans with knowledge of nature magic"
        },
        "cost" : {
            "items" : {
                "base" : 100,
                "multiplier" : 2
            },
            "armor" : {
                "base" : 200,
                "multiplier" : 2
            },
            "weapon" : {
                "base" : 100,
                "multiplier" : 2
            },
            "ammunition" : {
                "base" : 10,  # Additional cost per piece of ammunition
                "multiplier" : 2
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "Varies (depending on enchantment)",
                "weight" : "Comparable to steel",
                "glows" : "No",
                "other properties" : "Strong and durable, retains some natural wood properties"
            },
            "armor" : {
                "armor class" : "Same as base metal armor",
                "damage reduction" : "None",
                "magical" : "Varies",
                "weight" : "Slightly lighter than equivalent metal armor",
                "glows" : "No",
                "other properties" : "Environmentally integrated, often enchanted"
            },
            "weapon" : {
                "overcomes damage reduction" : "No",
                "attack modifier" : "Same as base weapon",
                "magical" : "Varies",
                "weight" : "Comparable to metal weapons",
                "glows" : "No",
                "other properties" : "Balanced, durable, often enchanted"
            },
            "ammunition" : {
                "overcomes damage reduction" : "No",
                "attack modifier" : "Same as base ammunition",
                "magical" : "Varies",
                "weight" : "Comparable to metal ammunition",
                "glows" : "No",
                "other properties" : "Durable, may have special effects based on enchantments"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : "None",
            "that are weak to material" : "None",
            "that are susceptible to material" : "None",
            "that can only be hurt by this material" : "None"
        },         
        "disadvantage" : {
            "items" : "May require magical upkeep",
            "armor" : "Less flexibility compared to light armors",
            "weapon" : "Requires proper maintenance to retain magical properties",
            "ammunition" : "May be less effective against certain types of creatures"
        },
        "change in" : {
            "weight" : "Slightly lighter than metal, increased by approximately 5-10% compared to normal wood",
            "size" : "Same",
            "durability" : "High, comparable to steel",
            "appearance" : "Rich, dark coloration, often with natural wood grain visible"
        },
        "time for craftsman to upgrade" : {
            "items" : "Varies",
            "armor" : "2-4 weeks",
            "weapon" : "1-3 weeks",
            "ammunition" : "1-2 days"
        }
    }, 
    "elemental_material" : {
        "description of material" : "Materials imbued with elemental properties, such as fire-forged steel, frost-forged steel, or items infused with elemental essences.",
        "special properties" : ["Imbued with elemental powers", "Offers resistance or extra damage of a specific element"],
        "locations" : {
            "raw material" : ["Elemental planes", "Locations of elemental convergence"],
            "processed material" : ["Specialist elemental smiths", "Mage forges"],
            "upgraded items" : ["Elemental mages", "Adventurers with elemental affinity"]
        },
        "availability and rarity" : {
            "raw material" : "Rare",
            "processed material" : "Uncommon",
            "upgraded items in town" : "Uncommon, varies based on region",
            "capable craftsman in town" : "Rare, specialized in elemental crafting"
        },
        "cost" : {
            "items" : {
                "base" : 200,
                "multiplier" : 2
            },
            "armor" : {
                "base" : 300,
                "multiplier" : 3
            },
            "weapon" : {
                "base" : 300,
                "multiplier" : 3
            },
            "ammunition" : {
                "base" : 20,  # Additional cost per piece of ammunition
                "multiplier" : 3
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "Yes",
                "weight" : "Varies based on element",
                "glows" : "Often",
                "other properties" : "Elemental resistance or damage (e.g., fire resistance, additional ice damage)"
            },
            "armor" : {
                "armor class" : "Same as base armor",
                "damage reduction" : "Elemental resistance",
                "magical" : "Yes",
                "weight" : "Varies based on element",
                "glows" : "Often",
                "other properties" : "Elemental-themed properties"
            },
            "weapon" : {
                "overcomes damage reduction" : "Yes, for creatures vulnerable to the element",
                "attack modifier" : "Same as base weapon",
                "magical" : "Yes",
                "weight" : "Varies based on element",
                "glows" : "Often",
                "other properties" : "Elemental damage addition"
            },
            "ammunition" : {
                "overcomes damage reduction" : "Yes, for creatures vulnerable to the element",
                "attack modifier" : "Same as base ammunition",
                "magical" : "Yes",
                "weight" : "Varies based on element",
                "glows" : "Often",
                "other properties" : "Elemental damage addition"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : ["Creatures immune to the specific element"],
            "that are weak to material" : ["Creatures vulnerable to the specific element"],
            "that are susceptible to material" : "None",
            "that can only be hurt by this material" : ["Specific elemental creatures, as determined by DM"]
        },         
        "disadvantage" : {
            "items" : "May be susceptible to opposing elements",
            "armor" : "May be less effective against opposite elemental damage",
            "weapon" : "May be less effective in environments opposite to the element",
            "ammunition" : "May lose elemental property in opposing environments"
        },
        "change in" : {
            "weight" : "Varies based on element",
            "size" : "Same",
            "durability" : "High, but may vary in opposing elemental conditions",
            "appearance" : "Reflects the nature of the element (e.g., fiery patterns, icy sheen)"
        },
        "time for craftsman to upgrade" : {
            "items" : "Varies",
            "armor" : "3-4 weeks",
            "weapon" : "2-3 weeks",
            "ammunition" : "1 week"
        }
    },
    "celestial_bronze" : {
        "description of material" : "A mythical metal imbued with celestial magic, effective against supernatural creatures, especially those of evil or chaotic alignment.",
        "special properties" : ["Magically enhanced", "Effective against supernatural and extraplanar entities"],
        "locations" : {
            "raw material" : ["Celestial realms", "Astral plane"],
            "processed material" : ["Divine forges", "Temples"],
            "upgraded items" : ["Champions of deities", "Celestial warlords", "Heroic adventurers"]
        },
        "availability and rarity" : {
            "raw material" : "Extremely rare",
            "processed material" : "Very rare",
            "upgraded items in town" : "Rare, often divinely gifted",
            "capable craftsman in town" : "Very rare, requires divine blessing or knowledge"
        },
        "cost" : {
            "items" : {
                "base" : 500,
                "multiplier" : 3
            },
            "armor" : {
                "base" : 500,
                "multiplier" : 3
            },
            "weapon" : {
                "base" : 500,
                "multiplier" : 3
            },
            "ammunition" : {
                "base" : 100,  # Additional cost per piece of ammunition
                "multiplier" : 3
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "Yes",
                "weight" : "Slightly lighter than typical bronze",
                "glows" : "Sometimes (especially in the presence of evil)",
                "other properties" : "Especially effective against supernatural and evil creatures"
            },
            "armor" : {
                "armor class" : "Same as base armor",
                "damage reduction" : "None",
                "magical" : "Yes",
                "weight" : "Slightly lighter than typical bronze",
                "glows" : "Sometimes",
                "other properties" : "Offers enhanced protection against evil entities"
            },
            "weapon" : {
                "overcomes damage reduction" : "Yes, especially for supernatural creatures",
                "attack modifier" : "Same as base weapon",
                "magical" : "Yes",
                "weight" : "Slightly lighter than typical bronze",
                "glows" : "Sometimes",
                "other properties" : "Especially effective against evil and chaotic beings"
            },
            "ammunition" : {
                "overcomes damage reduction" : "Yes, especially for supernatural creatures",
                "attack modifier" : "Same as base ammunition",
                "magical" : "Yes",
                "weight" : "Slightly lighter than typical bronze",
                "glows" : "Sometimes",
                "other properties" : "Effective against supernatural enemies"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : "None",
            "that are weak to material" : ["Evil extraplanar beings", "Undead", "Demons", "Devils"],
            "that are susceptible to material" : ["Supernatural creatures", "Chaos-aligned entities"],
            "that can only be hurt by this material" : ["Specific extraplanar or mythic creatures, as determined by DM"]
        },         
        "disadvantage" : {
            "items" : "Rare and difficult to work with, requiring special knowledge",
            "armor" : "May have restrictions or consequences for non-celestial users",
            "weapon" : "High cost, may attract unwanted attention from evil beings",
            "ammunition" : "Expensive to produce"
        },
        "change in" : {
            "weight" : "Reduced by approximately 10%",
            "size" : "Same",
            "durability" : "Highly durable, maintains sharpness and luster",
            "appearance" : "Gleaming, often with celestial or divine symbols"
        },
        "time for craftsman to upgrade" : {
            "items" : "Varies",
            "armor" : "1-2 months",
            "weapon" : "3-4 weeks",
            "ammunition" : "1-2 weeks"
        }
    },
    "star_metal" : {
        "description of material" : "A rare and powerful metal said to have fallen from the stars, imbued with cosmic energy. It is renowned for its strength and mystical properties.",
        "special properties" : ["Cosmic energy", "Extremely durable", "Magically conductive"],
        "locations" : {
            "raw material" : ["Meteorite impact sites", "Ancient astral realms"],
            "processed material" : ["Master blacksmiths", "Arcane forges"],
            "upgraded items" : ["Astronomers", "Spellcasters", "Cosmic adventurers"]
        },
        "availability and rarity" : {
            "raw material" : "Extremely rare",
            "processed material" : "Very rare",
            "upgraded items in town" : "Rare, often requires a quest to obtain",
            "capable craftsman in town" : "Very rare, needs profound knowledge of metallurgy and magic"
        },
        "cost" : {
            "items" : {
                "base" : 1000,
                "multiplier" : 4
            },
            "armor" : {
                "base" : 1000,
                "multiplier" : 4
            },
            "weapon" : {
                "base" : 1000,
                "multiplier" : 4
            },
            "ammunition" : {
                "base" : 200,  # Additional cost per piece of ammunition
                "multiplier" : 4
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "Yes",
                "weight" : "Slightly heavier than typical steel",
                "glows" : "Often (with a cosmic shimmer)",
                "other properties" : "Resistant to magic, can channel arcane energy"
            },
            "armor" : {
                "armor class" : "Same as base armor, potentially higher",
                "damage reduction" : "Magical resistance",
                "magical" : "Yes",
                "weight" : "Slightly heavier than typical steel",
                "glows" : "Often",
                "other properties" : "Provides enhanced protection, especially against magical attacks"
            },
            "weapon" : {
                "overcomes damage reduction" : "Yes, especially against creatures vulnerable to magic",
                "attack modifier" : "Potentially higher than base weapon",
                "magical" : "Yes",
                "weight" : "Slightly heavier than typical steel",
                "glows" : "Often",
                "other properties" : "Can have additional magical effects or enhancements"
            },
            "ammunition" : {
                "overcomes damage reduction" : "Yes, especially against creatures vulnerable to magic",
                "attack modifier" : "Potentially higher than base ammunition",
                "magical" : "Yes",
                "weight" : "Slightly heavier than typical steel",
                "glows" : "Often",
                "other properties" : "Magical effects, enhanced impact"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : "None",
            "that are weak to material" : ["Magically susceptible creatures", "Astral or cosmic entities"],
            "that are susceptible to material" : ["Creatures vulnerable to magic"],
            "that can only be hurt by this material" : ["Specific cosmic or magical creatures, as determined by DM"]
        },         
        "disadvantage" : {
            "items" : "Very expensive, rare and difficult to work with",
            "armor" : "Heavier, may require attunement or magical proficiency",
            "weapon" : "Requires careful handling, might have unpredictable effects",
            "ammunition" : "Expensive and rare, used for specific purposes"
        },
        "change in" : {
            "weight" : "Increased by approximately 10-15%",
            "size" : "Same",
            "durability" : "Extremely high, resistant to most forms of damage",
            "appearance" : "Metallic with a cosmic shimmer, sometimes showing star-like patterns"
        },
        "time for craftsman to upgrade" : {
            "items" : "Varies",
            "armor" : "Several months",
            "weapon" : "1-2 months",
            "ammunition" : "2-3 weeks"
        }
    },
    "glassteel" : {
        "description of material" : "A magical composite material that combines the transparency of glass and the strength of steel. It's often used for aesthetic purposes as well as practical combat advantages.",
        "special properties" : ["Transparent like glass", "Strong as steel", "Magically enhanced"],
        "locations" : {
            "raw material" : ["Magical artisans", "Enchanted regions"],
            "processed material" : ["Skilled mage-smiths", "Arcane workshops"],
            "upgraded items" : ["High-end armors", "Unique weapons", "Magical constructs"]
        },
        "availability and rarity" : {
            "raw material" : "Rare",
            "processed material" : "Uncommon",
            "upgraded items in town" : "Rare, typically seen in high magic societies",
            "capable craftsman in town" : "Rare, requires advanced magical knowledge"
        },
        "cost" : {
            "items" : {
                "base" : 300,
                "multiplier" : 2.5
            },
            "armor" : {
                "base" : 500,
                "multiplier" : 3
            },
            "weapon" : {
                "base" : 300,
                "multiplier" : 2.5
            },
            "ammunition" : {
                "base" : 50,  # Additional cost per piece of ammunition
                "multiplier" : 2.5
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "Yes",
                "weight" : "Slightly lighter than typical steel",
                "glows" : "No",
                "other properties" : "Can be made transparent, retaining strength of steel"
            },
            "armor" : {
                "armor class" : "Same as base armor made from steel",
                "damage reduction" : "None",
                "magical" : "Yes",
                "weight" : "Slightly lighter than typical steel",
                "glows" : "No",
                "other properties" : "Can be transparent, stylish, and practical"
            },
            "weapon" : {
                "overcomes damage reduction" : "No",
                "attack modifier" : "Same as base weapon",
                "magical" : "Yes",
                "weight" : "Slightly lighter than typical steel",
                "glows" : "No",
                "other properties" : "Can be transparent, offering strategic advantages"
            },
            "ammunition" : {
                "overcomes damage reduction" : "No",
                "attack modifier" : "Same as base ammunition",
                "magical" : "Yes",
                "weight" : "Slightly lighter than typical steel",
                "glows" : "No",
                "other properties" : "Transparency can offer strategic advantages"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : "None",
            "that are weak to material" : "None",
            "that are susceptible to material" : "None",
            "that can only be hurt by this material" : "None"
        },         
        "disadvantage" : {
            "items" : "Expensive to produce, requires magical expertise",
            "armor" : "May be less discreet due to transparency",
            "weapon" : "Transparency can be a double-edged sword, revealing hidden mechanisms",
            "ammunition" : "Higher cost, complexity in manufacturing"
        },
        "change in" : {
            "weight" : "Reduced by approximately 10%",
            "size" : "Same",
            "durability" : "High, comparable to steel",
            "appearance" : "Transparent with a glass-like finish, steel strength"
        },
        "time for craftsman to upgrade" : {
            "items" : "Varies",
            "armor" : "1-2 months",
            "weapon" : "3-4 weeks",
            "ammunition" : "1-2 weeks"
        }
    },
    "dragonbone" : {
        "description of material" : "Fabled to be stronger and lighter than steel, dragonbone is known for its unique properties and inherent magical potential. It's often used for making unique weapons or armor.",
        "special properties" : ["Magically potent", "Lighter and stronger than steel", "Possesses unique qualities of the dragon type it came from"],
        "locations" : {
            "raw material" : ["Dragon lairs", "Sites of dragon battles"],
            "processed material" : ["Expert bone smiths", "Magical workshops"],
            "upgraded items" : ["Dragon slayers", "High-level adventurers", "Enchanters"]
        },
        "availability and rarity" : {
            "raw material" : "Extremely rare",
            "processed material" : "Very rare",
            "upgraded items in town" : "Rare, often a sign of prestige or great achievement",
            "capable craftsman in town" : "Rare, requires specialized skills in bone crafting and magic"
        },
        "cost" : {
            "items" : {
                "base" : 800,
                "multiplier" : 3
            },
            "armor" : {
                "base" : 1000,
                "multiplier" : 4
            },
            "weapon" : {
                "base" : 800,
                "multiplier" : 3
            },
            "ammunition" : {
                "base" : 150,  # Additional cost per piece of ammunition
                "multiplier" : 3
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "Varies (inherent in the bone)",
                "weight" : "Reduced by approximately 30%",
                "glows" : "Sometimes (if enchanted)",
                "other properties" : "Varies based on dragon type; can include elemental resistance or affinity"
            },
            "armor" : {
                "armor class" : "Same or slightly higher than base armor",
                "damage reduction" : "Possible elemental resistance",
                "magical" : "Varies",
                "weight" : "Reduced by approximately 30%",
                "glows" : "Sometimes",
                "other properties" : "Can be inherently magical, offering unique advantages"
            },
            "weapon" : {
                "overcomes damage reduction" : "Yes, in certain cases",
                "attack modifier" : "Same or slightly higher than base weapon",
                "magical" : "Varies",
                "weight" : "Reduced by approximately 20%",
                "glows" : "Sometimes",
                "other properties" : "Can have additional magical effects; often associated with the dragon's breath type"
            },
            "ammunition" : {
                "overcomes damage reduction" : "Yes, in certain cases",
                "attack modifier" : "Same or slightly higher than base ammunition",
                "magical" : "Varies",
                "weight" : "Reduced by approximately 20%",
                "glows" : "Sometimes",
                "other properties" : "Can have elemental effects or enhanced impact"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : "None",
            "that are weak to material" : ["Depends on the dragon type; for example, creatures weak to fire might be more vulnerable to red dragonbone"],
            "that are susceptible to material" : "None",
            "that can only be hurt by this material" : ["Specific creatures, as determined by DM; could be dragon-related entities"]
        },         
        "disadvantage" : {
            "items" : "Difficult to obtain and craft, requiring specialized knowledge",
            "armor" : "May carry the essence of the dragon, potentially attracting attention or conflict",
            "weapon" : "Rare and highly sought after, can be a double-edged sword in terms of drawing attention",
            "ammunition" : "Expensive to make, not suitable for mass production"
        },
        "change in" : {
            "weight" : "Reduced by approximately 20-30%",
            "size" : "Same",
            "durability" : "Highly durable, maintains properties of the dragon",
            "appearance" : "Varies with dragon type, often striking and distinctive"
        },
        "time for craftsman to upgrade" : {
            "items" : "Varies",
            "armor" : "Several weeks to months",
            "weapon" : "1-2 months",
            "ammunition" : "2-3 weeks"
        }
    },
    "obsidian" : {
        "description of material" : "A naturally occurring volcanic glass, known for its sharpness and brittle nature. Often used for crafting sharp blades or arrowheads.",
        "special properties" : ["Extremely sharp", "Brittle", "Can hold a fine edge"],
        "locations" : {
            "raw material" : ["Volcanic regions", "Ancient lava flows"],
            "processed material" : ["Specialist craftsmen", "Volcanic forges"],
            "upgraded items" : ["Assassins", "Tribal warriors", "Specialized archers"]
        },
        "availability and rarity" : {
            "raw material" : "Uncommon",
            "processed material" : "Uncommon",
            "upgraded items in town" : "Rare, often seen in specific cultures or regions",
            "capable craftsman in town" : "Uncommon, requires specialized skills in obsidian crafting"
        },
        "cost" : {
            "items" : {
                "base" : 50,
                "multiplier" : 1.5
            },
            "armor" : {
                "base" : 0,  # Not typically used for armor
                "multiplier" : 0
            },
            "weapon" : {
                "base" : 100,  # Additional cost for weapons
                "multiplier" : 1.5
            },
            "ammunition" : {
                "base" : 10,  # Additional cost per piece of ammunition
                "multiplier" : 1.5
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "No",
                "weight" : "Light",
                "glows" : "No",
                "other properties" : "Exceptionally sharp, useful for cutting and piercing"
            },
            "armor" : {
                "armor class" : "Not applicable",
                "damage reduction" : "Not applicable",
                "magical" : "Not applicable",
                "weight" : "Not applicable",
                "glows" : "Not applicable",
                "other properties" : "Not typically used for armor"
            },
            "weapon" : {
                "overcomes damage reduction" : "No",
                "attack modifier" : "Same as base weapon",
                "magical" : "No",
                "weight" : "Lighter than metal weapons",
                "glows" : "No",
                "other properties" : "Fragile but incredibly sharp"
            },
            "ammunition" : {
                "overcomes damage reduction" : "No",
                "attack modifier" : "Same as base ammunition",
                "magical" : "No",
                "weight" : "Lighter than typical metal",
                "glows" : "No",
                "other properties" : "Sharp, effective for piercing"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : "None",
            "that are weak to material" : ["Creatures vulnerable to piercing damage"],
            "that are susceptible to material" : "None",
            "that can only be hurt by this material" : ["None specifically"]
        },         
        "disadvantage" : {
            "items" : "Brittle, can shatter or break upon hard impact",
            "armor" : "Not used for armor due to brittleness",
            "weapon" : "High risk of breaking, not suitable for parrying or heavy combat",
            "ammunition" : "Fragile, must be used with care"
        },
        "change in" : {
            "weight" : "Lighter than metal, increased by approximately 5-10% compared to wood",
            "size" : "Same",
            "durability" : "Low, prone to shattering",
            "appearance" : "Glassy, black, often with sharp edges"
        },
        "time for craftsman to upgrade" : {
            "items" : "Varies",
            "armor" : "Not applicable",
            "weapon" : "1-2 weeks",
            "ammunition" : "Few days"
        }
    },
    "living_wood" : {
        "description of material" : "A magically infused wood that is still alive, often with regenerative properties or other magical effects. It's used by those with a deep connection to nature, like druids.",
        "special properties" : ["Regenerative", "Magically responsive", "Connected to nature"],
        "locations" : {
            "raw material" : ["Enchanted forests", "Druid groves"],
            "processed material" : ["Druidic enclaves", "Sacred nature sites"],
            "upgraded items" : ["Druids", "Nature mages", "Forest guardians"]
        },
        "availability and rarity" : {
            "raw material" : "Rare",
            "processed material" : "Uncommon",
            "upgraded items in town" : "Uncommon, typically found in nature-focused societies",
            "capable craftsman in town" : "Rare, requires deep understanding of nature magic"
        },
        "cost" : {
            "items" : {
                "base" : 200,
                "multiplier" : 2
            },
            "armor" : {
                "base" : 300,
                "multiplier" : 2.5
            },
            "weapon" : {
                "base" : 200,
                "multiplier" : 2
            },
            "ammunition" : {
                "base" : 20,  # Additional cost per piece of ammunition
                "multiplier" : 2
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "Yes",
                "weight" : "Lighter than typical wood",
                "glows" : "Sometimes (if enchanted)",
                "other properties" : "Can self-repair, adapt to magical environments"
            },
            "armor" : {
                "armor class" : "Same as base wooden armor",
                "damage reduction" : "None",
                "magical" : "Yes",
                "weight" : "Lighter than typical wooden armor",
                "glows" : "Sometimes",
                "other properties" : "Can adapt to wearer, grow or shrink slightly to fit"
            },
            "weapon" : {
                "overcomes damage reduction" : "No",
                "attack modifier" : "Same as base wooden weapon",
                "magical" : "Yes",
                "weight" : "Lighter than typical wooden weapons",
                "glows" : "Sometimes",
                "other properties" : "Can adapt or change shape slightly during use"
            },
            "ammunition" : {
                "overcomes damage reduction" : "No",
                "attack modifier" : "Same as base wooden ammunition",
                "magical" : "Yes",
                "weight" : "Lighter than typical wooden ammunition",
                "glows" : "Sometimes",
                "other properties" : "Can alter flight slightly for accuracy"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : "None",
            "that are weak to material" : ["Creatures vulnerable to natural magic"],
            "that are susceptible to material" : ["Some undead, unnatural beings"],
            "that can only be hurt by this material" : ["Specific creatures vulnerable to druidic magic, as determined by DM"]
        },         
        "disadvantage" : {
            "items" : "Requires care, can be damaged by fire or dark magic",
            "armor" : "Not as sturdy as metal, vulnerable to fire",
            "weapon" : "Less effective in heavy combat, vulnerable to fire and rot",
            "ammunition" : "Can be more affected by environmental factors"
        },
        "change in" : {
            "weight" : "Reduced by approximately 20%",
            "size" : "Adaptive",
            "durability" : "Self-repairing, but vulnerable to certain elements",
            "appearance" : "Natural wood appearance, sometimes with a greenish hue or leaves"
        },
        "time for craftsman to upgrade" : {
            "items" : "Varies, often requires rituals",
            "armor" : "2-3 weeks",
            "weapon" : "1-2 weeks",
            "ammunition" : "1 week"
        }
    },
    "void_metal" : {
        "description of material" : "A mysterious and rare metal, often associated with the power of the void, the stars, or otherworldly realms. It is known for its strange properties and potential for powerful enchantments.",
        "special properties" : ["Otherworldly resilience", "Absorbs or nullifies certain magics", "Resonates with cosmic energy"],
        "locations" : {
            "raw material" : ["Otherworldly rifts", "Cosmic events"],
            "processed material" : ["Forbidden forges", "Secret arcane guilds"],
            "upgraded items" : ["Void sorcerers", "Interplanar travelers", "Cosmic entities"]
        },
        "availability and rarity" : {
            "raw material" : "Extremely rare",
            "processed material" : "Very rare",
            "upgraded items in town" : "Rare and often shrouded in mystery",
            "capable craftsman in town" : "Very rare, often requiring forbidden knowledge"
        },
        "cost" : {
            "items" : {
                "base" : 1000,
                "multiplier" : 5
            },
            "armor" : {
                "base" : 1200,
                "multiplier" : 5
            },
            "weapon" : {
                "base" : 1000,
                "multiplier" : 5
            },
            "ammunition" : {
                "base" : 300,  # Additional cost per piece of ammunition
                "multiplier" : 5
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "Yes",
                "weight" : "Comparable to steel",
                "glows" : "Sometimes (with an otherworldly light)",
                "other properties" : "Can have unpredictable magical effects, often potent"
            },
            "armor" : {
                "armor class" : "Same as base armor, potentially enhanced",
                "damage reduction" : "May nullify or absorb certain types of magic",
                "magical" : "Yes",
                "weight" : "Comparable to steel",
                "glows" : "Sometimes",
                "other properties" : "Protects against eldritch and cosmic forces"
            },
            "weapon" : {
                "overcomes damage reduction" : "Yes, especially against otherworldly creatures",
                "attack modifier" : "Potentially enhanced",
                "magical" : "Yes",
                "weight" : "Comparable to steel",
                "glows" : "Sometimes",
                "other properties" : "Can harness void energy or cosmic power"
            },
            "ammunition" : {
                "overcomes damage reduction" : "Yes, particularly against creatures of magical or otherworldly nature",
                "attack modifier" : "Potentially enhanced",
                "magical" : "Yes",
                "weight" : "Comparable to steel",
                "glows" : "Sometimes",
                "other properties" : "Can disrupt magic or affect otherworldly beings"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : "None",
            "that are weak to material" : ["Eldritch beings", "Cosmic entities", "Certain magical creatures"],
            "that are susceptible to material" : ["Beings vulnerable to void or cosmic energies"],
            "that can only be hurt by this material" : ["Specific otherworldly creatures, as determined by DM"]
        },         
        "disadvantage" : {
            "items" : "Extremely rare, often with dangerous or unpredictable side effects",
            "armor" : "May attract unwanted attention from otherworldly beings",
            "weapon" : "Can be volatile or dangerous to wield without proper knowledge",
            "ammunition" : "Rare and costly to produce, with potentially unstable effects"
        },
        "change in" : {
            "weight" : "Comparable to steel",
            "size" : "Same",
            "durability" : "Extremely high, resistant to most conventional damage",
            "appearance" : "Dark, often with a shimmering or shifting appearance"
        },
        "time for craftsman to upgrade" : {
            "items" : "Varies, often lengthy and complex",
            "armor" : "Several months",
            "weapon" : "1-2 months",
            "ammunition" : "2-3 weeks"
        }
    },
    "ethereal_silk" : {
        "description of material" : "A rare and exquisite silk sourced from creatures or plants within the Ethereal Plane, known for its lightweight and magical properties. It is often used in making lightweight and magically enhanced clothing or armor.",
        "special properties" : ["Incredibly lightweight", "Magical resilience", "Subtle ethereal shimmer"],
        "locations" : {
            "raw material" : ["Ethereal Plane", "Cross-planar trades"],
            "processed material" : ["Expert weavers", "Arcane tailors"],
            "upgraded items" : ["Spellcasters", "High-ranking nobles", "Otherworldly beings"]
        },
        "availability and rarity" : {
            "raw material" : "Very rare",
            "processed material" : "Rare",
            "upgraded items in town" : "Uncommon, often a sign of wealth or magical affinity",
            "capable craftsman in town" : "Rare, requires both weaving and magical expertise"
        },
        "cost" : {
            "items" : {
                "base" : 500,
                "multiplier" : 4
            },
            "armor" : {
                "base" : 700,
                "multiplier" : 5
            },
            "weapon" : {
                "base" : 0,  # Not typically used for weapons
                "multiplier" : 0
            },
            "ammunition" : {
                "base" : 0,  # Not typically used for ammunition
                "multiplier" : 0
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "Yes",
                "weight" : "Reduced by approximately 80%",
                "glows" : "Subtly in the moonlight or in the presence of magic",
                "other properties" : "Elegant, often used in magical robes or cloaks"
            },
            "armor" : {
                "armor class" : "Lighter armors, enhanced AC",
                "damage reduction" : "None",
                "magical" : "Yes",
                "weight" : "Reduced by approximately 80%",
                "glows" : "Subtly",
                "other properties" : "Can offer magical protection or enchantments"
            },
            "weapon" : {
                "overcomes damage reduction" : "Not applicable",
                "attack modifier" : "Not applicable",
                "magical" : "Not applicable",
                "weight" : "Not applicable",
                "glows" : "Not applicable",
                "other properties" : "Not applicable"
            },
            "ammunition" : {
                "overcomes damage reduction" : "Not applicable",
                "attack modifier" : "Not applicable",
                "magical" : "Not applicable",
                "weight" : "Not applicable",
                "glows" : "Not applicable",
                "other properties" : "Not applicable"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : "None",
            "that are weak to material" : "None",
            "that are susceptible to material" : "None",
            "that can only be hurt by this material" : "None"
        },         
        "disadvantage" : {
            "items" : "Fragile, requires careful handling",
            "armor" : "Provides minimal physical protection, vulnerable to fire and sharp objects",
            "weapon" : "Not used for weapons",
            "ammunition" : "Not used for ammunition"
        },
        "change in" : {
            "weight" : "Reduced by approximately 80%",
            "size" : "Same",
            "durability" : "Delicate, handle with care",
            "appearance" : "Translucent, shimmering, often with ethereal hues"
        },
        "time for craftsman to upgrade" : {
            "items" : "Varies",
            "armor" : "1-2 months",
            "weapon" : "Not applicable",
            "ammunition" : "Not applicable"
        }
    },
   "elemental_crystals" : {
        "description of material" : "Crystals imbued with elemental energy, such as fire, ice, wind, or earth. These crystals are used to add elemental effects to weapons, armor, and other items.",
        "special properties" : ["Elemental energy infusion", "Can add elemental damage or resistance"],
        "locations" : {
            "raw material" : ["Elemental planes", "Natural crystal formations"],
            "processed material" : ["Alchemists", "Elemental mages"],
            "upgraded items" : ["Elemental sorcerers", "Adventurers specializing in elemental magic"]
        },
        "availability and rarity" : {
            "raw material" : "Rare",
            "processed material" : "Uncommon",
            "upgraded items in town" : "Varies, based on the region and elemental alignment",
            "capable craftsman in town" : "Uncommon, requires knowledge of elemental magic"
        },
        "cost" : {
            "items" : {
                "base" : 300,
                "multiplier" : 2
            },
            "armor" : {
                "base" : 400,
                "multiplier" : 2.5
            },
            "weapon" : {
                "base" : 300,
                "multiplier" : 2
            },
            "ammunition" : {
                "base" : 50,  # Additional cost per piece of ammunition
                "multiplier" : 2
            }
        },
        "benefit" : {
            "items" : {
                "magical" : "Yes",
                "weight" : "Slight increase due to crystal integration",
                "glows" : "Often (glows with the color of the elemental energy)",
                "other properties" : "Adds elemental effects (e.g., fire damage, ice resistance)"
            },
            "armor" : {
                "armor class" : "Same as base armor",
                "damage reduction" : "Elemental resistance (based on crystal type)",
                "magical" : "Yes",
                "weight" : "Slight increase",
                "glows" : "Often",
                "other properties" : "Protects against specific elemental damage"
            },
            "weapon" : {
                "overcomes damage reduction" : "Yes, for creatures vulnerable to the specific element",
                "attack modifier" : "Same as base weapon",
                "magical" : "Yes",
                "weight" : "Slight increase",
                "glows" : "Often",
                "other properties" : "Inflicts additional elemental damage"
            },
            "ammunition" : {
                "overcomes damage reduction" : "Yes, for creatures vulnerable to the specific element",
                "attack modifier" : "Same as base ammunition",
                "magical" : "Yes",
                "weight" : "Slight increase",
                "glows" : "Often",
                "other properties" : "Inflicts elemental effects upon impact"
            }
        }, 
        "creatures" : {
            "that are immune to the material" : ["Creatures immune to the specific element"],
            "that are weak to material" : ["Creatures vulnerable to the specific element"],
            "that are susceptible to material" : ["Varies based on elemental alignment"],
            "that can only be hurt by this material" : ["Specific elemental creatures, as determined by DM"]
        },         
        "disadvantage" : {
            "items" : "Can be unstable or dangerous if mishandled",
            "armor" : "May be less effective against opposite elemental forces",
            "weapon" : "Risk of elemental backlash or unintended effects",
            "ammunition" : "Can be more complex to produce, with variable effects"
        },
        "change in" : {
            "weight" : "Slight increase due to crystal integration",
            "size" : "Same",
            "durability" : "High, but can be affected by opposing elemental forces",
            "appearance" : "Varies, often has an elemental glow or motif"
        },
        "time for craftsman to upgrade" : {
            "items" : "Varies",
            "armor" : "2-3 weeks",
            "weapon" : "1-2 weeks",
            "ammunition" : "1 week"
        }
    },
    "disguise" : {
        "description of item" : "A set of clothing, makeup, and accessories designed to alter one's appearance. Used by characters to blend in, impersonate others, or hide their identity.",
        "special properties" : ["Aids in concealing true identity", "Enhances ability to impersonate"],
        "locations" : {
            "raw material" : ["Clothiers", "Costume shops", "Theatrical suppliers"],
            "processed material" : ["Tailors", "Makeup artists", "Disguise specialists"],
            "upgraded items" : ["Spies", "Assassins", "Performers"]
        },
        "availability and rarity" : {
            "raw material" : "Common",
            "processed material" : "Common",
            "upgraded items in town" : "Uncommon, varies based on sophistication",
            "capable craftsman in town" : "Common for basic disguises, rare for intricate ones"
        },
        "cost" : {
            "basic disguise" : {
                "base" : 25,  # Basic disguise kit
                "multiplier" : 1
            },
            "advanced disguise" : {
                "base" : 100,  # More advanced kit with higher-quality materials
                "multiplier" : 1.5
            }
        },
        "benefit" : {
            "effectiveness" : "Grants bonuses to Deception or Stealth checks when trying to pass as someone else",
            "duration" : "Effective until removed or exposed",
            "glows" : "No",
            "other properties" : "Can include prosthetics, voice modulation tools, and other accessories"
        }, 
        "creatures" : {
            "that can see through the disguise" : ["Creatures with high Perception or Insight", "Some magical beings with true sight"],
            "that are fooled by the disguise" : ["Most common folk", "Guards", "Others not expecting deception"],
            "that are suspicious of the disguise" : ["Experienced investigators", "Certain cautious creatures"],
            "that can only be interacted with using this item" : "None"
        },         
        "disadvantage" : {
            "limitations" : "May not hold up to close scrutiny, physical examination, or magical detection",
            "risks" : "Risk of exposure, leading to potential conflict or complications"
        },
        "change in" : {
            "appearance" : "Varies based on the nature of the disguise",
            "durability" : "Varies, some components may be fragile or temporary"
        },
        "time for user to apply" : "Varies from minutes for simple disguises to hours for intricate ones"
    },
    "booby_trapped" : {
        "description of item" : "An item or area rigged with a hidden trap, designed to activate when interacted with in a certain way. Used to protect, deter, or harm those who unknowingly trigger it.",
        "special properties" : ["Hidden trap mechanism", "Can cause harm or create an obstacle", "Designed for protection or deterrence"],
        "locations" : {
            "raw material" : "None",
            "processed material" : "None",
            "upgraded items" : ["Trapsmiths", "Rogues", "Guardians of treasures"]
        },
        "availability and rarity" : {
            "raw material" : "None",
            "processed material" : "None",
            "upgraded items in town" : "Varies, depends on the presence of skilled trapsmiths or secretive protectors",
            "capable craftsman in town" : "Uncommon to rare, requires specialized skills"
        },
        "cost" : {
            "basic trap" : {
                "base" : 50,  # Cost for simple traps
                "multiplier" : 1
            },
            "advanced trap" : {
                "base" : 200,  # Cost for more complex and deadly traps
                "multiplier" : 2
            }
        },
        "benefit" : {
            "effectiveness" : "Varies, based on the complexity and design of the trap",
            "duration" : "Effective until triggered or disarmed",
            "glows" : "No",
            "other properties" : "Can include mechanisms like poison needles, explosive runes, or magical alarms"
        }, 
        "creatures" : {
            "that can detect the trap" : ["Creatures with high Perception or Investigation skills", "Some creatures with special senses or abilities"],
            "that are fooled by the trap" : ["Unwary intruders", "Thieves", "Most common creatures"],
            "that are immune to the trap" : ["Creatures immune to the specific trap mechanism (e.g., undead for poison traps)"],
            "that can only be interacted with using this item" : "None"
        },         
        "disadvantage" : {
            "limitations" : "Can be detected and disarmed by skilled individuals, might harm unintended targets",
            "risks" : "Potential collateral damage, legal or moral implications"
        },
        "change in" : {
            "appearance" : "Designed to be concealed or blend in with surroundings",
            "durability" : "Varies, often single-use",
            "weight" : "Varies based on trap type",
            "size" : "Varies based on trap type"
        },
        "time for craftsman to set up" : "Varies, from minutes for simple traps to hours or days for complex setups"
    },
    "ornamented" : {
        "description of item" : "Items enhanced with decorative elements such as jewels, intricate carvings, or precious metals. Often used to display wealth, status, or magical enhancement.",
        "special properties" : ["Aesthetic enhancement", "Potential for minor magical attributes", "Symbol of status or power"],
        "locations" : {
            "raw material" : "None",
            "processed material" : ["Jewelers", "Master craftsmen", "Enchanters"],
            "upgraded items" : ["Royalty", "High-ranking officials", "Wealthy individuals"]
        },
        "availability and rarity" : {
            "raw material" : "None",
            "processed material" : "Varies, based on the level of artistry",
            "upgraded items in town" : "Common in affluent areas, rare in others",
            "capable craftsman in town" : "Common for basic ornamentation, rare for intricate work"
        },
        "cost" : {
            "basic ornamentation" : {
                "base" : 100,  # Cost for adding basic decorative elements
                "multiplier" : 1.2
            },
            "luxurious ornamentation" : {
                "base" : 500,  # Cost for high-end decorations, possibly with precious materials
                "multiplier" : 2
            }
        },
        "benefit" : {
            "effectiveness" : "Primarily aesthetic, can have minor magical effects if enchanted",
            "duration" : "Permanent, unless physically damaged",
            "glows" : "Sometimes (if enchanted or adorned with luminescent materials)",
            "other properties" : "Can include symbols of power, family crests, or magical runes"
        }, 
        "creatures" : {
            "that can detect the significance" : ["Knowledgeable individuals", "Connoisseurs of art", "Certain magical beings"],
            "that are attracted to the item" : ["Thieves", "Collectors", "Admirers"],
            "that are indifferent to the item" : "Most common creatures",
            "that can only be interacted with using this item" : "None"
        },         
        "disadvantage" : {
            "limitations" : "Can draw unwanted attention, may not offer functional benefits",
            "risks" : "Risk of theft, can be costly to repair if damaged"
        },
        "change in" : {
            "appearance" : "Enhanced with decorative elements, more visually striking",
            "durability" : "Same as the base item, unless weakened by alterations",
            "weight" : "Slight increase due to added materials",
            "size" : "Slight increase or unchanged"
        },
        "time for craftsman to apply" : "Varies, from days for simple ornamentation to weeks or months for intricate work"
    },
    "weight_reduction" : {
        "description of item" : "Items modified to be lighter than their standard counterparts, often through magical means or advanced craftsmanship. Used to enhance mobility and ease of use.",
        "special properties" : ["Reduced weight", "Easier to carry and use", "Maintains original strength and functionality"],
        "locations" : {
            "raw material" : "None",
            "processed material" : ["Magical forges", "Advanced workshops", "Enchanters"],
            "upgraded items" : ["Adventurers", "Soldiers", "Travelers"]
        },
        "availability and rarity" : {
            "raw material" : "None",
            "processed material" : "Uncommon",
            "upgraded items in town" : "Uncommon, more frequent in advanced or magical societies",
            "capable craftsman in town" : "Uncommon, requires specialized skills or magic"
        },
        "cost" : {
            "basic weight reduction" : {
                "base" : 100,  # Cost for minor weight reduction
                "multiplier" : 1.5
            },
            "significant weight reduction" : {
                "base" : 300,  # Cost for significant weight reduction
                "multiplier" : 2
            }
        },
        "benefit" : {
            "effectiveness" : "Makes items easier to carry and use, especially for extended periods",
            "duration" : "Permanent, as long as the item remains intact",
            "glows" : "No",
            "other properties" : "Retains original strength and functionality despite being lighter"
        }, 
        "creatures" : {
            "that can detect the modification" : ["Knowledgeable craftsmen", "Magic users with detection abilities"],
            "that are attracted to the item" : ["Adventurers seeking ease of travel", "Individuals requiring mobility"],
            "that are indifferent to the item" : "Most common creatures",
            "that can only be interacted with using this item" : "None"
        },         
        "disadvantage" : {
            "limitations" : "Can be costly, may require maintenance to retain enchantment or structural integrity",
            "risks" : "None specific to the weight reduction"
        },
        "change in" : {
            "appearance" : "Unchanged or slightly altered to indicate modification",
            "durability" : "Maintained, unless structurally altered",
            "weight" : "Reduced by a specific percentage, varies based on modification",
            "size" : "Unchanged"
        },
        "time for craftsman to apply" : "Varies, from a few days for simple modifications to weeks for complex ones"
    },
    "reinforced" : {
        "description of item" : "Items that have been strengthened with additional materials or techniques to increase their durability, protection, or effectiveness.",
        "special properties" : ["Enhanced durability", "Increased strength", "Improved protection"],
        "locations" : {
            "raw material" : "None",
            "processed material" : ["Armories", "Blacksmiths", "Engineering workshops"],
            "upgraded items" : ["Warriors", "Engineers", "Construction workers"]
        },
        "availability and rarity" : {
            "raw material" : "None",
            "processed material" : "Common",
            "upgraded items in town" : "Common, especially in military or construction-focused areas",
            "capable craftsman in town" : "Common, requires skills in metalworking or engineering"
        },
        "cost" : {
            "basic reinforcement" : {
                "base" : 50,  # Cost for basic reinforcement
                "multiplier" : 1.2
            },
            "advanced reinforcement" : {
                "base" : 200,  # Cost for advanced, more effective reinforcement
                "multiplier" : 1.5
            }
        },
        "benefit" : {
            "effectiveness" : "Increases the item's resistance to damage, wear, and tear",
            "duration" : "Permanent, as long as the item remains intact",
            "glows" : "No",
            "other properties" : "Can make items slightly heavier or bulkier due to added materials"
        }, 
        "creatures" : {
            "that can detect the modification" : ["Skilled craftsmen", "Experienced warriors"],
            "that are attracted to the item" : ["People in need of durable equipment", "Military personnel"],
            "that are indifferent to the item" : "Most common creatures",
            "that can only be interacted with using this item" : "None"
        },         
        "disadvantage" : {
            "limitations" : "May increase weight or reduce flexibility of the item",
            "risks" : "None specific to the reinforcement"
        },
        "change in" : {
            "appearance" : "Slightly altered to show reinforcement",
            "durability" : "Increased, more resistant to damage",
            "weight" : "Increased due to additional materials",
            "size" : "Slightly increased or unchanged, depending on the reinforcement"
        },
        "time for craftsman to apply" : "Varies, from a few days for simple reinforcement to weeks for complex or extensive reinforcement"
    },
}



dnd_weapons = {
    "club" : {
        "description" : "A short, thick stick used as a weapon.",
        "type" : "simple melee",
        "cost" : "1 sp",
        "weight" : "2 lbs",
        "properties" : {
            "Light" : "When using two-weapon fighting and using this weapon as your off-hand attack, the character can add their ability modifier to the damage of the second weapon's attack provided it's light. You also don't suffer the normal disadvantage on the attack roll, which would typically apply to off-hand attacks without the 'light' property.",
        },
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "1d4"
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "bludgeoning",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : "strength"
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "dagger" : {
        "description" : "A small, sharp knife used for stabbing.",
        "type" : "simple melee",
        "cost" : "2 gp",
        "weight" : "1 lb",
        "properties" : {
            "Finesse" : "Allows the attacker to use their Dexterity modifier instead of Strength for both the attack and damage rolls when wielding that weapon.",
            "Light" : "When using two-weapon fighting and using this weapon as your off-hand attack, the character can add their ability modifier to the damage of the second weapon's attack provided it's light. You also don't suffer the normal disadvantage on the attack roll, which would typically apply to off-hand attacks without the 'light' property.",
            "Thrown" : " Weapons with the thrown property can be used effectively in both melee and ranged combat, making them versatile choices for characters who want the option to attack at different ranges."
            },
        "size" : "small",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "1d4"
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 20,
                "long" : 60,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength or dexterity",
            "thrown" : "strength or dexterity",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "greatclub" : {
        "description" : "A larger and heavier club, typically requiring two hands to use effectively.",
        "type" : "simple melee",
        "cost" : "2 sp",
        "weight" : "10 lbs",
        "properties" : {
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
        "size" : "large",
        "damage" : {
            "melee" : {
                "one_handed" : "None",
                "two_handed" : "1d8",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "bludgeoning",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 5,
                "long" : 15,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : {
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
    },
    "handaxe" : {
        "description" : "A small axe designed for use with one hand.",
        "type" : "simple melee",
        "cost" : "5 gp",
        "weight" : "2 lbs",
        "properties" : {
            "Light" : "When using two-weapon fighting and using this weapon as your off-hand attack, the character can add their ability modifier to the damage of the second weapon's attack provided it's light. You also don't suffer the normal disadvantage on the attack roll, which would typically apply to off-hand attacks without the 'light' property.", 
            "Thrown" : " Weapons with the thrown property can be used effectively in both melee and ranged combat, making them versatile choices for characters who want the option to attack at different ranges.",
        },
        "size" : "small",
        "damage" : {
            "melee" : {
                "one_handed" : "1d6",
                "two_handed" : "1d6",
            },
            "thrown" : "1d6",
            "ranged" : "0d0"
        },
        "damage type" : "slashing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 20,
                "long" : 60,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "javelin" : {
        "description" : "A light spear designed primarily to be thrown.",
        "type" : "simple melee",
        "cost" : "5 sp",
        "weight" : "2 lbs",
        "properties" : {
            "Thrown" : " Weapons with the thrown property can be used effectively in both melee and ranged combat, making them versatile choices for characters who want the option to attack at different ranges.",
        },
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d6",
                "two_handed" : "1d6",
            },
            "thrown" : "1d6",
            "ranged" : "0d0"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 30,
                "long" : 120,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,                
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "hammer, light" : {
        "description" : "A small hammer that can be used as a weapon.",
        "type" : "simple melee",
        "cost" : "2 gp",
        "weight" : "2 lbs",
        "properties" : {
            "Light" : "When using two-weapon fighting and using this weapon as your off-hand attack, the character can add their ability modifier to the damage of the second weapon's attack provided it's light. You also don't suffer the normal disadvantage on the attack roll, which would typically apply to off-hand attacks without the 'light' property.", 
            "Thrown" : " Weapons with the thrown property can be used effectively in both melee and ranged combat, making them versatile choices for characters who want the option to attack at different ranges.",
        },
        "size" : "small",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "1d4",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "bludgeoning",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 20,
                "long" : 60,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "mace" : {
        "description" : "A club-like weapon with a heavy head on the end.",
        "type" : "simple melee",
        "cost" : "5 gp",
        "weight" : "4 lbs",
        "properties" : "None",
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d6",
                "two_handed" : "1d6",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "bludgeoning",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "quarterstaff" : {
        "description" : "A long wooden staff, often used for defense and leverage.",
        "type" : "simple melee",
        "cost" : "2 sp",
        "weight" : "4 lbs",
        "properties" : {
            "Versatile" : "When wielding a versatile weapon with one hand, you can use it as you would any other one-handed melee weapon. You would typically use your Strength modifier for both the attack and damage rolls. When wielding a versatile weapon with two hands, you gain the benefit of additional damage. This means you can use both of your hands to swing the weapon with greater force. When you use a versatile weapon in this way, you typically use your Strength modifier for the attack roll but add an extra damage die to the weapon's damage.",
        },
        "size" : "large",
        "damage" : {
            "melee" : {
                "one_handed" : "1d6",
                "two_handed" : "1d6",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "bludgeoning",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 5,
                "long" : 15,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "sickle" : {
        "description" : "A curved, hand-held agricultural tool used as a weapon.",
        "type" : "simple melee",
        "cost" : "1 gp",
        "weight" : "2 lbs",
        "properties" : {
            "Light" : "When using two-weapon fighting and using this weapon as your off-hand attack, the character can add their ability modifier to the damage of the second weapon's attack provided it's light. You also don't suffer the normal disadvantage on the attack roll, which would typically apply to off-hand attacks without the 'light' property.",
        },
        "size" : "small",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "1d4"
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "slashing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 20,
                "long" : 60,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "spear" : {
        "description" : "A pole weapon with a sharp point, either used for thrusting or throwing.",
        "type" : "simple melee",
        "cost" : "1 gp",
        "weight" : "3 lbs",
        "properties" : {
            "Thrown" : " Weapons with the thrown property can be used effectively in both melee and ranged combat, making them versatile choices for characters who want the option to attack at different ranges.", 
            "Versatile" : "When wielding a versatile weapon with one hand, you can use it as you would any other one-handed melee weapon. You would typically use your Strength modifier for both the attack and damage rolls. When wielding a versatile weapon with two hands, you gain the benefit of additional damage. This means you can use both of your hands to swing the weapon with greater force. When you use a versatile weapon in this way, you typically use your Strength modifier for the attack roll but add an extra damage die to the weapon's damage.",
        },
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d6",
                "two_handed" : "1d8",
            },
            "thrown" : "1d6",
            "ranged" : "0d0"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,                
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },   
    "crossbow, light" : {
        "description" : "A light, two-handed ranged weapon that fires bolts.",
        "type" : "simple ranged",
        "cost" : "25 gp",
        "weight" : "5 lbs",
        "properties" : {
            "Ammunition" : "The weapon requires ammunition to use. In many cases, ammunition can be recovered after combat if you take the time to search for it.", 
            "Loading" : "can only be fired once per turn, regardless of the character's number of attacks. This means that even if a character has Extra Attack and can make multiple attacks in one turn, they can only fire a loading weapon once during that turn.", 
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "1d4",
            },
            "thrown" : "1d4",
            "ranged" : "1d8"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 80,
                "long" : 320,
            },
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : "dexterity"
        },
        "loading time" : "1 action",
        "special" : "None",
        "restrictions" : {
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
    },
    "dart" : {
        "description" : "A small, throwable weapon with a pointed tip.",
        "type" : "simple ranged",
        "cost" : "5 cp",
        "weight" : "1/4 lb",
        "properties" : {
            "Finesse" : "Allows the attacker to use their Dexterity modifier instead of Strength for both the attack and damage rolls when wielding that weapon.", 
            "Thrown" : " Weapons with the thrown property can be used effectively in both melee and ranged combat, making them versatile choices for characters who want the option to attack at different ranges.",
        },
        "size" : "small",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "1d4",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 20,
                "long" : 60,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            },
        },
        "modifier" : {
            "melee" : "strength or dexterity",
            "thrown" : "strength or dexterity",
            "ranged" : "dexterity"
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "shortbow" : {
        "description" : "A relatively small and light bow, used for firing arrows.",
        "type" : "simple ranged",
        "cost" : "25 gp",
        "weight" : "2 lbs",
        "properties" : {
            "Ammunition" : "The weapon requires ammunition to use. In many cases, ammunition can be recovered after combat if you take the time to search for it.", 
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "1d4",
            },
            "thrown" : "1d4",
            "ranged" : "1d6"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 80,
                "long" : 320,
            },
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : "dexterity"
        },
        "loading time" : "1 action",
        "special" : "None",
        "restrictions" : {
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
    },
    "sling" : {
        "description" : "A simple weapon used to hurl stones or small projectiles.",
        "type" : "simple ranged",
        "cost" : "1 sp",
        "weight" : "0 lbs",
        "properties" : {
            "Ammunition" : "The weapon requires ammunition to use. In many cases, ammunition can be recovered after combat if you take the time to search for it."
        },
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "1d4",
            },
            "thrown" : "1d4",
            "ranged" : "1d4"
        },
        "damage type" : "bludgeoning",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 30,
                "long" : 120,
            },
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : "dexterity"
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "battleaxe" : {
        "description" : "A large axe designed for combat, usable with one or two hands.",
        "type" : "martial melee",
        "cost" : "10 gp",
        "weight" : "4 lbs",
        "properties" : {
            "Versatile" : "When wielding a versatile weapon with one hand, you can use it as you would any other one-handed melee weapon. You would typically use your Strength modifier for both the attack and damage rolls. When wielding a versatile weapon with two hands, you gain the benefit of additional damage. This means you can use both of your hands to swing the weapon with greater force. When you use a versatile weapon in this way, you typically use your Strength modifier for the attack roll but add an extra damage die to the weapon's damage.",
        },
        "size" : "large",
        "damage" : {
            "melee" : {
                "one_handed" : "1d8",
                "two_handed" : "1d10",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "slashing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 5,
                "long" : 15,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "flail" : {
        "description" : "A weapon consisting of a striking head attached to a handle by a flexible rope, strap, or chain.",
        "type" : "martial melee",
        "cost" : "10 gp",
        "weight" : "2 lbs",
        "properties" : "None",
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d8",
                "two_handed" : "1d8",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "bludgeoning",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "glaive" : {
        "description" : "A polearm with a heavy blade on one end.",
        "type" : "martial melee",
        "cost" : "20 gp",
        "weight" : "6 lbs",
        "properties" : {
            "Heavy" : "A minimum of 15 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.", 
            "Reach" : "Weapons with the reach property typically have a longer reach than most other melee weapons. Instead of being limited to attacking creatures in adjacent squares or spaces, a character wielding a reach weapon can make melee attacks against creatures that are 10 feet away. They can threaten and potentially make opportunity attacks against creatures that enter or exit their reach, which is typically a 10-foot radius around them. This can be advantageous for controlling the battlefield and protecting allies. Reach weapons do not impose disadvantage on attack rolls when used to attack creatures that are adjacent to the wielder. This is an important distinction from some ranged weapons, like longbows, which have disadvantage when used in melee combat.", 
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon."
        },
        "size" : "large",
        "damage" : {
            "melee" : {
                "one_handed" : "None",
                "two_handed" : "1d10",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "slashing",
        "range" : {
            "melee" : 10,
            "thrown" : {
                "normal" : 5,
                "long" : 15,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : {
            "Heavy" : "A minimum of 15 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.",
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
    },
    "greataxe" : {
        "description" : "A larger, heavier axe, typically requiring two hands.",
        "type" : "martial melee",
        "cost" : "30 gp",
        "weight" : "7 lbs",
        "properties" : {
            "Heavy" : "A minimum of 13 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.", 
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
        "size" : "large",
        "damage" : {
            "melee" : {
                "one_handed" : "None",
                "two_handed" : "1d12",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "slashing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 5,
                "long" : 15,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : {
            "Heavy" : "A minimum of 15 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.",
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
    },
    "greatsword" : {
        "description" : "A large two-handed sword with a broad blade.",
        "type" : "martial melee",
        "cost" : "50 gp",
        "weight" : "6 lbs",
        "properties" : {
            "Heavy" : "A minimum of 15 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.", 
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
        "size" : "large",
        "damage" : {
            "melee" : {
                "one_handed" : "None",
                "two_handed" : "2d6",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "slashing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 5,
                "long" : 15,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : {
            "Heavy" : "A minimum of 15 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.",
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
    },
    "halberd" : {
        "description" : "A two-handed pole weapon with an axe blade topped with a spike and a hook on the back.",
        "type" : "martial melee",
        "cost" : "20 gp",
        "weight" : "6 lbs",
        "properties" : {
            "Heavy" : "A minimum of 15 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.", 
            "Reach" : "Weapons with the reach property typically have a longer reach than most other melee weapons. Instead of being limited to attacking creatures in adjacent squares or spaces, a character wielding a reach weapon can make melee attacks against creatures that are 10 feet away. They can threaten and potentially make opportunity attacks against creatures that enter or exit their reach, which is typically a 10-foot radius around them. This can be advantageous for controlling the battlefield and protecting allies. Reach weapons do not impose disadvantage on attack rolls when used to attack creatures that are adjacent to the wielder. This is an important distinction from some ranged weapons, like longbows, which have disadvantage when used in melee combat.", 
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
        "size" : "large",
        "damage" : {
            "melee" : {
                "one_handed" : "None",
                "two_handed" : "1d10",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "slashing",
        "range" : {
            "melee" : 10,
            "thrown" : {
                "normal" : 5,
                "long" : 15,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : {
            "Heavy" : "A minimum of 15 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.",
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
    },
    "lance" : {
        "description" : "A long weapon for thrusting, typically used on horseback.",
        "type" : "martial melee",
        "cost" : "10 gp",
        "weight" : "6 lbs",
        "properties" : {
            "Reach" : "Weapons with the reach property typically have a longer reach than most other melee weapons. Instead of being limited to attacking creatures in adjacent squares or spaces, a character wielding a reach weapon can make melee attacks against creatures that are 10 feet away. They can threaten and potentially make opportunity attacks against creatures that enter or exit their reach, which is typically a 10-foot radius around them. This can be advantageous for controlling the battlefield and protecting allies. Reach weapons do not impose disadvantage on attack rolls when used to attack creatures that are adjacent to the wielder. This is an important distinction from some ranged weapons, like longbows, which have disadvantage when used in melee combat.", 
            "Special" : "Aa lance is often associated with mounted combat, and it has the 'special' property that allows it to be used one-handed when mounted. While mounted and using a lance one-handed, a character can still make melee attacks with it.",
        },
        "size" : "large",
        "damage" : {
            "melee" : {
                "one_handed" : "1d12",
                "two_handed" : "1d12"
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 10,
            "thrown" : {
                "normal" : 5,
                "long" : 15,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "Disadvantage to attack target within 5 ft.",
        "restrictions" : [
            "You have disadvantage when you use a lance to attack a target within 5 feet of you.",
            "A lance requires two hands to wield when you aren't mounted."
        ]
    },
    "longsword" : {
        "description" : "A versatile one-handed sword.",
        "type" : "martial melee",
        "cost" : "15 gp",
        "weight" : "3 lbs",
        "properties" : {
            "Versatile" : "When wielding a versatile weapon with one hand, you can use it as you would any other one-handed melee weapon. You would typically use your Strength modifier for both the attack and damage rolls. When wielding a versatile weapon with two hands, you gain the benefit of additional damage. This means you can use both of your hands to swing the weapon with greater force. When you use a versatile weapon in this way, you typically use your Strength modifier for the attack roll but add an extra damage die to the weapon's damage.",
        },
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d8",
                "two_handed" : "1d10"
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "slashing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "maul" : {
        "description" : "A large hammer-like weapon.",
        "type" : "martial melee",
        "cost" : "10 gp",
        "weight" : "10 lbs",
        "properties" : {
            "Heavy" : "A minimum of 15 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.", 
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
        "size" : "large",
        "type" : "martial melee",
        "cost" : "10 gp",
        "weight" : "6 lbs",
        "properties" : {
            "Reach" : "Weapons with the reach property typically have a longer reach than most other melee weapons. Instead of being limited to attacking creatures in adjacent squares or spaces, a character wielding a reach weapon can make melee attacks against creatures that are 10 feet away. They can threaten and potentially make opportunity attacks against creatures that enter or exit their reach, which is typically a 10-foot radius around them. This can be advantageous for controlling the battlefield and protecting allies. Reach weapons do not impose disadvantage on attack rolls when used to attack creatures that are adjacent to the wielder. This is an important distinction from some ranged weapons, like longbows, which have disadvantage when used in melee combat.", 
        },
        "size" : "large",
        "damage" : {
            "melee" : {
                "one_handed" : "2d6",
                "two_handed" : "2d6"
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 10,
            "thrown" : {
                "normal" : 5,
                "long" : 15,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "Disadvantage to attack target within 5 ft.",
        "restrictions" : {
            "Heavy" : "A minimum of 15 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.",
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        }
    },
    "morningstar" : {
        "description" : "A weapon with a spiked club head.",
        "type" : "martial melee",
        "cost" : "15 gp",
        "weight" : "4 lbs",
        "properties" : "None",
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d8",
                "two_handed" : "1d8"
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "pike" : {
        "description" : "A very long spear used predominantly by infantry.",
        "type" : "martial melee",
        "cost" : "5 gp",
        "weight" : "18 lbs",
        "properties" : {
            "Heavy" : "A minimum of 15 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.", 
            "Reach" : "Weapons with the reach property typically have a longer reach than most other melee weapons. Instead of being limited to attacking creatures in adjacent squares or spaces, a character wielding a reach weapon can make melee attacks against creatures that are 10 feet away. They can threaten and potentially make opportunity attacks against creatures that enter or exit their reach, which is typically a 10-foot radius around them. This can be advantageous for controlling the battlefield and protecting allies. Reach weapons do not impose disadvantage on attack rolls when used to attack creatures that are adjacent to the wielder. This is an important distinction from some ranged weapons, like longbows, which have disadvantage when used in melee combat.", 
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
        "size" : "large",
        "damage" : {
            "melee" : {
                "one_handed" : "None",
                "two_handed" : "1d10"
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 10,
            "thrown" : {
                "normal" : 5,
                "long" : 15,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : {
            "Heavy" : "A minimum of 15 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.",
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
    },
    "rapier" : {
        "description" : "A slender, sharply pointed sword.",
        "type" : "martial melee",
        "cost" : "25 gp",
        "weight" : "2 lbs",
        "properties" : {
            "Finesse" : "Allows the attacker to use their Dexterity modifier instead of Strength for both the attack and damage rolls when wielding that weapon.",
        },
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d8",
                "two_handed" : "1d8"
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : ["dexterity", "strength"],
            "thrown" : ["dexterity", "strength"],
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "scimitar" : {
        "description" : "A short sword with a curved blade.",
        "type" : "martial melee",
        "cost" : "25 gp",
        "weight" : "3 lbs",
        "properties" : {
            "Finesse" : "Allows the attacker to use their Dexterity modifier instead of Strength for both the attack and damage rolls when wielding that weapon.", 
            "Light" : "When using two-weapon fighting and using this weapon as your off-hand attack, the character can add their ability modifier to the damage of the second weapon's attack provided it's light. You also don't suffer the normal disadvantage on the attack roll, which would typically apply to off-hand attacks without the 'light' property.",
        },
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d6",
                "two_handed" : "1d6"
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "slashing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : ["dexterity", "strength"],
            "thrown" : ["dexterity", "strength"],
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "shortsword" : {
        "description" : "A small, light, and fast weapon for close combat.",
        "type" : "martial melee",
        "cost" : "10 gp",
        "weight" : "2 lbs",
        "properties" : {
            "Finesse" : "Allows the attacker to use their Dexterity modifier instead of Strength for both the attack and damage rolls when wielding that weapon.", 
            "Light" : "When using two-weapon fighting and using this weapon as your off-hand attack, the character can add their ability modifier to the damage of the second weapon's attack provided it's light. You also don't suffer the normal disadvantage on the attack roll, which would typically apply to off-hand attacks without the 'light' property.",
        },
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d6",
                "two_handed" : "1d6"
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : ["dexterity", "strength"],
            "thrown" : ["dexterity", "strength"],
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "trident" : {
        "description" : "A three-pronged spear, resembling a large fork.",
        "type" : "martial melee",
        "cost" : "5 gp",
        "weight" : "4 lbs",
        "properties" : {
            "Thrown" : " Weapons with the thrown property can be used effectively in both melee and ranged combat, making them versatile choices for characters who want the option to attack at different ranges.",
            "Versatile" : "When wielding a versatile weapon with one hand, you can use it as you would any other one-handed melee weapon. You would typically use your Strength modifier for both the attack and damage rolls. When wielding a versatile weapon with two hands, you gain the benefit of additional damage. This means you can use both of your hands to swing the weapon with greater force. When you use a versatile weapon in this way, you typically use your Strength modifier for the attack roll but add an extra damage die to the weapon's damage.",
        },
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d6",
                "two_handed" : "1d8"
            },
            "thrown" : "1d6",
            "ranged" : "0d0"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "war pick" : {
        "description" : "A weapon with a heavy spiked head on a long handle.",
        "type" : "martial melee",
        "cost" : "5 gp",
        "weight" : "2 lbs",
        "properties" : "None",
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d8",
                "two_handed" : "1d8"
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "warhammer" : {
        "description" : "A hammer with a head suitable for battle.",
        "type" : "martial melee",
        "cost" : "15 gp",
        "weight" : "2 lbs",
        "properties" : {
            "Versatile" : "When wielding a versatile weapon with one hand, you can use it as you would any other one-handed melee weapon. You would typically use your Strength modifier for both the attack and damage rolls. When wielding a versatile weapon with two hands, you gain the benefit of additional damage. This means you can use both of your hands to swing the weapon with greater force. When you use a versatile weapon in this way, you typically use your Strength modifier for the attack roll but add an extra damage die to the weapon's damage.",
        },
        "size" : "large",
        "damage" : {
            "melee" : {
                "one_handed" : "1d8",
                "two_handed" : "1d10",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "bludgeoning",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 5,
                "long" : 15,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "whip" : {
        "description" : "A flexible weapon made from a plaited strip of leather or similar material.",
        "type" : "martial melee",
        "cost" : "2 gp",
        "weight" : "3 lbs",
        "properties" : {
            "Finesse" : "Allows the attacker to use their Dexterity modifier instead of Strength for both the attack and damage rolls when wielding that weapon.", 
            "Reach" : "Weapons with the reach property typically have a longer reach than most other melee weapons. Instead of being limited to attacking creatures in adjacent squares or spaces, a character wielding a reach weapon can make melee attacks against creatures that are 10 feet away. They can threaten and potentially make opportunity attacks against creatures that enter or exit their reach, which is typically a 10-foot radius around them. This can be advantageous for controlling the battlefield and protecting allies. Reach weapons do not impose disadvantage on attack rolls when used to attack creatures that are adjacent to the wielder. This is an important distinction from some ranged weapons, like longbows, which have disadvantage when used in melee combat.",
        },
        "size" : "small",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "1d4",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "slashing",
        "range" : {
            "melee" : 10,
            "thrown" : {
                "normal" : 20,
                "long" : 60,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength or dexterity",
            "thrown" : "strength or dexterity",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "blowgun" : {
        "description" : "A simple ranged weapon that uses the force of one's breath to fire a dart.",
        "type" : "martial ranged",
        "cost" : "10 gp",
        "weight" : "1 lb",
        "properties" : {
            "Ammunition" : "The weapon requires ammunition to use. In many cases, ammunition can be recovered after combat if you take the time to search for it.",
            "Loading" : "can only be fired once per turn, regardless of the character's number of attacks. This means that even if a character has Extra Attack and can make multiple attacks in one turn, they can only fire a loading weapon once during that turn.",
        },
        "size" : "small",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "1d4",
            },
            "thrown" : "1d4",
            "ranged" : "1d4"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 20,
                "long" : 60,
            },
            "ranged" : {
                "normal" : 25,
                "long" : 100,
            },
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : "dexterity"
        },
        "loading time" : "1 action",
        "special" : "None",
        "restrictions" : "None"
    },
    "crossbow, hand" : {
        "description" : "A small, one-handed crossbow.",
        "type" : "martial ranged",
        "cost" : "75 gp",
        "weight" : "3 lbs",
        "properties" : {
            "Ammunition" : "The weapon requires ammunition to use. In many cases, ammunition can be recovered after combat if you take the time to search for it.", 
            "Light" : "When using two-weapon fighting and using this weapon as your off-hand attack, the character can add their ability modifier to the damage of the second weapon's attack provided it's light. You also don't suffer the normal disadvantage on the attack roll, which would typically apply to off-hand attacks without the 'light' property.", 
            "Loading" : "can only be fired once per turn, regardless of the character's number of attacks. This means that even if a character has Extra Attack and can make multiple attacks in one turn, they can only fire a loading weapon once during that turn.",
        },
        "size" : "small",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "1d4",
            },
            "thrown" : "1d4",
            "ranged" : "1d6"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 20,
                "long" : 60,
            },
            "ranged" : {
                "normal" : 30,
                "long" : 120,
            },
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : "dexterity"
        },
        "loading time" : "1 action",
        "special" : "None",
        "restrictions" : ["light"]
    },
    "crossbow, heavy" : {
        "description" : "A large, powerful crossbow that requires two hands.",
        "type" : "martial ranged",
        "cost" : "50 gp",
        "weight" : "18 lbs",
        "properties" : {
            "Ammunition" : "The weapon requires ammunition to use. In many cases, ammunition can be recovered after combat if you take the time to search for it.",
            "Heavy" : "A minimum of 15 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.", 
            "Loading" : "can only be fired once per turn, regardless of the character's number of attacks. This means that even if a character has Extra Attack and can make multiple attacks in one turn, they can only fire a loading weapon once during that turn.", 
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
        "size" : "large",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "1d4",
            },
            "thrown" : "1d4",
            "ranged" : "1d10"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 5,
                "long" : 15,
            },
            "ranged" : {
                "normal" : 100,
                "long" : 400,
            },
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : "dexterity"
        },
        "loading time" : "1 action",
        "special" : "None",
        "restrictions" : {
            "Heavy" : "A minimum of 15 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.", 
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        }
    },
    "longbow" : {
        "description" : "A tall bow used for firing arrows over longer distances.",
        "type" : "martial ranged",
        "cost" : "50 gp",
        "weight" : "2 lbs",
        "properties" : {
            "Ammunition" : "The weapon requires ammunition to use. In many cases, ammunition can be recovered after combat if you take the time to search for it.", 
            "Heavy" : "A minimum of 11 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.", 
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        },
        "size" : "large",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "1d4",
            },
            "thrown" : "1d4",
            "ranged" : "1d8"
        },
        "damage type" : "piercing",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 5,
                "long" : 15,
            },
            "ranged" : {
                "normal" : 150,
                "long" : 600,
            },
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : "dexterity"
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : {
            "Heavy" : "A minimum of 11 strength is required for a character to wield this weapon effectively. If a character's Strength is less than the required amount, they have disadvantage on attack rolls made with the weapon.", 
            "Two-handed" : "Designed to be wielded with both hands. When using a two-handed weapon, a character must grip it with both hands, which means they cannot hold another weapon or shield in their off hand while using the two-handed weapon. Two-handed weapons often deal higher damage than one-handed weapons to offset this limitation. If a character tries to wield a two-handed weapon with only one hand, they usually have disadvantage on attack rolls made with that weapon.",
        }
    },
    "net" : {
        "description" : "A large or smaler creature hit by a net is restrained until it is freed. A creature can use its action to make a DC 10 strength check, freeing itself or another creature within its reach on success. Dealing 5 slashing damage to the net (AC 10) also frees the creature without harming it, ending the effect and destroying the net.",
        "type" : "martial ranged",
        "cost" : "1 gp",
        "weight" : "3 lbs",
        "properties" : ["Special", "Thrown"],
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "0d0",
                "two_handed" : "0d0",
            },
            "thrown" : "0d0",
            "ranged" : "0d0"
        },
        "damage type" : "None",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 5,
                "long" : 15,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "None",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "Restrains target",
        "restrictions" : [
            "A net has no effect on creatures that are formless, or creatures that are Huge or larger.",
            "When you use an action, bonus action, or reaction to attack with a net, you can make only one attack regardless of the number of attacks you can normally make.",
        ]
    },
    "improvised weapon, small" : {
        "description" : "These might include objects like bottles, small rocks, or utensils.",
        "type" : "improvised",
        "cost" : "None",
        "weight" : "varies",
        "properties" : "None",
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "None",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "varies",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "dexterity",
            "thrown" : "dexterity",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "improvised weapon, medium" : {
        "description" : "Medium items are of moderate size, such as chairs, helmets, or large rocks.",
        "type" : "improvised",
        "cost" : "None",
        "weight" : "varies",
        "properties" : "None",
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "1d4",
                "two_handed" : "1d4",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "varies",
        "range" : {
            "melee" : 5,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "strength",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            }
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
    "improvised weapon, large" : {
        "description" : "These are quite bulky or heavy objects like tables, large boulders, or heavy statues",
        "type" : "improvised",
        "cost" : "None",
        "weight" : "varies",
        "properties" : "None",
        "size" : "medium",
        "damage" : {
            "melee" : {
                "one_handed" : "None",
                "two_handed" : "1d4",
            },
            "thrown" : "1d4",
            "ranged" : "0d0"
        },
        "damage type" : "varies",
        "range" : {
            "melee" : 0,
            "thrown" : {
                "normal" : 10,
                "long" : 30,
            },
            "ranged" : {
                "normal" : 0,
                "long" : 0,
            }
        },
        "modifier" : {
            "melee" : "None",
            "thrown" : "strength",
            "ranged" : {
                "normal" : 20,
                "long" : 60,
            },
        },
        "loading time" : "None",
        "special" : "None",
        "restrictions" : "None"
    },
}



















































































dnd_locations = {
    "tavern" : "A place for travelers to rest and get food and drink.",
    "blacksmith" : "A workshop for forging and repairing metal items, especially weapons and armor.",
    "magic_shop" : "A store specializing in magical items, potions, and scrolls.",
    "town_square" : "The central square in a town or city, often a hub for gatherings and markets.",
    "kings_court" : "The royal court, where the king or queen holds audiences and conducts business.",
    "temple" : "A place of worship dedicated to a specific deity or pantheon.",
    "library" : "A large collection of books, often focused on history, magic, and lore.",
    "farm" : "An area of land used for agriculture, raising crops and livestock.",
    "stable" : "A place for housing and caring for horses and other mounts.",
    "forest" : "A dense area of trees and underbrush, home to many creatures.",
    "field" : "An open area of land, often used for farming or pasture.",
    "road" : "A path or way leading from one place to another, used for travel.",
    "marketplace" : "A public area where goods are traded and sold.",
    "inn" : "A place offering lodging and food for travelers.",
    "docks" : "A place where ships are moored, often bustling with trade.",
    "alchemist" : "A workshop for creating potions and alchemical substances.",
    "guard_barracks" : "Quarters for the town or city guards.",
    "sewer" : "Underground tunnels for waste, sometimes home to unsavory creatures.",
    "castle" : "A large fortified building or set of buildings.",
    "abandoned_house" : "A deserted and dilapidated building.",
    "crypt" : "An underground chamber or vault beneath a church, used as a burial place.",
    "graveyard" : "A place where the dead are buried.",
    "catacombs" : "Underground passageways used for burial, often extensive and labyrinthine.",
    "temple_ruins" : "The remains of an ancient place of worship.",
    "mysterious_shrine" : "An enigmatic and often magical monument or altar.",
    "wizard_tower" : "A tall, often isolated structure where a wizard conducts research and experiments.",
    "orc_camp" : "A temporary settlement created by orcs or similar creatures.",
    "goblin_hideout" : "A concealed refuge used by goblins or similar creatures.",
    "dragon_lair" : "The dwelling place of a dragon, typically filled with treasure.",
    "dungeon" : "An underground prison or storage area, often beneath a castle.",
    "mine" : "A site for extracting minerals or other geological materials.",
    "underground_tunnel" : "A subterranean passage, possibly connecting different locations.",
    "hidden_cove" : "A secluded spot along the coast, often used by smugglers.",
    "enchanted_forest" : "A mystical and magical woodland.",
    "haunted_mansion" : "A large, spooky house rumored to be occupied by spirits.",
    "bandit_camp" : "A base of operations for bandits or thieves.",
    "ruined_castle" : "The remains of a once-great fortress.",
    "witch_hut" : "A small dwelling inhabited by a witch or wise person.",
    "nomad_camp" : "A temporary settlement of nomadic people.",
    "mountain_pass" : "A navigable route through a mountain range.",
    "desert_oasis" : "A fertile spot in a desert where water is found.",
    "underground_city" : "A subterranean community, possibly built by dwarves or drow.",
    "floating_island" : "A landmass that floats in the sky, often accessible by airship or magic.",
    "ghost_town" : "An abandoned village or town.",
    "vampire_castle" : "The ominous residence of a vampire or similar being.",
    "war_camp" : "A temporary site established by an army for the duration of a campaign.",
    "lighthouse" : "A tower with a light to guide ships at sea.",
    "astronomical_observatory" : "A building equipped with telescopes for observing celestial events.",
    "monastery" : "A secluded residence, usually for monks or nuns dedicated to religious life.",
    "fishing_village" : "A small coastal settlement focused on fishing.",
    "hermit_cave" : "A solitary cave dwelling, often occupied by a hermit or recluse.",
    "art_gallery" : "A space displaying various forms of art, possibly with magical paintings.",
    "bathhouse" : "A communal bathing facility, often a place for relaxation and socializing.",
    "brewery" : "A place where beer is made, potentially with unique or magical brews.",
    "brothel" : "A place offering intimate services, often shrouded in secrecy.",
    "clocktower" : "A tall structure with a clock, often central and well-known.",
    "courthouse" : "A place where legal matters are heard and judged.",
    "druid_grove" : "A sacred natural area dedicated to druidic practices.",
    "elemental_portal" : "A gateway to an elemental plane or realm.",
    "embassy" : "A diplomatic residence representing a foreign land or power.",
    "execution_grounds" : "A public area designated for carrying out capital punishments.",
    "falconry" : "A place for training and keeping falcons and other birds of prey.",
    "fortress" : "A military stronghold, often heavily fortified.",
    "gambling_den" : "A hidden or exclusive place where patrons gamble.",
    "garden" : "A well-tended area with plants, flowers, and possibly magical flora.",
    "gladiator_arena" : "A large stadium for combat and entertainment.",
    "guildhall" : "The headquarters for a guild or organization.",
    "healer's_hut" : "A small dwelling where a healer or medic offers their services.",
    "herbalist_shop" : "A store specializing in herbs, potions, and natural remedies.",
    "hidden_chamber" : "A secret room, often concealed by magic or clever mechanisms.",
    "ice_cavern" : "A cave formed in ice, often dangerously cold and slippery.",
    "jeweler" : "A shop specializing in precious stones and fine jewelry.",
    "laboratory" : "A place for scientific or alchemical experiments.",
    "magic_academy" : "An institution for learning and studying magic.",
    "mausoleum" : "A large, stately building housing tombs.",
    "mercenary_camp" : "A temporary base for hired soldiers or adventurers.",
    "mill" : "A building where grain is ground into flour.",
    "museum" : "A place where historical, cultural, or magical artifacts are displayed.",
    "necromancer's_lair" : "A hidden place where a necromancer conducts dark rituals.",
    "observatory" : "A location equipped for observing celestial events.",
    "orphanage" : "A home for children without parents.",
    "outlaw_hideout" : "A secret base for outlaws or rebels.",
    "palace" : "A grand residence for a king, queen, or other sovereign.",
    "pilgrimage_site" : "A location with religious or spiritual significance.",
    "pirate_ship" : "A vessel used by pirates, often hidden or mobile.",
    "planar_gateway" : "A portal leading to another plane of existence.",
    "quarry" : "A large, open pit from which stone is extracted.",
    "sacred_tree" : "A tree of great age and magical properties, often revered.",
    "sage's_tower" : "A solitary tower where a sage or wise person dwells.",
    "sanctuary" : "A safe haven or refuge, often sacred or magically protected.",
    "secret_society_headquarters" : "The hidden base of operations for a clandestine group.",
    "shipyard" : "A place where ships are built and repaired.",
    "slave_market" : "A controversial place where slaves are bought and sold.",
    "smuggler's_cove" : "A concealed bay used by smugglers to hide their goods.",
    "sphinx_lair" : "The dwelling of a sphinx, filled with riddles and mysteries.",
    "tomb" : "A burial place, often grand and possibly cursed or trapped.",
    "treasure_vault" : "A secure room or chamber where treasure is stored.",
    "underground_market" : "A hidden market trading in illicit or rare goods.",
    "village_green" : "The common area in the center of a village, used for gatherings.",
    "gladiator_arena" : "A large, open-air venue used for gladiatorial combat and other spectacles.",
    "art_gallery" : "A space displaying artistic works for public viewing.",
    "botanical_garden" : "A well-tended area with a wide variety of plants and flowers.",
    "brewery" : "A place where beer is made commercially.",
    "bazaar" : "A permanent marketplace or street of shops and stalls.",
    "clock_tower" : "A tower with a public clock, often a town or city landmark.",
    "courthouse" : "A building where legal matters are adjudicated.",
    "cult_hideout" : "A secret meeting place for members of a cult.",
    "dragon_nest" : "A location where a dragon lays and cares for its eggs.",
    "druid_circle" : "A sacred natural space used by druids for rituals.",
    "elf_village" : "A settlement inhabited primarily by elves, typically in harmony with nature.",
    "execution_grounds" : "A designated area for carrying out capital punishment.",
    "fey_grove" : "A mystical grove connected to the Feywild.",
    "fortress" : "A military stronghold, especially one that is heavily fortified.",
    "fountain_of_youth" : "A legendary spring that supposedly restores the youth of anyone who drinks its waters.",
    "gambling_house" : "An establishment where people can gamble.",
    "giant_castle" : "A massive stronghold built by or for giants.",
    "guild_hall" : "The headquarters for a guild or similar organization.",
    "healer's_hut" : "A small dwelling where a healer or medic provides treatment.",
    "hidden_temple" : "A secret or secluded place of worship.",
    "ice_cave" : "A natural cave formed in ice, often found in glacial areas.",
    "jeweler" : "A shop specializing in precious stones and metals.",
    "lava_pit" : "A dangerous area filled with molten lava, often volcanic.",
    "mage_college" : "An institution for magical learning and research.",
    "mercenary_camp" : "A temporary base for mercenaries or hired soldiers.",
    "monument" : "A structure erected to commemorate a notable person or event.",
    "necromancer's_lair" : "A hideout or study for a practitioner of necromancy.",
    "opera_house" : "A theatre designed for opera performances.",
    "orc_stronghold" : "A fortified settlement occupied by orcs.",
    "paladin_order" : "The headquarters or main gathering place for a group of paladins.",
    "pirate_ship" : "A vessel used by pirates.",
    "planar_gateway" : "A portal or other means of traveling between different planes of existence.",
    "rebel_hideout" : "A concealed base for rebels or resistance fighters.",
    "royal_mausoleum" : "An elaborate tomb for royalty.",
    "sacred_shrine" : "A holy or sacred place dedicated to a deity, spirit, or ancestor.",
    "sage's_tower" : "A tower or study belonging to a sage or scholar.",
    "secret_passage" : "A hidden route or pathway, often unknown to outsiders.",
    "shipyard" : "A place where ships are built and repaired.",
    "slave_market" : "A public market where slaves are bought and sold.",
    "smuggler's_den" : "A hidden place used by smugglers to store illegal goods.",
    "sphinx_lair" : "The dwelling of a sphinx, often filled with riddles and challenges.",
    "sunken_city" : "A city that has been submerged underwater.",
    "thieves_guild" : "The secret headquarters of a band of thieves.",
    "tomb" : "A large vault for burying the dead.",
    "tower_of_silence" : "A structure where bodies are laid out for excarnation.",
    "underground_lake" : "A large body of water located beneath the surface.",
    "vampire_coven" : "A gathering place or community for vampires.",
    "wizarding_school" : "An educational institution for wizards and sorcerers.",
    "ziggurat" : "A terraced pyramid of successively receding stories.",
    "alchemy_lab" : "A workshop for experimenting with and creating potions and alchemical substances.",
    "ancient_ruins" : "The remains of a once-great civilization, now in ruins.",
    "bandit_hideout" : "A secret base or hideaway used by bandits or outlaws.",
    "battleground" : "A site where a significant battle once took place.",
    "border_fortress" : "A stronghold situated on the border of a kingdom or territory.",
    "burial_ground" : "A sacred place where the dead are laid to rest.",
    "caravan_sarai" : "A roadside inn where travelers and caravans can rest and recover.",
    "cave_system" : "An extensive network of caves, potentially home to various creatures.",
    "cliffside_village" : "A small community built on the side of a cliff, often overlooking the sea.",
    "coastal_town" : "A settlement situated on the coast, typically with a harbor.",
    "collapsed_dungeon" : "An old dungeon that has partially fallen in, creating new hazards.",
    "consecrated_ground" : "A holy site blessed by a deity or religious figure.",
    "crossroads" : "A point where multiple roads intersect, often a place of decision.",
    "dark_forest" : "A dense, shadowy woodland that is often feared and avoided.",
    "deserted_island" : "An uninhabited island, potentially holding secrets or danger.",
    "dimly_lit_alleyway" : "A narrow passageway between buildings, poorly lit and potentially dangerous.",
    "dragon's_peak" : "A mountain or high place known to be the home of a dragon.",
    "drow_enclave" : "A secretive community of Drow, typically underground.",
    "dwarven_mine" : "An underground excavation site run by dwarves, rich in minerals.",
    "elemental_plane_portal" : "A gateway leading to one of the elemental planes.",
    "enchanted_meadow" : "A field or meadow imbued with magical properties.",
    "exotic_pet_market" : "A market specializing in the sale of unusual and rare creatures.",
    "faerie_circle" : "A mystical ring of mushrooms said to be a gateway to the Feywild.",
    "fallen_meteorite" : "The site where a meteorite has crashed, often with strange properties.",
    "flooded_cavern" : "An underground cave system filled with water.",
    "forgotten_temple" : "An ancient place of worship that has been lost or abandoned.",
    "frozen_wastes" : "A barren, icy landscape, inhospitable and treacherous.",
    "ghost_ship" : "A spectral vessel said to be crewed by the undead or lost souls.",
    "giant's_causeway" : "A natural formation or structure built by giants.",
    "glacial_crevasse" : "A deep crack or opening in glacial ice.",
    "goblin_market" : "A marketplace run by goblins, known for trading in strange goods.",
    "hidden_glade" : "A secluded and often magical clearing in a forest.",
    "holy_sanctuary" : "A sacred and protected place, often associated with a deity.",
    "hunting_lodge" : "A house or cabin used as a base for hunting expeditions.",
    "impoverished_slum" : "A densely populated, poor, and run-down urban area.",
    "lost_city" : "An ancient city that has been forgotten or hidden away.",
    "mage's_sanctum" : "A private and secure place where a mage conducts their studies.",
    "mercantile_district" : "A part of a city or town known for its shops and traders.",
    "mountaintop_temple" : "A temple situated on the summit of a mountain.",
    "mystical_grotto" : "A small picturesque cave known for its magical properties.",
    "noble_estate" : "The luxurious residence of a noble or wealthy family.",
    "otherworldly_portal" : "A gateway to another dimension or realm of existence.",
    "pirate_cove" : "A sheltered bay used by pirates as a hideout.",
    "plague_village" : "A village or town that has been devastated by disease.",
    "prison_colony" : "A remote settlement used to house and isolate prisoners.",
    "sacred_spring" : "A natural spring with magical or holy properties.",
    "savage_jungle" : "A dense and perilous jungle, home to dangerous creatures.",
    "scorched_battlefield" : "A site of a battle, scarred by fire and conflict.",
    "secret_society_headquarters" : "The hidden base of a secretive group or organization.",
    "shifting_sands" : "A desert area with constantly moving and changing dunes.",
    "sun_temple" : "A temple dedicated to a sun deity or the sun itself.",
    "troll_bridge" : "A bridge inhabited or guarded by a troll.",
    "underwater_city" : "A city located beneath the surface of the water.",
    "warlock's_tower" : "A tower or stronghold belonging to a warlock.",
    "ancient_battlefield" : "A historic site where a great battle once took place.",
    "arcane_university" : "An institution of higher learning for magic and wizardry.",
    "bandit_roadblock" : "A section of a road or path commandeered by bandits for ambushing travelers.",
    "border_checkpoint" : "A guard post at the boundary of a kingdom or territory.",
    "cursed_forest" : "A woodland afflicted with a dark curse, home to malevolent spirits.",
    "decaying_mansion" : "An old, dilapidated mansion with a mysterious past.",
    "desert_caravanserai" : "A resting place in the desert for caravans and travelers.",
    "druidic_henge" : "A circle of stones or wood used by druids for ceremonies.",
    "dying_village" : "A small settlement suffering from decline or a mysterious affliction.",
    "earthquake_ravine" : "A deep fissure in the ground caused by seismic activity.",
    "eldritch_altar" : "A strange and ancient altar imbued with otherworldly magic.",
    "enchanted_orchard" : "A grove of fruit trees with magical properties.",
    "exotic_bazaar" : "A marketplace known for selling rare and unusual goods.",
    "feywild_crossing" : "A location where the barrier between the Material Plane and the Feywild is thin.",
    "flooded_ruins" : "Remnants of a structure submerged under water.",
    "forgotten_crypt" : "An old, hidden burial place, possibly holding secrets or treasures.",
    "fountain_of_miracles" : "A mystical fountain rumored to have miraculous powers.",
    "giant_boneyard" : "A place where the remains of giants are found.",
    "goblin_warren" : "A network of tunnels or dens inhabited by goblins.",
    "haunted_bog" : "A swamp or marsh said to be haunted by spirits or ghosts.",
    "herbalist_cottage" : "A small house where a herbalist grows and prepares medicinal plants.",
    "hidden_canyon" : "A secluded and hard-to-reach canyon, often holding secrets.",
    "holy_pilgrimage_site" : "A destination for religious pilgrims, often with a shrine or relic.",
    "hunting_camp" : "A temporary site set up by hunters in the wilderness.",
    "ice_palace" : "A stunning structure made entirely of ice, typically in a frozen landscape.",
    "isolated_monolith" : "A single, large standing stone, often surrounded by mystery.",
    "legendary_forge" : "A fabled place where masterful weapons and armor are crafted.",
    "mage's_hideaway" : "A secluded spot where a mage can work in privacy.",
    "magical_fen" : "A wetland area with enchanting or mystical qualities.",
    "mercenary_outpost" : "A base or camp used by a group of mercenaries.",
    "moonlit_grove" : "A forest clearing that is especially beautiful and magical under the moonlight.",
    "mountain_shrine" : "A sacred place of worship located high in the mountains.",
    "necropolis" : "A vast city of the dead, filled with tombs and mausoleums.",
    "ogre_den" : "A lair or dwelling place of ogres.",
    "otherworldly_inn" : "An inn or tavern that exists between worlds or dimensions.",
    "overgrown_temple" : "An ancient temple now covered in vegetation and largely forgotten.",
    "pirate_hideaway" : "A secret base or hideout used by pirates.",
    "planar_crossroads" : "A place where multiple planes of existence intersect.",
    "poisonous_garden" : "A garden filled with dangerous and toxic plants.",
    "portal_to_the_past" : "A mystical gateway that allows travel back in time.",
    "pristine_lake" : "A beautiful and untouched lake, often in a remote location.",
    "quarantined_city" : "A city that has been isolated to contain a disease or curse.",
    "relic_hunter_camp" : "A base for adventurers who seek ancient artifacts.",
    "ritual_circle" : "A designated area for performing magical rituals.",
    "rune-covered_monolith" : "A large stone inscribed with ancient and powerful runes.",
    "sacred_grove" : "A grove of trees considered holy or blessed.",
    "savage_lands" : "An untamed and dangerous region, home to fearsome beasts.",
    "sculpture_garden" : "An outdoor garden displaying various sculptures and statues.",
    "shadowy_alley" : "A dark and potentially dangerous back alley in a city.",
    "shipwreck_cove" : "A coastal area known for numerous shipwrecks.",
    "sky_castle" : "A castle or fortress suspended in the sky, possibly accessible by magic or airship.",
    "slavers_compound" : "A fortified area where slaves are held and traded.",
    "sunken_ship" : "A shipwreck lying at the bottom of a body of water.",
    "tinkerer's_workshop" : "A workshop filled with gadgets, inventions, and mechanical contraptions.",
    "treasure_vault" : "A heavily guarded place where valuables are stored.",
    "underground_market" : "A hidden marketplace specializing in illicit goods.",
    "volcanic_crater" : "The bowl-shaped depression at the top of a volcano.",
    "astral_gate" : "A portal leading to the Astral Plane.",
    "basilisk_den" : "A dangerous lair of a basilisk, known for petrifying its victims.",
    "celestial_sanctuary" : "A serene, sacred place touched by celestial beings.",
    "crumbling_keep" : "An old, decaying fortress.",
    "dark_fairy_glen" : "A mysterious, magical clearing, home to dark fairies.",
    "demon_summoning_chamber" : "A hidden room used for calling forth demons.",
    "desecrated_church" : "A holy place that has been violated or corrupted.",
    "drake_nest" : "A nesting ground for drakes.",
    "drow_outpost" : "A surface outpost operated by the Drow.",
    "dueling_arena" : "An arena used for one-on-one combat or contests.",
    "dwarven_hall" : "A grand chamber or meeting place in a dwarven stronghold.",
    "elemental_conflux" : "A rare location where elemental energies converge.",
    "enchanted_cascade" : "A waterfall imbued with magical properties.",
    "eternal_battleground" : "A place where spectral warriors eternally clash.",
    "fae_market" : "A magical market operated by faeries and other fey beings.",
    "fallen_star_site" : "The impact site of a fallen star or meteorite.",
    "fiendish_laboratory" : "A lab used for dark experiments and fiendish research.",
    "forgotten_isle" : "An island lost to time and memory.",
    "frozen_tomb" : "An icy grave, possibly containing ancient secrets or treasures.",
    "giant's_table" : "A flat mountain summit resembling a table, used by giants.",
    "gladiator_barracks" : "Living quarters for gladiators.",
    "goblin_market" : "A bustling market run by goblins, known for its chaos.",
    "guardian_statues" : "Large statues that are said to come to life to protect a place.",
    "hag's_swamp" : "A swampy area ruled by a hag.",
    "haunted_gallery" : "An art gallery filled with cursed or haunted paintings.",
    "hermit's_hideaway" : "A secluded spot where a hermit lives in solitude.",
    "hidden_archive" : "A secret storehouse of knowledge and ancient tomes.",
    "holy_spring" : "A natural spring with sacred properties.",
    "hunting_reserve" : "A protected area where nobles hunt game.",
    "illusory_maze" : "A maze created with powerful illusions.",
    "impenetrable_fortress" : "A fortress said to be unconquerable.",
    "infested_caverns" : "Caves overrun with dangerous creatures or vermin.",
    "kraken's_lair" : "The underwater dwelling of a monstrous kraken.",
    "lich's_phylactery_vault" : "A heavily guarded location where a lich stores its phylactery.",
    "lost_expedition_camp" : "The remains of a camp used by an expedition that never returned.",
    "magical_distillery" : "A place where magical potions and elixirs are brewed in large quantities.",
    "merfolk_city" : "An underwater city inhabited by merfolk.",
    "mimic_colony" : "An area infested with mimics, disguised as ordinary objects.",
    "minotaur_maze" : "A labyrinth home to a minotaur.",
    "mystic_observatory" : "A place for studying the stars and celestial events.",
    "noble_villa" : "An opulent residence owned by a noble family.",
    "ogre_village" : "A rough settlement inhabited by ogres.",
    "oracle's_sanctum" : "The sacred place where an oracle gives prophecies.",
    "pagan_altar" : "An ancient altar used for pagan rites.",
    "palace_gardens" : "Lavish gardens surrounding a royal palace.",
    "phantom_ship" : "A ghostly vessel that sails the seas, appearing and disappearing mysteriously.",
    "pirate's_trove" : "A hidden stash of a pirate's treasure.",
    "plague_doctor's_clinic" : "A medical clinic run by a plague doctor.",
    "portal_chamber" : "A room containing a magical portal to another location.",
    "primal_stone_circle" : "A circle of ancient stones imbued with primal magic.",
    "ruined_academy" : "The remains of an educational institution, now in ruins.",
    "sacred_cavern" : "A cave revered for its spiritual significance.",
    "scrying_pool" : "A mystical pool used for divination and seeing distant places",
    "abandoned_quarry" : "A deserted site where stone was once excavated.",
    "alchemist's_study" : "A room filled with books, potions, and alchemical equipment.",
    "ancient_library" : "A vast storehouse of old books, scrolls, and knowledge.",
    "arcane_research_facility" : "A place dedicated to the study and experimentation of magic.",
    "assassin's_guildhall" : "The secretive headquarters of a guild of assassins.",
    "astral_observatory" : "A structure equipped for observing the stars and planes.",
    "bandit_cave" : "A cave serving as a hideout for bandits.",
    "celestial_gateway" : "A portal leading to the celestial planes.",
    "cliffside_temple" : "A temple built on the side of a steep cliff.",
    "collapsed_bridge" : "A bridge that has fallen into disrepair, no longer passable.",
    "coral_reef" : "A diverse underwater ecosystem made up of coral.",
    "cursed_mausoleum" : "A tomb with a curse placed upon it.",
    "deep_sea_trench" : "A long, narrow, and deep depression in the ocean floor.",
    "deserted_villa" : "An abandoned upscale house or mansion.",
    "drake_nest" : "A location where drakes (smaller dragon-like creatures) lay their eggs.",
    "drowned_city" : "A city that has been submerged underwater due to a disaster.",
    "dryad_grove" : "A grove inhabited by dryads or tree nymphs.",
    "dungeon_complex" : "An extensive underground network of cells and chambers.",
    "elemental_conflux" : "A place where elemental forces converge.",
    "enchanted_cascade" : "A waterfall with magical properties.",
    "endless_staircase" : "A mystical staircase that seems to go on infinitely.",
    "eternal_battlefield" : "A field where spectral warriors reenact old battles.",
    "fairy_ring" : "A circle of mushrooms where fairies are said to gather.",
    "floating_market" : "A marketplace situated on boats or floating platforms.",
    "foggy_moor" : "A tract of open, uncultivated land with foggy weather.",
    "forbidden_archive" : "A secret or hidden collection of banned or dangerous knowledge.",
    "forgotten_harbor" : "An old, unused harbor with abandoned ships.",
    "frost_giant_hold" : "A stronghold inhabited by frost giants.",
    "geyser_field" : "An area with multiple geysers and hot springs.",
    "giant_spider_web" : "A large area covered in the webs of giant spiders.",
    "goblin_town" : "A settlement built and inhabited by goblins.",
    "god_forged_anvil" : "A mythical anvil used by gods or god-like beings for crafting.",
    "golem_factory" : "A workshop where golems are created and assembled.",
    "grand_palace" : "A luxurious and large residence of a king, queen, or similar ruler.",
    "great_wall" : "A massive wall built for protection, spanning a great distance.",
    "haunted_crossroads" : "A junction where ghosts or spirits are said to appear.",
    "hidden_citadel" : "A fortress concealed from the outside world.",
    "high_seas" : "Open ocean, far from land, a setting for nautical adventures.",
    "hobgoblin_fort" : "A fortified camp or stronghold occupied by hobgoblins.",
    "holy_sanctum" : "A private and sacred place for worship or meditation.",
    "iceberg" : "A large floating mass of ice, typically in polar regions.",
    "illusionist's_maze" : "A labyrinth that uses illusions to confuse and bewilder.",
    "infested_sewers" : "Sewer tunnels overrun by creatures or monsters.",
    "jungle_ruins" : "The remnants of an ancient civilization in a dense jungle.",
    "kraken's_lair" : "The underwater dwelling of a kraken.",
    "lich's_tomb" : "The burial place of a lich, often filled with traps and undead.",
    "magical_distillery" : "A place where magical potions and liquids are brewed.",
    "mimic_colony" : "An area infested with mimics, creatures that disguise themselves as ordinary objects.",
    "minotaur_maze" : "A labyrinth designed by or home to a minotaur.",
    "mirror_hall" : "A hall filled with mirrors, some of which may be magical or deceptive.",
    "mushroom_forest" : "A forest dominated by giant mushrooms and fungal growths.",
    "mystic_pool" : "A small body of water with magical or divinatory properties.",
    "noble_vineyard" : "A sprawling estate of grapevines owned by a noble family.",
    "ochre_jelly_pit" : "A dangerous pit filled with ochre jelly monsters.",
    "onyx_castle" : "A castle made of or decorated with onyx, radiating dark energy.",
    "orcish_warg_pens" : "Enclosures where orcs raise and train their warg mounts.",
    "phantom_galley" : "A ghostly ship that appears and disappears mysteriously.",
    "phoenix_nest" : "The resting place of a phoenix, potentially with rejuvenating powers.",
    "pirate_lagoon" : "A sheltered bay used as a haven by pirates.",
    "abandoned_shrine" : "A once-holy place, now forgotten and possibly housing dark secrets.",
    "alpine_pass" : "A high mountain path, treacherous and often snow-covered.",
    "ancient_stepwell" : "An old, intricately constructed well with steps leading down to the water.",
    "arcane_grotto" : "A small cave filled with magical energy and phenomena.",
    "bandit's_road" : "A notorious stretch of road known for frequent bandit attacks.",
    "basilisk_den" : "A cave or area where the dangerous basilisk resides.",
    "battle-scarred_plains" : "Wide open plains marked by numerous historic battles.",
    "beholder's_lair" : "A hidden stronghold of a beholder, filled with traps and magic.",
    "bloodied_coliseum" : "An arena with a history of brutal gladiatorial combat.",
    "bone-yard" : "A place where bones accumulate, possibly from battles or monsters.",
    "burned_village" : "A village that has been destroyed by fire, now in ruins.",
    "celestial_observatory" : "A place for studying the heavens and celestial events.",
    "cursed_glacier" : "A massive moving ice formation said to be cursed.",
    "darkwood_thicket" : "A dense and shadowy part of a forest, known for being dangerous.",
    "deadly_bog" : "A swamp filled with hazardous creatures and treacherous ground.",
    "desecrated_cathedral" : "A once-sacred church that has been defiled and abandoned.",
    "druid's_cove" : "A hidden seaside area used by druids for rituals.",
    "duelist's_arena" : "A place where formal one-on-one combat takes place.",
    "dusty_caravan_trail" : "A well-traveled route used by caravans and travelers.",
    "elemental_crossing" : "A location where elemental energies intersect, creating strange effects.",
    "enchanted_tower" : "A tall, magical structure, possibly home to a wizard or sorcerer.",
    "eroded_canyons" : "Canyons shaped by centuries of erosion, creating unique formations.",
    "fairy-tale_castle" : "An impressive and fantastical castle, as if from a fairy tale.",
    "fallen_star_site" : "The impact location of a fallen star or meteorite.",
    "forgotten_isle" : "A small, uncharted island lost to time.",
    "frost_drake_cave" : "A cave inhabited by a frost drake, a dragon-like creature of ice.",
    "giant's_tableland" : "A flat mountain or plateau, said to be used by giants as a table.",
    "goblin_bazaar" : "A market run by goblins, known for trading in strange and stolen goods.",
    "golden_palace" : "A magnificent palace adorned with gold and precious stones.",
    "grave_of_heroes" : "A burial ground for legendary heroes and champions.",
    "griffin_eyrie" : "A high place where griffins nest and roost.",
    "haunted_sea" : "A stretch of ocean rumored to be haunted by ghosts or spirits.",
    "hidden_dock" : "A concealed dock used for secret or illicit meetings and trade.",
    "hollow_mountain" : "A mountain that is hollow inside, potentially hiding something within.",
    "imp_camp" : "A small, makeshift camp set up by impish creatures.",
    "invoked_maze" : "A labyrinth created by magic, with ever-changing paths.",
    "iron_mines" : "Extensive mining operations extracting iron ore.",
    "jungle_temple" : "An ancient temple hidden deep within a jungle.",
    "knight's_keep" : "A fortress or castle owned by a knight or noble.",
    "lava_flows" : "Areas where molten lava from a volcano travels downhill.",
    "ley_line_nexus" : "A place where ley lines, sources of magical energy, converge.",
    "lich's_phylactery_vault" : "A hidden and heavily guarded place where a lich stores its phylactery.",
    "lost_expedition_camp" : "The remains of a camp used by an expedition that never returned.",
    "mage's_vault" : "A secure location where a mage keeps rare and powerful artifacts.",
    "magical_oasis" : "A verdant area in a desert, with magical properties.",
    "mercantile_port" : "A bustling port known for its extensive trade activities.",
    "meteor_impact_zone" : "The site where a meteor has struck, often with strange properties.",
    "monster_breeding_grounds" : "An area where dangerous creatures breed and nest.",
    "mystic_hot_springs" : "Natural springs with magical or healing properties.",
    "necromantic_altar" : "An altar used for necromantic rituals and summonings.",
    "ogre_village" : "A settlement inhabited by ogres.",
    "old_smuggler's_tunnel" : "A hidden tunnel once used by smugglers to transport goods.",
    "abandoned_mill" : "A once-busy mill, now left to decay and rumored to be haunted.",
    "arcane_power_node" : "A location where magical energy is particularly strong and concentrated.",
    "blighted_forest" : "A section of forest afflicted by a magical or natural corruption.",
    "celestial_garden" : "A beautiful and serene garden said to be blessed by celestial beings.",
    "champion's_hall" : "A grand hall where heroes and champions are celebrated and honored.",
    "circle_of_stones" : "An ancient circle of standing stones, possibly with magical significance.",
    "crystal_cavern" : "A cave filled with glowing crystals and gemstones.",
    "cursed_statue" : "A statue rumored to bring misfortune to those who approach it.",
    "deep_sea_vent" : "A fissure in the seabed releasing hot water and minerals.",
    "demonic_portal" : "A gateway through which demonic entities can enter the world.",
    "desert_mirage" : "An illusionary image in the desert, created by refracted light.",
    "dimensional_rift" : "A tear in the fabric of reality, leading to other dimensions.",
    "dragonbone_yard" : "A place where the bones of dragons are found, often of great age.",
    "dreamweaver's_grove" : "A mystical grove said to be connected to the world of dreams.",
    "drowned_temple" : "An ancient temple now submerged underwater.",
    "druid_stone_circle" : "A sacred stone arrangement used by druids for rituals.",
    "earth_elemental_plane" : "A plane of existence dominated by the element of earth.",
    "echoing_canyon" : "A canyon where sounds echo mysteriously, sometimes with magical effects.",
    "eldritch_fissure" : "A crack in the earth emitting strange, otherworldly energies.",
    "enchanted_grotto" : "A magical cave with a tranquil pool and glowing fungi.",
    "eternal_iceberg" : "An iceberg that never melts, rumored to be magical.",
    "fallen_star_crater" : "The impact site of a fallen star, often containing rare materials.",
    "feywild_glade" : "A magical clearing connected to the Feywild.",
    "fire_elemental_plane" : "A plane of existence dominated by the element of fire.",
    "forgotten_dock" : "An old, unused dock with a few derelict boats.",
    "forsaken_crypt" : "A crypt that has been abandoned and is now home to the undead.",
    "fountain_of_fate" : "A mystical fountain said to reveal one's destiny.",
    "ghostly_ruins" : "The remnants of an ancient city, now haunted by ghosts.",
    "giant_eagle_nest" : "A large nest high in the mountains, home to giant eagles.",
    "goblin_marketplace" : "A lively, chaotic market run by goblins.",
    "godly_realm_gate" : "A rare portal leading to the realms of the gods.",
    "great_bazaar" : "A huge, sprawling market with goods from many lands.",
    "hidden_cove" : "A secluded spot along the coast, used by pirates or smugglers.",
    "holy_spring" : "A spring with water said to have healing properties.",
    "ice_fortress" : "A stronghold made entirely of ice, often in a frozen landscape.",
    "infested_swamp" : "A swamp overrun with dangerous creatures and diseases.",
    "inquisitor's_chamber" : "A room used for interrogation and judgment, often by a religious authority.",
    "iron_fortress" : "A formidable fortress constructed entirely of iron.",
    "jade_palace" : "A stunning palace decorated with jade and precious stones.",
    "lake_of_dreams" : "A lake whose waters are said to grant visions or dreams.",
    "lava_lake" : "A lake of molten lava, typically found in volcanic areas.",
    "legendary_arena" : "An ancient arena where legendary battles and contests took place.",
    "lightning_plains" : "Vast plains where lightning strikes are incredibly frequent.",
    "lost_nomad_camp" : "An abandoned campsite of a nomadic tribe.",
    "mage_guildhall" : "The headquarters of a guild of mages and sorcerers.",
    "magical_menagerie" : "A collection or exhibition of magical and exotic creatures.",
    "magma_chamber" : "A large, underground pool of molten rock.",
    "marsh_of_sorrows" : "A gloomy, fog-covered marsh with a melancholic atmosphere.",
    "maze_of_mirrors" : "A labyrinth constructed entirely of mirrors, creating a disorienting place to get lost.",
    "mystical_orrery": "An intricate mechanical model representing the cosmic order and celestial bodies.",
    "naga_lair": "A hidden dwelling of a naga, a serpent-like creature with magical abilities.",
    "necrotic_vortex": "A sinister whirlpool of dark energy, often found in cursed lands.",
    "ogre_mound": "A large, rough structure serving as a home for ogres.",
    "oracle's_sanctuary": "A secluded retreat for an oracle or seer.",
    "pagan_ritual_site": "An ancient place outdoors used for pagan rites and ceremonies.",
    "phantasmal_forest": "A forest where the line between reality and illusion is blurred.",
    "phoenix_roost": "The nesting place of a phoenix, radiant with fire and rebirth.",
    "pirate's_haven": "A secret harbor or island used by pirates as a safe haven.",
    "planar_convergence": "A rare location where different planes of existence intersect.",
    "poisoned_well": "A well whose waters have been tainted with poison.",
    "primordial_cauldron": "A mythical site where new lands and creatures are said to be born.",
    "prismatic_fountain": "A magical fountain emitting a spectrum of colored lights.",
    "quicksand_pit": "A dangerous area of sinking sand, trapping the unwary.",
    "radiant_garden": "A beautiful garden illuminated by a perpetual, magical light.",
    "relic_keeper's_trove": "A hidden storehouse of ancient and powerful relics.",
    "ruined_aqueduct": "The remains of an ancient structure used to transport water.",
    "sacred_burial_mound": "A hallowed place where revered individuals are interred.",
    "sanguine_chapel": "A chapel dedicated to a deity of blood or sacrifice.",
    "savage_battleground": "A site of frequent and brutal clashes, often over contested territory.",
    "scorched_oasis": "An oasis that has been devastated by a magical or natural disaster.",
    "sea_witch's_grotto": "An underwater cave inhabited by a sea witch.",
    "shadow_realm_entrance": "A gateway to a dark and mysterious parallel dimension.",
    "shifting_sand_dunes": "A desert area with continuously moving and changing dunes.",
    "shimmering_glacier": "A glacier known for its reflective and mesmerizing ice.",
    "sinking_island": "An island that is slowly disappearing beneath the waves.",
    "sky_temple": "A temple located high in the sky, accessible by flight or magic.",
    "slumbering_volcano": "A dormant volcano with the potential to awaken.",
    "sorcerer's_lab": "A room filled with magical devices and ingredients for spellcasting.",
    "spectral_shipwreck": "A ghostly shipwreck, visible only under certain conditions.",
    "spellbound_library": "A library where the books are enchanted with various spells.",
    "spider_queen's_web": "A large area covered in the webs of a giant spider queen.",
    "spiritual_retreat": "A place where individuals go for spiritual healing and meditation.",
    "stalactite_cavern": "A cave filled with hanging stalactites, often forming unique shapes.",
    "starfall_field": "An open field where meteors frequently land.",
    "stone_giant_canyon": "A canyon inhabited by stone giants, filled with rock formations.",
    "stormcaller_peak": "A mountain known for its constant, raging storms.",
    "submerged_ruins": "Ancient ruins that now lie beneath the water.",
    "sunken_altar": "An altar that has been submerged, possibly holding forgotten power.",
    "sunlit_grove": "A serene grove bathed in perpetual sunlight.",
    "tainted_reservoir": "A water reservoir that has been corrupted or polluted.",
    "terracotta_armory": "A hidden cache of clay soldiers and weapons.",
    "thunderous_cascade": "A powerful waterfall with deafening, thunder-like sounds.",
    "titan's_valley": "A large valley said to have been formed by the footsteps of titans.",
    "torture_chamber": "A grim room used for inflicting pain and extracting information.",
    "tranquil_pond": "A small, peaceful body of water, perfect for quiet reflection.",
    "treacherous_bridgeway": "A bridge known for its perilous condition and the dangers it presents.",
    "troglodyte_caverns": "Dark, damp caverns inhabited by troglodytes.",
    "twisted_spire": "A tall, strangely warped tower, possibly of magical origin.",
    "undead_sanctuary": "A place where the undead gather, often for a specific purpose.",
    "unyielding_ice_field": "A vast expanse of ice that never thaws.",
    "verdant_paradise": "A lush, beautiful area teeming with life and vibrancy.",
    "vortex_of_time": "A location where time behaves erratically or is warped.",
    "warped_dimension": "An alternate dimension with strange physical laws and realities.",
    "whispering_canyon": "A canyon where the wind creates eerie, whisper-like sounds.",
    "wishing_well": "A well said to grant wishes to those who throw a coin in.",
    "abyssal_pit": "A seemingly bottomless pit, rumored to connect to the Abyss.",
    "ancient_grove": "A grove of ancient trees, teeming with primal magic and wildlife.",
    "arcane_sanctum": "A secluded retreat for mages, filled with magical tomes and artifacts.",
    "bandit_outpost": "A fortified outpost used as a base by a group of bandits.",
    "barren_wasteland": "A vast, lifeless landscape, devoid of vegetation and water.",
    "blood_moon_arena": "An arena where combatants fight under the light of a blood moon.",
    "celestial_archive": "A repository of celestial knowledge and wisdom, accessible to few.",
    "clandestine_meeting_place": "A secret location for discreet meetings and exchanges.",
    "conjured_labyrinth": "A maze created by magic, its paths ever-changing.",
    "coral_palace": "An underwater palace made entirely of colorful coral.",
    "covenstead": "The gathering place of a coven of witches or warlocks.",
    "crumbling_acropolis": "The remains of an ancient city, high on a hill.",
    "crystal_spire": "A towering spire made of glowing crystal.",
    "darkwater_lake": "A lake with dark, seemingly bottomless waters.",
    "decayed_coliseum": "An ancient coliseum, now in ruins and overgrown.",
    "deepwood_hideaway": "A hidden refuge deep within a dense forest.",
    "desert_fortress": "A stronghold situated in the harsh desert.",
    "dimensional_crossway": "A nexus point where various dimensions intersect.",
    "dragon's_eyrie": "A high mountain nest where dragons roost and guard their treasure.",
    "dreaded_fane": "A temple dedicated to dark deities or malevolent forces.",
    "duskwood_copse": "A small woodland known for its perpetual twilight.",
    "elemental_forge": "A mystical forge used to craft items with elemental powers.",
    "enchanted_maze": "A magical maze with ever-shifting walls.",
    "endless_chasm": "A deep chasm that appears to have no bottom.",
    "eternal_bazaar": "A marketplace that exists in its own pocket of time.",
    "fae_wilds": "A wild, untamed land ruled by the fae.",
    "fallen_tower": "The remains of a once-tall tower, now collapsed.",
    "fiendish_dungeon": "A dungeon with connections to fiendish realms.",
    "forgotten_dell": "A secluded valley lost to time.",
    "frostbound_vault": "A vault or repository locked in eternal frost.",
    "fungal_grotto": "A cave system filled with bioluminescent fungi.",
    "gilded_palazzo": "An opulent mansion adorned with gold and fine art.",
    "glacial_fissure": "A deep crack in a glacier, leading to unknown depths.",
    "gloaming_woods": "A forest where it is always dusk, never fully day or night.",
    "gnome_tinkering_lab": "A workshop filled with gnome inventions and contraptions.",
    "god_touched_meadow": "A meadow said to have been blessed by a deity.",
    "golden_oasis": "An oasis in the desert with water that sparkles like gold.",
    "gravemoss_hollow": "A swampy area covered in thick, eerie moss.",
    "haunted_gallery": "An art gallery where the paintings are said to come alive at night.",
    "hidden_sanctuary": "A safe haven concealed from the outside world.",
    "hollow_earth_cavern": "An expansive cavern system beneath the surface.",
    "illusory_garden": "A garden where the plants and paths seem to shift and change.",
    "impregnable_fortress": "A fortress known for its impenetrable defenses.",
    "incantation_chamber": "A room designed for casting complex spells.",
    "jade_garden": "A tranquil garden with sculptures and paths made of jade.",
    "kraken_bay": "A bay rumored to be the hunting ground of a kraken.",
    "lich_king's_crypt": "The burial place of a powerful lich king.",
    "living_forest": "A forest where the trees and plants are sentient to some degree.",
    "lodestone_cavern": "A cave filled with naturally magnetic stones.",
    "looming_spire": "A tall, foreboding tower that casts a long shadow.",
    "lost_catacombs": "An underground network of tunnels and tombs, long forgotten.",
    "mage's_folly": "The ruins of a magical experiment gone awry.",
    "magma_chambers": "Large, underground pools of molten rock.",
    "merfolk_city": "An underwater city inhabited by merfolk.",
    "mirror_lake": "A lake with a surface so still it perfectly reflects the sky.",
    "mist_shrouded_isle": "An island perpetually covered in thick mist.",
    "moonlit_clearing": "A forest clearing that is bathed in moonlight.",
    "mossy_glen": "A lush, green area covered in thick moss and gentle streams.",
    "mystic_falls": "Waterfalls with a soft, ethereal glow, believed to have magical properties.",
    "netherworld_portal": "A gateway to a dark and ominous netherworld.",
    "obsidian_cliff": "A sheer cliff face made of shiny, black obsidian.",
    "old_witch's_hut": "A small hut belonging to an old witch, shrouded in mystery.",
    "onyx_quarry": "A mine where precious black onyx is extracted.",
    "opal_caves": "Caverns filled with sparkling opals and other gemstones.",
    "oracle's_peak": "A high mountain peak where a famed oracle resides.",
    "orcish_war_camp": "A temporary camp set up by orcish tribes for war expeditions.",
    "overgrown_ruins": "Ancient ruins that have been reclaimed by nature.",
    "pale_forest": "A strange forest where the trees and foliage have lost all color.",
    "phantom_isle": "An island that appears only under certain conditions.",
    "pilgrim's_road": "A well-traveled path used by pilgrims to reach a sacred destination.",
    "plague_doctor's_lair": "A secretive location where a plague doctor conducts experiments.",
    "primal_jungle": "An ancient and untouched jungle, teeming with primordial life.",
    "prison_island": "An island used exclusively to house prisoners.",
    "prophetic_springs": "Springs whose waters are said to grant visions of the future.",
    "quarantined_village": "A village sealed off due to a mysterious and dangerous plague.",
    "queen's_garden": "An exquisite and beautifully maintained garden owned by a queen.",
    "ravaged_battleground": "A site of a recent and brutal battle, still scarred and littered with remnants.",
    "realm_of_echoes": "A mystical realm where every sound echoes endlessly.",
    "rebel_base": "A secret base of operations for a group of rebels.",
    "red_desert": "A vast desert with red sand, known for its harsh conditions.",
    "resonating_chamber": "A room designed to amplify sound in mysterious ways.",
    "ritual_stone": "A large stone used for ancient and sacred rituals.",
    "ruined_sky_tower": "The remains of a tower that once reached high into the sky.",
    "sacred_springs": "Natural springs believed to have healing properties.",
    "salt_flats": "Expansive flatlands covered in salt deposits.",
    "sanguine_orchard": "An orchard where the trees bear fruit of a deep, blood-red hue.",
    "sapphire_sea": "A sea with waters of a deep blue, sparkling like sapphires.",
    "sculptor's_studio": "A workshop filled with statues and sculptures in various stages of completion.",
    "sea_monster's_realm": "A part of the ocean said to be ruled by a fearsome sea monster.",
    "serpent's_nest": "A dangerous area known to be inhabited by large, deadly serpents.",
    "shadow_castle": "A castle that seems to be perpetually shrouded in shadows.",
    "shattered_isles": "A group of islands fragmented into numerous small pieces.",
    "ship_graveyard": "A coastal area where old ships are abandoned and left to decay.",
    "silver_mine": "A mine rich in silver ore, possibly guarded or cursed.",
    "sky_dock": "A dock for airships, typically located high above the ground.",
    "slime_pits": "Pools of viscous, sticky slime, home to strange creatures.",
    "sorcery_academy": "An academic institution specializing in the study of sorcery.",
    "soulbound_library": "A library where the books are bound to the souls of their authors.",
    "spellforge": "A forge where magical weapons and artifacts are created.",
    "spider_forest": "A forest overrun with spiders and their thick webs.",
    "spiritual_oasis": "An oasis that provides not only water but also spiritual rejuvenation.",
    "starry_vale": "A secluded valley where the stars appear exceptionally bright.",
    "steaming_hot_springs": "Natural springs emitting steam and hot water, often with medicinal properties.",
    "stonehenge": "An ancient arrangement of standing stones with mysterious origins.",
    "storm_peak": "The highest point of a mountain where storms are constant.",
    "subterranean_city": "An underground city, hidden beneath the earth's surface.",
    "sunken_galleon": "An old shipwrecked galleon, lying at the bottom of the sea.",
    "sunstone_quarry": "A place where sunstones, rare and luminous rocks, are mined.",
    "sylvan_glen": "A peaceful forest clearing, often inhabited by fey creatures.",
    "thieves_guild_hideout": "A hidden underground den where a thieves' guild operates.",
    "thorned_maze": "A maze of thorny bushes, treacherous to navigate.",
    "timeless_tower": "A tower where time flows differently, causing strange temporal effects.",
    "titan's_reach": "A mountain peak said to be touched by the gods, where titans once roamed.",
    "twilight_bog": "A swampy area perpetually covered in a dim twilight.",
    "umbral_crypt": "A crypt with connections to the Shadowfell, filled with shadowy undead.",
    "unholy_altar": "An altar used for dark rituals, often hidden away from prying eyes.",
    "vampiric_manor": "A grand manor inhabited by vampires, concealed from the outside world.",
    "void_gate": "A portal to the void, a place of nothingness and emptiness.",
    "wandering_merchant_caravan": "A nomadic group of traveling merchants and traders.",
    "watcher's_perch": "A high vantage point used for surveillance and lookout.",
    "waterclock_tower": "A tower with a massive water clock that tracks the passage of time.",
    "whispering_glade": "A serene glade where the wind whispers secrets to those who listen.",
    "windship_docks": "Docks where windships, powered by elemental air, are anchored.",
    "wispwood_forest": "A forest where will-o'-wisps lead travelers astray.",
    "witchlight_cave": "A cave illuminated by eerie, magical witchlights.",
    "wooden_coliseum": "A coliseum made entirely of interlocking wooden planks.",
    "yawning_cavern": "A vast cavern with an impossibly deep chasm at its center.",
    "zephyr_isles": "A collection of floating islands, suspended in the sky by elemental magic.",
    "zombie-infested_village": "A village overrun by the undead, with a dark curse plaguing it.",
    "astral_gate": "A portal to the Astral Plane, a realm of pure thought and energy.",
    "blacksmith's_forge": "A well-equipped blacksmith's workshop, often with magical tools.",
    "celestial_chapel": "A holy chapel dedicated to celestial beings and deities.",
    "crimson_falls": "A waterfall with water that appears to be crimson in color.",
    "dreamwalker's_sanctuary": "A place where dreamwalkers enter the dreamscape.",
    "elemental_temple": "A temple attuned to one of the elemental planes.",
    "fiery_furnace": "A chamber of intense heat and flames, used for forging magical items.",
    "forgotten_catastrophe": "A location where a forgotten cataclysmic event occurred.",
    "gemstone_mine": "A mine known for its abundance of valuable gemstones.",
    "goblin_market": "A bustling marketplace where goblins trade all manner of goods.",
    "goldleaf_grove": "A grove of trees with leaves made of pure, shimmering gold.",
    "hallowed_cemetery": "A cemetery considered sacred, where many heroes are buried.",
    "harrowing_moor": "A desolate moor where eerie wails can be heard at night.",
    "hollow_hill": "A hill with a hollow interior, rumored to hide secrets.",
    "infested_swamp": "A swamp teeming with dangerous insects and reptiles.",
    "inverted_tower": "A tower that defies gravity, with rooms on the ceiling and walls.",
    "iron_dockyard": "A dockyard specializing in the construction of ironclad ships.",
    "jeweled_grotto": "A hidden grotto with walls adorned with precious jewels.",
    "labyrinthine_caves": "Caves with a complex network of twisting passages.",
    "lunar_observatory": "An observatory used for studying celestial bodies and phases of the moon.",
    "magma_forge": "A forge fueled by molten lava, used to craft powerful weapons.",
    "mirage_oasis": "An oasis that appears and disappears with the shifting sands.",
    "monastic_retreat": "A secluded retreat for monks and martial artists to meditate and train.",
    "myconid_colony": "A subterranean colony of peaceful myconids and fungi.",
    "oracle's_grove": "A sacred grove where an oracle imparts prophecies and wisdom.",
    "phoenix_nest": "A nest where phoenixes are said to be reborn in flames.",
    "platinum_mine": "A mine yielding rare and precious platinum ore.",
    "quicksilver_river": "A river with shimmering, quicksilver-like waters.",
    "radiant_canyon": "A canyon where radiant energy flows freely.",
    "aetherial_bridges": "Ancient bridges that lead to otherworldly realms.",
    "amber_forest": "A forest where the trees exude amber sap with magical properties.",
    "ancient_crypts": "A labyrinthine crypt filled with the remains of long-forgotten civilizations.",
    "aquatic_colosseum": "An underwater arena where aquatic creatures battle for entertainment.",
    "arcane_library": "A vast library filled with arcane knowledge and rare spellbooks.",
    "aurora_glacier": "A glacier that emits colorful auroras in the night sky.",
    "blazing_mesa": "A plateau where the ground is constantly ablaze with fire.",
    "boreal_grove": "A secluded grove in a snowy forest inhabited by mystical creatures.",
    "cathedral_of_whispers": "A massive cathedral known for its ghostly echoes.",
    "caverns_of_eternity": "A series of interconnected caverns where time flows differently.",
    "celestial_bazaar": "A market where celestial beings trade celestial goods.",
    "chaos_tempest": "An ever-shifting storm that defies natural laws and reality.",
    "clockwork_mansion": "A mansion with rooms that rearrange themselves in a mechanical fashion.",
    "coral_canyon": "A canyon with vibrant coral formations deep beneath the sea.",
    "crystal_garden": "A garden where crystalline plants grow, each with unique properties.",
    "dancing_light_pier": "A pier where bioluminescent creatures create a mesmerizing light show.",
    "demonforge": "A foundry where demonic blacksmiths craft infernal weapons.",
    "dreamscape_tower": "A tower where dreamers can enter shared dreamscapes.",
    "elemental_fissure": "A rift leading to elemental planes, each fissure with unique properties.",
    "emerald_mine": "A mine known for its abundant emerald deposits.",
    "enchanted_orchard": "An orchard where fruit grants magical properties when consumed.",
    "eternal_storm": "A region where a storm has raged for centuries, never subsiding.",
    "fae_circle": "A mysterious circle of mushrooms that serves as a gateway to the Feywild.",
    "forgotten_outpost": "An abandoned outpost shrouded in secrecy and rumors.",
    "frozen_wastes": "A desolate tundra covered in eternal ice and snow.",
    "gargoyle_sanctuary": "A sanctuary guarded by animated gargoyles with cryptic knowledge.",
    "gemstone_caves": "Caves with walls adorned with precious gemstones of all colors.",
    "giant's_haven": "A hidden valley where peaceful giants reside.",
    "glacial_cavern": "A cavern deep within a glacier with frozen wonders and dangers.",
    "gnome_tinkertown": "A bustling town where gnomes invent fantastical contraptions.",
    "gold_vault": "A heavily guarded vault filled with unimaginable wealth in gold.",
    "griffin_aerie": "A high mountain aerie where griffins and riders form bonds.",
    "haunted_shipwreck": "A shipwreck inhabited by vengeful spirits and undead pirates.",
    "hollow_husk": "A colossal hollowed-out husk of a giant creature, now a dwelling.",
    "illuminated_grotto": "A grotto where glowing moss and crystals light up the cavern.",
    "ironwood_forest": "A forest where the trees are as hard as iron, sought after for construction.",
    "kobold_warrens": "A vast network of tunnels inhabited by mischievous kobolds.",
    "labyrinth_of_mirrors": "A maze-like labyrinth filled with magical mirrors.",
    "lethal_marsh": "A deadly marsh teeming with venomous creatures.",
    "luminous_falls": "A waterfall that glows with a soothing and radiant light.",
    "magical_boneyard": "A graveyard of magical creatures' remains, each with residual magic.",
    "moonlit_beach": "A beach that shines brightly under the light of the moon.",
    "mossy_tombs": "Ancient tombs covered in luminous moss, believed to house great power.",
    "mystic_meadow": "A meadow where magic flows like a gentle breeze.",
    "nightmare_fen": "A swamp where nightmares become real, haunting those who enter.",
    "oracle's_garden": "A serene garden where an oracle imparts cryptic prophecies.",
    "phoenix_sanctum": "A sanctuary where phoenixes are revered and protected.",
    "platinum_temple": "A temple adorned with platinum, housing divine relics.",
    "quicksand_desert": "A desert with treacherous quicksand pits and shifting dunes.",
    "radiant_crystal_reef": "A vibrant underwater reef with radiant, living crystals.",
    "reclaimed_airship": "A sunken airship that has been transformed into an underwater lair.",
    "roaring_furnace": "A furnace with a never-ending roar, used by fire elementals.",
    "sapphire_lake": "A lake with crystal-clear waters that reflect the sky like sapphires.",
    "serpent's_nest": "A jungle where colossal serpents nest and rule as predators.",
    "shifting_sands_market": "A bustling marketplace that appears and disappears in shifting sands.",
    "silvered_woods": "A forest where the trees shimmer like silver under the moonlight.",
    "skyship_docks": "Docks where skyships of various sizes and designs are moored.",
    "spectral_bridge": "A bridge that connects the Material Plane and the Ethereal Plane.",
    "starfall_meadow": "A meadow where fallen stars have left behind otherworldly magic.",
    "stone_giant_court": "A grand court where stone giants hold council and negotiations.",
    "sunken_cathedral": "An underwater cathedral of ancient design, still filled with life.",
    "temple_of_echoes": "A temple known for its perfect acoustic properties, creating eerie echoes.",
    "thundering_mountains": "A mountain range where constant thunderstorms rage.",
    "treant_enclave": "A hidden grove where treants protect the ancient trees.",
    "undercity_market": "A bustling market beneath the streets of a grand city.",
    "unseen_college": "A mysterious college where knowledge and secrets are traded.",
    "volcanic_citadel": "A citadel built within an active volcano, harnessing its power.",
    "wailing_glacier": "A glacier where the wind and ice create eerie, mournful sounds.",
    "watcher's_vault": "A vault containing priceless relics guarded by silent watchers.",
    "whispering_canyon": "A canyon where whispers can be heard from distant realms.",
    "windchime_forest": "A forest filled with ethereal wind chimes that create soothing melodies.",
    "wyrm_haven": "A hidden sanctuary for benevolent dragons and their followers.",
    "abyssal_chasm": "A deep and winding chasm leading to the Abyss, teeming with demonic presence.",
    "adamantine_mines": "Mines where the precious metal adamantine is extracted under dangerous conditions.",
    "astral_crossroads": "A nexus of the Astral Plane, a hub for planar travelers and strange phenomena.",
    "barrow_maze": "A labyrinth of ancient burial mounds filled with restless spirits.",
    "bloodstone_vault": "A hidden chamber containing the legendary Bloodstone, a source of great power.",
    "chaos_carnival": "A traveling carnival where reality bends and chaos reigns.",
    "crimson_citadel": "A fortress built from red-stone where a bloodthirsty warlord rules.",
    "cryptic_spire": "A towering spire where enigmatic sorcerers conduct mysterious experiments.",
    "crystal_lake": "A pristine lake with crystal-clear waters, rumored to have healing properties.",
    "darkling_woods": "A sinister forest where shadows seem to have a life of their own.",
    "dreamer's_sanctuary": "A sanctuary where dreamers seek refuge from the waking world.",
    "drowned_temple": "A sunken temple to an ancient sea god, guarded by watery spirits.",
    "dustbowl_oasis": "An oasis in the midst of a vast desert, a welcome respite for travelers.",
    "echoing_caverns": "Caverns where every sound echoes endlessly, creating an eerie chorus.",
    "eldritch_crossroads": "A crossroads where the fabric of reality is thin, allowing passage to other planes.",
    "elemental_spires": "Tall spires attuned to the elements, where elemental magic flows freely.",
    "emerald_citadel": "A city carved from emerald stone, ruled by an enigmatic council.",
    "ethereal_bazaar": "A bazaar on the border of the Ethereal Plane, filled with spectral wares.",
    "feywild_glade": "A glade that occasionally opens a portal to the vibrant Feywild.",
    "fiery_pit": "A pit filled with eternal flames, where fire elementals roam.",
    "floating_isles": "Islands suspended in the sky, accessible by airships or magic.",
    "frozen_cathedral": "A cathedral carved from ice, dedicated to a goddess of winter.",
    "gargantuan_cavern": "A cavern so immense that entire ecosystems thrive within.",
    "ghost_shipyard": "An abandoned shipyard haunted by the restless spirits of shipbuilders.",
    "goblin_market": "A market run by goblins, offering exotic and bizarre goods.",
    "goldmine_galley": "A ship-shaped tavern located inside an abandoned gold mine.",
    "haunted_manor": "A manor with a tragic history, now inhabited by vengeful spirits.",
    "howling_mist": "A region perpetually covered in dense, howling mist.",
    "illithid_lair": "A hidden lair of mind flayers, masters of psychic powers.",
    "infernal_forge": "A forge deep within the Nine Hells, where infernal weapons are crafted.",
    "ivory_tower": "A towering ivory structure with arcane secrets hidden within.",
    "labyrinthine_temple": "A temple complex designed to confuse and challenge the faithful.",
    "lair_of_the_lich": "The lair of a powerful lich, filled with traps and undead guardians.",
    "living_crystal_cave": "A cave where living crystals pulsate with strange energy.",
    "luminous_moor": "A moorland where luminescent plants light up the night.",
    "mad_alchemist's_lab": "The laboratory of a mad alchemist, filled with bizarre experiments.",
    "mirror_lake": "A lake where the surface acts as a portal to alternate dimensions.",
    "mystic_caravan": "A nomadic caravan with fortune tellers and mystical artifacts.",
    "necropolis": "A city of the dead, where undead creatures roam freely.",
    "obsidian_volcano": "A volcano with obsidian flows and pockets of molten rock.",
    "oracle's_pool": "A pool of enchanted water where prophetic visions can be seen.",
    "overgrown_ruins": "Ancient ruins overrun by lush vegetation and wildlife.",
    "palace_of_whispers": "A palace where every wall whispers secrets to those who listen.",
    "phantom_ship": "A spectral ship that sails the ethereal sea, crewed by ghostly sailors.",
    "quicksilver_falls": "A waterfall where the water flows like quicksilver, granting unique properties.",
    "realm_of_mirrors": "A realm entirely made of mirrors, with shifting reflections and illusions.",
    "ruined_colosseum": "A once-glorious colosseum now in ruins, home to deadly creatures.",
    "sanguine_grove": "A grove where trees drip with blood-red sap, known for dark rituals.",
    "scorched_desert": "A desert scorched by unrelenting heat, with shifting sand dunes.",
    "serpent's_lair": "A cavern filled with serpents of various sizes, guarding hidden treasures.",
    "shadowfen_swamp": "A swamp where shadows come to life, creating eerie specters.",
    "shifting_mountain": "A mountain known for its ever-changing terrain and unpredictable shifts.",
    "silvermine": "A mine rich in silver ore, a valuable resource for crafting and trade.",
    "spire_of_stars": "A spire that pierces the night sky, said to hold cosmic secrets.",
    "starlight_garden": "A garden where starlight nourishes rare and wondrous plants.",
    "stormhold_fortress": "A fortress built to harness the power of raging storms.",
    "temple_of_the_moon": "A temple dedicated to the moon, known for lunar magic.",
    "timeless_library": "A library where time stands still, preserving ancient tomes.",
    "underworld_market": "A black market thriving in the depths of the Underdark.",
    "unseen_observatory": "An observatory where invisible astronomers study celestial bodies.",
    "violet_crystal_mine": "A mine filled with radiant violet crystals, prized by collectors.",
    "whispering_crypt": "A crypt where the dead whisper secrets to those who dare to listen.",
    "wildfire_savannah": "A savannah where spontaneous wildfires ignite and extinguish.",
    "witch's_cauldron": "A cauldron-shaped cavern where a coven of witches brew dark potions.",
    "zephyr_mountain": "A mountain where gentle breezes carry enchanting melodies.",
    "abyssal_forges": "Fiery forges deep in the Abyss where demonic weapons are crafted.",
    "ancient_coliseum": "A colossal arena where legendary battles once took place.",
    "astral_citadel": "A floating citadel in the Astral Plane, home to enigmatic beings.",
    "azure_glacier": "A glacier of striking azure ice, said to conceal ancient secrets.",
    "blackthorn_forest": "A forest where thorny black vines entangle everything in their path.",
    "bloodmoon_mountain": "A mountain where the moon appears blood-red during certain nights.",
    "cairn_of_kings": "A sacred burial site where ancient rulers were interred with great ceremony.",
    "chalice_lake": "A serene lake where a mystical chalice is said to grant visions.",
    "clockwork_city": "A city with intricate clockwork mechanisms and automated constructs.",
    "crimson_marsh": "A marshland filled with red-hued flora and eerie, foggy mists.",
    "crystal_caverns": "Caverns adorned with luminous crystals that emit soft, colorful light.",
    "demon's_spine": "A mountain range believed to be the spine of a slumbering demon lord.",
    "dreamer's_pool": "A tranquil pool where dreamers gather to share their otherworldly visions.",
    "drowned_temple": "An ancient temple now submerged in the depths of a haunted lake.",
    "echoing_cathedral": "A grand cathedral where whispers echo and prayers are amplified.",
    "elemental_crossroads": "A crossroads where the elemental planes intersect, causing elemental phenomena.",
    "ember_mine": "A mine where rare, glowing embers are extracted for arcane use.",
    "ethereal_serpent": "A giant serpent-shaped landmass floating in the Ethereal Plane.",
    "feywild_orchard": "An orchard where fruits from the Feywild grow, imbued with magic.",
    "fiery_pits": "Fiery chasms in the earth where fire elementals emerge.",
    "floating_gardens": "Gardens suspended in the sky, tended by cloud giants.",
    "frozen_chapel": "A chapel constructed from ice, dedicated to a frigid deity.",
    "gargantuan_ravine": "A massive ravine carved by titanic forces, home to colossal creatures.",
    "ghoul_market": "A market in the Shadowfell where undead traders barter for souls.",
    "gilded_temple": "A temple covered in golden leaf, where wealth and devotion collide.",
    "goblin_stronghold": "A fortified goblin stronghold, fiercely defended against intruders.",
    "golden_bloom_fields": "Fields where golden flowers bloom, believed to hold the essence of sunlight.",
    "haunted_lighthouse": "A coastal lighthouse with a ghostly keeper who guides lost ships.",
    "howling_wastes": "A desolate wasteland where the wind howls relentlessly.",
    "illuminated_cavern": "A cavern lit by glowing fungi, revealing intricate cave paintings.",
    "infernal_palace": "A palace in the Nine Hells, where devil lords scheme for power.",
    "ironhold_fortress": "A fortress built from iron, impervious to siege and attack.",
    "ivory_vault": "A vault made of ivory, safeguarding treasures of incredible value.",
    "jade_bamboo_forest": "A bamboo forest with jade-colored stalks, home to reclusive monks.",
    "labyrinth_of_lies": "A labyrinth filled with illusions and deceit, designed to confound intruders.",
    "lair_of_shadows": "A lair where shadowy beings lurk, blending seamlessly with darkness.",
    "living_statues_gallery": "A gallery where statues come to life, creating mesmerizing performances.",
    "lunar_oasis": "An oasis where moonlight nourishes rare and magical flora.",
    "magma_falls": "A waterfall of molten lava, casting a fiery glow on the surroundings.",
    "mindflayer_colony": "A hidden colony of mind flayers, masters of psionic abilities.",
    "mirrored_maze": "A maze of mirrors reflecting endless corridors, designed to disorient.",
    "necrotic_wilds": "Wastelands where necrotic energy has tainted the land, raising undead.",
    "obsidian_throne": "A throne carved from obsidian, where a dark ruler commands allegiance.",
    "oracle's_temple": "A temple where oracles divine the future, offering cryptic prophecies.",
    "overgrown_temple": "A temple overrun by lush vegetation, concealing ancient relics.",
    "palace_of_whispers": "A palace where every word spoken becomes a haunting whisper.",
    "phantom_library": "A library where phantom librarians guard knowledge from intruders.",
    "quicksilver_mines": "Mines where quicksilver is harvested, sought after by alchemists.",
    "realm_of_illusions": "A realm of ever-changing illusions, bending reality to its whims.",
    "ruined_keep": "A keep now in ruins, where echoes of past battles linger.",
    "sapphire_cave": "A cave with walls encrusted in precious sapphires, reflecting cool blue light.",
    "scorched_wasteland": "A barren wasteland scorched by unrelenting sun, devoid of life.",
    "serpent's_sanctuary": "A sanctuary where serpents are revered and protected.",
    "shadowy_grove": "A grove where darkness reigns, casting perpetual gloom.",
    "shimmering_desert": "A desert with sands that shimmer like liquid gold in the sun.",
    "shifting_portals": "A nexus of portals to other realms, shifting unpredictably.",
    "silverlight_falls": "A waterfall with silver-hued water that grants visions to those who touch it.",
    "spire_of_destiny": "A spire said to hold the key to one's true destiny.",
    "starfall_canyon": "A canyon where celestial meteors fall, said to bring blessings.",
    "sunken_shipwreck": "A shipwreck submerged in the depths, hiding lost treasures.",
    "temple_of_suns": "A temple where sun deities are revered, radiating warmth and light.",
    "timeless_tavern": "A tavern where time stands still, perfect for clandestine meetings.",
    "underworld_marketplace": "A bustling marketplace in the depths of the Underdark.",
    "unseen_gallery": "An art gallery showcasing invisible artworks, challenging perception.",
    "verdant_grove": "A lush grove where vibrant flora and fauna thrive.",
    "whispering_falls": "A waterfall where water whispers secrets to those who listen.",
    "wildwood_sanctuary": "A sanctuary in the heart of the untamed wilderness, protected by druids.",
    "witch's_cottage": "A cottage deep in the woods, home to a reclusive and powerful witch.",
    "zephyr_valley": "A valley where gentle zephyrs carry enchanting melodies on the breeze.",
    "abandoned_shipyard": "A shipyard left in disrepair, haunted by the spirits of shipbuilders.",
    "arcane_laboratory": "A laboratory filled with magical experiments and arcane apparatus.",
    "beastmaster_arena": "An arena where beastmasters showcase their trained creatures in battles.",
    "black_market": "An illicit market where stolen goods and forbidden artifacts are sold.",
    "bubbling_springs": "Natural springs with bubbling, healing waters that soothe ailments.",
    "cursed_crypt": "A crypt cursed by dark magic, where restless spirits torment intruders.",
    "divine_sanctum": "A divine sanctuary where clerics seek guidance from their deities.",
    "dreamers_respite": "A haven for dreamers and travelers to rest and share their dreams.",
    "elemental_forge": "A forge fueled by elemental fire, crafting weapons of elemental power.",
    "enchanted_garden": "A garden enchanted by fey magic, home to talking animals and enchanted flora.",
    "eternal_watchtower": "A watchtower that stands eternally vigilant, even through the ages.",
    "frostbite_peak": "A towering mountain where frost giants reside, guarding ancient relics.",
    "glowing_moor": "A moor where bioluminescent fungi create a mesmerizing, eerie glow.",
    "golden_treasury": "A treasury filled with unimaginable wealth, guarded by intricate traps.",
    "haunted_mansion": "A mansion haunted by vengeful spirits, each with a tragic tale.",
    "holy_shrine": "A shrine revered by pilgrims, believed to have divine healing powers.",
    "infinite_staircase": "A staircase that ascends infinitely, leading to otherworldly realms.",
    "jeweled_cavern": "A cavern adorned with precious gemstones, coveted by treasure hunters.",
    "kraken's_lair": "A lair where the Kraken, a legendary sea monster, rests between rampages.",
    "labyrinth_of_fate": "A labyrinth where destinies are woven and unraveled by enigmatic beings.",
    "lunar_temple": "A temple devoted to moon deities, where moonlight rituals are held.",
    "mimic's_gallery": "A gallery filled with shape-shifting mimics that mimic priceless artworks.",
    "mossy_ruins": "Ruins overgrown with ancient moss, hiding secrets of a forgotten civilization.",
    "mystic_obelisk": "An obelisk etched with mystic symbols, attracting seekers of arcane knowledge.",
    "nightmare_alley": "A shadowy alley where nightmares come to life during the witching hour.",
    "obelisk_of_ages": "An obelisk that records the history of the world in intricate carvings.",
    "phantom_opera": "An opera house where ghostly performers deliver hauntingly beautiful shows.",
    "quicksand_quagmire": "A quagmire with treacherous quicksand, where lost souls are trapped.",
    "runic_crypt": "A crypt inscribed with ancient runes, said to hold the secrets of the cosmos.",
    "sacred_cascade": "A cascade with waters blessed by the gods, purifying those who bathe in it.",
    "shadow_courtyard": "A courtyard cloaked in perpetual darkness, home to shadowy creatures.",
    "silversmith_workshop": "A workshop where skilled silversmiths craft exquisite silverware.",
    "soulforge": "A forge where souls are bound to weapons, granting them extraordinary power.",
    "spectral_tavern": "A tavern where spirits from beyond gather to share tales of the afterlife.",
    "starlit_beach": "A beach bathed in starlight, where wishes upon falling stars come true.",
    "tangled_grove": "A grove where thorny vines form intricate patterns, ensnaring those who trespass.",
    "timeless_archives": "Archives that transcend time, holding knowledge from countless epochs.",
    "titanic_coliseum": "A colossal coliseum where titans once engaged in epic battles.",
    "twilight_bazaar": "A bazaar that operates only during the twilight hours, offering mystical wares.",
    "underworld_portal": "A portal to the Underworld, guarded by sinister entities.",
    "violet_mountain": "A mountain where rare violet crystals emit a calming, ethereal light.",
    "whispering_cave": "A cave where whispers of long-forgotten secrets echo endlessly.",
    "woodland_retreat": "A hidden retreat within a forest, where druids commune with nature.",
    "xenophobe's_citadel": "A citadel where xenophobic zealots guard against outsiders.",
    "yawning_abyss": "A chasm so deep that it seems to yawn into the very bowels of the earth.",
    "zephyr_sanctuary": "A sanctuary where gentle zephyrs bring solace to troubled minds.",
    "abyssal_forge": "A forge fueled by the power of the Abyss, crafting demonic weaponry.",
    "arcane_library": "A vast library filled with arcane tomes, guarded by magical constructs.",
    "beacon_of_hope": "A towering beacon that grants hope and guidance to lost travelers.",
    "bitter_cold_tundra": "An icy tundra where bitter cold and blizzards are a constant challenge.",
    "blackened_keep": "A keep shrouded in darkness, rumored to be cursed and home to undead.",
    "briar_maze": "A labyrinthine maze of thorny briars, home to elusive and cunning creatures.",
    "celestial_orchard": "An orchard where celestial fruits possess incredible healing properties.",
    "chaotic_portal": "A portal that opens to random planes, leading to unpredictable adventures.",
    "crimson_canyon": "A canyon where the earth's crimson hue holds ancient secrets.",
    "crystal_caves": "Caves adorned with glittering crystals, illuminating the underground.",
    "cursed_gallery": "An art gallery filled with cursed paintings that come to life at night.",
    "desert_oasis": "An oasis in the scorching desert, offering respite to weary travelers.",
    "divine_pool": "A pool blessed by deities, granting visions to those who drink from it.",
    "dreamer's_haven": "A haven for dreamers, where dreams can be traded, bought, and sold.",
    "elemental_temple": "A temple devoted to elemental forces, where rituals harness their power.",
    "eternal_forest": "A forest that defies time, its ancient trees holding ancient wisdom.",
    "fiery_pit": "A pit of eternal flames, guarded by fire elementals and salamanders.",
    "forgotten_tombs": "Ancient tombs forgotten by time, holding the remains of long-lost kings.",
    "frostwood_grove": "A grove where frost-covered trees sing haunting melodies in the wind.",
    "gemstone_mine": "A mine rich in precious gemstones, coveted by miners and thieves alike.",
    "golden_temple": "A temple gilded in gold, a sanctuary of wealth and opulence.",
    "haunted_ship": "A ghostly ship that sails the ethereal seas, crewed by restless spirits.",
    "holy_spring": "A spring believed to have been touched by the divine, healing all ailments.",
    "infernal_citadel": "A citadel forged in the heart of Hell, ruled by fiendish overlords.",
    "labyrinth_of_souls": "A labyrinth where lost souls wander, seeking redemption or escape.",
    "lunar_well": "A well said to connect to the moon, offering mystical insights at night.",
    "mystic_oracle": "An oracle whose cryptic prophecies shape the fate of kingdoms.",
    "nightshade_garden": "A garden of nightshade flowers, potent in both beauty and poison.",
    "obsidian_spire": "A spire made of obsidian, said to house forbidden knowledge and horrors.",
    "phantom_shipwreck": "A shipwreck trapped between realms, home to spectral sailors.",
    "quicksilver_mine": "A mine where quicksilver flows like water, sought after by alchemists.",
    "runic_altar": "An altar inscribed with ancient runes, a site of forgotten rituals.",
    "sacred_crypt": "A crypt where relics of saints and holy artifacts are safeguarded.",
    "shadowed_hollow": "A hollow cloaked in perpetual shadow, rumored to be a portal to darkness.",
    "silvermoon_tavern": "A tavern known for its silvery moonlight, a gathering place for mystics.",
    "soulscourge_temple": "A temple where souls are cleansed and purified through sacred rites.",
    "spiritual_retreat": "A retreat for spiritual seekers, where enlightenment is the ultimate goal.",
    "starry_grove": "A grove where starlight bathes the earth, revealing hidden constellations.",
    "tainted_moor": "A moor tainted by dark magic, where malevolent forces stir in the night.",
    "thundering_falls": "A waterfall that roars with thunder, said to hold the power of storms.",
    "timeless_bazaar": "A bazaar where time has no dominion, selling relics from ages past.",
    "tower_of_sorcery": "A towering citadel of sorcery, home to enigmatic wizards and their experiments.",
    "underworld_temple": "A temple that descends into the depths, where infernal rites are conducted.",
    "void_gate": "A gate leading to the void, where unspeakable horrors lurk in the cosmic abyss.",
    "wailing_woods": "Woods where the trees wail mournful songs, haunted by spirits of the lost.",
    "waterclock_tower": "A tower with a waterclock that measures time in ripples and waves.",
    "whispers_in_the_dark": "A cavern where whispers in the dark reveal hidden truths and lies.",
    "wildfire_sanctuary": "A sanctuary where wildfires burn eternally, a symbol of primal power.",
    "witch's_cauldron": "A cauldron bubbling with mysterious brews, brewed by a secretive witch.",
    "zeppelin_dock": "A dock where fantastical zeppelins embark on journeys through the skies.",
    "abandoned_sanctuary": "A once-holy sanctuary, now forsaken and overgrown by nature.",
    "ancient_portal": "A portal that leads to a forgotten realm, where time flows differently.",
    "astral_spires": "Majestic spires that connect to the Astral Plane, inhabited by astral beings.",
    "barren_badlands": "A desolate wasteland where nothing grows, rumored to hide ancient ruins.",
    "beastmaster's_glade": "A glade where a reclusive beastmaster communicates with wild creatures.",
    "bubbling_cauldron": "A bubbling cauldron that grants mysterious visions to those who dare to peer inside.",
    "celestial_staircase": "A spiraling staircase that ascends to celestial realms, guarded by angelic sentinels.",
    "chained_volcano": "A volcano bound in chains, its fiery heart harbors a slumbering titan.",
    "coral_cathedral": "An underwater cathedral made of living coral, home to merfolk clerics.",
    "crystal_wastes": "Endless crystal wastelands, where reflections can lead to otherworldly dimensions.",
    "cursed_fountain": "A fountain cursed to grant wishes with unintended and dire consequences.",
    "dark_alleyways": "Narrow alleyways where shadowy figures conduct illicit dealings.",
    "dreamer's_vault": "A vault where dreamers' most cherished dreams are kept safe from nightmares.",
    "elemental_forges": "Forges fueled by the elements, crafting weapons of elemental power.",
    "enchanted_falls": "A waterfall enchanted to flow with a cascade of different magical effects.",
    "everbloom_grove": "A grove where flowers bloom year-round, prized by herbalists.",
    "fey_crossroads": "A mystical crossroads where fey creatures gather to trade secrets.",
    "flaming_chasm": "A chasm filled with eternal flames, home to fire-resistant creatures.",
    "forgotten_prison": "A prison where forgotten prisoners have been left to their own devices for centuries.",
    "gargoyle_garden": "A garden adorned with stone gargoyles that come to life under a full moon.",
    "gilded_labyrinth": "A labyrinth made of solid gold, guarded by constructs of opulence.",
    "grand_exposition": "A grand exposition showcasing the wonders of different realms and cultures.",
    "hallowed_grove": "A grove blessed by celestial beings, a place of healing and solace.",
    "haunted_mine": "A mine where the echoes of miners lost to cave-ins still linger.",
    "ironwood_forest": "A forest of ironwood trees, prized for their durability and mystical properties.",
    "jeweled_caves": "Caves filled with precious gems that emit radiant light when touched.",
    "lunar_sanctum": "A sanctum on the moon's surface, inhabited by lunar scholars and explorers.",
    "magma_falls": "Falls of molten lava that cascade into an underground river of fire.",
    "mirror_maze": "A maze filled with mirrors that reflect different realities and illusions.",
    "mystic_boneyard": "A boneyard where the remains of legendary creatures lie, sought after by collectors.",
    "planar_crossroads": "Crossroads where planar travelers meet to exchange knowledge and stories.",
    "radiant_citadel": "A citadel glowing with radiant energy, guarded by radiant knights.",
    "rift_in_the_sky": "A rift in the sky leading to a realm of floating islands and aerial creatures.",
    "sanguine_crypts": "Crypts filled with ancient blood magic, guarded by vampiric guardians.",
    "shadowed_mansion": "A mansion cloaked in perpetual darkness, a den of thieves and spies.",
    "silverveil_grove": "A grove where the trees have silver leaves and hold ancient secrets.",
    "soothsayer's_tent": "A tent where a mysterious soothsayer reveals glimpses of the future.",
    "soulforge_temple": "A temple where souls are forged into weapons and armor of great power.",
    "spiritual_bazaar": "A bazaar where spiritual artifacts and relics are bought and sold.",
    "starry_night_sky": "A night sky that's always filled with constellations, guiding travelers.",
    "tainted_well": "A well tainted by dark magic, granting sinister wishes to those who drink from it.",
    "thunderhead_peak": "A peak always surrounded by thunderstorms, home to storm giants.",
    "timeless_garden": "A garden where time stands still, preserving its beauty for eternity.",
    "towering_mushroom_forest": "A forest of towering mushrooms, home to fungal creatures.",
    "underworld_market": "A market in the depths of the underworld, where infernal deals are made.",
    "veiled_lake": "A lake veiled in mist, said to hide entrances to hidden realms.",
    "void_sculptor's_gallery": "A gallery where artists shape void energy into abstract sculptures.",
    "wandering_merchant_caravan": "A nomadic caravan of merchants, selling exotic goods from distant lands.",
    "whispering_canyon": "A canyon where the wind whispers secrets and hidden knowledge.",
    "wild_magic_wilderness": "A wilderness where wild magic surges unpredictably, creating chaos.",
    "witch's_cottage": "A cottage inhabited by a reclusive witch, skilled in both curses and remedies.",
    "zenith_peak": "A peak that touches the heavens, granting enlightenment to those who reach it.",
    "amber_infested_swamp": "A swamp where the waters are infused with golden amber, attracting rare insects.",
    "ancient_burial_grounds": "Burial grounds containing the remains of long-forgotten civilizations.",
    "astral_reflection_pool": "A pool that reflects the Astral Plane, granting glimpses of otherworldly beings.",
    "beacon_of_hope": "A lighthouse-like structure that guides lost souls to safety in the afterlife.",
    "celestial_nursery": "A celestial nursery where newborn celestial creatures are cared for by divine attendants.",
    "chaos_forged_citadel": "A citadel built from chaotic matter, constantly shifting its form and layout.",
    "crimson_tides_beach": "A beach where the tide washes ashore red-hued shells and mysterious relics.",
    "dreamer's_crossroads": "A crossroads where travelers' dreams often intertwine, leading to shared visions.",
    "elemental_tempest": "A location where the elements collide, creating volatile and unpredictable phenomena.",
    "enchanted_tapestries": "A chamber adorned with enchanted tapestries that come to life when touched.",
    "eternal_song_cave": "A cave where a mystical song echoes, granting inspiration to those who listen.",
    "fiery_forgotten_furnace": "A forgotten furnace that still burns with magical fire, forging elemental items.",
    "floating_observatory": "An observatory hovering in the sky, providing unparalleled views of celestial bodies.",
    "forgotten_menagerie": "A hidden menagerie filled with magical creatures from around the world.",
    "goblin_marketplace": "A marketplace run by goblins, where the most unusual goods can be found.",
    "haunted_shipwreck": "A shipwreck said to be haunted by vengeful spirits, hidden treasures within.",
    "ivory_spire_library": "A library housed in a towering ivory spire, containing ancient tomes of knowledge.",
    "living_crystal_cave": "A cave filled with living crystals that emit harmonious melodies when touched.",
    "luminous_fog_bank": "A fog bank illuminated by radiant light, leading to unknown realms.",
    "midsummer_festival_square": "A town square where a perpetual midsummer festival is celebrated.",
    "oracle's_haven": "A secluded haven where an oracle imparts cryptic visions to seekers.",
    "pandemonium_caverns": "Caverns where chaos reigns, home to unpredictable elemental creatures.",
    "radiant_crypt": "A crypt filled with the remains of paladins, their spirits offering guidance.",
    "shifting_sands_oasis": "An oasis in the midst of shifting sands, rumored to hide ancient treasures.",
    "silver_harp_glade": "A glade where a silver harp plays on its own, soothing troubled souls.",
    "spiritual_boneyard": "A boneyard where the spirits of animals and familiars rest in peace.",
    "starfall_peak": "A peak where meteor showers are a nightly occurrence, a place of celestial wonder.",
    "timeless_watchtower": "A watchtower where time is frozen, its guardian eternal and unchanging.",
    "underworld_tavern": "A tavern located deep in the underworld, a haven for weary adventurers.",
    "veil_of_shadows_forest": "A forest shrouded in shadows, home to elusive and enigmatic creatures.",
    "voidgate_arch": "An arch that leads to the Void, said to be a passage to the unknown.",
    "whisperwind_sanctuary": "A sanctuary where the wind carries messages from distant lands.",
    "wild_beast_arena": "An arena where adventurers can test their skills against powerful beasts.",
    "witchlight_moor": "A moor where mystical witchlights guide travelers through treacherous terrain.",
    "zenith_garden": "A garden where plants and flowers grow toward the zenith, defying gravity.",
    "astral_library": "A library floating in the Astral Plane, containing boundless knowledge from across the multiverse.",
    "dreamwalker's_sanctuary": "A hidden sanctuary accessible only through dreams, where dreamwalkers seek guidance.",
    "gilded_spire_bazaar": "A bustling bazaar located within a towering gilded spire, where exotic goods are traded.",
    "mystic_tidepool": "A tidepool filled with mysterious aquatic creatures and magical seaweed.",
    "voidshroud_forest": "A forest covered in an eerie voidshroud, home to creatures of darkness and shadow.",
    "starry_maze": "A labyrinthine maze with walls made of twinkling stars, where travelers navigate by constellations.",
}



