#! /usr/bin/env python3

# ASCII Art
# https://patorjk.com/software/taag/#p=display&f=Big&t=DnD

dnd_races = {



    "Elf": {
        "ASCII Art": """
  ______ _  __ 
 |  ____| |/ _|
 | |__  | | |_ 
 |  __| | |  _|
 | |____| | |  
 |______|_|_|  
               
        """,
        "Name" : "Elf",
        "Description": "Elves are a magical people of otherworldly grace, living in the world but not entirely part of it. They live in places of ethereal beauty, in the midst of ancient forests or in silvery spires glittering with faerie light.",
        "Traits": {
            "Speed" : {
                "Ground" : 30,
                "Flight" : 0
            },
            "Vision": {
                "Normal" : {
                    "Description": "Normal vision is the default vision type for most humanoid characters in the game.",
                    "Range" : "Characters with normal vision typically have a visual range determined by the lighting conditions in the game. In normal daylight or well-lit areas, characters with normal vision can see up to a specific distance without any hindrance. The exact range may vary depending on factors like the time of day, weather, and the DM's discretion.",
                    "Light Sources" : "Characters with normal vision rely on natural or artificial light sources to see in dimly lit or dark areas. If there is insufficient light, they may suffer from the effects of dim light or darkness, which can impose penalties on their ability to see and perceive their surroundings.",
                    "No Special Features" : "Normal vision does not grant any special abilities like darkvision, which allows characters to see in darkness as if it were dim light. Characters with normal vision may require torches, lanterns, or other light sources in dark environments.",
                    "No Stat Modifications" : "Characters with normal vision do not receive any specific stat modifications related to their vision. Their vision is considered the standard baseline for visual perception."
                },
                "Darkvision": {
                    "Possesses" : False,
                    "Description": "Grants the ability to see in dim light within a certain radius as if it were bright light, and in darkness as if it were dim light. This trait allows characters to see in near-total darkness.",
                    "Range": "Typically 60 feet",
                    "Monochromatic": "Able to descern color in dim light as if it were bright light and in darkness as if it were dim light, but they can't discern color in darkness, only shades of gray."
                }
            },
            "Keen Senses": {
                "Description": "Provides proficiency in the perception skill. This trait reflects a character's acute senses, allowing them to be more aware of their surroundings.",
                "Skill Benefit": "perception",
                "Type": "Skill Proficiency"
            },
            "Fey Ancestry": {
                "Description": "Grants advantage on saving throws against being charmed, and magic cannot put the character to sleep. This trait represents a character's magical heritage and resistance to certain enchantments.",
                "Advantage": "Against being charmed",
                "Immunity": "Magic-induced sleep",
                "Type": "Magical Resistance"
            },
            "Trance": {
                "Description": "Elves do not need to sleep. Instead, they meditate deeply for 4 hours a day. The meditation is as restful as 8 hours of sleep for other races. This trait reflects an elf's connection to their ancient origins and a different approach to rest.",
                "Duration": "4 hours",
                "Equivalent Rest": "8 hours of sleep",
                "Type": "Resting Method"
            }
        },
        "Proficiencies": {
            "languages": ["Common", "Elvish"],
            "tools": [],
            "weapons": ["Longsword", "Shortsword", "Shortbow", "Longbow"]
        },
        "Ability Score Increase": {'dexterity' : 2}
    },



    "Dwarf": {
        "ASCII Art": """
  _____                      __ 
 |  __ \                    / _|
 | |  | |_      ____ _ _ __| |_ 
 | |  | \ \ /\ / / _` | '__|  _|
 | |__| |\ V  V / (_| | |  | |  
 |_____/  \_/\_/ \__,_|_|  |_|  
                                
        """,
        "Name" : "Dwarf",
        "Description": "Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal. Dwarven kingdoms are located deep underground and they have a deep respect for their ancestors.",
        "Traits": {
            "Speed" : {
                "Ground" : 25,
                "Flight" : 0
            },
            "Vision": {
                "Normal" : {
                    "Description": "Normal vision is the default vision type for most humanoid characters in the game.",
                    "Range" : "Characters with normal vision typically have a visual range determined by the lighting conditions in the game. In normal daylight or well-lit areas, characters with normal vision can see up to a specific distance without any hindrance. The exact range may vary depending on factors like the time of day, weather, and the DM's discretion.",
                    "Light Sources" : "Characters with normal vision rely on natural or artificial light sources to see in dimly lit or dark areas. If there is insufficient light, they may suffer from the effects of dim light or darkness, which can impose penalties on their ability to see and perceive their surroundings.",
                    "No Special Features" : "Normal vision does not grant any special abilities like darkvision, which allows characters to see in darkness as if it were dim light. Characters with normal vision may require torches, lanterns, or other light sources in dark environments.",
                    "No Stat Modifications" : "Characters with normal vision do not receive any specific stat modifications related to their vision. Their vision is considered the standard baseline for visual perception."
                },
                "Darkvision": {
                    "Possesses" : True,
                    "Description": "Grants the ability to see in dim light within a certain radius as if it were bright light, and in darkness as if it were dim light. This trait allows characters to see in near-total darkness.",
                    "Range": "Typically 60 feet",
                    "Monochromatic": "Able to see in shades of gray without the ability to discern colors."
                }
            },
            "Dwarven Resilience": {
                "Description": "Dwarves have an innate resistance to poison damage and an advantage on saving throws against poison, reflecting their hardy nature and strong constitution.",
                "Benefit": "Advantage on saving throws against poison, resistance to poison damage",
                "Type": "Resilience"
            },
            "Dwarven Combat Training": {
                "Description": "Dwarves are proficient with certain weapons as a result of their martial training, including battleaxes, handaxes, light hammers, and warhammers.",
                "Weapon Proficiencies": ["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"],
                "Type": "Combat Proficiency"
            },
            "Stonecunning": {
                "Description": "This trait represents the dwarven affinity for stonework. Dwarves receive double their proficiency bonus on Intelligence (history) checks related to the origin of stonework.",
                "Benefit": "Double proficiency bonus on certain history checks",
                "Type": "Skill Enhancement"
            }
        },
        "Proficiencies": {
            "languages": ["Common", "Dwarvish"],
            "tools": ["One type of artisan's tools"],
            "weapons": ["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"]
        },
        "Ability Score Increase": {
            'constitution': 2
        }
    },



    "Dragonborn": {
        "ASCII Art": """
  _____                              _                      
 |  __ \                            | |                     
 | |  | |_ __ __ _  __ _  ___  _ __ | |__   ___  _ __ _ __  
 | |  | | '__/ _` |/ _` |/ _ \| '_ \| '_ \ / _ \| '__| '_ \ 
 | |__| | | | (_| | (_| | (_) | | | | |_) | (_) | |  | | | |
 |_____/|_|  \__,_|\__, |\___/|_| |_|_.__/ \___/|_|  |_| |_|
                    __/ |                                   
                   |___/                                    
        """,
        "Name" : "Dragonborn",
        "Description": "Dragonborn look very much like dragons standing erect in humanoid form, though they lack wings or a tail. The first dragonborn had scales of vibrant hues matching the colors of their dragon kin, but generations of interbreeding have created a more uniform appearance.",
        "Traits": {
            "Speed" : {
                "Ground" : 30,
                "Flight" : 0
            },
            "Vision" : {
                "Normal" : {
                    "Description": "Normal vision is the default vision type for most humanoid characters in the game.",
                    "Range" : "Characters with normal vision typically have a visual range determined by the lighting conditions in the game. In normal daylight or well-lit areas, characters with normal vision can see up to a specific distance without any hindrance. The exact range may vary depending on factors like the time of day, weather, and the DM's discretion.",
                    "Light Sources" : "Characters with normal vision rely on natural or artificial light sources to see in dimly lit or dark areas. If there is insufficient light, they may suffer from the effects of dim light or darkness, which can impose penalties on their ability to see and perceive their surroundings.",
                    "No Special Features" : "Normal vision does not grant any special abilities like darkvision, which allows characters to see in darkness as if it were dim light. Characters with normal vision may require torches, lanterns, or other light sources in dark environments.",
                    "No Stat Modifications" : "Characters with normal vision do not receive any specific stat modifications related to their vision. Their vision is considered the standard baseline for visual perception."
                },
                "Darkvision": {
                    "Possesses" : False
                }
            },
            "Draconic Ancestry": {
                "Description": "Dragonborn characters have an ancestral link to dragons, which influences their breath weapon and damage resistance. They choose a type of dragon as their ancestor, which determines these traits.",
                "Benefit": "Determines type of breath weapon and resistance",
                "Type": "Ancestral Trait",
                "Options": "Chromatic or Metallic dragon types (e.g., Black, Blue, Brass, Bronze, Copper, Gold, Green, Red, Silver, White)"
            },
            "Breath Weapon": {
                "Description": "As part of their draconic heritage, Dragonborn can exhale destructive energy in a specific area. The type (such as fire, cold, acid, etc.) and shape (like a line or cone) of this breath weapon are determined by their Draconic Ancestry.",
                "Type": "Attack Ability",
                "Usage": "Typically once per short or long rest",
                "Determined By": "Draconic Ancestry"
            },
            "Damage Resistance": {
                "Description": "Dragonborn have resistance to the type of damage associated with their draconic ancestry. For example, a Dragonborn with Red dragon ancestry would have resistance to fire damage.",
                "Benefit": "Resistance to a specific type of damage",
                "Type": "Defensive Trait",
                "Determined By": "Draconic Ancestry"
            }
        },
        "Proficiencies": {
            "languages": ["Common", "Draconic"],
            "tools": [],
            "weapons": []
        },
        "Ability Score Increase": {
            'strength': 2,
            'charisma': 1
        }
    },



    "Gnome": {
        "ASCII Art": """
   _____                             
  / ____|                            
 | |  __ _ __   ___  _ __ ___   ___  
 | | |_ | '_ \ / _ \| '_ ` _ \ / _ \ 
 | |__| | | | | (_) | | | | | |  __/ 
  \_____|_| |_|\___/|_| |_| |_|\___| 
                                    
        """,
        "Name" : "Gnome",
        "Description": "A gnome’s energy and enthusiasm for living shines through every inch of their tiny body. Gnomes average slightly over 3 feet tall and weigh 40 to 45 pounds. Their tan or brown faces are usually adorned with broad smiles.",
        "Traits": {
            "Speed" : {
                "Ground" : 25,
                "Flight" : 0
            },
            "Vision": {
                "Normal" : {
                    "Description": "Normal vision is the default vision type for most humanoid characters in the game.",
                    "Range" : "Characters with normal vision typically have a visual range determined by the lighting conditions in the game. In normal daylight or well-lit areas, characters with normal vision can see up to a specific distance without any hindrance. The exact range may vary depending on factors like the time of day, weather, and the DM's discretion.",
                    "Light Sources" : "Characters with normal vision rely on natural or artificial light sources to see in dimly lit or dark areas. If there is insufficient light, they may suffer from the effects of dim light or darkness, which can impose penalties on their ability to see and perceive their surroundings.",
                    "No Special Features" : "Normal vision does not grant any special abilities like darkvision, which allows characters to see in darkness as if it were dim light. Characters with normal vision may require torches, lanterns, or other light sources in dark environments.",
                    "No Stat Modifications" : "Characters with normal vision do not receive any specific stat modifications related to their vision. Their vision is considered the standard baseline for visual perception."
                },
                "Darkvision": {
                    "Possesses" : True,
                    "Description": "Grants the ability to see in dim light within a certain radius as if it were bright light, and in darkness as if it were dim light. This trait allows characters to see in near-total darkness.",
                    "Range": "Typically 60 feet",
                    "Monochromatic": "Able to see in shades of gray without the ability to discern colors."
                }
            },
            "Gnome Cunning": {
                "Description": "Gnome Cunning provides Gnomes with an innate mental fortitude against certain types of magical illusions, as well as against spells and effects that attempt to charm or deceive them. This reflects their inherently quick and perceptive mind, which makes them adept at avoiding magical deceit.",
                "Benefit": "Advantage on all Intelligence, Wisdom, and Charisma saving throws against magic.",
                "Type": "Magical Resistance",
                "Usage": "Applicable against magic that deceives or charms"
            }
        },
        "Proficiencies": {
            "languages": ["Common", "Gnomish"],
            "tools": [],
            "weapons": []
        },
        "Ability Score Increase": {
            'intelligence': 2
        }
    },



    "Half-Elf": {
        "ASCII Art": """
  _    _       _  __      ______ _  __ 
 | |  | |     | |/ _|    |  ____| |/ _|
 | |__| | __ _| | |_ ____| |__  | | |_ 
 |  __  |/ _` | |  _|____|  __| | |  _|
 | |  | | (_| | | |      | |____| | |  
 |_|  |_|\__,_|_|_|      |______|_|_|  
                                           
        """,
        "Name" : "Half-Elf",
        "Description": "Half-elves combine what some say are the best qualities of their elf and human parents. They are as versatile and diverse as humans, while also possessing some of the grace and natural talents of elves.",
        "Traits": {
            "Speed" : {
                "Ground" : 30,
                "Flight" : 0
            },
            "Vision": {
                "Normal" : {
                    "Description": "Normal vision is the default vision type for most humanoid characters in the game.",
                    "Range" : "Characters with normal vision typically have a visual range determined by the lighting conditions in the game. In normal daylight or well-lit areas, characters with normal vision can see up to a specific distance without any hindrance. The exact range may vary depending on factors like the time of day, weather, and the DM's discretion.",
                    "Light Sources" : "Characters with normal vision rely on natural or artificial light sources to see in dimly lit or dark areas. If there is insufficient light, they may suffer from the effects of dim light or darkness, which can impose penalties on their ability to see and perceive their surroundings.",
                    "No Special Features" : "Normal vision does not grant any special abilities like darkvision, which allows characters to see in darkness as if it were dim light. Characters with normal vision may require torches, lanterns, or other light sources in dark environments.",
                    "No Stat Modifications" : "Characters with normal vision do not receive any specific stat modifications related to their vision. Their vision is considered the standard baseline for visual perception."
                },
                "Darkvision": {
                    "Possesses" : False
                }
            },
            "Fey Ancestry": {
                "Description": "This trait reflects the magical heritage of a character, providing them with a natural defense against being charmed. Additionally, magic cannot put them to sleep. It is a manifestation of their elven or other fey lineage, granting them an innate resilience against enchantments and illusions.",
                "Benefit": "Advantage on saving throws against being charmed, immunity to sleep spells and effects",
                "Type": "Magical Resistance"
            },
            "Skill Versatility": {
                "Description": "Skill Versatility allows a character, particularly Half-Elves, to be more adaptable and proficient in a variety of skills. This trait reflects their diverse heritage and experiences, enabling them to acquire proficiency in two skills of their choice.",
                "Benefit": "Proficiency in two skills of the player's choice",
                "Type": "Skill Proficiency",
                "Flexibility": "Choice of any two skills"
            }
        },
        "Proficiencies": {
            "languages": ["Common", "Elvish", "One of player's choice"],
            "tools": [],
            "weapons": []
        },
        "Ability Score Increase": {
            'charisma': 2,
            'random' : 1,
            'random' : 1
        }
    },



    "Half-Orc": {
        "ASCII Art": """
  _    _       _  __       ____           
 | |  | |     | |/ _|     / __ \          
 | |__| | __ _| | |_ ____| |  | |_ __ ___ 
 |  __  |/ _` | |  _|____| |  | | '__/ __|
 | |  | | (_| | | |      | |__| | | | (__ 
 |_|  |_|\__,_|_|_|       \____/|_|  \___|
                                            
        """,
        "Name" : "Half-Orc",
        "Description": "Half-orcs’ grayish pigmentation, sloping foreheads, jutting jaws, prominent teeth, and towering builds make their orcish heritage plain for all to see. They are often the ambassadors between orc and human societies.",
        "Traits": {
            "Speed" : {
                "Ground" : 30,
                "Flight" : 0
            },
            "Vision": {
                "Normal" : {
                    "Description": "Normal vision is the default vision type for most humanoid characters in the game.",
                    "Range" : "Characters with normal vision typically have a visual range determined by the lighting conditions in the game. In normal daylight or well-lit areas, characters with normal vision can see up to a specific distance without any hindrance. The exact range may vary depending on factors like the time of day, weather, and the DM's discretion.",
                    "Light Sources" : "Characters with normal vision rely on natural or artificial light sources to see in dimly lit or dark areas. If there is insufficient light, they may suffer from the effects of dim light or darkness, which can impose penalties on their ability to see and perceive their surroundings.",
                    "No Special Features" : "Normal vision does not grant any special abilities like darkvision, which allows characters to see in darkness as if it were dim light. Characters with normal vision may require torches, lanterns, or other light sources in dark environments.",
                    "No Stat Modifications" : "Characters with normal vision do not receive any specific stat modifications related to their vision. Their vision is considered the standard baseline for visual perception."
                },
                "Darkvision": {
                    "Possesses" : True,
                    "Description": "Grants the ability to see in dim light within a certain radius as if it were bright light, and in darkness as if it were dim light. This trait allows characters to see in near-total darkness.",
                    "Range": "Typically 60 feet",
                    "Monochromatic": "Able to see in shades of gray without the ability to discern colors."
                }
            },
            "Relentless Endurance": {
                "Description": "This trait allows a character to push through injuries that would incapacitate others. When a character with Relentless Endurance would be reduced to 0 hit points but not killed outright, they can instead drop to 1 hit point once per long rest. It reflects their extraordinary grit and determination to stay standing despite grievous harm.",
                "Benefit": "Drop to 1 hit point instead of 0, once per long rest",
                "Type": "Survivability",
                "Usage": "Once per long rest"
            },
            "Savage Attacks": {
                "Description": "When a character lands a critical hit with a melee weapon attack, Savage Attacks allows them to roll one of the weapon’s damage dice one additional time and add it to the extra damage of the critical hit. This trait represents the character's ability to inflict particularly brutal injuries in combat.",
                "Benefit": "Extra damage die on a critical hit with a melee weapon",
                "Type": "Combat Enhancement",
                "Applicability": "Melee weapon critical hits"
            }
        },
        "Proficiencies": {
            "languages": ["Common", "Orc"],
            "tools": [],
            "weapons": ["Greataxes", "Greatswords"]
        },
        "Ability Score Increase": {
            'strength' : 2,
            'constitution' : 1
        }
    },



    "Halfling": {
        "ASCII Art": """
  _    _       _  __ _ _             
 | |  | |     | |/ _| (_)            
 | |__| | __ _| | |_| |_ _ __   __ _ 
 |  __  |/ _` | |  _| | | '_ \ / _` |
 | |  | | (_| | | | | | | | | | (_| |
 |_|  |_|\__,_|_|_| |_|_|_| |_|\__, |
                                __/ |
                               |___/ 
        """,
        "Name" : "Halfling",
        "Description": "The diminutive halflings survive in a world full of larger creatures by avoiding notice or, barring that, avoiding offense. They are adept at fitting into a community of humans, dwarves, or elves, making themselves valuable and welcome.",
        "Traits": {
            "Speed" : {
                "Ground" : 25,
                "Flight" : 0
            },
            "Vision": {
                "Normal" : {
                    "Description": "Normal vision is the default vision type for most humanoid characters in the game.",
                    "Range" : "Characters with normal vision typically have a visual range determined by the lighting conditions in the game. In normal daylight or well-lit areas, characters with normal vision can see up to a specific distance without any hindrance. The exact range may vary depending on factors like the time of day, weather, and the DM's discretion.",
                    "Light Sources" : "Characters with normal vision rely on natural or artificial light sources to see in dimly lit or dark areas. If there is insufficient light, they may suffer from the effects of dim light or darkness, which can impose penalties on their ability to see and perceive their surroundings.",
                    "No Special Features" : "Normal vision does not grant any special abilities like darkvision, which allows characters to see in darkness as if it were dim light. Characters with normal vision may require torches, lanterns, or other light sources in dark environments.",
                    "No Stat Modifications" : "Characters with normal vision do not receive any specific stat modifications related to their vision. Their vision is considered the standard baseline for visual perception."
                },
                "Darkvision": {
                    "Possesses" : False
                }
            },
            "Lucky": {
                "Description": "The Lucky trait allows a Halfling to reroll a 1 on any attack roll, ability check, or saving throw. The new roll must be used, even if it is another 1. This trait represents the Halfling’s inherent luck, turning potential failures into new opportunities.",
                "Benefit": "Reroll if you roll a 1 on attack rolls, ability checks, or saving throws",
                "Type": "Luck",
                "Usage": "Every time a 1 is rolled"
            },
            "Brave": {
                "Description": "Halflings have an innate courage and are surprisingly brave for their size. This trait gives them an advantage on saving throws against being frightened, helping them stand their ground in the face of terrifying threats.",
                "Benefit": "Advantage on saving throws against being frightened",
                "Type": "Courage",
                "Usage": "Applicable in frightening situations"
            },
            "Halfling Nimbleness": {
                "Description": "Halflings are agile and can move through the space of any creature that is of a size larger than theirs. This trait represents their ability to nimbly navigate around others, especially in combat or crowded situations.",
                "Benefit": "Move through the space of larger creatures",
                "Type": "Agility",
                "Applicability": "In movement, particularly in combat or tight spaces"
            }
        },
        "Proficiencies": {
            "languages": ["Common", "Halfling"],
            "tools": [],
            "weapons": []
        },
        "Ability Score Increase": {
            'dexterity': 2
        }
    },



    "Human": {
        "ASCII Art": """
  _    _                             
 | |  | |                            
 | |__| |_   _ _ __ ___   __ _ _ __  
 |  __  | | | | '_ ` _ \ / _` | '_ \ 
 | |  | | |_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_| |_|\__,_|_| |_|
                                     
        """,
        "Name" : "Human",
        "Description": "Humans are the most adaptable and ambitious people among the common races. Whatever drives them, humans are the innovators, the achievers, and the pioneers of the worlds.",
        "Traits": {
            "Speed" : {
                "Ground" : 30,
                "Flight" : 0
            },
            "Vision": {
                "Normal" : {
                    "Description": "Normal vision is the default vision type for most humanoid characters in the game.",
                    "Range" : "Characters with normal vision typically have a visual range determined by the lighting conditions in the game. In normal daylight or well-lit areas, characters with normal vision can see up to a specific distance without any hindrance. The exact range may vary depending on factors like the time of day, weather, and the DM's discretion.",
                    "Light Sources" : "Characters with normal vision rely on natural or artificial light sources to see in dimly lit or dark areas. If there is insufficient light, they may suffer from the effects of dim light or darkness, which can impose penalties on their ability to see and perceive their surroundings.",
                    "No Special Features" : "Normal vision does not grant any special abilities like darkvision, which allows characters to see in darkness as if it were dim light. Characters with normal vision may require torches, lanterns, or other light sources in dark environments.",
                    "No Stat Modifications" : "Characters with normal vision do not receive any specific stat modifications related to their vision. Their vision is considered the standard baseline for visual perception."
                },
                "Darkvision": {
                    "Possesses" : False
                }
            }            
        },
        "Proficiencies": {
            "languages": ["Common", "One of player's choice"],
            "tools": [],
            "weapons": []
        },
        "Ability Score Increase": {
            'strength' : 1,
            'dexterity' : 1,
            'constitution' : 1,
            'intelligence' : 1,
            'wisdom' : 1,
            'charisma' : 1
        }
    },



    "Tiefling": {
        "ASCII Art": """
  _______ _       __ _ _             
 |__   __(_)     / _| (_)            
    | |   _  ___| |_| |_ _ __   __ _ 
    | |  | |/ _ \  _| | | '_ \ / _` |
    | |  | |  __/ | | | | | | | (_| |
    |_|  |_|\___|_| |_|_|_| |_|\__, |
                                __/ |
                               |___/ 
        """,
        "Name" : "Tiefling",
        "Description": "To be greeted with stares and whispers, to suffer violence and insult on the street, to see mistrust and fear in every eye: this is the lot of the tiefling. They have infernal heritage and bear the physical marks of their lineage.",
        "Traits": {
            "Speed" : {
                "Ground" : 30,
                "Flight" : 0
            },
            "Vision": {
                "Normal" : {
                    "Description": "Normal vision is the default vision type for most humanoid characters in the game.",
                    "Range" : "Characters with normal vision typically have a visual range determined by the lighting conditions in the game. In normal daylight or well-lit areas, characters with normal vision can see up to a specific distance without any hindrance. The exact range may vary depending on factors like the time of day, weather, and the DM's discretion.",
                    "Light Sources" : "Characters with normal vision rely on natural or artificial light sources to see in dimly lit or dark areas. If there is insufficient light, they may suffer from the effects of dim light or darkness, which can impose penalties on their ability to see and perceive their surroundings.",
                    "No Special Features" : "Normal vision does not grant any special abilities like darkvision, which allows characters to see in darkness as if it were dim light. Characters with normal vision may require torches, lanterns, or other light sources in dark environments.",
                    "No Stat Modifications" : "Characters with normal vision do not receive any specific stat modifications related to their vision. Their vision is considered the standard baseline for visual perception."
                },
                "Darkvision": {
                    "Possesses" : True,
                    "Description": "Grants the ability to see in dim light within a certain radius as if it were bright light, and in darkness as if it were dim light. This trait allows characters to see in near-total darkness.",
                    "Range": "Typically 60 feet",
                    "Monochromatic": "Able to see in shades of gray without the ability to discern colors."
                }
            },
            "Hellish Resistance": {
                "Description": "This trait gives Tieflings resistance to fire damage, a reflection of their infernal heritage. It symbolizes their innate ability to withstand fiery environments and effects, a legacy from their fiendish ancestors.",
                "Benefit": "Resistance to fire damage",
                "Type": "Elemental Resistance"
            },
            "Infernal Legacy": {
                "Description": "Infernal Legacy grants Tieflings the ability to cast certain spells as innate magical abilities. At the start, they can cast the Thaumaturgy cantrip. At higher levels, this trait allows them to cast spells like Hellish Rebuke and Darkness, usually once per day, with Charisma as their spellcasting ability.",
                "Benefit": "Access to specific spells without expending spell slots (Thaumaturgy, Hellish Rebuke, Darkness)",
                "Type": "Innate Spellcasting",
                "Spellcasting Ability": "Charisma",
                "Usage": "Varies (e.g., Thaumaturgy at will, others once per day)"
            }
        },
        "Proficiencies": {
            "languages": ["Common", "Infernal"],
            "tools": [],
            "weapons": []
        },
        "Ability Score Increase": {
            'charisma' : 2,
            'intelligence' : 1
        },
    }
}


