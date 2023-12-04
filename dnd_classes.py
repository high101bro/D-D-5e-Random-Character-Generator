#! /usr/bin/env python3

dnd_classes = {
    "Barbarian": {
        "Name": "Barbarian",
        "Description": "A fierce warrior of primitive background who can enter a battle rage.",
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
            'Hit Dice': '1d12',
            'Hit Points at 1st Level': '12 + your Constitution modifier',
            'Hit Points at Higher Levels': '1d12 (or 7) + your Constitution modifier per barbarian level after 1st',
            'Proficiencies': {
                'Armor': ['Light armor', 'medium armor', 'shields'],
                'Weapons': ['Simple weapons', 'martial weapons'],
                'Tools': 'None',
                "Spellcasting Modifier" : "None",
                'Saving Throws': ['Strength', 'Constitution'],
                'Skills': 'Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival',
                "Languages": []
            },
            'Equipment': [
                'a greataxe or any martial melee weapon',
                'two handaxes or any simple weapon',
                'An explorer\'s pack and four javelins',
            ]
        },
        "Spells" : {
            "Spellcasting Modifier" : "None",
            "Available" : {}
        }
    },
    "Bard": {
        "Name": "Bard",
        "Description": "An inspiring magician whose power echoes the music of creation.",
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
        "Features": {
            'Hit Dice': '1d8',
            'Hit Points at 1st Level': '8 + your Constitution modifier',
            'Hit Points at Higher Levels': '1d8 (or 5) + your Constitution modifier per bard level after 1st',
            'Proficiencies': {
                'Armor': 'Light armor',
                'Weapons': 'Simple weapons, hand crossbows, longswords, rapiers, shortswords',
                'Tools': 'Three musical instruments of your choice',
                "Spellcasting Modifier" : "Charisma",
                'Saving Throws': 'Dexterity, Charisma',
                'Skills': 'Choose any three',
                "Languages": []
            },
            'Equipment': {
                '(a) a rapier, (b) a longsword, or (c) any simple weapon': 1,
                '(a) a diplomat\'s pack or (b) an entertainer\'s pack': 1,
                '(a) a lute or (b) any other musical instrument': 1,
                'Leather armor and a dagger': 1
            }
        },
        "Spells" : {
            "Spellcasting Modifier" : "charisma",
            "Available" : {
                "Cantrips" : ["Blade Ward","Dancing Lights","Friends","Light","Mage Hand","Mending","Message","Minor Illusion","Prestidigitation","Thunderclap","True Strike","Vicious Mockery"],
                "1st Level" : ["Animal Friendship","Bane","Charm Person","Comprehend Languages","Cure Wounds","Detect Magic","Disguise Self","Dissonant Whispers","Distort Value","Earth Tremor","Faerie Fire","Feather Fall","Healing Word","Heroism","Identify","Illusory Script","Longstrider","Silent Image","Silvery Barbs","Sleep","Speak with Animals","Tasha's Hideous Laughter","Thunderwave","Unseen Servant"],
                "2nd Level" : ["Animal Messenger","Blindness/Deafness","Borrowed Knowledge","Calm Emotions","Cloud of Daggers","Crown of Madness","Detect Thoughts","Enhance Ability","Enthrall","Gift of Gab","Heat Metal","Hold Person","Invisibility","Kinetic Jaunt","Knock","Lesser Restoration","Locate Animals or Plants","Locate Object","Magic Mouth","Nathair's Mischief","Phantasmal Force","Pyrotechnics","See Invisibility","Shatter","Silence","Skywrite","Spray Of Cards","Suggestion","Warding Wind","Zone of Truth"],
                "3rd Level" : ["Antagonize","Bestow Curse","Catnap","Clairvoyance","Dispel Magic","Enemies Abound","Fast Friends","Fear","Feign Death","Glyph of Warding","Hypnotic Pattern","Leomund's Tiny Hut","Major Image","Motivational Speech","Nondetection","Plant Growth","Sending","Speak with Dead","Speak with Plants","Stinking Cloud","Tongues"],
                "4th Level" : ["Charm Monster","Compulsion","Confusion","Dimension Door","Freedom of Movement","Greater Invisibility","Hallucinatory Terrain","Locate Creature","Polymorph","Raulothim's Psychic Lance"],
                "5th Level" : ["Animate Objects","Awaken","Dominate Person","Dream","Geas","Greater Restoration","Hold Monster","Legend Lore","Mass Cure Wounds","Mislead","Modify Memory","Planar Binding","Raise Dead","Scrying","Seeming","Skill Empowerment","Synaptic Static","Teleportation Circle"],
                "6th Level" : ["Eyebite","Find the Path","Guards and Wards","Mass Suggestion","Otto's Irresistible Dance","Programmed Illusion","True Seeing"],
                "7th Level" : ["Etherealness","Forcecage","Mirage Arcane","Mordenkainen's Magnificent Mansion","Mordenkainen's Sword","Prismatic Spray","Project Image","Regenerate","Resurrection","Symbol","Teleport"],
                "8th Level" : ["Dominate Monster","Feeblemind","Glibness","Mind Blank","Power Word: Stun"],
                "9th Level" : ["Foresight","Mass Polymorph","Power Word: Heal","Power Word: Kill","Psychic Scream","True Polymorph"]
            }
        }
    },
    "Cleric": {
        "Name": "Cleric",
        "Description": "A priestly champion who wields divine magic in service of a higher power.",
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
        "Features": {
            'Hit Dice': '1d8',
            'Hit Points at 1st Level': '8 + your Constitution modifier',
            'Hit Points at Higher Levels': '1d8 (or 5) + your Constitution modifier per cleric level after 1st',
            'Proficiencies': {
                'Armor': 'Light armor, medium armor, shields',
                'Weapons': 'All simple weapons',
                'Tools': 'None',
                "Spellcasting Modifier" : "Wisdom",
                'Saving Throws': 'Wisdom, Charisma',
                'Skills': 'Choose two from History, Insight, Medicine, Persuasion, and Religion',
                "Languages": []
            },
            'Equipment': {
                'Choice 1': 'a mace',
                'Choice 2': 'scale mail',
                'Choice 3': 'a light crossbow and 20 bolts',
                'Choice 4': 'a priest\'s pack',
                'Choice 5': 'A shield and a holy symbol',
                'Choice 6 (if proficient)': 'a warhammer',
                'Choice 7 (if proficient)': 'leather armor',
                'Choice 8 (if proficient)': 'chain mail'
            }
        },
        "Spells" : {
            "Spellcasting Modifier" : "wisdom",
            "Available" : {
                "Cantrips" : ["Guidance","Light","Mending","Resistance","Sacred Flame","Spare the Dying","Thaumaturgy","Toll the Dead","Word of Radiance"],
                "1st Level" : ["Bane","Bless","Ceremony","Command","Create or Destroy Water","Cure Wounds","Detect Evil and Good","Detect Magic","Detect Poison and Disease","Guiding Bolt","Healing Word","Inflict Wounds","Protection from Evil and Good","Purify Food and Drink","Sanctuary","Shield of Faith"],
                "2nd Level" : ["Aid","Augury","Blindness/Deafness","Borrowed Knowledge","Calm Emotions","Continual Flame","Enhance Ability","Find Traps","Gentle Repose","Hold Person","Lesser Restoration","Locate Object","Prayer of Healing","Protection from Poison","Silence","Spiritual Weapon","Warding Bond","Zone of Truth"],
                "3rd Level" : ["Animate Dead","Beacon of Hope","Bestow Curse","Clairvoyance","Create Food and Water","Daylight","Dispel Magic","Fast Friends","Feign Death","Glyph of Warding","Incite Greed","Life Transference","Magic Circle","Mass Healing Word","Meld into Stone","Motivational Speech","Protection from Energy","Remove Curse","Revivify","Sending","Speak with Dead","Spirit Guardians","Tongues","Water Walk"],
                "4th Level" : ["Banishment","Control Water","Death Ward","Divination","Freedom of Movement","Guardian of Faith","Locate Creature","Stone Shape"],
                "5th Level" : ["Commune","Contagion","Dawn","Dispel Evil and Good","Flame Strike","Geas","Greater Restoration","Hallow","Holy Weapon","Insect Plague","Legend Lore","Mass Cure Wounds","Planar Binding","Raise Dead","Scrying"],
                "6th Level" : ["Blade Barrier","Create Undead","Find the Path","Forbiddance","Harm","Heal","Heroes' Feast","Planar Ally","True Seeing","Word of Recall"],
                "7th Level" : ["Conjure Celestial","Divine Word","Etherealness","Fire Storm","Plane Shift","Regenerate","Resurrection","Symbol","Temple of the Gods"],
                "8th Level" : ["Antimagic Field","Control Weather","Earthquake","Holy Aura"],
                "9th Level" : ["Astral Projection","Gate","Mass Heal","True Resurrection"]
            }
        }
    },
    "Druid": {
        "Name": "Druid",
        "Description": "A priest of the Old Faith, wielding the powers of nature and adopting animal forms.",
        "Level Chart" : {
            
        },
        "Features": {
            "Spellcasting Modifier" : "Wisdom",
            "Languages": {
                "Druidic": "You know Druidic, the secret language of druids."
            }
        },
        "Spells" : {
            "Spellcasting Modifier" : "wisdom",
            "Available" : {
                "Cantrips" : ["Control Flames","Create Bonfire","Druidcraft","Frostbite","Guidance","Gust","Infestation","Magic Stone","Mending","Mold Earth","Poison Spray","Primal Savagery","Produce Flame","Resistance","Shape Water","Shillelagh","Thorn Whip","Thunderclap"],
                "1st Level" : ["Absorb Elements","Animal Friendship","Beast Bond","Charm Person","Create or Destroy Water","Cure Wounds","Detect Magic","Detect Poison and Disease","Earth Tremor","Entangle","Faerie Fire","Fog Cloud","Goodberry","Healing Word","Ice Knife","Jump","Longstrider","Purify Food and Drink","Snare","Speak with Animals","Thunderwave"],
                "2nd Level" : ["Air Bubble","Animal Messenger","Barkskin","Beast Sense","Darkvision","Dust Devil","Earthbind","Enhance Ability","Find Traps","Flame Blade","Flaming Sphere","Gust of Wind","Healing Spirit","Heat Metal","Hold Person","Lesser Restoration","Locate Animals or Plants","Locate Object","Moonbeam","Pass Without Trace","Protection from Poison","Skywrite","Spike Growth","Warding Wind","Wither and Bloom"],
                "3rd Level" : ["Call Lightning","Conjure Animals","Daylight","Dispel Magic","Erupting Earth","Feign Death","Flame Arrows","Meld into Stone","Plant Growth","Protection from Energy","Sleet Storm","Speak with Plants","Tidal Wave","Wall of Water","Water Breathing","Water Walk","Wind Wall"],
                "4th Level" : ["Blight","Charm Monster","Confusion","Conjure Minor Elementals","Conjure Woodland Beings","Control Water","Dominate Beast","Elemental Bane","Freedom of Movement","Giant Insect","Grasping Vine","Guardian of Nature","Hallucinatory Terrain","Ice Storm","Locate Creature","Polymorph","Stone Shape","Stoneskin","Wall of Fire","Watery Sphere"],
                "5th Level" : ["Antilife Shell","Awaken","Commune with Nature","Conjure Elemental","Contagion","Control Winds","Geas","Greater Restoration","Insect Plague","Maelstrom","Mass Cure Wounds","Planar Binding","Reincarnate","Scrying","Summon Draconic Spirit","Transmute Rock","Tree Stride","Wall of Stone","Wrath Of Nature"],
                "6th Level" : ["Bones of the Earth","Conjure Fey","Druid Grove","Find the Path","Heal","Heroes' Feast","Investiture of Flame","Investiture of Ice","Investiture of Stone","Investiture of Wind","Move Earth","Primordial Ward","Sunbeam","Transport via Plants","Wall of Thorns","Wind Walk"],
                "7th Level" : ["Draconic Transformation","Fire Storm","Mirage Arcane","Plane Shift","Regenerate","Reverse Gravity","Whirlwind"],
                "8th Level" : ["Animal Shapes","Antipathy/Sympathy","Control Weather","Earthquake","Feeblemind","Sunburst","Tsunami"],
                "9th Level" : ["Foresight","Shapechange","Storm of Vengeance","True Resurrection"]
            }
        }
    },
    "Fighter": {
        "Name": "Fighter",
        "Description": "A master of martial combat, skilled with a variety of weapons and armor.",
        "Level Chart" : {
            
        },
        "Features": {
            "Spellcasting Modifier" : "None",
            "Languages": []
        },
        "Spells" : {
            "Spellcasting Modifier" : "None",
            "Available" : {}
        }
    },
    "Monk": {
        "Name": "Monk",
        "Description": "A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection.",
        "Level Chart" : {
            
        },
        "Features": {
            "Spellcasting Modifier" : "None",
            "Languages": []
        },
        "Spells" : {
            "Spellcasting Modifier" : "None",
            "Available" : {}
        }
    },
    "Paladin": {
        "Name": "Paladin",
        "Description": "A holy warrior bound to a sacred oath.",
        "Level Chart" : {
            1: {'Proficiency Bonus': '+2', 'Features': 'Divine Sense, Lay on Hands', '1st Level Spell Slots': '-', '2nd Level Spell Slots': '-', '3rd Level Spell Slots': '-', '4th Level Spell Slots': '-', '5th Level Spell Slots': '-'},
            2: {'Proficiency Bonus': '+2', 'Features': 'Fighting Style, Spellcasting, Divine Smite', '1st Level Spell Slots': '2', '2nd Level Spell Slots': '-', '3rd Level Spell Slots': '-', '4th Level Spell Slots': '-', '5th Level Spell Slots': '-'},
            3: {'Proficiency Bonus': '+2', 'Features': 'Divine Health, Sacred Oath, Harness Divine Power (Optional)', '1st Level Spell Slots': '3', '2nd Level Spell Slots': '-', '3rd Level Spell Slots': '-', '4th Level Spell Slots': '-', '5th Level Spell Slots': '-'},
            4: {'Proficiency Bonus': '+2', 'Features': 'Ability Score Improvement, Martial Versatility (Optional)', '1st Level Spell Slots': '3', '2nd Level Spell Slots': '-', '3rd Level Spell Slots': '-', '4th Level Spell Slots': '-', '5th Level Spell Slots': '-'},
            5: {'Proficiency Bonus': '+3', 'Features': 'Extra Attack', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '2', '3rd Level Spell Slots': '-', '4th Level Spell Slots': '-', '5th Level Spell Slots': '-'},
            6: {'Proficiency Bonus': '+3', 'Features': 'Aura of Protection', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '2', '3rd Level Spell Slots': '-', '4th Level Spell Slots': '-', '5th Level Spell Slots': '-'},
            7: {'Proficiency Bonus': '+3', 'Features': 'Sacred Oath feature', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '3', '3rd Level Spell Slots': '-', '4th Level Spell Slots': '-', '5th Level Spell Slots': '-'},
            8: {'Proficiency Bonus': '+3', 'Features': 'Ability Score Improvement, Martial Versatility (Optional)', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '3', '3rd Level Spell Slots': '-', '4th Level Spell Slots': '-', '5th Level Spell Slots': '-'},
            9: {'Proficiency Bonus': '+4', 'Features': '', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '3', '3rd Level Spell Slots': '2', '4th Level Spell Slots': '-', '5th Level Spell Slots': '-'},
            10: {'Proficiency Bonus': '+4', 'Features': 'Aura of Courage', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '3', '3rd Level Spell Slots': '2', '4th Level Spell Slots': '-', '5th Level Spell Slots': '-'},
            11: {'Proficiency Bonus': '+4', 'Features': 'Improved Divine Smite', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '3', '3rd Level Spell Slots': '3', '4th Level Spell Slots': '-', '5th Level Spell Slots': '-'},
            12: {'Proficiency Bonus': '+4', 'Features': 'Ability Score Improvement, Martial Versatility (Optional)', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '3', '3rd Level Spell Slots': '3', '4th Level Spell Slots': '-', '5th Level Spell Slots': '-'},
            13: {'Proficiency Bonus': '+5', 'Features': '', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '3', '3rd Level Spell Slots': '3', '4th Level Spell Slots': '1', '5th Level Spell Slots': '-'},
            14: {'Proficiency Bonus': '+5', 'Features': 'Cleansing Touch', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '3', '3rd Level Spell Slots': '3', '4th Level Spell Slots': '1', '5th Level Spell Slots': '-'},
            15: {'Proficiency Bonus': '+5', 'Features': 'Sacred Oath feature', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '3', '3rd Level Spell Slots': '3', '4th Level Spell Slots': '2', '5th Level Spell Slots': '-'},
            16: {'Proficiency Bonus': '+5', 'Features': 'Ability Score Improvement, Martial Versatility (Optional)', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '3', '3rd Level Spell Slots': '3', '4th Level Spell Slots': '2', '5th Level Spell Slots': '-'},
            17: {'Proficiency Bonus': '+6', 'Features': '', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '3', '3rd Level Spell Slots': '3', '4th Level Spell Slots': '3', '5th Level Spell Slots': '1'},
            18: {'Proficiency Bonus': '+6', 'Features': 'Aura improvements', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '3', '3rd Level Spell Slots': '3', '4th Level Spell Slots': '3', '5th Level Spell Slots': '1'},
            19: {'Proficiency Bonus': '+6', 'Features': 'Ability Score Improvement, Martial Versatility (Optional)', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '3', '3rd Level Spell Slots': '3', '4th Level Spell Slots': '3', '5th Level Spell Slots': '2'},
            20: {'Proficiency Bonus': '+6', 'Features': 'Sacred Oath feature', '1st Level Spell Slots': '4', '2nd Level Spell Slots': '3', '3rd Level Spell Slots': '3', '4th Level Spell Slots': '3', '5th Level Spell Slots': '2'}
        },
        "Features" : {
            "Hit Dice": "1d10",
            "Hit Points at 1st Level": "10 + your Constitution modifier",
            "Hit Points at Higher Levels": "1d10 (or 6) + your Constitution modifier per paladin level after 1st",
            "Proficiencies": {
                "Armor": "All armor, shields",
                "Weapons": ["simple weapons", "martial weapons"],
                "Tools": "None",
                "Spellcasting Modifier" : "Charisma",
                "Saving Throws": ["Wisdom, Charisma"],
                "Skills": ["Choose two from Athletics, Insight, Intimidation, Medicine, Persuasion, and Religion"],
                "Languages": []
            },
            "Equipment": {
                "Choice 1": "(a) a martial weapon and a shield or (b) two martial weapons",
                "Choice 2": "(a) five javelins or (b) any simple melee weapon",
                "Choice 3": "(a) a priest's pack or (b) an explorer's pack",
                "Additional": "Chain mail and a holy symbol"
            }            
        },
        "Spells" : {
            "Spellcasting Modifier" : "charisma",
            "Spell Slots" : "Paladins have a limited number of spell slots of different levels, which they use to cast spells. The number and level of these slots depend on the paladin's level. Refer to the 'The Paladin Spell Slots per Spell Level' table in your class description to see how many spell slots of each level you have.",
            "Preparing Spells" : "Unlike spellcasters like wizards who prepare spells each day, paladins know all the spells available to them at their level. They don't need to prepare spells in advance. Instead, they choose which spells to cast from their known spells when they use their spell slots.",
            "Casting Spells" : "To cast a spell, a paladin expends one of their spell slots of the appropriate level. The paladin then uses their spellcasting ability (Charisma) to determine the spell's effects, such as its attack roll or saving throw DC, if applicable.",
            "Divine Smite" : "Paladins have a unique ability called Divine Smite. This ability allows them to expend spell slots to deal extra damage when they hit with a melee weapon attack. The higher the level of the spell slot they expend, the more damage they can add.",
            "Spell Levels" : "Spells in D&D 5e are categorized into spell levels, ranging from 1st level to 9th level, with 1st-level spells being the least powerful and 9th-level spells the most powerful. The level of a spell slot determines the highest-level spell a paladin can cast using that slot. For example, a 2nd-level spell slot can be used to cast a 1st-level or 2nd-level spell.",
            "Spell Preparation" : "At the end of a long rest, paladins can change their known spells by meditating and praying for their spells. They can swap out spells they know for other spells from the paladin spell list, as long as they have spell slots of the appropriate level.",
            "Spell List" : "Paladins have access to a specific list of spells, which is outlined in the Paladin class description. They can only choose spells from this list when they gain access to new spells.",
            "Available" : {
                "1st Level" : ["Bless","Ceremony","Command","Compelled Duel","Cure Wounds","Detect Evil and Good","Detect Magic","Detect Poison and Disease","Divine Favor","Heroism","Protection from Evil and Good","Purify Food and Drink","Searing Smite","Shield of Faith","Thunderous Smite","Wrathful Smite"],
                "2nd Level" : ["Aid","Branding Smite","Find Steed","Lesser Restoration","Locate Object","Magic Weapon","Protection from Poison","Zone of Truth"],
                "3rd Level" : ["Aura of Vitality","Blinding Smite","Create Food and Water","Crusader's Mantle","Daylight","Dispel Magic","Elemental Weapon","Magic Circle","Remove Curse","Spirit Shroud"],
                "4th Level" : ["Aura of Life","Aura of Purity","Banishment","Death Ward","Find Greater Steed","Locate Creature","Staggering Smite"],
                "5th Level" : ["Banishing Smite","Circle of Power","Destructive Wave","Dispel Evil and Good","Geas","Holy Weapon","Raise Dead"]
            }
        }
    },
    "Ranger": {
        "Name": "Ranger",
        "Description": "A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization.",
        "Level Chart" : {
            
        },
        "Features": {
            "Spellcasting Modifier" : "Widsom",
            "Languages": []
        },
        "Spells" : {
            "Spellcasting Modifier" : "wisdom",
            "Available" : {
                "1st Level" : ["Absorb Elements","Alarm","Animal Friendship","Beast Bond","Cure Wounds","Detect Magic","Detect Poison and Disease","Ensnaring Strike","Fog Cloud","Goodberry","Hail of Thorns","Hunter's Mark","Jump","Longstrider","Snare","Speak with Animals","Zephyr Strike"],
                "2nd Level" : ["Air Bubble","Animal Messenger","Barkskin","Beast Sense","Cordon of Arrows","Darkvision","Find Traps","Healing Spirit","Lesser Restoration","Locate Animals or Plants","Locate Object","Pass Without Trace","Protection from Poison","Silence","Spike Growth"],
                "3rd Level" : ["Ashardalon's Stride","Conjure Animals","Conjure Barrage","Daylight","Flame Arrows","Lightning Arrow","Nondetection","Plant Growth","Protection from Energy","Speak with Plants","Water Breathing","Water Walk","Wind Wall"],
                "4th Level" : ["Conjure Woodland Beings","Freedom of Movement","Grasping Vine","Guardian of Nature","Locate Creature","Stoneskin"],
                "5th Level" : ["Commune with Nature","Conjure Volley","Steel Wind Strike","Swift Quiver","Tree Stride","Wrath Of Nature"]           
            }
        }
    },
    "Rogue": {
        "Name": "Rogue",
        "Description": "A scoundrel who uses stealth and trickery to overcome obstacles and enemies.",
        "Level Chart" : {
            
        },
        "Features": {
            "Spellcasting Modifier" : "None",
            "Languages": []
        },
        "Spells" : {
            "Spellcasting Modifier" : "None",
            "Available" : {}
        }
    },
    "Sorcerer": {
        "Name": "Sorcerer",
        "Description": "A spellcaster who draws on inherent magic from a gift or bloodline.",
        "Level Chart" : {
            
        },
        "Features": {
            "Spellcasting": "Cast sorcerer spells.",
            "Sorcerous Origin": "Gain special magical abilities based on your magical origin."
        },
        "Proficiencies": {
            "Armor": [],
            "Weapons": ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light crossbows"],
            "Tools": [],
            "Spellcasting Modifier" : "Charisma",
            "Saving Throws": ["Constitution", "Charisma"],
            "Skills": "Choose two from Arcana, Deception, Insight, Intimidation, Persuasion, and Religion",
            "Languages": []
        },
        "Spells" : {
            "Spellcasting Modifier" : "charisma",
            "Available" : {
                "Cantrips" : ["Acid Splash","Blade Ward","Chill Touch","Control Flames","Create Bonfire","Dancing Lights","Fire Bolt","Friends","Frostbite","Gust","Infestation","Light","Mage Hand","Mending","Message","Minor Illusion","Mold Earth","Poison Spray","Prestidigitation","Ray of Frost","Shape Water","Shocking Grasp","Thunderclap","True Strike"],
                "1st Level" : ["Absorb Elements","Burning Hands","Catapult","Chaos Bolt","Charm Person","Chromatic Orb","Color Spray","Comprehend Languages","Detect Magic","Disguise Self","Distort Value","Earth Tremor","Expeditious Retreat","False Life","Feather Fall","Fog Cloud","Ice Knife","Jump","Mage Armor","Magic Missile","Ray of Sickness","Shield","Silent Image","Silvery Barbs","Sleep","Thunderwave","Witch Bolt"],
                "2nd Level" : ["Aganazzar's Scorcher","Air Bubble","Alter Self","Blindness/Deafness","Blur","Cloud of Daggers","Crown of Madness","Darkness","Darkvision","Detect Thoughts","Dragon's Breath","Dust Devil","Earthbind","Enhance Ability","Enlarge/Reduce","Gust of Wind","Hold Person","Invisibility","Kinetic Jaunt","Knock","Levitate","Maximillian's Earthen Grasp","Mind Spike","Mirror Image","Misty Step","Nathair's Mischief","Phantasmal Force","Pyrotechnics","Rime's Binding Ice","Scorching Ray","See Invisibility","Shadow Blade","Shatter","Snilloc's Snowball Storm","Spider Climb","Spray Of Cards","Suggestion","Vortex Warp","Warding Wind","Warp Sense","Web","Wither and Bloom"],
                "3rd Level" : ["Antagonize","Ashardalon's Stride","Blink","Catnap","Clairvoyance","Counterspell","Daylight","Dispel Magic","Enemies Abound","Erupting Earth","Fear","Fireball","Flame Arrows","Fly","Gaseous Form","Haste","Hypnotic Pattern","Incite Greed","Lightning Bolt","Major Image","Melf's Minute Meteors","Protection from Energy","Sleet Storm","Slow","Stinking Cloud","Thunder Step","Tongues","Wall of Water","Water Breathing","Water Walk"],
                "4th Level" : ["Banishment","Blight","Charm Monster","Confusion","Dimension Door","Dominate Beast","Gate Seal","Greater Invisibility","Ice Storm","Polymorph","Raulothim's Psychic Lance","Sickening Radiance","Spirit Of Death","Stoneskin","Storm Sphere","Vitriolic Sphere","Wall of Fire","Watery Sphere"],
                "5th Level" : ["Animate Objects","Cloudkill","Cone of Cold","Control Winds","Creation","Dominate Person","Enervation","Far Step","Hold Monster","Immolation","Insect Plague","Seeming","Skill Empowerment","Summon Draconic Spirit","Synaptic Static","Telekinesis","Teleportation Circle","Wall of Light","Wall of Stone"],
                "6th Level" : ["Arcane Gate","Chain Lightning","Circle of Death","Disintegrate","Eyebite","Fizban's Platinum Shield","Globe of Invulnerability","Investiture of Flame","Investiture of Ice","Investiture of Stone","Investiture of Wind","Mass Suggestion","Mental Prison","Move Earth","Scatter","Sunbeam","True Seeing"],
                "7th Level" : ["Crown of Stars","Delayed Blast Fireball","Draconic Transformation","Etherealness","Finger of Death","Fire Storm","Plane Shift","Power Word: Pain","Prismatic Spray","Reverse Gravity","Teleport"],
                "8th Level" : ["Abi-Dalzim's Horrid Wilting","Dominate Monster","Earthquake","Incendiary Cloud","Power Word: Stun","Sunburst"],
                "9th Level" : ["Blade of Disaster","Gate","Mass Polymorph","Meteor Swarm","Power Word: Kill","Psychic Scream","Time Stop","Wish"]
            }
        }
    },
    "Warlock": {
        "Name": "Warlock",
        "Description": "A wielder of magic that is derived from a bargain with an extraplanar entity.",
        "Level Chart" : {
            
        },
        "Features": {
            "Spellcasting Modifier" : "Charisma",
            "Languages": []
        },
        "Spells" : {
            "Spellcasting Modifier" : "charisma",
            "Available" : {
                "Cantrips" : ["Blade Ward","Chill Touch","Create Bonfire","Eldritch Blast","Friends","Frostbite","Infestation","Mage Hand","Magic Stone","Minor Illusion","Poison Spray","Prestidigitation","Thunderclap","Toll the Dead","True Strike"],
                "1st Level" : ["Armor of Agathys","Arms of Hadar","Cause Fear","Charm Person","Comprehend Languages","Distort Value","Expeditious Retreat","Hellish Rebuke","Hex","Illusory Script","Protection from Evil and Good","Unseen Servant","Witch Bolt"],
                "2nd Level" : ["Borrowed Knowledge","Cloud of Daggers","Crown of Madness","Darkness","Earthbind","Enthrall","Flock of Familiars","Hold Person","Invisibility","Mind Spike","Mirror Image","Misty Step","Ray of Enfeeblement","Shadow Blade","Shatter","Spider Climb","Spray Of Cards","Suggestion","Warp Sense"],
                "3rd Level" : ["Antagonize","Counterspell","Dispel Magic","Enemies Abound","Fear","Fly","Gaseous Form","Hunger Of Hadar","Hypnotic Pattern","Incite Greed","Magic Circle","Major Image","Remove Curse","Summon Lesser Demons","Thunder Step","Tongues","Vampiric Touch"],
                "4th Level" : ["Banishment","Blight","Charm Monster","Dimension Door","Elemental Bane","Galder's Speedy Courier","Gate Seal","Hallucinatory Terrain","Raulothim's Psychic Lance","Shadow Of Moil","Sickening Radiance","Spirit Of Death"],
                "5th Level" : ["Contact Other Plane","Danse Macabre","Dream","Enervation","Far Step","Hold Monster","Infernal Calling","Negative Energy Flood","Scrying","Synaptic Static","Wall of Light"],
                "6th Level" : ["Arcane Gate","Circle of Death","Conjure Fey","Create Undead","Eyebite","Flesh to Stone","Investiture of Flame","Investiture of Ice","Investiture of Stone","Investiture of Wind","Mass Suggestion","Mental Prison","Scatter","Soul Cage","True Seeing"],
                "7th Level" : ["Crown of Stars","Etherealness","Finger of Death","Forcecage","Plane Shift","Power Word: Pain"],
                "8th Level" : ["Demiplane","Dominate Monster","Feeblemind","Glibness","Maddening Darkness","Power Word: Stun"],
                "9th Level" : ["Astral Projection","Foresight","Imprisonment","Power Word: Kill","Psychic Scream","True Polymorph"]
            }
        }
    },
    "Wizard": {
        "Description": "A scholarly magic-user capable of manipulating the structures of reality.",
        "Level Chart" : {
            
        },
        "Features": {
            "Spellcasting Modifier" : "Intelligence",
            "Languages": []
        },
        "Spells" : {
            "Spellcasting Modifier" : "intelligence",
            "Available" : {
                "Cantrips" : ["Acid Splash","Blade Ward","Chill Touch","Control Flames","Create Bonfire","Dancing Lights","Encode Thoughts","Fire Bolt","Friends","Frostbite","Gust","Infestation","Light","Mage Hand","Mending","Message","Minor Illusion","Mold Earth","Poison Spray","Prestidigitation","Ray of Frost","Sapping Sting","Shape Water","Shocking Grasp","Thunderclap","Toll the Dead","True Strike"],
                "1st Level" : ["Absorb Elements","Alarm","Burning Hands","Catapult","Cause Fear","Charm Person","Chromatic Orb","Color Spray","Comprehend Languages","Detect Magic","Disguise Self","Distort Value","Earth Tremor","Expeditious Retreat","False Life","Feather Fall","Find Familiar","Fog Cloud","Frost Fingers","Gift of Alacrity","Grease","Ice Knife","Identify","Illusory Script","Jim's Magic Missile","Jump","Longstrider","Mage Armor","Magic Missile","Magnify Gravity","Protection from Evil and Good","Ray of Sickness","Shield","Silent Image","Silvery Barbs","Sleep","Snare","Tasha's Hideous Laughter","Tenser's Floating Disk","Thunderwave","Unseen Servant","Witch Bolt"],
                "2nd Level" : ["Aganazzar's Scorcher","Air Bubble","Alter Self","Arcane Lock","Blindness/Deafness","Blur","Borrowed Knowledge","Cloud of Daggers","Continual Flame","Crown of Madness","Darkness","Darkvision","Detect Thoughts","Dragon's Breath","Dust Devil","Earthbind","Enlarge/Reduce","Flaming Sphere","Flock of Familiars","Fortune's Favor","Gentle Repose","Gift of Gab","Gust of Wind","Hold Person","Immovable Object","Invisibility","Jim's Glowing Coin","Kinetic Jaunt","Knock","Levitate","Locate Object","Magic Mouth","Magic Weapon","Maximillian's Earthen Grasp","Melf's Acid Arrow","Mind Spike","Mirror Image","Misty Step","Nathair's Mischief","Nystul's Magic Aura","Phantasmal Force","Pyrotechnics","Ray of Enfeeblement","Rime's Binding Ice","Rope Trick","Scorching Ray","See Invisibility","Shadow Blade","Shatter","Skywrite","Snilloc's Snowball Storm","Spider Climb","Spray Of Cards","Suggestion","Vortex Warp","Warding Wind","Warp Sense","Web","Wither and Bloom","Wristpocket"],
                "3rd Level" : ["Animate Dead","Antagonize","Ashardalon's Stride","Bestow Curse","Blink","Catnap","Clairvoyance","Counterspell","Dispel Magic","Enemies Abound","Erupting Earth","Fast Friends","Fear","Feign Death","Fireball","Flame Arrows","Fly","Galder's Tower","Gaseous Form","Glyph of Warding","Haste","Hypnotic Pattern","Incite Greed","Leomund's Tiny Hut","Life Transference","Lightning Bolt","Magic Circle","Major Image","Melf's Minute Meteors","Nondetection","Phantom Steed","Protection from Energy","Pulse Wave","Remove Curse","Sending","Sleet Storm","Slow","Stinking Cloud","Summon Lesser Demons","Thunder Step","Tidal Wave","Tiny Servant","Tongues","Vampiric Touch","Wall of Sand","Wall of Water","Water Breathing"],
                "4th Level" : ["Arcane Eye","Banishment","Blight","Charm Monster","Confusion","Conjure Minor Elementals","Control Water","Dimension Door","Elemental Bane","Evard's Black Tentacles","Fabricate","Fire Shield","Galder's Speedy Courier","Gate Seal","Gravity Sinkhole","Greater Invisibility","Hallucinatory Terrain","Ice Storm","Leomund's Secret Chest","Locate Creature","Mordenkainen's Faithful Hound","Mordenkainen's Private Sanctum","Otiluke's Resilient Sphere","Phantasmal Killer","Polymorph","Raulothim's Psychic Lance","Sickening Radiance","Spirit Of Death","Stone Shape","Stoneskin","Storm Sphere","Summon Greater Demon","Vitriolic Sphere","Wall of Fire","Watery Sphere"],
                "5th Level" : ["Animate Objects","Bigby's Hand","Cloudkill","Cone of Cold","Conjure Elemental","Contact Other Plane","Control Winds","Create Spelljamming Helm","Creation","Danse Macabre","Dawn","Dominate Person","Dream","Enervation","Far Step","Geas","Hold Monster","Immolation","Infernal Calling","Legend Lore","Mislead","Modify Memory","Negative Energy Flood","Passwall","Planar Binding","Rary's Telepathic Bond","Scrying","Seeming","Skill Empowerment","Steel Wind Strike","Summon Draconic Spirit","Synaptic Static","Telekinesis","Teleportation Circle","Temporal Shunt","Transmute Rock","Wall of Force","Wall of Light","Wall of Stone"],
                "6th Level" : ["Arcane Gate","Chain Lightning","Circle of Death","Contingency","Create Homunculus","Create Undead","Disintegrate","Drawmij's Instant Summons","Eyebite","Fizban's Platinum Shield","Flesh to Stone","Globe of Invulnerability","Gravity Fissure","Guards and Wards","Investiture of Flame","Investiture of Ice","Investiture of Stone","Investiture of Wind","Magic Jar","Mass Suggestion","Mental Prison","Move Earth","Otiluke's Freezing Sphere","Otto's Irresistible Dance","Programmed Illusion","Scatter","Soul Cage","Sunbeam","Tenser's Transformation","True Seeing","Wall of Ice"],
                "7th Level" : ["Create Magen","Crown of Stars","Delayed Blast Fireball","Draconic Transformation","Etherealness","Finger of Death","Forcecage","Mirage Arcane","Mordenkainen's Magnificent Mansion","Mordenkainen's Sword","Plane Shift","Power Word: Pain","Prismatic Spray","Project Image","Reverse Gravity","Sequester","Simulacrum","Symbol","Teleport","Tether Essence","Whirlwind"],
                "8th Level" : ["Abi-Dalzim's Horrid Wilting","Antimagic Field","Antipathy/Sympathy","Clone","Control Weather","Dark Star","Demiplane","Dominate Monster","Feeblemind","Illusory Dragon","Incendiary Cloud","Maddening Darkness","Maze","Mighty Fortress","Mind Blank","Power Word: Stun","Reality Break","Sunburst","Telepathy"],
                "9th Level" : ["Astral Projection","Foresight","Gate","Imprisonment","Invulnerability","Mass Polymorph","Meteor Swarm","Power Word: Kill","Prismatic Wall","Psychic Scream","Ravenous Void","Shapechange","Time Ravage","Time Stop","True Polymorph","Weird","Wish"]
            }
        }
    }
}
