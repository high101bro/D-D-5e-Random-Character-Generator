#! /usr/bin/env python3

import random

dnd_backgrounds = {
    "Acolyte": {
        "Name": "Acolyte",
        "Source": "Dnd 5e Player's Handbook",
        "Details": "You are devoted to a deity or a religious life, serving a temple or religious community.",
        "Features": "Shelter of the Faithful - Gain support from religious communities.",
        "Skill Proficiencies": ["insight", "religion"],
        "Tool Proficiencies": ['None'],
        "Languages": ['Common',"Two of your choice"],
        "Equipment": "Holy symbol, prayer book, 5 sticks of incense, vestments, common clothes, 15 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I idolize a particular hero of my faith and constantly refer to their deeds and example.",
            "Ideal": "Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld.",
            "Bond": "I will do anything to protect my temple.",
            "Flaw": "I am inflexible in my thinking."
        }
    },
    "Baker": {
        "Name": "Baker",
        "Source": "Custom",
        "Details": "You have spent much of your life baking, creating breads, pastries, and other delights.",
        "Features": "Baker's Delight",
        "Skill Proficiencies": ["investigation", "nature"],
        "Tool Proficiencies": ["Baker's tools", "Cook's utensils"],
        "Languages": ['Common'],
        "Equipment": "A set of baker's tools, a set of common clothes stained with flour, a loaf of fresh bread, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I rise early and am used to the morning hours.",
            "Ideal": "Nourishment. Good food brings comfort and happiness.",
            "Bond": "I inherited my recipes from a beloved mentor, and they are precious to me.",
            "Flaw": "I am very particular about my ingredients and workspace."
        }
    },
    "Blacksmith": {
        "Name": "Blacksmith",
        "Source": "Custom",
        "Details": "You have honed your skills in the forge, crafting items from metal and repairing them.",
        "Features": "Smith's Intuition",
        "Skill Proficiencies": ["athletics", "investigation"],
        "Tool Proficiencies": ["Smith's tools", "Vehicles (land)"],
        "Languages": ['Common'],
        "Equipment": "A set of common clothes, a smith's hammer, a block of metal, smith's tools, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am meticulous and precise in my work.",
            "Ideal": "Creation. The act of creation, of making something lasting, is what drives me.",
            "Bond": "My work is a testament to my skills, and I strive to make each piece better than the last.",
            "Flaw": "I can be a bit of a perfectionist, often at the expense of time and social interactions."
        }
    },    
    "Charlatan": {
        "Name": "Charlatan",
        "Source": "Dnd 5e Player's Handbook",
        "Details": "You have always had a way with people. You know what makes them tick, and you can tease out their heart's desires after a few minutes of conversation.",
        "Features": "False Identity",
        "Skill Proficiencies": ["deception", "sleight of hand"],
        "Tool Proficiencies": ["Disguise kit", "Forgery kit"],
        "Languages": ['Common'],
        "Equipment": "A set of fine clothes, a disguise kit, tools of the con of your choice (ten stoppered bottles filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an imaginary duke), and a belt pouch containing 15 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I fall in and out of love easily, and am always pursuing someone.",
            "Ideal": "Independence. I am a free spirit—no one tells me what to do.",
            "Bond": "I fleeced the wrong person and must work to ensure that this individual never crosses paths with me or those I care about.",
            "Flaw": "I can't resist a pretty face."
        }
    },
    "Criminal": {
        "Name" : "Criminal",
        "Source": "Dnd 5e Player's Handbook",
        "Details": "You've a past filled with crime, possibly still mingling with thieves and rogues.",
        "Features": "Criminal Contact - You have a reliable and trustworthy contact in the criminal underworld.",
        "Skill Proficiencies": ["deception", "stealth"],
        "Tool Proficiencies": ["One type of gaming set", "Thieves' tools"],
        "Languages": ['Common'],
        "Equipment": "Crowbar, set of dark common clothes including a hood, 15 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I always have a plan for what to do when things go wrong.",
            "Ideal": "Freedom. Chains are meant to be broken, as are those who would forge them.",
            "Bond": "I'm trying to pay off an old debt I owe to a generous benefactor.",
            "Flaw": "When I see something valuable, I can't think about anything but how to steal it."
        }
    },
    "Entertainer": {
        "Name" : "Entertainer",
        "Source": "Dnd 5e Player's Handbook",
        "Details": "You thrive in front of an audience. You are a musician, a poet, a jester, a storyteller, or some other kind of performer.",
        "Features": "By Popular Demand",
        "Skill Proficiencies": ["acrobatics", "performance"],
        "Tool Proficiencies": ["Disguise kit", "One type of musical instrument"],
        "Languages": ['Common'],
        "Equipment": "A musical instrument, the favor of an admirer, a costume, a set of common clothes, and a belt pouch containing 15 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I know a story relevant to almost every situation.",
            "Ideal": "Creativity. The world is in need of new ideas and bold action.",
            "Bond": "I will do anything to prove myself superior to my hated rival.",
            "Flaw": "I’m a sucker for a pretty face."
        }
    },
    "Farmer": {
        "Name" : "Farmer",
        "Source": "Custom",
        "Details": "You have spent a significant portion of your life working the land, tending to crops and livestock.",
        "Features": "Rustic Hospitality",
        "Skill Proficiencies": ["animal handling", "nature"],
        "Tool Proficiencies": ["Vehicles (land)", "One type of artisan's tools related to farming"],
        "Languages": ['Common'],
        "Equipment": "A set of common clothes, a shovel, an iron pot, a hat or other piece of headwear, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am most at peace when I am working the land.",
            "Ideal": "Hard Work. Honest labor brings honest rewards.",
            "Bond": "My land and my crops are everything to me.",
            "Flaw": "I am stubborn and set in my ways."
        }
    },    
    "Folk Hero": {
        "Name" : "Folk Hero",
        "Source": "Dnd 5e Player's Handbook",
        "Details": "You come from a humble social rank, but you are destined for so much more. Already the people of your home village regard you as their champion.",
        "Features": "Rustic Hospitality",
        "Skill Proficiencies": ["animal handling", "survival"],
        "Tool Proficiencies": ["One type of artisan's tools", "Vehicles (land)"],
        "Languages": ['Common'],
        "Equipment": "A set of artisan's tools, a shovel, an iron pot, common clothes, 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I judge people by their actions, not their words.",
            "Ideal": "Sincerity. There’s no good in pretending to be something I’m not.",
            "Bond": "I protect those who cannot protect themselves.",
            "Flaw": "I have a weakness for the vices of the city, especially hard drink."
        }
    },
    "Guild Artisan": {
        "Name" : "Guild Artisan",
        "Source": "Dnd 5e Player's Handbook",
        "Details": "You are a member of an artisan’s guild, skilled in a particular craft, and closely associated with other artisans.",
        "Features": "Guild Membership",
        "Skill Proficiencies": ["insight", "persuasion"],
        "Tool Proficiencies": ["One type of artisan's tools"],
        "Languages": ['Common',"One of your choice"],
        "Equipment": "A set of artisan's tools, a letter of introduction from your guild, a set of traveler’s clothes, and a belt pouch containing 15 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I believe that anything worth doing is worth doing right.",
            "Ideal": "Community. It is the duty of all civilized people to strengthen the bonds of community and the security of civilization.",
            "Bond": "The workshop where I learned my trade is the most important place in the world to me.",
            "Flaw": "I’ll do anything to get my hands on something rare or priceless."
        }
    },
    "Hermit": {
        "Name" : "Hermit",
        "Source": "Dnd 5e Player's Handbook",
        "Details": "You have lived in seclusion, away from the bustling societies, either in a sheltered community such as a monastery or entirely alone.",
        "Features": "Discovery",
        "Skill Proficiencies": ["medicine", "religion"],
        "Tool Proficiencies": ["Herbalism kit"],
        "Languages": ['Common',"One of your choice"],
        "Equipment": "A scroll case stuffed full of notes from your studies or prayers, a winter blanket, a set of common clothes, a herbalism kit, and 5 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I often get lost in my own thoughts and contemplation, becoming oblivious to my surroundings.",
            "Ideal": "Self-Knowledge. If you know yourself, there’s nothing left to know.",
            "Bond": "I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them.",
            "Flaw": "Now that I've returned to the world, I enjoy its delights a little too much."
        }
    },
    "Hunter": {
        "Name" : "Hunter",
        "Source": "Custom",
        "Details": "You have lived in the wilderness, relying on your skills in tracking and hunting for survival.",
        "Features": "Tracker's Eye",
        "Skill Proficiencies": ["survival", "stealth"],
        "Tool Proficiencies": ["One type of gaming set", "Vehicles (land)"],
        "Languages": ['Common'],
        "Equipment": "A set of traveler's clothes, a hunting trap, a trophy from an animal you killed, a set of common clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am patient and observant, a predator waiting for the perfect moment.",
            "Ideal": "Balance. nature teaches us that balance must be maintained.",
            "Bond": "I hunt not just for food, but to protect the wilderness.",
            "Flaw": "I have little respect for those who do not understand or respect nature."
        }
    },    
    "Innkeeper": {
        "Name" : "InnKeeper",
        "Source": "Custom",
        "Details": "You have managed an inn, tavern, or similar establishment, providing a place of rest and nourishment for travelers.",
        "Features": "Hospitality",
        "Skill Proficiencies": ["insight", "persuasion"],
        "Tool Proficiencies": ["Cook's utensils", "Brewer's supplies"],
        "Languages": ['Common'],
        "Equipment": "A set of common clothes, a ledger, a key to your establishment, cook's utensils, and a belt pouch containing 15 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I have a story for every occasion.",
            "Ideal": "Community. It's the duty of all to help others, especially travelers in need.",
            "Bond": "My establishment is my life, and I'll do anything to protect it and my patrons.",
            "Flaw": "I'm a notorious gossip."
        }
    },
    "Knight": {
        "Name" : "Knight",
        "Source": "Custom",
        "Details": "You have been granted a knighthood. You might be a minor scion of a noble house, or perhaps you earned your title on the battlefield.",
        "Features": "Retainers",
        "Skill Proficiencies": ["history", "persuasion"],
        "Tool Proficiencies": ["One type of gaming set", "Vehicles (land)"],
        "Languages": ['Common'],
        "Equipment": "A set of fine clothes, a signet ring, a scroll of pedigree, and a purse containing 25 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "My flattery makes those I talk to feel wonderful and important.",
            "Ideal": "Respect. People deserve to be treated with dignity and respect.",
            "Bond": "The common folk must see me as a hero of the realm.",
            "Flaw": "The monstrous enemy we faced in battle still leaves me quivering with fear."
        }
    },
    "Merchant": {
        "Name" : "Merchant",
        "Source": "Custom",
        "Details": "You have spent your life in the pursuit of commerce, trading goods across the land or even across seas.",
        "Features": "Deal Maker",
        "Skill Proficiencies": ["persuasion", "insight"],
        "Tool Proficiencies": ["One type of artisan's tools related to your goods", "Vehicles (land or water)"],
        "Languages": ['Common',"One of your choice"],
        "Equipment": "A set of common clothes, an abacus, a sample of goods, a ledger, and a belt pouch containing 15 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I can haggle prices with the best of them.",
            "Ideal": "Wealth. The accumulation of wealth allows for a comfortable and influential life.",
            "Bond": "I will go to great lengths to protect my trading network.",
            "Flaw": "I am obsessed with making the next big deal."
        }
    },
    "Miner": {
        "Name" : "Miner",
        "Source": "Custom",
        "Details": "You have spent years working in mines, extracting minerals and ores from the earth.",
        "Features": "Stone Knowledge",
        "Skill Proficiencies": ["athletics", "survival"],
        "Tool Proficiencies": ["Pickaxe", "Vehicles (land)"],
        "Languages": ['Common'],
        "Equipment": "A pickaxe, a miner's helmet, a set of common clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am used to hard labor and long hours of work.",
            "Ideal": "Persistence. Hard work always pays off.",
            "Bond": "The mine where I worked is my second home.",
            "Flaw": "I am uncomfortable in open spaces and feel exposed and vulnerable."
        }
    },    
    "Noble": {
        "Name" : "Noble",
        "Source": "Dnd 5e Player's Handbook",
        "Details": "You understand wealth, power, and privilege. You carry a noble title, and your family owns land, collects taxes, and wields significant political influence.",
        "Features": "Position of Privilege",
        "Skill Proficiencies": ["history", "persuasion"],
        "Tool Proficiencies": ["One type of gaming set"],
        "Languages": ['Common',"One of your choice"],
        "Equipment": "A set of fine clothes, a signet ring, a scroll of pedigree, a purse containing 25 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world.",
            "Ideal": "Respect. Respect is due to me because of my position, but all people regardless of station deserve to be treated with dignity.",
            "Bond": "The common folk must see me as a hero of the people.",
            "Flaw": "In fact, the world does revolve around me."
        }
    },
    "Outlander": {
        "Name" : "Outlander",
        "Source": "Dnd 5e Player's Handbook",
        "Details": "You grew up in the wilds, far from civilization and the comforts of town and technology.",
        "Features": "Wanderer",
        "Skill Proficiencies": ["athletics", "survival"],
        "Tool Proficiencies": ["One type of musical instrument"],
        "Languages": ['Common',"One of your choice"],
        "Equipment": "A staff, a hunting trap, a trophy from an animal you killed, a set of traveler's clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I’m driven by a wanderlust that led me away from home.",
            "Ideal": "Nature. The natural world is more important than all the constructs of civilization.",
            "Bond": "An injury to the unspoiled wilderness of my home is an injury to me.",
            "Flaw": "I am too enamored of ale, wine, and other intoxicants."
        }
    },
    "Pirate": {
        "Name" : "Pirate",
        "Source": "Custom",
        "Details": "You spent your youth under the sway of a dread pirate, a ruthless cutthroat who taught you how to survive in a world of sharks and savages.",
        "Features": "Bad Reputation",
        "Skill Proficiencies": ["athletics", "perception"],
        "Tool Proficiencies": ["Navigator's tools", "Vehicles (water)"],
        "Languages": ['Common'],
        "Equipment": "A belaying pin (club), 50 feet of silk rope, a lucky charm or a trinket from your piracy days, a set of common clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I stretch the truth for the sake of a good story.",
            "Ideal": "Freedom. The sea is freedom—the freedom to go anywhere and do anything.",
            "Bond": "I'll always remember my first ship.",
            "Flaw": "Once someone questions my courage, I never back down no matter how dangerous the situation."
        }
    },    
    "Sailor": {
        "Name" : "Sailor",
        "Source": "Dnd 5e Player's Handbook",
        "Details": "You have spent your life on the seas, aboard a ship, facing the dangers of waves and wind.",
        "Features": "Ship's Passage",
        "Skill Proficiencies": ["athletics", "perception"],
        "Tool Proficiencies": ["Navigator's tools", "Vehicles (water)"],
        "Languages": ['Common'],
        "Equipment": "A belaying pin (club), 50 feet of silk rope, a lucky charm, a set of common clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I work hard so that I can play hard when the work is done.",
            "Ideal": "Respect. The thing that keeps a ship together is mutual respect between captain and crew.",
            "Bond": "I was cheated out of my fair share of the profits, and I want to get my due.",
            "Flaw": "I follow orders, even if I think they’re wrong."
        }
    },
    "Sage": {
        "Name" : "Sage",
        "Source": "Dnd 5e Player's Handbook",
        "Details": "You spent years learning the lore of the multiverse. You scoured manuscripts, studied scrolls, and listened to the greatest experts on the subjects that interest you.",
        "Features": "Researcher",
        "Skill Proficiencies": ["arcana", "history"],
        "Tool Proficiencies": ['None'],
        "Languages": ['Common',"Two of your choice"],
        "Equipment": "A bottle of black ink, a quill, a small knife, a letter from a dead colleague posing a question you have not yet been able to answer, a set of common clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I use polysyllabic words that convey the impression of great erudition.",
            "Ideal": "Knowledge. The path to power and self-improvement is through knowledge.",
            "Bond": "I've been searching my whole life for the answer to a certain question.",
            "Flaw": "I am easily distracted by the promise of information."
        }
    },
    "Scribe": {
        "Name" : "Scribe",
        "Source": "Custom",
        "Details": "You have spent years copying and studying texts, working as a scribe for a library, a private individual, or a guild.",
        "Features": "Lore of the Scribe",
        "Skill Proficiencies": ["history", "investigation"],
        "Tool Proficiencies": ["Calligrapher's supplies"],
        "Languages": ['Common',"Two of your choice"],
        "Equipment": "A bottle of black ink, a quill, a small knife, a letter from a former client asking a question you have not yet been able to answer, a set of common clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am meticulous and methodical in my work and life.",
            "Ideal": "Knowledge. The preservation and dissemination of knowledge is the key to progress.",
            "Bond": "I have an ancient text that holds terrible secrets that must not fall into the wrong hands.",
            "Flaw": "I am easily lost in my work, forgetting everything else."
        }
    },    
    "Soldier": {
        "Name" : "Soldier",
        "Source": "Dnd 5e Player's Handbook",
        "Details": "You have served in an army, learning the ways of war. You might have been part of a standing army or a local militia, or perhaps a mercenary company.",
        "Features": "Military Rank",
        "Skill Proficiencies": ["athletics", "intimidation"],
        "Tool Proficiencies": ["One type of gaming set", "Vehicles (land)"],
        "Languages": ['Common'],
        "Equipment": "An insignia of rank, trophies from fallen enemies, a set of bone dice or deck of cards, a set of common clothes, and a pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I’m always polite and respectful.",
            "Ideal": "Greater Good. Our lot is to lay down our lives in defense of others.",
            "Bond": "I’ll never forget the crushing defeat my company suffered or the enemies who dealt it.",
            "Flaw": "I’d rather eat my armor than admit when I’m wrong."
        }
    },
    "Tailor": {
        "Name" : "Tailor",
        "Source": "Custom",
        "Details": "You have a knack for creating and altering clothing, working with fine fabrics and designs.",
        "Features": "Eye for Detail",
        "Skill Proficiencies": ["persuasion", "performance"],
        "Tool Proficiencies": ["Tailor's tools"],
        "Languages": ['Common'],
        "Equipment": "A set of tailor's tools, a fine outfit of your own creation, a bolt of fine fabric, and a belt pouch containing 15 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I can't help but measure and assess everyone I meet.",
            "Ideal": "Beauty. Beauty is in every stitch and seam.",
            "Bond": "I created a masterpiece garment that I will never part with.",
            "Flaw": "I am overly critical of others' appearances."
        }
    },
    "Urchin": {
        "Name" : "Urchin",
        "Source": "Dnd 5e Player's Handbook",
        "Details": "You grew up on the streets, alone, orphaned, and poor, learning to fend for yourself.",
        "Features": "City Secrets",
        "Skill Proficiencies": ["sleight of hand", "stealth"],
        "Tool Proficiencies": ["Disguise kit", "Thieves’ tools"],
        "Languages": ['Common'],
        "Equipment": "A small knife, a map of the city you grew up in, a pet mouse, a token to remember your parents by, a set of common clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I hide scraps of food and trinkets away in my pockets.",
            "Ideal": "Retribution. I steal from the wealthy so that I can help people in need.",
            "Bond": "I owe everything to my mentor – a horrible person who’s probably rotting in jail somewhere.",
            "Flaw": "If I'm outnumbered, I will run away from a fight."
        }
    },
    'Skyship Captain': {
        "Name": 'Skyship Captain',
        'Details': "You've risen to the rank of captain in the adventurous world of sky piracy, commanding a formidable airship.",
        "Features": 'Aerial Command',
        "Skill Proficiencies": ['Persuasion', 'Navigation'],
        "Tool Proficiencies": ['Navigator\'s tools', 'Cartographer\'s tools'],
        "Languages": ['Common','Auran'],
        "Equipment": 'Captain\'s coat, a set of airship blueprints, a compass, a telescope, and a belt pouch containing 10 gp',
        'Roleplaying Suggestions': {
            'Personality Trait': 'I exude confidence and authority when leading my crew.',
            'Ideal': 'Freedom. The skies are my domain, and I\'ll defend it against all who seek to control it.',
            'Bond': 'My airship is my home, and I\'ll protect my crew like family.',
            'Flaw': 'I\'m always tempted by the allure of new treasures and relics.'
        }
    },
    'Planar Traveler': {
        "Name": 'Planar Traveler',
        'Details': 'You\'ve explored the multiverse, hopping between planes of existence and uncovering their mysteries.',
        "Features": 'Planar Insight',
        "Skill Proficiencies": ['Arcana', 'Religion'],
        "Tool Proficiencies": ['Astrologer\'s tools', 'Planar map'],
        "Languages": ['Common','Primordial'],
        "Equipment": 'Multicolored robes, a small crystal from an unknown plane, a planar compass, a journal, and a belt pouch containing 10 gp',
        'Roleplaying Suggestions': {
            'Personality Trait': 'I\'m endlessly curious about the secrets of other planes.',
            'Ideal': 'Discovery. Knowledge of other realms enriches our understanding of the universe.',
            'Bond': 'I seek to return to a plane I stumbled upon accidentally, but its location remains a mystery.',
            'Flaw': 'I can be distant and detached from the concerns of the Material Plane.'
        }
    },
    'Celestial Scholar': {
        "Name": 'Celestial Scholar',
        'Details': 'You\'ve dedicated your life to studying the celestial realms, seeking to understand the divine and their influence on mortals.',
        "Features": 'Celestial Insights',
        "Skill Proficiencies": ['Arcana', 'Insight'],
        "Tool Proficiencies": ['Celestial texts', 'Holy symbols'],
        "Languages": ['Common','Celestial'],
        "Equipment": 'Elaborate celestial robes, a holy relic, a set of celestial scrolls, a quill, and a belt pouch containing 10 gp',
        'Roleplaying Suggestions': {
            'Personality Trait': 'I radiate a sense of calm and divine understanding.',
            'Ideal': 'Enlightenment. The celestial realms hold the key to greater wisdom and harmony.',
            'Bond': 'I\'m on a quest to uncover the long-lost celestial artifact, rumored to hold immense power.',
            'Flaw': 'I can be overly dogmatic, believing my insights are infallible.'
        }
    },
    'Archaeological Historian': {
        "Name": 'Archaeological Historian',
        'Details': 'Your passion lies in unearthing ancient relics and deciphering the secrets of forgotten civilizations.',
        "Features": 'Relic Expertise',
        "Skill Proficiencies": ['History', 'Investigation'],
        "Tool Proficiencies": ['Archaeologist\'s tools', 'Ancient Language Translation Book'],
        "Languages": ['Common','Ancient'],
        "Equipment": 'Dusty explorer\'s attire, an ancient artifact, a magnifying glass, excavation tools, and a belt pouch containing 10 gp',
        'Roleplaying Suggestions': {
            'Personality Trait': 'I\'m always eager to share fascinating historical tidbits.',
            'Ideal': 'Preservation. History must be protected, and its stories must be told.',
            'Bond': 'I seek the legendary lost city, said to be filled with untold treasures and knowledge.',
            'Flaw': 'I can become obsessed with uncovering the truth, sometimes at the expense of personal safety.'
        }
    },
    'Cursed Artisan': {
        "Name": 'Cursed Artisan',
        'Details': 'Your craft is tainted by a mysterious curse, granting you unnatural abilities but at a steep price.',
        "Features": 'Cursed Craft',
        "Skill Proficiencies": ['Arcana', 'Crafting'],
        "Tool Proficiencies": ['Artisan\'s tools (related to your craft)'],
        "Languages": ['Common','Infernal'],
        "Equipment": 'A cursed crafting tool, a piece of your own cursed creation, a dark hooded cloak, a set of common clothes, and a belt pouch containing 10 gp',
        'Roleplaying Suggestions': {
            'Personality Trait': 'I carry the weight of my curse in every step.',
            'Ideal': 'Redemption. I seek a way to lift my curse and use my craft for good.',
            'Bond': 'I must find the origin of my curse and confront the entity responsible.',
            'Flaw': 'The curse sometimes takes control, pushing me to create malevolent items.'
        }
    },
    'Gourmet Chef': {
        "Name": "Gourmet Chef",
        "Source": "Custom",
        "Details": "You are a culinary master, known for your exquisite dishes and culinary expertise.",
        "Features": "Master of Cuisine",
        "Skill Proficiencies": ["Cooking", "Persuasion"],
        "Tool Proficiencies": ["Cook's utensils"],
        "Languages": ['Common'],
        "Equipment": "A set of fine chef's utensils, a cookbook of your own creation, a signature dish, a chef's hat, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I take immense pride in my culinary creations.",
            "Ideal": "Artistry. Cooking is an art form, and I'm its master.",
            "Bond": "My culinary mentor taught me everything, and I'll honor their legacy.",
            "Flaw": "I can be overly critical of others' cooking."
        }
    },

    'Shadowy Infiltrator': {
        "Name": "Shadowy Infiltrator",
        "Source": "Custom",
        "Details": "You are a master of stealth and espionage, skilled in infiltrating the most secure locations.",
        "Features": "Shadowstep",
        "Skill Proficiencies": ["Stealth", "Deception"],
        "Tool Proficiencies": ["Thieves' tools", "Disguise kit"],
        "Languages": ['Common'],
        "Equipment": "A set of dark, nondescript clothing, a mask of your own design, a lockpick, a concealed weapon, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am always aware of my surroundings, even in the darkest corners.",
            "Ideal": "Freedom. The shadows are my allies, and I'll use them to protect it.",
            "Bond": "I have a secret mission that must be completed at all costs.",
            "Flaw": "I find it hard to trust others completely."
        }
    },

    'Dreamweaver': {
        "Name": "Dreamweaver",
        "Source": "Custom",
        "Details": "You possess the rare ability to enter and shape dreams, wielding the power of the subconscious.",
        "Features": "Dream Manipulator",
        "Skill Proficiencies": ["Insight", "Arcana"],
        "Tool Proficiencies": ["One musical instrument of your choice"],
        "Languages": ['Common'],
        "Equipment": "A dreamcatcher amulet, a book of dream interpretations, a small vial of sand from the ethereal plane, a set of traveler's clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I have a mystical aura that draws people in.",
            "Ideal": "Empathy. I use my powers to heal the emotional wounds of others.",
            "Bond": "I seek to uncover the meaning behind a recurring, enigmatic dream.",
            "Flaw": "The line between dreams and reality can blur for me."
        }
    },

    'Beast Tamer': {
        "Name": "Beast Tamer",
        "Source": "Custom",
        "Details": "You have a deep connection with the animal kingdom, able to communicate and form bonds with even the wildest creatures.",
        "Features": "Animal Kinship",
        "Skill Proficiencies": ["Animal Handling", "Survival"],
        "Tool Proficiencies": ["Herbalism kit", "Animal training tools"],
        "Languages": ['Common'],
        "Equipment": "A token of your favorite animal companion, a pouch of rare animal treats, a cloak of animal hides, a set of wilderness clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "Animals seem to trust me instinctively.",
            "Ideal": "Harmony. The natural world should be protected and preserved.",
            "Bond": "I share a unique bond with a legendary beast, and I must protect it.",
            "Flaw": "I sometimes prefer the company of animals to people."
        }
    },

    'Potion Alchemist': {
        "Name": "Potion Alchemist",
        "Source": "Custom",
        "Details": "You are a skilled alchemist, brewing concoctions with various effects, from healing to destruction.",
        "Features": "Alchemy Mastery",
        "Skill Proficiencies": ["Alchemy", "Medicine"],
        "Tool Proficiencies": ["Alchemist's supplies"],
        "Languages": ['Common'],
        "Equipment": "A set of alchemist's tools, a vial of a mysterious elixir, a mortar and pestle, a collection of rare herbs, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I'm always experimenting with new potions and concoctions.",
            "Ideal": "Knowledge. Alchemy holds the secrets of the universe, and I must unlock them.",
            "Bond": "I seek to discover the recipe for the ultimate, legendary potion.",
            "Flaw": "I can be a bit absent-minded, forgetting important details."
        }
    },
    'Elemental Acolyte': {
        "Name": "Elemental Acolyte",
        "Source": "Custom",
        "Details": "You have devoted your life to the study and worship of the elemental forces that shape the world.",
        "Features": "Elemental Attunement",
        "Skill Proficiencies": ["Arcana", "Nature"],
        "Tool Proficiencies": ['None'],
        "Languages": ['Common'],
        "Equipment": "A sacred symbol representing your chosen elemental affinity, a vial of purified elemental essence, a set of simple robes, a tome of elemental teachings, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I have a deep reverence for the natural world and its elemental forces.",
            "Ideal": "Balance. Harmony between the elements is the key to peace.",
            "Bond": "I seek to unravel the mysteries of the elemental planes.",
            "Flaw": "I can be overly absorbed in my studies, oblivious to the world around me."
        }
    },

    'Circus Performer': {
        "Name": "Circus Performer",
        "Source": "Custom",
        "Details": "You are a skilled performer, dazzling audiences with your acrobatics, tricks, and showmanship.",
        "Features": "Showstopper",
        "Skill Proficiencies": ["Acrobatics", "Performance"],
        "Tool Proficiencies": ["Disguise kit"],
        "Languages": ['Common'],
        "Equipment": "A set of colorful performance attire, a collection of juggling balls and props, a mask or face paint, a circus poster featuring your act, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I thrive in the spotlight and love to make people smile.",
            "Ideal": "Joy. Laughter and entertainment bring happiness to the world.",
            "Bond": "The circus is my family, and I'll do anything to protect it.",
            "Flaw": "I can't resist showing off, even in inappropriate situations."
        }
    },

    'Spirit Medium': {
        "Name": "Spirit Medium",
        "Source": "Custom",
        "Details": "You have the ability to communicate with spirits and the ethereal realm, serving as a bridge between the living and the dead.",
        "Features": "Ethereal Connection",
        "Skill Proficiencies": ["Religion", "Insight"],
        "Tool Proficiencies": ["Spiritual focus (crystal ball, tarot cards, etc.)"],
        "Languages": ['Common'],
        "Equipment": "A spiritual focus of your choice, a journal filled with your encounters with spirits, a set of candles and incense, a robe or shroud, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am attuned to the subtle whispers of the spirits.",
            "Ideal": "Compassion. I use my gift to bring closure and peace to the departed.",
            "Bond": "I have a spirit guide that guides and protects me.",
            "Flaw": "I sometimes become lost in the spirit world, neglecting the living."
        }
    },

    'Time Traveler': {
        "Name": "Time Traveler",
        "Source": "Custom",
        "Details": "You possess a unique artifact or power that allows you to journey through time, experiencing different eras and historical events.",
        "Features": "Temporal Anomaly",
        "Skill Proficiencies": ["History", "Investigation"],
        "Tool Proficiencies": ['None'],
        "Languages": ['Common'],
        "Equipment": "A mysterious time-traveling device or artifact, a journal of your temporal experiences, anachronistic clothing, a map of historical events, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I have a deep fascination with history and the unfolding of time.",
            "Ideal": "Discovery. I seek to uncover the secrets of the past and future.",
            "Bond": "I am connected to a pivotal moment in history and must ensure it unfolds as it should.",
            "Flaw": "The linearity of time can be a burden, and I often struggle with the concept of cause and effect."
        }
    },

    'Mysterious Investigator': {
        "Name": "Mysterious Investigator",
        "Source": "Custom",
        "Details": "You are a detective of the occult and the unknown, specializing in solving supernatural mysteries and unearthing ancient secrets.",
        "Features": "Occult Insights",
        "Skill Proficiencies": ["Investigation", "Arcana"],
        "Tool Proficiencies": ["Occult paraphernalia (crystals, runes, etc.)"],
        "Languages": ['Common'],
        "Equipment": "A collection of occult books and tomes, a set of divination tools, a trench coat or cloak, a magnifying glass, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am always on the lookout for hidden clues and signs of the supernatural.",
            "Ideal": "Knowledge. The truth, no matter how unsettling, must be uncovered.",
            "Bond": "I have an unsolved case that haunts me, and I am determined to solve it.",
            "Flaw": "My obsession with the unknown can make me come across as eccentric or paranoid."
        }
    },
    'Moonlit Bard': {
        "Name": "Moonlit Bard",
        "Source": "Custom",
        "Details": "You draw inspiration from the celestial bodies and the mystical influence of the moon, weaving its magic into your performances.",
        "Features": "Lunar Harmony",
        "Skill Proficiencies": ["Performance", "Arcana"],
        "Tool Proficiencies": ["Musical instrument of your choice"],
        "Languages": ['Common'],
        "Equipment": "A moonstone amulet, a musical instrument of your choice, a set of colorful and ethereal clothing, a moonlit scroll with celestial poetry, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am most creative and inspired under the moon's gentle light.",
            "Ideal": "Harmony. My music brings people together and soothes their souls.",
            "Bond": "I have a deep connection with the moon and its mysteries.",
            "Flaw": "I am entranced by the moon's beauty, sometimes to the detriment of my awareness."
        }
    },

    'Astral Navigator': {
        "Name": "Astral Navigator",
        "Source": "Custom",
        "Details": "You have the ability to traverse the astral plane, exploring the endless cosmos and uncovering hidden knowledge among the stars.",
        "Features": "Astral Insight",
        "Skill Proficiencies": ["Astronomy", "Insight"],
        "Tool Proficiencies": ['None'],
        "Languages": ['Common'],
        "Equipment": "A star chart of the astral plane, a telescope or celestial navigation tool, a set of starry robes, a cosmic journal, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I see the patterns in the stars and seek to decipher their meaning.",
            "Ideal": "Exploration. The cosmos is my playground, and I yearn to explore its mysteries.",
            "Bond": "I have glimpsed a future prophecy among the stars, and it drives my journey.",
            "Flaw": "I can become lost in the vastness of the astral plane, losing touch with reality."
        }
    },

    'Underworld Smuggler': {
        "Name": "Underworld Smuggler",
        "Source": "Custom",
        "Details": "You have a dark and dangerous profession, smuggling illicit goods through the treacherous depths of the underworld.",
        "Features": "Shadow Networks",
        "Skill Proficiencies": ["Stealth", "Deception"],
        "Tool Proficiencies": ["Thieves' tools"],
        "Languages": ['Common'],
        "Equipment": "A concealed compartment for hiding contraband, a shadowy cloak or disguise, a forged identification, a smuggler's ledger, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I thrive in the shadows and know how to keep secrets.",
            "Ideal": "Freedom. The underworld provides a path to independence and wealth.",
            "Bond": "I owe a dangerous crime lord a substantial debt, and they won't forget.",
            "Flaw": "My illegal activities make me a target, and I'm always looking over my shoulder."
        }
    },

    'Starforged Artificer': {
        "Name": "Starforged Artificer",
        "Source": "Custom",
        "Details": "You are a master of infusing celestial energy into your creations, forging items that harness the power of the stars themselves.",
        "Features": "Celestial Infusion",
        "Skill Proficiencies": ["Arcana", "Crafting (Artificer's tools)"],
        "Tool Proficiencies": ["Artificer's tools"],
        "Languages": ['Common'],
        "Equipment": "A set of artificer's tools, a celestial-infused gemstone, a blueprint for a celestial invention, a collection of star charts, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I see the potential for celestial power in everything I create.",
            "Ideal": "Innovation. I strive to push the boundaries of what can be achieved through artifice.",
            "Bond": "I have glimpsed a divine entity in my dreams, inspiring my celestial creations.",
            "Flaw": "I can become obsessed with my inventions, neglecting personal relationships."
        }
    },

    'Blood Mage': {
        "Name": "Blood Mage",
        "Source": "Custom",
        "Details": "You harness the forbidden magic of blood, sacrificing your own life essence to cast powerful spells and manipulate the life force of others.",
        "Features": "Blood Pact",
        "Skill Proficiencies": ["Arcana", "Medicine"],
        "Tool Proficiencies": ['None'],
        "Languages": ['Common'],
        "Equipment": "A vial of your own blood, an arcane grimoire filled with blood magic rituals, a blood-infused dagger, a crimson robe, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I have a mysterious and eerie aura, often unsettling those around me.",
            "Ideal": "Power. Blood is the source of true magical might, and I will harness it at any cost.",
            "Bond": "I have a blood debt with a dark entity, and I must fulfill its sinister requests.",
            "Flaw": "My reliance on blood magic is a constant risk to my own health and sanity."
        }
    },
    'Gnomish Tinkerer': {
        "Name": "Gnomish Tinkerer",
        "Source": "Custom",
        "Details": "You are a master of gnomish engineering, creating intricate contraptions and devices that boggle the mind.",
        "Features": "Inventor's Ingenuity",
        "Skill Proficiencies": ["Investigation", "Crafting (Tinker's tools)"],
        "Tool Proficiencies": ["Tinker's tools"],
        "Languages": ['Common'],
        "Equipment": "A set of tinker's tools, a collection of gears and gadgets, a prototype invention, a set of work clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am endlessly curious and always tinkering with new ideas.",
            "Ideal": "Innovation. The pursuit of knowledge and invention drives me.",
            "Bond": "I have a lifelong rival in the world of gnomish engineering, and I seek to outdo them.",
            "Flaw": "I can be absent-minded and forgetful when absorbed in my tinkering."
        }
    },

    'Feywild Ambassador': {
        "Name": "Feywild Ambassador",
        "Source": "Custom",
        "Details": "You have been chosen as a representative of the Feywild, tasked with bridging the gap between the mortal realm and the enchanting Feywild.",
        "Features": "Fey Enchantment",
        "Skill Proficiencies": ["Persuasion", "Nature"],
        "Tool Proficiencies": ['None'],
        "Languages": ['Common',"Sylvan"],
        "Equipment": "A token of the Feywild's favor, a finely crafted elven or fey item, a cloak woven from enchanted plants, a diary of your experiences, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I possess an otherworldly charm and a whimsical sense of humor.",
            "Ideal": "Harmony. I seek to foster understanding and harmony between mortals and fey.",
            "Bond": "I have a deep connection to a powerful fey patron who watches over me.",
            "Flaw": "My fey nature can be capricious and unpredictable, causing unintended consequences."
        }
    },

    'Clockwork Engineer': {
        "Name": "Clockwork Engineer",
        "Source": "Custom",
        "Details": "You specialize in the construction and maintenance of intricate clockwork mechanisms, from automatons to timekeeping devices.",
        "Features": "Clockwork Craft",
        "Skill Proficiencies": ["Arcana", "Crafting (Tinker's tools)"],
        "Tool Proficiencies": ["Tinker's tools"],
        "Languages": ['Common'],
        "Equipment": "A set of clockwork engineer's tools, a miniature clockwork model of your first invention, a set of work clothes, a technical manual, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I have a precise and methodical approach to problem-solving.",
            "Ideal": "Precision. The intricacies of clockwork are a testament to perfection.",
            "Bond": "My greatest invention was stolen, and I am determined to recover it.",
            "Flaw": "I can be overly critical of imperfections in both people and machines."
        }
    },

    'Haunted Librarian': {
        "Name": "Haunted Librarian",
        "Source": "Custom",
        "Details": "You have dedicated your life to the preservation and study of forbidden and arcane texts, often delving into dark and haunted tomes.",
        "Features": "Dark Knowledge",
        "Skill Proficiencies": ["Arcana", "Investigation"],
        "Tool Proficiencies": ["Library access"],
        "Languages": ['Common'],
        "Equipment": "A collection of eerie and forbidden books, a spectral quill that writes on its own, a cryptic tome filled with forbidden knowledge, a set of scholar's robes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am haunted by the knowledge I have uncovered, often lost in thought.",
            "Ideal": "Discovery. The pursuit of forbidden knowledge is my ultimate goal.",
            "Bond": "I am bound by an otherworldly entity to uncover the secrets hidden within the tomes I protect.",
            "Flaw": "My obsession with the occult can lead me to make dangerous and reckless decisions."
        }
    },

    'Plague Doctor': {
        "Name": "Plague Doctor",
        "Source": "Custom",
        "Details": "You are a skilled physician and alchemist who specializes in treating and preventing the spread of deadly diseases.",
        "Features": "Plague Remedies",
        "Skill Proficiencies": ["Medicine", "Alchemy"],
        "Tool Proficiencies": ["Alchemist's supplies"],
        "Languages": ['Common'],
        "Equipment": "A set of plague doctor's robes and mask, a satchel filled with potent antidotes and remedies, a collection of alchemical ingredients, a set of medical instruments, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am stoic and unflinching in the face of sickness and death.",
            "Ideal": "Healing. My skills are dedicated to preserving life and curing ailments.",
            "Bond": "I have sworn an oath to protect my community from the horrors of disease.",
            "Flaw": "I am haunted by the memories of patients I could not save."
        }
    },
    'Dragon Whisperer': {
        "Name": "Dragon Whisperer",
        "Source": "Custom",
        "Details": "You possess a unique bond with dragons, allowing you to communicate with and influence these powerful creatures.",
        "Features": "Dragon Affinity",
        "Skill Proficiencies": ["Persuasion", "Arcana"],
        "Tool Proficiencies": ["Dragon-related item (e.g., dragon scale, tooth, or claw)"],
        "Languages": ['Common'],
        "Equipment": "A dragon-related trinket, a dragon scale as a symbol of your bond, a tome of dragon lore, a set of fine clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I have a deep respect for the majesty and power of dragons.",
            "Ideal": "Balance. Maintaining a harmonious relationship between dragons and mortals is my mission.",
            "Bond": "I was saved by a dragon as a child, and I owe my life to them.",
            "Flaw": "My obsession with dragons can sometimes blind me to other important matters."
        }
    },

    'Arcane Cartographer': {
        "Name": "Arcane Cartographer",
        "Source": "Custom",
        "Details": "You are a skilled mapmaker who specializes in charting the hidden and magical realms of the world.",
        "Features": "Mystical Mapping",
        "Skill Proficiencies": ["Survival", "Cartography (Mapmaking)"],
        "Tool Proficiencies": ["Cartographer's tools"],
        "Languages": ['Common'],
        "Equipment": "A set of specialized cartographer's tools, a magical compass that points to hidden places, a collection of enchanted maps, a set of explorer's clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am meticulous and detail-oriented in my mapmaking.",
            "Ideal": "Discovery. Revealing the secrets of the world through maps is my life's purpose.",
            "Bond": "My maps have the power to uncover hidden treasures, and I guard them with my life.",
            "Flaw": "I can become obsessed with mapping to the detriment of other aspects of life."
        }
    },

    'Planar Diplomat': {
        "Name": "Planar Diplomat",
        "Source": "Custom",
        "Details": "You serve as an ambassador between the material plane and various extraplanar realms, negotiating treaties and maintaining peace.",
        "Features": "Planar Connection",
        "Skill Proficiencies": ["Diplomacy", "Insight"],
        "Tool Proficiencies": ['None'],
        "Languages": ['Common',"Two of your choice"],
        "Equipment": "A diplomatic insignia, a treaty signed by a powerful extraplanar being, a celestial feather as a symbol of your authority, a set of noble's clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am skilled at reading the intentions of otherworldly beings.",
            "Ideal": "Peace. My mission is to prevent conflicts between planes and foster understanding.",
            "Bond": "I have forged a deep friendship with a powerful entity from another plane.",
            "Flaw": "I am cautious to the point of being overly diplomatic, often avoiding taking sides."
        }
    },

    'Elemental Forger': {
        "Name": "Elemental Forger",
        "Source": "Custom",
        "Details": "You are a master craftsman who specializes in creating weapons and armor infused with the elemental forces of the world.",
        "Features": "Elemental Infusion",
        "Skill Proficiencies": ["Crafting (Smithing)", "Arcana"],
        "Tool Proficiencies": ["Smith's tools"],
        "Languages": ['Common'],
        "Equipment": "A set of masterwork smith's tools, a small elemental gem, a blueprint for an elemental-infused item, a set of fine clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am passionate about the elemental forces and their potential in crafting.",
            "Ideal": "Creation. Crafting masterpieces that harness elemental power is my calling.",
            "Bond": "I seek to create a legendary artifact that will be remembered throughout the ages.",
            "Flaw": "I can be overly protective of my elemental secrets, even at the cost of cooperation."
        }
    },

    'Dreamcatcher': {
        "Name": "Dreamcatcher",
        "Source": "Custom",
        "Details": "You possess the ability to enter and manipulate dreams, using this power for various purposes, including guidance and protection.",
        "Features": "Dreamweaver's Gift",
        "Skill Proficiencies": ["Insight", "Occultism"],
        "Tool Proficiencies": ['None'],
        "Languages": ['Common'],
        "Equipment": "A dreamcatcher talisman, a diary filled with dream interpretations, a small vial of dream essence, a set of mystical robes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am calm and introspective, often lost in thought.",
            "Ideal": "Guidance. I use my dreamweaving abilities to guide others on their paths.",
            "Bond": "I have a connection to a dream spirit that aids me in my journey.",
            "Flaw": "I can become distant and detached from the waking world due to my preoccupation with dreams."
        }
    },
    'Animal Whisperer': {
        "Name": "Animal Whisperer",
        "Source": "Custom",
        "Details": "You have an innate connection with animals, allowing you to communicate with and understand them on a profound level.",
        "Features": "Beast Bond",
        "Skill Proficiencies": ["Animal Handling", "Nature"],
        "Tool Proficiencies": ["Animal handling kit"],
        "Languages": ['Common'],
        "Equipment": "An animal charm as a symbol of your connection, a pouch of animal treats, a collection of sketches of animals, a set of outdoor clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I have a deep empathy for animals and their needs.",
            "Ideal": "Harmony. I seek to promote balance and understanding between the animal kingdom and civilization.",
            "Bond": "I have a loyal animal companion who is my constant companion and protector.",
            "Flaw": "I can be overly protective of animals, sometimes to the detriment of other interests."
        }
    },

    'Crystal Enchanter': {
        "Name": "Crystal Enchanter",
        "Source": "Custom",
        "Details": "You are a skilled enchanter who specializes in infusing magical properties into crystals and gemstones.",
        "Features": "Crystal Mastery",
        "Skill Proficiencies": ["Arcana", "Jeweler's tools"],
        "Tool Proficiencies": ["Jeweler's tools"],
        "Languages": ['Common'],
        "Equipment": "A set of jeweler's tools, a selection of enchanted crystals, a crystal amulet, a set of fine clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am fascinated by the beauty and power of gemstones and crystals.",
            "Ideal": "Enchantment. I believe that magic should be infused into the world's natural beauty.",
            "Bond": "I seek to discover the lost secrets of a legendary gemcrafter from ages past.",
            "Flaw": "I can become overly absorbed in my enchanting work, neglecting other aspects of life."
        }
    },

    'Cosmic Wanderer': {
        "Name": "Cosmic Wanderer",
        "Source": "Custom",
        "Details": "You are an explorer of the cosmos, traveling through the night sky and seeking knowledge among the stars and celestial bodies.",
        "Features": "Celestial Insights",
        "Skill Proficiencies": ["Astronomy", "Survival"],
        "Tool Proficiencies": ["Telescope"],
        "Languages": ['Common'],
        "Equipment": "A telescope, a star map of the night sky, a celestial compass, a set of explorer's clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am inquisitive and always looking to the stars for answers.",
            "Ideal": "Discovery. The cosmos holds endless secrets waiting to be uncovered.",
            "Bond": "I have glimpsed a cosmic event that changed the course of my life forever.",
            "Flaw": "I can become overly obsessed with celestial phenomena, neglecting practical concerns."
        }
    },

    'Shadow Walker': {
        "Name": "Shadow Walker",
        "Source": "Custom",
        "Details": "You are a master of stealth and deception, moving through the shadows with grace and skill.",
        "Features": "Shadow Step",
        "Skill Proficiencies": ["Stealth", "Deception"],
        "Tool Proficiencies": ["Thieves' tools"],
        "Languages": ['Common'],
        "Equipment": "A set of thieves' tools, a shadowy cloak, a mask or disguise, a set of dark clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am secretive and rarely reveal my true intentions.",
            "Ideal": "Freedom. The shadows are my domain, and I seek to remain free and unseen.",
            "Bond": "I owe a life debt to a fellow shadow walker who saved me from a deadly encounter.",
            "Flaw": "I can be mistrustful and find it difficult to open up to others."
        }
    },

    'Astral Artisan': {
        "Name": "Astral Artisan",
        "Source": "Custom",
        "Details": "You are a skilled craftsman who draws inspiration and materials from the astral plane to create unique and otherworldly items.",
        "Features": "Astral Crafting",
        "Skill Proficiencies": ["Crafting (Artisan's tools of your choice)", "Arcana"],
        "Tool Proficiencies": ["Artisan's tools of your choice"],
        "Languages": ['Common'],
        "Equipment": "A set of artisan's tools of your choice, a piece of astral material, a mystical blueprint, a set of fine clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am constantly seeking new astral inspirations for my craft.",
            "Ideal": "Innovation. My creations push the boundaries of what is possible.",
            "Bond": "I have a deep connection to the astral plane, where I draw my creative energy.",
            "Flaw": "I can become consumed by my artistic pursuits, neglecting practical matters."
        }
    },
    'Alchemical Trickster': {
        "Name": "Alchemical Trickster",
        "Source": "Custom",
        "Details": "You are a master of alchemy, using your knowledge to create potions, poisons, and trickery.",
        "Features": "Alchemy Expertise",
        "Skill Proficiencies": ["Arcana", "Sleight of Hand"],
        "Tool Proficiencies": ["Alchemist's supplies"],
        "Languages": ['Common'],
        "Equipment": "A set of alchemist's supplies, a collection of rare herbs and ingredients, an alchemical concoction of your own creation, a set of traveler's clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I have a mischievous streak and enjoy playing pranks on others.",
            "Ideal": "Innovation. Alchemy opens up endless possibilities for creative experimentation.",
            "Bond": "I seek to uncover the legendary formula for the Elixir of Immortality.",
            "Flaw": "I can be careless with my experiments, leading to unexpected consequences."
        }
    },

    'Time Bender': {
        "Name": "Time Bender",
        "Source": "Custom",
        "Details": "You possess the rare ability to manipulate time, allowing you to glimpse into the past and future.",
        "Features": "Temporal Insight",
        "Skill Proficiencies": ["Arcana", "Insight"],
        "Tool Proficiencies": ['None'],
        "Languages": ['Common'],
        "Equipment": "A time-keeping device of your own creation, a mysterious hourglass, a diary filled with cryptic time-related notes, a set of fine clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am contemplative and often lost in thought about the nature of time.",
            "Ideal": "Balance. The past, present, and future are all connected, and I seek to maintain that balance.",
            "Bond": "I once had a vision of a cataclysmic event that I must prevent from happening.",
            "Flaw": "I can become obsessed with the passage of time, neglecting the present moment."
        }
    },

    'Ghostly Scholar': {
        "Name": "Ghostly Scholar",
        "Source": "Custom",
        "Details": "You have made contact with spirits from beyond the grave and have become a scholar of the afterlife.",
        "Features": "Ethereal Knowledge",
        "Skill Proficiencies": ["Religion", "Investigation"],
        "Tool Proficiencies": ['None'],
        "Languages": ['Common',"Two of your choice"],
        "Equipment": "A spectral tome filled with ghostly lore, a vial of ectoplasmic essence, a haunted relic, a set of scholar's clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am calm and composed, even in the presence of supernatural entities.",
            "Ideal": "Understanding. I seek to unravel the mysteries of the afterlife and provide solace to the living.",
            "Bond": "I have a spectral mentor who guides me in my studies.",
            "Flaw": "I can become distant and detached from the concerns of the living world."
        }
    },

    'Lunar Sage': {
        "Name": "Lunar Sage",
        "Source": "Custom",
        "Details": "You are a scholar of the moon, its phases, and its mystical influence on the world.",
        "Features": "Moonlit Insights",
        "Skill Proficiencies": ["Nature", "Perception"],
        "Tool Proficiencies": ["Navigator's tools"],
        "Languages": ['Common'],
        "Equipment": "A lunar calendar, a moonstone amulet, a telescope for lunar observations, a set of explorer's clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am attuned to the subtle changes of the moon and its impact on nature.",
            "Ideal": "Harmony. The cycles of the moon reflect the balance of all things in the world.",
            "Bond": "I have witnessed a lunar phenomenon that defied explanation, and I seek to understand its significance.",
            "Flaw": "I can be overly superstitious, believing that the moon's phases govern all aspects of life."
        }
    },

    'Abyssal Conqueror': {
        "Name": "Abyssal Conqueror",
        "Source": "Custom",
        "Details": "You have faced the horrors of the Abyss and emerged as a conqueror of its dark denizens.",
        "Features": "Abyssal Resilience",
        "Skill Proficiencies": ["Survival", "Intimidation"],
        "Tool Proficiencies": ["Demon-slaying weapons"],
        "Languages": ['Common'],
        "Equipment": "A weapon forged from Abyssal materials, a trophy from a slain demon, a dark and battle-worn cloak, a set of savage clothing, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am fearless in the face of demonic threats and exude an aura of confidence.",
            "Ideal": "Defiance. I stand against the Abyss and its corruption, ready to confront it at any cost.",
            "Bond": "I have sworn to rid the world of a specific demon lord who once terrorized my homeland.",
            "Flaw": "I can become reckless in my pursuit of demonic foes, risking everything for vengeance."
        }
    },
    'Elemental Shaman': {
        "Name": "Elemental Shaman",
        "Source": "Custom",
        "Details": "You are a master of harnessing the elemental forces of nature, forging a deep connection with the primal elements.",
        "Features": "Elemental Attunement",
        "Skill Proficiencies": ["Nature", "Arcana"],
        "Tool Proficiencies": ["Herbalism kit"],
        "Languages": ['Common'],
        "Equipment": "An elemental focus (a crystal, a staff, or a totem), a pouch of elemental components, a book of elemental rituals, a set of shamanic clothing, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am in tune with the rhythms of nature and often speak in metaphorical language.",
            "Ideal": "Balance. The elements are in harmony, and I seek to maintain that balance in all things.",
            "Bond": "I have communed with ancient elemental spirits, and they guide my actions.",
            "Flaw": "I can become fiercely protective of nature, even to the detriment of civilization."
        }
    },

    'Illusionist Acrobat': {
        "Name": "Illusionist Acrobat",
        "Source": "Custom",
        "Details": "You are a master of illusion magic, using your skills to captivate audiences and confound your enemies.",
        "Features": "Illusionist's Mastery",
        "Skill Proficiencies": ["Performance", "Sleight of Hand"],
        "Tool Proficiencies": ["Disguise kit"],
        "Languages": ['Common'],
        "Equipment": "A set of illusionist's tools, a collection of enchanted trick props, a book of illusion spells, a set of flamboyant performance attire, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am a natural show-off and love being the center of attention.",
            "Ideal": "Wonder. Illusions can bring joy and astonishment to the world.",
            "Bond": "I owe my success to my mentor, a legendary illusionist.",
            "Flaw": "I have a tendency to exaggerate my abilities and accomplishments."
        }
    },

    'Spiritbound Hunter': {
        "Name": "Spiritbound Hunter",
        "Source": "Custom",
        "Details": "You have formed a mystical bond with the spirits of the natural world, guiding your hunting and tracking skills.",
        "Features": "Spiritual Connection",
        "Skill Proficiencies": ["Survival", "Animal Handling"],
        "Tool Proficiencies": ["Hunter's kit"],
        "Languages": ['Common'],
        "Equipment": "A spirit-infused weapon, a set of animal totems, a pouch of herbs and incense for rituals, a set of rugged wilderness clothing, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am calm and patient, in tune with the subtle signs of nature.",
            "Ideal": "Harmony. The spirits guide my actions, and I seek to maintain harmony with the natural world.",
            "Bond": "I have a spirit animal companion that has been with me since childhood.",
            "Flaw": "I can be overly superstitious, interpreting every event as a sign from the spirits."
        }
    },

    'Starship Pilot': {
        "Name": "Starship Pilot",
        "Source": "Custom",
        "Details": "You are a skilled pilot who navigates the vastness of space, commanding advanced starships with precision.",
        "Features": "Astro-Navigation",
        "Skill Proficiencies": ["Piloting", "Astrogation"],
        "Tool Proficiencies": ["Starship controls"],
        "Languages": ['Common'],
        "Equipment": "A holographic star map, a data pad with starship schematics, a pilot's jumpsuit, a set of communication devices, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am confident and unflappable, even in the face of interstellar dangers.",
            "Ideal": "Exploration. The cosmos are vast and full of wonders, and I seek to explore them all.",
            "Bond": "I have a personal starship that I consider my second home.",
            "Flaw": "I can be overly competitive, always striving to prove my skills as a pilot."
        }
    },

    'Witch Hunter': {
        "Name": "Witch Hunter",
        "Source": "Custom",
        "Details": "You are a dedicated hunter of witches and practitioners of dark magic, using your skills to root out and eliminate supernatural threats.",
        "Features": "Witchfinder",
        "Skill Proficiencies": ["Investigation", "Insight"],
        "Tool Proficiencies": ["Exorcism tools"],
        "Languages": ['Common'],
        "Equipment": "A collection of holy symbols and protective talismans, a book of dark magic lore, a set of witch-hunting attire, a set of concealed weapons, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am skeptical and vigilant, always on the lookout for signs of dark magic.",
            "Ideal": "Purification. I seek to rid the world of witchcraft and dark sorcery.",
            "Bond": "I have a personal vendetta against a powerful witch who once eluded capture.",
            "Flaw": "I can be overly zealous, sometimes seeing witchcraft where none exists."
        }
    },
    'Eldritch Archaeologist': {
        "Name": "Eldritch Archaeologist",
        "Source": "Custom",
        "Details": "You are an adventurer and scholar who specializes in uncovering ancient and eldritch secrets buried beneath the earth.",
        "Features": "Eldritch Insights",
        "Skill Proficiencies": ["History", "Investigation"],
        "Tool Proficiencies": ["Archaeologist's tools"],
        "Languages": ['Common'],
        "Equipment": "A set of archaeologist's tools, a mysterious relic from a previous excavation, a worn journal filled with cryptic notes, a set of durable expedition clothing, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am endlessly curious and driven to uncover hidden knowledge.",
            "Ideal": "Discovery. The secrets of the past hold the key to understanding the present.",
            "Bond": "I have a mentor who disappeared while searching for an ancient artifact, and I am determined to find them.",
            "Flaw": "I can become obsessed with unraveling mysteries, sometimes to the detriment of personal relationships."
        }
    },

    'Planar Nomad': {
        "Name": "Planar Nomad",
        "Source": "Custom",
        "Details": "You are a wanderer who has traversed the planes of existence, gaining unique insights into the multiverse.",
        "Features": "Planar Affinity",
        "Skill Proficiencies": ["Arcana", "Survival"],
        "Tool Proficiencies": ['None'],
        "Languages": ['Common',"Two of your choice"],
        "Equipment": "A planar map filled with notes and annotations, a trinket from another plane, a set of traveler's clothes suitable for multiple environments, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am adaptable and open-minded, comfortable in unfamiliar surroundings.",
            "Ideal": "Exploration. The multiverse is vast and full of wonders, and I am eager to explore its every corner.",
            "Bond": "I have a deep connection to a specific plane and consider it my true home.",
            "Flaw": "I can be restless, always seeking the next interplanar adventure."
        }
    },

    'Sky Pirate': {
        "Name": "Sky Pirate",
        "Source": "Custom",
        "Details": "You are a swashbuckling pirate who commands an airborne ship, plundering the skies and living by your own code of honor.",
        "Features": "Skystealer",
        "Skill Proficiencies": ["Acrobatics", "Perception"],
        "Tool Proficiencies": ["Navigator's tools", "Thieves' tools"],
        "Languages": ['Common'],
        "Equipment": "A compass that always points to the skies, a personalized airship emblem, a trusty grappling hook, a set of buccaneer attire, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am daring and fearless, always ready for an airborne brawl.",
            "Ideal": "Freedom. The open skies are my domain, and I'll be bound by no one.",
            "Bond": "My airship is my most prized possession, and I'll do anything to protect it.",
            "Flaw": "I can be overly competitive, sometimes risking everything for a chance at glory."
        }
    },

    'Spellforged Blacksmith': {
        "Name": "Spellforged Blacksmith",
        "Source": "Custom",
        "Details": "You are a master blacksmith who combines craftsmanship with arcane magic, creating enchanted weapons and armor.",
        "Features": "Arcane Smithing",
        "Skill Proficiencies": ["Smith's tools", "Arcana"],
        "Tool Proficiencies": ['None'],
        "Languages": ['Common'],
        "Equipment": "A set of exquisite smith's tools, a magical rune-inscribed hammer, a sample of your finest enchanted creation, a set of sturdy blacksmith's attire, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I take immense pride in my work and craftsmanship.",
            "Ideal": "Mastery. The fusion of magic and metal is an art, and I am its master.",
            "Bond": "My mentor, a legendary spellforged blacksmith, taught me everything I know.",
            "Flaw": "I can be obsessive about creating the perfect enchanted item, sometimes neglecting other aspects of life."
        }
    },

    'Abyssal Scholar': {
        "Name": "Abyssal Scholar",
        "Source": "Custom",
        "Details": "You are a dedicated scholar who delves into the forbidden knowledge of the Abyss, seeking to understand its dark secrets.",
        "Features": "Abyssal Insights",
        "Skill Proficiencies": ["Arcana", "Religion"],
        "Tool Proficiencies": ['None'],
        "Languages": ['Common',"Abyssal"],
        "Equipment": "A grimoire filled with abyssal runes and forbidden lore, a vial of demonic ichor, a black hooded robe, a set of ink and parchment, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am unshakably determined to uncover the mysteries of the Abyss, no matter the cost.",
            "Ideal": "Knowledge. Understanding the darkest forces can lead to their destruction.",
            "Bond": "I carry the curse of a demonic entity that I seek to control.",
            "Flaw": "I can be reckless in my pursuit of abyssal knowledge, disregarding personal safety."
        }
    },
}

