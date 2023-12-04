#! /usr/bin/env python3


dnd_backgrounds = {
    "Acolyte": {
        "Name": "Acolyte",
        "Details": "Devoted to a deity or a religious life, serving a temple or religious community.",
        "Features": "Shelter of the Faithful - Gain support from religious communities.",
        "Skill Proficiencies": ["Insight", "Religion"],
        "Tool Proficiencies": 'None',
        "Languages": "Two of your choice",
        "Equipment": "Holy symbol, prayer book, 5 sticks of incense, vestments, common clothes, 15 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I idolize a particular hero of my faith and constantly refer to their deeds and example.",
            "Ideal": "Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld.",
            "Bond": "I will do anything to protect my temple.",
            "Flaw": "I am inflexible in my thinking."
        }
    },
    "Baker (Custom)": {
        "Name": "Baker (Custom)",
        "Details": "You have spent much of your life baking, creating breads, pastries, and other delights.",
        "Features": "Baker's Delight",
        "Skill Proficiencies": ["Investigation", "Nature"],
        "Tool Proficiencies": ["Baker's tools", "Cook's utensils"],
        "Languages": None,
        "Equipment": "A set of baker's tools, a set of common clothes stained with flour, a loaf of fresh bread, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I rise early and am used to the morning hours.",
            "Ideal": "Nourishment. Good food brings comfort and happiness.",
            "Bond": "I inherited my recipes from a beloved mentor, and they are precious to me.",
            "Flaw": "I am very particular about my ingredients and workspace."
        }
    },
    "Blacksmith (Custom)": {
        "Name": "Blacksmith (Custom)",
        "Details": "You have honed your skills in the forge, crafting items from metal and repairing them.",
        "Features": "Smith's Intuition",
        "Skill Proficiencies": ["Athletics", "Investigation"],
        "Tool Proficiencies": ["Smith's tools", "Vehicles (land)"],
        "Languages": None,
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
        "Details": "You have always had a way with people. You know what makes them tick, and you can tease out their heart's desires after a few minutes of conversation.",
        "Features": "False Identity",
        "Skill Proficiencies": ["Deception", "Sleight of Hand"],
        "Tool Proficiencies": ["Disguise kit", "Forgery kit"],
        "Languages": None,
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
        "Details": "A past filled with crime, possibly still mingling with thieves and rogues.",
        "Features": "Criminal Contact - You have a reliable and trustworthy contact in the criminal underworld.",
        "Skill Proficiencies": ["Deception", "Stealth"],
        "Tool Proficiencies": ["One type of gaming set", "Thieves' tools"],
        "Languages": [],
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
        "Details": "You thrive in front of an audience. You are a musician, a poet, a jester, a storyteller, or some other kind of performer.",
        "Features": "By Popular Demand",
        "Skill Proficiencies": ["Acrobatics", "Performance"],
        "Tool Proficiencies": ["Disguise kit", "One type of musical instrument"],
        "Languages": [],
        "Equipment": "A musical instrument, the favor of an admirer, a costume, a set of common clothes, and a belt pouch containing 15 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I know a story relevant to almost every situation.",
            "Ideal": "Creativity. The world is in need of new ideas and bold action.",
            "Bond": "I will do anything to prove myself superior to my hated rival.",
            "Flaw": "I’m a sucker for a pretty face."
        }
    },
    "Farmer (Custom)": {
        "Name" : "Farmer (Custom)",
        "Details": "You have spent a significant portion of your life working the land, tending to crops and livestock.",
        "Features": "Rustic Hospitality",
        "Skill Proficiencies": ["Animal Handling", "Nature"],
        "Tool Proficiencies": ["Vehicles (land)", "One type of artisan's tools related to farming"],
        "Languages": None,
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
        "Details": "You come from a humble social rank, but you are destined for so much more. Already the people of your home village regard you as their champion.",
        "Features": "Rustic Hospitality",
        "Skill Proficiencies": ["Animal Handling", "Survival"],
        "Tool Proficiencies": ["One type of artisan's tools", "Vehicles (land)"],
        "Languages": [],
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
        "Details": "You are a member of an artisan’s guild, skilled in a particular craft, and closely associated with other artisans.",
        "Features": "Guild Membership",
        "Skill Proficiencies": ["Insight", "Persuasion"],
        "Tool Proficiencies": ["One type of artisan's tools"],
        "Languages": "One of your choice",
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
        "Details": "You have lived in seclusion, away from the bustling societies, either in a sheltered community such as a monastery or entirely alone.",
        "Features": "Discovery",
        "Skill Proficiencies": ["Medicine", "Religion"],
        "Tool Proficiencies": ["Herbalism kit"],
        "Languages": "One of your choice",
        "Equipment": "A scroll case stuffed full of notes from your studies or prayers, a winter blanket, a set of common clothes, a herbalism kit, and 5 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I often get lost in my own thoughts and contemplation, becoming oblivious to my surroundings.",
            "Ideal": "Self-Knowledge. If you know yourself, there’s nothing left to know.",
            "Bond": "I entered seclusion to hide from the ones who might still be hunting me. I must someday confront them.",
            "Flaw": "Now that I've returned to the world, I enjoy its delights a little too much."
        }
    },
    "Hunter (Custom)": {
        "Name" : "Hunter (Custom)",
        "Details": "You have lived in the wilderness, relying on your skills in tracking and hunting for survival.",
        "Features": "Tracker's Eye",
        "Skill Proficiencies": ["Survival", "Stealth"],
        "Tool Proficiencies": ["One type of gaming set", "Vehicles (land)"],
        "Languages": None,
        "Equipment": "A set of traveler's clothes, a hunting trap, a trophy from an animal you killed, a set of common clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I am patient and observant, a predator waiting for the perfect moment.",
            "Ideal": "Balance. Nature teaches us that balance must be maintained.",
            "Bond": "I hunt not just for food, but to protect the wilderness.",
            "Flaw": "I have little respect for those who do not understand or respect nature."
        }
    },    
    "Innkeeper (Custom)": {
        "Name" : "InnKeeper (Custom)",
        "Details": "You have managed an inn, tavern, or similar establishment, providing a place of rest and nourishment for travelers.",
        "Features": "Hospitality",
        "Skill Proficiencies": ["Insight", "Persuasion"],
        "Tool Proficiencies": ["Cook's utensils", "Brewer's supplies"],
        "Languages": None,
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
        "Details": "You have been granted a knighthood. You might be a minor scion of a noble house, or perhaps you earned your title on the battlefield.",
        "Features": "Retainers",
        "Skill Proficiencies": ["History", "Persuasion"],
        "Tool Proficiencies": ["One type of gaming set", "Vehicles (land)"],
        "Languages": None,
        "Equipment": "A set of fine clothes, a signet ring, a scroll of pedigree, and a purse containing 25 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "My flattery makes those I talk to feel wonderful and important.",
            "Ideal": "Respect. People deserve to be treated with dignity and respect.",
            "Bond": "The common folk must see me as a hero of the realm.",
            "Flaw": "The monstrous enemy we faced in battle still leaves me quivering with fear."
        }
    },
    "Merchant (Custom)": {
        "Name" : "Merchant (Custom)",
        "Details": "You have spent your life in the pursuit of commerce, trading goods across the land or even across seas.",
        "Features": "Deal Maker",
        "Skill Proficiencies": ["Persuasion", "Insight"],
        "Tool Proficiencies": ["One type of artisan's tools related to your goods", "Vehicles (land or water)"],
        "Languages": "One of your choice",
        "Equipment": "A set of common clothes, an abacus, a sample of goods, a ledger, and a belt pouch containing 15 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I can haggle prices with the best of them.",
            "Ideal": "Wealth. The accumulation of wealth allows for a comfortable and influential life.",
            "Bond": "I will go to great lengths to protect my trading network.",
            "Flaw": "I am obsessed with making the next big deal."
        }
    },
    "Miner (Custom)": {
        "Name" : "Miner (Custom)",
        "Details": "You have spent years working in mines, extracting minerals and ores from the earth.",
        "Features": "Stone Knowledge",
        "Skill Proficiencies": ["Athletics", "Survival"],
        "Tool Proficiencies": ["Pickaxe", "Vehicles (land)"],
        "Languages": None,
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
        "Details": "You understand wealth, power, and privilege. You carry a noble title, and your family owns land, collects taxes, and wields significant political influence.",
        "Features": "Position of Privilege",
        "Skill Proficiencies": ["History", "Persuasion"],
        "Tool Proficiencies": ["One type of gaming set"],
        "Languages": "One of your choice",
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
        "Details": "You grew up in the wilds, far from civilization and the comforts of town and technology.",
        "Features": "Wanderer",
        "Skill Proficiencies": ["Athletics", "Survival"],
        "Tool Proficiencies": ["One type of musical instrument"],
        "Languages": "One of your choice",
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
        "Details": "You spent your youth under the sway of a dread pirate, a ruthless cutthroat who taught you how to survive in a world of sharks and savages.",
        "Features": "Bad Reputation",
        "Skill Proficiencies": ["Athletics", "Perception"],
        "Tool Proficiencies": ["Navigator's tools", "Vehicles (water)"],
        "Languages": None,
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
        "Details": "You have spent your life on the seas, aboard a ship, facing the dangers of waves and wind.",
        "Features": "Ship's Passage",
        "Skill Proficiencies": ["Athletics", "Perception"],
        "Tool Proficiencies": ["Navigator's tools", "Vehicles (water)"],
        "Languages": None,
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
        "Details": "You spent years learning the lore of the multiverse. You scoured manuscripts, studied scrolls, and listened to the greatest experts on the subjects that interest you.",
        "Features": "Researcher",
        "Skill Proficiencies": ["Arcana", "History"],
        "Tool Proficiencies": [],
        "Languages": "Two of your choice",
        "Equipment": "A bottle of black ink, a quill, a small knife, a letter from a dead colleague posing a question you have not yet been able to answer, a set of common clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I use polysyllabic words that convey the impression of great erudition.",
            "Ideal": "Knowledge. The path to power and self-improvement is through knowledge.",
            "Bond": "I've been searching my whole life for the answer to a certain question.",
            "Flaw": "I am easily distracted by the promise of information."
        }
    },
    "Scribe (Custom)": {
        "Name" : "Scribe (Custom)",
        "Details": "You have spent years copying and studying texts, working as a scribe for a library, a private individual, or a guild.",
        "Features": "Lore of the Scribe",
        "Skill Proficiencies": ["History", "Investigation"],
        "Tool Proficiencies": ["Calligrapher's supplies"],
        "Languages": "Two of your choice",
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
        "Details": "You have served in an army, learning the ways of war. You might have been part of a standing army or a local militia, or perhaps a mercenary company.",
        "Features": "Military Rank",
        "Skill Proficiencies": ["Athletics", "Intimidation"],
        "Tool Proficiencies": ["One type of gaming set", "Vehicles (land)"],
        "Languages": [],
        "Equipment": "An insignia of rank, trophies from fallen enemies, a set of bone dice or deck of cards, a set of common clothes, and a pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I’m always polite and respectful.",
            "Ideal": "Greater Good. Our lot is to lay down our lives in defense of others.",
            "Bond": "I’ll never forget the crushing defeat my company suffered or the enemies who dealt it.",
            "Flaw": "I’d rather eat my armor than admit when I’m wrong."
        }
    },
    "Tailor (Custom)": {
        "Name" : "Tailor (Custom)",
        "Details": "You have a knack for creating and altering clothing, working with fine fabrics and designs.",
        "Features": "Eye for Detail",
        "Skill Proficiencies": ["Persuasion", "Performance"],
        "Tool Proficiencies": ["Tailor's tools"],
        "Languages": None,
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
        "Details": "You grew up on the streets, alone, orphaned, and poor, learning to fend for yourself.",
        "Features": "City Secrets",
        "Skill Proficiencies": ["Sleight of Hand", "Stealth"],
        "Tool Proficiencies": ["Disguise kit", "Thieves’ tools"],
        "Languages": None,
        "Equipment": "A small knife, a map of the city you grew up in, a pet mouse, a token to remember your parents by, a set of common clothes, and a belt pouch containing 10 gp",
        "Roleplaying Suggestions": {
            "Personality Trait": "I hide scraps of food and trinkets away in my pockets.",
            "Ideal": "Retribution. I steal from the wealthy so that I can help people in need.",
            "Bond": "I owe everything to my mentor – a horrible person who’s probably rotting in jail somewhere.",
            "Flaw": "If I'm outnumbered, I will run away from a fight."
        }
    }
}
