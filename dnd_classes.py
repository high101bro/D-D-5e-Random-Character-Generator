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
        "Features": {
            "Rage": "At 1st level, you can enter a rage as a bonus action. "
                    "While raging, you gain several benefits, including advantage on Strength checks and saves, "
                    "bonus damage to melee attacks, and resistance to certain types of damage. "
                    "Rage lasts for 1 minute and ends early if you are knocked unconscious or your turn ends and you haven’t attacked "
                    "a hostile creature or taken damage since your last turn.",
            "Unarmored Defense": "Beginning at 1st level, while not wearing armor, "
                                "your Armor Class (AC) equals 10 + your Dexterity modifier + your Constitution modifier. "
                                "This allows you to have a strong defense even without traditional armor.",
            "Reckless Attack": "Starting at 2nd level, you can choose to make your attacks with advantage on your turn, "
                            "but this also allows enemies to have advantage on their attacks against you until your next turn. "
                            "This feature enhances your combat abilities but comes with increased vulnerability.",
            "Danger Sense": "At 2nd level, you gain an uncanny sense of danger. "
                            "You have advantage on Dexterity saving throws against effects that you can see, "
                            "such as traps and spells, to avoid danger more effectively.",
            "Primal Path": "At 3rd level, you choose a Primal Path that defines your barbarian archetype, "
                        "granting you additional features and abilities based on your chosen path.",
            "Primal Knowledge (Optional)": "At 3rd level, you have the option to gain proficiency with two skills from the list: "
                                            "Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival.",
            "Ability Score Improvement": "At 4th level and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice "
                                        "by 2, or you can increase two ability scores of your choice by 1. This allows you to customize your character as you progress.",
            "Extra Attack": "Starting at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. "
                            "This feature significantly enhances your combat capabilities.",
            "Fast Movement": "At 5th level, your speed increases by 10 feet while you are not wearing heavy armor. "
                            "This allows you to move swiftly in combat and exploration.",
            "Path feature": "At 6th level and again at 10th, 14th, and 18th level, your chosen Primal Path grants you additional features and abilities "
                            "that reflect the unique path you've embraced.",
            "Feral Instinct": "At 7th level, you have advantage on initiative rolls, and you can act normally on your first turn in combat, "
                            "even if you are surprised. This feature reflects your heightened awareness and readiness in battle.",
            "Instinctive Pounce (Optional)": "At 7th level, you can use your reaction to move up to half your speed when a creature ends its turn "
                                            "within 30 feet of you. This allows you to quickly close the distance to your foes.",
            "Brutal Critical (1 die)": "Beginning at 9th level, you can roll one additional weapon damage die when determining the extra damage for a critical hit. "
                                    "This feature increases your damage potential in combat.",
            "Relentless Rage": "At 11th level, if you drop to 0 hit points while you’re raging and don’t die outright, "
                            "you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead. "
                            "This feature reflects your sheer determination and ability to push through even when severely wounded.",
            "Brutal Critical (2 dice)": "Starting at 13th level, you can roll two additional weapon damage dice when determining the extra damage for a critical hit. "
                                    "This further enhances your damage output during critical hits.",
            "Persistent Rage": "At 15th level, your rage can't be ended early due to failing to attack a hostile creature or take damage since your last turn. "
                            "This allows you to maintain your rage for longer durations.",
            "Brutal Critical (3 dice)": "Beginning at 17th level, you can roll three additional weapon damage dice when determining the extra damage for a critical hit. "
                                    "This makes your critical hits even more devastating in combat.",
            "Indomitable Might": "At 18th level, if your total for a Strength check is less than your Strength score, "
                                "you can use that score in place of the total. This feature showcases your incredible physical strength.",
            "Primal Champion": "At 20th level, your Strength and Constitution scores increase by 4"
        },
        "Hit Die": '1d12',
        "Proficiencies": {
            'Armor': ['Light armor', 'medium armor', 'shields'],
            'Weapons': ['Simple weapons', 'martial weapons'],
            'Tools': 'None',
            "Spellcasting Modifier" : "None",
            'Saving Throws': ['Strength', 'Constitution'],
            "Skills": {
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
            1: {'Proficiency Bonus': '+2','Features': ['Spellcasting', 'Bardic Inspiration (d6)'],'Cantrips Known': 2,'Spells Known': 4,'1st': 2,'2nd': '-','3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            2: {'Proficiency Bonus': '+2','Features': ['Jack of All Trades', 'Song of Rest (d6)', 'Magical Inspiration (Optional)'],'Cantrips Known': 2,'Spells Known': 5,'1st': 3,'2nd': '-','3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            3: {'Proficiency Bonus': '+2','Features': ['Bard College', 'Expertise'],'Cantrips Known': 2,'Spells Known': 6,'1st': 4,'2nd': 2,'3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            4: {'Proficiency Bonus': '+2','Features': ['Ability Score Improvement', 'Bardic Versatility (Optional)'],'Cantrips Known': 3,'Spells Known': 7,'1st': 4,'2nd': 3,'3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            5: {'Proficiency Bonus': '+3','Features': ['Bardic Inspiration (d8)', 'Font of Inspiration'],'Cantrips Known': 3,'Spells Known': 8,'1st': 4,'2nd': 3,'3rd': 2,'4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            6: {'Proficiency Bonus': '+3','Features': ['Countercharm', 'Bard College Feature'],'Cantrips Known': 3,'Spells Known': 9,'1st': 4,'2nd': 3,'3rd': 3,'4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            7: {'Proficiency Bonus': '+3','Features': ['-'],'Cantrips Known': 3,'Spells Known': 10,'1st': 4,'2nd': 3,'3rd': 3,'4th': 1,'5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            8: {'Proficiency Bonus': '+3','Features': ['Ability Score Improvement', 'Bardic Versatility (Optional)'],'Cantrips Known': 3,'Spells Known': 11,'1st': 4,'2nd': 3,'3rd': 3,'4th': 2,'5th': '-','6th': '-','7th': '-','8th': '-','9th': '-',},
            9: {'Proficiency Bonus': '+4','Features': ['Song of Rest (d8)'],'Cantrips Known': 3,'Spells Known': 12,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 1,'6th': '-','7th': '-','8th': '-','9th': '-',},
            10: {'Proficiency Bonus': '+4','Features': ['Bardic Inspiration (d10)', 'Expertise', 'Magical Secrets'],'Cantrips Known': 4,'Spells Known': 14,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': '-','7th': '-','8th': '-','9th': '-',},
            11: {'Proficiency Bonus': '+4','Features': ['-'],'Cantrips Known': 4,'Spells Known': 15,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': '-','8th': '-','9th': '-',},
            12: {'Proficiency Bonus': '+4','Features': ['Ability Score Improvement', 'Bardic Versatility (Optional)'],'Cantrips Known': 4,'Spells Known': 15,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': '-','8th': '-','9th': '-',},
            13: {'Proficiency Bonus': '+5','Features': ['Song of Rest (d10)'],'Cantrips Known': 4,'Spells Known': 16,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': '-','9th': '-',},
            14: {'Proficiency Bonus': '+5','Features': ['Magical Secrets', 'Bard College Feature'],'Cantrips Known': 4,'Spells Known': 18,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': '-','9th': '-',},
            15: {'Proficiency Bonus': '+5','Features': ['Bardic Inspiration (d12)'],'Cantrips Known': 4,'Spells Known': 19,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': '-',},
            16: {'Proficiency Bonus': '+5','Features': ['Ability Score Improvement', 'Bardic Versatility (Optional)'],'Cantrips Known': 4,'Spells Known': 19,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': '-',},
            17: {'Proficiency Bonus': '+6','Features': ['Song of Rest (d12)'],'Cantrips Known': 4,'Spells Known': 20,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': 1,},
            18: {'Proficiency Bonus': '+6','Features': ['Magical Secrets'],'Cantrips Known': 4,'Spells Known': 22,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 1,'7th': 1,'8th': 1,'9th': 1,},
            19: {'Proficiency Bonus': '+6','Features': ['Ability Score Improvement', 'Bardic Versatility (Optional)'],'Cantrips Known': 4,'Spells Known': 22,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 2,'7th': 1,'8th': 1,'9th': 1,},
            20: {'Proficiency Bonus': '+6','Features': ['Superior Inspiration'],'Cantrips Known': 4,'Spells Known': 22,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 2,'7th': 2,'8th': 1,'9th': 1,}
        },
        "Features": {
            "Spellcasting": "At 1st level, you gain the ability to cast spells from the bard spell list. "
                            "You learn a number of cantrips and spells, and your spellcasting ability is Charisma. "
                            "You can use a musical instrument as a spellcasting focus.",
            "Bardic Inspiration (d6)": "At 1st level, you can inspire others through stirring words or music. "
                                        "As a bonus action, you can grant a creature within 60 feet of you a Bardic Inspiration die (d6). "
                                        "The creature can roll this die and add the number rolled to one ability check, "
                                        "attack roll, or saving throw it makes. The die can be used after the roll, but before the outcome is determined.",
            "Bard Song of Rest (d10)": "The Bard Song of Rest (d10) is a feature of the bard class in Dungeons and Dragons (D&D) 5th Edition. "
                                       "When a bard plays soothing music or offers words of encouragement during a short rest, "
                                       "the party members regain an extra 1d10 hit points if they spend Hit Dice to heal. "
                                       "This bonus hit points restoration is in addition to any Hit Dice spent normally during the rest.",
            "Bard College Feature": "The Bard College Feature is a key aspect of the bard class in Dungeons and Dragons (D&D) 5th Edition. "
                                    "Bards choose a specific college that represents their area of expertise and style of performance. "
                                    "This choice grants them unique abilities, spells, and a thematic connection to their chosen college, enhancing their bardic talents and role within the party.",
            "Jack of All Trades": "Starting at 2nd level, you can add half your proficiency bonus, rounded down, to any ability check you make "
                                "that doesn't already include your proficiency bonus. This feature reflects your broad range of skills.",
            "Song of Rest (d6)": "At 2nd level, if you or any friendly creatures who can hear your performance regain hit points at the end of a short rest, "
                                "each of those creatures regains an extra 1d6 hit points. The extra hit points increase as you gain bard levels.",
            "Magical Inspiration (Optional)": "Starting at 2nd level, you can use your Bardic Inspiration to inspire someone to create a magical effect. "
                                            "The creature can add the Bardic Inspiration die to one damage roll it makes for a spell it casts. "
                                            "This feature enhances the magical abilities of your allies.",
            "Bard College": "At 3rd level, you choose a Bard College that represents your area of expertise and focus. "
                            "This choice grants you additional features and abilities based on your chosen college.",
            "Expertise": "Starting at 3rd level, choose two of your skill proficiencies or one of your skill proficiencies and your proficiency "
                        "with thieves' tools. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies. "
                        "This reflects your growing expertise in certain skills.",
            "Ability Score Improvement": "At 4th level and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice "
                                        "by 2, or you can increase two ability scores of your choice by 1. This allows you to customize your character as you progress.",
            "Bardic Versatility (Optional)": "Starting at 4th level, you can replace one spell you know with another from the bard spell list "
                                            "whenever you gain a level in this class. This allows you to adapt your spells known as your character grows.",
            "Bardic Inspiration (d8)": "At 5th level, the Bardic Inspiration die increases to a d8, providing more potent inspiration to your allies.",
            "Font of Inspiration": "Starting at 5th level, you regain expended uses of Bardic Inspiration when you finish a short rest. "
                                "This feature allows you to inspire your allies more frequently.",
            "Countercharm": "At 6th level, you gain the ability to use musical notes or words of power to disrupt mind-influencing effects. "
                            "As an action, you can start a performance that lasts until the end of your next turn. "
                            "During that time, you and any friendly creatures within 30 feet of you have advantage on saving throws against being frightened or charmed. "
                            "This feature reflects your ability to bolster your allies' mental fortitude.",
            "Song of Rest (d8)": "At 9th level, the extra hit points granted by your Song of Rest feature increase to 1d8.",
            "Bardic Inspiration (d10)": "At 10th level, the Bardic Inspiration die increases to a d10, providing even greater inspiration to your allies.",
            "Magical Secrets": "Starting at 10th level, you can learn two spells from any class, including spells that are not on the bard spell list. "
                            "This allows you to expand your magical repertoire significantly.",
            "Bardic Inspiration (d12)": "At 15th level, the Bardic Inspiration die increases to a d12, providing the most potent inspiration to your allies.",
            "Superior Inspiration": "At 20th level, when you roll initiative and have no uses of Bardic Inspiration left, you regain one use. "
                                    "Additionally, whenever you use Bardic Inspiration, you can roll a d12 instead of the normal die. "
                                    "This feature reflects your unmatched ability to inspire and lead your allies."
        },
        "Hit Die": '1d8',
        "Proficiencies": {
            'Armor': 'Light armor',
            'Weapons': 'Simple weapons, hand crossbows, longswords, rapiers, shortswords',
            'Tools': 'Three musical instruments of your choice',
            "Spellcasting Modifier" : "Charisma",
            'Saving Throws': ['Dexterity', 'Charisma'],
            "Skills": {
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
                "8th" : ["Dominate Monster","Feeblemind","Glibness","Mind Blank","Power Word - Stun"],
                "9th" : ["Foresight","Mass Polymorph","Power Word - Heal","Power Word - Kill","Psychic Scream","True Polymorph"]
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
            1: {'Proficiency Bonus': '+2','Features': ['Spellcasting', 'Divine Domain'],'Cantrips Known': 3,'1st': 2,'2nd': '-','3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            2: {'Proficiency Bonus': '+2','Features': ['Channel Divinity (x1)', 'Divine Domain Feature', 'Harness Divine Power (Optional)'],'Cantrips Known': 3,'1st': 3,'2nd': '-','3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            3: {'Proficiency Bonus': '+2','Features': ['-'],'Cantrips Known': 3,'1st': 4,'2nd': 2,'3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            4: {'Proficiency Bonus': '+2','Features': ['Ability Score Improvement', 'Cantrip Versatility (Optional)'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            5: {'Proficiency Bonus': '+3','Features': ['Destroy Undead (CR 1/2)'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 2,'4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            6: {'Proficiency Bonus': '+3','Features': ['Channel Divinity (x2)', 'Divine Domain Feature'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            7: {'Proficiency Bonus': '+3','Features': ['-'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 1,'5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            8: {'Proficiency Bonus': '+3','Features': ['Ability Score Improvement', 'Destroy Undead (CR 1)', 'Divine Domain Feature', 'Cantrip Versatility (Optional)'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 2,'5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            9: {'Proficiency Bonus': '+4','Features': ['-'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 1,'6th': '-','7th': '-','8th': '-','9th': '-'},
            10: {'Proficiency Bonus': '+4','Features': ['Divine Intervention'],'Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': '-','7th': '-','8th': '-','9th': '-'},
            11: {'Proficiency Bonus': '+4','Features': ['Destroy Undead (CR 2)'],'Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': '-','8th': '-','9th': '-'},
            12: {'Proficiency Bonus': '+4','Features': ['Ability Score Improvement', 'Cantrip Versatility (Optional)'],'Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': '-','8th': '-','9th': '-'},
            13: {'Proficiency Bonus': '+5','Features': ['-'],'Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': '-','9th': '-'},
            14: {'Proficiency Bonus': '+5','Features': ['Destroy Undead (CR 3)'],'Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': '-','9th': '-'},
            15: {'Proficiency Bonus': '+5','Features': ['-'],'Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': '-'},
            16: {'Proficiency Bonus': '+5','Features': ['Ability Score Improvement', 'Cantrip Versatility (Optional)'],'Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': '-'},
            17: {'Proficiency Bonus': '+6','Features': ['Destroy Undead (CR 4)', 'Divine Domain Feature'],'Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': 1},
            18: {'Proficiency Bonus': '+6','Features': ['Channel Divinity (x3)'],'Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 1,'7th': 1,'8th': 1,'9th': 1},
            19: {'Proficiency Bonus': '+6','Features': ['Ability Score Improvement', 'Cantrip Versatility (Optional)'],'Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 1,'7th': 1,'8th': 1,'9th': 1},
            20: {'Proficiency Bonus': '+6','Features': ['Divine Intervention improvement'],'Cantrips Known': 5,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 2,'7th': 2,'8th': 1,'9th': 1}
        },
        "Features": {
            "Spellcasting": "At 1st level, you gain the ability to cast spells from the cleric spell list. "
                            "You learn a number of cantrips and spells, and your spellcasting ability is Wisdom. "
                            "You can use a holy symbol as a spellcasting focus.",
            "Divine Domain": "At 1st level, you choose a Divine Domain that represents your deity's domain of influence. "
                            "This choice grants you additional features and abilities based on your chosen domain.",
            "Divine Domain Feature" : "This feature represents the specific domain or aspect of their deity that a cleric dedicates themselves to. "
                                      "It grants unique abilities, spells, and powers that align with the cleric's chosen domain. "
                                      "Each domain has its own set of features, such as bonus spells, Channel Divinity options, and domain-specific abilities, "
                                      "that enhance the cleric's role and capabilities within the party. The Divine Domain Feature is a fundamental choice for clerics, "
                                      "shaping their role and abilities as they serve their deity's divine purpose.",
            "Channel Divinity (x1)": "At 2nd level, you gain the ability to channel divine energy directly from your deity. "
                                    "You can use this ability to invoke divine effects based on your chosen domain. "
                                    "You have one use of this ability before needing a short or long rest to use it again.",
            "Harness Divine Power (Optional)": "Starting at 2nd level, you can call upon your deity's power to regain expended spell slots. "
                                            "This feature enhances your spellcasting capabilities.",
            "Jack of All Trades": "Starting at 2nd level, you can add half your proficiency bonus, rounded down, to any ability check you make "
                                "that doesn't already include your proficiency bonus. This feature reflects your diverse knowledge.",
            "Destroy Undead (CR 1/2)": "At 5th level, you gain the ability to turn or destroy undead creatures with a Challenge Rating of 1/2 or lower. "
                                    "This ability allows you to repel or destroy undead foes.",
            "Channel Divinity (x2)": "At 6th level, you gain an additional use of your Channel Divinity ability, "
                                    "allowing you to call upon your deity's power more frequently.",
            "Destroy Undead (CR 1)": "At 8th level, your Destroy Undead ability now affects undead creatures with a Challenge Rating of 1 or lower. "
                                    "This allows you to combat stronger undead foes.",
            "Divine Intervention": "At 10th level, you can call upon your deity for divine intervention in dire situations. "
                                "This ability allows your deity to directly intervene in the world on your behalf.",
            "Destroy Undead (CR 2)": "At 11th level, your Destroy Undead ability now affects undead creatures with a Challenge Rating of 2 or lower. "
                                    "This allows you to confront even more powerful undead foes.",
            "Destroy Undead (CR 3)": "At 14th level, your Destroy Undead ability now affects undead creatures with a Challenge Rating of 3 or lower. "
                                    "You become a formidable force against undead enemies.",
            "Destroy Undead (CR 4)": "At 17th level, your Destroy Undead ability now affects undead creatures with a Challenge Rating of 4 or lower. "
                                    "This ability allows you to confront the most powerful undead foes.",
            "Divine Intervention improvement": "At 20th level, your Divine Intervention ability becomes more reliable and effective. "
                                            "Your deity is more likely to respond to your call for intervention.",
            "Cantrip Versatility (Optional)": "Starting at 4th level, you can replace one cantrip you know with another from the cleric spell list "
                                            "whenever you gain a level in this class. This allows you to adapt your cantrips as your character grows.",
            "Ability Score Improvement": "At 4th level and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice "
                                        "by 2, or you can increase two ability scores of your choice by 1. This allows you to customize your character as you progress."
        },
        "Hit Die": '1d8',
        "Proficiencies": {
            'Armor': 'Light armor, medium armor, shields',
            'Weapons': 'All simple weapons',
            'Tools': 'None',
            "Spellcasting Modifier" : "Wisdom",
            'Saving Throws': ['Wisdom', 'Charisma'],
            "Skills": {
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
            1: {'Proficiency Bonus': '+2','Features': ['Druidic', 'Spellcasting'],'Cantrips Known': 2,'1st': 2,'2nd': '-','3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            2: {'Proficiency Bonus': '+2','Features': ['Wild Shape', 'Druid Circle', 'Wild Companion (Optional)'],'Cantrips Known': 2,'1st': 3,'2nd': '-','3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            3: {'Proficiency Bonus': '+2','Features': ['-'],'Cantrips Known': 2,'1st': 4,'2nd': 2,'3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            4: {'Proficiency Bonus': '+2','Features': ['Wild Shape improvement', 'Ability Score Improvement', 'Cantrip Versatility (Optional)'],'Cantrips Known': 3,'1st': 4,'2nd': 3,'3rd': '-','4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            5: {'Proficiency Bonus': '+3','Features': ['-'],'Cantrips Known': 3,'1st': 4,'2nd': 3,'3rd': 2,'4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            6: {'Proficiency Bonus': '+3','Features': ['Druid Circle Feature'],'Cantrips Known': 3,'1st': 4,'2nd': 3,'3rd': 3,'4th': '-','5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            7: {'Proficiency Bonus': '+3','Features': ['-'],'Cantrips Known': 3,'1st': 4,'2nd': 3,'3rd': 3,'4th': 1,'5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            8: {'Proficiency Bonus': '+3','Features': ['Wild Shape improvement', 'Ability Score Improvement', 'Cantrip Versatility (Optional)'],'Cantrips Known': 3,'1st': 4,'2nd': 3,'3rd': 3,'4th': 2,'5th': '-','6th': '-','7th': '-','8th': '-','9th': '-'},
            9: {'Proficiency Bonus': '+4','Features': ['-'],'Cantrips Known': 3,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 1,'6th': '-','7th': '-','8th': '-','9th': '-'},
            10: {'Proficiency Bonus': '+4','Features': ['Druid Circle Feature'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': '-','7th': '-','8th': '-','9th': '-'},
            11: {'Proficiency Bonus': '+4','Features': ['-'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': '-','8th': '-','9th': '-'},
            12: {'Proficiency Bonus': '+4','Features': ['Ability Score Improvement', 'Cantrip Versatility (Optional)'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': '-','8th': '-','9th': '-'},
            13: {'Proficiency Bonus': '+5','Features': ['-'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': '-','9th': '-'},
            14: {'Proficiency Bonus': '+5','Features': ['Druid Circle Feature'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': '-','9th': '-'},
            15: {'Proficiency Bonus': '+5','Features': ['-'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': '-'},
            16: {'Proficiency Bonus': '+5','Features': ['Ability Score Improvement', 'Cantrip Versatility (Optional)'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': '-'},
            17: {'Proficiency Bonus': '+6','Features': ['-'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 2,'6th': 1,'7th': 1,'8th': 1,'9th': 1},
            18: {'Proficiency Bonus': '+6','Features': ['Timeless Body', 'Beast Spells'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 1,'7th': 1,'8th': 1,'9th': 1},
            19: {'Proficiency Bonus': '+6','Features': ['Ability Score Improvement', 'Cantrip Versatility (Optional)'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 2,'7th': 1,'8th': 1,'9th': 1},
            20: {'Proficiency Bonus': '+6','Features': ['Archdruid'],'Cantrips Known': 4,'1st': 4,'2nd': 3,'3rd': 3,'4th': 3,'5th': 3,'6th': 2,'7th': 2,'8th': 1,'9th': 1}
        },
        "Features": {
            "Druidic": "At 1st level, you gain the ability to speak and understand Druidic, the secret language of the druids. "
                    "This language allows you to communicate with other druids and understand the natural world better.",
            "Druid Circle Feature": "The Druid Circle Feature is a key aspect of the druid class in Dungeons and Dragons (D&D) 5th Edition. "
                                    "Druids choose a specific circle, such as the Circle of the Land or Circle of the Moon, "
                                    "which represents their connection to nature and their unique magical abilities. "
                                    "This choice grants them access to circle-specific spells and features, shaping their role and abilities within the party.",
            "Spellcasting": "At 1st level, you gain the ability to cast spells from the druid spell list. "
                            "You learn a number of cantrips and spells, and your spellcasting ability is Wisdom. "
                            "You can use a druidic focus as a spellcasting focus.",
            "Wild Shape": "At 2nd level, you gain the ability to transform into animals using Wild Shape. "
                        "This ability allows you to take on the form of a variety of creatures, gaining their abilities and physical characteristics.",
            "Druid Circle": "At 2nd level, you choose a Druid Circle that represents your connection to a particular aspect of nature. "
                            "This choice grants you additional features and abilities based on your chosen circle.",
            "Wild Companion (Optional)": "Starting at 2nd level, you can choose to have a faithful animal companion by your side. "
                                        "This companion aids you in various ways and grows stronger as you level up.",
            "Wild Shape improvement": "At 4th level, your Wild Shape ability improves, allowing you to transform into more powerful creatures. "
                                    "You can also choose to become more proficient with a specific Wild Shape form.",
            "Ability Score Improvement": "At 4th level and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice "
                                        "by 2, or you can increase two ability scores of your choice by 1. This allows you to customize your character as you progress.",
            "Cantrip Versatility (Optional)": "Starting at 4th level, you can replace one cantrip you know with another from the druid spell list "
                                            "whenever you gain a level in this class. This allows you to adapt your cantrips as your character grows.",
            "Beast Spells": "At 18th level, you can cast spells while in Wild Shape form, merging your spellcasting abilities with your transformed state.",
            "Archdruid": "At 20th level, you become an Archdruid, gaining powerful abilities. "
                        "You can use your Wild Shape an unlimited number of times, and you gain access to high-level spells."

        },
        "Hit Die": "1d8",
        "Proficiencies": {
            "Armor": "Light armor, medium armor, shields (druids will not wear armor or use shields made of metal)",
            "Weapons": "Clubs, daggers, darts, javelins, maces, quarterstaffs, scimitars, sickles, slings, spears",
            "Tools": "Herbalism kit",
            "Spellcasting Modifier" : "Wisdom",
            "Saving Throws": ["Intelligence", "Wisdom"],
            "Skills": {
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
                "4th" : ["Blight","Charm Monster","Confusion","Conjure Minor Elementals","Conjure Woodland Beings","Control Water","Dominate Beast","Elemental Bane","Freedom of Movement","Giant Insect","Grasping Vine","Guardian of Nature","Hallucinatory Terrain","Ice Storm","Locate Creature","Polymorph","Stone Shape","Stoneskin","Wall of Fire","Watery Sphere"],
                "5th" : ["Antilife Shell","Awaken","Commune with Nature","Conjure Elemental","Contagion","Control Winds","Geas","Greater Restoration","Insect Plague","Maelstrom","Mass Cure Wounds","Planar Binding","Reincarnate","Scrying","Summon Draconic Spirit","Transmute Rock","Tree Stride","Wall of Stone","Wrath of Nature"],
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
            1: {"Proficiency Bonus": "+2","Features": ["Fighting Style", "Second Wind"]},
            2: {"Proficiency Bonus": "+2","Features": ["Action Surge (x1)"]},
            3: {"Proficiency Bonus": "+2","Features": ["Martial Archetype"]},
            4: {"Proficiency Bonus": "+2","Features": ["Ability Score Improvement", "Martial Versatility (Optional)"]},
            5: {"Proficiency Bonus": "+3","Features": ["Extra Attack (x1)"]},
            6: {"Proficiency Bonus": "+3","Features": ["Ability Score Improvement", "Martial Versatility (Optional)"]},
            7: {"Proficiency Bonus": "+3","Features": ["Martial Archetype Feature"]},
            8: {"Proficiency Bonus": "+3","Features": ["Ability Score Improvement", "Martial Versatility (Optional)"]},
            9: {"Proficiency Bonus": "+4","Features": ["Indomitable (x1)"]},
            10: {"Proficiency Bonus": "+4","Features": ["Martial Archetype Feature"]},
            11: {"Proficiency Bonus": "+4","Features": ["Extra Attack (x2)"]},
            12: {"Proficiency Bonus": "+4","Features": ["Ability Score Improvement", "Martial Versatility (Optional)"]},
            13: {"Proficiency Bonus": "+5","Features": ["Indomitable (x2)"]},
            14: {"Proficiency Bonus": "+5","Features": ["Ability Score Improvement", "Martial Versatility (Optional)"]},
            15: {"Proficiency Bonus": "+5","Features": ["Martial Archetype Feature"]},
            16: {"Proficiency Bonus": "+5","Features": ["Ability Score Improvement", "Martial Versatility (Optional)"]},
            17: {"Proficiency Bonus": "+6","Features": ["Action Surge (x2)", "Indomitable (x3)"]},
            18: {"Proficiency Bonus": "+6","Features": ["Martial Archetype Feature"]},
            19: {"Proficiency Bonus": "+6","Features": ["Ability Score Improvement", "Martial Versatility (Optional)"]},
            20: {"Proficiency Bonus": "+6","Features": ["Extra Attack (x3)"]}
        },
        "Features": {
            "Fighting Style": "At 1st level, you choose a Fighting Style that defines your approach to combat. "
                            "This choice grants you specific combat benefits such as increased accuracy or better defense.",
            "Second Wind": "At 1st level, you can tap into your reserves to regain some hit points as a bonus action in combat.",
            "Action Surge (x1)": "At 2nd level, you can push yourself beyond your normal limits, taking an additional action on your turn. "
                                "You regain this ability after a short or long rest.",
            "Martial Archetype": "At 3rd level, you choose a Martial Archetype that represents your specialized combat path, "
                                "such as being a Champion, Battle Master, or Eldritch Knight. This choice grants you unique features "
                                "and abilities related to your chosen path.",
            "Ability Score Improvement": "At 4th level and again at 6th, 8th, 12th, 14th, 16th, and 19th level, you can increase one ability score "
                                        "of your choice by 2, or you can increase two ability scores of your choice by 1. This allows you to customize your character.",
            "Martial Versatility (Optional)": "Starting at 4th level, you can replace one fighting style or Martial Archetype Feature you know "
                                            "with another option whenever you gain a level in this class. This allows you to adapt your abilities as needed.",
            "Martial Archetype Feature": "The Martial Archetype Feature is a key aspect of the fighter class in the Dungeons and Dragons (D&D) 5th Edition role-playing game. "
                                         "It represents the fighter's chosen combat specialization, granting them unique abilities and combat techniques that define their style and role on the battlefield.",
            "Extra Attack (x1)": "At 5th level, you gain the ability to make two attacks instead of one when you take the Attack action on your turn.",
            "Indomitable (x1)": "At 9th level, you can reroll a saving throw that you fail, potentially avoiding the negative effects of a failed save.",
            "Extra Attack (x2)": "At 11th level, you gain a second extra attack, allowing you to make three attacks when taking the Attack action on your turn.",
            "Indomitable (x2)": "At 13th level, you gain an additional use of the Indomitable feature, increasing your resilience against failed saving throws.",
            "Action Surge (x2)": "At 17th level, you gain a second use of the Action Surge feature, allowing you to take two additional actions between rests.",
            "Indomitable (x3)": "At 17th level, you gain a third use of the Indomitable feature, further improving your ability to resist the effects of failed saves.",
            "Extra Attack (x3)": "At 20th level, you gain a third extra attack, allowing you to make four attacks when taking the Attack action on your turn."
        },
        "Hit Die": "1d10",
        "Proficiencies": {
            "Armor": "All armor, shields",
            "Weapons": "Simple weapons, martial weapons",
            "Tools": "None",
            "Spellcasting Modifier" : "None",
            "Saving Throws": ["Strength", "Constitution"],
            "Skills": {
                'Choose Number' : 2,
                'Choose From' : ['acrobatics', 'animal handling', 'athletics', 'history', 'insight', 'intimidation', 'perception', 'survival']
            },
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
            1: {'Proficiency Bonus': '+2','Martial Arts': '1d4','Ki Points': '–','Unarmored Movement': '–','Features': ['Unarmored Defense', 'Martial Arts']},
            2: {'Proficiency Bonus': '+2','Martial Arts': '1d4','Ki Points': '2','Unarmored Movement': '+10 ft.','Features': ['Ki', 'Unarmored Movement', 'Dedicated Weapon (Optional)']},
            3: {'Proficiency Bonus': '+2','Martial Arts': '1d4','Ki Points': '3','Unarmored Movement': '+10 ft.','Features': ['Monastic Tradition', 'Deflect Missiles', 'Ki-Fueled Attack (Optional)']},
            4: {'Proficiency Bonus': '+2','Martial Arts': '1d4','Ki Points': '4','Unarmored Movement': '+10 ft.','Features': ['Ability Score Improvement', 'Slow Fall', 'Quickened Healing (Optional)']},
            5: {'Proficiency Bonus': '+3','Martial Arts': '1d6','Ki Points': '5','Unarmored Movement': '+10 ft.','Features': ['Extra Attack', 'Stunning Strike', 'Focused Aim (Optional)']},
            6: {'Proficiency Bonus': '+3','Martial Arts': '1d6','Ki Points': '6','Unarmored Movement': '+15 ft.','Features': ['Ki-Empowered Strikes', 'Monastic Tradition Feature']},
            7: {'Proficiency Bonus': '+3','Martial Arts': '1d6','Ki Points': '7','Unarmored Movement': '+15 ft.','Features': ['Evasion', 'Stillness of Mind']},
            8: {'Proficiency Bonus': '+3','Martial Arts': '1d6','Ki Points': '8','Unarmored Movement': '+15 ft.','Features': ['Ability Score Improvement']},
            9: {'Proficiency Bonus': '+4','Martial Arts': '1d6','Ki Points': '9','Unarmored Movement': '+15 ft.','Features': ['Unarmored Movement improvement']},
            10: {'Proficiency Bonus': '+4','Martial Arts': '1d6','Ki Points': '10','Unarmored Movement': '+20 ft.','Features': ['Purity of Body']},
            11: {'Proficiency Bonus': '+4','Martial Arts': '1d8','Ki Points': '11','Unarmored Movement': '+20 ft.','Features': ['Monastic Tradition Feature']},
            12: {'Proficiency Bonus': '+4','Martial Arts': '1d8','Ki Points': '12','Unarmored Movement': '+20 ft.','Features': ['Ability Score Improvement']},
            13: {'Proficiency Bonus': '+5','Martial Arts': '1d8','Ki Points': '13','Unarmored Movement': '+20 ft.','Features': ['Tongue of the Sun and Moon']},
            14: {'Proficiency Bonus': '+5','Martial Arts': '1d8','Ki Points': '14','Unarmored Movement': '+25 ft.','Features': ['Diamond Soul']},
            15: {'Proficiency Bonus': '+5','Martial Arts': '1d8','Ki Points': '15','Unarmored Movement': '+25 ft.','Features': ['Timeless Body']},
            16: {'Proficiency Bonus': '+5','Martial Arts': '1d8','Ki Points': '16','Unarmored Movement': '+25 ft.','Features': ['Ability Score Improvement']},
            17: {'Proficiency Bonus': '+6','Martial Arts': '1d10','Ki Points': '17','Unarmored Movement': '+25 ft.','Features': ['Monastic Tradition Feature']},
            18: {'Proficiency Bonus': '+6','Martial Arts': '1d10','Ki Points': '18','Unarmored Movement': '+30 ft.','Features': ['Empty Body']},
            19: {'Proficiency Bonus': '+6','Martial Arts': '1d10','Ki Points': '19','Unarmored Movement': '+30 ft.','Features': ['Ability Score Improvement']},
            20: {'Proficiency Bonus': '+6','Martial Arts': '1d10','Ki Points': '20','Unarmored Movement': '+30 ft.','Features': ['Perfect Self']}
        },
        "Features": {
            "Unarmored Defense": "Starting at 1st level, while you are not wearing armor or using a shield, your AC equals 10 + "
                                "your Dexterity modifier + your Wisdom modifier. This reflects your ability to defend yourself "
                                "without the need for traditional armor.",
            "Martial Arts": "At 1st level, your martial training allows you to use unarmed strikes as a monk weapon, "
                            "and you can use Dexterity instead of Strength for the attack and damage rolls. Additionally, "
                            "your unarmed strike damage increases as you gain levels in this class.",
            "Ki Points": "Starting at 2nd level, you gain the ability to use ki points to fuel various features and abilities. "
                        "The number of ki points you have increases as you gain levels in this class.",
            "Monastic Tradition Feature": "The Monastic Tradition Feature is a key element of the monk class in the Dungeons and Dragons (D&D) 5th Edition role-playing game. "
                                          "It represents the monk's chosen path or school of martial arts and philosophy, shaping their unique abilities and combat style.",
            "Unarmored Movement": "At 2nd level, your speed increases, and it continues to increase as you gain levels in this class. "
                                "This reflects your agility and ability to move quickly even without heavy armor.",
            "Ki": "Starting at 2nd level, you gain access to ki features. These features include Flurry of Blows, Patient Defense, "
                "and Step of the Wind, which allow you to manipulate your ki energy for different effects in combat.",
            "Dedicated Weapon (Optional)": "At 2nd level, you can choose a specific type of monk weapon as your dedicated weapon. "
                                        "This choice enhances your proficiency with that weapon.",
            "Monastic Tradition": "At 3rd level, you choose a Monastic Tradition that reflects your specific style and philosophy as a monk. "
                                "This choice grants you additional features and abilities based on your chosen tradition.",
            "Deflect Missiles": "At 3rd level, you gain the ability to deflect or catch missiles and projectiles. "
                                "This allows you to reduce or negate ranged attacks against you.",
            "Ki-Fueled Attack (Optional)": "Starting at 3rd level, you can spend ki points to enhance your unarmed strikes with additional effects. "
                                        "This provides you with more versatility in combat.",
            "Ability Score Improvement": "At 4th level and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice "
                                        "by 2, or you can increase two ability scores of your choice by 1. This allows you to customize your character as you progress.",
            "Slow Fall": "At 4th level, you gain the ability to reduce falling damage, allowing you to safely land from great heights.",
            "Quickened Healing (Optional)": "Starting at 4th level, you can spend ki points to heal yourself or others, "
                                            "granting you a way to provide support and recovery in combat.",
            "Extra Attack": "At 5th level, you can make two unarmed strikes instead of one when you use the Attack action on your turn. "
                            "This increases your damage output in combat.",
            "Stunning Strike": "At 5th level, you gain the ability to stun a creature with your unarmed strikes, rendering them incapacitated. "
                            "This is a powerful crowd control ability.",
            "Focused Aim (Optional)": "Starting at 5th level, you can spend ki points to gain advantage on attack rolls, "
                                    "ensuring that your attacks are more likely to hit their target.",
            "Ki-Empowered Strikes": "At 6th level, your unarmed strikes are considered magical for the purpose of overcoming resistances and immunities.",
            "Evasion": "At 7th level, you gain the ability to avoid damage from area-effect spells and abilities with a successful Dexterity saving throw.",
            "Stillness of Mind": "At 7th level, you gain the ability to end an effect on yourself that is causing you to be charmed or frightened. "
                                "This reflects your mental discipline and inner calm.",
            "Unarmored Movement improvement": "At 9th level, your Unarmored Movement feature improves, allowing you to move more quickly and easily.",
            "Purity of Body": "At 10th level, you become immune to disease and poison, reflecting your physical and mental purity.",
            "Tongue of the Sun and Moon": "At 13th level, you can understand and speak any language, allowing you to communicate with almost anyone.",
            "Diamond Soul": "At 14th level, you gain proficiency in all saving throws, and you can spend ki points to reroll failed saving throws.",
            "Timeless Body": "At 15th level, you no longer age and are immune to the effects of aging. This reflects your attunement to the flow of time.",
            "Empty Body": "At 18th level, you gain the ability to become invisible and immune to damage, allowing you to escape danger or ambush foes.",
            "Perfect Self": "At 20th level, you achieve a state of perfect physical and mental being, gaining resistance to all damage types "
                            "and the ability to use your ki points without limit for certain features."
        },
        "Hit Die": "1d8",
        "Proficiencies": {
            "Armor": "None",
            "Weapons": "Simple weapons, shortswords",
            "Tools": "Choose one type of artisan's tools or one musical instrument",
            "Spellcasting Modifier" : "None",
            "Saving Throws": ["Strength", "Dexterity"],
            "Skills": {
                'Choose Number' : 2,
                'Choose From' : ['acrobatics', 'athletics', 'history', 'insight', 'religion', 'stealth']
            },
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
            1: {'Proficiency Bonus': '+2', 'Features': ['Divine Sense', 'Lay on Hands'], '1st': '-', '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            2: {'Proficiency Bonus': '+2', 'Features': ['Fighting Style', 'Spellcasting', 'Divine Smite'], '1st': '2', '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            3: {'Proficiency Bonus': '+2', 'Features': ['Divine Health', 'Sacred Oath', 'Harness Divine Power (Optional)'], '1st': '3', '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            4: {'Proficiency Bonus': '+2', 'Features': ['Ability Score Improvement', 'Martial Versatility (Optional)'], '1st': '3', '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            5: {'Proficiency Bonus': '+3', 'Features': ['Extra Attack'], '1st': '4', '2nd': '2', '3rd': '-', '4th': '-', '5th': '-'},
            6: {'Proficiency Bonus': '+3', 'Features': ['Aura of Protection'], '1st': '4', '2nd': '2', '3rd': '-', '4th': '-', '5th': '-'},
            7: {'Proficiency Bonus': '+3', 'Features': ['Sacred Oath feature'], '1st': '4', '2nd': '3', '3rd': '-', '4th': '-', '5th': '-'},
            8: {'Proficiency Bonus': '+3', 'Features': ['Ability Score Improvement', 'Martial Versatility (Optional)'], '1st': '4', '2nd': '3', '3rd': '-', '4th': '-', '5th': '-'},
            9: {'Proficiency Bonus': '+4', 'Features': ['-'], '1st': '4', '2nd': '3', '3rd': '2', '4th': '-', '5th': '-'},
            10: {'Proficiency Bonus': '+4', 'Features': ['Aura of Courage'], '1st': '4', '2nd': '3', '3rd': '2', '4th': '-', '5th': '-'},
            11: {'Proficiency Bonus': '+4', 'Features': ['Improved Divine Smite'], '1st': '4', '2nd': '3', '3rd': '3', '4th': '-', '5th': '-'},
            12: {'Proficiency Bonus': '+4', 'Features': ['Ability Score Improvement', 'Martial Versatility (Optional)'], '1st': '4', '2nd': '3', '3rd': '3', '4th': '-', '5th': '-'},
            13: {'Proficiency Bonus': '+5', 'Features': ['-'], '1st': '4', '2nd': '3', '3rd': '3', '4th': '1', '5th': '-'},
            14: {'Proficiency Bonus': '+5', 'Features': ['Cleansing Touch'], '1st': '4', '2nd': '3', '3rd': '3', '4th': '1', '5th': '-'},
            15: {'Proficiency Bonus': '+5', 'Features': ['Sacred Oath feature'], '1st': '4', '2nd': '3', '3rd': '3', '4th': '2', '5th': '-'},
            16: {'Proficiency Bonus': '+5', 'Features': ['Ability Score Improvement', 'Martial Versatility (Optional)'], '1st': '4', '2nd': '3', '3rd': '3', '4th': '2', '5th': '-'},
            17: {'Proficiency Bonus': '+6', 'Features': ['-'], '1st': '4', '2nd': '3', '3rd': '3', '4th': '3', '5th': '1'},
            18: {'Proficiency Bonus': '+6', 'Features': ['Aura improvements'], '1st': '4', '2nd': '3', '3rd': '3', '4th': '3', '5th': '1'},
            19: {'Proficiency Bonus': '+6', 'Features': ['Ability Score Improvement', 'Martial Versatility (Optional)'], '1st': '4', '2nd': '3', '3rd': '3', '4th': '3', '5th': '2'},
            20: {'Proficiency Bonus': '+6', 'Features': ['Sacred Oath feature'], '1st': '4', '2nd': '3', '3rd': '3', '4th': '3', '5th': '2'}
        },
        "Features" : {
            "Divine Sense": "At 1st level, you gain the ability to sense the presence of celestial, fiend, or undead creatures "
                            "within 60 feet of you. This allows you to detect the presence of such creatures, but it doesn't provide "
                            "specific information about their identity or location. You can use this feature a number of times equal "
                            "to 1 + your Charisma modifier before needing to complete a long rest.",
            "Lay on Hands": "Also at 1st level, you can use your Paladin's Touch to heal wounds. As an action, you can touch a creature "
                            "and restore hit points equal to your Paladin level x 5. You have a pool of healing power, and this pool "
                            "refreshes after a long rest.",
            "Fighting Style": "At 2nd level, you adopt a particular style of fighting as your specialty. "
                            "This choice grants you a feature to enhance your combat abilities, such as Dueling for increased damage or "
                            "Protection to aid in defense.",
            "Spellcasting": "Also at 2nd level, you gain the ability to cast spells as a Paladin. You prepare and cast spells "
                            "from the Paladin spell list, using your Charisma as your spellcasting ability. This feature allows you to "
                            "smite enemies with divine power and provide support to your allies through spells.",
            "Divine Smite": "Starting at 2nd level, when you hit a creature with a melee weapon attack, you can expend one spell slot "
                            "to deal radiant damage to the target in addition to the weapon's damage. The extra damage increases as you "
                            "gain higher-level spell slots.",
            "Divine Health": "At 3rd level, your divine magic makes you immune to disease. You are now not only a warrior but also a beacon "
                            "of health and vitality.",
            "Sacred Oath": "Also at 3rd level, you swear an oath to uphold certain principles and ideals. This choice determines your Paladin "
                        "Oath, granting you additional features and abilities based on your chosen oath.",
            "Harness Divine Power (Optional)": "At 3rd level, you gain the ability to channel your divine energy to fuel certain class features. "
                                                "This optional feature allows you to regain expended spell slots through prayer.",
            "Ability Score Improvement": "At 4th level and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice "
                                        "by 2, or you can increase two ability scores of your choice by 1. This allows you to customize your character as you progress.",
            "Martial Versatility (Optional)": "At 4th level, you can replace a fighting style you previously chose with another one. "
                                            "This option grants you greater flexibility in adapting your combat style to different situations.",
            "Extra Attack": "Starting at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. "
                            "This feature significantly enhances your combat capabilities.",
            "Aura of Protection": "At 6th level, you and friendly creatures within 10 feet of you gain a bonus to saving throws equal to your "
                                "Charisma modifier. This aura enhances your allies' resilience to various threats.",
            "Sacred Oath feature": "At 7th level and again at 15th and 20th level, your chosen Sacred Oath grants you additional features and abilities "
                                "that reflect your oath's tenets and purpose.",
            "Aura of Courage": "At 10th level, you and friendly creatures within 10 feet of you can't be frightened while you are conscious. "
                            "This aura instills bravery and determination in your allies.",
            "Improved Divine Smite": "Starting at 11th level, your Divine Smite feature now adds extra damage to your weapon attacks even without "
                                    "expending spell slots. Your attacks carry an increased divine impact.",
            "Cleansing Touch": "At 14th level, you gain the ability to cure disease or end a condition afflicting a creature. "
                            "Your touch can purify and heal, providing aid to your allies in need.",
            "Aura improvements": "At 18th level, the range of your Aura of Protection and Aura of Courage increases, benefiting more allies "
                                "with your protective auras.",
        },
        "Hit Die": "1d10",
        "Proficiencies": {
            "Armor": "All armor, shields",
            "Weapons": ["simple weapons", "martial weapons"],
            "Tools": "None",
            "Spellcasting Modifier" : "Charisma",
            "Saving Throws": ["Wisdom", "Charisma"],
            "Skills": {
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
            1: {'Proficiency Bonus': '+2', 'Features': ['Favored Enemy', 'Natural Explorer', 'Deft Explorer (Optional)', 'Favored Foe (Optional)'], 'Spells Known': '-', '1st': '-', '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            2: {'Proficiency Bonus': '+2', 'Features': ['Fighting Style', 'Spellcasting', 'Spellcasting Focus (Optional)'], 'Spells Known': 2, '1st': 2, '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            3: {'Proficiency Bonus': '+2', 'Features': ['Primeval Awareness', 'Ranger Conclave', 'Primal Awareness (Optional)'], 'Spells Known': 3, '1st': 3, '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            4: {'Proficiency Bonus': '+2', 'Features': ['Ability Score Improvement', 'Martial Versatility (Optional)'], 'Spells Known': 3, '1st': 3, '2nd': '-', '3rd': '-', '4th': '-', '5th': '-'},
            5: {'Proficiency Bonus': '+3', 'Features': ['Extra Attack'], 'Spells Known': 4, '1st': 4, '2nd': 2, '3rd': '-', '4th': '-', '5th': '-'},
            6: {'Proficiency Bonus': '+3', 'Features': ['Favored Enemy Improvement', 'Natural Explorer Improvement', 'Deft Explorer Improvement (Optional)'], 'Spells Known': 4, '1st': 4, '2nd': 2, '3rd': '-', '4th': '-', '5th': '-'},
            7: {'Proficiency Bonus': '+3', 'Features': ['Ranger Conclave feature'], 'Spells Known': 5, '1st': 4, '2nd': 3, '3rd': '-', '4th': '-', '5th': '-'},
            8: {'Proficiency Bonus': '+3', 'Features': ['Ability Score Improvement', "Land's Stride", 'Martial Versatility (Optional)'], 'Spells Known': 5, '1st': 4, '2nd': 3, '3rd': '-', '4th': '-', '5th': '-'},
            9: {'Proficiency Bonus': '+4', 'Features': ['-'], 'Spells Known': 6, '1st': 4, '2nd': 3, '3rd': 2, '4th': '-', '5th': '-'},
            10: {'Proficiency Bonus': '+4', 'Features': ["Natural Explorer Improvement", "Hide in Plain Sight", "Deft Explorer Feature (Optional)", "Nature's Veil (Optional)"], 'Spells Known': 6, '1st': 4, '2nd': 3, '3rd': 2, '4th': '-', '5th': '-'},
            11: {'Proficiency Bonus': '+4', 'Features': ['Ranger Conclave feature'], 'Spells Known': 7, '1st': 4, '2nd': 3, '3rd': 3, '4th': '-', '5th': '-'},
            12: {'Proficiency Bonus': '+4', 'Features': ['Ability Score Improvement', 'Martial Versatility (Optional)'], 'Spells Known': 7, '1st': 4, '2nd': 3, '3rd': 3, '4th': '-', '5th': '-'},
            13: {'Proficiency Bonus': '+5', 'Features': ['-'], 'Spells Known': 8, '1st': 4, '2nd': 3, '3rd': 3, '4th': 1, '5th': '-'},
            14: {'Proficiency Bonus': '+5', 'Features': ['Favored Enemy Improvement', 'Vanish'], 'Spells Known': 8, '1st': 4, '2nd': 3, '3rd': 3, '4th': 1, '5th': '-'},
            15: {'Proficiency Bonus': '+5', 'Features': ['Ranger Conclave feature'], 'Spells Known': 9, '1st': 4, '2nd': 3, '3rd': 3, '4th': 2, '5th': '-'},
            16: {'Proficiency Bonus': '+5', 'Features': ['Ability Score Improvement', 'Martial Versatility (Optional)'], 'Spells Known': 9, '1st': 4, '2nd': 3, '3rd': 3, '4th': 2, '5th': '-'},
            17: {'Proficiency Bonus': '+6', 'Features': ['-'], 'Spells Known': 10, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 1},
            18: {'Proficiency Bonus': '+6', 'Features': ['Feral Senses'], 'Spells Known': 10, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 1},
            19: {'Proficiency Bonus': '+6', 'Features': ['Ability Score Improvement', 'Martial Versatility (Optional)'], 'Spells Known': 11, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2},
            20: {'Proficiency Bonus': '+6', 'Features': ['Foe Slayer'], 'Spells Known': 11, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2}
        },
        "Features": {
            "Favored Enemy": "At 1st level, you choose a type of creature to be your favored enemy. You gain bonuses when tracking, "
                            "hunting, and interacting with creatures of this type. You can choose additional favored enemies as you level up.",
            "Natural Explorer": "Also at 1st level, you gain benefits when traveling through specific types of terrain. You become skilled at "
                                "navigating the wilderness and avoiding hazards associated with your favored terrain.",
            "Deft Explorer (Optional)": "At 1st level, you gain one of three features (Canny, Roving, or Tireless) that enhance your "
                                        "abilities based on your preferred exploration style. You can choose an additional feature at later levels.",
            "Favored Foe (Optional)": "At 1st level, you can mark a creature as your favored foe. You gain bonus damage against this target, "
                                    "and you can designate a new favored foe after a short or long rest.",
            "Fighting Style": "At 2nd level, you choose a fighting style that defines your combat preferences. Options include Archery, "
                            "Two-Weapon Fighting, and more, each granting specific combat benefits.",
            "Spellcasting": "Also at 2nd level, you gain the ability to cast spells as a Ranger. You prepare and cast spells from the Ranger "
                            "spell list, using your Wisdom as your spellcasting ability.",
            "Spellcasting Focus (Optional)": "At 2nd level, you can use a druidic focus as a spellcasting focus for your Ranger spells. "
                                            "This is an optional feature for added flavor.",
            "Primeval Awareness": "At 3rd level, you gain the ability to use your awareness to detect nearby creatures. This helps you sense "
                                "the presence of certain types of creatures within 1 mile of you.",
            "Ranger Conclave": "Also at 3rd level, you choose a Ranger Conclave that represents your specialization, such as Hunter or Beast Master. "
                            "This choice grants you unique features based on your selected Conclave.",
            "Primal Awareness (Optional)": "At 3rd level, you can expend spell slots to gain the ability to cast additional spells, such as "
                                        "Detect Magic or Speak with Animals, without preparing them in advance. This is an optional feature.",
            "Ability Score Improvement": "At 4th level and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice "
                                        "by 2, or you can increase two ability scores of your choice by 1. This allows you to customize your character as you progress.",
            "Martial Versatility (Optional)": "At 4th level, you can replace a favored enemy or favored foe with another one. This option grants you greater "
                                            "flexibility in adapting your specialization to different situations.",
            "Extra Attack": "Starting at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn. "
                            "This feature significantly enhances your combat capabilities.",
            "Favored Enemy Improvement": "At 6th level, your expertise in dealing with your favored enemy improves. You gain additional bonuses when "
                                        "interacting with them.",
            "Natural Explorer Improvement": "At 6th level, your Natural Explorer feature is enhanced, granting you further advantages when traveling "
                                        "through your favored terrain.",
            "Deft Explorer Improvement (Optional)": "At 6th level, you can choose another feature to improve your exploration skills further. "
                                                    "This is an optional feature.",
            "Ranger Conclave feature": "At 7th level and again at 11th and 15th level, your chosen Ranger Conclave grants you additional features "
                                    "and abilities that reflect your specialization within the Ranger class.",
            "Land's Stride": "At 8th level, moving through non-magical difficult terrain doesn't cost you extra movement, and you can't be "
                            "tracked by non-magical means unless you choose to leave tracks.",
            "Hide in Plain Sight": "At 10th level, you can blend into your surroundings while lightly obscured by natural phenomena, "
                                    "making you exceptionally stealthy.",
            "Nature's Veil (Optional)": "At 10th level, you can use magic to conceal yourself or allies from view, enhancing your ability to "
                                        "ambush or hide. This is an optional feature.",
            "Vanish": "At 14th level, you can disappear from view as a bonus action, gaining improved stealth and the ability to hide more easily.",
            "Feral Senses": "At 18th level, your senses become incredibly sharp. You gain advantage on Wisdom (Perception) checks, and you can "
                            "sense the presence of invisible creatures within 30 feet of you.",
            "Foe Slayer": "At 20th level, you become a master of hunting. You can add your Wisdom modifier to the attack and damage rolls against "
                        "your favored enemies, making you a formidable adversary."

        },
        "Hit Die": '1d10',
        "Proficiencies": {
            'Armor': 'Light armor, medium armor, shields',
            'Weapons': 'Simple weapons, martial weapons',
            'Tools': 'None',
            "Spellcasting Modifier" : "Widsom",
            'Saving Throws': ['Strength', 'Dexterity'],
            "Skills": {
                'Choose Number' : 3,
                'Choose From' :  ['animal handling', 'athletics', 'insight', 'investigation', 'nature', 'perception', 'stealth', 'survival']
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
                "4th" : ["Conjure Woodland Beings","Freedom of Movement","Grasping Vine","Guardian of Nature","Locate Creature","Stoneskin"],
                "5th" : ["Commune with Nature","Conjure Volley","Steel Wind Strike","Swift Quiver","Tree Stride","Wrath of Nature"]           
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
            1: {'Proficiency Bonus': '+2', 'Sneak Attack': '1d6', 'Features': ['Expertise', 'Sneak Attack', "Thieves' Cant"]},
            2: {'Proficiency Bonus': '+2', 'Sneak Attack': '1d6', 'Features': ['Cunning Action']},
            3: {'Proficiency Bonus': '+2', 'Sneak Attack': '2d6', 'Features': ['Roguish Archetype', 'Steady Aim (Optional)']},
            4: {'Proficiency Bonus': '+2', 'Sneak Attack': '2d6', 'Features': ['Ability Score Improvement']},
            5: {'Proficiency Bonus': '+3', 'Sneak Attack': '3d6', 'Features': ['Uncanny Dodge']},
            6: {'Proficiency Bonus': '+3', 'Sneak Attack': '3d6', 'Features': ['Expertise']},
            7: {'Proficiency Bonus': '+3', 'Sneak Attack': '4d6', 'Features': ['Evasion']},
            8: {'Proficiency Bonus': '+3', 'Sneak Attack': '4d6', 'Features': ['Ability Score Improvement']},
            9: {'Proficiency Bonus': '+4', 'Sneak Attack': '5d6', 'Features': ['Roguish Archetype feature']},
            10: {'Proficiency Bonus': '+4', 'Sneak Attack': '5d6', 'Features': ['Ability Score Improvement']},
            11: {'Proficiency Bonus': '+4', 'Sneak Attack': '6d6', 'Features': ['Reliable Talent']},
            12: {'Proficiency Bonus': '+4', 'Sneak Attack': '6d6', 'Features': ['Ability Score Improvement']},
            13: {'Proficiency Bonus': '+5', 'Sneak Attack': '7d6', 'Features': ['Roguish Archetype feature']},
            14: {'Proficiency Bonus': '+5', 'Sneak Attack': '7d6', 'Features': ['Blindsense']},
            15: {'Proficiency Bonus': '+5', 'Sneak Attack': '8d6', 'Features': ['Slippery Mind']},
            16: {'Proficiency Bonus': '+5', 'Sneak Attack': '8d6', 'Features': ['Ability Score Improvement']},
            17: {'Proficiency Bonus': '+6', 'Sneak Attack': '9d6', 'Features': ['Roguish Archetype feature']},
            18: {'Proficiency Bonus': '+6', 'Sneak Attack': '9d6', 'Features': ['Elusive']},
            19: {'Proficiency Bonus': '+6', 'Sneak Attack': '10d6', 'Features': ['Ability Score Improvement']},
            20: {'Proficiency Bonus': '+6', 'Sneak Attack': '10d6', 'Features': ['Stroke of Luck']}
        },
        "Features": {
            "Expertise": "At 1st level, you gain proficiency in two of your choice of skills, tools, or languages. Your proficiency bonus "
                        "is doubled for any ability check you make using these chosen proficiencies. This feature is gained again at 6th level.",
            "Sneak Attack": "At 1st level, you can deal extra damage to creatures you hit with an attack if you have advantage on the attack roll, "
                            "or if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage "
                            "on the attack roll. The extra damage increases as you level up.",
            "Thieves' Cant": "At 1st level, you learn the secret language of thieves. You can communicate in a hidden manner with other rogues "
                            "who know this language.",
            "Cunning Action": "At 2nd level, you can take a bonus action on each of your turns in combat to Dash, Disengage, or Hide, allowing you to "
                            "be more agile and elusive in combat.",
            "Roguish Archetype": "At 3rd level, you choose a Roguish Archetype that defines your specialization as a rogue, such as Thief or Assassin. "
                                "This choice grants you unique features based on your selected archetype.",
            "Steady Aim (Optional)": "At 3rd level, you can use your bonus action to carefully aim your ranged weapon, giving you advantage on your next "
                                    "attack roll with it. This is an optional feature.",
            "Ability Score Improvement": "At 4th level and again at 8th, 10th, 12th, 16th, and 19th level, you can increase one ability score of your choice "
                                        "by 2, or you can increase two ability scores of your choice by 1. This allows you to customize your character as you progress.",
            "Uncanny Dodge": "At 5th level, you can use your reaction to halve the damage from an incoming attack that you can see, as long as you're wielding "
                            "a finesse weapon or a ranged weapon.",
            "Evasion": "At 7th level, you can nimbly dodge out of the way of certain area effects, such as a red dragon's fiery breath or an ice storm spell, "
                    "taking no damage on a successful Dexterity saving throw.",
            "Roguish Archetype feature": "At 9th, 13th, and 17th level, your chosen Roguish Archetype grants you additional features and abilities that reflect "
                                        "your specialization within the rogue class.",
            "Reliable Talent": "At 11th level, you can add your proficiency bonus to any ability check you make that uses one of your skill proficiencies, "
                            "ensuring that you are incredibly skilled in those areas.",
            "Blindsense": "At 14th level, you gain the ability to detect the presence of creatures even if they are invisible or heavily obscured, "
                        "as long as they are within 10 feet of you.",
            "Slippery Mind": "At 15th level, you have acquired mental resilience, allowing you to use your action to end an effect on yourself that is causing "
                            "you to be charmed or frightened, helping you break free from such conditions.",
            "Elusive": "At 18th level, you become exceptionally difficult to pin down during combat. Attackers have disadvantage on attack rolls against you, "
                    "and you can use your action to make yourself effectively invisible for a turn.",
            "Stroke of Luck": "At 20th level, you have an uncanny ability to avoid failure. If your attack misses a target or a saving throw fails, you can "
                            "use Stroke of Luck to turn the failure into a success, potentially saving the day."

        },
        "Hit Die": '1d8',
        "Proficiencies": {
            'Armor': 'Light armor',
            'Weapons': 'Simple weapons, hand crossbows, longswords, rapiers, shortswords',
            'Tools': 'Thieves\' tools',
            "Spellcasting Modifier" : "None",
            'Saving Throws': ['Dexterity', 'Intelligence'],
            "Skills": {
                'Choose Number' : 4,
                'Choose From' :  ['acrobatics', 'athletics', 'deception', 'insight', 'intimidation', 'investigation', 'perception', 'performance', 'persuasion', 'sleight of hand', 'stealth']
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
            1: {'Proficiency Bonus': '+2', 'Sorcery Points': '-', 'Features': ['Spellcasting', 'Sorcerous Origin'], 'Cantrips Known': 4, 'Spells Known': 2, '1st': 2, '2nd': '-', '3rd': '-', '4th': '-', '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            2: {'Proficiency Bonus': '+2', 'Sorcery Points': '2', 'Features': ['Font of Magic'], 'Cantrips Known': 4, 'Spells Known': 3, '1st': 3, '2nd': '-', '3rd': '-', '4th': '-', '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            3: {'Proficiency Bonus': '+2', 'Sorcery Points': '3', 'Features': ['Metamagic'], 'Cantrips Known': 4, 'Spells Known': 4, '1st': 4, '2nd': 2, '3rd': '-', '4th': '-', '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            4: {'Proficiency Bonus': '+2', 'Sorcery Points': '4', 'Features': ['Ability Score Improvement', 'Sorcerous Versatility (Optional)'], 'Cantrips Known': 5, 'Spells Known': 5, '1st': 4, '2nd': 3, '3rd': '-', '4th': '-', '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            5: {'Proficiency Bonus': '+3', 'Sorcery Points': '5', 'Features': ['Magical Guidance (Optional)'], 'Cantrips Known': 5, 'Spells Known': 6, '1st': 4, '2nd': 3, '3rd': 2, '4th': '-', '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            6: {'Proficiency Bonus': '+3', 'Sorcery Points': '6', 'Features': ['Sorcerous Origin feature'], 'Cantrips Known': 5, 'Spells Known': 7, '1st': 4, '2nd': 3, '3rd': 3, '4th': '-', '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            7: {'Proficiency Bonus': '+3', 'Sorcery Points': '7', 'Features': ['-'], 'Cantrips Known': 5, 'Spells Known': 8, '1st': 4, '2nd': 3, '3rd': 3, '4th': 1, '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            8: {'Proficiency Bonus': '+3', 'Sorcery Points': '8', 'Features': ['Ability Score Improvement', 'Sorcerous Versatility (Optional)'], 'Cantrips Known': 5, 'Spells Known': 9, '1st': 4, '2nd': 3, '3rd': 3, '4th': 2, '5th': '-', '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            9: {'Proficiency Bonus': '+4', 'Sorcery Points': '9', 'Features': ['-'], 'Cantrips Known': 5, 'Spells Known': 10, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 1, '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            10: {'Proficiency Bonus': '+4', 'Sorcery Points': '10', 'Features': ['Metamagic'], 'Cantrips Known': 6, 'Spells Known': 11, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': '-', '7th': '-', '8th': '-', '9th': '-'},
            11: {'Proficiency Bonus': '+4', 'Sorcery Points': '11', 'Features': ['-'], 'Cantrips Known': 6, 'Spells Known': 12, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': '-', '8th': '-', '9th': '-'},
            12: {'Proficiency Bonus': '+4', 'Sorcery Points': '12', 'Features': ['Ability Score Improvement', 'Sorcerous Versatility (Optional)'], 'Cantrips Known': 6, 'Spells Known': 12, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': '-', '8th': '-', '9th': '-'},
            13: {'Proficiency Bonus': '+5', 'Sorcery Points': '13', 'Features': ['-'], 'Cantrips Known': 6, 'Spells Known': 13, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': '-', '9th': '-'},
            14: {'Proficiency Bonus': '+5', 'Sorcery Points': '14', 'Features': ['Sorcerous Origin feature'], 'Cantrips Known': 6, 'Spells Known': 13, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': '-', '9th': '-'},
            15: {'Proficiency Bonus': '+5', 'Sorcery Points': '15', 'Features': ['-'], 'Cantrips Known': 6, 'Spells Known': 14, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': '-'},
            16: {'Proficiency Bonus': '+5', 'Sorcery Points': '16', 'Features': ['Ability Score Improvement', 'Sorcerous Versatility (Optional)'], 'Cantrips Known': 6, 'Spells Known': 14, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': '-'},
            17: {'Proficiency Bonus': '+6', 'Sorcery Points': '17', 'Features': ['Metamagic'], 'Cantrips Known': 6, 'Spells Known': 15, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': 1},
            18: {'Proficiency Bonus': '+6', 'Sorcery Points': '18', 'Features': ['Sorcerous Origin feature'], 'Cantrips Known': 6, 'Spells Known': 15, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': 1},
            19: {'Proficiency Bonus': '+6', 'Sorcery Points': '19', 'Features': ['Ability Score Improvement', 'Sorcerous Versatility (Optional)'], 'Cantrips Known': 6, 'Spells Known': 15, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': 1},
            20: {'Proficiency Bonus': '+6', 'Sorcery Points': '20', 'Features': ['Sorcerous Restoration'], 'Cantrips Known': 6, 'Spells Known': 15, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': 1}
        },
        "Features": {
            "Spellcasting": "At 1st level, you gain the ability to cast spells using your innate magical ability, known as Sorcery Points. "
                            "You can choose spells from the sorcerer spell list and cast them using spell slots.",
            "Sorcerous Origin": "At 1st level, you choose a Sorcerous Origin, which represents the source of your innate magical power. "
                                "Different origins grant you unique abilities and features.",
            "Font of Magic": "At 2nd level, you gain the ability to manipulate your Sorcery Points. You can use Sorcery Points to create spell slots "
                            "or convert unused spell slots into Sorcery Points.",
            "Metamagic": "At 3rd level, you gain access to Metamagic options, which allow you to modify your spells in various ways. You can choose "
                        "Metamagic options as you level up.",
            "Ability Score Improvement": "At 4th level and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice "
                                        "by 2, or you can increase two ability scores of your choice by 1. This allows you to customize your character as you progress.",
            "Sorcerous Versatility (Optional)": "At 4th level, you can choose to gain proficiency with a new set of tools or a new language instead of "
                                                "increasing your ability scores. This is an optional feature.",
            "Magical Guidance (Optional)": "At 5th level, you can choose to gain proficiency in a skill or a set of tools instead of increasing your ability scores. "
                                        "This is an optional feature.",
            "Sorcerous Origin feature": "At 6th, 14th, and 18th level, your chosen Sorcerous Origin grants you additional features and abilities that reflect "
                                        "your magical heritage.",
            "Sorcerous Restoration": "At 20th level, you regain expended Sorcery Points when you finish a short rest, giving you more versatility in "
                                    "managing your magical resources."
        },
        "Hit Die": '1d6',
        "Proficiencies": {
            'Armor': 'None',
            'Weapons': 'Daggers, darts, slings, quarterstaffs, light crossbows',
            'Tools': 'None',
            "Spellcasting Modifier" : "Charisma",
            'Saving Throws': ['Constitution', 'Charisma'],
            "Skills": {
                'Choose Number' : 2,
                'Choose From' :  ['arcana', 'deception', 'insight', 'intimidation', 'persuasion', 'religion']
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
                "7th" : ["Crown of Stars","Delayed Blast Fireball","Draconic Transformation","Etherealness","Finger of Death","Fire Storm","Plane Shift","Power Word - Pain","Prismatic Spray","Reverse Gravity","Teleport"],
                "8th" : ["Abi-Dalzim's Horrid Wilting","Dominate Monster","Earthquake","Incendiary Cloud","Power Word - Stun","Sunburst"],
                "9th" : ["Blade of Disaster","Gate","Mass Polymorph","Meteor Swarm","Power Word - Kill","Psychic Scream","Time Stop","Wish"]
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
            1: {'Proficiency Bonus': '+2', 'Features': ['Otherworldly Patron', 'Pact Magic'], 'Cantrips Known': 2, 'Spells Known': 2, 'Spell Slots': 1, 'Slot Level': '1st', 'Invocations Known': '-'},
            2: {'Proficiency Bonus': '+2', 'Features': ['Eldritch Invocations'], 'Cantrips Known': 2, 'Spells Known': 3, 'Spell Slots': 2, 'Slot Level': '1st', 'Invocations Known': '2'},
            3: {'Proficiency Bonus': '+2', 'Features': ['Pact Boon'], 'Cantrips Known': 2, 'Spells Known': 4, 'Spell Slots': 2, 'Slot Level': '2nd', 'Invocations Known': '2'},
            4: {'Proficiency Bonus': '+2', 'Features': ['Ability Score Improvement', 'Eldritch Versatility (Optional)'], 'Cantrips Known': 3, 'Spells Known': 5, 'Spell Slots': 2, 'Slot Level': '2nd', 'Invocations Known': '2'},
            5: {'Proficiency Bonus': '+3', 'Features': ['-'], 'Cantrips Known': 3, 'Spells Known': 6, 'Spell Slots': 2, 'Slot Level': '3rd', 'Invocations Known': '3'},
            6: {'Proficiency Bonus': '+3', 'Features': ['Otherworldly Patron Feature'], 'Cantrips Known': 3, 'Spells Known': 7, 'Spell Slots': 2, 'Slot Level': '3rd', 'Invocations Known': '3'},
            7: {'Proficiency Bonus': '+3', 'Features': ['-'], 'Cantrips Known': 3, 'Spells Known': 8, 'Spell Slots': 2, 'Slot Level': '4th', 'Invocations Known': '4'},
            8: {'Proficiency Bonus': '+3', 'Features': ['Ability Score Improvement', 'Eldritch Versatility (Optional)'], 'Cantrips Known': 3, 'Spells Known': 9, 'Spell Slots': 2, 'Slot Level': '4th', 'Invocations Known': '4'},
            9: {'Proficiency Bonus': '+4', 'Features': ['-'], 'Cantrips Known': 3, 'Spells Known': 10, 'Spell Slots': 2, 'Slot Level': '5th', 'Invocations Known': '5'},
            10: {'Proficiency Bonus': '+4', 'Features': ['Otherworldly Patron Feature'], 'Cantrips Known': 4, 'Spells Known': 10, 'Spell Slots': 2, 'Slot Level': '5th', 'Invocations Known': '5'},
            11: {'Proficiency Bonus': '+4', 'Features': ['Mystic Arcanum (6th level)'], 'Cantrips Known': 4, 'Spells Known': 11, 'Spell Slots': 3, 'Slot Level': '5th', 'Invocations Known': '5'},
            12: {'Proficiency Bonus': '+4', 'Features': ['Ability Score Improvement', 'Eldritch Versatility (Optional)'], 'Cantrips Known': 4, 'Spells Known': 11, 'Spell Slots': 3, 'Slot Level': '5th', 'Invocations Known': '6'},
            13: {'Proficiency Bonus': '+5', 'Features': ['Mystic Arcanum (7th level)'], 'Cantrips Known': 4, 'Spells Known': 12, 'Spell Slots': 3, 'Slot Level': '5th', 'Invocations Known': '6'},
            14: {'Proficiency Bonus': '+5', 'Features': ['Otherworldly Patron Feature'], 'Cantrips Known': 4, 'Spells Known': 12, 'Spell Slots': 3, 'Slot Level': '5th', 'Invocations Known': '6'},
            15: {'Proficiency Bonus': '+5', 'Features': ['Mystic Arcanum (8th level)'], 'Cantrips Known': 4, 'Spells Known': 13, 'Spell Slots': 3, 'Slot Level': '5th', 'Invocations Known': '7'},
            16: {'Proficiency Bonus': '+5', 'Features': ['Ability Score Improvement', 'Eldritch Versatility (Optional)'], 'Cantrips Known': 4, 'Spells Known': 13, 'Spell Slots': 3, 'Slot Level': '5th', 'Invocations Known': '7'},
            17: {'Proficiency Bonus': '+6', 'Features': ['Mystic Arcanum (9th level)'], 'Cantrips Known': 4, 'Spells Known': 14, 'Spell Slots': 4, 'Slot Level': '5th', 'Invocations Known': '7'},
            18: {'Proficiency Bonus': '+6', 'Features': ['-'], 'Cantrips Known': 4, 'Spells Known': 14, 'Spell Slots': 4, 'Slot Level': '5th', 'Invocations Known': '8'},
            19: {'Proficiency Bonus': '+6', 'Features': ['Ability Score Improvement', 'Eldritch Versatility (Optional)'], 'Cantrips Known': 4, 'Spells Known': 15, 'Spell Slots': 4, 'Slot Level': '5th', 'Invocations Known': '8'},
            20: {'Proficiency Bonus': '+6', 'Features': ['Eldritch Master'], 'Cantrips Known': 4, 'Spells Known': 15, 'Spell Slots': 4, 'Slot Level': '5th', 'Invocations Known': '8'}
        },
        "Features": {
            "Otherworldly Patron": "At 1st level, you choose an Otherworldly Patron, a powerful being that grants you warlock powers. "
                                "This choice determines your Patron's features and spells you can cast.",
            "Otherworldly Patron Feature": "The Otherworldly Patron Feature is a key element of the warlock class in the Dungeons and Dragons (D&D) 5th Edition role-playing game. "
                                           "It represents the warlock's pact with a powerful otherworldly being, granting them special abilities, spells, and a unique connection to their patron. "
                                           "This choice of patron significantly influences the warlock's character and abilities.",
            "Pact Magic": "At 1st level, you gain the ability to cast spells through a mystical connection to your Patron. You have a limited number "
                        "of spell slots, and your spells are always cast at their highest possible level.",
            "Eldritch Invocations": "At 2nd level, you gain the ability to choose Eldritch Invocations, which grant you unique abilities and enhancements. "
                                    "You can select two Eldritch Invocations at this level.",
            "Pact Boon": "At 3rd level, you receive a special gift from your Patron known as a Pact Boon. There are three types of Pact Boons: Pact of the Chain, "
                        "Pact of the Blade, and Pact of the Tome. Each provides different benefits.",
            "Ability Score Improvement": "At 4th level and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, "
                                        "or you can increase two ability scores of your choice by 1. This allows you to customize your character as you progress.",
            "Eldritch Versatility (Optional)": "At 4th level, you can choose to gain proficiency in a new set of tools or a new language instead of "
                                                "increasing your ability scores. This is an optional feature.",
            "Mystic Arcanum (6th level)": "At 11th level, you gain access to a special spell known as a Mystic Arcanum. This spell is of 6th-level and can "
                                        "be cast once without expending a spell slot.",
            "Mystic Arcanum (7th level)": "At 13th level, you gain access to a 7th-level Mystic Arcanum spell, which can be cast once without expending a spell slot.",
            "Mystic Arcanum (8th level)": "At 15th level, you gain access to an 8th-level Mystic Arcanum spell, which can be cast once without expending a spell slot.",
            "Mystic Arcanum (9th level)": "At 17th level, you gain access to a 9th-level Mystic Arcanum spell, which can be cast once without expending a spell slot.",
            "Eldritch Master": "At 20th level, you can spend 1 minute to regain all expended spell slots once per day when you finish a short rest."

        },
        "Hit Die": '1d8',
        "Proficiencies": {
            'Armor': 'Light armor',
            'Weapons': 'Simple weapons',
            'Tools': 'None',
            "Spellcasting Modifier" : "Charisma",
            'Saving Throws': ['Wisdom', 'Charisma'],
            "Skills": {
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
                "3rd" : ["Antagonize","Counterspell","Dispel Magic","Enemies Abound","Fear","Fly","Gaseous Form","Hunger of Hadar","Hypnotic Pattern","Incite Greed","Magic Circle","Major Image","Remove Curse","Summon Lesser Demons","Thunder Step","Tongues","Vampiric Touch"],
                "4th" : ["Banishment","Blight","Charm Monster","Dimension Door","Elemental Bane","Galder's Speedy Courier","Gate Seal","Hallucinatory Terrain","Raulothim's Psychic Lance","Shadow of Moil","Sickening Radiance","Spirit Of Death"],
                "5th" : ["Contact Other Plane","Danse Macabre","Dream","Enervation","Far Step","Hold Monster","Infernal Calling","Negative Energy Flood","Scrying","Synaptic Static","Wall of Light"],
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
            1: {'Proficiency Bonus': '+2', 'Features': ['Spellcasting', 'Arcane Recovery'], 'Cantrips Known': 3, '1st': 2},
            2: {'Proficiency Bonus': '+2', 'Features': ['Arcane Tradition'], 'Cantrips Known': 3, '1st': 3},
            3: {'Proficiency Bonus': '+2', 'Features': ['Cantrip Formulas (Optional)'], 'Cantrips Known': 3, '1st': 4, '2nd': 2},
            4: {'Proficiency Bonus': '+2', 'Features': ['Ability Score Improvement'], 'Cantrips Known': 4, '1st': 4, '2nd': 3},
            5: {'Proficiency Bonus': '+3', 'Features': ['-'], 'Cantrips Known': 4, '1st': 4, '2nd': 3, '3rd': 2},
            6: {'Proficiency Bonus': '+3', 'Features': ['Arcane Tradition feature'], 'Cantrips Known': 4, '1st': 4, '2nd': 3, '3rd': 3},
            7: {'Proficiency Bonus': '+3', 'Features': ['-'], 'Cantrips Known': 4, '1st': 4, '2nd': 3, '3rd': 3, '4th': 1},
            8: {'Proficiency Bonus': '+3', 'Features': ['Ability Score Improvement'], 'Cantrips Known': 4, '1st': 4, '2nd': 3, '3rd': 3, '4th': 2},
            9: {'Proficiency Bonus': '+4', 'Features': ['-'], 'Cantrips Known': 4, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 1},
            10: {'Proficiency Bonus': '+4', 'Features': ['Arcane Tradition feature'], 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2},
            11: {'Proficiency Bonus': '+4', 'Features': ['-'], 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1},
            12: {'Proficiency Bonus': '+4', 'Features': ['Ability Score Improvement'], 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1},
            13: {'Proficiency Bonus': '+5', 'Features': ['-'], 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1},
            14: {'Proficiency Bonus': '+5', 'Features': ['Arcane Tradition feature'], 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1},
            15: {'Proficiency Bonus': '+5', 'Features': ['-'], 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1},
            16: {'Proficiency Bonus': '+5', 'Features': ['Ability Score Improvement'], 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1},
            17: {'Proficiency Bonus': '+6', 'Features': ['-'], 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 2, '6th': 1, '7th': 1, '8th': 1, '9th': 1},
            18: {'Proficiency Bonus': '+6', 'Features': ['Spell Mastery'], 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 3, '6th': 1, '7th': 1, '8th': 1, '9th': 1},
            19: {'Proficiency Bonus': '+6', 'Features': ['-'], 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 3, '6th': 2, '7th': 1, '8th': 1, '9th': 1},
            20: {'Proficiency Bonus': '+6', 'Features': ['Signature Spells'], 'Cantrips Known': 5, '1st': 4, '2nd': 3, '3rd': 3, '4th': 3, '5th': 3, '6th': 2, '7th': 2, '8th': 1, '9th': 1}    
        },
        "Features": {
            "Spellcasting": "At 1st level, you gain the ability to cast spells. You can prepare a number of spells each day from your spellbook and cast them using "
                            "spell slots. Your spellbook is a crucial tool for your spellcasting.",
            "Arcane Recovery": "At 1st level, you have the ability to recover some of your expended spell slots during a short rest. This feature helps you regain "
                            "magical energy quickly.",
            "Arcane Tradition": "At 2nd level, you choose an Arcane Tradition, which determines your focus within the magical arts. Each tradition offers unique abilities "
                                "and spells related to that school of magic.",
            "Cantrip Formulas (Optional)": "At 3rd level, you can create formulas that allow you to switch out one or more of your cantrips when you gain a level. "
                                        "This is an optional feature and provides flexibility in your cantrip choices.",
            "Ability Score Improvement": "At 4th level and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can "
                                        "increase two ability scores of your choice by 1. This allows you to customize your character as you progress.",
            "Spell Mastery": "At 18th level, you gain mastery over certain spells, allowing you to cast them at will without expending a spell slot. This demonstrates "
                            "your deep understanding of these spells.",
            "Signature Spells": "At 20th level, you gain access to a special list of Signature Spells, which are always prepared for you. You can cast these spells "
                                "without expending a spell slot, adding versatility to your spellcasting."

        },
        "Hit Die": '1d6',
        "Proficiencies": {
            'Armor': 'None',
            'Weapons': 'Daggers, darts, slings, quarterstaffs, light crossbows',
            'Tools': 'None',
            "Spellcasting Modifier" : "Intelligence",
            'Saving Throws': ['Intelligence', 'Wisdom'],
            "Skills": {
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
                "7th" : ["Create Magen","Crown of Stars","Delayed Blast Fireball","Draconic Transformation","Etherealness","Finger of Death","Forcecage","Mirage Arcane","Mordenkainen's Magnificent Mansion","Mordenkainen's Sword","Plane Shift","Power Word - Pain","Prismatic Spray","Project Image","Reverse Gravity","Sequester","Simulacrum","Symbol","Teleport","Tether Essence","Whirlwind"],
                "8th" : ["Abi-Dalzim's Horrid Wilting","Antimagic Field","Antipathy/Sympathy","Clone","Control Weather","Dark Star","Demiplane","Dominate Monster","Feeblemind","Illusory Dragon","Incendiary Cloud","Maddening Darkness","Maze","Mighty Fortress","Mind Blank","Power Word - Stun","Reality Break","Sunburst","Telepathy"],
                "9th" : ["Astral Projection","Foresight","Gate","Imprisonment","Invulnerability","Mass Polymorph","Meteor Swarm","Power Word - Kill","Prismatic Wall","Psychic Scream","Ravenous Void","Shapechange","Time Ravage","Time Stop","True Polymorph","Weird","Wish"]
            }
        }
    }
}