def generate_random_background(dnd_backgrounds):
    random_background = random.choice(list(dnd_backgrounds.keys()))
    random_background_roleplaying_suggestions = {}
    for trait, description in dnd_backgrounds[random_background]['Roleplaying Suggestions'].items():
        random_background_roleplaying_suggestions[trait] = dnd_backgrounds[random.choice(list(dnd_backgrounds.keys()))]['Roleplaying Suggestions'][trait]

    randomly_generated_background = {
        "Name": random.choice(list(dnd_backgrounds.keys())),
        "Source": "Randomly Generated from Templates",
        "Details": dnd_backgrounds[random.choice(list(dnd_backgrounds.keys()))]['Details'],
        "Features": dnd_backgrounds[random.choice(list(dnd_backgrounds.keys()))]['Features'],
        "Skill Proficiencies": ', '.join(dnd_backgrounds[random.choice(list(dnd_backgrounds.keys()))]["Skill Proficiencies"]),
        "Tool Proficiencies": ', '.join(dnd_backgrounds[random.choice(list(dnd_backgrounds.keys()))]["Tool Proficiencies"]),
        "Languages": dnd_backgrounds[random.choice(list(dnd_backgrounds.keys()))]["Languages"],
        "Equipment": dnd_backgrounds[random.choice(list(dnd_backgrounds.keys()))]["Equipment"],
        "Roleplaying Suggestions": random_background_roleplaying_suggestions
    }
    return randomly_generated_background


