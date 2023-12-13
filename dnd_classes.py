#! /usr/bin/env python3

# ASCII Art
# https://patorjk.com/software/taag/#p=display&f=Big&t=DnD

dnd_classes = {



    "Barbarian": {
        "ASCII Art": """
  ____             _                _             
 |  _ \           | |              (_)            
 | |_) | __ _ _ __| |__   __ _ _ __ _  __ _ _ __  
 |  _ < / _` | '__| '_ \ / _` | '__| |/ _` | '_ \ 
 | |_) | (_| | |  | |_) | (_| | |  | | (_| | | | |
 |____/ \__,_|_|  |_.__/ \__,_|_|  |_|\__,_|_| |_|
 
        """,
        "Name": "Barbarian",
        "Description": "A fierce warrior of primitive background who can enter a battle rage. For some, their rage springs from a communion with fierce animal spirits. Others draw from a roiling reservoir of anger at a world full of pain. For every barbarian, rage is a power that fuels not just a battle frenzy but also uncanny reflexes, resilience, and feats of strength.",
        "Requirements" : "You must have a Strength score of 13 or higher in order to multiclass in or out of this class.",
        "Level Chart" : {
            1: {'Proficiency Bonus': '+2', 'Features': ['Rage', 'Unarmored Defense'], 'Rages': 2, 'Rage Damage': '+2'},
            2: {'Proficiency Bonus': '+2', 'Features': ['Reckless Attack', 'Danger Sense'], 'Rages': 2, 'Rage Damage': '+2'},
            3: {'Proficiency Bonus': '+2', 'Features': ['Primal Path', 'Primal Knowledge (Optional)'], 'Rages': 3, 'Rage Damage': '+2'},
            4: {'Proficiency Bonus': '+2', 'Features': ['Ability Score Improvement'], 'Rages': 3, 'Rage Damage': '+2'},
            5: {'Proficiency Bonus': '+3', 'Features': ['Extra Attack', 'Fast Movement'], 'Rages': 3, 'Rage Damage': '+2'},
            6: {'Proficiency Bonus': '+3', 'Features': ['Path feature'], 'Rages': 4, 'Rage Damage': '+2'},
            7: {'Proficiency Bonus': '+3', 'Features': ['Feral Instinct', 'Instinctive Pounce (Optional)'], 'Rages': 4, 'Rage Damage': '+2'},
            8: {'Proficiency Bonus': '+3', 'Features': ['Ability Score Improvement'], 'Rages': 4, 'Rage Damage': '+2'},
            9: {'Proficiency Bonus': '+4', 'Features': ['Brutal Critical (1 die)'], 'Rages': 4, 'Rage Damage': '+3'},
            10: {'Proficiency Bonus': '+4', 'Features': ['Path feature', 'Primal Knowledge (Optional)'], 'Rages': 4, 'Rage Damage': '+3'},
            11: {'Proficiency Bonus': '+4', 'Features': ['Relentless Rage'], 'Rages': 4, 'Rage Damage': '+3'},
            12: {'Proficiency Bonus': '+4', 'Features': ['Ability Score Improvement'], 'Rages': 5, 'Rage Damage': '+3'},
            13: {'Proficiency Bonus': '+5', 'Features': ['Brutal Critical (2 dice)'], 'Rages': 5, 'Rage Damage': '+3'},
            14: {'Proficiency Bonus': '+5', 'Features': ['Path feature'], 'Rages': 5, 'Rage Damage': '+3'},
            15: {'Proficiency Bonus': '+5', 'Features': ['Persistent Rage'], 'Rages': 5, 'Rage Damage': '+3'},
            16: {'Proficiency Bonus': '+5', 'Features': ['Ability Score Improvement'], 'Rages': 5, 'Rage Damage': '+4'},
            17: {'Proficiency Bonus': '+6', 'Features': ['Brutal Critical (3 dice)'], 'Rages': 6, 'Rage Damage': '+4'},
            18: {'Proficiency Bonus': '+6', 'Features': ['Indomitable Might'], 'Rages': 6, 'Rage Damage': '+4'},
            19: {'Proficiency Bonus': '+6', 'Features': ['Ability Score Improvement'], 'Rages': 6, 'Rage Damage': '+4'},
            20: {'Proficiency Bonus': '+6', 'Features': ['Primal Champion'], 'Rages': 'Unlimited', 'Rage Damage': '+4'}
        },
        "Features": {},
        "Hit Die": '1d12',
        "Proficiencies": {
            'Armor': ['Light armor', 'medium armor', 'shields'],
            'Weapons': ['Simple weapons', 'martial weapons'],
            'Tools': 'None',
            "Spellcasting Modifier" : "None",
            'Saving Throws': ['Strength', 'Constitution'],
            'Skills': {
                'Choose Number' : 2,
                'Choose From' :  ['animal handling', 'athletics', 'intimidation', 'nature', 'perception', 'survival']
            },
            "Languages": []
        },
        "Equipment": {
            'Choices' : {
                'Choice 1' : {
                    'greataxe' : 1,
                    'any martial melee weapon' : 1
                    },
                'Choice 2' : {
                    'handaxe': 2,
                    'any simple weapon' : 1
                },
            },
            "Start With" : {
                "explorer's pack" : 1,
                "javelins" : 4
            }
        },
        "Attribute Priority" : ["strength", "constitution", "dexterity", "wisdom", "charisma", "intelligence"],
        "Spells" : {
            "Spellcasting": "None",
            "Spellcasting Modifier": "None",
            "Spell Attack Modifier": "None",
            "Spell DC Save": "None",
            "Preparation": "None",
            "Recovery": "None",
            "Spell Slots": "None",
            "Spells Known": "None",
            "Change Up": "None",
            "Progression": "None",
            "Requirements": "None",
            "Key Difference": "None",
            "Uniqueness": "None",
            "Magic Lore": "None",
            "All Class Spells" : "None"
        }
    },



    "Bard": {
        "ASCII Art": """
  ____                _ 
 |  _ \              | |
 | |_) | __ _ _ __ __| |
 |  _ < / _` | '__/ _` |
 | |_) | (_| | | | (_| |
 |____/ \__,_|_|  \__,_| 

        """,
        "Name": "Bard",
        "Description": "An inspiring magician whose power echoes the music of creation. Whether scholar, skald, or scoundrel, a bard weaves magic through words and music to inspire allies, demoralize foes, manipulate minds, create illusions, and even heal wounds. The bard is a master of song, speech, and the magic they contain.",
        "Requirements" : "You must have a Charisma score of 13 or higher in order to multiclass in or out of this class.",
        "Level Chart" : {
            1: {'Proficiency Bonus': '+2','Features': 'Spellcasting, Bardic Inspiration (d6)','Cantrips Known': 2,'Spells Known': 4,'1st': 2,'2nd': '-','3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            2: {'Proficiency Bonus': '+2','Features': 'Jack of All Trades, Song of Rest (d6), Magical Inspiration (Optional)','Cantrips Known': 2,'Spells Known': 5,'1st': 3,'2nd': '-','3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            3: {'Proficiency Bonus': '+2','Features': 'Bard College, Expertise','Cantrips Known': 2,'Spells Known': 6,'1st': 4,'2nd': 2,'3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            4: {'Proficiency Bonus': '+2','Features': 'Ability Score Improvement, Bardic Versatility (Optional)','Cantrips Known': 3,'Spells Known': 7,'1st': 4,'2nd': 3,'3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            5: {'Proficiency Bonus': '+3','Features': 'Bardic Inspiration (d8), Font of Inspiration','Cantrips Known': 3,'Spells Known': 8,'1st': 4,'2nd': 3,'3rd': 2,'4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            6: {'Proficiency Bonus': '+3','Features': 'Countercharm, Bard College feature','Cantrips Known': 3,'Spells Known': 9,'1st': 4,'2nd': 3,'3rd': 3,'4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            7: {'Proficiency Bonus': '+3','Features': ' ','Cantrips Known': 3,'Spells Known': 10,'1st': 4,'2nd': 3,'3rd': 3,'4th': 1,'5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            8: {'Proficiency Bonus': '+3','Features': 'Ability Score Improvement, Bardic Versatility (Optional)','Cantrips Known': 3,'Spells Known': 11,'1st': 4,'2nd': 3,'3rd': 3,'4th': 2,'5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            9: {'Proficiency Bonus': '+4','Features': 'Song of Rest (d8)','Cantrips Known': 3,'Spells Known': 12,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 1,'6th': '-','7th': '-','8th': '-','9th': '-',},
            10: {'Proficiency Bonus': '+4','Features': 'Bardic Inspiration (d10), Expertise, Magical Secrets','Cantrips Known': 4,'Spells Known': 14,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': '-','7th': '-','8th': '-','9th': '-',},
            11: {'Proficiency Bonus': '+4','Features': ' ','Cantrips Known': 4,'Spells Known': 15,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': '-','8th': '-','9th': '-',},
            12: {'Proficiency Bonus': '+4','Features': 'Ability Score Improvement, Bardic Versatility (Optional)','Cantrips Known': 4,'Spells Known': 15,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': '-','8th': '-','9th': '-',},
            13: {'Proficiency Bonus': '+5','Features': 'Song of Rest (d10)','Cantrips Known': 4,'Spells Known': 16,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': '-','9th': '-',},
            14: {'Proficiency Bonus': '+5','Features': 'Magical Secrets, Bard College feature','Cantrips Known': 4,'Spells Known': 18,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': '-','9th': '-',},
            15: {'Proficiency Bonus': '+5','Features': 'Bardic Inspiration (d12)','Cantrips Known': 4,'Spells Known': 19,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': '-',},
            16: {'Proficiency Bonus': '+5','Features': 'Ability Score Improvement, Bardic Versatility (Optional)','Cantrips Known': 4,'Spells Known': 19,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': '-',},
            17: {'Proficiency Bonus': '+6','Features': 'Song of Rest (d12)','Cantrips Known': 4,'Spells Known': 20,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': 1,},
            18: {'Proficiency Bonus': '+6','Features': 'Magical Secrets','Cantrips Known': 4,'Spells Known': 22,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 1,'7th': 1,'8th': 1,'9th': 1,},
            19: {'Proficiency Bonus': '+6','Features': 'Ability Score Improvement, Bardic Versatility (Optional)','Cantrips Known': 4,'Spells Known': 22,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 2,'7th': 1,'8th': 1,'9th': 1,},
            20: {'Proficiency Bonus': '+6','Features': 'Superior Inspiration','Cantrips Known': 4,'Spells Known': 22,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 2,'7th': 2,'8th': 1,'9th': 1,}
        },
        "Features": {},
        "Hit Die": '1d8',
        "Proficiencies": {
            'Armor': 'Light armor',
            'Weapons': 'Simple weapons, hand crossbows, longswords, rapiers, shortswords',
            'Tools': 'Three musical instruments of your choice',
            "Spellcasting Modifier" : "Charisma",
            'Saving Throws': ['Dexterity', 'Charisma'],
            'Skills': {
                'Choose Number' : 3,
                'Choose From' :  ['acrobatics','animal handling','arcana','athletics','deception','history','insight','intimidation','investigation','medicine','nature','perception','performance','persuasion','religion','sleight of hand','stealth', 'survival']
            },
            "Languages": []
        },
        "Equipment": {
            'Choices' : {
                'Choice 1' : {
                    'rapier' : 1,
                    'longsword' : 1,
                    'any simple weapon' : 1
                    },
                'Choice 2' : {
                    "diplomat's pack": 1,
                    "entertainer's pack" : 1
                },
                'Choice 3' : {
                    'lute': 1,
                    'any other musical instrument' : 1
                },
            },
            "Start With" : {
                "lether armor" : 1,
                "dagger" : 1
            }            
        },
        "Attribute Priority" : ['charisma', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'strength'],
        "Spells" : {
            "Spellcasting": "Bards use the power of music and performance to cast spells. They combine the arts with magical abilities, using their talents to weave magic through song, poetry, or other forms of artistic expression.",
            "Spellcasting Modifier": "Charisma",
            "Spell Attack Modifier": "Proficiency bonus + Charisma modifier",
            "Spell DC Save": "8 + Proficiency bonus + Charisma modifier",
            "Preparation": "Bards do not prepare spells in the traditional sense. They have a list of spells known and can cast any spell from that list as long as they have spell slots available.",
            "Recovery": "Bards recover their spell slots after a long rest. They do not have the option for short rest recovery like some other classes.",
            "Spell Slots": "Bards have a limited number of spell slots per day, which are divided into spell levels. They can use these slots to cast their spells.",
            "Spells Known": "Bards start with a certain number of spells known based on their level, and they learn new spells as they level up.",
            "Change Up": "Bards can change their known spells whenever they level up. They have the flexibility to adapt to different situations by selecting new spells.",
            "Progression": "Bards have subclasses, such as the College of Lore and the College of Valor, which provide additional spells and modify their spellcasting abilities.",
            "Requirements": "Bards often use musical instruments or their voice as a focus for their spells, but they can cast spells without any material components.",
            "Key Difference": "Bards are unique in their ability to learn spells from any class's spell list at higher levels, making them versatile spellcasters.",
            "Uniqueness": "Bards can use their Bardic Inspiration feature to enhance their spells, allowing them to add a bonus to the roll of a creature affected by their spells.",
            "Magic Lore": "Bards often have a deep understanding of the history and stories associated with magic, and their spellcasting is intertwined with their artistic talents.",
            "All Class Spells" : {
                "Cantrips" : ["Blade Ward","Dancing Lights","Friends","Light","Mage Hand","Mending","Message","Minor Illusion","Prestidigitation","Thunderclap","True Strike","Vicious Mockery"],
                "1st" : ["Animal Friendship","Bane","Charm Person","Comprehend Languages","Cure Wounds","Detect Magic","Disguise Self","Dissonant Whispers","Distort Value","Earth Tremor","Faerie Fire","Feather Fall","Healing Word","Heroism","Identify","Illusory Script","Longstrider","Silent Image","Silvery Barbs","Sleep","Speak with Animals","Tasha's Hideous Laughter","Thunderwave","Unseen Servant"],
                "2nd" : ["Animal Messenger","Blindness/Deafness","Borrowed Knowledge","Calm Emotions","Cloud of Daggers","Crown of Madness","Detect Thoughts","Enhance Ability","Enthrall","Gift of Gab","Heat Metal","Hold Person","Invisibility","Kinetic Jaunt","Knock","Lesser Restoration","Locate Animals or Plants","Locate Object","Magic Mouth","Nathair's Mischief","Phantasmal Force","Pyrotechnics","See Invisibility","Shatter","Silence","Skywrite","Spray Of Cards","Suggestion","Warding Wind","Zone of Truth"],
                "3rd" : ["Antagonize","Bestow Curse","Catnap","Clairvoyance","Dispel Magic","Enemies Abound","Fast Friends","Fear","Feign Death","Glyph of Warding","Hypnotic Pattern","Leomund's Tiny Hut","Major Image","Motivational Speech","Nondetection","Plant Growth","Sending","Speak with Dead","Speak with Plants","Stinking Cloud","Tongues"],
                "4th" : ["Charm Monster","Compulsion","Confusion","Dimension Door","Freedom of Movement","Greater Invisibility","Hallucinatory Terrain","Locate Creature","Polymorph","Raulothim's Psychic Lance"],
                "5th" : ["Animate Objects","Awaken","Dominate Person","Dream","Geas","Greater Restoration","Hold Monster","Legend Lore","Mass Cure Wounds","Mislead","Modify Memory","Planar Binding","Raise Dead","Scrying","Seeming","Skill Empowerment","Synaptic Static","Teleportation Circle"],
                "6th" : ["Eyebite","Find the Path","Guards and Wards","Mass Suggestion","Otto's Irresistible Dance","Programmed Illusion","True Seeing"],
                "7th" : ["Etherealness","Forcecage","Mirage Arcane","Mordenkainen's Magnificent Mansion","Mordenkainen's Sword","Prismatic Spray","Project Image","Regenerate","Resurrection","Symbol","Teleport"],
                "8th" : ["Dominate Monster","Feeblemind","Glibness","Mind Blank","Power Word: Stun"],
                "9th" : ["Foresight","Mass Polymorph","Power Word: Heal","Power Word: Kill","Psychic Scream","True Polymorph"]
            }
        }
    },



    "Cleric": {
        "ASCII Art": """
   _____ _           _      
  / ____| |         (_)     
 | |    | | ___ _ __ _  ___ 
 | |    | |/ _ \ '__| |/ __|
 | |____| |  __/ |  | | (__ 
  \_____|_|\___|_|  |_|\___|

        """,
        "Name": "Cleric",
        "Description": "A priestly champion who wields divine magic in service of a higher power. Clerics are intermediaries between the mortal world and the distant planes of the gods. As varied as the gods they serve, clerics strive to embody the handiwork of their deities. No ordinary priest, a cleric is imbued with divine magic.",
        "Requirements" : "You must have a Wisdom score of 13 or higher in order to multiclass in or out of this class.",
        "Level Chart" : {
            1: {'Proficiency Bonus': '+2','Features': 'Spellcasting, Divine Domain','Cantrips Known': 3,'1st': 2,'2nd': '-','3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            2: {'Proficiency Bonus': '+2','Features': 'Channel Divinity (x1), Divine Domain feature, Harness Divine Power (Optional)','Cantrips Known': 3,'1st': 3,'2nd': '-','3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            3: {'Proficiency Bonus': '+2','Features': '-','Cantrips Known': 3,'1st': 4,'2nd': 2,'3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            4: {'Proficiency Bonus': '+2','Features': 'Ability Score Improvement, Cantrip Versatility (Optional)','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            5: {'Proficiency Bonus': '+3','Features': 'Destroy Undead (CR 1/2)','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 2,'4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            6: {'Proficiency Bonus': '+3','Features': 'Channel Divinity (x2), Divine Domain feature','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            7: {'Proficiency Bonus': '+3','Features': '-','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 1,'5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            8: {'Proficiency Bonus': '+3','Features': 'Ability Score Improvement, Destroy Undead (CR 1), Divine Domain feature, Cantrip Versatility (Optional)','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 2,'5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            9: {'Proficiency Bonus': '+4','Features': '-','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 1,'6th': '-','7th': '-','8th': '-','9th': '-'},
            10: {'Proficiency Bonus': '+4','Features': 'Divine Intervention','Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': '-','7th': '-','8th': '-','9th': '-'},
            11: {'Proficiency Bonus': '+4','Features': 'Destroy Undead (CR 2)','Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': '-','8th': '-','9th': '-'},
            12: {'Proficiency Bonus': '+4','Features': 'Ability Score Improvement, Cantrip Versatility (Optional)','Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': '-','8th': '-','9th': '-'},
            13: {'Proficiency Bonus': '+5','Features': '-','Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': '-','9th': '-'},
            14: {'Proficiency Bonus': '+5','Features': 'Destroy Undead (CR 3)','Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': '-','9th': '-'},
            15: {'Proficiency Bonus': '+5','Features': '-','Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': '-'},
            16: {'Proficiency Bonus': '+5','Features': 'Ability Score Improvement, Cantrip Versatility (Optional)','Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': '-'},
            17: {'Proficiency Bonus': '+6','Features': 'Destroy Undead (CR 4), Divine Domain feature','Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': 1},
            18: {'Proficiency Bonus': '+6','Features': 'Channel Divinity (x3)','Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 1,'7th': 1,'8th': 1,'9th': 1},
            19: {'Proficiency Bonus': '+6','Features': 'Ability Score Improvement, Cantrip Versatility (Optional)','Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 1,'7th': 1,'8th': 1,'9th': 1},
            20: {'Proficiency Bonus': '+6','Features': 'Divine Intervention improvement','Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 2,'7th': 1,'8th': 1,'9th': 1}
        },
        "Features": {},
        "Hit Die": '1d8',
        "Proficiencies": {
            'Armor': 'Light armor, medium armor, shields',
            'Weapons': 'All simple weapons',
            'Tools': 'None',
            "Spellcasting Modifier" : "Wisdom",
            'Saving Throws': ['Wisdom', 'Charisma'],
            'Skills': {
                'Choose Number' : 2,
                'Choose From' :  ['history', 'insight', 'medicine', 'persuasion', 'religion']
            },
            "Languages": []
        },
        "Equipment": {
            'Choices' : {
                'Choice 1' : {
                    'mace' : 1,
                    'warhammer (if proficient)' : 1,
                    },
                'Choice 2' : {
                    "scale mail": 1,
                    "leather armor" : 1,
                    "chain mail (if proficient)" : 1
                },
                'Choice 3' : {
                    'light crossbow and 20 bolts': 1,
                    'any simple weapon' : 1
                },
                'Choice 4' : {
                    "priest's pack" : 1,
                    "explorer's pack" : 1
                },
            },
            "Start With" : {
                "shield" : 1,
                "holy symbol" : 1
            }
        },
        "Attribute Priority" : ['wisdom', 'constitution', 'strength', 'charisma', 'dexterity', 'intelligence'],
        "Spells" : {
            "Spellcasting": "Clerics draw their magical power from their devotion to a deity or a divine force. They serve as conduits for divine energy and channel it through prayers and rituals to cast spells.",
            "Spellcasting Modifier": "Wisdom",
            "Spell Attack Modifier": "Proficiency bonus + Wisdom modifier",
            "Spell DC Save": "8 + Proficiency bonus + Wisdom modifier",
            "Preparation": "Clerics prepare their spells each day by communing with their deity through prayer. They choose a specific number of spells from their cleric spell list to have prepared for the day.",
            "Recovery": "Clerics recover their expended spell slots after a long rest. They do not have the option for short rest recovery like some other classes.",
            "Spell Slots": "Clerics have a limited number of spell slots per day, which are divided into spell levels. They can use these slots to cast their prepared spells.",
            "Spells Known": "Clerics have access to their entire cleric spell list, but they must prepare a subset of these spells each day for casting.",
            "Change Up": "Clerics can change their prepared spells each day after a long rest, allowing them to adapt to different challenges.",
            "Progression": "Clerics choose a Divine Domain, such as Life or War, which grants them additional spells and abilities related to their chosen domain.",
            "Requirements": "Clerics often use holy symbols or focus items associated with their deity to aid in spellcasting, but they can cast spells without material components.",
            "Key Difference": "Clerics have a unique ability called Channel Divinity, which allows them to use powerful divine features tied to their chosen domain.",
            "Uniqueness": "Clerics can also prepare cure spells as many times as they like, giving them the ability to heal their allies effectively.",
            "Magic Lore": "Clerics have deep religious and spiritual knowledge and often serve as spiritual leaders within their communities.",
            "All Class Spells" : {
                "Cantrips" : ["Guidance","Light","Mending","Resistance","Sacred Flame","Spare the Dying","Thaumaturgy","Toll the Dead","Word of Radiance"],
                "1st" : ["Bane","Bless","Ceremony","Command","Create or Destroy Water","Cure Wounds","Detect Evil and Good","Detect Magic","Detect Poison and Disease","Guiding Bolt","Healing Word","Inflict Wounds","Protection from Evil and Good","Purify Food and Drink","Sanctuary","Shield of Faith"],
                "2nd" : ["Aid","Augury","Blindness/Deafness","Borrowed Knowledge","Calm Emotions","Continual Flame","Enhance Ability","Find Traps","Gentle Repose","Hold Person","Lesser Restoration","Locate Object","Prayer of Healing","Protection from Poison","Silence","Spiritual Weapon","Warding Bond","Zone of Truth"],
                "3rd" : ["Animate Dead","Beacon of Hope","Bestow Curse","Clairvoyance","Create Food and Water","Daylight","Dispel Magic","Fast Friends","Feign Death","Glyph of Warding","Incite Greed","Life Transference","Magic Circle","Mass Healing Word","Meld into Stone","Motivational Speech","Protection from Energy","Remove Curse","Revivify","Sending","Speak with Dead","Spirit Guardians","Tongues","Water Walk"],
                "4th" : ["Banishment","Control Water","Death Ward","Divination","Freedom of Movement","Guardian of Faith","Locate Creature","Stone Shape"],
                "5th" : ["Commune","Contagion","Dawn","Dispel Evil and Good","Flame Strike","Geas","Greater Restoration","Hallow","Holy Weapon","Insect Plague","Legend Lore","Mass Cure Wounds","Planar Binding","Raise Dead","Scrying"],
                "6th" : ["Blade Barrier","Create Undead","Find the Path","Forbiddance","Harm","Heal","Heroes' Feast","Planar Ally","True Seeing","Word of Recall"],
                "7th" : ["Conjure Celestial","Divine Word","Etherealness","Fire Storm","Plane Shift","Regenerate","Resurrection","Symbol","Temple of the Gods"],
                "8th" : ["Antimagic Field","Control Weather","Earthquake","Holy Aura"],
                "9th" : ["Astral Projection","Gate","Mass Heal","True Resurrection"]
            }
        }
    },



    "Druid": {
        "ASCII Art": """
  _____             _     _ 
 |  __ \           (_)   | |
 | |  | |_ __ _   _ _  __| |
 | |  | | '__| | | | |/ _` |
 | |__| | |  | |_| | | (_| |
 |_____/|_|   \__,_|_|\__,_|

        """,
        "Name": "Druid",
        "Description": "A priest of the Old Faith, wielding the powers of nature and adopting animal forms. Whether calling on the elemental forces of nature or emulating the creatures of the animal world, druids are an embodiment of nature's resilience, cunning, and fury. They claim no mastery over nature, but see themselves as extensions of nature's indomitable will.",
        "Requirements" : "You must have a Wisdom score of 13 or higher in order to multiclass in or out of this class.",
        "Level Chart" : {
            1: {'Proficiency Bonus': '+2','Features': 'Druidic, Spellcasting','Cantrips Known': 2,'1st': 2,'2nd': '-','3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            2: {'Proficiency Bonus': '+2','Features': 'Wild Shape, Druid Circle, Wild Companion (Optional)','Cantrips Known': 2,'1st': 3,'2nd': '-','3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            3: {'Proficiency Bonus': '+2','Features': '-','Cantrips Known': 2,'1st': 4,'2nd': 2,'3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            4: {'Proficiency Bonus': '+2','Features': 'Wild Shape improvement, Ability Score Improvement, Cantrip Versatility (Optional)','Cantrips Known': 3,'1st': 4,'2nd': 3,'3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            5: {'Proficiency Bonus': '+3','Features': '-','Cantrips Known': 3,'1st': 4,'2nd': 3,'3rd': 2,'4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            6: {'Proficiency Bonus': '+3','Features': 'Druid Circle feature','Cantrips Known': 3,'1st': 4,'2nd': 3,'3rd': 3,'4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            7: {'Proficiency Bonus': '+3','Features': '-','Cantrips Known': 3,'1st': 4,'2nd': 3,'3rd': 3,'4th': 1,'5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            8: {'Proficiency Bonus': '+3','Features': 'Wild Shape improvement, Ability Score Improvement, Cantrip Versatility (Optional)','Cantrips Known': 3,'1st': 4,'2nd': 3,'3rd': 3,'4th': 2,'5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            9: {'Proficiency Bonus': '+4','Features': '-','Cantrips Known': 3,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 1,'6th': '-','7th': '-','8th': '-','9th': '-'},
            10: {'Proficiency Bonus': '+4','Features': 'Druid Circle feature','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': '-','7th': '-','8th': '-','9th': '-'},
            11: {'Proficiency Bonus': '+4','Features': '-','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': '-','8th': '-','9th': '-'},
            12: {'Proficiency Bonus': '+4','Features': 'Ability Score Improvement, Cantrip Versatility (Optional)','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': '-','8th': '-','9th': '-'},
            13: {'Proficiency Bonus': '+5','Features': '-','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': '-','9th': '-'},
            14: {'Proficiency Bonus': '+5','Features': 'Druid Circle feature','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': '-','9th': '-'},
            15: {'Proficiency Bonus': '+5','Features': '-','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': '-'},
            16: {'Proficiency Bonus': '+5','Features': 'Ability Score Improvement, Cantrip Versatility (Optional)','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': '-'},
            17: {'Proficiency Bonus': '+6','Features': '-','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': 1},
            18: {'Proficiency Bonus': '+6','Features': 'Timeless Body, Beast Spells','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 1,'7th': 1,'8th': 1,'9th': 1},
            19: {'Proficiency Bonus': '+6','Features': 'Ability Score Improvement, Cantrip Versatility (Optional)','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 2,'7th': 1,'8th': 1,'9th': 1},
            20: {'Proficiency Bonus': '+6','Features': 'Archdruid','Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 2,'7th': 2,'8th': 1,'9th': 1}
        },
        "Features": {},
        "Hit Die": "1d8",
        "Proficiencies": {
            "Armor": "Light armor, medium armor, shields (druids will not wear armor or use shields made of metal)",
            "Weapons": "Clubs, daggers, darts, javelins, maces, quarterstaffs, scimitars, sickles, slings, spears",
            "Tools": "Herbalism kit",
            "Spellcasting Modifier" : "Wisdom",
            "Saving Throws": ["Intelligence", "Wisdom"],
            'Skills': {
                'Choose Number' : 2,
                'Choose From' :  ['arcana', 'animal handling', 'insight', 'medicine', 'nature', 'perception', 'religion', 'survival']
            },
            "Languages": {
                "Druidic": "You know Druidic, the secret language of druids."
            }
        },
        "Equipment": {
            'Choices' : {
                'Choice 1' : {
                    'wooden shield' : 1,
                    'any simple weapon' : 1,
                    },
                'Choice 2' : {
                    "scimitar": 1,
                    "any simple melee weapon" : 1,
                },
            },
            "Start With" : {
                "leather armor" : 1,
                "explorer's pack" : 1,
                "druidic focus" : 1
            }
        },
        "Attribute Priority" : ['wisdom', 'constitution', 'dexterity', 'intelligence', 'charisma', 'strength'],
        "Spells" : {
            "Spellcasting": "Druids harness the power of nature and the primal forces. They are spellcasters who draw their magic from the natural world, tapping into the elements, plants, and animals to cast spells.",
            "Spellcasting Modifier": "Wisdom",
            "Spell Attack Modifier": "Proficiency bonus + Wisdom modifier",
            "Spell DC Save": "8 + Proficiency bonus + Wisdom modifier",
            "Preparation": "Druids do not prepare spells in the traditional sense. They have a list of spells known and can cast any spell from that list as long as they have spell slots available.",
            "Recovery": "Druids recover their spell slots after a long rest. They do not have the option for short rest recovery like some other classes.",
            "Spell Slots": "Druids have a limited number of spell slots per day, which are divided into spell levels. They can use these slots to cast their spells.",
            "Spells Known": "Druids start with a certain number of spells known based on their level, and they learn new spells as they level up.",
            "Change Up": "Druids can change their known spells whenever they level up. They have the flexibility to adapt to different situations by selecting new spells.",
            "Progression": "Druids choose a Circle, such as the Circle of the Land or the Circle of the Moon, which provides additional spells and unique abilities related to their chosen circle.",
            "Requirements": "Druids often use druidic focuses like mistletoe, totems, or staves as spellcasting focuses, but they can cast spells without material components.",
            "Key Difference": "Druids have the unique ability to Wild Shape, allowing them to transform into animals and gain their abilities.",
            "Uniqueness": "Druids have an affinity for the natural world, and some of their spells interact with the environment and wildlife in unique ways.",
            "Magic Lore": "Druids have a deep understanding of the natural world, ecology, and the balance of life. Their magic is rooted in their connection to nature.",
            "All Class Spells" : {
                "Cantrips" : ["Control Flames","Create Bonfire","Druidcraft","Frostbite","Guidance","Gust","Infestation","Magic Stone","Mending","Mold Earth","Poison Spray","Primal Savagery","Produce Flame","Resistance","Shape Water","Shillelagh","Thorn Whip","Thunderclap"],
                "1st" : ["Absorb Elements","Animal Friendship","Beast Bond","Charm Person","Create or Destroy Water","Cure Wounds","Detect Magic","Detect Poison and Disease","Earth Tremor","Entangle","Faerie Fire","Fog Cloud","Goodberry","Healing Word","Ice Knife","Jump","Longstrider","Purify Food and Drink","Snare","Speak with Animals","Thunderwave"],
                "2nd" : ["Air Bubble","Animal Messenger","Barkskin","Beast Sense","Darkvision","Dust Devil","Earthbind","Enhance Ability","Find Traps","Flame Blade","Flaming Sphere","Gust of Wind","Healing Spirit","Heat Metal","Hold Person","Lesser Restoration","Locate Animals or Plants","Locate Object","Moonbeam","Pass Without Trace","Protection from Poison","Skywrite","Spike Growth","Warding Wind","Wither and Bloom"],
                "3rd" : ["Call Lightning","Conjure Animals","Daylight","Dispel Magic","Erupting Earth","Feign Death","Flame Arrows","Meld into Stone","Plant Growth","Protection from Energy","Sleet Storm","Speak with Plants","Tidal Wave","Wall of Water","Water Breathing","Water Walk","Wind Wall"],
                "4th" : ["Blight","Charm Monster","Confusion","Conjure Minor Elementals","Conjure Woodland Beings","Control Water","Dominate Beast","Elemental Bane","Freedom of Movement","Giant Insect","Grasping Vine","Guardian of nature","Hallucinatory Terrain","Ice Storm","Locate Creature","Polymorph","Stone Shape","Stoneskin","Wall of Fire","Watery Sphere"],
                "5th" : ["Antilife Shell","Awaken","Commune with nature","Conjure Elemental","Contagion","Control Winds","Geas","Greater Restoration","Insect Plague","Maelstrom","Mass Cure Wounds","Planar Binding","Reincarnate","Scrying","Summon Draconic Spirit","Transmute Rock","Tree Stride","Wall of Stone","Wrath Of nature"],
                "6th" : ["Bones of the Earth","Conjure Fey","Druid Grove","Find the Path","Heal","Heroes' Feast","Investiture of Flame","Investiture of Ice","Investiture of Stone","Investiture of Wind","Move Earth","Primordial Ward","Sunbeam","Transport via Plants","Wall of Thorns","Wind Walk"],
                "7th" : ["Draconic Transformation","Fire Storm","Mirage Arcane","Plane Shift","Regenerate","Reverse Gravity","Whirlwind"],
                "8th" : ["Animal Shapes","Antipathy/Sympathy","Control Weather","Earthquake","Feeblemind","Sunburst","Tsunami"],
                "9th" : ["Foresight","Shapechange","Storm of Vengeance","True Resurrection"]
            }
        }
    },



    "Fighter": {
        "ASCII Art": """
  ______ _       _     _            
 |  ____(_)     | |   | |           
 | |__   _  __ _| |__ | |_ ___ _ __ 
 |  __| | |/ _` | '_ \| __/ _ \ '__|
 | |    | | (_| | | | | ||  __/ |   
 |_|    |_|\__, |_| |_|\__\___|_|   
            __/ |                   
           |___/                    
        """,
        "Name": "Fighter",
        "Description": "A master of martial combat, skilled with a variety of weapons and armor. Fighters share an unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat. They are well acquainted with death, both meting it out and staring it defiantly in the face.",
        "Requirements" : "You must have a Dexterity or Strength score of 13 or higher in order to multiclass in or out of this class.",
        "Level Chart" : {
            1: {"Proficiency Bonus": "+2","Features": "Fighting Style, Second Wind"},
            2: {"Proficiency Bonus": "+2","Features": "Action Surge (x1)"},
            3: {"Proficiency Bonus": "+2","Features": "Martial Archetype"},
            4: {"Proficiency Bonus": "+2","Features": "Ability Score Improvement, Martial Versatility (Optional)"},
            5: {"Proficiency Bonus": "+3","Features": "Extra Attack (x1)"},
            6: {"Proficiency Bonus": "+3","Features": "Ability Score Improvement, Martial Versatility (Optional)"},
            7: {"Proficiency Bonus": "+3","Features": "Martial Archetype feature"},
            8: {"Proficiency Bonus": "+3","Features": "Ability Score Improvement, Martial Versatility (Optional)"},
            9: {"Proficiency Bonus": "+4","Features": "Indomitable (x1)"},
            10: {"Proficiency Bonus": "+4","Features": "Martial Archetype feature"},
            11: {"Proficiency Bonus": "+4","Features": "Extra Attack (x2)"},
            12: {"Proficiency Bonus": "+4","Features": "Ability Score Improvement, Martial Versatility (Optional)"},
            13: {"Proficiency Bonus": "+5","Features": "Indomitable (x2)"},
            14: {"Proficiency Bonus": "+5","Features": "Ability Score Improvement, Martial Versatility (Optional)"},
            15: {"Proficiency Bonus": "+5","Features": "Martial Archetype feature"},
            16: {"Proficiency Bonus": "+5","Features": "Ability Score Improvement, Martial Versatility (Optional)"},
            17: {"Proficiency Bonus": "+6","Features": "Action Surge (x2), Indomitable (x3)"},
            18: {"Proficiency Bonus": "+6","Features": "Martial Archetype feature"},
            19: {"Proficiency Bonus": "+6","Features": "Ability Score Improvement, Martial Versatility (Optional)"},
            20: {"Proficiency Bonus": "+6","Features": "Extra Attack (x3)"}
        },
        "Features": {},
        "Hit Die": "1d10",
        "Proficiencies": {
            "Armor": "All armor, shields",
            "Weapons": "Simple weapons, martial weapons",
            "Tools": "None",
            "Spellcasting Modifier" : "None",
            "Saving Throws": "Strength, Constitution",
            "Skills": "Choose two skills from acrobatics, animal handling, athletics, history, insight, intimidation, perception, and survival",
            "Languages": []
        },
        "Equipment": {
            'Choices' : {
                'Choice 1' : {
                    'chain mail' : 1,
                    'leather and longbow and 20 arrows' : 1,
                    },
                'Choice 2' : {
                    "any martial weapon and shield": 1,
                    "any martial weapon" : 2
                },
                'Choice 3' : {
                    'light crossbow and 20 bolts': 1,
                    'handaxe' : 2
                },
                'Choice 4' : {
                    "dungeoneer's pack" : 1,
                    "explorer's pack" : 1
                },
            },
            "Start With" : "None"
        },
        "Attribute Priority" : ['strength', 'constitution', 'dexterity', 'intelligence', 'wisdom', 'charisma'],
        "Spells" : {
            "Spellcasting": "None",
            "Spellcasting Modifier": "None",
            "Spell Attack Modifier": "None",
            "Spell DC Save": "None",
            "Preparation": "None",
            "Recovery": "None",
            "Spell Slots": "None",
            "Spells Known": "None",
            "Change Up": "None",
            "Progression": "None",
            "Requirements": "None",
            "Key Difference": "None",
            "Uniqueness": "None",
            "Magic Lore": "None",
            "All Class Spells" : "None"
        }
    },



    "Monk": {
        "ASCII Art": """
  __  __             _    
 |  \/  |           | |   
 | \  / | ___  _ __ | | __
 | |\/| |/ _ \| '_ \| |/ /
 | |  | | (_) | | | |   < 
 |_|  |_|\___/|_| |_|_|\_\
                          
        """,
        "Name": "Monk",
        "Description": "A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection. Monks are united in their ability to magically harness the energy that flows in their bodies. Whether channeled as a striking display of combat prowess or a subtler focus of defensive ability and speed, this energy infuses all that a monk does.",
        "Requirements" : "You must have a Dexterity score and a Wisdom score of 13 or higher in order to multiclass in or out of this class.",
        "Level Chart" : {
            1: {'Proficiency Bonus': '+2','Martial Arts': '1d4','Ki Points': '–','Unarmored Movement': '–','Features': 'Unarmored Defense, Martial Arts'},
            2: {'Proficiency Bonus': '+2','Martial Arts': '1d4','Ki Points': '2','Unarmored Movement': '+10 ft.','Features': 'Ki, Unarmored Movement, Dedicated Weapon (Optional)'},
            3: {'Proficiency Bonus': '+2','Martial Arts': '1d4','Ki Points': '3','Unarmored Movement': '+10 ft.','Features': 'Monastic Tradition, Deflect Missiles, Ki-Fueled Attack (Optional)'},
            4: {'Proficiency Bonus': '+2','Martial Arts': '1d4','Ki Points': '4','Unarmored Movement': '+10 ft.','Features': 'Ability Score Improvement, Slow Fall, Quickened Healing (Optional)'},
            5: {'Proficiency Bonus': '+3','Martial Arts': '1d6','Ki Points': '5','Unarmored Movement': '+10 ft.','Features': 'Extra Attack, Stunning Strike, Focused Aim (Optional)'},
            6: {'Proficiency Bonus': '+3','Martial Arts': '1d6','Ki Points': '6','Unarmored Movement': '+15 ft.','Features': 'Ki-Empowered Strikes, Monastic Tradition feature'},
            7: {'Proficiency Bonus': '+3','Martial Arts': '1d6','Ki Points': '7','Unarmored Movement': '+15 ft.','Features': 'Evasion, Stillness of Mind'},
            8: {'Proficiency Bonus': '+3','Martial Arts': '1d6','Ki Points': '8','Unarmored Movement': '+15 ft.','Features': 'Ability Score Improvement'},
            9: {'Proficiency Bonus': '+4','Martial Arts': '1d6','Ki Points': '9','Unarmored Movement': '+15 ft.','Features': 'Unarmored Movement improvement'},
            10: {'Proficiency Bonus': '+4','Martial Arts': '1d6','Ki Points': '10','Unarmored Movement': '+20 ft.','Features': 'Purity of Body'},
            11: {'Proficiency Bonus': '+4','Martial Arts': '1d8','Ki Points': '11','Unarmored Movement': '+20 ft.','Features': 'Monastic Tradition feature'},
            12: {'Proficiency Bonus': '+4','Martial Arts': '1d8','Ki Points': '12','Unarmored Movement': '+20 ft.','Features': 'Ability Score Improvement'},
            13: {'Proficiency Bonus': '+5','Martial Arts': '1d8','Ki Points': '13','Unarmored Movement': '+20 ft.','Features': 'Tongue of the Sun and Moon'},
            14: {'Proficiency Bonus': '+5','Martial Arts': '1d8','Ki Points': '14','Unarmored Movement': '+25 ft.','Features': 'Diamond Soul'},
            15: {'Proficiency Bonus': '+5','Martial Arts': '1d8','Ki Points': '15','Unarmored Movement': '+25 ft.','Features': 'Timeless Body'},
            16: {'Proficiency Bonus': '+5','Martial Arts': '1d8','Ki Points': '16','Unarmored Movement': '+25 ft.','Features': 'Ability Score Improvement'},
            17: {'Proficiency Bonus': '+6','Martial Arts': '1d10','Ki Points': '17','Unarmored Movement': '+25 ft.','Features': 'Monastic Tradition feature'},
            18: {'Proficiency Bonus': '+6','Martial Arts': '1d10','Ki Points': '18','Unarmored Movement': '+30 ft.','Features': 'Empty Body'},
            19: {'Proficiency Bonus': '+6','Martial Arts': '1d10','Ki Points': '19','Unarmored Movement': '+30 ft.','Features': 'Ability Score Improvement'},
            20: {'Proficiency Bonus': '+6','Martial Arts': '1d10','Ki Points': '20','Unarmored Movement': '+30 ft.','Features': 'Perfect Self'}
        },
        "Features": {},
        "Hit Die": "1d8",
        "Proficiencies": {
            "Armor": "None",
            "Weapons": "Simple weapons, shortswords",
            "Tools": "Choose one type of artisan's tools or one musical instrument",
            "Spellcasting Modifier" : "None",
            "Saving Throws": "Strength, Dexterity",
            "Skills": "Choose two from Acrobatics, Athletics, History, Insight, Religion, and Stealth",
            "Languages": []
        },
        "Equipment": {
            'Choices' : {
                'Choice 1' : {
                    'shortsword' : 1,
                    'any simple weapon' : 1,
                    },
                'Choice 2' : {
                    "dungeoneer's pack": 1,
                    "explorer's pack" : 1,
                },
            },
            "Start With" : {
                "dart" : 10,
            }   
        },
        "Attribute Priority" : ['dexterity', 'wisdom', 'constitution', 'strength', 'charisma', 'intelligence'],
        "Spells" : {
            "Spellcasting": "None",
            "Spellcasting Modifier": "None",
            "Spell Attack Modifier": "None",
            "Spell DC Save": "None",
            "Preparation": "None",
            "Recovery": "None",
            "Spell Slots": "None",
            "Spells Known": "None",
            "Change Up": "None",
            "Progression": "None",
            "Requirements": "None",
            "Key Difference": "None",
            "Uniqueness": "None",
            "Magic Lore": "None",
            "All Class Spells" : "None"
        }
    },



    "Paladin": {
        "ASCII Art": """
  _____      _           _ _       
 |  __ \    | |         | (_)      
 | |__) |_ _| | __ _  __| |_ _ __  
 |  ___/ _` | |/ _` |/ _` | | '_ \ 
 | |  | (_| | | (_| | (_| | | | | |
 |_|   \__,_|_|\__,_|\__,_|_|_| |_|
                                   
        """,
        "Name": "Paladin",
        "Description": "A holy warrior bound to a sacred oath. Whether sworn before a god's altar and the witness of a priest, in a sacred glade before nature spirits and fey beings, or in a moment of desperation and grief with the dead as the only witness, a paladin's oath is a powerful bond.",
        "Requirements" : "You must have a Charisma score and a Strength score of 13 or higher in order to multiclass in or out of this class.",
        "Level Chart" : {
            1: {'Proficiency Bonus': '+2', 'Features': 'Divine Sense, Lay on Hands', '1st': '-', '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            2: {'Proficiency Bonus': '+2', 'Features': 'Fighting Style, Spellcasting, Divine Smite', '1st': '2', '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            3: {'Proficiency Bonus': '+2', 'Features': 'Divine Health, Sacred Oath, Harness Divine Power (Optional)', '1st': '3', '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            4: {'Proficiency Bonus': '+2', 'Features': 'Ability Score Improvement, Martial Versatility (Optional)', '1st': '3', '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            5: {'Proficiency Bonus': '+3', 'Features': 'Extra Attack', '1st': '4', '2nd': '2', '3rd': '-', '4th': '-', '5th': '-'},
            6: {'Proficiency Bonus': '+3', 'Features': 'Aura of Protection', '1st': '4', '2nd': '2', '3rd': '-', '4th': '-', '5th': '-'},
            7: {'Proficiency Bonus': '+3', 'Features': 'Sacred Oath feature', '1st': '4', '2nd': '3', '3rd': '-', '4th': '-', '5th': '-'},
            8: {'Proficiency Bonus': '+3', 'Features': 'Ability Score Improvement, Martial Versatility (Optional)', '1st': '4', '2nd': '3', '3rd': '-', '4th': '-', '5th': '-'},
            9: {'Proficiency Bonus': '+4', 'Features': '', '1st': '4', '2nd': '3', '3rd': '2', '4th': '-', '5th': '-'},
            10: {'Proficiency Bonus': '+4', 'Features': 'Aura of Courage', '1st': '4', '2nd': '3', '3rd': '2', '4th': '-', '5th': '-'},
            11: {'Proficiency Bonus': '+4', 'Features': 'Improved Divine Smite', '1st': '4', '2nd': '3', '3rd': '3', '4th': '-', '5th': '-'},
            12: {'Proficiency Bonus': '+4', 'Features': 'Ability Score Improvement, Martial Versatility (Optional)', '1st': '4', '2nd': '3', '3rd': '3', '4th': '-', '5th': '-'},
            13: {'Proficiency Bonus': '+5', 'Features': '', '1st': '4', '2nd': '3', '3rd': '3', '4th': '1', '5th': '-'},
            14: {'Proficiency Bonus': '+5', 'Features': 'Cleansing Touch', '1st': '4', '2nd': '3', '3rd': '3', '4th': '1', '5th': '-'},
            15: {'Proficiency Bonus': '+5', 'Features': 'Sacred Oath feature', '1st': '4', '2nd': '3', '3rd': '3', '4th': '2', '5th': '-'},
            16: {'Proficiency Bonus': '+5', 'Features': 'Ability Score Improvement, Martial Versatility (Optional)', '1st': '4', '2nd': '3', '3rd': '3', '4th': '2', '5th': '-'},
            17: {'Proficiency Bonus': '+6', 'Features': '', '1st': '4', '2nd': '3', '3rd': '3', '4th': '3', '5th': '1'},
            18: {'Proficiency Bonus': '+6', 'Features': 'Aura improvements', '1st': '4', '2nd': '3', '3rd': '3', '4th': '3', '5th': '1'},
            19: {'Proficiency Bonus': '+6', 'Features': 'Ability Score Improvement, Martial Versatility (Optional)', '1st': '4', '2nd': '3', '3rd': '3', '4th': '3', '5th': '2'},
            20: {'Proficiency Bonus': '+6', 'Features': 'Sacred Oath feature', '1st': '4', '2nd': '3', '3rd': '3', '4th': '3', '5th': '2'}
        },
        "Features" : {},
        "Hit Die": "1d10",
        "Proficiencies": {
            "Armor": "All armor, shields",
            "Weapons": ["simple weapons", "martial weapons"],
            "Tools": "None",
            "Spellcasting Modifier" : "Charisma",
            "Saving Throws": ["Wisdom, Charisma"],
            'Skills': {
                'Choose Number' : 2,
                'Choose From' :  ['athletics', 'insight', 'intimidation', 'medicine', 'persuasion', 'religion']
            },
            "Languages": []
        },
        "Equipment": {
            'Choices' : {
                'Choice 1' : {
                    'any martial weapon and shield' : 1,
                    'any martial weapon' : 2,
                    },
                'Choice 2' : {
                    "javelins": 5,
                    "any simple melee weaon" : 1,
                },
                'Choice 3' : {
                    "priest's pack" : 1,
                    "explorer's pack" : 1
                },
            },
            "Start With" : {
                "chain mail" : 1,
                "holy symbol" : 1
            }  
        },
        "Attribute Priority": ['strength', 'charisma', 'constitution', 'dexterity', 'wisdom', 'intelligence'],
        "Spells" : {
            "Spellcasting": "Paladins are holy warriors who receive divine magic from their oath and unwavering devotion to a cause or deity. They use their faith and righteousness to cast spells.",
            "Spellcasting Modifier": "Charisma",
            "Spell Attack Modifier": "Proficiency bonus + Charisma modifier",
            "Spell DC Save": "8 + Proficiency bonus + Charisma modifier",
            "Preparation": "Paladins do not prepare spells in the traditional sense. They have a list of spells known and can cast any spell from that list as long as they have spell slots available.",
            "Recovery": "Paladins recover their spell slots after a long rest. They do not have the option for short rest recovery like some other classes.",
            "Spell Slots": "Paladins have a limited number of spell slots per day, which are divided into spell levels. They can use these slots to cast their spells.",
            "Spells Known": "Paladins start with a certain number of spells known based on their level, and they learn new spells as they level up.",
            "Change Up": "Paladins can change their known spells whenever they level up. They have the flexibility to adapt to different situations by selecting new spells.",
            "Progression": "Paladins take Oaths, such as the Oath of Devotion or the Oath of Vengeance, which grant them additional spells and abilities based on their chosen oath.",
            "Requirements": "Paladins often use holy symbols or their weapon as a focus for their spells, but they can cast spells without material components.",
            "Key Difference": "Paladins have the unique ability to use their spell slots to fuel Divine Smite, allowing them to deal extra damage with melee weapon attacks.",
            "Uniqueness": "Paladins are known for their righteousness and adherence to a strict code of conduct, and their spells often reflect their commitment to their chosen path.",
            "Magic Lore": "Paladins have a deep understanding of divine magic and their faith, and their spellcasting is an expression of their unwavering devotion.",
            "All Class Spells" : {
                "1st" : ["Bless","Ceremony","Command","Compelled Duel","Cure Wounds","Detect Evil and Good","Detect Magic","Detect Poison and Disease","Divine Favor","Heroism","Protection from Evil and Good","Purify Food and Drink","Searing Smite","Shield of Faith","Thunderous Smite","Wrathful Smite"],
                "2nd" : ["Aid","Branding Smite","Find Steed","Lesser Restoration","Locate Object","Magic Weapon","Protection from Poison","Zone of Truth"],
                "3rd" : ["Aura of Vitality","Blinding Smite","Create Food and Water","Crusader's Mantle","Daylight","Dispel Magic","Elemental Weapon","Magic Circle","Remove Curse","Spirit Shroud"],
                "4th" : ["Aura of Life","Aura of Purity","Banishment","Death Ward","Find Greater Steed","Locate Creature","Staggering Smite"],
                "5th" : ["Banishing Smite","Circle of Power","Destructive Wave","Dispel Evil and Good","Geas","Holy Weapon","Raise Dead"]
            }
        }
    },



    "Ranger": {
        "ASCII Art": """
  _____                             
 |  __ \                            
 | |__) |__ _ _ __   __ _  ___ _ __ 
 |  _  // _` | '_ \ / _` |/ _ \ '__|
 | | \ \ (_| | | | | (_| |  __/ |   
 |_|  \_\__,_|_| |_|\__, |\___|_|   
                     __/ |          
                    |___/           
        """,
        "Name": "Ranger",
        "Description": "A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization. Far from the bustle of cities and towns, past the hedges that shelter the most distant farms from the terrors of the wild, amid the dense-packed trees of trackless forests and across wide and empty plains, rangers keep their unending watch.",
        "Requirements" : "You must have a Dexterity score and a Wisdom score of 13 or higher in order to multiclass in or out of this class.",
        "Level Chart" : {
            1: {'Proficiency Bonus': '+2', 'Features': 'Favored Enemy, Natural Explorer, Deft Explorer (Optional), Favored Foe (Optional)', 'Spells Known': '-', '1st': '-', '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            2: {'Proficiency Bonus': '+2', 'Features': 'Fighting Style, Spellcasting, Spellcasting Focus (Optional)', 'Spells Known': 2, '1st': 2, '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            3: {'Proficiency Bonus': '+2', 'Features': 'Primeval Awareness, Ranger Conclave, Primal Awareness (Optional)', 'Spells Known': 3, '1st': 3, '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            4: {'Proficiency Bonus': '+2', 'Features': 'Ability Score Improvement, Martial Versatility (Optional)', 'Spells Known': 3, '1st': 3, '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            5: {'Proficiency Bonus': '+3', 'Features': 'Extra Attack', 'Spells Known': 4, '1st': 4, '2nd': 2, '3rd': '-', '4th': '-', '5th': '-'},
            6: {'Proficiency Bonus': '+3', 'Features': 'Favored Enemy Improvement, Natural Explorer Improvement, Deft Explorer Improvement (Optional)', 'Spells Known': 4, '1st': 4, '2nd': 2, '3rd': '-', '4th': '-', '5th': '-'},
            7: {'Proficiency Bonus': '+3', 'Features': 'Ranger Conclave feature', 'Spells Known': 5, '1st': 4, '2nd': 3, '3rd': '-', '4th': '-', '5th': '-'},
            8: {'Proficiency Bonus': '+3', 'Features': "Ability Score Improvement, Land's Stride, Martial Versatility (Optional)", 'Spells Known': 5, '1st': 4, '2nd': 3, '3rd': '-', '4th': '-', '5th': '-'},
            9: {'Proficiency Bonus': '+4', 'Features': '-', 'Spells Known': 6, '1st': 4, '2nd': 3, '3rd': 2, '4th': '-', '5th': '-'},
            10: {'Proficiency Bonus': '+4', 'Features': "Natural Explorer Improvement, Hide in Plain Sight, Deft Explorer Feature (Optional), Nature's Veil (Optional)", 'Spells Known': 6, '1st': 4, '2nd': 3, '3rd': 2, '4th': '-', '5th': '-'},
            11: {'Proficiency Bonus': '+4', 'Features': 'Ranger Conclave feature', 'Spells Known': 7, '1st': 4, '2nd': 3, '3rd': 3, '4th': '-', '5th': '-'},
            12: {'Proficiency Bonus': '+4', 'Features': 'Ability Score Improvement, Martial Versatility (Optional)', 'Spells Known': 7, '1st': 4, '2nd': 3, '3rd': 3, '4th': '-', '5th': '-'},
            13: {'Proficiency Bonus': '+5', 'Features': '-', 'Spells Known': 8, '1st': 4, '2nd': 3, '3rd': 3, '4th': 1, '5th': '-'},
            14: {'Proficiency Bonus': '+5', 'Features': 'Favored Enemy Improvement, Vanish', 'Spells Known': 8, '1st': 4, '2nd': 3, '3rd': 3, '4th': 1, '5th': '-'},
            15: {'Proficiency Bonus': '+5', 'Features': 'Ranger Conclave feature', 'Spells Known': 9, '1st': 4, '2nd': 3, '3rd': 3, '4th': 2, '5th': '-'},
            16: {'Proficiency Bonus': '+5', 'Features': 'Ability Score Improvement, Martial Versatility (Optional)', 'Spells Known': 9, '1st': 4, '2nd': 3, '3rd': 3, '4th': 2, '5th': '-'},
            17: {'Proficiency Bonus': '+6', 'Features': '-', 'Spells Known': 10, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 1},
            18: {'Proficiency Bonus': '+6', 'Features': 'Feral Senses', 'Spells Known': 10, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 1},
            19: {'Proficiency Bonus': '+6', 'Features': 'Ability Score Improvement, Martial Versatility (Optional)', 'Spells Known': 11, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2},
            20: {'Proficiency Bonus': '+6', 'Features': 'Foe Slayer', 'Spells Known': 11, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2}
        },
        "Features": {},
        "Hit Die": '1d10',
        "Proficiencies": {
            'Armor': 'Light armor, medium armor, shields',
            'Weapons': 'Simple weapons, martial weapons',
            'Tools': 'None',
            "Spellcasting Modifier" : "Widsom",
            'Saving Throws': ['Strength', 'Dexterity'],
            'Skills': {
                'Choose Number' : 3,
                'Choose From' :  ['Animal Handling', 'Athletics', 'Insight', 'Investigation', 'Nature', 'Perception', 'Stealth', 'Survival']
            },
            "Languages": []
        },
        "Equipment": {
            'Choices' : {
                'Choice 1' : {
                    'scale mail' : 1,
                    'any simple melee weapon' : 2,
                    },
                'Choice 2' : {
                    "shortsword" : 2,
                    "any simple melee weapon" : 2,
                },
                'Choice 3' : {
                    "dungeoneer's pack" : 1,
                    "explorer's pack" : 1
                },
            },
            "Start With" : {
                "longbow" : 1,
                "arrow" : 20
            }              
        },
        "Attribute Priority" : ['dexterity', 'wisdom', 'constitution', 'strength', 'intelligence', 'charisma'],
        "Spells" : {
            "Spellcasting": "Rangers are skilled hunters and trackers who have a deep connection with nature. They cast spells that enhance their combat abilities and allow them to interact with the natural world.",
            "Spellcasting Modifier": "Wisdom",
            "Spell Attack Modifier": "Proficiency bonus + Wisdom modifier",
            "Spell DC Save": "8 + Proficiency bonus + Wisdom modifier",
            "Preparation": "Rangers do not prepare spells in the traditional sense. They have a list of spells known and can cast any spell from that list as long as they have spell slots available.",
            "Recovery": "Rangers recover their spell slots after a long rest. They do not have the option for short rest recovery like some other classes.",
            "Spell Slots": "Rangers have a limited number of spell slots per day, which are divided into spell levels. They can use these slots to cast their spells.",
            "Spells Known": "Rangers start with a certain number of spells known based on their level, and they learn new spells as they level up.",
            "Change Up": "Rangers can change their known spells whenever they level up. They have the flexibility to adapt to different situations by selecting new spells.",
            "Progression": "Rangers choose a Ranger Archetype, such as the Hunter or the Beast Master, which provides additional spells and unique abilities related to their chosen archetype.",
            "Requirements": "Rangers often use components like a sprig of mistletoe or holly as a focus for their spells, but they can cast spells without material components.",
            "Key Difference": "Rangers have a unique ability called Primeval Awareness, which allows them to detect creatures of a specific type within a certain radius.",
            "Uniqueness": "Rangers are known for their survival skills and their ability to blend into the wilderness. Some of their spells reflect their deep connection with nature.",
            "Magic Lore": "Rangers have a deep understanding of the natural world and its creatures. Their spellcasting is rooted in their knowledge of the wilderness.",
            "All Class Spells" : {
                "1st" : ["Absorb Elements","Alarm","Animal Friendship","Beast Bond","Cure Wounds","Detect Magic","Detect Poison and Disease","Ensnaring Strike","Fog Cloud","Goodberry","Hail of Thorns","Hunter's Mark","Jump","Longstrider","Snare","Speak with Animals","Zephyr Strike"],
                "2nd" : ["Air Bubble","Animal Messenger","Barkskin","Beast Sense","Cordon of Arrows","Darkvision","Find Traps","Healing Spirit","Lesser Restoration","Locate Animals or Plants","Locate Object","Pass Without Trace","Protection from Poison","Silence","Spike Growth"],
                "3rd" : ["Ashardalon's Stride","Conjure Animals","Conjure Barrage","Daylight","Flame Arrows","Lightning Arrow","Nondetection","Plant Growth","Protection from Energy","Speak with Plants","Water Breathing","Water Walk","Wind Wall"],
                "4th" : ["Conjure Woodland Beings","Freedom of Movement","Grasping Vine","Guardian of nature","Locate Creature","Stoneskin"],
                "5th" : ["Commune with nature","Conjure Volley","Steel Wind Strike","Swift Quiver","Tree Stride","Wrath Of nature"]           
            }
        }
    },



    "Rogue": {
        "ASCII Art": """
  _____                        
 |  __ \                       
 | |__) |___   __ _ _   _  ___ 
 |  _  // _ \ / _` | | | |/ _ \
 | | \ \ (_) | (_| | |_| |  __/
 |_|  \_\___/ \__, |\__,_|\___|
               __/ |           
              |___/            
        """,
        "Name": "Rogue",
        "Description": "A scoundrel who uses stealth and trickery to overcome obstacles and enemies. Rogues rely on skill, stealth, and their foes' vulnerabilities to get the upper hand in any situation. They have a knack for finding the solution to just about any problem, demonstrating a resourcefulness and versatility that is the cornerstone of any successful adventuring party.",
        "Requirements" : "You must have a Dexterity score of 13 or higher in order to multiclass in or out of this class.",
        "Level Chart" : {
            1: {'Proficiency Bonus': '+2', 'Sneak Attack': '1d6', 'Features': 'Expertise, Sneak Attack, Thieves\' Cant'},
            2: {'Proficiency Bonus': '+2', 'Sneak Attack': '1d6', 'Features': 'Cunning Action'},
            3: {'Proficiency Bonus': '+2', 'Sneak Attack': '2d6', 'Features': 'Roguish Archetype, Steady Aim (Optional)'},
            4: {'Proficiency Bonus': '+2', 'Sneak Attack': '2d6', 'Features': 'Ability Score Improvement'},
            5: {'Proficiency Bonus': '+3', 'Sneak Attack': '3d6', 'Features': 'Uncanny Dodge'},
            6: {'Proficiency Bonus': '+3', 'Sneak Attack': '3d6', 'Features': 'Expertise'},
            7: {'Proficiency Bonus': '+3', 'Sneak Attack': '4d6', 'Features': 'Evasion'},
            8: {'Proficiency Bonus': '+3', 'Sneak Attack': '4d6', 'Features': 'Ability Score Improvement'},
            9: {'Proficiency Bonus': '+4', 'Sneak Attack': '5d6', 'Features': 'Roguish Archetype feature'},
            10: {'Proficiency Bonus': '+4', 'Sneak Attack': '5d6', 'Features': 'Ability Score Improvement'},
            11: {'Proficiency Bonus': '+4', 'Sneak Attack': '6d6', 'Features': 'Reliable Talent'},
            12: {'Proficiency Bonus': '+4', 'Sneak Attack': '6d6', 'Features': 'Ability Score Improvement'},
            13: {'Proficiency Bonus': '+5', 'Sneak Attack': '7d6', 'Features': 'Roguish Archetype feature'},
            14: {'Proficiency Bonus': '+5', 'Sneak Attack': '7d6', 'Features': 'Blindsense'},
            15: {'Proficiency Bonus': '+5', 'Sneak Attack': '8d6', 'Features': 'Slippery Mind'},
            16: {'Proficiency Bonus': '+5', 'Sneak Attack': '8d6', 'Features': 'Ability Score Improvement'},
            17: {'Proficiency Bonus': '+6', 'Sneak Attack': '9d6', 'Features': 'Roguish Archetype feature'},
            18: {'Proficiency Bonus': '+6', 'Sneak Attack': '9d6', 'Features': 'Elusive'},
            19: {'Proficiency Bonus': '+6', 'Sneak Attack': '10d6', 'Features': 'Ability Score Improvement'},
            20: {'Proficiency Bonus': '+6', 'Sneak Attack': '10d6', 'Features': 'Stroke of Luck'}
        },
        "Features": {},
        "Hit Die": '1d8',
        "Proficiencies": {
            'Armor': 'Light armor',
            'Weapons': 'Simple weapons, hand crossbows, longswords, rapiers, shortswords',
            'Tools': 'Thieves\' tools',
            "Spellcasting Modifier" : "None",
            'Saving Throws': ['Dexterity', 'Intelligence'],
            'Skills': {
                'Choose Number' : 4,
                'Choose From' :  ['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth']
            },
            "Languages": []
        },
        "Equipment": {
            'Choices' : {
                'Choice 1' : {
                    'rapier' : 1,
                    'shortsword' : 1,
                    },
                'Choice 2' : {
                    "shortbow and 20 arrows": 1,
                    "shortsword" : 1,
                },
                'Choice 3' : {
                    "burglar's pack": 1,
                    "dungeoneer's pack" : 1,
                    "explorer's pack": 1
                },
            },
            "Start With" : {
                "leather armor" : 1,
                "dagger" : 2,
                "theives' tools" : 1,
            }  
        },
        "Attribute Priority" : ['dexterity', 'intelligence', 'constitution', 'charisma', 'wisdom', 'strength'],
        "Spells" : {
            "Spellcasting": "None",
            "Spellcasting Modifier": "None",
            "Spell Attack Modifier": "None",
            "Spell DC Save": "None",
            "Preparation": "None",
            "Recovery": "None",
            "Spell Slots": "None",
            "Spells Known": "None",
            "Change Up": "None",
            "Progression": "None",
            "Requirements": "None",
            "Key Difference": "None",
            "Uniqueness": "None",
            "Magic Lore": "None",
            "All Class Spells" : "None"
        }
    },



    "Sorcerer": {
        "ASCII Art": """
   _____                                  
  / ____|                                 
 | (___   ___  _ __ ___ ___ _ __ ___ _ __ 
  \___ \ / _ \| '__/ __/ _ \ '__/ _ \ '__|
  ____) | (_) | | | (_|  __/ | |  __/ |   
 |_____/ \___/|_|  \___\___|_|  \___|_|   
                                          
        """,
        "Name": "Sorcerer",
        "Description": "A spellcaster who draws on inherent magic from a gift or bloodline. Sorcerers carry a magical birthright conferred upon them by an exotic bloodline, some otherworldly influence, or exposure to unknown cosmic forces. No one chooses sorcery; the power chooses the sorcerer.",
        "Requirements" : "You must have a Charisma score of 13 or higher in order to multiclass in or out of this class.",
        "Level Chart" : {
            1: {'Proficiency Bonus': '+2', 'Sorcery Points': '-', 'Features': 'Spellcasting, Sorcerous Origin', 'Cantrips Known': 4, 'Spells Known': 2, '1st': 2, '2nd': '-', '3rd': '-', '4th': '-', '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            2: {'Proficiency Bonus': '+2', 'Sorcery Points': '2', 'Features': 'Font of Magic', 'Cantrips Known': 4, 'Spells Known': 3, '1st': 3, '2nd': '-', '3rd': '-', '4th': '-', '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            3: {'Proficiency Bonus': '+2', 'Sorcery Points': '3', 'Features': 'Metamagic', 'Cantrips Known': 4, 'Spells Known': 4, '1st': 4, '2nd': 2, '3rd': '-', '4th': '-', '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            4: {'Proficiency Bonus': '+2', 'Sorcery Points': '4', 'Features': 'Ability Score Improvement, Sorcerous Versatility (Optional)', 'Cantrips Known': 5, 'Spells Known': 5, '1st': 4, '2nd': 3, '3rd': '-', '4th': '-', '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            5: {'Proficiency Bonus': '+3', 'Sorcery Points': '5', 'Features': 'Magical Guidance (Optional)', 'Cantrips Known': 5, 'Spells Known': 6, '1st': 4, '2nd': 3, '3rd': 2, '4th': '-', '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            6: {'Proficiency Bonus': '+3', 'Sorcery Points': '6', 'Features': 'Sorcerous Origin feature', 'Cantrips Known': 5, 'Spells Known': 7, '1st': 4, '2nd': 3, '3rd': 3, '4th': '-', '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            7: {'Proficiency Bonus': '+3', 'Sorcery Points': '7', 'Features': '-', 'Cantrips Known': 5, 'Spells Known': 8, '1st': 4, '2nd': 3, '3rd': 3, '4th': 1, '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            8: {'Proficiency Bonus': '+3', 'Sorcery Points': '8', 'Features': 'Ability Score Improvement, Sorcerous Versatility (Optional)', 'Cantrips Known': 5, 'Spells Known': 9, '1st': 4, '2nd': 3, '3rd': 3, '4th': 2, '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            9: {'Proficiency Bonus': '+4', 'Sorcery Points': '9', 'Features': '-', 'Cantrips Known': 5, 'Spells Known': 10, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 1, '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            10: {'Proficiency Bonus': '+4', 'Sorcery Points': '10', 'Features': 'Metamagic', 'Cantrips Known': 6, 'Spells Known': 11, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            11: {'Proficiency Bonus': '+4', 'Sorcery Points': '11', 'Features': '-', 'Cantrips Known': 6, 'Spells Known': 12, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': '-', '8th': '-', '9th': '-'},
            12: {'Proficiency Bonus': '+4', 'Sorcery Points': '12', 'Features': 'Ability Score Improvement, Sorcerous Versatility (Optional)', 'Cantrips Known': 6, 'Spells Known': 12, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': '-', '8th': '-', '9th': '-'},
            13: {'Proficiency Bonus': '+5', 'Sorcery Points': '13', 'Features': '-', 'Cantrips Known': 6, 'Spells Known': 13, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': '-', '9th': '-'},
            14: {'Proficiency Bonus': '+5', 'Sorcery Points': '14', 'Features': 'Sorcerous Origin feature', 'Cantrips Known': 6, 'Spells Known': 13, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': '-', '9th': '-'},
            15: {'Proficiency Bonus': '+5', 'Sorcery Points': '15', 'Features': '-', 'Cantrips Known': 6, 'Spells Known': 14, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': '-'},
            16: {'Proficiency Bonus': '+5', 'Sorcery Points': '16', 'Features': 'Ability Score Improvement, Sorcerous Versatility (Optional)', 'Cantrips Known': 6, 'Spells Known': 14, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': '-'},
            17: {'Proficiency Bonus': '+6', 'Sorcery Points': '17', 'Features': 'Metamagic', 'Cantrips Known': 6, 'Spells Known': 15, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': 1},
            18: {'Proficiency Bonus': '+6', 'Sorcery Points': '18', 'Features': 'Sorcerous Origin feature', 'Cantrips Known': 6, 'Spells Known': 15, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': 1},
            19: {'Proficiency Bonus': '+6', 'Sorcery Points': '19', 'Features': 'Ability Score Improvement, Sorcerous Versatility (Optional)', 'Cantrips Known': 6, 'Spells Known': 15, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': 1},
            20: {'Proficiency Bonus': '+6', 'Sorcery Points': '20', 'Features': 'Sorcerous Restoration', 'Cantrips Known': 6, 'Spells Known': 15, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': 1}
        },
        "Features": {},
        "Hit Die": '1d6',
        "Proficiencies": {
            'Armor': 'None',
            'Weapons': 'Daggers, darts, slings, quarterstaffs, light crossbows',
            'Tools': 'None',
            "Spellcasting Modifier" : "Charisma",
            'Saving Throws': ['Constitution', 'Charisma'],
            'Skills': {
                'Choose Number' : 2,
                'Choose From' :  ['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion', 'Religion']
            },
            "Languages": []
        },
        "Equipment": {
            'Choices' : {
                'Choice 1' : {
                    'light crossbow and 20 bolts' : 1,
                    'any simple weapon' : 1,
                    },
                'Choice 2' : {
                    "component pouch": 1,
                    "arcane focus" : 1,
                    "chain mail (if proficient)" : 1
                },
                'Choice 3' : {
                    "dungeoneer's pack" : 1,
                    "explorer's pack" : 1
                },
            },
            "Start With" : {
                "dagger" : 2,
            }  
        },
        "Attribute Priority" : ['charisma', 'constitution', 'dexterity', 'intelligence', 'wisdom', 'strength'],
        "Spells" : {
            "Spellcasting": "Sorcerers are innate spellcasters who derive their magical powers from their own bloodline or innate magical talent. They do not need to study or prepare spells; magic flows through them naturally.",
            "Spellcasting Modifier": "Charisma",
            "Spell Attack Modifier": "Proficiency bonus + Charisma modifier",
            "Spell DC Save": "8 + Proficiency bonus + Charisma modifier",
            "Preparation": "Sorcerers do not prepare spells in the traditional sense. They have a known list of spells and can cast any spell from that list as long as they have spell slots available.",
            "Recovery": "Sorcerers recover their expended spell slots after a long rest. They do not have the option for short rest recovery like some other classes.",
            "Spell Slots": "Sorcerers have a limited number of spell slots per day, which are divided into spell levels. They can use these slots to cast their spells.",
            "Spells Known": "Sorcerers start with a certain number of spells known based on their level, and they learn new spells as they level up.",
            "Change Up": "Sorcerers can change their known spells whenever they level up, giving them the flexibility to adapt to different situations by selecting new spells.",
            "Progression": "Sorcerers choose a Sorcerous Origin, such as Draconic Bloodline or Wild Magic, which grants them additional spells and unique abilities related to their chosen origin.",
            "Requirements": "Sorcerers do not require material components for their spells, as they cast magic innately through their bloodline or talent.",
            "Key Difference": "Sorcerers have a unique ability called Sorcery Points, which they can use to convert into spell slots or enhance their spells through Metamagic.",
            "Uniqueness": "Sorcerers are unique in their innate connection to magic and their ability to manipulate spells with Metamagic options, such as Twin Spell and Quickened Spell.",
            "Magic Lore": "Sorcerers often have a mystical understanding of their own magic and its origins, exploring the mysteries of their innate powers.",
            "All Class Spells" : {
                "Cantrips" : ["Acid Splash","Blade Ward","Chill Touch","Control Flames","Create Bonfire","Dancing Lights","Fire Bolt","Friends","Frostbite","Gust","Infestation","Light","Mage Hand","Mending","Message","Minor Illusion","Mold Earth","Poison Spray","Prestidigitation","Ray of Frost","Shape Water","Shocking Grasp","Thunderclap","True Strike"],
                "1st" : ["Absorb Elements","Burning Hands","Catapult","Chaos Bolt","Charm Person","Chromatic Orb","Color Spray","Comprehend Languages","Detect Magic","Disguise Self","Distort Value","Earth Tremor","Expeditious Retreat","False Life","Feather Fall","Fog Cloud","Ice Knife","Jump","Mage Armor","Magic Missile","Ray of Sickness","Shield","Silent Image","Silvery Barbs","Sleep","Thunderwave","Witch Bolt"],
                "2nd" : ["Aganazzar's Scorcher","Air Bubble","Alter Self","Blindness/Deafness","Blur","Cloud of Daggers","Crown of Madness","Darkness","Darkvision","Detect Thoughts","Dragon's Breath","Dust Devil","Earthbind","Enhance Ability","Enlarge/Reduce","Gust of Wind","Hold Person","Invisibility","Kinetic Jaunt","Knock","Levitate","Maximillian's Earthen Grasp","Mind Spike","Mirror Image","Misty Step","Nathair's Mischief","Phantasmal Force","Pyrotechnics","Rime's Binding Ice","Scorching Ray","See Invisibility","Shadow Blade","Shatter","Snilloc's Snowball Storm","Spider Climb","Spray Of Cards","Suggestion","Vortex Warp","Warding Wind","Warp Sense","Web","Wither and Bloom"],
                "3rd" : ["Antagonize","Ashardalon's Stride","Blink","Catnap","Clairvoyance","Counterspell","Daylight","Dispel Magic","Enemies Abound","Erupting Earth","Fear","Fireball","Flame Arrows","Fly","Gaseous Form","Haste","Hypnotic Pattern","Incite Greed","Lightning Bolt","Major Image","Melf's Minute Meteors","Protection from Energy","Sleet Storm","Slow","Stinking Cloud","Thunder Step","Tongues","Wall of Water","Water Breathing","Water Walk"],
                "4th" : ["Banishment","Blight","Charm Monster","Confusion","Dimension Door","Dominate Beast","Gate Seal","Greater Invisibility","Ice Storm","Polymorph","Raulothim's Psychic Lance","Sickening Radiance","Spirit Of Death","Stoneskin","Storm Sphere","Vitriolic Sphere","Wall of Fire","Watery Sphere"],
                "5th" : ["Animate Objects","Cloudkill","Cone of Cold","Control Winds","Creation","Dominate Person","Enervation","Far Step","Hold Monster","Immolation","Insect Plague","Seeming","Skill Empowerment","Summon Draconic Spirit","Synaptic Static","Telekinesis","Teleportation Circle","Wall of Light","Wall of Stone"],
                "6th" : ["Arcane Gate","Chain Lightning","Circle of Death","Disintegrate","Eyebite","Fizban's Platinum Shield","Globe of Invulnerability","Investiture of Flame","Investiture of Ice","Investiture of Stone","Investiture of Wind","Mass Suggestion","Mental Prison","Move Earth","Scatter","Sunbeam","True Seeing"],
                "7th" : ["Crown of Stars","Delayed Blast Fireball","Draconic Transformation","Etherealness","Finger of Death","Fire Storm","Plane Shift","Power Word: Pain","Prismatic Spray","Reverse Gravity","Teleport"],
                "8th" : ["Abi-Dalzim's Horrid Wilting","Dominate Monster","Earthquake","Incendiary Cloud","Power Word: Stun","Sunburst"],
                "9th" : ["Blade of Disaster","Gate","Mass Polymorph","Meteor Swarm","Power Word: Kill","Psychic Scream","Time Stop","Wish"]
            }
        }
    },



    "Warlock": {
        "ASCII Art": """
 __          __        _            _    
 \ \        / /       | |          | |   
  \ \  /\  / /_ _ _ __| | ___   ___| | __
   \ \/  \/ / _` | '__| |/ _ \ / __| |/ /
    \  /\  / (_| | |  | | (_) | (__|   < 
     \/  \/ \__,_|_|  |_|\___/ \___|_|\_\
                                         
        """,
        "Name": "Warlock",
        "Description": "A wielder of magic that is derived from a bargain with an extraplanar entity. Warlocks are seekers of the knowledge that lies hidden in the fabric of the multiverse. Through pacts made with mysterious beings of supernatural power, warlocks unlock magical effects both subtle and spectacular.",
        "Requirements" : "You must have a Charisma score of 13 or higher in order to multiclass in or out of this class.",
        "Level Chart" : {
            1: {'Proficiency Bonus': '+2', 'Features': 'Otherworldly Patron, Pact Magic', 'Cantrips Known': 2, 'Spells Known': 2, 'Spell Slots': 1, 'Slot Level': '1st', 'Invocations Known': '-'},
            2: {'Proficiency Bonus': '+2', 'Features': 'Eldritch Invocations', 'Cantrips Known': 2, 'Spells Known': 3, 'Spell Slots': 2, 'Slot Level': '1st', 'Invocations Known': '2'},
            3: {'Proficiency Bonus': '+2', 'Features': 'Pact Boon', 'Cantrips Known': 2, 'Spells Known': 4, 'Spell Slots': 2, 'Slot Level': '2nd', 'Invocations Known': '2'},
            4: {'Proficiency Bonus': '+2', 'Features': 'Ability Score Improvement, Eldritch Versatility (Optional)', 'Cantrips Known': 3, 'Spells Known': 5, 'Spell Slots': 2, 'Slot Level': '2nd', 'Invocations Known': '2'},
            5: {'Proficiency Bonus': '+3', 'Features': '-', 'Cantrips Known': 3, 'Spells Known': 6, 'Spell Slots': 2, 'Slot Level': '3rd', 'Invocations Known': '3'},
            6: {'Proficiency Bonus': '+3', 'Features': 'Otherworldly Patron feature', 'Cantrips Known': 3, 'Spells Known': 7, 'Spell Slots': 2, 'Slot Level': '3rd', 'Invocations Known': '3'},
            7: {'Proficiency Bonus': '+3', 'Features': '-', 'Cantrips Known': 3, 'Spells Known': 8, 'Spell Slots': 2, 'Slot Level': '4th', 'Invocations Known': '4'},
            8: {'Proficiency Bonus': '+3', 'Features': 'Ability Score Improvement, Eldritch Versatility (Optional)', 'Cantrips Known': 3, 'Spells Known': 9, 'Spell Slots': 2, 'Slot Level': '4th', 'Invocations Known': '4'},
            9: {'Proficiency Bonus': '+4', 'Features': '-', 'Cantrips Known': 3, 'Spells Known': 10, 'Spell Slots': 2, 'Slot Level': '5th', 'Invocations Known': '5'},
            10: {'Proficiency Bonus': '+4', 'Features': 'Otherworldly Patron feature', 'Cantrips Known': 4, 'Spells Known': 10, 'Spell Slots': 2, 'Slot Level': '5th', 'Invocations Known': '5'},
            11: {'Proficiency Bonus': '+4', 'Features': 'Mystic Arcanum (6th level)', 'Cantrips Known': 4, 'Spells Known': 11, 'Spell Slots': 3, 'Slot Level': '5th', 'Invocations Known': '5'},
            12: {'Proficiency Bonus': '+4', 'Features': 'Ability Score Improvement, Eldritch Versatility (Optional)', 'Cantrips Known': 4, 'Spells Known': 11, 'Spell Slots': 3, 'Slot Level': '5th', 'Invocations Known': '6'},
            13: {'Proficiency Bonus': '+5', 'Features': 'Mystic Arcanum (7th level)', 'Cantrips Known': 4, 'Spells Known': 12, 'Spell Slots': 3, 'Slot Level': '5th', 'Invocations Known': '6'},
            14: {'Proficiency Bonus': '+5', 'Features': 'Otherworldly Patron feature', 'Cantrips Known': 4, 'Spells Known': 12, 'Spell Slots': 3, 'Slot Level': '5th', 'Invocations Known': '6'},
            15: {'Proficiency Bonus': '+5', 'Features': 'Mystic Arcanum (8th level)', 'Cantrips Known': 4, 'Spells Known': 13, 'Spell Slots': 3, 'Slot Level': '5th', 'Invocations Known': '7'},
            16: {'Proficiency Bonus': '+5', 'Features': 'Ability Score Improvement, Eldritch Versatility (Optional)', 'Cantrips Known': 4, 'Spells Known': 13, 'Spell Slots': 3, 'Slot Level': '5th', 'Invocations Known': '7'},
            17: {'Proficiency Bonus': '+6', 'Features': 'Mystic Arcanum (9th level)', 'Cantrips Known': 4, 'Spells Known': 14, 'Spell Slots': 4, 'Slot Level': '5th', 'Invocations Known': '7'},
            18: {'Proficiency Bonus': '+6', 'Features': '-', 'Cantrips Known': 4, 'Spells Known': 14, 'Spell Slots': 4, 'Slot Level': '5th', 'Invocations Known': '8'},
            19: {'Proficiency Bonus': '+6', 'Features': 'Ability Score Improvement, Eldritch Versatility (Optional)', 'Cantrips Known': 4, 'Spells Known': 15, 'Spell Slots': 4, 'Slot Level': '5th', 'Invocations Known': '8'},
            20: {'Proficiency Bonus': '+6', 'Features': 'Eldritch Master', 'Cantrips Known': 4, 'Spells Known': 15, 'Spell Slots': 4, 'Slot Level': '5th', 'Invocations Known': '8'}
        },
        "Features": {},
        "Hit Die": '1d8',
        "Proficiencies": {
            'Armor': 'Light armor',
            'Weapons': 'Simple weapons',
            'Tools': 'None',
            "Spellcasting Modifier" : "Charisma",
            'Saving Throws': ['Wisdom', 'Charisma'],
            'Skills': {
                'Choose Number' : 2,
                'Choose From' :  ['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation', 'Nature', 'Religion']
            },
            "Languages": []
        },
        "Equipment": {
            'Choices' : {
                'Choice 1' : {
                    'light crossbow and 20 bolts' : 1,
                    'any simple weapon' : 1,
                    },
                'Choice 2' : {
                    "component pouch": 1,
                    "arcane focus" : 1,
                },
                'Choice 3' : {
                    "scholar's pack" : 1,
                    "dungeoneer's pack" : 1
                },
            },
            "Start With" : {
                "leather armor" : 1,
                "any wimple weapon" : 1,
                "dagger" : 2
            }  
        },
        "Attribute Priority" : ['charisma', 'constitution', 'dexterity', 'intelligence', 'wisdom', 'strength'],
        "Spells" : {
            "Spellcasting": "Warlocks gain their magical abilities through a pact with a powerful otherworldly entity, such as a fiend, a fey, or an otherworldly patron. They have a limited number of spell slots, but their spells are always cast at the highest level.",
            "Spellcasting Modifier": "Charisma",
            "Spell Attack Modifier": "Proficiency bonus + Charisma modifier",
            "Spell DC Save": "8 + Proficiency bonus + Charisma modifier",
            "Preparation": "Warlocks do not prepare spells in the traditional sense. They have a known list of spells and can cast any spell from that list as long as they have spell slots available.",
            "Recovery": "Warlocks recover their expended spell slots after a short rest, making them highly adaptable in spellcasting.",
            "Spell Slots": "Warlocks have a limited number of spell slots per day, but all of their spells are cast at the highest level available to them.",
            "Spells Known": "Warlocks start with a certain number of spells known based on their level, and they learn new spells as they level up.",
            "Change Up": "Warlocks can change their known spells whenever they level up, allowing them to adapt to different situations by selecting new spells.",
            "Progression": "Warlocks choose an Otherworldly Patron, such as the Fiend or the Archfey, which grants them additional spells and unique abilities based on their chosen patron.",
            "Requirements": "Warlocks often use arcane focuses, such as an eldritch tome or a pact weapon, as their spellcasting focuses. They can also use a component pouch.",
            "Key Difference": "Warlocks have a unique feature called Eldritch Invocations, which allows them to customize their spellcasting abilities with various special abilities.",
            "Uniqueness": "Warlocks have a limited number of spell slots, but they can recover them quickly through short rests, making them resourceful spellcasters.",
            "Magic Lore": "Warlocks often have a deep understanding of the otherworldly entities they form pacts with and the dark or mysterious forces they manipulate.",
            "All Class Spells" : {
                "Cantrips" : ["Blade Ward","Chill Touch","Create Bonfire","Eldritch Blast","Friends","Frostbite","Infestation","Mage Hand","Magic Stone","Minor Illusion","Poison Spray","Prestidigitation","Thunderclap","Toll the Dead","True Strike"],
                "1st" : ["Armor of Agathys","Arms of Hadar","Cause Fear","Charm Person","Comprehend Languages","Distort Value","Expeditious Retreat","Hellish Rebuke","Hex","Illusory Script","Protection from Evil and Good","Unseen Servant","Witch Bolt"],
                "2nd" : ["Borrowed Knowledge","Cloud of Daggers","Crown of Madness","Darkness","Earthbind","Enthrall","Flock of Familiars","Hold Person","Invisibility","Mind Spike","Mirror Image","Misty Step","Ray of Enfeeblement","Shadow Blade","Shatter","Spider Climb","Spray Of Cards","Suggestion","Warp Sense"],
                "3rd" : ["Antagonize","Counterspell","Dispel Magic","Enemies Abound","Fear","Fly","Gaseous Form","Hunger Of Hadar","Hypnotic Pattern","Incite Greed","Magic Circle","Major Image","Remove Curse","Summon Lesser Demons","Thunder Step","Tongues","Vampiric Touch"],
                "4th" : ["Banishment","Blight","Charm Monster","Dimension Door","Elemental Bane","Galder's Speedy Courier","Gate Seal","Hallucinatory Terrain","Raulothim's Psychic Lance","Shadow Of Moil","Sickening Radiance","Spirit Of Death"],
                "5th" : ["Contact Other Plane","Danse Macabre","Dream","Enervation","Far Step","Hold Monster","Infernal Calling","Negative Energy Flood","Scrying","Synaptic Static","Wall of Light"],
                "6th" : ["Arcane Gate","Circle of Death","Conjure Fey","Create Undead","Eyebite","Flesh to Stone","Investiture of Flame","Investiture of Ice","Investiture of Stone","Investiture of Wind","Mass Suggestion","Mental Prison","Scatter","Soul Cage","True Seeing"],
                "7th" : ["Crown of Stars","Etherealness","Finger of Death","Forcecage","Plane Shift","Power Word: Pain"],
                "8th" : ["Demiplane","Dominate Monster","Feeblemind","Glibness","Maddening Darkness","Power Word: Stun"],
                "9th" : ["Astral Projection","Foresight","Imprisonment","Power Word: Kill","Psychic Scream","True Polymorph"]
            }
        }
    },



    "Wizard": {
        "ASCII Art": """
 __          ___                  _ 
 \ \        / (_)                | |
  \ \  /\  / / _ ______ _ _ __ __| |
   \ \/  \/ / | |_  / _` | '__/ _` |
    \  /\  /  | |/ / (_| | | | (_| |
     \/  \/   |_/___\__,_|_|  \__,_|
                                    
        """,
        "Name": "Wizard",
        "Description": "A scholarly magic-user capable of manipulating the structures of reality. Wizards are supreme magic-users, defined and united as a class by the spells they cast. Drawing on the subtle weave of magic that permeates the cosmos, wizards cast spells of explosive fire, arcing lightning, subtle deception, brute-force mind control, and much more.",
        "Requirements": "You must have an Intelligence score of 13 or higher in order to multiclass in or out of this class.",
        "Level Chart" : {
            1: {'Proficiency Bonus': '+2', 'Features': 'Spellcasting, Arcane Recovery', 'Cantrips Known': 3, '1st': 2},
            2: {'Proficiency Bonus': '+2', 'Features': 'Arcane Tradition', 'Cantrips Known': 3, '1st': 3},
            3: {'Proficiency Bonus': '+2', 'Features': 'Cantrip Formulas (Optional)', 'Cantrips Known': 3, '1st': 4, '2nd': 2},
            4: {'Proficiency Bonus': '+2', 'Features': 'Ability Score Improvement', 'Cantrips Known': 4, '1st': 4, '2nd': 3},
            5: {'Proficiency Bonus': '+3', 'Cantrips Known': 4, '1st': 4, '2nd': 3, '3rd': 2},
            6: {'Proficiency Bonus': '+3', 'Features': 'Arcane Tradition feature', 'Cantrips Known': 4, '1st': 4, '2nd': 3, '3rd': 3},
            7: {'Proficiency Bonus': '+3', 'Cantrips Known': 4, '1st': 4, '2nd': 3, '3rd': 3, '4th': 1},
            8: {'Proficiency Bonus': '+3', 'Features': 'Ability Score Improvement', 'Cantrips Known': 4, '1st': 4, '2nd': 3, '3rd': 3, '4th': 2},
            9: {'Proficiency Bonus': '+4', 'Cantrips Known': 4, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 1},
            10: {'Proficiency Bonus': '+4', 'Features': 'Arcane Tradition feature', 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2},
            11: {'Proficiency Bonus': '+4', 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1},
            12: {'Proficiency Bonus': '+4', 'Features': 'Ability Score Improvement', 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1},
            13: {'Proficiency Bonus': '+5', 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1},
            14: {'Proficiency Bonus': '+5', 'Features': 'Arcane Tradition feature', 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1},
            15: {'Proficiency Bonus': '+5', 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1},
            16: {'Proficiency Bonus': '+5', 'Features': 'Ability Score Improvement', 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1},
            17: {'Proficiency Bonus': '+6', 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': 1},
            18: {'Proficiency Bonus': '+6', 'Features': 'Spell Mastery', 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 3, '6th': 1, '7th': 1, '8th': 1, '9th': 1},
            19: {'Proficiency Bonus': '+6', 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 3, '6th': 2, '7th': 1, '8th': 1, '9th': 1},
            20: {'Proficiency Bonus': '+6', 'Features': 'Signature Spells', 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 3, '6th': 2, '7th': 2, '8th': 1, '9th': 1}    
        },
        "Features": {},
        "Hit Die": '1d6',
        "Proficiencies": {
            'Armor': 'None',
            'Weapons': 'Daggers, darts, slings, quarterstaffs, light crossbows',
            'Tools': 'None',
            "Spellcasting Modifier" : "Intelligence",
            'Saving Throws': ['Intelligence', 'Wisdom'],
            'Skills': {
                'Choose Number' : 2,
                'Choose From' :  ['Arcana', 'History', 'Insight', 'Investigation', 'Medicine', 'Religion']
            },
            "Languages": []
        },
        "Equipment": {
            'Choices' : {
                'Choice 1' : {
                    'quarterstaff' : 1,
                    'dagger' : 1,
                    },
                'Choice 2' : {
                    "component pouch": 1,
                    "arcane focus" : 1,
                },
                'Choice 3' : {
                    "scholar's pack" : 1,
                    "explorer's pack" : 1
                },
            },
            "Start With" : {
                "spellbook" : 1,
            }  
        },
        "Attribute Priority" : ['intelligence', 'constitution', 'dexterity', 'wisdom', 'charisma', 'strength'],
        "Spells" : {
            "Spellcasting": "Wizards are scholarly spellcasters who learn magic through rigorous study and research. They record spells in their spellbooks and prepare spells each day.",
            "Spellcasting Modifier": "Intelligence",
            "Spell Attack Modifier": "Proficiency bonus + Intelligence modifier",
            "Spell DC Save": "8 + Proficiency bonus + Intelligence modifier",
            "Preparation": "Wizards prepare spells each day by studying their spellbook. They choose a specific number of spells from their spellbook to have prepared for the day.",
            "Recovery": "Wizards recover their expended spell slots after a long rest. They do not have the option for short rest recovery like some other classes.",
            "Spell Slots": "Wizards have a limited number of spell slots per day, which are divided into spell levels. They can use these slots to cast their prepared spells.",
            "Spells Known": "Wizards start with a certain number of spells in their spellbook based on their level. They can learn additional spells by copying them into their spellbook.",
            "Change Up": "Wizards can change their prepared spells each day after a long rest, allowing them to adapt to different challenges.",
            "Progression": "Wizards choose an Arcane Tradition, such as the School of Evocation or the School of Abjuration, which grants them additional spells and unique abilities related to their chosen tradition.",
            "Requirements": "Wizards often use spellbooks as their focus for spellcasting. They must have a spellbook and a component pouch to cast spells.",
            "Key Difference": "Wizards have a unique feature called Arcane Recovery, which allows them to recover spell slots during a short rest, making them highly resourceful spellcasters.",
            "Uniqueness": "Wizards are known for their extensive spellbooks and their ability to prepare spells daily, giving them great versatility in their spellcasting.",
            "Magic Lore": "Wizards are scholars of arcane magic, and they often have a deep understanding of magical theory, history, and the intricacies of spellcraft.",
            "All Class Spells" : {
                "Cantrips" : ["Acid Splash","Blade Ward","Chill Touch","Control Flames","Create Bonfire","Dancing Lights","Encode Thoughts","Fire Bolt","Friends","Frostbite","Gust","Infestation","Light","Mage Hand","Mending","Message","Minor Illusion","Mold Earth","Poison Spray","Prestidigitation","Ray of Frost","Sapping Sting","Shape Water","Shocking Grasp","Thunderclap","Toll the Dead","True Strike"],
                "1st" : ["Absorb Elements","Alarm","Burning Hands","Catapult","Cause Fear","Charm Person","Chromatic Orb","Color Spray","Comprehend Languages","Detect Magic","Disguise Self","Distort Value","Earth Tremor","Expeditious Retreat","False Life","Feather Fall","Find Familiar","Fog Cloud","Frost Fingers","Gift of Alacrity","Grease","Ice Knife","Identify","Illusory Script","Jim's Magic Missile","Jump","Longstrider","Mage Armor","Magic Missile","Magnify Gravity","Protection from Evil and Good","Ray of Sickness","Shield","Silent Image","Silvery Barbs","Sleep","Snare","Tasha's Hideous Laughter","Tenser's Floating Disk","Thunderwave","Unseen Servant","Witch Bolt"],
                "2nd" : ["Aganazzar's Scorcher","Air Bubble","Alter Self","Arcane Lock","Blindness/Deafness","Blur","Borrowed Knowledge","Cloud of Daggers","Continual Flame","Crown of Madness","Darkness","Darkvision","Detect Thoughts","Dragon's Breath","Dust Devil","Earthbind","Enlarge/Reduce","Flaming Sphere","Flock of Familiars","Fortune's Favor","Gentle Repose","Gift of Gab","Gust of Wind","Hold Person","Immovable Object","Invisibility","Jim's Glowing Coin","Kinetic Jaunt","Knock","Levitate","Locate Object","Magic Mouth","Magic Weapon","Maximillian's Earthen Grasp","Melf's Acid Arrow","Mind Spike","Mirror Image","Misty Step","Nathair's Mischief","Nystul's Magic Aura","Phantasmal Force","Pyrotechnics","Ray of Enfeeblement","Rime's Binding Ice","Rope Trick","Scorching Ray","See Invisibility","Shadow Blade","Shatter","Skywrite","Snilloc's Snowball Storm","Spider Climb","Spray Of Cards","Suggestion","Vortex Warp","Warding Wind","Warp Sense","Web","Wither and Bloom","Wristpocket"],
                "3rd" : ["Animate Dead","Antagonize","Ashardalon's Stride","Bestow Curse","Blink","Catnap","Clairvoyance","Counterspell","Dispel Magic","Enemies Abound","Erupting Earth","Fast Friends","Fear","Feign Death","Fireball","Flame Arrows","Fly","Galder's Tower","Gaseous Form","Glyph of Warding","Haste","Hypnotic Pattern","Incite Greed","Leomund's Tiny Hut","Life Transference","Lightning Bolt","Magic Circle","Major Image","Melf's Minute Meteors","Nondetection","Phantom Steed","Protection from Energy","Pulse Wave","Remove Curse","Sending","Sleet Storm","Slow","Stinking Cloud","Summon Lesser Demons","Thunder Step","Tidal Wave","Tiny Servant","Tongues","Vampiric Touch","Wall of Sand","Wall of Water","Water Breathing"],
                "4th" : ["Arcane Eye","Banishment","Blight","Charm Monster","Confusion","Conjure Minor Elementals","Control Water","Dimension Door","Elemental Bane","Evard's Black Tentacles","Fabricate","Fire Shield","Galder's Speedy Courier","Gate Seal","Gravity Sinkhole","Greater Invisibility","Hallucinatory Terrain","Ice Storm","Leomund's Secret Chest","Locate Creature","Mordenkainen's Faithful Hound","Mordenkainen's Private Sanctum","Otiluke's Resilient Sphere","Phantasmal Killer","Polymorph","Raulothim's Psychic Lance","Sickening Radiance","Spirit Of Death","Stone Shape","Stoneskin","Storm Sphere","Summon Greater Demon","Vitriolic Sphere","Wall of Fire","Watery Sphere"],
                "5th" : ["Animate Objects","Bigby's Hand","Cloudkill","Cone of Cold","Conjure Elemental","Contact Other Plane","Control Winds","Create Spelljamming Helm","Creation","Danse Macabre","Dawn","Dominate Person","Dream","Enervation","Far Step","Geas","Hold Monster","Immolation","Infernal Calling","Legend Lore","Mislead","Modify Memory","Negative Energy Flood","Passwall","Planar Binding","Rary's Telepathic Bond","Scrying","Seeming","Skill Empowerment","Steel Wind Strike","Summon Draconic Spirit","Synaptic Static","Telekinesis","Teleportation Circle","Temporal Shunt","Transmute Rock","Wall of Force","Wall of Light","Wall of Stone"],
                "6th" : ["Arcane Gate","Chain Lightning","Circle of Death","Contingency","Create Homunculus","Create Undead","Disintegrate","Drawmij's Instant Summons","Eyebite","Fizban's Platinum Shield","Flesh to Stone","Globe of Invulnerability","Gravity Fissure","Guards and Wards","Investiture of Flame","Investiture of Ice","Investiture of Stone","Investiture of Wind","Magic Jar","Mass Suggestion","Mental Prison","Move Earth","Otiluke's Freezing Sphere","Otto's Irresistible Dance","Programmed Illusion","Scatter","Soul Cage","Sunbeam","Tenser's Transformation","True Seeing","Wall of Ice"],
                "7th" : ["Create Magen","Crown of Stars","Delayed Blast Fireball","Draconic Transformation","Etherealness","Finger of Death","Forcecage","Mirage Arcane","Mordenkainen's Magnificent Mansion","Mordenkainen's Sword","Plane Shift","Power Word: Pain","Prismatic Spray","Project Image","Reverse Gravity","Sequester","Simulacrum","Symbol","Teleport","Tether Essence","Whirlwind"],
                "8th" : ["Abi-Dalzim's Horrid Wilting","Antimagic Field","Antipathy/Sympathy","Clone","Control Weather","Dark Star","Demiplane","Dominate Monster","Feeblemind","Illusory Dragon","Incendiary Cloud","Maddening Darkness","Maze","Mighty Fortress","Mind Blank","Power Word: Stun","Reality Break","Sunburst","Telepathy"],
                "9th" : ["Astral Projection","Foresight","Gate","Imprisonment","Invulnerability","Mass Polymorph","Meteor Swarm","Power Word: Kill","Prismatic Wall","Psychic Scream","Ravenous Void","Shapechange","Time Ravage","Time Stop","True Polymorph","Weird","Wish"]
            }
        }
    }
}
