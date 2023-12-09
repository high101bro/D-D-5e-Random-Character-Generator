#! /usr/bin/env python3

dnd_monsters = {
    "aarakocra": {
        "name": "Aarakocra",
        "type": "Medium humanoid (Aarakocra)",
        "alignment": "neutral good",
        "Armor Class": "12",
        "Hit Points": "13 (3d8)",
        "Speed": "20 ft., fly 50 ft.",
        "Skills": "Perception +5",
        "Senses": "passive Perception 15",
        "Languages": "Auran, Aarakocra",
        "Challenge": "1/4 (50 XP)",
        "STR": "10 (+0)",
        "DEX": "14 (+2)",
        "CON": "10 (+0)",
        "INT": "11 (+0)",
        "WIS": "12 (+1)",
        "CHA": "11 (+0)",
        "features": [
            "Dive Attack. If the aarakocra is flying and dives at least 30 feet straight toward a target and then hits it with a melee weapon attack, the attack deals an extra 3 (1d6) damage to the target."
        ],
        "Actions": [
            "Talon.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 4 (1d4 + 2) slashing damage.",
            "Javelin.Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target.Hit: 5 (1d6 + 2) piercing damage."
        ]
    },
    "aboleth": {
        "name": "Aboleth",
        "type": "Large aberration",
        "alignment": "lawful evil",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "135 (18d10 + 36)",
        "Speed": "10 ft., swim 40 ft.",
        "Saving Throws": "Con +6, Int +8, Wis +6",
        "Skills": "History +12, Perception +10",
        "Senses": "darkvision 120 ft., passive Perception 20",
        "Languages": "Deep Speech, telepathy 120 ft.",
        "Challenge": "10 (5900 XP)",
        "STR": "21 (+5)",
        "DEX": "9 (-1)",
        "CON": "15 (+2)",
        "INT": "18 (+4)",
        "WIS": "15 (+2)",
        "CHA": "18 (+4)",
        "Legendary actions": [
            "The aboleth can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The aboleth regains spent legendary actions at the start of its turn.",
            "Detect. The aboleth makes a Wisdom (Perception) check.",
            "Tail Swipe. The aboleth makes one tail attack.",
            "Psychic Drain (Costs 2 Actions). One creature charmed by the aboleth takes 10 (3d6) psychic damage, and the aboleth regains hit points equal to the damage the creature takes."
        ],
        "features": [
            "Amphibious. The aboleth can breathe air and water.",
            "Mucous Cloud. While underwater, the aboleth is surrounded by transformative mucus. A creature that touches the aboleth or that hits it with a melee attack while within 5 feet of it must make a DC 14 Constitution saving throw. On a failure, the creature is diseased for 1d4 hours. The diseased creature can breathe only underwater.",
            "Probing Telepathy. If a creature communicates telepathically with the aboleth, the aboleth learns the creature's greatest desires if the aboleth can see the creature."
        ],
        "Actions": [
            "Multiattack. The aboleth makes three tentacle attacks.",
            "Tentacle.Melee Weapon Attack: +9 to hit, reach 10 ft., one target.Hit: 12 (2d6 + 5) bludgeoning damage. If the target is a creature, it must succeed on a DC 14 Constitution saving throw or become diseased. The disease has no effect for 1 minute and can be removed by any magic that cures disease. After 1 minute, the diseased creature's skin becomes translucent and slimy, the creature can't regain hit points unless it is underwater, and the disease can be removed only byhealor another disease-curing spell of 6th level or higher. When the creature is outside a body of water, it takes 6 (1d12) acid damage every 10 minutes unless moisture is applied to the skin before 10 minutes have passed.",
            "Tail.Melee Weapon Attack: +9 to hit, reach 10 ft., one target.Hit: 15 (3d6 + 5) bludgeoning damage.",
            "Enslave (3/Day). The aboleth targets one creature it can see within 30 feet of it. The target must succeed on a DC 14 Wisdom saving throw or be magically charmed by the aboleth until the aboleth dies or until it is on a different plane of existence from the target. The charmed target is under the aboleth's control and can't take reactions, and the aboleth and the target can communicate telepathically with each other over any distance. Whenever the charmed target takes damage, the target can repeat the saving throw. On a success, the effect ends. No more than once every 24 hours, the target can also repeat the saving throw when it is at least 1 mile away from the aboleth."
        ]
    },
    "abominable-yeti": {
        "name": "Abominable Yeti",
        "type": "Huge monstrosity",
        "alignment": "chaotic evil",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "137 (11d12 + 66)",
        "Speed": "40 ft., climb 40 ft.",
        "Skills": "Perception +5, Stealth +4",
        "Damage Immunities": "cold",
        "Senses": "darkvision 60 ft., passive Perception 15",
        "Languages": "Yeti",
        "Challenge": "9 (5000 XP)",
        "STR": "24 (+7)",
        "DEX": "10 (+0)",
        "CON": "22 (+6)",
        "INT": "9 (-1)",
        "WIS": "13 (+1)",
        "CHA": "9 (-1)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "acolyte": {
        "name": "Acolyte",
        "type": "Medium humanoid (any race)",
        "alignment": "any alignment",
        "Armor Class": "10",
        "Hit Points": "9 (2d8)",
        "Speed": "30 ft.",
        "Skills": "Medicine +4, Religion +2",
        "Senses": "passive Perception 12",
        "Languages": "any one language (usually Common)",
        "Challenge": "1/4 (50 XP)",
        "STR": "10 (+0)",
        "DEX": "10 (+0)",
        "CON": "10 (+0)",
        "INT": "10 (+0)",
        "WIS": "14 (+2)",
        "CHA": "11 (+0)",
        "features": [
            "Spellcasting. The acolyte is a 1st-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). The acolyte has the following cleric spells prepared:"
        ],
        "Actions": [
            "Club.Melee Weapon Attack: +2 to hit, reach 5 ft., one target.Hit: 2 (1d4) bludgeoning damage."
        ]
    },
    "adult-black-dragon": {
        "name": "Adult Black Dragon",
        "type": "Huge dragon (Chromatic)",
        "alignment": "chaotic evil",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "195 (17d12 + 85)",
        "Speed": "40 ft., fly 80 ft., swim 40 ft.",
        "Saving Throws": "Dex +7, Con +10, Wis +6, Cha +8",
        "Skills": "Perception +11, Stealth +7",
        "Damage Immunities": "acid",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 21",
        "Languages": "Common, Draconic",
        "Challenge": "14 (11500 XP)",
        "STR": "23 (+6)",
        "DEX": "14 (+2)",
        "CON": "21 (+5)",
        "INT": "14 (+2)",
        "WIS": "13 (+1)",
        "CHA": "17 (+3)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 19 Dexterity saving throw or take 13 (2d6 + 6) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
        ],
        "features": [
            "Amphibious. The dragon can breathe air and water.",
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +11 to hit, reach 10 ft., one target.Hit: 17 (2d10 + 6) piercing damage plus 4 (1d8) acid damage.",
            "Claw.Melee Weapon Attack: +11 to hit, reach 5 ft., one target.Hit: 13 (2d6 + 6) slashing damage.",
            "Tail.Melee Weapon Attack: +11 to hit, reach 15 ft., one target.Hit: 15 (2d8 + 6) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 16 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Acid Breath (Recharge 5-6). The dragon exhales acid in a 60-foot line that is 5 feet wide. Each creature in that line must make a DC 18 Dexterity saving throw, taking 54 (12d8) acid damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "adult-blue-dracolich": {
        "name": "Adult Blue Dracolich",
        "type": "Huge undead",
        "alignment": "lawful evil",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "225 (18d12 + 108)",
        "Speed": "40 ft., burrow 30 ft., fly 80 ft.",
        "Saving Throws": "Dex +6, Con +12, Wis +8, Cha +10",
        "Skills": "Perception +14, Stealth +6",
        "Damage Resistances": "necrotic",
        "Damage Immunities": "lightning, poison",
        "Condition Immunities": "charmed, exhaustion, frightened, paralyzed, poisoned",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 24",
        "Languages": "Common, Draconic",
        "Challenge": "17 (18000 XP)",
        "STR": "25 (+7)",
        "DEX": "10 (+0)",
        "CON": "23 (+6)",
        "INT": "16 (+3)",
        "WIS": "15 (+2)",
        "CHA": "19 (+4)",
        "Legendary actions": [
            "The dracolich can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dracolich regains spent legendary actions at the start of its turn.",
            "Detect. The dracolich makes a Wisdom (Perception) check.",
            "Tail Attack. The dracolich makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dracolich beats its tattered wings. Each creature within 10 ft. of the dracolich must succeed on a DC 21 Dexterity saving throw or take 14 (2d6 + 7) bludgeoning damage and be knocked prone. After beating its wings this way, the dracolich can fly up to half its flying speed."
        ],
        "features": [
            "Legendary Resistance (3/Day). If the dracolich fails a saving throw, it can choose to succeed instead.",
            "Magic Resistance. The dracolich has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack. The dracolich can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +12 to hit, reach 10 ft., one target.Hit: 18 (2d10 + 7) piercing damage plus 5 (1d10) lightning damage.",
            "Claw.Melee Weapon Attack: +12 to hit, reach 5 ft., one target.Hit: 14 (2d6 + 7) slashing damage.",
            "Tail.Melee Weapon Attack: +12 to hit, reach 15 ft., one target.Hit: 16 (2d8 + 7) bludgeoning damage.",
            "Frightful Presence. Each creature of the dracolich's choice that is within 120 feet of the dracolich and aware of it must succeed on a DC 18 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dracolich's Frightful Presence for the next 24 hours.",
            "Lightning Breath (Recharge 5\u20136). The dracolich exhales lightning in a 90-foot line that is 5 feet wide. Each creature in that line must make a DC 20 Dexterity saving throw, taking 66 (12d10) lightning damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "adult-blue-dragon": {
        "name": "Adult Blue Dragon",
        "type": "Huge dragon (Chromatic)",
        "alignment": "lawful evil",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "225 (18d12 + 108)",
        "Speed": "40 ft., burrow 30 ft., fly 80 ft.",
        "Saving Throws": "Dex +5, Con +11, Wis +7, Cha +9",
        "Skills": "Perception +12, Stealth +5",
        "Damage Immunities": "lightning",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 22",
        "Languages": "Common, Draconic",
        "Challenge": "16 (15000 XP)",
        "STR": "25 (+7)",
        "DEX": "10 (+0)",
        "CON": "23 (+6)",
        "INT": "16 (+3)",
        "WIS": "15 (+2)",
        "CHA": "19 (+4)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 20 Dexterity saving throw or take 14 (2d6 + 7) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
        ],
        "features": [
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +12 to hit, reach 10 ft., one target.Hit: 18 (2d10 + 7) piercing damage plus 5 (1d10) lightning damage.",
            "Claw.Melee Weapon Attack: +12 to hit, reach 5 ft., one target.Hit: 14 (2d6 + 7) slashing damage.",
            "Tail.Melee Weapon Attack: +12 to hit, reach 15 ft., one target.Hit: 16 (2d8 + 7) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 17 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Lightning Breath (Recharge 5-6). The dragon exhales lightning in a 90-foot line that is 5 feet wide. Each creature in that line must make a DC 19 Dexterity saving throw, taking 66 (12d10) lightning damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "adult-brass-dragon": {
        "name": "Adult Brass Dragon",
        "type": "Huge dragon (Metallic)",
        "alignment": "chaotic good",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "172 (15d12 + 75)",
        "Speed": "40 ft., burrow 30 ft., fly 80 ft.",
        "Saving Throws": "Dex +5, Con +10, Wis +6, Cha +8",
        "Skills": "History +7, Perception +11, Persuasion +8, Stealth +5",
        "Damage Immunities": "fire",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 21",
        "Languages": "Common, Draconic",
        "Challenge": "13 (10000 XP)",
        "STR": "23 (+6)",
        "DEX": "10 (+0)",
        "CON": "21 (+5)",
        "INT": "14 (+2)",
        "WIS": "13 (+1)",
        "CHA": "17 (+3)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 19 Dexterity saving throw or take 13 (2d6 + 6) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying Speed."
        ],
        "features": [
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +11 to hit, reach 10 ft., one target.Hit: 17 (2d10 + 6) piercing damage.",
            "Claw.Melee Weapon Attack: +11 to hit, reach 5 ft., one target.Hit: 13 (2d6 + 6) slashing damage.",
            "Tail.Melee Weapon Attack: +11 to hit, reach 15 ft., one target.Hit: 15 (2d8 + 6) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 16 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.",
            "Fire Breath. The dragon exhales fire in an 60-foot line that is 5 feet wide. Each creature in that line must make a DC 18 Dexterity saving throw, taking 45 (13d6) fire damage on a failed save, or half as much damage on a successful one.",
            "Sleep Breath. The dragon exhales sleep gas in a 60-foot cone. Each creature in that area must succeed on a DC 18 Constitution saving throw or fall unconscious for 10 minutes. This effect ends for a creature if the creature takes damage or someone uses an action to wake it."
        ]
    },
    "adult-bronze-dragon": {
        "name": "Adult Bronze Dragon",
        "type": "Huge dragon (Metallic)",
        "alignment": "lawful good",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "212 (17d12 + 102)",
        "Speed": "40 ft., fly 80 ft., swim 40 ft.",
        "Saving Throws": "Dex +5, Con +11, Wis +7, Cha +9",
        "Skills": "Insight +7, Perception +12, Stealth +5",
        "Damage Immunities": "lightning",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 22",
        "Languages": "Common, Draconic",
        "Challenge": "15 (13000 XP)",
        "STR": "25 (+7)",
        "DEX": "10 (+0)",
        "CON": "23 (+6)",
        "INT": "16 (+3)",
        "WIS": "15 (+2)",
        "CHA": "19 (+4)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 20 Dexterity saving throw or take 14 (2d6 + 7) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
        ],
        "features": [
            "Amphibious. The dragon can breathe air and water.",
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +12 to hit, reach 10 ft., one target.Hit: 18 (2d10 + 7) piercing damage.",
            "Claw.Melee Weapon Attack: +12 to hit, reach 5 ft., one target.Hit: 14 (2d6 + 7) slashing damage.",
            "Tail.Melee Weapon Attack: +12 to hit, reach 15 ft., one target.Hit: 16 (2d8 + 7) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 17 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.",
            "Lightning Breath. The dragon exhales lightning in a 90-foot line that is 5 feet wide. Each creature in that line must make a DC 19 Dexterity saving throw, taking 66 (12d10) lightning damage on a failed save, or half as much damage on a successful one.",
            "Repulsion Breath. The dragon exhales repulsion energy in a 30-foot cone. Each creature in that area must succeed on a DC 19 Strength saving throw. On a failed save, the creature is pushed 60 feet away from the dragon.",
            "Change Shape. The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice). In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."
        ]
    },
    "adult-copper-dragon": {
        "name": "Adult Copper Dragon",
        "type": "Huge dragon (Metallic)",
        "alignment": "chaotic good",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "184 (16d12 + 80)",
        "Speed": "40 ft., climb 40 ft., fly 80 ft.",
        "Saving Throws": "Dex +6, Con +10, Wis +7, Cha +8",
        "Skills": "Deception +8, Perception +12, Stealth +6",
        "Damage Immunities": "acid",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 22",
        "Languages": "Common, Draconic",
        "Challenge": "14 (11500 XP)",
        "STR": "23 (+6)",
        "DEX": "12 (+1)",
        "CON": "21 (+5)",
        "INT": "18 (+4)",
        "WIS": "15 (+2)",
        "CHA": "17 (+3)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 19 Dexterity saving throw or take 13 (2d6 + 6) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying Speed."
        ],
        "features": [
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +11 to hit, reach 10 ft., one target.Hit: 17 (2d10 + 6) piercing damage.",
            "Claw.Melee Weapon Attack: +11 to hit, reach 5 ft., one target.Hit: 13 (2d6 + 6) slashing damage.",
            "Tail.Melee Weapon Attack: +11 to hit, reach 15 ft., one target.Hit: 15 (2d8 + 6) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 16 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.",
            "Acid Breath. The dragon exhales acid in an 60-foot line that is 5 feet wide. Each creature in that line must make a DC 18 Dexterity saving throw, taking 54 (12d8) acid damage on a failed save, or half as much damage on a successful one.",
            "Slowing Breath. The dragon exhales gas in a 60-foot cone. Each creature in that area must succeed on a DC 18 Constitution saving throw. On a failed save, the creature can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the creature can use either an action or a bonus action on its turn, but not both. These effects last for 1 minute. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself with a successful save."
        ]
    },
    "adult-gold-dragon": {
        "name": "Adult Gold Dragon",
        "type": "Huge dragon (Metallic)",
        "alignment": "lawful good",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "256 (19d12 + 133)",
        "Speed": "40 ft., fly 80 ft., swim 40 ft.",
        "Saving Throws": "Dex +8, Con +13, Wis +8, Cha +13",
        "Skills": "Insight +8, Perception +14, Persuasion +13, Stealth +8",
        "Damage Immunities": "fire",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 24",
        "Languages": "Common, Draconic",
        "Challenge": "17 (18000 XP)",
        "STR": "27 (+8)",
        "DEX": "14 (+2)",
        "CON": "25 (+7)",
        "INT": "16 (+3)",
        "WIS": "15 (+2)",
        "CHA": "24 (+7)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 22 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying Speed."
        ],
        "features": [
            "Amphibious. The dragon can breathe air and water.",
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +14 to hit, reach 10 ft., one target.Hit: 19 (2d10 + 8) piercing damage.",
            "Claw.Melee Weapon Attack: +14 to hit, reach 5 ft., one target.Hit: 15 (2d6 + 8) slashing damage.",
            "Tail.Melee Weapon Attack: +14 to hit, reach 15 ft., one target.Hit: 17 (2d8 + 8) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 21 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.",
            "Fire Breath. The dragon exhales fire in a 60-foot cone. Each creature in that area must make a DC 21 Dexterity saving throw, taking 66 (12d10) fire damage on a failed save, or half as much damage on a successful one.",
            "Weakening Breath. The dragon exhales gas in a 60-foot cone. Each creature in that area must succeed on a DC 21 Strength saving throw or have disadvantage on Strength-based attack rolls, Strength checks, and Strength saving throws for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
            "Change Shape. The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice). In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."
        ]
    },
    "adult-green-dragon": {
        "name": "Adult Green Dragon",
        "type": "Huge dragon (Chromatic)",
        "alignment": "lawful evil",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "207 (18d12 + 90)",
        "Speed": "40 ft., fly 80 ft., swim 40 ft.",
        "Saving Throws": "Dex +6, Con +10, Wis +7, Cha +8",
        "Skills": "Deception +8, Insight +7, Perception +12, Persuasion +8, Stealth +6",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 22",
        "Languages": "Common, Draconic",
        "Challenge": "15 (13000 XP)",
        "STR": "23 (+6)",
        "DEX": "12 (+1)",
        "CON": "21 (+5)",
        "INT": "18 (+4)",
        "WIS": "15 (+2)",
        "CHA": "17 (+3)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 19 Dexterity saving throw or take 13 (2d6 + 6) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
        ],
        "features": [
            "Amphibious. The dragon can breathe air and water.",
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +11 to hit, reach 10 ft., one target.Hit: 17 (2d10 + 6) piercing damage plus 7 (2d6) poison damage.",
            "Claw.Melee Weapon Attack: +11 to hit, reach 5 ft., one target.Hit: 13 (2d6 + 6) slashing damage.",
            "Tail.Melee Weapon Attack: +11 to hit, reach 15 ft., one target.Hit: 15 (2d8 + 6) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 16 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Poison Breath (Recharge 5-6). The dragon exhales poisonous gas in a 60-foot cone. Each creature in that area must make a DC 18 Constitution saving throw, taking 56 (16d6) poison damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "adult-red-dragon": {
        "name": "Adult Red Dragon",
        "type": "Huge dragon (Chromatic)",
        "alignment": "chaotic evil",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "256 (19d12 + 133)",
        "Speed": "40 ft., climb 40 ft., fly 80 ft.",
        "Saving Throws": "Dex +6, Con +13, Wis +7, Cha +11",
        "Skills": "Perception +13, Stealth +6",
        "Damage Immunities": "fire",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 23",
        "Languages": "Common, Draconic",
        "Challenge": "17 (18000 XP)",
        "STR": "27 (+8)",
        "DEX": "10 (+0)",
        "CON": "25 (+7)",
        "INT": "16 (+3)",
        "WIS": "13 (+1)",
        "CHA": "21 (+5)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 22 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
        ],
        "features": [
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +14 to hit, reach 10 ft., one target.Hit: 19 (2d10 + 8) piercing damage plus 7 (2d6) fire damage.",
            "Claw.Melee Weapon Attack: +14 to hit, reach 5 ft., one target.Hit: 15 (2d6 + 8) slashing damage.",
            "Tail.Melee Weapon Attack: +14 to hit, reach 15 ft., one target.Hit: 17 (2d8 + 8) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 19 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Fire Breath (Recharge 5-6). The dragon exhales fire in a 60-foot cone. Each creature in that area must make a DC 21 Dexterity saving throw, taking 63 (18d6) fire damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "adult-silver-dragon": {
        "name": "Adult Silver Dragon",
        "type": "Huge dragon (Metallic)",
        "alignment": "lawful good",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "243 (18d12 + 126)",
        "Speed": "40 ft., fly 80 ft.",
        "Saving Throws": "Dex +5, Con +12, Wis +6, Cha +10",
        "Skills": "Arcana +8, History +8, Perception +11, Stealth +5",
        "Damage Immunities": "cold",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 21",
        "Languages": "Common, Draconic",
        "Challenge": "16 (15000 XP)",
        "STR": "27 (+8)",
        "DEX": "10 (+0)",
        "CON": "25 (+7)",
        "INT": "16 (+3)",
        "WIS": "13 (+1)",
        "CHA": "21 (+5)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 21 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying Speed."
        ],
        "features": [
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +13 to hit, reach 10 ft., one target.Hit: 19 (2d10 + 8) piercing damage.",
            "Claw.Melee Weapon Attack: +13 to hit, reach 5 ft., one target.Hit: 15 (2d6 + 8) slashing damage.",
            "Tail.Melee Weapon Attack: +13 to hit, reach 15 ft., one target.Hit: 17 (2d8 + 8) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 18 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.",
            "Cold Breath. The dragon exhales an icy blast in a 60-foot cone. Each creature in that area must make a DC 20 Constitution saving throw, taking 58 (13d8) cold damage on a failed save, or half as much damage on a successful one.",
            "Paralyzing Breath. The dragon exhales paralyzing gas in a 60-foot cone. Each creature in that area must succeed on a DC 20 Constitution saving throw or be paralyzed for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
            "Change Shape. The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice). In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."
        ]
    },
    "adult-white-dragon": {
        "name": "Adult White Dragon",
        "type": "Huge dragon (Chromatic)",
        "alignment": "chaotic evil",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "200 (16d12 + 96)",
        "Speed": "40 ft., burrow 30 ft., fly 80 ft., swim 40 ft.",
        "Saving Throws": "Dex +5, Con +11, Wis +6, Cha +6",
        "Skills": "Perception +11, Stealth +5",
        "Damage Immunities": "cold",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 21",
        "Languages": "Common, Draconic",
        "Challenge": "13 (10000 XP)",
        "STR": "22 (+6)",
        "DEX": "10 (+0)",
        "CON": "22 (+6)",
        "INT": "8 (-1)",
        "WIS": "12 (+1)",
        "CHA": "12 (+1)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 10 feet of the dragon must succeed on a DC 19 Dexterity saving throw or take 13 (2d6 + 6) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
        ],
        "features": [
            "Ice Walk. The dragon can move across and climb icy surfaces without needing to make an ability check. Additionally, difficult terrain composed of ice or snow doesn't cost it extra moment.",
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +11 to hit, reach 10 ft., one target.Hit: 17 (2d10 + 6) piercing damage plus 4 (1d8) cold damage.",
            "Claw.Melee Weapon Attack: +11 to hit, reach 5 ft., one target.Hit: 13 (2d6 + 6) slashing damage.",
            "Tail.Melee Weapon Attack: +11 to hit, reach 15 ft., one target.Hit: 15 (2d8 + 6) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 14 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Cold Breath (Recharge 5-6). The dragon exhales an icy blast in a 60-foot cone. Each creature in that area must make a DC 19 Constitution saving throw, taking 54 (12d8) cold damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "air-elemental": {
        "name": "Air Elemental",
        "type": "Large elemental",
        "alignment": "neutral",
        "Armor Class": "15",
        "Hit Points": "90 (12d10 + 24)",
        "Speed": "0 ft., fly 90 ft. (hover)",
        "Damage Resistances": "lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "poison",
        "Condition Immunities": "exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Auran",
        "Challenge": "5 (1800 XP)",
        "STR": "14 (+2)",
        "DEX": "20 (+5)",
        "CON": "14 (+2)",
        "INT": "6 (-2)",
        "WIS": "10 (+0)",
        "CHA": "6 (-2)",
        "features": [
            "Air Form. The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing."
        ],
        "Actions": [
            "Multiattack. The elemental makes two slam attacks.",
            "Slam.Melee Weapon Attack: +8 to hit, reach 5 ft., one target.Hit: 14 (2d8 + 5) bludgeoning damage.",
            "Whirlwind (Recharge 4-6). Each creature in the elemental's space must make a DC 13 Strength saving throw. On a failure, a target takes 15 (3d8 + 2) bludgeoning damage and is flung up 20 feet away from the elemental in a random direction and knocked prone. If a thrown target strikes an object, such as a wall or floor, the target takes 3 (1d6) bludgeoning damage for every 10 feet it was thrown. If the target is thrown at another creature, that creature must succeed on a DC 13 Dexterity saving throw or take the same damage and be knocked prone. If the saving throw is successful, the target takes half the bludgeoning damage and isn't flung away or knocked prone."
        ]
    },
    "allosaurus": {
        "name": "Allosaurus",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "51 (6d10 + 18)",
        "Speed": "60 ft.",
        "Skills": "Perception +5",
        "Senses": "passive Perception 15",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "19 (+4)",
        "DEX": "13 (+1)",
        "CON": "17 (+3)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "5 (-3)",
        "features": [
            "Pounce. If the allosaurus moves at least 30 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone. If the target is prone, the allosaurus can make one bite attack against it as a bonus action."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 15 (2d10 + 4) piercing damage.",
            "Claw.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 8 (1d8 + 4) slashing damage."
        ]
    },
    "ancient-black-dragon": {
        "name": "Ancient Black Dragon",
        "type": "Gargantuan dragon (Chromatic)",
        "alignment": "chaotic evil",
        "Armor Class": "22 (natural armor)",
        "Hit Points": "367 (21d20 + 147)",
        "Speed": "40 ft., fly 80 ft., swim 40 ft.",
        "Saving Throws": "Dex +9, Con +14, Wis +9, Cha +11",
        "Skills": "Perception +16, Stealth +9",
        "Damage Immunities": "acid",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 26",
        "Languages": "Common, Draconic",
        "Challenge": "21 (33000 XP)",
        "STR": "27 (+8)",
        "DEX": "14 (+2)",
        "CON": "25 (+7)",
        "INT": "16 (+3)",
        "WIS": "15 (+2)",
        "CHA": "19 (+4)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 15 feet of the dragon must succeed on a DC 23 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying Speed."
        ],
        "features": [
            "Amphibious. The dragon can breathe air and water.",
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +15 to hit, reach 15 ft., one target.Hit: 19 (2d10 + 8) piercing damage plus 9 (2d8) acid damage.",
            "Claw.Melee Weapon Attack: +15 to hit, reach 10 ft., one target.Hit: 15 (2d6 + 8) slashing damage.",
            "Tail.Melee Weapon Attack: +15 to hit, reach 20 ft., one target.Hit: 17 (2d8 + 8) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 19 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Acid Breath (Recharge 5-6). The dragon exhales acid in a 90-foot line that is 10 feet wide. Each creature in that line must make a DC 22 Dexterity saving throw, taking 67 (15d8) acid damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "ancient-blue-dragon": {
        "name": "Ancient Blue Dragon",
        "type": "Gargantuan dragon (Chromatic)",
        "alignment": "lawful evil",
        "Armor Class": "22 (natural armor)",
        "Hit Points": "481 (26d20 + 208)",
        "Speed": "40 ft., burrow 40 ft., fly 80 ft.",
        "Saving Throws": "Dex +7, Con +15, Wis +10, Cha +12",
        "Skills": "Perception +17, Stealth +7",
        "Damage Immunities": "lightning",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 27",
        "Languages": "Common, Draconic",
        "Challenge": "23 (50000 XP)",
        "STR": "29 (+9)",
        "DEX": "10 (+0)",
        "CON": "27 (+8)",
        "INT": "18 (+4)",
        "WIS": "17 (+3)",
        "CHA": "21 (+5)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 15 feet of the dragon must succeed on a DC 24 Dexterity saving throw or take 16 (2d6 + 9) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying Speed."
        ],
        "features": [
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +16 to hit, reach 15 ft., one target.Hit: 20 (2d10 + 9) piercing damage plus 11 (2d10) lightning damage.",
            "Claw.Melee Weapon Attack: +16 to hit, reach 10 ft., one target.Hit: 16 (2d6 + 9) slashing damage.",
            "Tail.Melee Weapon Attack: +16 to hit, reach 20 ft., one target.Hit: 18 (2d8 + 9) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 20 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Lightning Breath (Recharge 5-6). The dragon exhales lightning in a 120-foot line that is 10 feet wide. Each creature in that line must make a DC 23 Dexterity saving throw, taking 88 (16d10) lightning damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "ancient-brass-dragon": {
        "name": "Ancient Brass Dragon",
        "type": "Gargantuan dragon (Metallic)",
        "alignment": "chaotic good",
        "Armor Class": "20 (natural armor)",
        "Hit Points": "297 (17d20 + 119)",
        "Speed": "40 ft., burrow 40 ft., fly 80 ft.",
        "Saving Throws": "Dex +6, Con +13, Wis +8, Cha +10",
        "Skills": "History +9, Perception +14, Persuasion +10, Stealth +6",
        "Damage Immunities": "fire",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 24",
        "Languages": "Common, Draconic",
        "Challenge": "20 (25000 XP)",
        "STR": "27 (+8)",
        "DEX": "10 (+0)",
        "CON": "25 (+7)",
        "INT": "16 (+3)",
        "WIS": "15 (+2)",
        "CHA": "19 (+4)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 15 feet of the dragon must succeed on a DC 22 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying Speed."
        ],
        "features": [
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +14 to hit, reach 15 ft., one target.Hit: 19 (2d10 + 8) piercing damage.",
            "Claw.Melee Weapon Attack: +14 to hit, reach 10 ft., one target.Hit: 15 (2d6 + 8) slashing damage.",
            "Tail.Melee Weapon Attack: +14 to hit, reach 20 ft., one target.Hit: 17 (2d8 + 8) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 18 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons:",
            "Fire Breath. The dragon exhales fire in an 90-foot line that is 10 feet wide. Each creature in that line must make a DC 21 Dexterity saving throw, taking 56 (16d6) fire damage on a failed save, or half as much damage on a successful one.",
            "Sleep Breath. The dragon exhales sleep gas in a 90-foot cone. Each creature in that area must succeed on a DC 21 Constitution saving throw or fall unconscious for 10 minutes. This effect ends for a creature if the creature takes damage or someone uses an action to wake it.",
            "Change Shape. The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice). In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."
        ]
    },
    "ancient-bronze-dragon": {
        "name": "Ancient Bronze Dragon",
        "type": "Gargantuan dragon (Metallic)",
        "alignment": "lawful good",
        "Armor Class": "22 (natural armor)",
        "Hit Points": "444 (24d20 + 192)",
        "Speed": "40 ft., fly 80 ft., swim 40 ft.",
        "Saving Throws": "Dex +7, Con +15, Wis +10, Cha +12",
        "Skills": "Insight +10, Perception +17, Stealth +7",
        "Damage Immunities": "lightning",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 27",
        "Languages": "Common, Draconic",
        "Challenge": "22 (41000 XP)",
        "STR": "29 (+9)",
        "DEX": "10 (+0)",
        "CON": "27 (+8)",
        "INT": "18 (+4)",
        "WIS": "17 (+3)",
        "CHA": "21 (+5)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 15 feet of the dragon must succeed on a DC 24 Dexterity saving throw or take 16 (2d6 + 9) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying Speed."
        ],
        "features": [
            "Amphibious. The dragon can breathe air and water.",
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +16 to hit, reach 15 ft., one target.Hit: 20 (2d10 + 9) piercing damage.",
            "Claw.Melee Weapon Attack: +16 to hit, reach 10 ft., one target.Hit: 16 (2d6 + 9) slashing damage.",
            "Tail.Melee Weapon Attack: +16 to hit, reach 20 ft., one target.Hit: 18 (2d8 + 9) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 20 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.",
            "Lightning Breath. The dragon exhales lightning in a 120-foot line that is 10 feet wide. Each creature in that line must make a DC 23 Dexterity saving throw, taking 88 (16d10) lightning damage on a failed save, or half as much damage on a successful one.",
            "Repulsion Breath. The dragon exhales repulsion energy in a 30-foot cone. Each creature in that area must succeed on a DC 23 Strength saving throw. On a failed save, the creature is pushed 60 feet away from the dragon.",
            "Change Shape. The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice). In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."
        ]
    },
    "ancient-copper-dragon": {
        "name": "Ancient Copper Dragon",
        "type": "Gargantuan dragon (Metallic)",
        "alignment": "chaotic good",
        "Armor Class": "21 (natural armor)",
        "Hit Points": "350 (20d20 + 140)",
        "Speed": "40 ft., climb 40 ft., fly 80 ft.",
        "Saving Throws": "Dex +8, Con +14, Wis +10, Cha +11",
        "Skills": "Deception +11, Perception +17, Stealth +8",
        "Damage Immunities": "acid",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 27",
        "Languages": "Common, Draconic",
        "Challenge": "21 (33000 XP)",
        "STR": "27 (+8)",
        "DEX": "12 (+1)",
        "CON": "25 (+7)",
        "INT": "20 (+5)",
        "WIS": "17 (+3)",
        "CHA": "19 (+4)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 15 feet of the dragon must succeed on a DC 23 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying Speed."
        ],
        "features": [
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +15 to hit, reach 15 ft., one target.Hit: 19 (2d10 + 8) piercing damage.",
            "Claw.Melee Weapon Attack: +15 to hit, reach 10 ft., one target.Hit: 15 (2d6 + 8) slashing damage.",
            "Tail.Melee Weapon Attack: +15 to hit, reach 20 ft., one target.Hit: 17 (2d8 + 8) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 19 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.",
            "Acid Breath. The dragon exhales acid in an 90-foot line that is 10 feet wide. Each creature in that line must make a DC 22 Dexterity saving throw, taking 63 (14d8) acid damage on a failed save, or half as much damage on a successful one.",
            "Slowing Breath. The dragon exhales gas in a 90-foot cone. Each creature in that area must succeed on a DC 22 Constitution saving throw. On a failed save, the creature can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the creature can use either an action or a bonus action on its turn, but not both. These effects last for 1 minute. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself with a successful save.",
            "Change Shape. The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice). In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."
        ]
    },
    "ancient-gold-dragon": {
        "name": "Ancient Gold Dragon",
        "type": "Gargantuan dragon (Metallic)",
        "alignment": "lawful good",
        "Armor Class": "22 (natural armor)",
        "Hit Points": "546 (28d20 + 252)",
        "Speed": "40 ft., fly 80 ft., swim 40 ft.",
        "Saving Throws": "Dex +9, Con +16, Wis +10, Cha +16",
        "Skills": "Insight +10, Perception +17, Persuasion +16, Stealth +9",
        "Damage Immunities": "fire",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 27",
        "Languages": "Common, Draconic",
        "Challenge": "24 (62000 XP)",
        "STR": "30 (+10)",
        "DEX": "14 (+2)",
        "CON": "29 (+9)",
        "INT": "18 (+4)",
        "WIS": "17 (+3)",
        "CHA": "28 (+9)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 15 feet of the dragon must succeed on a DC 25 Dexterity saving throw or take 17 (2d6 + 10) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying Speed."
        ],
        "features": [
            "Amphibious. The dragon can breathe air and water.",
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +17 to hit, reach 15 ft., one target.Hit: 21 (2d10 + 10) piercing damage.",
            "Claw.Melee Weapon Attack: +17 to hit, reach 10 ft., one target.Hit: 17 (2d6 + 10) slashing damage.",
            "Tail.Melee Weapon Attack: +17 to hit, reach 20 ft., one target.Hit: 19 (2d8 + 10) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 24 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.",
            "Fire Breath. The dragon exhales fire in a 90-foot cone. Each creature in that area must make a DC 24 Dexterity saving throw, taking 71 (13d10) fire damage on a failed save, or half as much damage on a successful one.",
            "Weakening Breath. The dragon exhales gas in a 90-foot cone. Each creature in that area must succeed on a DC 24 Strength saving throw or have disadvantage on Strength-based attack rolls, Strength checks, and Strength saving throws for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
            "Change Shape. The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice). In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."
        ]
    },
    "ancient-green-dragon": {
        "name": "Ancient Green Dragon",
        "type": "Gargantuan dragon (Chromatic)",
        "alignment": "lawful evil",
        "Armor Class": "21 (natural armor)",
        "Hit Points": "385 (22d20 + 154)",
        "Speed": "40 ft., fly 80 ft., swim 40 ft.",
        "Saving Throws": "Dex +8, Con +14, Wis +10, Cha +11",
        "Skills": "Deception +11, Insight +10, Perception +17, Persuasion +11, Stealth +8",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 27",
        "Languages": "Common, Draconic",
        "Challenge": "22 (41000 XP)",
        "STR": "27 (+8)",
        "DEX": "12 (+1)",
        "CON": "25 (+7)",
        "INT": "20 (+5)",
        "WIS": "17 (+3)",
        "CHA": "19 (+4)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 15 feet of the dragon must succeed on a DC 23 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying Speed."
        ],
        "features": [
            "Amphibious. The dragon can breathe air and water.",
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +15 to hit, reach 15 ft., one target.Hit: 19 (2d10 + 8) piercing damage plus 10 (3d6) poison damage.",
            "Claw.Melee Weapon Attack: +15 to hit, reach 10 ft., one target.Hit: 22 (4d6 + 8) slashing damage.",
            "Tail.Melee Weapon Attack: +15 to hit, reach 20 ft., one target.Hit: 17 (2d8 + 8) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 19 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Poison Breath (Recharge 5-6). The dragon exhales poisonous gas in a 90-foot cone. Each creature in that area must make a DC 22 Constitution saving throw, taking 77 (22d6) poison damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "ancient-red-dragon": {
        "name": "Ancient Red Dragon",
        "type": "Gargantuan dragon (Chromatic)",
        "alignment": "chaotic evil",
        "Armor Class": "22 (natural armor)",
        "Hit Points": "546 (28d20 + 252)",
        "Speed": "40 ft., climb 40 ft., fly 80 ft.",
        "Saving Throws": "Dex +7, Con +16, Wis +9, Cha +13",
        "Skills": "Perception +16, Stealth +7",
        "Damage Immunities": "fire",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 26",
        "Languages": "Common, Draconic",
        "Challenge": "24 (62000 XP)",
        "STR": "30 (+10)",
        "DEX": "10 (+0)",
        "CON": "29 (+9)",
        "INT": "18 (+4)",
        "WIS": "15 (+2)",
        "CHA": "23 (+6)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 15 feet of the dragon must succeed on a DC 25 Dexterity saving throw or take 17 (2d6 + 10) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying speed."
        ],
        "features": [
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite. Melee Weopon Attack: +17 to hit, reach 15 ft., one target.Hit: 21 (2d10 + 10) piercing damage plus 14 (4d6) fire damage.",
            "Claw.Melee Weapon Attack: +17 to hit, reach 10 ft., one target.Hit: 17 (2d6 + 10) slashing damage.",
            "Tail.Melee Weapon Attack: +17 to hit, reach 20 ft., one target.Hit: 19 (2d8 + 10) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 21 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Fire Breath (Recharge 5-6). The dragon exhales fire in a 90-foot cone. Each creature in that area must make a DC 24 Dexterity saving throw, taking 91 (26d6) fire damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "ancient-silver-dragon": {
        "name": "Ancient Silver Dragon",
        "type": "Gargantuan dragon (Metallic)",
        "alignment": "lawful good",
        "Armor Class": "22 (natural armor)",
        "Hit Points": "487 (25d20 + 225)",
        "Speed": "40 ft., fly 80 ft.",
        "Saving Throws": "Dex +7, Con +16, Wis +9, Cha +13",
        "Skills": "Arcana +11, History +11, Perception +16, Stealth +7",
        "Damage Immunities": "cold",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 26",
        "Languages": "Common, Draconic",
        "Challenge": "23 (50000 XP)",
        "STR": "30 (+10)",
        "DEX": "10 (+0)",
        "CON": "29 (+9)",
        "INT": "18 (+4)",
        "WIS": "15 (+2)",
        "CHA": "23 (+6)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 15 feet of the dragon must succeed on a DC 25 Dexterity saving throw or take 17 (2d6 + 10) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying Speed."
        ],
        "features": [
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +17 to hit, reach 15 ft., one target.Hit: 21 (2d10 + 10) piercing damage.",
            "Claw.Melee Weapon Attack: +17 to hit, reach 10 ft., one target.Hit: 17 (2d6 + 10) slashing damage.",
            "Tail.Melee Weapon Attack: +17 to hit, reach 20 ft., one target.Hit: 19 (2d8 + 10) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 21 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.",
            "Cold Breath. The dragon exhales an icy blast in a 90-foot cone. Each creature in that area must make a DC 24 Constitution saving throw, taking 67 (15d8) cold damage on a failed save, or half as much damage on a successful one.",
            "Paralyzing Breath. The dragon exhales paralyzing gas in a 90-foot cone. Each creature in that area must succeed on a DC 24 Constitution saving throw or be paralyzed for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
            "Change Shape. The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice). In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."
        ]
    },
    "ancient-white-dragon": {
        "name": "Ancient White Dragon",
        "type": "Gargantuan dragon (Chromatic)",
        "alignment": "chaotic evil",
        "Armor Class": "20 (natural armor)",
        "Hit Points": "333 (18d20 + 144)",
        "Speed": "40 ft., burrow 40 ft., fly 80 ft., swim 40 ft.",
        "Saving Throws": "Dex +6, Con +14, Wis +7, Cha +8",
        "Skills": "Perception +13, Stealth +6",
        "Damage Immunities": "cold",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 23",
        "Languages": "Common, Draconic",
        "Challenge": "20 (25000 XP)",
        "STR": "26 (+8)",
        "DEX": "10 (+0)",
        "CON": "26 (+8)",
        "INT": "10 (+0)",
        "WIS": "13 (+1)",
        "CHA": "14 (+2)",
        "Legendary actions": [
            "The dragon can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The dragon regains spent legendary actions at the start of its turn.",
            "Detect. The dragon makes a Wisdom (Perception) check.",
            "Tail Attack. The dragon makes a tail attack.",
            "Wing Attack (Costs 2 Actions). The dragon beats its wings. Each creature within 15 feet of the dragon must succeed on a DC 22 Dexterity saving throw or take 15 (2d6 + 8) bludgeoning damage and be knocked prone. The dragon can then fly up to half its flying Speed."
        ],
        "features": [
            "Ice Walk. The dragon can move across and climb icy surfaces without needing to make an ability check. Additionally, difficult terrain composed of ice or snow doesn't cost it extra moment.",
            "Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."
        ],
        "Actions": [
            "Multiattack. The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +14 to hit, reach 15 ft., one target.Hit: 19 (2d10 + 8) piercing damage plus 9 (2d8) cold damage.",
            "Claw.Melee Weapon Attack: +14 to hit, reach 10 ft., one target.Hit: 15 (2d6 + 8) slashing damage.",
            "Tail.Melee Weapon Attack: +14 to hit, reach 20 ft., one target.Hit: 17 (2d8 + 8) bludgeoning damage.",
            "Frightful Presence. Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 16 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours.",
            "Cold Breath (Recharge 5-6). The dragon exhales an icy blast in a 90-foot cone. Each creature in that area must make a DC 22 Constitution saving throw, taking 72 (16d8) cold damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "androsphinx": {
        "name": "Androsphinx",
        "type": "Large monstrosity",
        "alignment": "lawful neutral",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "199 (19d10 + 95)",
        "Speed": "40 ft., fly 60 ft.",
        "Saving Throws": "Dex +6, Con +11, Int +9, Wis +10",
        "Skills": "Arcana +9, Perception +10, Religion +15",
        "Damage Immunities": "psychic; bludgeoning, piercing and slashing from nonmagical attacks",
        "Condition Immunities": "charmed, frightened",
        "Senses": "truesight 120 ft., passive Perception 20",
        "Languages": "Common, Sphinx",
        "Challenge": "17 (18000 XP)",
        "STR": "22 (+6)",
        "DEX": "10 (+0)",
        "CON": "20 (+5)",
        "INT": "16 (+3)",
        "WIS": "18 (+4)",
        "CHA": "23 (+6)",
        "Legendary actions": [
            "The sphinx can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The sphinx regains spent legendary actions at the start of its turn.",
            "Claw Attack. The sphinx makes one claw attack.",
            "Teleport (Costs 2 Actions). The sphinx magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see.",
            "Cast a Spell (Costs 3 Actions). The sphinx casts a spell from its list of prepared spells, using a spell slot as normal."
        ],
        "features": [
            "Inscrutable. The sphinx is immune to any effect that would sense its emotions or read its thoughts, as well as any divination spell that it refuses. Wisdom (Insight) checks made to ascertain the sphinx's intentions or sincerity have disadvantage.",
            "Magic Weapons. The sphinx's weapon attacks are magical.",
            "Spellcasting. The sphinx is a 12th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 18, +10 to hit with spell attacks). It requires no material components to cast its spells. The sphinx has the following cleric spells prepared:"
        ],
        "Actions": [
            "Multiattack. The sphinx makes two claw attacks.",
            "Claw.Melee Weapon Attack: +12 to hit, reach 5 ft., one target.Hit: 17 (2d10 + 6) slashing damage.",
            "Roar (3/Day). The sphinx emits a magical roar. Each time it roars before finishing a long rest, the roar is louder and the effect is different, as detailed below. Each creature within 500 feet of the sphinx and able to hear the roar must make a saving throw.",
            "First Roar. Each creature that fails a DC 18 Wisdom saving throw is frightened for 1 minute. A frightened creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
            "Second Roar. Each creature that fails a DC 18 Wisdom saving throw is deafened and frightened for 1 minute. A frightened creature is paralyzed and can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
            "Third Roar. Each creature makes a DC 18 Constitution saving throw. On a failed save, a creature takes 44 (8d10) thunder damage and is knocked prone. On a successful save, the creature takes half as much damage and isn't knocked prone."
        ]
    },
    "animated-armor": {
        "name": "Animated Armor",
        "type": "Medium construct",
        "alignment": "unaligned",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "33 (6d8 + 6)",
        "Speed": "25 ft.",
        "Damage Immunities": "poison, psychic",
        "Condition Immunities": "blinded, charmed, deafened, exhaustion, frightened, paralyzed, petrified, poisoned",
        "Senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 6",
        "Languages": "\u2014",
        "Challenge": "1 (200 XP)",
        "STR": "14 (+2)",
        "DEX": "11 (+0)",
        "CON": "13 (+1)",
        "INT": "1 (-5)",
        "WIS": "3 (-4)",
        "CHA": "1 (-5)",
        "features": [
            "Antimagic Susceptibility. The armor is incapacitated while in the area of anantimagic field. If targeted bydispel magic, the armor must succeed on a Constitution saving throw against the caster's spell save DC or fall unconscious for 1 minute.",
            "False. Appearance. While the armor remains motionless, it is indistinguishable from a normal suit of armor."
        ],
        "Actions": [
            "Multiattack. The armor makes two melee attacks.",
            "Slam.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) bludgeoning damage."
        ]
    },
    "ankheg": {
        "name": "Ankheg",
        "type": "Large monstrosity",
        "alignment": "unaligned",
        "Armor Class": "14 (natural armor), 11 while prone",
        "Hit Points": "39 (6d10 + 6)",
        "Speed": "30 ft., burrow 10 ft.",
        "Senses": "darkvision 60 ft., tremorsense 60 ft., passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "17 (+3)",
        "DEX": "11 (+0)",
        "CON": "13 (+1)",
        "INT": "1 (-5)",
        "WIS": "13 (+1)",
        "CHA": "6 (-2)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) slashing damage plus 3 (1d6) acid damage. If the target is a Large or smaller creature, it is grappled (escape DC 13). Until this grapple ends, the ankheg can bite only the grappled creature and has advantage on attack rolls to do so.",
            "Acid Spray (Recharge 6). The ankheg spits acid in a line that is 30 feet long and 5 feet wide, provided that it has no creature grappled. Each creature in that line must make a DC 13 Dexterity saving throw, taking 10 (3d6) acid damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "ankylosaurus": {
        "name": "Ankylosaurus",
        "type": "Huge beast",
        "alignment": "unaligned",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "68 (8d12 + 16)",
        "Speed": "30 ft.",
        "Senses": "passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "3 (700 XP)",
        "STR": "19 (+4)",
        "DEX": "11 (+0)",
        "CON": "15 (+2)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "5 (-3)",
        "features": [],
        "Actions": [
            "Tail.Melee Weapon Attack: +7 to hit, reach 10 ft., one target.Hit: 18 (4d6 + 4) bludgeoning damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or be knocked prone."
        ]
    },
    "ape": {
        "name": "Ape",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "19 (3d8 + 6)",
        "Speed": "30 ft., climb 30 ft.",
        "Skills": "Athletics +5, Perception +3",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "16 (+3)",
        "DEX": "14 (+2)",
        "CON": "14 (+2)",
        "INT": "6 (-2)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [],
        "Actions": [
            "Multiattack. The ape makes two fist attacks.",
            "Fist.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 6 (1d6 + 3) bludgeoning damage.",
            "Rock.Ranged Weapon Attack: +5 to hit, range 25/50 ft., one target.Hit: 6 (1d6 + 3) bludgeoning damage."
        ]
    },
    "arcanaloth": {
        "name": "Arcanaloth",
        "type": "Medium fiend (Yugoloth)",
        "alignment": "neutral evil",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "104 (16d8 + 32)",
        "Speed": "30 ft., fly 30 ft.",
        "Saving Throws": "Dex +5, Int +9, Wis +7, Cha +7",
        "Skills": "Arcana +13, Deception +9, Insight +9, Perception +7",
        "Damage Resistances": "cold, fire, lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "acid, poison",
        "Condition Immunities": "charmed, poisoned",
        "Senses": "truesight 120 ft., passive Perception 17",
        "Languages": "all, telepathy 120 ft.",
        "Challenge": "12 (8400 XP)",
        "STR": "17 (+3)",
        "DEX": "12 (+1)",
        "CON": "14 (+2)",
        "INT": "20 (+5)",
        "WIS": "16 (+3)",
        "CHA": "17 (+3)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "archmage": {
        "name": "Archmage",
        "type": "Medium humanoid (any race)",
        "alignment": "any alignment",
        "Armor Class": "12 (15 with",
        "Hit Points": "99 (18d8 + 18)",
        "Speed": "30 ft.",
        "Saving Throws": "Int +9, Wis +6",
        "Skills": "Arcana +13, History +13",
        "Damage Resistances": "damage from spells; nonmagical bludgeoning, piercing, and slashing (from",
        "Senses": "passive Perception 12",
        "Languages": "any six languages",
        "Challenge": "12 (8400 XP)",
        "STR": "10 (+0)",
        "DEX": "14 (+2)",
        "CON": "12 (+1)",
        "INT": "20 (+5)",
        "WIS": "15 (+2)",
        "CHA": "16 (+3)",
        "features": [
            "Magic Resistance. The archmage has advantage on saving throws against spells and other magical effects.",
            "Spellcasting. The archmage is an 18th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 17, +9 to hit with spell attacks). The archmage can castdisguise selfandinvisibilityat will and has the following wizard spells prepared:"
        ],
        "Actions": [
            "Dagger.Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target.Hit: 4 (1d4 + 2) piercing damage."
        ]
    },
    "assassin": {
        "name": "Assassin",
        "type": "Medium humanoid (any race)",
        "alignment": "any non-good alignment",
        "Armor Class": "15 (studded leather)",
        "Hit Points": "78 (12d8 + 24)",
        "Speed": "30 ft.",
        "Saving Throws": "Dex +6, Int +4",
        "Skills": "Acrobatics +6, Deception +3, Perception +3, Stealth +9",
        "Damage Resistances": "poison",
        "Senses": "passive Perception 13",
        "Languages": "Thieves' cant plus any two languages",
        "Challenge": "8 (3900 XP)",
        "STR": "11 (+0)",
        "DEX": "16 (+3)",
        "CON": "14 (+2)",
        "INT": "13 (+1)",
        "WIS": "11 (+0)",
        "CHA": "10 (+0)",
        "features": [
            "Assassinate. During its first turn, the assassin has advantage on attack rolls against any creature that hasn't taken a turn. Any hit the assassin scores against a surprised creature is a critical hit.",
            "Evasion. If the assassin is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, the assassin instead takes no damage if it succeeds on the saving throw, and only half damage if it fails.",
            "Sneak Attack. Once per turn, the assassin deals an extra 14 (4d6) damage when it hits a target with a weapon attack and has advantage on the attack roll, or when the target is within 5 feet of an ally of the assassin that isn't incapacitated and the assassin doesn't have disadvantage on the attack roll."
        ],
        "Actions": [
            "Multiattack. The assassin makes two shortsword attacks.",
            "Shortsword.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 6 (1d6 + 3) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 24 (7d6) poison damage on a failed save, or half as much damage on a successful one.",
            "Light Crossbow.Ranged Weapon Attack: +6 to hit, range 80/320 ft., one target.Hit: 7 (1d8 + 3) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 24 (7d6) poison damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "awakened-shrub": {
        "name": "Awakened Shrub",
        "type": "Small plant",
        "alignment": "unaligned",
        "Armor Class": "9",
        "Hit Points": "10 (3d6)",
        "Speed": "20 ft.",
        "Damage Vulnerabilities": "fire",
        "Damage Resistances": "piercing",
        "Senses": "passive Perception 10",
        "Languages": "one language known by its creator",
        "Challenge": "0 (10 XP)",
        "STR": "3 (-4)",
        "DEX": "8 (-1)",
        "CON": "11 (+0)",
        "INT": "10 (+0)",
        "WIS": "10 (+0)",
        "CHA": "6 (-2)",
        "features": [
            "False Appearance. While the shrub remains motionless, it is indistinguishable from a normal shrub."
        ],
        "Actions": [
            "Rake.Melee Weapon Attack: +1 to hit, reach 5 ft., one target.Hit: 1 (1d4 - 1) slashing damage."
        ]
    },
    "awakened-tree": {
        "name": "Awakened Tree",
        "type": "Huge plant",
        "alignment": "unaligned",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "59 (7d12 + 14)",
        "Speed": "20 ft.",
        "Damage Vulnerabilities": "fire",
        "Damage Resistances": "bludgeoning, piercing",
        "Senses": "passive Perception 10",
        "Languages": "one language known by its creator",
        "Challenge": "2 (450 XP)",
        "STR": "19 (+4)",
        "DEX": "6 (-2)",
        "CON": "15 (+2)",
        "INT": "10 (+0)",
        "WIS": "10 (+0)",
        "CHA": "7 (-2)",
        "features": [
            "False Appearance. While the tree remains motionless, it is indistinguishable from a normal tree."
        ],
        "Actions": [
            "Slam.Melee Weapon Attack: +6 to hit, reach 10 ft., one target.Hit: 14 (3d6 + 4) bludgeoning damage."
        ]
    },
    "axe-beak": {
        "name": "Axe Beak",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "11",
        "Hit Points": "19 (3d10 + 3)",
        "Speed": "50 ft.",
        "Senses": "passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "14 (+2)",
        "DEX": "12 (+1)",
        "CON": "12 (+1)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "5 (-3)",
        "features": [],
        "Actions": [
            "Beak.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 6 (1d8 + 2) slashing damage."
        ]
    },
    "azer": {
        "name": "Azer",
        "type": "Medium elemental",
        "alignment": "lawful neutral",
        "Armor Class": "17 (natural armor, shield)",
        "Hit Points": "39 (6d8 + 12)",
        "Speed": "30 ft.",
        "Saving Throws": "Con +4",
        "Damage Immunities": "fire, poison",
        "Condition Immunities": "poisoned",
        "Senses": "passive Perception 11",
        "Languages": "Ignan",
        "Challenge": "2 (450 XP)",
        "STR": "17 (+3)",
        "DEX": "12 (+1)",
        "CON": "15 (+2)",
        "INT": "12 (+1)",
        "WIS": "13 (+1)",
        "CHA": "10 (+0)",
        "features": [
            "Heated Body. A creature that touches the azer or hits it with a melee attack while within 5 feet of it takes 5 (1d10) fire damage.",
            "Heated Weapons. When the azer hits with a metal melee weapon, it deals an extra 3 (1d6) fire damage (included in the attack).",
            "Illumination. The azer sheds bright light in a 10-foot radius and dim light for an additional 10 feet."
        ],
        "Actions": [
            "Warhammer.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 7 (1d8 + 3) bludgeoning damage, or 8 (1d10 + 3) bludgeoning damage if used with two hands to make a melee attack, plus 3 (1d6) fire damage."
        ]
    },
    "baboon": {
        "name": "Baboon",
        "type": "Small beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "3 (1d6)",
        "Speed": "30 ft., climb 30 ft.",
        "Senses": "passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "8 (-1)",
        "DEX": "14 (+2)",
        "CON": "11 (+0)",
        "INT": "4 (-3)",
        "WIS": "12 (+1)",
        "CHA": "6 (-2)",
        "features": [
            "Pack Tactics. The baboon has advantage on an attack roll against a creature if at least one of the baboon's allies is within 5 feet of the creature and the ally isn't incapacitated."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +1 to hit, reach 5 ft., one target.Hit: 1 (1d4 - 1) piercing damage."
        ]
    },
    "badger": {
        "name": "Badger",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "10",
        "Hit Points": "3 (1d4 + 1)",
        "Speed": "20 ft., burrow 5 ft.",
        "Senses": "darkvision 30 ft., passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "4 (-3)",
        "DEX": "11 (+0)",
        "CON": "12 (+1)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "5 (-3)",
        "features": [
            "Keen Smell. The badger has advantage on Wisdom (Perception) checks that rely on smell."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +2 to hit, reach 5 ft., one target.Hit: 1 piercing damage."
        ]
    },
    "balor": {
        "name": "Balor",
        "type": "Huge fiend (Demon)",
        "alignment": "chaotic evil",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "262 (21d12 + 126)",
        "Speed": "40 ft., fly 80 ft.",
        "Saving Throws": "Str +14, Con +12, Wis +9, Cha +12",
        "Damage Resistances": "cold, lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "fire, poison",
        "Condition Immunities": "poisoned",
        "Senses": "truesight 120 ft., passive Perception 13",
        "Languages": "Abyssal, telepathy 120 ft.",
        "Challenge": "19 (22000 XP)",
        "STR": "26 (+8)",
        "DEX": "15 (+2)",
        "CON": "22 (+6)",
        "INT": "20 (+5)",
        "WIS": "16 (+3)",
        "CHA": "22 (+6)",
        "features": [
            "Death Throes. When the balor dies, it explodes, and each creature within 30 feet of it must make a DC 20 Dexterity saving throw, taking 70 (20d6) fire damage on a failed save, or half as much damage on a successful one. The explosion ignites flammable objects in that area that aren't being worn or carried, and it destroys the balor's weapons.",
            "Fire Aura. At the start of each of the balor's turns, each creature within 5 feet of it takes 10 (3d6) fire damage, and flammable objects in the aura that aren't being worn or carried ignite. A creature that touches the balor or hits it with a melee attack while within 5 feet of it takes 10 (3d6) fire damage.",
            "Magic Resistance. The balor has advantage on saving throws against spells and other magical effects.",
            "Magic Weapons. The balor's weapon attacks are magical."
        ],
        "Actions": [
            "Multiattack. The balor makes two attacks: one with its longsword and one with its whip.",
            "Longsword.Melee Weapon Attack: +14 to hit, reach 10 ft., one target.Hit: 21 (3d8 + 8) slashing damage plus 13 (3d8) lightning damage. If the balor scores a critical hit, it rolls damage dice three times, instead of twice.",
            "Whip.Melee Weapon Attack: +14 to hit, reach 30 ft., one target.Hit: 15 (2d6 + 8) slashing damage plus 10 (3d6) fire damage, and the target must succeed on a DC 20 Strength saving throw or be pulled up to 25 feet toward the balor.",
            "Teleport. The balor magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see."
        ]
    },
    "bandit": {
        "name": "Bandit",
        "type": "Medium humanoid (any race)",
        "alignment": "any non-lawful alignment",
        "Armor Class": "12 (leather armor)",
        "Hit Points": "11 (2d8 + 2)",
        "Speed": "30 ft.",
        "Senses": "passive Perception 10",
        "Languages": "any one language (usually Common)",
        "Challenge": "1/8 (25 XP)",
        "STR": "11 (+0)",
        "DEX": "12 (+1)",
        "CON": "12 (+1)",
        "INT": "10 (+0)",
        "WIS": "10 (+0)",
        "CHA": "10 (+0)",
        "features": [],
        "Actions": [
            "Scimitar.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 4 (1d6 + 1) slashing damage.",
            "Light Crossbow.Ranged Weapon Attack: +3 to hit, range 80 ft./320 ft., one target.Hit: 5 (1d8 + 1) piercing damage."
        ]
    },
    "bandit-captain": {
        "name": "Bandit Captain",
        "type": "Medium humanoid (any race)",
        "alignment": "any non-lawful alignment",
        "Armor Class": "15 (studded leather)",
        "Hit Points": "65 (10d8 + 20)",
        "Speed": "30 ft.",
        "Saving Throws": "Str +4, Dex +5, Wis +2",
        "Skills": "Athletics +4, Deception +4",
        "Senses": "passive Perception 10",
        "Languages": "any two languages",
        "Challenge": "2 (450 XP)",
        "STR": "15 (+2)",
        "DEX": "16 (+3)",
        "CON": "14 (+2)",
        "INT": "14 (+2)",
        "WIS": "11 (+0)",
        "CHA": "14 (+2)",
        "features": [],
        "Actions": [
            "Multiattack. The captain makes three melee attacks: two with its scimitar and one with its dagger. Or the captain makes two ranged attacks with its daggers.",
            "Scimitar.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 6 (1d6 + 3) slashing damage.",
            "Dagger.Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target.Hit: 5 (1d4 + 3) piercing damage.",
            "Parry. The captain adds 2 to its AC against one melee attack that would hit it. To do so, the captain must see the attacker and be wielding a melee weapon."
        ]
    },
    "banshee": {
        "name": "Banshee",
        "type": "Medium undead",
        "alignment": "chaotic evil",
        "Armor Class": "12",
        "Hit Points": "58 (13d8)",
        "Speed": "0 ft., fly 40 ft. (hover)",
        "Saving Throws": "Wis +2, Cha +5",
        "Damage Resistances": "acid, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "cold, necrotic, poison",
        "Condition Immunities": "charmed, exhaustion, frightened, grappled, paralyzed, petrified, poisoned, prone, restrained",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Common, Elvish",
        "Challenge": "4 (1100 XP)",
        "STR": "1 (-5)",
        "DEX": "14 (+2)",
        "CON": "10 (+0)",
        "INT": "12 (+1)",
        "WIS": "11 (+0)",
        "CHA": "17 (+3)",
        "features": [
            "Detect Life. The banshee can magically sense the presence of creatures up to 5 miles away that aren't undead or constructs. She knows the general direction they're in but not their exact locations.",
            "Incorporeal Movement. The banshee can move through other creatures and objects as if they were difficult terrain. She takes 5 (1d10) force damage if she ends her turn inside an object."
        ],
        "Actions": [
            "Corrupting Touch.Melee Spell Attack: +4 to hit, reach 5 ft., one target.Hit: 12 (3d6 + 2) necrotic damage.",
            "Horrifying Visage. Each non-undead creature within 60 feet of the banshee that can see her must succeed on a DC 13 Wisdom saving throw or be frightened for 1 minute. A frightened target can repeat the saving throw at the end of each of its turns, with disadvantage if the banshee is within line of sight, ending the effect on itself on a success. If a target's saving throw is successful or the effect ends for it, the target is immune to the banshee's Horrifying Visage for the next 24 hours.",
            "Wail (1/Day). The banshee releases a mournful wail, provided that she isn't in sunlight. This wail has no effect on constructs and undead. All other creatures within 30 feet of her that can hear her must make a DC 13 Constitution saving throw. On a failure, a creature drops to 0 hit points. On a success, a creature takes 10 (3d6) psychic damage."
        ]
    },
    "barbed-devil": {
        "name": "Barbed Devil",
        "type": "Medium fiend (Devil)",
        "alignment": "lawful evil",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "110 (13d8 + 52)",
        "Speed": "30 ft.",
        "Saving Throws": "Str +6, Con +7, Wis +5, Cha +5",
        "Skills": "Deception +5, Insight +5, Perception +8",
        "Damage Resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered",
        "Damage Immunities": "fire, poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 120 ft., passive Perception 18",
        "Languages": "Infernal, telepathy 120 ft.",
        "Challenge": "5 (1800 XP)",
        "STR": "16 (+3)",
        "DEX": "17 (+3)",
        "CON": "18 (+4)",
        "INT": "12 (+1)",
        "WIS": "14 (+2)",
        "CHA": "14 (+2)",
        "features": [
            "Barbed Hide. At the start of each of its turns, the barbed devil deals 5 (1d10) piercing damage to any creature grappling it.",
            "Devil's Sight. Magical darkness doesn't impede the devil's darkvision.",
            "Magic Resistance. The devil has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack. The devil makes three melee attacks: one with its tail and two with its claws. Alternatively, it can use Hurl Flame twice.",
            "Claw.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 6 (1d6 + 3) piercing damage.",
            "Tail.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) piercing damage.",
            "Hurl Flame.Ranged Spell Attack: +5 to hit, range 150 ft., one target.Hit: 10 (3d6) fire damage. If the target is a flammable object that isn't being worn or carried, it also catches fire."
        ]
    },
    "barlgura": {
        "name": "Barlgura",
        "type": "Large fiend (Demon)",
        "alignment": "chaotic evil",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "68 (8d10 + 24)",
        "Speed": "40 ft., climb 40 ft.",
        "Saving Throws": "Dex +5, Con +6",
        "Skills": "Perception +5, Stealth +5",
        "Damage Resistances": "cold, fire, lightning",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "blindsight 30 ft., darkvision 120 ft., passive Perception 15",
        "Languages": "Abyssal, telepathy 120 ft.",
        "Challenge": "5 (1800 XP)",
        "STR": "18 (+4)",
        "DEX": "15 (+2)",
        "CON": "16 (+3)",
        "INT": "7 (-2)",
        "WIS": "14 (+2)",
        "CHA": "9 (-1)",
        "features": [
            "Innate Spellcasting. The barlgura's spellcasting ability is Wisdom (spell save DC 13). The barlgura can innately cast the following spells, requiring no material components:",
            "Reckless. At the start of its turn, the barlgura can gain advantage on all melee weapon attack rolls it makes during that turn, but attack rolls against it have advantage until the start of its next turn.",
            "Running Leap. The barlgura's long jump is up to 40 feet and its high jump is up to 20 feet when it has a running start."
        ],
        "Actions": [
            "Multiattack. The barlgura makes three attacks: one with its bite and two with its fists.",
            "Bite.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) piercing damage.",
            "Fist.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 9 (1d10 + 4) bludgeoning damage."
        ]
    },
    "basilisk": {
        "name": "Basilisk",
        "type": "Medium monstrosity",
        "alignment": "unaligned",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "52 (8d8 + 16)",
        "Speed": "20 ft.",
        "Senses": "darkvision 60 ft., passive Perception 9",
        "Languages": "\u2014",
        "Challenge": "3 (700 XP)",
        "STR": "16 (+3)",
        "DEX": "8 (-1)",
        "CON": "15 (+2)",
        "INT": "2 (-4)",
        "WIS": "8 (-1)",
        "CHA": "7 (-2)",
        "features": [
            "Petrifying Gaze. If a creature starts its turn within 30 feet of the basilisk and the two of them can see each other, the basilisk can force the creature to make a DC 12 Constitution saving throw if the basilisk isn't incapacitated. On a failed save, the creature magically begins to turn to stone and is restrained. It must repeat the saving throw at the end of its next turn. On a success, the effect ends. On a failure, the creature is petrified until freed by thegreater restorationspell or other magic. A creature that isn't surprised can avert its eyes to avoid the saving throw at the start of its turn. If it does so, it can't see the basilisk until the start of its next turn, when it can avert its eyes again. If it looks at the basilisk in the meantime, it must immediately make the save. If the basilisk sees its reflection within 30 feet of it in bright light, it mistakes itself for a rival and targets itself with its gaze."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) piercing damage plus 7 (2d6) poison damage."
        ]
    },
    "bat": {
        "name": "Bat",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "1 (1d4 - 1)",
        "Speed": "5 ft., fly 30 ft.",
        "Senses": "blindsight 60 ft., passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "2 (-4)",
        "DEX": "15 (+2)",
        "CON": "8 (-1)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "4 (-3)",
        "features": [
            "Echolocation. The bat can't use its blindsight while deafened.",
            "Keen Hearing. The bat has advantage on Wisdom (Perception) checks that rely on hearing."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +0 to hit, reach 5 ft., one creature.Hit: 1 piercing damage."
        ]
    },
    "bearded-devil": {
        "name": "Bearded Devil",
        "type": "Medium fiend (Devil)",
        "alignment": "lawful evil",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "52 (8d8 + 16)",
        "Speed": "30 ft.",
        "Saving Throws": "Str +5, Con +4, Wis +2",
        "Damage Resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered",
        "Damage Immunities": "fire, poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 120 ft., passive Perception 10",
        "Languages": "Infernal, telepathy 120 ft.",
        "Challenge": "3 (700 XP)",
        "STR": "16 (+3)",
        "DEX": "15 (+2)",
        "CON": "15 (+2)",
        "INT": "9 (-1)",
        "WIS": "11 (+0)",
        "CHA": "11 (+0)",
        "features": [
            "Devil's Sight. Magical darkness doesn't impede the devil's darkvision.",
            "Magic Resistance. The devil has advantage on saving throws against spells and other magical effects.",
            "Steadfast. The devil can't be frightened while it can see an allied creature within 30 feet of it."
        ],
        "Actions": [
            "Multiattack. The devil makes two attacks: one with its beard and one with its glaive.",
            "Beard.Melee Weapon Attack: +5 to hit, reach 5 ft., one creature.Hit: 6 (1d8 + 2) piercing damage, and the target must succeed on a DC 12 Constitution saving throw or be poisoned for 1 minute. While poisoned in this way, the target can't regain hit points. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
            "Glaive.Melee Weapon Attack: +5 to hit, reach 10 ft., one target.Hit: 8 (1d10 + 3) slashing damage. If the target is a creature other than an undead or a construct, it must succeed on a DC 12 Constitution saving throw or lose 5 (1d10) hit points at the start of each of its turns due to an infernal wound. Each time the devil hits the wounded target with this attack, the damage dealt by the wound increases by 5 (1d10). Any creature can take an action to stanch the wound with a successful DC 12 Wisdom (Medicine) check. The wound also closes if the target receives magical healing."
        ]
    },
    "behir": {
        "name": "Behir",
        "type": "Huge monstrosity",
        "alignment": "neutral evil",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "168 (16d12 + 64)",
        "Speed": "50 ft., climb 40 ft.",
        "Skills": "Perception +6, Stealth +7",
        "Damage Immunities": "lightning",
        "Senses": "darkvision 90 ft., passive Perception 16",
        "Languages": "Draconic",
        "Challenge": "11 (7200 XP)",
        "STR": "23 (+6)",
        "DEX": "16 (+3)",
        "CON": "18 (+4)",
        "INT": "7 (-2)",
        "WIS": "14 (+2)",
        "CHA": "12 (+1)",
        "features": [],
        "Actions": [
            "Multiattack. The behir makes two attacks: one with its bite and one to constrict.",
            "Bite.Melee Weapon Attack: +10 to hit, reach 10 ft., one target.Hit: 22 (3d10 + 6) piercing damage.",
            "Constrict.Melee Weapon Attack: +10 to hit, reach 5 ft., one Large or smaller creature.Hit: 17 (2d10 + 6) bludgeoning damage plus 17 (2d10 + 6) slashing damage. The target is grappled (escape DC 16) if the behir isn't already constricting a creature, and the target is restrained until this grapple ends.",
            "Lightning Breath (Recharge 5-6). The behir exhales a line of lightning that is 20 feet long and 5 feet wide. Each creature in that line must make a DC 16 Dexterity saving throw, taking 66 (12d10) lightning damage on a failed save, or half as much damage on a successful one.",
            "Swallow. The behir makes one bite attack against a Medium or smaller target it is grappling. If the attack hits, the target is also swallowed, and the grapple ends. While swallowed, the target is blinded and restrained, it has total cover against attacks and other effects outside the behir, and it takes 21 (6d6) acid damage at the start of each of the behir's turns. A behir can have only one creature swallowed at a time. If the behir takes 30 damage or more on a single turn from the swallowed creature, the behir must succeed on a DC 14 Constitution saving throw at the end of that turn or regurgitate the creature, which falls prone in a space within 10 feet of the behir. If the behir dies, a swallowed creature is no longer restrained by it and can escape from the corpse by using 15 feet of movement, exiting prone."
        ]
    },
    "beholder": {
        "name": "Beholder",
        "type": "Large aberration",
        "alignment": "lawful evil",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "180 (19d10 + 76)",
        "Speed": "0 ft., fly 20 ft. (hover)",
        "Saving Throws": "Int +8, Wis +7, Cha +8",
        "Skills": "Perception +12",
        "Condition Immunities": "prone",
        "Senses": "darkvision 120 ft., passive Perception 22",
        "Languages": "Deep Speech, Undercommon",
        "Challenge": "13 (10000 XP)",
        "STR": "10 (+0)",
        "DEX": "14 (+2)",
        "CON": "18 (+4)",
        "INT": "17 (+3)",
        "WIS": "15 (+2)",
        "CHA": "17 (+3)",
        "Legendary actions": [
            "This full creature's stat block is not available (not OGL)."
        ],
        "features": [],
        "Actions": []
    },
    "beholder-zombie": {
        "name": "Beholder Zombie",
        "type": "Large undead",
        "alignment": "neutral evil",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "93 (11d10 + 33)",
        "Speed": "0 ft., fly 20 ft. (hover)",
        "Saving Throws": "Wis +2",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 60 ft., passive Perception 9",
        "Languages": "understands Deep Speech and Undercommon but can't speak",
        "Challenge": "5 (1800 XP)",
        "STR": "10 (+0)",
        "DEX": "8 (-1)",
        "CON": "16 (+3)",
        "INT": "3 (-4)",
        "WIS": "8 (-1)",
        "CHA": "5 (-3)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "berserker": {
        "name": "Berserker",
        "type": "Medium humanoid (any race)",
        "alignment": "any chaotic alignment",
        "Armor Class": "13 (hide armor)",
        "Hit Points": "67 (9d8 + 27)",
        "Speed": "30 ft.",
        "Senses": "passive Perception 10",
        "Languages": "any one language (usually Common)",
        "Challenge": "2 (450 XP)",
        "STR": "16 (+3)",
        "DEX": "12 (+1)",
        "CON": "17 (+3)",
        "INT": "9 (-1)",
        "WIS": "11 (+0)",
        "CHA": "9 (-1)",
        "features": [
            "Reckless. At the start of its turn, the berserker can gain advantage on all melee weapon attack rolls during that turn, but attack rolls against it have advantage until the start of its next turn."
        ],
        "Actions": [
            "Greataxe.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 9 (1d12 + 3) slashing damage."
        ]
    },
    "black-bear": {
        "name": "Black Bear",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "11 (natural armor)",
        "Hit Points": "19 (3d8 + 6)",
        "Speed": "40 ft., climb 30 ft.",
        "Skills": "Perception +3",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "15 (+2)",
        "DEX": "10 (+0)",
        "CON": "14 (+2)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Keen Smell. The bear has advantage on Wisdom (Perception) checks that rely on smell."
        ],
        "Actions": [
            "Multiattack. The bear makes two attacks: one with its bite and one with its claws.",
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) piercing damage.",
            "Claws.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 7 (2d4 + 2) slashing damage."
        ]
    },
    "black-dragon-wyrmling": {
        "name": "Black Dragon Wyrmling",
        "type": "Medium dragon (Chromatic)",
        "alignment": "chaotic evil",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "33 (6d8 + 6)",
        "Speed": "30 ft., fly 60 ft., swim 30 ft.",
        "Saving Throws": "Dex +4, Con +3, Wis +2, Cha +3",
        "Skills": "Perception +4, Stealth +4",
        "Damage Immunities": "acid",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 14",
        "Languages": "Draconic",
        "Challenge": "2 (450 XP)",
        "STR": "15 (+2)",
        "DEX": "14 (+2)",
        "CON": "13 (+1)",
        "INT": "10 (+0)",
        "WIS": "11 (+0)",
        "CHA": "13 (+1)",
        "features": [
            "Amphibious. The dragon can breathe air and water."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 7 (1d10 + 2) piercing damage plus 2 (1d4) acid damage.",
            "Acid Breath (Recharge 5\u20136). The dragon exhales acid in a 15-foot line that is 5 feet wide. Each creature in that line must make a DC 11 Dexterity saving throw, taking 22 (5d8) acid damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "black-pudding": {
        "name": "Black Pudding",
        "type": "Large ooze",
        "alignment": "unaligned",
        "Armor Class": "7",
        "Hit Points": "85 (10d10 + 30)",
        "Speed": "20 ft., climb 20 ft.",
        "Damage Immunities": "acid, cold, lightning, slashing",
        "Condition Immunities": "blinded, charmed, deafened, exhaustion, frightened, prone",
        "Senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 8",
        "Languages": "\u2014",
        "Challenge": "4 (1100 XP)",
        "STR": "16 (+3)",
        "DEX": "5 (-3)",
        "CON": "16 (+3)",
        "INT": "1 (-5)",
        "WIS": "6 (-2)",
        "CHA": "1 (-5)",
        "Reactions": [
            "Split. When a pudding that is Medium or larger is subjected to lightning or slashing damage, it splits into two new puddings if it has at least 10 hit points. Each new pudding has hit points equal to half the original pudding's, rounded down. New puddings are one size smaller than the original pudding."
        ],
        "features": [
            "Amorphous. The pudding can move through a space as narrow as 1 inch wide without squeezing.",
            "Corrosive Form. A creature that touches the pudding or hits it with a melee attack while within 5 feet of it takes 4 (1d8) acid damage. Any nonmagical weapon made of metal or wood that hits the pudding corrodes. After dealing damage, the weapon takes a permanent and cumulative -1 penalty to damage rolls. If its penalty drops to -5, the weapon is destroyed. Nonmagical ammunition made of metal or wood that hits the pudding is destroyed after dealing damage. The pudding can eat through 2-inch-thick, nonmagical wood or metal in 1 round.",
            "Spider Climb. The pudding can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
        ],
        "Actions": [
            "Pseudopod.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 6 (1d6 + 3) bludgeoning damage plus 18 (4d8) acid damage. In addition, nonmagical armor worn by the target is partly dissolved and takes a permanent and cumulative -1 penalty to the AC it offers. The armor is destroyed if the penalty reduces its AC to 10."
        ]
    },
    "blink-dog": {
        "name": "Blink Dog",
        "type": "Medium fey",
        "alignment": "lawful good",
        "Armor Class": "13",
        "Hit Points": "22 (4d8 + 4)",
        "Speed": "40 ft.",
        "Skills": "Perception +3, Stealth +5",
        "Senses": "passive Perception 13",
        "Languages": "Blink Dog, understands Sylvan but can't speak it",
        "Challenge": "1/4 (50 XP)",
        "STR": "12 (+1)",
        "DEX": "17 (+3)",
        "CON": "12 (+1)",
        "INT": "10 (+0)",
        "WIS": "13 (+1)",
        "CHA": "11 (+0)",
        "features": [
            "Keen Hearing and Smell. The dog has advantage on Wisdom (Perception) checks that rely on hearing or smell."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 4 (1d6 + 1) piercing damage.",
            "Teleport (Recharge 4-6). The dog magically teleports, along with any equipment it is wearing or carrying, up to 40 feet to an unoccupied space it can see. Before or after teleporting, the dog can make one bite attack."
        ]
    },
    "blood-hawk": {
        "name": "Blood Hawk",
        "type": "Small beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "7 (2d6)",
        "Speed": "10 ft., fly 60 ft.",
        "Skills": "Perception +4",
        "Senses": "passive Perception 14",
        "Languages": "\u2014",
        "Challenge": "1/8 (25 XP)",
        "STR": "6 (-2)",
        "DEX": "14 (+2)",
        "CON": "10 (+0)",
        "INT": "3 (-4)",
        "WIS": "14 (+2)",
        "CHA": "5 (-3)",
        "features": [
            "Keen Sight. The hawk has advantage on Wisdom (Perception) checks that rely on sight.",
            "Pack Tactics. The hawk has advantage on an attack roll against a creature if at least one of the hawk's allies is within 5 feet of the creature and the ally isn't incapacitated."
        ],
        "Actions": [
            "Beak.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 4 (1d4 + 2) piercing damage."
        ]
    },
    "blue-dragon-wyrmling": {
        "name": "Blue Dragon Wyrmling",
        "type": "Medium dragon (Chromatic)",
        "alignment": "lawful evil",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "52 (8d8 + 16)",
        "Speed": "30 ft., burrow 15 ft., fly 60 ft.",
        "Saving Throws": "Dex +2, Con +4, Wis +2, Cha +4",
        "Skills": "Perception +4, Stealth +2",
        "Damage Immunities": "lightning",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 14",
        "Languages": "Draconic",
        "Challenge": "3 (700 XP)",
        "STR": "17 (+3)",
        "DEX": "10 (+0)",
        "CON": "15 (+2)",
        "INT": "12 (+1)",
        "WIS": "11 (+0)",
        "CHA": "15 (+2)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 8 (1d10 + 3) piercing damage plus 3 (1d6) lightning damage.",
            "Lightning Breath (Recharge 5-6). The dragon exhales lightning in a 30-foot line that is 5 feet wide. Each creature in that line must make a DC 12 Dexterity saving throw, taking 22 (4d10) lightning damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "blue-slaad": {
        "name": "Blue Slaad",
        "type": "Large aberration",
        "alignment": "chaotic neutral",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "123 (13d10 + 52)",
        "Speed": "30 ft.",
        "Skills": "Perception + 1",
        "Damage Resistances": "acid, cold, fire, lightning, thunder",
        "Senses": "darkvision 60 ft., passive Perception 11",
        "Languages": "Slaad, telepathy 60 ft.",
        "Challenge": "7 (2900 XP)",
        "STR": "20 (+5)",
        "DEX": "15 (+2)",
        "CON": "18 (+4)",
        "INT": "7 (-2)",
        "WIS": "7 (-2)",
        "CHA": "9 (-1)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "boar": {
        "name": "Boar",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "11 (natural armor)",
        "Hit Points": "11 (2d8 + 2)",
        "Speed": "40 ft.",
        "Senses": "passive Perception 9",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "13 (+1)",
        "DEX": "11 (+0)",
        "CON": "12 (+1)",
        "INT": "2 (-4)",
        "WIS": "9 (-1)",
        "CHA": "5 (-3)",
        "features": [
            "Charge. If the boar moves at least 20 feet straight toward a target and then hits it with a tusk attack on the same turn, the target takes an extra 3 (1d6) slashing damage. If the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone.",
            "Relentless (Recharges after a Short or Long Rest). If the boar takes 7 damage or less that would reduce it to 0 hit points, it is reduced to 1 hit point instead."
        ],
        "Actions": [
            "Tusk.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 4 (1d6 + 1) slashing damage."
        ]
    },
    "bone-devil": {
        "name": "Bone Devil",
        "type": "Large fiend (Devil)",
        "alignment": "lawful evil",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "142 (15d10 + 60)",
        "Speed": "40 ft., fly 40 ft.",
        "Saving Throws": "Int +5, Wis +6, Cha +7",
        "Skills": "Deception +7, Insight +6",
        "Damage Resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered",
        "Damage Immunities": "fire, poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 120 ft., passive Perception 12",
        "Languages": "Infernal, telepathy 120 ft.",
        "Challenge": "9 (5000 XP)",
        "STR": "18 (+4)",
        "DEX": "16 (+3)",
        "CON": "18 (+4)",
        "INT": "13 (+1)",
        "WIS": "14 (+2)",
        "CHA": "16 (+3)",
        "features": [
            "Devil's Sight. Magical darkness doesn't impede the devil's darkvision.",
            "Magic Resistance. The devil has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack. The devil makes three attacks: two with its claws and one with its sting.",
            "Claw.Melee Weapon Attack: +8 to hit, reach 10 ft., one target.Hit: 8 (1d8 + 4) slashing damage.",
            "Sting.Melee Weapon Attack: +8 to hit, reach 10 ft., one target.Hit: 13 (2d8 + 4) piercing damage plus 17 (5d6) poison damage, and the target must succeed on a DC 14 Constitution saving throw or become poisoned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        ]
    },
    "bone-naga": {
        "name": "Bone Naga",
        "type": "Large undead",
        "alignment": "lawful evil",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "58 (9d10 + 9)",
        "Speed": "30 ft.",
        "Damage Immunities": "poison",
        "Condition Immunities": "charmed, exhaustion, paralyzed, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 12",
        "Languages": "Common plus one other language",
        "Challenge": "4 (1100 XP)",
        "STR": "15 (+2)",
        "DEX": "16 (+3)",
        "CON": "12 (+1)",
        "INT": "15 (+2)",
        "WIS": "15 (+2)",
        "CHA": "16 (+3)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "brass-dragon-wyrmling": {
        "name": "Brass Dragon Wyrmling",
        "type": "Medium dragon (Metallic)",
        "alignment": "chaotic good",
        "Armor Class": "16 (natural armor)",
        "Hit Points": "16 (3d8 + 3)",
        "Speed": "30 ft., burrow 15 ft., fly 60 ft.",
        "Saving Throws": "Dex +2, Con +3, Wis +2, Cha +3",
        "Skills": "Perception +4, Stealth +2",
        "Damage Immunities": "fire",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 14",
        "Languages": "Draconic",
        "Challenge": "1 (200 XP)",
        "STR": "15 (+2)",
        "DEX": "10 (+0)",
        "CON": "13 (+1)",
        "INT": "10 (+0)",
        "WIS": "11 (+0)",
        "CHA": "13 (+1)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 7 (1d10 + 2) piercing damage.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.",
            "Fire Breath. The dragon exhales fire in an 20-foot line that is 5 feet wide. Each creature in that line must make a DC 11 Dexterity saving throw, taking 14 (4d6) fire damage on a failed save, or half as much damage on a successful one.",
            "Sleep Breath. The dragon exhales sleep gas in a 15-foot cone. Each creature in that area must succeed on a DC 11 Constitution saving throw or fall unconscious for 1 minute. This effect ends for a creature if the creature takes damage or someone uses an action to wake it."
        ]
    },
    "bronze-dragon-wyrmling": {
        "name": "Bronze Dragon Wyrmling",
        "type": "Medium dragon (Metallic)",
        "alignment": "lawful good",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "32 (5d8 + 10)",
        "Speed": "30 ft., fly 60 ft., swim 30 ft.",
        "Saving Throws": "Dex +2, Con +4, Wis +2, Cha +4",
        "Skills": "Perception +4, Stealth +2",
        "Damage Immunities": "lightning",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 14",
        "Languages": "Draconic",
        "Challenge": "2 (450 XP)",
        "STR": "17 (+3)",
        "DEX": "10 (+0)",
        "CON": "15 (+2)",
        "INT": "12 (+1)",
        "WIS": "11 (+0)",
        "CHA": "15 (+2)",
        "features": [
            "Amphibious. The dragon can breathe air and water."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 8 (1d10 + 3) piercing damage.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.",
            "Lightning Breath. The dragon exhales lightning in a 40-foot line that is 5 feet wide. Each creature in that line must make a DC 12 Dexterity saving throw, taking 16 (3d10) lightning damage on a failed save, or half as much damage on a successful one.",
            "Repulsion Breath. The dragon exhales repulsion energy in a 30-foot cone. Each creature in that area must succeed on a DC 12 Strength saving throw. On a failed save, the creature is pushed 30 feet away from the dragon."
        ]
    },
    "brown-bear": {
        "name": "Brown Bear",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "11 (natural armor)",
        "Hit Points": "34 (4d10 + 12)",
        "Speed": "40 ft., climb 30 ft.",
        "Skills": "Perception +3",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "1 (200 XP)",
        "STR": "19 (+4)",
        "DEX": "10 (+0)",
        "CON": "16 (+3)",
        "INT": "2 (-4)",
        "WIS": "13 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Keen Smell. The bear has advantage on Wisdom (Perception) checks that rely on smell."
        ],
        "Actions": [
            "Multiattack. The bear makes two attacks: one with its bite and one with its claws.",
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 8 (1d8 + 4) piercing damage.",
            "Claws.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) slashing damage."
        ]
    },
    "bugbear": {
        "name": "Bugbear",
        "type": "Medium humanoid (Goblinoid)",
        "alignment": "chaotic evil",
        "Armor Class": "16 (hide armor, shield)",
        "Hit Points": "27 (5d8 + 5)",
        "Speed": "30 ft.",
        "Skills": "Stealth +6, Survival +2",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Common, Goblin",
        "Challenge": "1 (200 XP)",
        "STR": "15 (+2)",
        "DEX": "14 (+2)",
        "CON": "13 (+1)",
        "INT": "8 (-1)",
        "WIS": "11 (+0)",
        "CHA": "9 (-1)",
        "features": [
            "Brute. A melee weapon deals one extra die of its damage when the bugbear hits with it (included in the attack).",
            "Surprise Attack. If the bugbear surprises a creature and hits it with an attack during the first round of combat, the target takes an extra 7 (2d6) damage from the attack."
        ],
        "Actions": [
            "Morningstar.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 11 (2d8 + 2) piercing damage.",
            "Javelin.Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target.Hit: 9 (2d6 + 2) piercing damage in melee or 5 (1d6 + 2) piercing damage at range."
        ]
    },
    "bugbear-chief": {
        "name": "Bugbear Chief",
        "type": "Medium humanoid (Goblinoid)",
        "alignment": "chaotic evil",
        "Armor Class": "17 (chain shirt, shield)",
        "Hit Points": "65 (10d8 + 20)",
        "Speed": "30 ft.",
        "Skills": "Intimidation +2, Stealth +6, Survival +3",
        "Senses": "darkvision 60 ft., passive Perception 11",
        "Languages": "Common, Goblin",
        "Challenge": "3 (700 XP)",
        "STR": "17 (+3)",
        "DEX": "14 (+2)",
        "CON": "14 (+2)",
        "INT": "11 (+0)",
        "WIS": "12 (+1)",
        "CHA": "11 (+0)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "bulette": {
        "name": "Bulette",
        "type": "Large monstrosity",
        "alignment": "unaligned",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "94 (9d10 + 45)",
        "Speed": "40 ft., burrow 40 ft.",
        "Skills": "Perception +6",
        "Senses": "darkvision 60 ft., tremorsense 60 ft., passive Perception 16",
        "Languages": "\u2014",
        "Challenge": "5 (1800 XP)",
        "STR": "19 (+4)",
        "DEX": "11 (+0)",
        "CON": "21 (+5)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "5 (-3)",
        "features": [
            "Standing Leap. The bulette's long jump is up to 30 feet and its high jump is up to 15 feet, with or without a running start."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 30 (4d12 + 4) piercing damage.",
            "Deadly Leap. If the bulette jumps at least 15 feet as part of its movement, it can then use this action to land on its feet in a space that contains one or more other creatures. Each of those creatures must succeed on a DC 16 Strength or Dexterity saving throw (target's choice) or be knocked prone and take 14 (3d6 + 4) bludgeoning damage plus 14 (3d6 + 4) slashing damage. On a successful save, the creature takes only half the damage, isn't knocked prone, and is pushed 5 feet out of the bulette's space into an unoccupied space of the creature's choice. If no unoccupied space is within range, the creature instead falls prone in the bulette's space."
        ]
    },
    "bullywug": {
        "name": "Bullywug",
        "type": "Medium humanoid (Bullywug)",
        "alignment": "neutral evil",
        "Armor Class": "15 (hide armor, shield)",
        "Hit Points": "11 (2d8 + 2)",
        "Speed": "20 ft., swim 40 ft.",
        "Skills": "Stealth +3",
        "Senses": "passive Perception 10",
        "Languages": "Bullywug",
        "Challenge": "1/4 (50 XP)",
        "STR": "12 (+1)",
        "DEX": "12 (+1)",
        "CON": "13 (+1)",
        "INT": "7 (-2)",
        "WIS": "10 (+0)",
        "CHA": "7 (-2)",
        "features": [
            "Amphibious. The bullywug can breathe air and water.",
            "Speak with Frogs and Toads. The bullywug can communicate simple concepts to frogs and toads when it speaks in Bullywug.",
            "Swamp Camouflage. The bullywug has advantage on Dexterity (Stealth) checks made to hide in swampy terrain.",
            "Standing Leap. The bullywug's long jump is up to 20 feet and its high jump is up to 10 feet, with or without a running start."
        ],
        "Actions": [
            "Multiattack. The bullywug makes two melee attacks: one with its bite and one with its spear.",
            "Bite.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 3 (1d4 + 1) bludgeoning damage.",
            "Spear.Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target.Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack."
        ]
    },
    "cambion": {
        "name": "Cambion",
        "type": "Medium fiend",
        "alignment": "any evil alignment",
        "Armor Class": "19 (scale mail)",
        "Hit Points": "82 (11d8 + 33)",
        "Speed": "30 ft., fly 60 ft.",
        "Saving Throws": "Str +7, Con +6, Int +5, Cha +6",
        "Skills": "Deception +6, Intimidation +6, Perception +4, Stealth +7",
        "Damage Resistances": "cold, fire, lightning, poison; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Senses": "darkvision 60 ft., passive Perception 14",
        "Languages": "Abyssal, Common, Infernal",
        "Challenge": "5 (1800 XP)",
        "STR": "18 (+4)",
        "DEX": "18 (+4)",
        "CON": "16 (+3)",
        "INT": "14 (+2)",
        "WIS": "12 (+1)",
        "CHA": "16 (+3)",
        "features": [
            "Fiendish Blessing. The AC of the cambion includes its Charisma bonus.",
            "Innate Spellcasting. The cambion's spellcasting ability is Charisma (spell save DC 14). The cambion can innately cast the following spells, requiring no material components:"
        ],
        "Actions": [
            "Multiattack. The cambion makes two melee attacks or uses its Fire Ray twice.",
            "Spear.Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 20/60 ft., one target.Hit: 7 (1d6 + 4) piercing damage, or 8 (1d8 + 4) piercing damage if used with two hands to make a melee attack, plus 3 (1d6) fire damage.",
            "Fire Ray.Ranged Spell Attack: +7 to hit, range 120 ft., one target.Hit: 10 (3d6) fire damage.",
            "Fiendish Charm. One humanoid the cambion can see within 30 feet of it must succeed on a DC 14 Wisdom saving throw or be magically charmed for 1 day. The charmed target obeys the cambion's spoken commands. If the target suffers any harm from the cambion or another creature or receives a suicidal command from the cambion, the target can repeat the saving throw, ending the effect on itself on a success. If a target's saving throw is successful, or if the effect ends for it, the creature is immune to the cambion's Fiendish Charm for the next 24 hours."
        ]
    },
    "camel": {
        "name": "Camel",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "9",
        "Hit Points": "15 (2d10 + 4)",
        "Speed": "50 ft.",
        "Senses": "passive Perception 9",
        "Languages": "\u2014",
        "Challenge": "1/8 (25 XP)",
        "STR": "16 (+3)",
        "DEX": "8 (-1)",
        "CON": "14 (+2)",
        "INT": "2 (-4)",
        "WIS": "8 (-1)",
        "CHA": "5 (-3)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 2 (1d4) bludgeoning damage."
        ]
    },
    "carrion-crawler": {
        "name": "Carrion Crawler",
        "type": "Large monstrosity",
        "alignment": "unaligned",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "51 (6d10 + 18)",
        "Speed": "30 ft., climb 30 ft.",
        "Skills": "Perception +3",
        "Senses": "darkvision 60 ft., passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "14 (+2)",
        "DEX": "13 (+1)",
        "CON": "16 (+3)",
        "INT": "1 (-5)",
        "WIS": "12 (+1)",
        "CHA": "5 (-3)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "cat": {
        "name": "Cat",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "2 (1d4)",
        "Speed": "40 ft., climb 30 ft.",
        "Skills": "Perception +3, Stealth +4",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "3 (-4)",
        "DEX": "15 (+2)",
        "CON": "10 (+0)",
        "INT": "3 (-4)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Keen Smell. The cat has advantage on Wisdom (Perception) checks that rely on smell."
        ],
        "Actions": [
            "Claws.Melee Weapon Attack: +0 to hit, reach 5 ft., one target.Hit: 1 slashing damage."
        ]
    },
    "centaur": {
        "name": "Centaur",
        "type": "Large monstrosity",
        "alignment": "neutral good",
        "Armor Class": "12",
        "Hit Points": "45 (6d10 + 12)",
        "Speed": "50 ft.",
        "Skills": "Athletics +6, Perception +3, Survival +3",
        "Senses": "passive Perception 13",
        "Languages": "Elvish, Sylvan",
        "Challenge": "2 (450 XP)",
        "STR": "18 (+4)",
        "DEX": "14 (+2)",
        "CON": "14 (+2)",
        "INT": "9 (-1)",
        "WIS": "13 (+1)",
        "CHA": "11 (+0)",
        "features": [
            "Charge. If the centaur moves at least 30 feet straight toward a target and then hits it with a pike attack on the same turn, the target takes an extra 10 (3d6) piercing damage."
        ],
        "Actions": [
            "Multiattack. The centaur makes two attacks: one with its pike and one with its hooves or two with its longbow.",
            "Pike.Melee Weapon Attack: +6 to hit, reach 10 ft., one target.Hit: 9 (1d10 + 4) piercing damage.",
            "Hooves.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) bludgeoning damage.",
            "Longbow.Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target.Hit: 6 (1d8 + 2) piercing damage."
        ]
    },
    "chain-devil": {
        "name": "Chain Devil",
        "type": "Medium fiend (Devil)",
        "alignment": "lawful evil",
        "Armor Class": "16 (natural armor)",
        "Hit Points": "85 (10d8 + 40)",
        "Speed": "30 ft.",
        "Saving Throws": "Con +7, Wis +4, Cha +5",
        "Damage Resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered",
        "Damage Immunities": "fire, poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 120 ft., passive Perception 11",
        "Languages": "Infernal, telepathy 120 ft.",
        "Challenge": "8 (3900 XP)",
        "STR": "18 (+4)",
        "DEX": "15 (+2)",
        "CON": "18 (+4)",
        "INT": "11 (+0)",
        "WIS": "12 (+1)",
        "CHA": "14 (+2)",
        "Reactions": [
            "Unnerving Mask. When a creature the devil can see starts its turn within 30 feet of the devil, the devil can create the illusion that it looks like one of the creature's departed loved ones or bitter enemies. If the creature can see the devil, it must succeed on a DC 14 Wisdom saving throw or be frightened until the end of its turn."
        ],
        "features": [
            "Devil's Sight. Magical darkness doesn't impede the devil's darkvision.",
            "Magic Resistance. The devil has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack. The devil makes two attacks with its chains.",
            "Chain.Melee Weapon Attack: +8 to hit, reach 10 ft., one target.Hit: 11 (2d6 + 4) slashing damage. The target is grappled (escape DC 14) if the devil isn't already grappling a creature. Until this grapple ends, the target is restrained and takes 7 (2d6) piercing damage at the start of each of its turns.",
            "Animate Chains (Recharges after a Short or Long Rest). Up to four chains the devil can see within 60 feet of it magically sprout razor-edged barbs and animate under the devil's control, provided that the chains aren't being worn or carried. Each animated chain is an object with AC 20, 20 hit points, resistance to piercing damage, and immunity to psychic and thunder damage. When the devil uses Multiattack on its turn, it can use each animated chain to make one additional chain attack. An animated chain can grapple one creature of its own but can't make attacks while grappling. An animated chain reverts to its inanimate state if reduced to 0 hit points or if the devil is incapacitated or dies."
        ]
    },
    "chasme": {
        "name": "Chasme",
        "type": "Large fiend (Demon)",
        "alignment": "chaotic evil",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "84 (13d10 + 13)",
        "Speed": "20 ft., fly 60 ft.",
        "Saving Throws": "Dex +5, Wis +5",
        "Skills": "Perception +5",
        "Damage Resistances": "cold, fire, lightning",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "blindsight 10 ft., darkvision 120 ft., passive Perception 15",
        "Languages": "Abyssal, telepathy 120 ft.",
        "Challenge": "6 (2300 XP)",
        "STR": "15 (+2)",
        "DEX": "15 (+2)",
        "CON": "12 (+1)",
        "INT": "11 (+0)",
        "WIS": "14 (+2)",
        "CHA": "10 (+0)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "chimera": {
        "name": "Chimera",
        "type": "Large monstrosity",
        "alignment": "chaotic evil",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "114 (12d10 + 48)",
        "Speed": "30 ft., fly 60 ft.",
        "Skills": "Perception +8",
        "Senses": "darkvision 60 ft., passive Perception 18",
        "Languages": "understands Draconic but can't speak",
        "Challenge": "6 (2300 XP)",
        "STR": "19 (+4)",
        "DEX": "11 (+0)",
        "CON": "19 (+4)",
        "INT": "3 (-4)",
        "WIS": "14 (+2)",
        "CHA": "10 (+0)",
        "features": [],
        "Actions": [
            "Multiattack. The chimera makes three attacks: one with its bite, one with its horns, and one with its claws. When its fire breath is available, it can use the breath in place of its bite or horns.",
            "Bite.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) piercing damage.",
            "Horns.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 10 (1d12 + 4) bludgeoning damage.",
            "Claws.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) slashing damage.",
            "Fire Breath (Recharge 5-6). The dragon head exhales fire in a 15-foot cone. Each creature in that area must make a DC 15 Dexterity saving throw, taking 31 (7d8) fire damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "chuul": {
        "name": "Chuul",
        "type": "Large aberration",
        "alignment": "chaotic evil",
        "Armor Class": "16 (natural armor)",
        "Hit Points": "93 (11d10 + 33)",
        "Speed": "30 ft., swim 30 ft.",
        "Skills": "Perception +4",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 60 ft., passive Perception 14",
        "Languages": "understands Deep Speech but can't speak",
        "Challenge": "4 (1100 XP)",
        "STR": "19 (+4)",
        "DEX": "10 (+0)",
        "CON": "16 (+3)",
        "INT": "5 (-3)",
        "WIS": "11 (+0)",
        "CHA": "5 (-3)",
        "features": [
            "Amphibious. The chuul can breathe air and water.",
            "Sense Magic. The chuul senses magic within 120 feet of it at will. This trait otherwise works like thedetect magicspell but isn't itself magical."
        ],
        "Actions": [
            "Multiattack. The chuul makes two pincer attacks. If the chuul is grappling a creature, the chuul can also use its tentacles once.",
            "Pincer.Melee Weapon Attack: +6 to hit, reach 10 ft., one target.Hit: 11 (2d6 + 4) bludgeoning damage. The target is grappled (escape DC 14) if it is a Large or smaller creature and the chuul doesn't have two other creatures grappled.",
            "Tentacles. One creature grappled by the chuul must succeed on a DC 13 Constitution saving throw or be poisoned for 1 minute. Until this poison ends, the target is paralyzed. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        ]
    },
    "clay-golem": {
        "name": "Clay Golem",
        "type": "Large construct",
        "alignment": "unaligned",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "133 (14d10 + 56)",
        "Speed": "20 ft.",
        "Damage Immunities": "acid, poison, psychic; bludgeoning, piercing and slashing from nonmagical attacks that aren't adamantine",
        "Condition Immunities": "charmed, exhaustion, frightened, paralyzed, petrified, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 9",
        "Languages": "understands the languages of its creator but can't speak",
        "Challenge": "9 (5000 XP)",
        "STR": "20 (+5)",
        "DEX": "9 (-1)",
        "CON": "18 (+4)",
        "INT": "3 (-4)",
        "WIS": "8 (-1)",
        "CHA": "1 (-5)",
        "features": [
            "Acid Absorption. Whenever the golem is subjected to acid damage, it takes no damage and instead regains a number of hit points equal to the acid damage dealt.",
            "Berserk. Whenever the golem starts its turn with 60 hit points or fewer, roll a d6. On a 6, the golem goes berserk. On each of its turns while berserk, the golem attacks the nearest creature it can see. If no creature is near enough to move to and attack, the golem attacks an object, with preference for an object smaller than itself. Once the golem goes berserk, it continues to do so until it is destroyed or regains all its hit points.",
            "Immutable Form. The golem is immune to any spell or effect that would alter its form.",
            "Magic Resistance. The golem has advantage on saving throws against spells and other magical effects.",
            "Magic Weapons. The golem's weapon attacks are magical."
        ],
        "Actions": [
            "Multiattack. The golem makes two slam attacks.",
            "Slam.Melee Weapon Attack: +8 to hit, reach 5 ft., one target.Hit: 16 (2d10 + 5) bludgeoning damage. If the target is a creature, it must succeed on a DC 15 Constitution saving throw or have its hit point maximum reduced by an amount equal to the damage taken. The target dies if this attack reduces its hit point maximum to 0. The reduction lasts until removed by thegreater restorationspell or other magic.",
            "Haste (Recharge 5-6). Until the end of its next turn, the golem magically gains a +2 bonus to its AC, has advantage on Dexterity saving throws, and can use its slam attack as a bonus action."
        ]
    },
    "cloaker": {
        "name": "Cloaker",
        "type": "Large aberration",
        "alignment": "chaotic neutral",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "78 (12d10 + 12)",
        "Speed": "10 ft., fly 40 ft.",
        "Skills": "Stealth +5",
        "Senses": "darkvision 60 ft., passive Perception 11",
        "Languages": "Deep Speech, Undercommon",
        "Challenge": "8 (3900 XP)",
        "STR": "17 (+3)",
        "DEX": "15 (+2)",
        "CON": "12 (+1)",
        "INT": "13 (+1)",
        "WIS": "12 (+1)",
        "CHA": "14 (+2)",
        "features": [
            "Damage Transfer. While attached to a creature, the cloaker takes only half the damage dealt to it (rounded down), and that creature takes the other half.",
            "False Appearance. While the cloaker remains motionless without its underside exposed, it is indistinguishable from a dark leather cloak.",
            "Light Sensitivity. While in bright light, the cloaker has disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight."
        ],
        "Actions": [
            "Multiattack. The cloaker makes two attacks: one with its bite and one with its tail.",
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one creature.Hit: 10 (2d6 + 3) piercing damage, and if the target is Large or smaller, the cloaker attaches to it. If the cloaker has advantage against the target, the cloaker attaches to the target's head, and the target is blinded and unable to breathe while the cloaker is attached. While attached, the cloaker can make this attack only against the target and has advantage on the attack roll. The cloaker can detach itself by spending 5 feet of its movement. A creature, including the target, can take its action to detach the cloaker by succeeding on a DC 16 Strength check.",
            "Tail.Melee Weapon Attack: +6 to hit, reach 10 ft., one creature.Hit: 7 (1d8 + 3) slashing damage.",
            "Moan. Each creature within 60 feet of the cloaker that can hear its moan and that isn't an aberration must succeed on a DC 13 Wisdom saving throw or become frightened until the end of the cloaker's next turn. If a creature's saving throw is successful, the creature is immune to the cloaker's moan for the next 24 hours",
            "Phantasms (Recharges after a Short or Long Rest). The cloaker magically creates three illusory duplicates of itself if it isn't in bright light. The duplicates move with it and mimic its actions, shifting position so as to make it impossible to track which cloaker is the real one. If the cloaker is ever in an area of bright light, the duplicates disappear. Whenever any creature targets the cloaker with an attack or a harmful spell while a duplicate remains, that creature rolls randomly to determine whether it targets the cloaker or one of the duplicates. A creature is unaffected by this magical effect if it can't see or if it relies on senses other than sight. A duplicate has the cloaker's AC and uses its saving throws. If an attack hits a duplicate, or if a duplicate fails a saving throw against an effect that deals damage, the duplicate disappears."
        ]
    },
    "cloud-giant": {
        "name": "Cloud Giant",
        "type": "Huge giant",
        "alignment": "neutral good (50 %) or neutral evil (50 %)",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "200 (16d12 + 96)",
        "Speed": "40 ft.",
        "Saving Throws": "Con +10, Wis +7, Cha +7",
        "Skills": "Insight +7, Perception +7",
        "Senses": "passive Perception 17",
        "Languages": "Common, Giant",
        "Challenge": "9 (5000 XP)",
        "STR": "27 (+8)",
        "DEX": "10 (+0)",
        "CON": "22 (+6)",
        "INT": "12 (+1)",
        "WIS": "16 (+3)",
        "CHA": "16 (+3)",
        "features": [
            "Keen Smell. The giant has advantage on Wisdom (Perception) checks that rely on smell.",
            "InnateSpellcasting. The giant's innate spellcasting ability is Charisma. It can innately cast the following spells, requiring no material components:"
        ],
        "Actions": [
            "Multiattack. The giant makes two morningstar attacks.",
            "Morningstar.Melee Weapon Attack: +12 to hit, reach 10 ft., one target.Hit: 21 (3d8 + 8) piercing damage.",
            "Rock.Ranged Weapon Attack: +12 to hit, range 60/240 ft., one target.Hit: 30 (4d10 + 8) bludgeoning damage."
        ]
    },
    "cockatrice": {
        "name": "Cockatrice",
        "type": "Small monstrosity",
        "alignment": "unaligned",
        "Armor Class": "11",
        "Hit Points": "27 (6d6 + 6)",
        "Speed": "20 ft., fly 40 ft.",
        "Senses": "darkvision 60 ft., passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "6 (-2)",
        "DEX": "12 (+1)",
        "CON": "12 (+1)",
        "INT": "2 (-4)",
        "WIS": "13 (+1)",
        "CHA": "5 (-3)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +3 to hit, reach 5 ft., one creature.Hit: 3 (1d4 + 1) piercing damage, and the target must succeed on a DC 11 Constitution saving throw against being magically petrified. On a failed save, the creature begins to turn to stone and is restrained. It must repeat the saving throw at the end of its next turn. On a success, the effect ends. On a failure, the creature is petrified for 24 hours."
        ]
    },
    "commoner": {
        "name": "Commoner",
        "type": "Medium humanoid (any race)",
        "alignment": "any alignment",
        "Armor Class": "10",
        "Hit Points": "4 (1d8)",
        "Speed": "30 ft.",
        "Senses": "passive Perception 10",
        "Languages": "any one language (usually Common)",
        "Challenge": "0 (10 XP)",
        "STR": "10 (+0)",
        "DEX": "10 (+0)",
        "CON": "10 (+0)",
        "INT": "10 (+0)",
        "WIS": "10 (+0)",
        "CHA": "10 (+0)",
        "features": [],
        "Actions": [
            "Club.Melee Weapon Attack: +2 to hit, reach 5 ft., one target.Hit: 2 (1d4) bludgeoning damage."
        ]
    },
    "constrictor-snake": {
        "name": "Constrictor Snake",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "13 (2d10 + 2)",
        "Speed": "30 ft., swim 30 ft.",
        "Senses": "blindsight 10 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "15 (+2)",
        "DEX": "14 (+2)",
        "CON": "12 (+1)",
        "INT": "1 (-5)",
        "WIS": "10 (+0)",
        "CHA": "3 (-4)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 5 (1d6 + 2) piercing damage.",
            "Constrict.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 6 (1d8 + 2) bludgeoning damage, and the target is grappled (escape DC 14). Until this grapple ends, the creature is restrained, and the snake can't constrict another target."
        ]
    },
    "copper-dragon-wyrmling": {
        "name": "Copper Dragon Wyrmling",
        "type": "Medium dragon (Metallic)",
        "alignment": "chaotic good",
        "Armor Class": "16 (natural armor)",
        "Hit Points": "22 (4d8 + 4)",
        "Speed": "30 ft., climb 30 ft., fly 60 ft.",
        "Saving Throws": "Dex +3, Con +3, Wis +2, Cha +3",
        "Skills": "Perception +4, Stealth +3",
        "Damage Immunities": "acid",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 14",
        "Languages": "Draconic",
        "Challenge": "1 (200 XP)",
        "STR": "15 (+2)",
        "DEX": "12 (+1)",
        "CON": "13 (+1)",
        "INT": "14 (+2)",
        "WIS": "11 (+0)",
        "CHA": "13 (+1)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 7 (1d10 + 2) piercing damage.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.",
            "Acid Breath. The dragon exhales acid in an 20-foot line that is 5 feet wide. Each creature in that line must make a DC 11 Dexterity saving throw, taking 18 (4d8) acid damage on a failed save, or half as much damage on a successful one.",
            "Slowing Breath. The dragon exhales gas in a 15-foot cone. Each creature in that area must succeed on a DC 11 Constitution saving throw. On a failed save, the creature can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the creature can use either an action or a bonus action on its turn, but not both. These effects last for 1 minute. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself with a successful save."
        ]
    },
    "couatl": {
        "name": "Couatl",
        "type": "Medium celestial",
        "alignment": "lawful good",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "97 (13d8 + 39)",
        "Speed": "30 ft., fly 90 ft.",
        "Saving Throws": "Con +5, Wis +7, Cha +6",
        "Damage Resistances": "radiant",
        "Damage Immunities": "psychic; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Senses": "truesight 120 ft., passive Perception 15",
        "Languages": "all, telepathy 120 ft.",
        "Challenge": "4 (1100 XP)",
        "STR": "16 (+3)",
        "DEX": "20 (+5)",
        "CON": "17 (+3)",
        "INT": "18 (+4)",
        "WIS": "20 (+5)",
        "CHA": "18 (+4)",
        "features": [
            "Innate Spellcasting. The couatl's spellcasting ability is Charisma (spell save DC 14). It can innately cast the following spells, requiring only verbal components:",
            "Magic Weapons. The couatl's weapon attacks are magical.",
            "Shielded Mind. The couatl is immune to scrying and to any effect that would sense its emotions, read its thoughts, or detect its location."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +8 to hit, reach 5 ft., one creature.Hit: 8 (1d6 + 5) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 24 hours. Until this poison ends, the target is unconscious. Another creature can use an action to shake the target awake.",
            "Constrict.Melee Weapon Attack: +6 to hit, reach 10 ft., one Medium or smaller creature.Hit: 10 (2d6 + 3) bludgeoning damage, and the target is grappled (escape DC 15). Until this grapple ends, the target is restrained, and the couatl can't constrict another target.",
            "Change Shape. The couatl magically polymorphs into a humanoid or beast that has a challenge rating equal to or less than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the couatl's choice). In a new form, the couatl retains its game statistics and ability to speak, but its AC, movement modes, Strength, Dexterity, and other actions are replaced by those of the new form, and it gains any statistics and capabilities (except class features, legendary actions, and lair actions) that the new form has but that it lacks. If the new form has a bite attack, the couatl can use its bite in that form."
        ]
    },
    "crab": {
        "name": "Crab",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "11 (natural armor)",
        "Hit Points": "2 (1d4)",
        "Speed": "20 ft., swim 20 ft.",
        "Skills": "Stealth +2",
        "Senses": "blindsight 30 ft., passive Perception 9",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "2 (-4)",
        "DEX": "11 (+0)",
        "CON": "10 (+0)",
        "INT": "1 (-5)",
        "WIS": "8 (-1)",
        "CHA": "2 (-4)",
        "features": [
            "Amphibious. The crab can breathe air and water."
        ],
        "Actions": [
            "Claw.Melee Weapon Attack: +0 to hit, reach 5 ft., one target.Hit: 1 bludgeoning damage."
        ]
    },
    "crawling-claw": {
        "name": "Crawling Claw",
        "type": "Tiny undead",
        "alignment": "neutral evil",
        "Armor Class": "12",
        "Hit Points": "2 (1d4)",
        "Speed": "20 ft., climb 20 ft.",
        "Damage Immunities": "poison",
        "Condition Immunities": "charmed, exhaustion, poisoned",
        "Senses": "blindsight 30 ft. (blind beyond this radius), passive Perception 10",
        "Languages": "understands Common but can't speak",
        "Challenge": "0 (10 XP)",
        "STR": "13 (+1)",
        "DEX": "14 (+2)",
        "CON": "11 (+0)",
        "INT": "5 (-3)",
        "WIS": "10 (+0)",
        "CHA": "4 (-3)",
        "features": [
            "Turn Immunity. The claw is immune to effects that turn undead."
        ],
        "Actions": [
            "Claw.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 3 (1d4 + 1) bludgeoning or slashing damage (claw's choice)."
        ]
    },
    "crocodile": {
        "name": "Crocodile",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "19 (3d10 + 3)",
        "Speed": "20 ft., swim 30 ft.",
        "Skills": "Stealth +2",
        "Senses": "passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "15 (+2)",
        "DEX": "10 (+0)",
        "CON": "13 (+1)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "5 (-3)",
        "features": [
            "Hold Breath. The crocodile can hold its breath for 15 minutes."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 7 (1d10 + 2) piercing damage, and the target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the crocodile can't bite another target."
        ]
    },
    "cult-fanatic": {
        "name": "Cult Fanatic",
        "type": "Medium humanoid (any race)",
        "alignment": "any non-good alignment",
        "Armor Class": "13 (leather armor)",
        "Hit Points": "33 (6d8 + 6)",
        "Speed": "30 ft.",
        "Skills": "Deception +4, Persuasion +4, Religion +2",
        "Senses": "passive Perception 11",
        "Languages": "any one language (usually Common)",
        "Challenge": "2 (450 XP)",
        "STR": "11 (+0)",
        "DEX": "14 (+2)",
        "CON": "12 (+1)",
        "INT": "10 (+0)",
        "WIS": "13 (+1)",
        "CHA": "14 (+2)",
        "features": [
            "Dark Devotion. The fanatic has advantage on saving throws against being charmed or frightened.",
            "Spellcasting. The fanatic is a 4th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 11, +3 to hit with spell attacks). The fanatic has the following cleric spells prepared:"
        ],
        "Actions": [
            "Multiattack. The fanatic makes two melee attacks.",
            "Dagger.Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one creature.Hit: 4 (1d4 + 2) piercing damage."
        ]
    },
    "cultist": {
        "name": "Cultist",
        "type": "Medium humanoid (any race)",
        "alignment": "any non-good alignment",
        "Armor Class": "12 (leather armor)",
        "Hit Points": "9 (2d8)",
        "Speed": "30 ft.",
        "Skills": "Deception +2, Religion +2",
        "Senses": "passive Perception 10",
        "Languages": "any one language (usually Common)",
        "Challenge": "1/8 (25 XP)",
        "STR": "11 (+0)",
        "DEX": "12 (+1)",
        "CON": "10 (+0)",
        "INT": "10 (+0)",
        "WIS": "11 (+0)",
        "CHA": "10 (+0)",
        "features": [
            "Dark Devotion. The cultist has advantage on saving throws against being charmed or frightened."
        ],
        "Actions": [
            "Scimitar.Melee Weapon Attack: +3 to hit, reach 5 ft., one creature.Hit: 4 (1d6 + 1) slashing damage."
        ]
    },
    "cyclops": {
        "name": "Cyclops",
        "type": "Huge giant",
        "alignment": "chaotic neutral",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "138 (12d12 + 60)",
        "Speed": "30 ft.",
        "Senses": "passive Perception 8",
        "Languages": "Giant",
        "Challenge": "6 (2300 XP)",
        "STR": "22 (+6)",
        "DEX": "11 (+0)",
        "CON": "20 (+5)",
        "INT": "8 (-1)",
        "WIS": "6 (-2)",
        "CHA": "10 (+0)",
        "features": [
            "Poor Depth Perception. The cyclops has disadvantage on any attack roll against a target more than 30 feet away."
        ],
        "Actions": [
            "Multiattack. The cyclops makes two greatclub attacks.",
            "Greatclub.Melee Weapon Attack: +9 to hit, reach 10 ft., one target.Hit: 19 (3d8 + 6) bludgeoning damage.",
            "Rock.Ranged Weapon Attack: +9 to hit, range 30/120 ft., one target.Hit: 28 (4d10 + 6) bludgeoning damage."
        ]
    },
    "dao": {
        "name": "Dao",
        "type": "Large elemental",
        "alignment": "neutral evil",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "187 (15d10 + 105)",
        "Speed": "30 ft., burrow 30 ft., fly 30 ft.",
        "Saving Throws": "Int +5, Wis +5, Cha +6",
        "Condition Immunities": "petrified",
        "Senses": "darkvision 120 ft., passive Perception 11",
        "Languages": "Terran",
        "Challenge": "11 (7200 XP)",
        "STR": "23 (+6)",
        "DEX": "12 (+1)",
        "CON": "24 (+7)",
        "INT": "12 (+1)",
        "WIS": "13 (+1)",
        "CHA": "14 (+2)",
        "features": [
            "Earth Glide. The dao can burrow through nonmagical, unworked earth and stone. While doing so, the dao doesn't disturb the material it moves through.",
            "Elemental Demise. If the dao dies, its body disintegrates into crystalline powder, leaving behind only equipment the dao was wearing or carrying.",
            "Innate Spellcasting. The dao's innate spellcasting ability is Charisma (spell save DC 14, +6 to hit with spell attacks). It can innately cast the following spells, requiring no material components:",
            "Sure-Footed. The dao has advantage on Strength and Dexterity saving throws made against effects that would knock it prone."
        ],
        "Actions": [
            "Multiattack. The dao makes two fist attacks or two maul attacks.",
            "Fist.Melee Weapon Attack: +10 to hit, reach 5 ft., one target.Hit: 15 (2d8 + 6) bludgeoning damage.",
            "Maul.Melee Weapon Attack: +10 to hit, reach 5 ft., one target.Hit: 20 (4d6 + 6) bludgeoning damage. If the target is a Huge or smaller creature, it must succeed on a DC 18 Strength check or be knocked prone."
        ]
    },
    "darkmantle": {
        "name": "Darkmantle",
        "type": "Small monstrosity",
        "alignment": "unaligned",
        "Armor Class": "11",
        "Hit Points": "22 (5d6 + 5)",
        "Speed": "10 ft., fly 30 ft.",
        "Skills": "Stealth +3",
        "Senses": "blindsight 60 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "16 (+3)",
        "DEX": "12 (+1)",
        "CON": "13 (+1)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "5 (-3)",
        "features": [
            "Echolocation. The darkmantle can't use its blindsight while deafened.",
            "False Appearance. While the darkmantle remains motionless, it is indistinguishable from a cave formation such as a stalactite or stalagmite."
        ],
        "Actions": [
            "Crush.Melee Weapon Attack: +5 to hit, reach 5 ft., one creature.Hit: 6 (1d6 + 3) bludgeoning damage, and the darkmantle attaches to the target. If the target is Medium or smaller and the darkmantle has advantage on the attack roll, it attaches by engulfing the target's head, and the target is also blinded and unable to breathe while the darkmantle is attached in this way. While attached to the target, the darkmantle can attack no other creature except the target but has advantage on its attack rolls. The darkmantle's speed also becomes 0, it can't benefit from any bonus to its speed, and it moves with the target. A creature can detach the darkmantle by making a successful DC 13 Strength check as an action. On its turn, the darkmantle can detach itself from the target by using 5 feet of movement.",
            "Darkness Aura (1/Day). A 15-foot radius of magical darkness extends out from the darkmantle, moves with it, and spreads around corners. The darkness lasts as long as the darkmantle maintains concentration, up to 10 minutes (as if concentrating on a spell). Darkvision can't penetrate this darkness, and no natural light can illuminate it. If any of the darkness overlaps with an area of light created by a spell of 2nd level or lower, the spell creating the light is dispelled."
        ]
    },
    "death-dog": {
        "name": "Death Dog",
        "type": "Medium monstrosity",
        "alignment": "neutral evil",
        "Armor Class": "12",
        "Hit Points": "39 (6d8 + 12)",
        "Speed": "40 ft.",
        "Skills": "Perception +5, Stealth +4",
        "Senses": "darkvision 120 ft., passive Perception 15",
        "Languages": "\u2014",
        "Challenge": "1 (200 XP)",
        "STR": "15 (+2)",
        "DEX": "14 (+2)",
        "CON": "14 (+2)",
        "INT": "3 (-4)",
        "WIS": "13 (+1)",
        "CHA": "6 (-2)",
        "features": [
            "Two-Headed. The dog has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned, or knocked unconscious."
        ],
        "Actions": [
            "Multiattack. The dog makes two bite attacks.",
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) piercing damage. If the target is a creature, it must succeed on a DC 12 Constitution saving throw against disease or become poisoned until the disease is cured. Every 24 hours that elapse, the creature must repeat the saving throw, reducing its hit point maximum by 5 (1d10) on a failure. This reduction lasts until the disease is cured. The creature dies if the disease reduces its hit point maximum to 0."
        ]
    },
    "death-knight": {
        "name": "Death Knight",
        "type": "Medium undead",
        "alignment": "chaotic evil",
        "Armor Class": "20 (plate, shield)",
        "Hit Points": "180 (19d8 + 95)",
        "Speed": "30 ft.",
        "Saving Throws": "Dex +6, Wis +9, Cha +10",
        "Damage Immunities": "necrotic, poison",
        "Condition Immunities": "exhaustion, frightened, poisoned",
        "Senses": "darkvision 120 ft., passive Perception 13",
        "Languages": "Abyssal, Common",
        "Challenge": "17 (18000 XP)",
        "STR": "20 (+5)",
        "DEX": "11 (+0)",
        "CON": "20 (+5)",
        "INT": "12 (+1)",
        "WIS": "16 (+3)",
        "CHA": "18 (+4)",
        "Reactions": [
            "Parry. The death knight adds 6 to its AC against one melee attack that would hit it. To do so, the death knight must see the attacker and be wielding a melee weapon."
        ],
        "features": [
            "Magic Resistance. The death knight has advantage on saving throws against spells and other magical effects.",
            "Marshal Undead. Unless the death knight is incapacitated, it and undead creatures of its choice within 60 feet of it have advantage on saving throws against features that turn undead.",
            "Spellcasting. The death knight is a 19th-level spell caster. Its spellcasting ability is Charisma (spell save DC 18, +10 to hit with spell attacks). It has the following paladin spells prepared:"
        ],
        "Actions": [
            "Multiattack. The death knight makes three longsword attacks.",
            "Longsword.Melee Weapon Attack: +11 to hit, reach 5 ft., one target.Hit: 9 (1d8 + 5) slashing damage, or 10 (1d10 + 5) slashing damage if used with two hands, plus 18 (4d8) necrotic damage.",
            "Hellfire Orb (1/Day). The death knight hurls a magical ball of fire that explodes at a point it can see within 120 feet of it. Each creature in a 20-foot-radius sphere centered on that point must make a DC 18 Dexterity saving throw. The sphere spreads around corners. A creature takes 35 (10d6) fire damage and 35 (10d6) necrotic damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "death-slaad": {
        "name": "Death Slaad",
        "type": "Medium aberration (Shapechanger)",
        "alignment": "chaotic evil",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "170 (20d8 + 80)",
        "Speed": "30 ft.",
        "Skills": "Arcana +6, Perception +8",
        "Damage Resistances": "acid, cold, fire, lightning, thunder",
        "Senses": "blindsight 60 ft., darkvision 60 ft., passive Perception 18",
        "Languages": "Slaad, telepathy 60 ft.",
        "Challenge": "10 (5900 XP)",
        "STR": "20 (+5)",
        "DEX": "15 (+2)",
        "CON": "19 (+4)",
        "INT": "15 (+2)",
        "WIS": "10 (+0)",
        "CHA": "16 (+3)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "death-tyrant": {
        "name": "Death Tyrant",
        "type": "Large undead",
        "alignment": "lawful evil",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "187 (25d10 + 50)",
        "Speed": "0 ft., fly 20 ft. (hover)",
        "Saving Throws": "Str +5, Con +7, Int +9, Wis +7, Cha +9",
        "Skills": "Perception +12",
        "Damage Immunities": "poison",
        "Condition Immunities": "charmed, exhaustion, paralyzed, petrified, poisoned, prone",
        "Senses": "darkvision 120 ft., passive Perception 22",
        "Languages": "Deep Speech, Undercommon",
        "Challenge": "14 (11500 XP)",
        "STR": "10 (+0)",
        "DEX": "14 (+2)",
        "CON": "14 (+2)",
        "INT": "19 (+4)",
        "WIS": "15 (+2)",
        "CHA": "19 (+4)",
        "Legendary actions": [
            "This full creature's stat block is not available (not OGL)."
        ],
        "features": [],
        "Actions": []
    },
    "deep-gnome-(svirfneblin)": {
        "features": []
    },
    "deer": {
        "name": "Deer",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "13",
        "Hit Points": "4 (1d8)",
        "Speed": "50 ft.",
        "Senses": "passive Perception 12",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "11 (+0)",
        "DEX": "16 (+3)",
        "CON": "11 (+0)",
        "INT": "2 (-4)",
        "WIS": "14 (+2)",
        "CHA": "5 (-3)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +2 to hit, reach 5 ft., one target.Hit: 2 (1d4) piercing damage."
        ]
    },
    "demilich": {
        "name": "Demilich",
        "type": "Tiny undead",
        "alignment": "neutral evil",
        "Armor Class": "20 (natural armor)",
        "Hit Points": "80 (32d4)",
        "Speed": "0 ft., fly 30 ft. (hover)",
        "Saving Throws": "Con +6, Int +11, Wis +9, Cha +11",
        "Damage Resistances": "bludgeoning, piercing, and slashing from magic weapons",
        "Damage Immunities": "necrotic, poison, psychic; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Condition Immunities": "charmed, deafened, exhaustion, frightened, paralyzed, petrified, poisoned, prone, stunned",
        "Senses": "truesight 120 ft., passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "18 (20000 XP)",
        "STR": "1 (-5)",
        "DEX": "20 (+5)",
        "CON": "10 (+0)",
        "INT": "20 (+5)",
        "WIS": "17 (+3)",
        "CHA": "20 (+5)",
        "Legendary actions": [
            "This full creature's stat block is not available (not OGL)."
        ],
        "features": [],
        "Actions": []
    },
    "deva": {
        "name": "Deva",
        "type": "Medium celestial",
        "alignment": "lawful good",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "136 (16d8 + 64)",
        "Speed": "30 ft., fly 90 ft.",
        "Saving Throws": "Wis +9, Cha +9",
        "Skills": "Insight +9, Perception +9",
        "Damage Resistances": "radiant; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Condition Immunities": "charmed, exhaustion, frightened",
        "Senses": "darkvision 120 ft., passive Perception 19",
        "Languages": "all, telepathy 120 ft.",
        "Challenge": "10 (5900 XP)",
        "STR": "18 (+4)",
        "DEX": "18 (+4)",
        "CON": "18 (+4)",
        "INT": "17 (+3)",
        "WIS": "20 (+5)",
        "CHA": "20 (+5)",
        "features": [
            "Angelic Weapons. The deva's weapon attacks are magical. When the deva hits with any weapon, the weapon deals an extra 4d8 radiant damage (included in the attack).",
            "Innate Spellcasting. The deva's spellcasting ability is Charisma (spell save DC 17). The deva can innately cast the following spells, requiring only verbal components:",
            "Magic Resistance. The deva has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack. The deva makes two melee attacks.",
            "Mace.Melee Weapon Attack: +8 to hit, reach 5 ft., one target.Hit: 7 (1d6 + 4) bludgeoning damage plus 18 (4d8) radiant damage.",
            "Healing Touch (3/Day). The deva touches another creature. The target magically regains 20 (4d8 + 2) hit points and is freed from any curse, disease, poison, blindness, or deafness.",
            "Change Shape. The deva magically polymorphs into a humanoid or beast that has a challenge rating equal to or less than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the deva's choice). In a new form, the deva retains its game statistics and ability to speak, but its AC, movement modes, Strength, Dexterity, and special senses are replaced by those of the new form, and it gains any statistics and capabilities (except class features, legendary actions, and lair actions) that the new form has but that it lacks."
        ]
    },
    "dire-wolf": {
        "name": "Dire Wolf",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "37 (5d10 + 10)",
        "Speed": "50 ft.",
        "Skills": "Perception +3, Stealth +4",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "1 (200 XP)",
        "STR": "17 (+3)",
        "DEX": "15 (+2)",
        "CON": "15 (+2)",
        "INT": "3 (-4)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Keen Hearing and Smell. The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell.",
            "Pack Tactics. The wolf has advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally isn't incapacitated."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) piercing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone."
        ]
    },
    "displacer-beast": {
        "name": "Displacer Beast",
        "type": "Large monstrosity",
        "alignment": "lawful evil",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "85 (10d10 + 30)",
        "Speed": "40 ft.",
        "Senses": "darkvision 60 ft., passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "3 (700 XP)",
        "STR": "18 (+4)",
        "DEX": "15 (+2)",
        "CON": "16 (+3)",
        "INT": "6 (-2)",
        "WIS": "12 (+1)",
        "CHA": "8 (-1)",
        "features": [
            "Avoidance. If the displacer beast is subjected to an effect that allows it to make a saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it fails.",
            "Displacement. The displacer beast projects a magical illusion that makes it appear to be standing near its actual location, causing attack rolls against it to have disadvantage. If it is hit by an attack, this trait is disrupted until the end of its next turn. This trait is also disrupted while the displacer beast is incapacitated or has a speed of 0."
        ],
        "Actions": [
            "Multiattack. The displacer beast makes two attacks with its tentacles.",
            "Tentacle.Melee Weapon Attack: +6 to hit, reach 10 ft., one target.Hit: 7 (1d6 + 4) bludgeoning damage plus 3 (1d6) piercing damage."
        ]
    },
    "djinni": {
        "name": "Djinni",
        "type": "Large elemental",
        "alignment": "chaotic good",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "161 (14d10 + 84)",
        "Speed": "30 ft., fly 90 ft.",
        "Saving Throws": "Dex +6, Wis +7, Cha +9",
        "Damage Immunities": "lightning, thunder",
        "Senses": "darkvision 120 ft., passive Perception 13",
        "Languages": "Auran",
        "Challenge": "11 (7200 XP)",
        "STR": "21 (+5)",
        "DEX": "15 (+2)",
        "CON": "22 (+6)",
        "INT": "15 (+2)",
        "WIS": "16 (+3)",
        "CHA": "20 (+5)",
        "features": [
            "Elemental Demise. If the djinni dies, its body disintegrates into a warm breeze, leaving behind only equipment the djinni was wearing or carrying.",
            "Innate Spellcasting. The djinni's innate spellcasting ability is Charisma (spell save DC 17, +9 to hit with spell attacks). It can innately cast the following spells, requiring no material components:"
        ],
        "Actions": [
            "Multiattack. The djinni makes three scimitar attacks.",
            "Scimitar.Melee Weapon Attack: +9 to hit, reach 5 ft., one target.Hit: 12 (2d6 + 5) slashing damage plus 3 (1d6) lightning or thunder damage (djinni's choice).",
            "Create Whirlwind. A 5-foot-radius, 30-foot-tall cylinder of swirling air magically forms on a point the djinni can see within 120 feet of it. The whirlwind lasts as long as the djinni maintains concentration (as if concentrating on a spell). Any creature but the djinni that enters the whirlwind must succeed on a DC 18 Strength saving throw or be restrained by it. The djinni can move the whirlwind up to 60 feet as an action, and creatures restrained by the whirlwind move with it. The whirlwind ends if the djinni loses sight of it. A creature can use its action to free a creature restrained by the whirlwind, including itself, by succeeding on a DC 18 Strength check. If the check succeeds, the creature is no longer restrained and moves to the nearest space outside the whirlwind."
        ]
    },
    "doppelganger": {
        "name": "Doppelganger",
        "type": "Medium monstrosity (Shapechanger)",
        "alignment": "neutral",
        "Armor Class": "14",
        "Hit Points": "52 (8d8 + 16)",
        "Speed": "30 ft.",
        "Skills": "Deception +6, Insight +3",
        "Condition Immunities": "charmed",
        "Senses": "darkvision 60 ft., passive Perception 11",
        "Languages": "Common",
        "Challenge": "3 (700 XP)",
        "STR": "11 (+0)",
        "DEX": "18 (+4)",
        "CON": "14 (+2)",
        "INT": "11 (+0)",
        "WIS": "12 (+1)",
        "CHA": "14 (+2)",
        "features": [
            "Shapechanger. The doppelganger can use its action to polymorph into a Small or Medium humanoid it has seen, or back into its true form. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.",
            "Ambusher. In the first round of a combat, the doppelganger has advantage on attack rolls against any creature it surprised.",
            "Surprise Attack. If the doppelganger surprises a creature and hits it with an attack during the first round of combat, the target takes an extra 10 (3d6) damage from the attack."
        ],
        "Actions": [
            "Multiattack. The doppelganger makes two melee attacks.",
            "Slam.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 7 (1d6 + 4) bludgeoning damage.",
            "Read Thoughts. The doppelganger magically reads the surface thoughts of one creature within 60 feet of it. The effect can penetrate barriers, but 3 feet of wood or dirt, 2 feet of stone, 2 inches of metal, or a thin sheet of lead blocks it. While the target is in range, the doppelganger can continue reading its thoughts, as long as the doppelganger's concentration isn't broken (as if concentrating on a spell). While reading the target's mind, the doppelganger has advantage on Wisdom (Insight) and Charisma (Deception, Intimidation, and Persuasion) checks against the target."
        ]
    },
    "draft-horse": {
        "name": "Draft Horse",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "10",
        "Hit Points": "19 (3d10 + 3)",
        "Speed": "40 ft.",
        "Senses": "passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "18 (+4)",
        "DEX": "10 (+0)",
        "CON": "12 (+1)",
        "INT": "2 (-4)",
        "WIS": "11 (+0)",
        "CHA": "7 (-2)",
        "features": [],
        "Actions": [
            "Hooves.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 9 (2d4 + 4) bludgeoning damage."
        ]
    },
    "dragon-turtle": {
        "name": "Dragon Turtle",
        "type": "Gargantuan dragon",
        "alignment": "neutral",
        "Armor Class": "20 (natural armor)",
        "Hit Points": "341 (22d20 + 110)",
        "Speed": "20 ft., swim 40 ft.",
        "Saving Throws": "Dex +6, Con +11, Wis +7",
        "Damage Resistances": "fire",
        "Senses": "darkvision 120 ft., passive Perception 11",
        "Languages": "Aquan, Draconic",
        "Challenge": "17 (18000 XP)",
        "STR": "25 (+7)",
        "DEX": "10 (+0)",
        "CON": "20 (+5)",
        "INT": "10 (+0)",
        "WIS": "12 (+1)",
        "CHA": "12 (+1)",
        "features": [
            "Amphibious. The dragon turtle can breathe air and water."
        ],
        "Actions": [
            "Multiattack. The dragon turtle makes three attacks: one with its bite and two with its claws. It can make one tail attack in place of its two claw attacks.",
            "Bite.Melee Weapon Attack: +13 to hit, reach 15 ft., one target.Hit: 26 (3d12 + 7) piercing damage.",
            "Claw.Melee Weapon Attack: +13 to hit, reach 10 ft., one target.Hit: 16 (2d8 + 7) slashing damage.",
            "Tail.Melee Weapon Attack: +13 to hit, reach 15 ft., one target.Hit: 26 (3d12 + 7) bludgeoning damage. If the target is a creature, it must succeed on a DC 20 Strength saving throw or be pushed up to 10 feet away from the dragon turtle and knocked prone.",
            "Steam Breath (Recharge 5-6). The dragon turtle exhales scalding steam in a 60-foot cone. Each creature in that area must make a DC 18 Constitution saving throw, taking 52 (15d 6) fire damage on a failed save, or half as much damage on a successful one. Being underwater doesn't grant resistance against this damage."
        ]
    },
    "dretch": {
        "name": "Dretch",
        "type": "Small fiend (Demon)",
        "alignment": "chaotic evil",
        "Armor Class": "11 (natural armor)",
        "Hit Points": "18 (4d6 + 4)",
        "Speed": "20 ft.",
        "Damage Resistances": "cold, fire, lightning",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 60 ft., passive Perception 9",
        "Languages": "Abyssal, telepathy 60 ft. (works only with creatures that understand Abyssal)",
        "Challenge": "1/4 (50 XP)",
        "STR": "11 (+0)",
        "DEX": "11 (+0)",
        "CON": "12 (+1)",
        "INT": "5 (-3)",
        "WIS": "8 (-1)",
        "CHA": "3 (-4)",
        "features": [],
        "Actions": [
            "Multiattack. The dretch makes two attacks: one with its bite and one with its claws.",
            "Bite.Melee Weapon Attack: +2 to hit, reach 5 ft., one target.Hit: 3 (1d6) piercing damage.",
            "Claws.Melee Weapon Attack: +2 to hit, reach 5 ft., one target.Hit: 5 (2d4) slashing damage.",
            "Fetid Cloud (1/Day). A 10-foot radius of disgusting green gas extends out from the dretch. The gas spreads around corners, and its area is lightly obscured. It lasts for 1 minute or until a strong wind disperses it. Any creature that starts its turn in that area must succeed on a DC 11 Constitution saving throw or be poisoned until the start of its next turn. While poisoned in this way, the target can take either an action or a bonus action on its turn, not both, and can't take reactions."
        ]
    },
    "drider": {
        "name": "Drider",
        "type": "Large monstrosity",
        "alignment": "chaotic evil",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "123 (13d10 + 52)",
        "Speed": "30 ft., climb 30 ft.",
        "Skills": "Perception +5, Stealth +9",
        "Senses": "darkvision 120 ft., passive Perception 15",
        "Languages": "Elvish, Undercommon",
        "Challenge": "6 (2300 XP)",
        "STR": "16 (+3)",
        "DEX": "16 (+3)",
        "CON": "18 (+4)",
        "INT": "13 (+1)",
        "WIS": "14 (+2)",
        "CHA": "12 (+1)",
        "features": [
            "Fey Ancestry. The drider has advantage on saving throws against being charmed, and magic can't put the drider to sleep.",
            "Innate Spellcasting. The drider's innate spellcasting ability is Wisdom (spell save DC 13). The drider can innately cast the following spells, requiring no material components:",
            "Spider Climb. The drider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.",
            "Sunlight Sensitivity. While in sunlight, the drider has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.",
            "Web Walker. The drider ignores movement restrictions caused by webbing."
        ],
        "Actions": [
            "Multiattack. The drider makes three attacks, either with its longsword or its longbow. It can replace one of those attacks with a bite attack.",
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one creature.Hit: 2 (1d4) piercing damage plus 9 (2d8) poison damage.",
            "Longsword.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands.",
            "Longbow.Ranged Weapon Attack: +6 to hit, range 150/600 ft., one target.Hit: 7 (1d8 + 3) piercing damage plus 4 (1d8) poison damage."
        ]
    },
    "drow": {
        "name": "Drow",
        "type": "Medium humanoid (Elf)",
        "alignment": "neutral evil",
        "Armor Class": "15 (chain shirt)",
        "Hit Points": "13 (3d8)",
        "Speed": "30 ft.",
        "Skills": "Perception +2, Stealth +4",
        "Senses": "darkvision 120 ft., passive Perception 12",
        "Languages": "Elvish, Undercommon",
        "Challenge": "1/4 (50 XP)",
        "STR": "10 (+0)",
        "DEX": "14 (+2)",
        "CON": "10 (+0)",
        "INT": "11 (+0)",
        "WIS": "11 (+0)",
        "CHA": "12 (+1)",
        "features": [
            "Fey Ancestry. The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.",
            "Innate Spellcasting. The drow's spellcasting ability is Charisma (spell save DC 11). It can innately cast the following spells, requiring no material components:",
            "Sunlight Sensitivity. While in sunlight, the drow has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
        ],
        "Actions": [
            "Shortsword.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) piercing damage.",
            "Hand Crossbow.Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target.Hit: 5 (1d6 + 2) piercing damage, and the target must succeed on a DC 13 Constitution saving throw or be poisoned for 1 hour. If the saving throw fails by 5 or more, the target is also unconscious while poisoned in this way. The target wakes up if it takes damage or if another creature takes an action to shake it awake."
        ]
    },
    "drow-elite-warrior": {
        "name": "Drow Elite Warrior",
        "type": "Medium humanoid (Elf)",
        "alignment": "neutral evil",
        "Armor Class": "18 (studded leather, shield)",
        "Hit Points": "71 (11d8 + 22)",
        "Speed": "30 ft.",
        "Saving Throws": "Dex +7, Con +5, Wis +4",
        "Skills": "Perception +4, Stealth +10",
        "Senses": "darkvision 120 ft., passive Perception 14",
        "Languages": "Elvish, Undercommon",
        "Challenge": "5 (1800 XP)",
        "STR": "13 (+1)",
        "DEX": "18 (+4)",
        "CON": "14 (+2)",
        "INT": "11 (+0)",
        "WIS": "13 (+1)",
        "CHA": "12 (+1)",
        "Reactions": [
            "This full creature's stat block is not available (not OGL)."
        ],
        "features": [],
        "Actions": []
    },
    "drow-mage": {
        "name": "Drow Mage",
        "type": "Medium humanoid (Elf)",
        "alignment": "neutral evil",
        "Armor Class": "12 (15 with",
        "Hit Points": "45 (10d8)",
        "Speed": "30 ft.",
        "Skills": "Arcana +6, Deception +5, Perception +4, Stealth +5",
        "Senses": "darkvision 120 ft., passive Perception 14",
        "Languages": "Elvish, Undercommon",
        "Challenge": "7 (2900 XP)",
        "STR": "9 (-1)",
        "DEX": "14 (+2)",
        "CON": "10 (+0)",
        "INT": "17 (+3)",
        "WIS": "13 (+1)",
        "CHA": "12 (+1)",
        "features": [
            "Fey Ancestry. The drow has advantage on saving throws against being charmed, and magic can't put the drow to sleep.",
            "Innate Spellcasting. The drow's innate spellcasting ability is Charisma (spell save DC 12). It can innately cast the following spells, requiring no material components:",
            "Spellcasting. The drow is a 10th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 14, +6 to hit with spell attacks). The drow has the following wizard spells prepared:",
            "Sunlight Sensitivity. While in sunlight, the drow has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
        ],
        "Actions": [
            "Staff.Melee Weapon Attack: +2 to hit, reach 5 ft., one target.Hit: 2 (1d6 - 1) bludgeoning damage, or 3 (1d8 - 1) bludgeoning damage if used with two hands, plus 3 (1d 6) poison damage.",
            "Summon Demon (1/Day). The drow magically summons a quasit, or attempts to summon a shadow demon with a 50 percent chance of success. The summoned demon appears in an unoccupied space within 60 feet of its summoner, acts as an ally of its summoner, and can't summon other demons. It remains for 10 minutes, until it or its summoner dies, or until its summoner dismisses it as an action."
        ]
    },
    "drow-priestess-of-lolth": {
        "name": "Drow Priestess of Lolth",
        "type": "Medium humanoid (Elf)",
        "alignment": "neutral evil",
        "Armor Class": "16 (scale mail)",
        "Hit Points": "71 (13d8 + 13)",
        "Speed": "30 ft.",
        "Saving Throws": "Con +4, Wis +6, Cha +7",
        "Skills": "Insight +6, Perception +6, Religion +4, Stealth +5",
        "Senses": "darkvision 120 ft., passive Perception 16",
        "Languages": "Elvish, Undercommon",
        "Challenge": "8 (3900 XP)",
        "STR": "10 (+0)",
        "DEX": "14 (+2)",
        "CON": "12 (+1)",
        "INT": "13 (+1)",
        "WIS": "17 (+3)",
        "CHA": "18 (+4)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "druid": {
        "name": "Druid",
        "type": "Medium humanoid (any race)",
        "alignment": "any alignment",
        "Armor Class": "11 (16 with",
        "Hit Points": "27 (5d8 + 5)",
        "Speed": "30 ft.",
        "Skills": "Medicine +4, Nature +3, Perception +4",
        "Senses": "passive Perception 14",
        "Languages": "Druidic plus any two languages",
        "Challenge": "2 (450 XP)",
        "STR": "10 (+0)",
        "DEX": "12 (+1)",
        "CON": "13 (+1)",
        "INT": "12 (+1)",
        "WIS": "15 (+2)",
        "CHA": "11 (+0)",
        "features": [
            "Spellcasting. The druid is a 4th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). It has the following druid spells prepared:"
        ],
        "Actions": [
            "Quarterstaff.Melee Weapon Attack: +2 to hit (+4 to hit withshillelagh), reach 5 ft., one target.Hit: 3 (1d6) bludgeoning damage, 4 (1d8) bludgeoning damage if wielded with two hands, or 6 (1d8 + 2) bludgeoning damage withshillelagh."
        ]
    },
    "dryad": {
        "name": "Dryad",
        "type": "Medium fey",
        "alignment": "neutral",
        "Armor Class": "11 (16 with",
        "Hit Points": "22 (5d8)",
        "Speed": "30 ft.",
        "Skills": "Perception +4, Stealth +5",
        "Senses": "darkvision 60 ft., passive Perception 14",
        "Languages": "Elvish, Sylvan",
        "Challenge": "1 (200 XP)",
        "STR": "10 (+0)",
        "DEX": "12 (+1)",
        "CON": "11 (+0)",
        "INT": "14 (+2)",
        "WIS": "15 (+2)",
        "CHA": "18 (+4)",
        "features": [
            "Innate Spellcasting. The dryad's innate spellcasting ability is Charisma (spell save DC 14). The dryad can innately cast the following spells, requiring no material components:",
            "Magic Resistance. The dryad has advantage on saving throws against spells and other magical effects.",
            "Speak with Beasts and Plants. The dryad can communicate with beasts and plants as if they shared a language.",
            "Tree Stride. Once on her turn, the dryad can use 10 feet of her movement to step magically into one living tree within her reach and emerge from a second living tree within 60 feet of the first tree, appearing in an unoccupied space within 5 feet of the second tree. Both trees must be Large or bigger."
        ],
        "Actions": [
            "Club.Melee Weapon Attack: +2 to hit (+6 to hit withshillelagh), reach 5 ft., one target.Hit: 2 (1d4) bludgeoning damage, or 8 (1d8 + 4) bludgeoning damage withshillelagh.",
            "Fey Charm. The dryad targets one humanoid or beast that she can see within 30 feet of her. If the target can see the dryad, it must succeed on a DC 14 Wisdom saving throw or be magically charmed. The charmed creature regards the dryad as a trusted friend to be heeded and protected. Although the target isn't under the dryad's control, it takes the dryad's requests or actions in the most favorable way it can. Each time the dryad or its allies do anything harmful to the target, it can repeat the saving throw, ending the effect on itself on a success. Otherwise, the effect lasts 24 hours or until the dryad dies, is on a different plane of existence from the target, or ends the effect as a bonus action. If a target's saving throw is successful, the target is immune to the dryad's Fey Charm for the next 24 hours. The dryad can have no more than one humanoid and up to three beasts charmed at a time."
        ]
    },
    "duergar": {
        "name": "Duergar",
        "type": "Medium humanoid (Dwarf)",
        "alignment": "lawful evil",
        "Armor Class": "16 (scale mail, shield)",
        "Hit Points": "26 (4d8 + 8)",
        "Speed": "25 ft.",
        "Damage Resistances": "poison",
        "Senses": "darkvision 120 ft., passive Perception 10",
        "Languages": "Dwarvish, Undercommon",
        "Challenge": "1 (200 XP)",
        "STR": "14 (+2)",
        "DEX": "11 (+0)",
        "CON": "14 (+2)",
        "INT": "11 (+0)",
        "WIS": "10 (+0)",
        "CHA": "9 (-1)",
        "features": [
            "Duergar Resilience. The duergar has advantage on saving throws against poison, spells, and illusions, as well as to resist being charmed or paralyzed.",
            "Sunlight Sensitivity. While in sunlight, the duergar has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
        ],
        "Actions": [
            "Enlarge (Recharges after a Short or Long Rest). For 1 minute, the duergar magically increases in size, along with anything it is wearing or carrying. While enlarged, the duergar is Large, doubles its damage dice on Strength-based weapon attacks (included in the attacks), and makes Strength checks and Strength saving throws with advantage. If the duergar lacks the room to become Large, it attains the maximum size possible in the space available.",
            "War Pick.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 6 (1d8 + 2) piercing damage, or 11 (2d8 + 2) piercing damage while enlarged.",
            "Javelin.Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target.Hit: 5 (1d6 + 2) piercing damage, or 9 (2d6 + 2) piercing damage while enlarged.",
            "Invisibility (Recharges after a Short or Long Rest). The duergar magically turns invisible until it attacks, casts a spell, or uses its Enlarge, or until its concentration is broken, up to 1 hour (as if concentrating on a spell). Any equipment the duergar wears or carries is invisible with it."
        ]
    },
    "duodrone": {
        "name": "Duodrone",
        "type": "Medium construct",
        "alignment": "lawful neutral",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "11 (2d8 + 2)",
        "Speed": "30 ft.",
        "Senses": "truesight 120 ft., passive Perception 10",
        "Languages": "Modron",
        "Challenge": "1/4 (50 XP)",
        "STR": "11 (+0)",
        "DEX": "13 (+1)",
        "CON": "12 (+1)",
        "INT": "6 (-2)",
        "WIS": "10 (+0)",
        "CHA": "7 (-2)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "dust-mephit": {
        "name": "Dust Mephit",
        "type": "Small elemental",
        "alignment": "neutral evil",
        "Armor Class": "12",
        "Hit Points": "17 (5d6)",
        "Speed": "30 ft., fly 30 ft.",
        "Skills": "Perception +2, Stealth +4",
        "Damage Vulnerabilities": "fire",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 60 ft., passive Perception 12",
        "Languages": "Auran, Terran",
        "Challenge": "1/2 (100 XP)",
        "STR": "5 (-3)",
        "DEX": "14 (+2)",
        "CON": "10 (+0)",
        "INT": "9 (-1)",
        "WIS": "11 (+0)",
        "CHA": "10 (+0)",
        "features": [
            "Death Burst. When the mephit dies, it explodes in a burst of dust. Each creature within 5 feet of it must then succeed on a DC 10 Constitution saving throw or be blinded for 1 minute. A blinded creature can repeat the saving throw on each of its turns, ending the effect on itself on a success.",
            "Innate Spellcasting (1/Day). The mephit can innately castsleep, requiring no material components. Its innate spellcasting ability is Charisma."
        ],
        "Actions": [
            "Claws.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 4 (1d4 + 2) slashing damage.",
            "Blinding Breath (Recharge 6). The mephit exhales a 15-foot cone of blinding dust. Each creature in that area must succeed on a DC 10 Dexterity saving throw or be blinded for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        ]
    },
    "eagle": {
        "name": "Eagle",
        "type": "Small beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "3 (1d6)",
        "Speed": "10 ft., fly 60 ft.",
        "Skills": "Perception +4",
        "Senses": "passive Perception 14",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "6 (-2)",
        "DEX": "15 (+2)",
        "CON": "10 (+0)",
        "INT": "2 (-4)",
        "WIS": "14 (+2)",
        "CHA": "7 (-2)",
        "features": [
            "Keen Sight. The eagle has advantage on Wisdom (Perception) checks that rely on sight."
        ],
        "Actions": [
            "Talons.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 4 (1d4 + 2) slashing damage."
        ]
    },
    "earth-elemental": {
        "name": "Earth Elemental",
        "type": "Large elemental",
        "alignment": "neutral",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "126 (12d10 + 60)",
        "Speed": "30 ft., burrow 30 ft.",
        "Damage Vulnerabilities": "thunder",
        "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "poison",
        "Condition Immunities": "exhaustion, paralyzed, petrified, poisoned, unconscious",
        "Senses": "darkvision 60 ft., tremorsense 60 ft., passive Perception 10",
        "Languages": "Terran",
        "Challenge": "5 (1800 XP)",
        "STR": "20 (+5)",
        "DEX": "8 (-1)",
        "CON": "20 (+5)",
        "INT": "5 (-3)",
        "WIS": "10 (+0)",
        "CHA": "5 (-3)",
        "features": [
            "Earth Glide. The elemental can burrow through nonmagical, unworked earth and stone. While doing so, the elemental doesn't disturb the material it moves through.",
            "Siege Monster. The elemental deals double damage to objects and structures."
        ],
        "Actions": [
            "Multiattack. The elemental makes two slam attacks.",
            "Slam.Melee Weapon Attack: +8 to hit, reach 10 ft., one target.Hit: 14 (2d8 + 5) bludgeoning damage."
        ]
    },
    "efreeti": {
        "name": "Efreeti",
        "type": "Large elemental",
        "alignment": "lawful evil",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "200 (16d10 + 112)",
        "Speed": "40 ft., fly 60 ft.",
        "Saving Throws": "Int +7, Wis +6, Cha +7",
        "Damage Immunities": "fire",
        "Senses": "darkvision 120 ft., passive Perception 12",
        "Languages": "Ignan",
        "Challenge": "11 (7200 XP)",
        "STR": "22 (+6)",
        "DEX": "12 (+1)",
        "CON": "24 (+7)",
        "INT": "16 (+3)",
        "WIS": "15 (+2)",
        "CHA": "16 (+3)",
        "features": [
            "Elemental Demise. If the efreeti dies, its body disintegrates in a flash of fire and puff of smoke, leaving behind only equipment the efreeti was wearing or carrying.",
            "Innate Spellcasting. The efreeti's innate spellcasting ability is Charisma (spell save DC 15, +7 to hit with spell attacks). It can innately cast the following spells, requiring no material components:"
        ],
        "Actions": [
            "Multiattack. The efreeti makes two scimitar attacks or uses its Hurl Flame twice.",
            "Scimitar.Melee Weapon Attack: +10 to hit, reach 5 ft., one target.Hit: 13 (2d6 + 6) slashing damage plus 7 (2d6) fire damage.",
            "Hurl Flame.Ranged Spell Attack: +7 to hit, range 120 ft., one target.Hit: 17 (5d6) fire damage."
        ]
    },
    "elephant": {
        "name": "Elephant",
        "type": "Huge beast",
        "alignment": "unaligned",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "76 (8d12 + 24)",
        "Speed": "40 ft.",
        "Senses": "passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "4 (1100 XP)",
        "STR": "22 (+6)",
        "DEX": "9 (-1)",
        "CON": "17 (+3)",
        "INT": "3 (-4)",
        "WIS": "11 (+0)",
        "CHA": "6 (-2)",
        "features": [
            "Trampling Charge. If the elephant moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 12 Strength saving throw or be knocked prone. If the target is prone, the elephant can make one stomp attack against it as a bonus action."
        ],
        "Actions": [
            "Gore.Melee Weapon Attack: +8 to hit, reach 5 ft., one target.Hit: 19 (3d8 + 6) piercing damage.",
            "Stomp.Melee Weapon Attack: +8 to hit, reach 5 ft., one prone creature.Hit: 22 (3d10 + 6) bludgeoning damage."
        ]
    },
    "elk": {
        "name": "Elk",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "10",
        "Hit Points": "13 (2d10 + 2)",
        "Speed": "50 ft.",
        "Senses": "passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "16 (+3)",
        "DEX": "10 (+0)",
        "CON": "12 (+1)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "6 (-2)",
        "features": [
            "Charge. If the elk moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone."
        ],
        "Actions": [
            "Ram.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 6 (1d6 + 3) bludgeoning damage.",
            "Hooves.Melee Weapon Attack: +5 to hit, reach 5 ft., one prone creature.Hit: 8 (2d4 + 3) bludgeoning damage."
        ]
    },
    "empyrean": {
        "name": "Empyrean",
        "type": "Huge celestial (Titan)",
        "alignment": "chaotic good (75 %) or neutral evil (25 %)",
        "Armor Class": "22 (natural armor)",
        "Hit Points": "313 (19d12 + 190)",
        "Speed": "50 ft., fly 50 ft., swim 50 ft.",
        "Saving Throws": "Str +17, Int +12, Wis +13, Cha +15",
        "Skills": "Insight +13, Persuasion +15",
        "Damage Immunities": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "Senses": "truesight 120 ft., passive Perception 16",
        "Languages": "all",
        "Challenge": "23 (50000 XP)",
        "STR": "30 (+10)",
        "DEX": "21 (+5)",
        "CON": "30 (+10)",
        "INT": "21 (+5)",
        "WIS": "22 (+6)",
        "CHA": "27 (+8)",
        "Legendary actions": [
            "This full creature's stat block is not available (not OGL)."
        ],
        "features": [],
        "Actions": []
    },
    "erinyes": {
        "name": "Erinyes",
        "type": "Medium fiend (Devil)",
        "alignment": "lawful evil",
        "Armor Class": "18 (plate)",
        "Hit Points": "153 (18d8 + 72)",
        "Speed": "30 ft., fly 60 ft.",
        "Saving Throws": "Dex +7, Con +8, Wis +6, Cha +8",
        "Damage Resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered",
        "Damage Immunities": "fire, poison",
        "Condition Immunities": "poisoned",
        "Senses": "truesight 120 ft., passive Perception 12",
        "Languages": "Infernal, telepathy 120 ft.",
        "Challenge": "12 (8400 XP)",
        "STR": "18 (+4)",
        "DEX": "16 (+3)",
        "CON": "18 (+4)",
        "INT": "14 (+2)",
        "WIS": "14 (+2)",
        "CHA": "18 (+4)",
        "Reactions": [
            "Parry. The erinyes adds 4 to its AC against one melee attack that would hit it. To do so, the erinyes must see the attacker and be wielding a melee weapon."
        ],
        "features": [
            "Hellish Weapons. The erinyes's weapon attacks are magical and deal an extra 13 (3d8) poison damage on a hit (included in the attacks).",
            "Magic Resistance. The erinyes has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack. The erinyes makes three attacks.",
            "Longsword.Melee Weapon Attack: +8 to hit, reach 5 ft., one target.Hit: 8 (1d8 + 4) slashing damage, or 9 (1d10 + 4) slashing damage if used with two hands, plus 13 (3d8) poison damage.",
            "Longbow.Ranged Weapon Attack: +7 to hit, range 150/600 ft., one target.Hit: 7 (1d8 + 3) piercing damage plus 13 (3d8) poison damage, and the target must succeed on a DC 14 Constitution saving throw or be poisoned. The poison lasts until it is removed by thelesser restorationspell or similar magic."
        ]
    },
    "ettercap": {
        "name": "Ettercap",
        "type": "Medium monstrosity",
        "alignment": "neutral evil",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "44 (8d8 + 8)",
        "Speed": "30 ft., climb 30 ft.",
        "Skills": "Perception +3, Stealth +4, Survival +3",
        "Senses": "darkvision 60 ft., passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "14 (+2)",
        "DEX": "15 (+2)",
        "CON": "13 (+1)",
        "INT": "7 (-2)",
        "WIS": "12 (+1)",
        "CHA": "8 (-1)",
        "features": [
            "Spider Climb. The ettercap can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.",
            "Web Sense. While in contact with a web, the ettercap knows the exact location of any other creature in contact with the same web.",
            "Web Walker. The ettercap ignores movement restrictions caused by webbing."
        ],
        "Actions": [
            "Multiattack. The ettercap makes two attacks: one with its bite and one with its claws.",
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 6 (1d8 + 2) piercing damage plus 4 (1d8) poison damage. The target must succeed on a DC 11 Constitution saving throw or be poisoned for 1 minute. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
            "Claws.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 7 (2d4 + 2) slashing damage.",
            "Web (Recharge 5-6).Ranged Weapon Attack: +4 to hit, range 30/60 ft., one Large or smaller creature.Hit: The creature is restrained by webbing. As an action, the restrained creature can make a DC 11 Strength check, escaping from the webbing on a success. The effect ends if the webbing is destroyed. The webbing has AC 10, 5 hit points, vulnerability to fire damage, and immunity to bludgeoning, poison, and psychic damage."
        ]
    },
    "ettin": {
        "name": "Ettin",
        "type": "Large giant",
        "alignment": "chaotic evil",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "85 (10d10 + 30)",
        "Speed": "40 ft.",
        "Skills": "Perception +4",
        "Senses": "darkvision 60 ft., passive Perception 14",
        "Languages": "Giant, Orc",
        "Challenge": "4 (1100 XP)",
        "STR": "21 (+5)",
        "DEX": "8 (-1)",
        "CON": "17 (+3)",
        "INT": "6 (-2)",
        "WIS": "10 (+0)",
        "CHA": "8 (-1)",
        "features": [
            "Two Heads. The ettin has advantage on Wisdom (Perception) checks and on saving throws against being blinded, charmed, deafened, frightened, stunned and knocked unconscious.",
            "Wakeful. When one of the ettin's heads is asleep, its other head is awake."
        ],
        "Actions": [
            "Multiattack. The ettin makes two attacks: one with its battleaxe and one with its morningstar.",
            "Battleaxe.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 14 (2d8 + 5) slashing damage.",
            "Morningstar.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 14 (2d8 + 5) piercing damage."
        ]
    },
    "faerie-dragon": {
        "name": "Faerie Dragon",
        "type": "Tiny dragon",
        "alignment": "chaotic good",
        "Armor Class": "15",
        "Hit Points": "14 (4d4 + 4)",
        "Speed": "10 ft., fly 60 ft.",
        "Skills": "Arcana +4, Perception +3, Stealth +7",
        "Senses": "darkvision 60 ft., passive Perception 13",
        "Languages": "Draconic, Sylvan",
        "Challenge": "1 (200 XP)",
        "STR": "3 (-4)",
        "DEX": "20 (+5)",
        "CON": "13 (+1)",
        "INT": "14 (+2)",
        "WIS": "12 (+1)",
        "CHA": "16 (+3)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "fire-elemental": {
        "name": "Fire Elemental",
        "type": "Large elemental",
        "alignment": "neutral",
        "Armor Class": "13",
        "Hit Points": "102 (12d10 + 36)",
        "Speed": "50 ft.",
        "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "fire, poison",
        "Condition Immunities": "exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Ignan",
        "Challenge": "5 (1800 XP)",
        "STR": "10 (+0)",
        "DEX": "17 (+3)",
        "CON": "16 (+3)",
        "INT": "6 (-2)",
        "WIS": "10 (+0)",
        "CHA": "7 (-2)",
        "features": [
            "Fire Form. The elemental can move through a space as narrow as 1 inch wide without squeezing. A creature that touches the elemental or hits it with a melee attack while within 5 feet of it takes 5 (1d10) fire damage. In addition, the elemental can enter a hostile creature's space and stop there. The first time it enters a creature's space on a turn, that creature takes 5 (1d10) fire damage and catches fire; until someone takes an action to douse the fire, the creature takes 5 (1d10) fire damage at the start of each of its turns.",
            "Illumination. The elemental sheds bright light in a 30-foot radius and dim light in an additional 30 feet.",
            "Water Susceptibility. For every 5 feet the elemental moves in water, or for every gallon of water splashed on it, it takes 1 cold damage."
        ],
        "Actions": [
            "Multiattack. The elemental makes two touch attacks.",
            "Touch.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) fire damage. If the target is a creature or a flammable object, it ignites. Until a creature takes an action to douse the fire, the target takes 5 (1d10) fire damage at the start of each of its turns."
        ]
    },
    "fire-giant": {
        "name": "Fire Giant",
        "type": "Huge giant",
        "alignment": "lawful evil",
        "Armor Class": "18 (plate)",
        "Hit Points": "162 (13d12 + 78)",
        "Speed": "30 ft.",
        "Saving Throws": "Dex +3, Con +10, Cha +5",
        "Skills": "Athletics +11, Perception +6",
        "Damage Immunities": "fire",
        "Senses": "passive Perception 16",
        "Languages": "Giant",
        "Challenge": "9 (5000 XP)",
        "STR": "25 (+7)",
        "DEX": "9 (-1)",
        "CON": "23 (+6)",
        "INT": "10 (+0)",
        "WIS": "14 (+2)",
        "CHA": "13 (+1)",
        "features": [],
        "Actions": [
            "Multiattack. The giant makes two greatsword attacks.",
            "Greatsword.Melee Weapon Attack: +11 to hit, reach 10 ft., one target.Hit: 28 (6d6 + 7) slashing damage.",
            "Rock.Ranged Weapon Attack: +11 to hit, range 60/240 ft., one target.Hit: 29 (4d10 + 7) bludgeoning damage."
        ]
    },
    "fire-snake": {
        "name": "Fire Snake",
        "type": "Medium elemental",
        "alignment": "neutral evil",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "22 (5d8)",
        "Speed": "30 ft.",
        "Damage Vulnerabilities": "cold",
        "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "fire",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "understands Ignan but can't speak",
        "Challenge": "1 (200 XP)",
        "STR": "12 (+1)",
        "DEX": "14 (+2)",
        "CON": "11 (+0)",
        "INT": "7 (-2)",
        "WIS": "10 (+0)",
        "CHA": "8 (-1)",
        "features": [
            "Heated Body. A creature that touches the snake or hits it with a melee attack while within 5 feet of it takes 3 (1d6) fire damage."
        ],
        "Actions": [
            "Multiattack. The snake makes two attacks: one with its bite and one with its tail.",
            "Bite.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 3 (1d4 + 1) piercing damage plus 3 (1d6) fire damage.",
            "Tail.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 3 (1d4 + 1) bludgeoning damage plus 3 (1d6) fire damage."
        ]
    },
    "flameskull": {
        "name": "Flameskull",
        "type": "Tiny undead",
        "alignment": "neutral evil",
        "Armor Class": "13",
        "Hit Points": "40 (9d4 + 18)",
        "Speed": "0 ft., fly 40 ft. (hover)",
        "Skills": "Arcana +5, Perception +2",
        "Damage Resistances": "lightning, necrotic, piercing",
        "Damage Immunities": "cold, fire, poison",
        "Condition Immunities": "charmed, frightened, paralyzed, poisoned, prone",
        "Senses": "darkvision 60 ft., passive Perception 12",
        "Languages": "Common",
        "Challenge": "4 (1100 XP)",
        "STR": "1 (-5)",
        "DEX": "17 (+3)",
        "CON": "14 (+2)",
        "INT": "16 (+3)",
        "WIS": "10 (+0)",
        "CHA": "11 (+0)",
        "features": [
            "Illumination. The flameskull sheds either dim light in a 15-foot radius, or bright light in a 15-foot radius and dim light for an additional 15 feet. It can switch between the options as an action.",
            "Magic Resistance. The flameskull has advantage on saving throws against spells and other magical effects.",
            "Rejuvenation. If the flameskull is destroyed, it regains all its hit points in 1 hour unless holy water is sprinkled on its remains or adispel magicorremove cursespell is cast on them.",
            "Spellcasting. The flameskull is a 5th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 13, +5 to hit with spell attacks). It requires no somatic or material components to cast its spells. The flameskull has the following wizard spells prepared:"
        ],
        "Actions": [
            "Multiattack. The flameskull uses Fire Ray twice.",
            "Fire Ray.Ranged Spell Attack: +5 to hit, range 30 ft., one target.Hit: 10 (3d6) fire damage."
        ]
    },
    "flesh-golem": {
        "name": "Flesh Golem",
        "type": "Medium construct",
        "alignment": "neutral",
        "Armor Class": "9",
        "Hit Points": "93 (11d8 + 44)",
        "Speed": "30 ft.",
        "Damage Immunities": "lightning, poison; bludgeoning, piercing, and slashing from nonmagical attacks that aren't adamantine",
        "Condition Immunities": "charmed, exhaustion, frightened, paralyzed, petrified, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "understands the languages of its creator but can't speak",
        "Challenge": "5 (1800 XP)",
        "STR": "19 (+4)",
        "DEX": "9 (-1)",
        "CON": "18 (+4)",
        "INT": "6 (-2)",
        "WIS": "10 (+0)",
        "CHA": "5 (-3)",
        "features": [
            "Berserk. Whenever the golem starts its turn with 40 hit points or fewer, roll a d6. On a 6, the golem goes berserk. On each of its turns while berserk, the golem attacks the nearest creature it can see. If no creature is near enough to move to and attack, the golem attacks an object, with preference for an object smaller than itself. Once the golem goes berserk, it continues to do so until it is destroyed or regains all its hit points. The golem's creator, if within 60 feet of the berserk golem, can try to calm it by speaking firmly and persuasively. The golem must be able to hear its creator, who must take an action to make a DC 15 Charisma (Persuasion) check. If the check succeeds, the golem ceases being berserk. If it takes damage while still at 40 hit points or fewer, the golem might go berserk again.",
            "Aversion of Fire. If the golem takes fire damage, it has disadvantage on attack rolls and ability checks until the end of its next turn.",
            "Immutable Form. The golem is immune to any spell or effect that would alter its form.",
            "Lightning Absorption. Whenever the golem is subjected to lightning damage, it takes no damage and instead regains a number of hit points equal to the lightning damage dealt.",
            "Magic Resistance. The golem has advantage on saving throws against spells and other magical effects.",
            "Magic Weapons. The golem's weapon attacks are magical."
        ],
        "Actions": [
            "Multiattack. The golem makes two slam attacks.",
            "Slam.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 13 (2d8 + 4) bludgeoning damage."
        ]
    },
    "flumph": {
        "name": "Flumph",
        "type": "Small aberration",
        "alignment": "lawful good",
        "Armor Class": "12",
        "Hit Points": "7 (2d6)",
        "Speed": "5 ft., fly 30 ft.",
        "Skills": "Arcana +4, History +4, Religion +4",
        "Damage Vulnerabilities": "psychic",
        "Senses": "darkvision 60 ft., passive Perception 12",
        "Languages": "understands Undercommon but can't speak, telepathy 60 ft.",
        "Challenge": "1/8 (25 XP)",
        "STR": "6 (-2)",
        "DEX": "15 (+2)",
        "CON": "10 (+0)",
        "INT": "14 (+2)",
        "WIS": "14 (+2)",
        "CHA": "11 (+0)",
        "features": [
            "Advanced Telepathy. The flumph can perceive the content of any telepathic communication used within 60 feet of it, and it can't be surprised by creatures with any form of telepathy.",
            "Prone Deficiency. If the flumph is knocked prone, roll a die. On an odd result, the flumph lands upside-down and is in capacitated. At the end of each of its turns, the flumph can make a DC 10 Dexterity saving throw, righting itself and ending the incapacitated condition if it succeeds.",
            "Telepathic Shroud. The flumph is immune to any effect that would sense its emotions or read its thoughts, as well as all divination spells."
        ],
        "Actions": [
            "Tendrils.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 4 (1d4 + 2) piercing damage plus 2 (1d4) acid damage. At the end of each of its turns, the target must make a DC 10 Constitution saving throw, taking 2 (1d4) acid damage on a failure or ending the recurring acid damage on a success. A lesser restoration spell cast on the target also ends the recurring acid damage.",
            "Stench Spray (1/Day). Each creature in a 15-foot cone originating from the flumph must succeed on a DC 10 Dexterity saving throw or be coated in a foul-smelling liquid. A coated creature exudes a horrible stench for 1d4 hours. The coated creature is poisoned as long as the stench lasts, and other creatures are poisoned while within 5 feet of the coated creature. A creature can remove the stench on itself by using a short rest to bathe in water, alcohol, or vinegar."
        ]
    },
    "flying-snake": {
        "name": "Flying Snake",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "14",
        "Hit Points": "5 (2d4)",
        "Speed": "30 ft., fly 60 ft., swim 30 ft.",
        "Senses": "blindsight 10 ft., passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "1/8 (25 XP)",
        "STR": "4 (-3)",
        "DEX": "18 (+4)",
        "CON": "11 (+0)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "5 (-3)",
        "features": [
            "Flyby. The snake doesn't provoke opportunity attacks when it flies out of an enemy's reach."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 1 piercing damage plus 7 (3d4) poison damage."
        ]
    },
    "flying-sword": {
        "name": "Flying Sword",
        "type": "Small construct",
        "alignment": "unaligned",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "17 (5d6)",
        "Speed": "0 ft., fly 50 ft. (hover)",
        "Saving Throws": "Dex +4",
        "Damage Immunities": "poison, psychic",
        "Condition Immunities": "blinded, charmed, deafened, frightened, paralyzed, petrified, poisoned",
        "Senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 7",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "12 (+1)",
        "DEX": "15 (+2)",
        "CON": "11 (+0)",
        "INT": "1 (-5)",
        "WIS": "5 (-3)",
        "CHA": "1 (-5)",
        "features": [
            "Antimagic Susceptibility. The sword is incapacitated while in the area of anantimagic field. If targeted bydispel magic, the sword must succeed on a Constitution saving throw against the caster's spell save DC or fall unconscious for 1 minute.",
            "False Appearance. While the sword remains motionless and isn't flying, it is indistinguishable from a normal sword."
        ],
        "Actions": [
            "Longsword.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 5 (1d8 + 1) slashing damage."
        ]
    },
    "fomorian": {
        "name": "Fomorian",
        "type": "Huge giant",
        "alignment": "chaotic evil",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "149 (13d12 + 65)",
        "Speed": "30 ft.",
        "Skills": "Perception +8, Stealth +3",
        "Senses": "darkvision 120 ft., passive Perception 18",
        "Languages": "Giant, Undercommon",
        "Challenge": "8 (3900 XP)",
        "STR": "23 (+6)",
        "DEX": "10 (+0)",
        "CON": "20 (+5)",
        "INT": "9 (-1)",
        "WIS": "14 (+2)",
        "CHA": "6 (-2)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "frog": {
        "features": [
            "Amphibious. The frog can breathe air and water.",
            "Standing Leap. The frog's long jump is up to 10 feet and its high jump is up to 5 feet, with or without a running start."
        ],
        "name": "Frog",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "11",
        "Hit Points": "1 (1d4 - 1)",
        "Speed": "20 ft., swim 20 ft.",
        "Skills": "Perception +1, Stealth +3",
        "Senses": "darkvision 30 ft., passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "0 (0 XP)",
        "STR": "1 (-5)",
        "DEX": "13 (+1)",
        "CON": "8 (-1)",
        "INT": "1 (-5)",
        "WIS": "8 (-1)",
        "CHA": "3 (-4)"
    },
    "frost-giant": {
        "name": "Frost Giant",
        "type": "Huge giant",
        "alignment": "neutral evil",
        "Armor Class": "15 (patchwork armor)",
        "Hit Points": "138 (12d12 + 60)",
        "Speed": "40 ft.",
        "Saving Throws": "Con +8, Wis +3, Cha +4",
        "Skills": "Athletics +9, Perception +3",
        "Damage Immunities": "cold",
        "Senses": "passive Perception 13",
        "Languages": "Giant",
        "Challenge": "8 (3900 XP)",
        "STR": "23 (+6)",
        "DEX": "9 (-1)",
        "CON": "21 (+5)",
        "INT": "9 (-1)",
        "WIS": "10 (+0)",
        "CHA": "12 (+1)",
        "features": [],
        "Actions": [
            "Multiattack. The giant makes two greataxe attacks.",
            "Greataxe.Melee Weapon Attack: +9 to hit, reach 10 ft., one target.Hit: 25 (3d12 + 6) slashing damage.",
            "Rock.Ranged Weapon Attack: +9 to hit, range 60/240 ft., one target.Hit: 28 (4d10 + 6) bludgeoning damage."
        ]
    },
    "galeb-duhr": {
        "name": "Galeb Duhr",
        "type": "Medium elemental",
        "alignment": "neutral",
        "Armor Class": "16 (natural armor)",
        "Hit Points": "85 (9d8 + 45)",
        "Speed": "15 ft. (30 ft. when rolling, 60 ft. rolling downhill)",
        "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "poison",
        "Condition Immunities": "exhaustion, paralyzed, poisoned, petrified",
        "Senses": "darkvision 60 ft., tremorsense 60 ft., passive Perception 11",
        "Languages": "Terran",
        "Challenge": "6 (2300 XP)",
        "STR": "20 (+5)",
        "DEX": "14 (+2)",
        "CON": "20 (+5)",
        "INT": "11 (+0)",
        "WIS": "12 (+1)",
        "CHA": "11 (+0)",
        "features": [
            "False Appearance. While the galeb duhr remains motionless, it is indistinguishable from a normal boulder.",
            "Rolling Charge. If the galeb duhr rolls at least 20 feet straight toward a target and then hits it with a slam attack on the same turn, the target takes an extra 7 (2d6) bludgeoning damage. If the target is a creature, it must succeed on a DC 16 Strength saving throw or be knocked prone."
        ],
        "Actions": [
            "Slam.Melee Weapon Attack: +8 to hit, reach 5 ft., one target.Hit: 12 (2d6 + 5) bludgeoning damage.",
            "Animate Boulders (1/Day). The galeb duhr magically animates up to two boulders it can see within 60 feet of it. A boulder has statistics like those of a galeb duhr, except it has Intelligence 1 and Charisma 1, it can't be charmed or frightened, and it lacks this action option. A boulder remains animated as long as the galeb duhr maintains concentration, up to 1 minute (as if concentrating on a spell)."
        ]
    },
    "gargoyle": {
        "name": "Gargoyle",
        "type": "Medium elemental",
        "alignment": "chaotic evil",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "52 (7d8 + 21)",
        "Speed": "30 ft., fly 60 ft.",
        "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks that aren't adamantine",
        "Damage Immunities": "poison",
        "Condition Immunities": "exhaustion, petrified, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Terran",
        "Challenge": "2 (450 XP)",
        "STR": "15 (+2)",
        "DEX": "11 (+0)",
        "CON": "16 (+3)",
        "INT": "6 (-2)",
        "WIS": "11 (+0)",
        "CHA": "7 (-2)",
        "features": [
            "False Appearance. While the gargoyle remains motionless, it is indistinguishable from an inanimate statue."
        ],
        "Actions": [
            "Multiattack. The gargoyle makes two attacks: one with its bite and one with its claws.",
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) piercing damage.",
            "Claws.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) slashing damage."
        ]
    },
    "gas-spore": {
        "name": "Gas Spore",
        "type": "Large plant",
        "alignment": "unaligned",
        "Armor Class": "5",
        "Hit Points": "1 (1d10 - 4)",
        "Speed": "0 ft., fly 10 ft. (hover)",
        "Damage Immunities": "poison",
        "Condition Immunities": "blinded, deafened, frightened, paralyzed, poisoned, prone",
        "Senses": "blindsight 30 ft. (blind beyond this radius), passive Perception 5",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "5 (-3)",
        "DEX": "1 (-5)",
        "CON": "3 (-4)",
        "INT": "1 (-5)",
        "WIS": "1 (-5)",
        "CHA": "1 (-5)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "gelatinous-cube": {
        "name": "Gelatinous Cube",
        "type": "Large ooze",
        "alignment": "unaligned",
        "Armor Class": "6",
        "Hit Points": "84 (8d10 + 40)",
        "Speed": "15 ft.",
        "Condition Immunities": "blinded, charmed, deafened, exhaustion, frightened, prone",
        "Senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 8",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "14 (+2)",
        "DEX": "3 (-4)",
        "CON": "20 (+5)",
        "INT": "1 (-5)",
        "WIS": "6 (-2)",
        "CHA": "1 (-5)",
        "features": [
            "Ooze Cube. The cube takes up its entire space. Other creatures can enter the space, but a creature that does so is subjected to the cube's Engulf and has disadvantage on the saving throw. Creatures inside the cube can be seen but have total cover. A creature within 5 feet of the cube can take an action to pull a creature or object out of the cube. Doing so requires a successful DC 12 Strength check, and the creature making the attempt takes 10 (3d6) acid damage. The cube can hold only one Large creature or up to four Medium or smaller creatures inside it at a time.",
            "Transparent. Even when the cube is in plain sight, it takes a successful DC 15 Wisdom (Perception) check to spot a cube that has neither moved nor attacked. A creature that tries to enter the cube's space while unaware of the cube is surprised by the cube."
        ],
        "Actions": [
            "Pseudopod.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 10 (3d6) acid damage.",
            "Engulf. The cube moves up to its speed. While doing so, it can enter Large or smaller creatures' spaces. Whenever the cube enters a creature's space, the creature must make a DC 12 Dexterity saving throw. On a successful save, the creature can choose to be pushed 5 feet back or to the side of the cube. A creature that chooses not to be pushed suffers the consequences of a failed saving throw. On a failed save, the cube enters the creature's space, and the creature takes 10 (3d6) acid damage and is engulfed. The engulfed creature can't breathe, is restrained, and takes 21 (6d6) acid damage at the start of each of the cube's turns. When the cube moves, the engulfed creature moves with it. An engulfed creature can try to escape by taking an action to make a DC 12 Strength check. On a success, the creature escapes and enters a space of its choice within 5 feet of the cube."
        ]
    },
    "ghast": {
        "name": "Ghast",
        "type": "Medium undead",
        "alignment": "chaotic evil",
        "Armor Class": "13",
        "Hit Points": "36 (8d8)",
        "Speed": "30 ft.",
        "Damage Resistances": "necrotic",
        "Damage Immunities": "poison",
        "Condition Immunities": "charmed, exhaustion, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Common",
        "Challenge": "2 (450 XP)",
        "STR": "16 (+3)",
        "DEX": "17 (+3)",
        "CON": "10 (+0)",
        "INT": "11 (+0)",
        "WIS": "10 (+0)",
        "CHA": "8 (-1)",
        "features": [
            "Stench. Any creature that starts its turn within 5 feet of the ghast must succeed on a DC 10 Constitution saving throw or be poisoned until the start of its next turn. On a successful saving throw, the creature is immune to the ghast's Stench for 24 hours.",
            "Turning Defiance. The ghast and any ghouls within 30 feet of it have advantage on saving throws against effects that turn undead."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +3 to hit, reach 5 ft., one creature.Hit: 12 (2d8 + 3) piercing damage.",
            "Claws.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) slashing damage. If the target is a creature other than an undead, it must succeed on a DC 10 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        ]
    },
    "ghost": {
        "name": "Ghost",
        "type": "Medium undead",
        "alignment": "any alignment",
        "Armor Class": "11",
        "Hit Points": "45 (10d8)",
        "Speed": "0 ft., fly 40 ft. (hover)",
        "Damage Resistances": "acid, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "cold, necrotic, poison",
        "Condition Immunities": "charmed, exhaustion, frightened, grappled, paralyzed, petrified, poisoned, prone, restrained",
        "Senses": "darkvision 60 ft., passive Perception 11",
        "Languages": "the languages it knew in life",
        "Challenge": "4 (1100 XP)",
        "STR": "7 (-2)",
        "DEX": "13 (+1)",
        "CON": "10 (+0)",
        "INT": "10 (+0)",
        "WIS": "12 (+1)",
        "CHA": "17 (+3)",
        "features": [
            "Ethereal Sight. The ghost can see 60 feet into the Ethereal Plane when it is on the Material Plane, and vice versa.",
            "Incorporeal Movement. The ghost can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object."
        ],
        "Actions": [
            "Withering Touch.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 17 (4d6 + 3) necrotic damage.",
            "Etherealness. The ghost enters the Ethereal Plane from the Material Plane, or vice versa. It is visible on the Material Plane while it is in the Border Ethereal, and vice versa, yet it can't affect or be affected by anything on the other plane.",
            "Horrifying Visage. Each non-undead creature within 60 feet of the ghost that can see it must succeed on a DC 13 Wisdom saving throw or be frightened for 1 minute. If the save fails by 5 or more, the target also ages 1d4 x 10 years. A frightened target can repeat the saving throw at the end of each of its turns, ending the frightened condition on itself on a success. If a target's saving throw is successful or the effect ends for it, the target is immune to this ghost's Horrifying Visage for the next 24 hours. The aging effect can be reversed with agreater restorationspell, but only within 24 hours of it occurring.",
            "Possession (Recharge 6). One humanoid that the ghost can see within 5 feet of it must succeed on a DC 13 Charisma saving throw or be possessed by the ghost; the ghost then disappears, and the target is incapacitated and loses control of its body. The ghost now controls the body but doesn't deprive the target of awareness. The ghost can't be targeted by any attack, spell, or other effect, except ones that turn undead, and it retains its alignment, Intelligence, Wisdom, Charisma, and immunity to being charmed and frightened. It otherwise uses the possessed target's statistics, but doesn't gain access to the target's knowledge, class features, or proficiencies. The possession lasts until the body drops to 0 hit points, the ghost ends it as a bonus action, or the ghost is turned or forced out by an effect like thedispel evil and goodspell. When the possession ends, the ghost reappears in an unoccupied space within 5 feet of the body. The target is immune to this ghost's Possession for 24 hours after succeeding on the saving throw or after the possession ends."
        ]
    },
    "ghoul": {
        "name": "Ghoul",
        "type": "Medium undead",
        "alignment": "chaotic evil",
        "Armor Class": "12",
        "Hit Points": "22 (5d8)",
        "Speed": "30 ft.",
        "Damage Immunities": "poison",
        "Condition Immunities": "charmed, exhaustion, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Common",
        "Challenge": "1 (200 XP)",
        "STR": "13 (+1)",
        "DEX": "15 (+2)",
        "CON": "10 (+0)",
        "INT": "7 (-2)",
        "WIS": "10 (+0)",
        "CHA": "6 (-2)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +2 to hit, reach 5 ft., one creature.Hit: 9 (2d6 + 2) piercing damage.",
            "Claws.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 7 (2d4 + 2) slashing damage. If the target is a creature other than an elf or undead, it must succeed on a DC 10 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        ]
    },
    "giant-ape": {
        "name": "Giant Ape",
        "type": "Huge beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "157 (15d12 + 60)",
        "Speed": "40 ft., climb 40 ft.",
        "Skills": "Athletics +9, Perception +4",
        "Senses": "passive Perception 14",
        "Languages": "\u2014",
        "Challenge": "7 (2900 XP)",
        "STR": "23 (+6)",
        "DEX": "14 (+2)",
        "CON": "18 (+4)",
        "INT": "7 (-2)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [],
        "Actions": [
            "Multiattack. The ape makes two fist attacks.",
            "Fist.Melee Weapon Attack: +9 to hit, reach 10 ft., one target.Hit: 22 (3d10 + 6) bludgeoning damage.",
            "Rock.Ranged Weapon Attack: +9 to hit, range 50/100 ft., one target.Hit: 30 (7d6 + 6) bludgeoning damage."
        ]
    },
    "giant-badger": {
        "name": "Giant Badger",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "10",
        "Hit Points": "13 (2d8 + 4)",
        "Speed": "30 ft., burrow 10 ft.",
        "Senses": "darkvision 30 ft., passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "13 (+1)",
        "DEX": "10 (+0)",
        "CON": "15 (+2)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "5 (-3)",
        "features": [
            "Keen Smell. The badger has advantage on Wisdom (Perception) checks that rely on smell."
        ],
        "Actions": [
            "Multiattack. The badger makes two attacks: one with its bite and one with its claws.",
            "Bite.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 4 (1d6 + 1) piercing damage.",
            "Claws.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 6 (2d4 + 1) slashing damage."
        ]
    },
    "giant-bat": {
        "name": "Giant Bat",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "13",
        "Hit Points": "22 (4d10)",
        "Speed": "10 ft., fly 60 ft.",
        "Senses": "blindsight 60 ft., passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "15 (+2)",
        "DEX": "16 (+3)",
        "CON": "11 (+0)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "6 (-2)",
        "features": [
            "Echolocation. The bat can't use its blindsight while deafened.",
            "Keen Hearing. The bat has advantage on Wisdom (Perception) checks that rely on hearing."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 5 (1d6 + 2) piercing damage."
        ]
    },
    "giant-boar": {
        "name": "Giant Boar",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "42 (5d10 + 15)",
        "Speed": "40 ft.",
        "Senses": "passive Perception 8",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "17 (+3)",
        "DEX": "10 (+0)",
        "CON": "16 (+3)",
        "INT": "2 (-4)",
        "WIS": "7 (-2)",
        "CHA": "5 (-3)",
        "features": [
            "Charge. If the boar moves at least 20 feet straight toward a target and then hits it with a tusk attack on the same turn, the target takes an extra 7 (2d6) slashing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone.",
            "Relentless (Recharges after a Short or Long Rest). If the boar takes 10 damage or less that would reduce it to 0 hit points, it is reduced to 1 hit point instead."
        ],
        "Actions": [
            "Tusk.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) slashing damage."
        ]
    },
    "giant-centipede": {
        "name": "Giant Centipede",
        "type": "Small beast",
        "alignment": "unaligned",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "4 (1d6 + 1)",
        "Speed": "30 ft., climb 30 ft.",
        "Senses": "blindsight 30 ft., passive Perception 8",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "5 (-3)",
        "DEX": "14 (+2)",
        "CON": "12 (+1)",
        "INT": "1 (-5)",
        "WIS": "7 (-2)",
        "CHA": "3 (-4)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 4 (1d4 + 2) piercing damage, and the target must succeed on a DC 11 Constitution saving throw or take 10 (3d6) poison damage. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way."
        ]
    },
    "giant-constrictor-snake": {
        "name": "Giant Constrictor Snake",
        "type": "Huge beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "60 (8d12 + 8)",
        "Speed": "30 ft., swim 30 ft.",
        "Skills": "Perception +2",
        "Senses": "blindsight 10 ft., passive Perception 12",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "19 (+4)",
        "DEX": "14 (+2)",
        "CON": "12 (+1)",
        "INT": "1 (-5)",
        "WIS": "10 (+0)",
        "CHA": "3 (-4)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +6 to hit, reach 10 ft., one creature.Hit: 11 (2d6 + 4) piercing damage.",
            "Constrict.Melee Weapon Attack: +6 to hit, reach 5 ft., one creature.Hit: 13 (2d8 + 4) bludgeoning damage, and the target is grappled (escape DC 16). Until this grapple ends, the creature is restrained, and the snake can't constrict another target."
        ]
    },
    "giant-crab": {
        "name": "Giant Crab",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "13 (3d8)",
        "Speed": "30 ft., swim 30 ft.",
        "Skills": "Stealth +4",
        "Senses": "blindsight 30 ft., passive Perception 9",
        "Languages": "\u2014",
        "Challenge": "1/8 (25 XP)",
        "STR": "13 (+1)",
        "DEX": "15 (+2)",
        "CON": "11 (+0)",
        "INT": "1 (-5)",
        "WIS": "9 (-1)",
        "CHA": "3 (-4)",
        "features": [
            "Amphibious. The crab can breathe air and water."
        ],
        "Actions": [
            "Claw.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 4 (1d6 + 1) bludgeoning damage, and the target is grappled (escape DC 11). The crab has two claws, each of which can grapple only one target."
        ]
    },
    "giant-crocodile": {
        "name": "Giant Crocodile",
        "type": "Huge beast",
        "alignment": "unaligned",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "85 (9d12 + 27)",
        "Speed": "30 ft., swim 50 ft.",
        "Skills": "Stealth +5",
        "Senses": "passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "5 (1800 XP)",
        "STR": "21 (+5)",
        "DEX": "9 (-1)",
        "CON": "17 (+3)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "7 (-2)",
        "features": [
            "Hold Breath. The crocodile can hold its breath for 30 minutes."
        ],
        "Actions": [
            "Multiattack. The crocodile makes two attacks: one with its bite and one with its tail.",
            "Bite.Melee Weapon Attack: +8 to hit, reach 5 ft., one target.Hit: 21 (3d10 + 5) piercing damage, and the target is grappled (escape DC 16). Until this grapple ends, the target is restrained, and the crocodile can't bite another target.",
            "Tail.Melee Weapon Attack: +8 to hit, reach 10 ft., one target not grappled by the crocodile.Hit: 14 (2d8 + 5) bludgeoning damage. If the target is a creature, it must succeed on a DC 16 Strength saving throw or be knocked prone."
        ]
    },
    "giant-eagle": {
        "name": "Giant Eagle",
        "type": "Large beast",
        "alignment": "neutral good",
        "Armor Class": "13",
        "Hit Points": "26 (4d10 + 4)",
        "Speed": "10 ft., fly 80 ft.",
        "Skills": "Perception +4",
        "Senses": "passive Perception 14",
        "Languages": "Giant Eagle understands Common and Auran but can't speak them",
        "Challenge": "1 (200 XP)",
        "STR": "16 (+3)",
        "DEX": "17 (+3)",
        "CON": "13 (+1)",
        "INT": "8 (-1)",
        "WIS": "14 (+2)",
        "CHA": "10 (+0)",
        "features": [
            "Keen Sight. The eagle has advantage on Wisdom (Perception) checks that rely on sight."
        ],
        "Actions": [
            "Multiattack. The eagle makes two attacks: one with its beak and one with its talons.",
            "Beak.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 6 (1d6 + 3) piercing damage.",
            "Talons.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) slashing damage."
        ]
    },
    "giant-elk": {
        "name": "Giant Elk",
        "type": "Huge beast",
        "alignment": "unaligned",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "42 (5d12 + 10)",
        "Speed": "60 ft.",
        "Skills": "Perception +4",
        "Senses": "passive Perception 14",
        "Languages": "Giant Elk understands Common, Elvish, and Sylvan but can't speak them",
        "Challenge": "2 (450 XP)",
        "STR": "19 (+4)",
        "DEX": "16 (+3)",
        "CON": "14 (+2)",
        "INT": "7 (-2)",
        "WIS": "14 (+2)",
        "CHA": "10 (+0)",
        "features": [
            "Charge. If the elk moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or be knocked prone."
        ],
        "Actions": [
            "Ram.Melee Weapon Attack: +6 to hit, reach 10 ft., one target.Hit: 11 (2d6 + 4) bludgeoning damage.",
            "Hooves.Melee Weapon Attack: +6 to hit, reach 5 ft., one prone creature.Hit: 22 (4d8 + 4) bludgeoning damage."
        ]
    },
    "giant-fire-beetle": {
        "name": "Giant Fire Beetle",
        "type": "Small beast",
        "alignment": "unaligned",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "4 (1d6 + 1)",
        "Speed": "30 ft.",
        "Senses": "blindsight 30 ft., passive Perception 8",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "8 (-1)",
        "DEX": "10 (+0)",
        "CON": "12 (+1)",
        "INT": "1 (-5)",
        "WIS": "7 (-2)",
        "CHA": "3 (-4)",
        "features": [
            "Illumination. The beetle sheds bright light in a 10-foot radius and dim light for an additional 10 feet."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +1 to hit, reach 5 ft., one target.Hit: 2 (1d6 - 1) slashing damage."
        ]
    },
    "giant-frog": {
        "name": "Giant Frog",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "11",
        "Hit Points": "18 (4d8)",
        "Speed": "30 ft., swim 30 ft.",
        "Skills": "Perception +2, Stealth +3",
        "Senses": "darkvision 30 ft., passive Perception 12",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "12 (+1)",
        "DEX": "13 (+1)",
        "CON": "11 (+0)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "3 (-4)",
        "features": [
            "Amphibious. The frog can breathe air and water.",
            "Standing Leap. The frog's long jump is up to 20 feet and its high jump is up to 10 feet, with or without a running start."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 4 (1d6 + 1) piercing damage, and the target is grappled (escape DC 11). Until this grapple ends, the target is restrained, and the frog can't bite another target.",
            "Swallow. The frog makes one bite attack against a Small or smaller target it is grappling. If the attack hits, the target is swallowed, and the grapple ends. The swallowed target is blinded and restrained, it has total cover against attacks and other effects outside the frog, and it takes 5 (2d4) acid damage at the start of each of the frog's turns. The frog can have only one target swallowed at a time. If the frog dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 5 feet of movement, exiting prone."
        ]
    },
    "giant-goat": {
        "name": "Giant Goat",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "11 (natural armor)",
        "Hit Points": "19 (3d10 + 3)",
        "Speed": "40 ft.",
        "Senses": "passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "17 (+3)",
        "DEX": "11 (+0)",
        "CON": "12 (+1)",
        "INT": "3 (-4)",
        "WIS": "12 (+1)",
        "CHA": "6 (-2)",
        "features": [
            "Charge. If the goat moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 5 (2d4) bludgeoning damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone.",
            "Sure-Footed. The goat has advantage on Strength and Dexterity saving throws made against effects that would knock it prone."
        ],
        "Actions": [
            "Ram.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 8 (2d4 + 3) bludgeoning damage."
        ]
    },
    "giant-hyena": {
        "name": "Giant Hyena",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "45 (6d10 + 12)",
        "Speed": "50 ft.",
        "Skills": "Perception +3",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "1 (200 XP)",
        "STR": "16 (+3)",
        "DEX": "14 (+2)",
        "CON": "14 (+2)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Rampage. When the hyena reduces a creature to 0 hit points with a melee attack on its turn, the hyena can take a bonus action to move up to half its speed and make a bite attack."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) piercing damage."
        ]
    },
    "giant-lizard": {
        "name": "Giant Lizard",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "19 (3d10 + 3)",
        "Speed": "30 ft., climb 30 ft.",
        "Senses": "darkvision 30 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "15 (+2)",
        "DEX": "12 (+1)",
        "CON": "13 (+1)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "5 (-3)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 6 (1d8 + 2) piercing damage."
        ]
    },
    "giant-octopus": {
        "name": "Giant Octopus",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "11",
        "Hit Points": "52 (8d10 + 8)",
        "Speed": "10 ft., swim 60 ft.",
        "Skills": "Perception +4, Stealth +5",
        "Senses": "darkvision 60 ft., passive Perception 14",
        "Languages": "\u2014",
        "Challenge": "1 (200 XP)",
        "STR": "17 (+3)",
        "DEX": "13 (+1)",
        "CON": "13 (+1)",
        "INT": "4 (-3)",
        "WIS": "10 (+0)",
        "CHA": "4 (-3)",
        "features": [
            "Hold Breath. While out of water, the octopus can hold its breath for 1 hour.",
            "Underwater Camouflage. The octopus has advantage on Dexterity (Stealth) checks made while underwater.",
            "Water Breathing. The octopus can breathe only underwater."
        ],
        "Actions": [
            "Tentacles.Melee Weapon Attack: +5 to hit, reach 15 ft., one target.Hit: 10 (2d6 + 3) bludgeoning damage. If the target is a creature, it is grappled (escape DC 16). Until this grapple ends, the target is restrained, and the octopus can't use its tentacles on another target.",
            "Ink Cloud (Recharges after a Short or Long Rest). A 20-foot-radius cloud of ink extends all around the octopus if it is underwater. The area is heavily obscured for 1 minute, although a significant current can disperse the ink. After releasing the ink, the octopus can use the Dash action as a bonus action."
        ]
    },
    "giant-owl": {
        "name": "Giant Owl",
        "type": "Large beast",
        "alignment": "neutral",
        "Armor Class": "12",
        "Hit Points": "19 (3d10 + 3)",
        "Speed": "5 ft., fly 60 ft.",
        "Skills": "Perception +5, Stealth +4",
        "Senses": "darkvision 120 ft., passive Perception 15",
        "Languages": "Giant Owl understands Common, Elvish, and Sylvan but can't speak them",
        "Challenge": "1/4 (50 XP)",
        "STR": "13 (+1)",
        "DEX": "15 (+2)",
        "CON": "12 (+1)",
        "INT": "8 (-1)",
        "WIS": "13 (+1)",
        "CHA": "10 (+0)",
        "features": [
            "Flyby. The owl doesn't provoke opportunity attacks when it flies out of an enemy's reach.",
            "Keen Hearing and Sight. The owl has advantage on Wisdom (Perception) checks that rely on hearing or sight."
        ],
        "Actions": [
            "Talons.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 8 (2d6 + 1) slashing damage."
        ]
    },
    "giant-poisonous-snake": {
        "name": "Giant Poisonous Snake",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "14",
        "Hit Points": "11 (2d8 + 2)",
        "Speed": "30 ft., swim 30 ft.",
        "Skills": "Perception +2",
        "Senses": "blindsight 10 ft., passive Perception 12",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "10 (+0)",
        "DEX": "18 (+4)",
        "CON": "13 (+1)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "3 (-4)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +6 to hit, reach 10 ft., one target.Hit: 6 (1d4 + 4) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "giant-rat": {
        "name": "Giant Rat",
        "type": "Small beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "7 (2d6)",
        "Speed": "30 ft.",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/8 (25 XP)",
        "STR": "7 (-2)",
        "DEX": "15 (+2)",
        "CON": "11 (+0)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "4 (-3)",
        "features": [
            "Keen Smell. The rat has advantage on Wisdom (Perception) checks that rely on smell.",
            "Pack Tactics. The rat has advantage on an attack roll against a creature if at least one of the rat's allies is within 5 feet of the creature and the ally isn't incapacitated."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 4 (1d4 + 2) piercing damage."
        ]
    },
    "giant-scorpion": {
        "name": "Giant Scorpion",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "52 (7d10 + 14)",
        "Speed": "40 ft.",
        "Senses": "blindsight 60 ft., passive Perception 9",
        "Languages": "\u2014",
        "Challenge": "3 (700 XP)",
        "STR": "15 (+2)",
        "DEX": "13 (+1)",
        "CON": "15 (+2)",
        "INT": "1 (-5)",
        "WIS": "9 (-1)",
        "CHA": "3 (-4)",
        "features": [],
        "Actions": [
            "Multiattack. The scorpion makes three attacks: two with its claws and one with its sting.",
            "Claw.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 6 (1d8 + 2) bludgeoning damage, and the target is grappled (escape DC 12). The scorpion has two claws, each of which can grapple only one target.",
            "Sting.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 7 (1d10 + 2) piercing damage, and the target must make a DC 12 Constitution saving throw, taking 22 (4d10) poison damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "giant-sea-horse": {
        "name": "Giant Sea Horse",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "16 (3d10)",
        "Speed": "0 ft., swim 40 ft.",
        "Senses": "passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "12 (+1)",
        "DEX": "15 (+2)",
        "CON": "11 (+0)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "5 (-3)",
        "features": [
            "Charge. If the sea horse moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 7 (2d6) bludgeoning damage. If the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone.",
            "Water Breathing. The sea horse can breathe only underwater."
        ],
        "Actions": [
            "Ram.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 4 (1d6 + 1) bludgeoning damage."
        ]
    },
    "giant-shark": {
        "name": "Giant Shark",
        "type": "Huge beast",
        "alignment": "unaligned",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "126 (11d12 + 55)",
        "Speed": "0 ft., swim 50 ft.",
        "Skills": "Perception +3",
        "Senses": "blindsight 60 ft., passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "5 (1800 XP)",
        "STR": "23 (+6)",
        "DEX": "11 (+0)",
        "CON": "21 (+5)",
        "INT": "1 (-5)",
        "WIS": "10 (+0)",
        "CHA": "5 (-3)",
        "features": [
            "Blood Frenzy. The shark has advantage on melee attack rolls against any creature that doesn't have all its hit points.",
            "Water Breathing. The shark can breathe only underwater."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +9 to hit, reach 5 ft., one target.Hit: 22 (3d10 + 6) piercing damage."
        ]
    },
    "giant-spider": {
        "name": "Giant Spider",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "26 (4d10 + 4)",
        "Speed": "30 ft., climb 30 ft.",
        "Skills": "Stealth +7",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1 (200 XP)",
        "STR": "14 (+2)",
        "DEX": "16 (+3)",
        "CON": "12 (+1)",
        "INT": "2 (-4)",
        "WIS": "11 (+0)",
        "CHA": "4 (-3)",
        "features": [
            "Spider Climb. The spider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.",
            "Web Sense. While in contact with a web, the spider knows the exact location of any other creature in contact with the same web.",
            "Web Walker. The spider ignores movement restrictions caused by webbing."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one creature.Hit: 7 (1d8 + 3) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 9 (2d8) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way.",
            "Web (Recharge 5-6).Ranged Weapon Attack: +5 to hit, range 30/60 ft., one creature.Hit: The target is restrained by webbing. As an action, the restrained target can make a DC 12 Strength check, bursting the webbing on a success. The webbing can also be attacked and destroyed (AC 10; hp 5; vulnerability to fire damage; immunity to bludgeoning, poison, and psychic damage)."
        ]
    },
    "giant-toad": {
        "name": "Giant Toad",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "11",
        "Hit Points": "39 (6d10 + 6)",
        "Speed": "20 ft., swim 40 ft.",
        "Senses": "darkvision 30 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1 (200 XP)",
        "STR": "15 (+2)",
        "DEX": "13 (+1)",
        "CON": "13 (+1)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "3 (-4)",
        "features": [
            "Amphibious. The toad can breathe air and water.",
            "Standing Leap. The toad's long jump is up to 20 feet and its high jump is up to 10 feet, with or without a running start."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 7 (1d10 + 2) piercing damage plus 5 (1d10) poison damage, and the target is grappled (escape DC 13). Until this grapple ends, the target is restrained, and the toad can't bite another target.",
            "Swallow. The toad makes one bite attack against a Medium or smaller target it is grappling. If the attack hits, the target is swallowed, and the grapple ends. The swallowed target is blinded and restrained, it has total cover against attacks and other effects outside the toad, and it takes 10 (3d6) acid damage at the start of each of the toad's turns. The toad can have only one target swallowed at a time. If the toad dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 5 feet of movement, exiting prone."
        ]
    },
    "giant-vulture": {
        "name": "Giant Vulture",
        "type": "Large beast",
        "alignment": "neutral evil",
        "Armor Class": "10",
        "Hit Points": "22 (3d10 + 6)",
        "Speed": "10 ft., fly 60 ft.",
        "Skills": "Perception +3",
        "Senses": "passive Perception 13",
        "Languages": "understands Common but can't speak",
        "Challenge": "1 (200 XP)",
        "STR": "15 (+2)",
        "DEX": "10 (+0)",
        "CON": "15 (+2)",
        "INT": "6 (-2)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Keen Sight and Smell. The vulture has advantage on Wisdom (Perception) checks that rely on sight or smell.",
            "Pack Tactics. The vulture has advantage on an attack roll against a creature if at least one of the vulture's allies is within 5 feet of the creature and the ally isn't incapacitated."
        ],
        "Actions": [
            "Multiattack. The vulture makes two attacks: one with its beak and one with its talons.",
            "Beak.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 7 (2d4 + 2) piercing damage.",
            "Talons.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 9 (2d6 + 2) slashing damage."
        ]
    },
    "giant-wasp": {
        "name": "Giant Wasp",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "13 (3d8)",
        "Speed": "10 ft., fly 50 ft.",
        "Senses": "passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "10 (+0)",
        "DEX": "14 (+2)",
        "CON": "10 (+0)",
        "INT": "1 (-5)",
        "WIS": "10 (+0)",
        "CHA": "3 (-4)",
        "features": [],
        "Actions": [
            "Sting.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 5 (1d6 + 2) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way."
        ]
    },
    "giant-weasel": {
        "name": "Giant Weasel",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "13",
        "Hit Points": "9 (2d8)",
        "Speed": "40 ft.",
        "Skills": "Perception +3, Stealth +5",
        "Senses": "darkvision 60 ft., passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "1/8 (25 XP)",
        "STR": "11 (+0)",
        "DEX": "16 (+3)",
        "CON": "10 (+0)",
        "INT": "4 (-3)",
        "WIS": "12 (+1)",
        "CHA": "5 (-3)",
        "features": [
            "Keen Hearing and Smell. The weasel has advantage on Wisdom (Perception) checks that rely on hearing or smell."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 5 (1d4 + 3) piercing damage."
        ]
    },
    "giant-wolf-spider": {
        "name": "Giant Wolf Spider",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "13",
        "Hit Points": "11 (2d8 + 2)",
        "Speed": "40 ft., climb 40 ft.",
        "Skills": "Perception +3, Stealth +7",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "12 (+1)",
        "DEX": "16 (+3)",
        "CON": "13 (+1)",
        "INT": "3 (-4)",
        "WIS": "12 (+1)",
        "CHA": "4 (-3)",
        "features": [
            "Spider Climb. The spider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.",
            "Web Sense. While in contact with a web, the spider knows the exact location of any other creature in contact with the same web.",
            "Web Walker. The spider ignores movement restrictions caused by webbing."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +3 to hit, reach 5 ft., one creature.Hit: 4 (1d6 + 1) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 7 (2d6) poison damage on a failed save, or half as much damage on a successful one. If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour, even after regaining hit points, and is paralyzed while poisoned in this way."
        ]
    },
    "gibbering-mouther": {
        "name": "Gibbering Mouther",
        "type": "Medium aberration",
        "alignment": "neutral",
        "Armor Class": "9",
        "Hit Points": "67 (9d8 + 27)",
        "Speed": "10 ft., swim 10 ft.",
        "Condition Immunities": "prone",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "10 (+0)",
        "DEX": "8 (-1)",
        "CON": "16 (+3)",
        "INT": "3 (-4)",
        "WIS": "10 (+0)",
        "CHA": "6 (-2)",
        "features": [
            "Aberrant Ground. The ground in a 10-foot radius around the mouther is doughlike difficult terrain. Each creature that starts its turn in that area must succeed on a DC 10 Strength saving throw or have its",
            "Gibbering. The mouther babbles incoherently while it can see any creature and isn't incapacitated. Each creature that starts its turn within 20 feet of the mouther and can hear the gibbering must succeed on a DC 10 Wisdom saving throw. On a failure, the creature can't take reactions until the start of its next turn and rolls a d8 to determine what it does during its turn. On a 1 to 4, the creature does nothing. On a 5 or 6, the creature takes no action or bonus action and uses all its movement to move in a randomly determined direction. On a 7 or 8, the creature makes a melee attack against a randomly determined creature within its reach or does nothing if it can't make such an attack."
        ],
        "Actions": [
            "Multiattack. The gibbering mouther makes one bite attack and, if it can, uses its Blinding Spittle.",
            "Bites.Melee Weapon Attack: +2 to hit, reach 5 ft., one creature.Hit: 17 (5d6) piercing damage. If the target is Medium or smaller, it must succeed on a DC 10 Strength saving throw or be knocked prone. If the target is killed by this damage, it is absorbed into the mouther.",
            "Blinding Spittle (Recharge 5-6). The mouther spits a chemical glob at a point it can see within 15 feet of it. The glob explodes in a blinding flash of light on impact. Each creature within 5 feet of the flash must succeed on a DC 13 Dexterity saving throw or be blinded until the end of the mouther's next turn."
        ]
    },
    "glabrezu": {
        "name": "Glabrezu",
        "type": "Large fiend (Demon)",
        "alignment": "chaotic evil",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "157 (15d10 + 75)",
        "Speed": "40 ft.",
        "Saving Throws": "Str +9, Con +9, Wis +7, Cha +7",
        "Damage Resistances": "cold, fire, lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "truesight 120 ft., passive Perception 13",
        "Languages": "Abyssal, telepathy 120 ft.",
        "Challenge": "9 (5000 XP)",
        "STR": "20 (+5)",
        "DEX": "15 (+2)",
        "CON": "21 (+5)",
        "INT": "19 (+4)",
        "WIS": "17 (+3)",
        "CHA": "16 (+3)",
        "features": [
            "Innate Spellcasting. The glabrezu's spellcasting ability is Intelligence (spell save DC 16). The glabrezu can innately cast the following spells, requiring no material components:",
            "Magic Resistance. The glabrezu has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack. The glabrezu makes four attacks: two with its pincers and two with its fists. Alternatively, it makes two attacks with its pincers and casts one spell.",
            "Pincer.Melee Weapon Attack: +9 to hit, reach 10 ft., one target.Hit: 16 (2d10 + 5) bludgeoning damage. If the target is a Medium or smaller creature, it is grappled (escape DC 15). The glabrezu has two pincers, each of which can grapple only one target.",
            "Fist.Melee Weapon Attack: +9 to hit, reach 5 ft., one target.Hit: 7 (2d4 + 2) bludgeoning damage."
        ]
    },
    "gladiator": {
        "name": "Gladiator",
        "type": "Medium humanoid (any race)",
        "alignment": "any alignment",
        "Armor Class": "16 (studded leather, shield)",
        "Hit Points": "112 (15d8 + 45)",
        "Speed": "30 ft.",
        "Saving Throws": "Str +7, Dex +5, Con +6",
        "Skills": "Athletics +10, Intimidation +5",
        "Senses": "passive Perception 11",
        "Languages": "any one language (usually Common)",
        "Challenge": "5 (1800 XP)",
        "STR": "18 (+4)",
        "DEX": "15 (+2)",
        "CON": "16 (+3)",
        "INT": "10 (+0)",
        "WIS": "12 (+1)",
        "CHA": "15 (+2)",
        "Reactions": [
            "Parry. The gladiator adds 3 to its AC against one melee attack that would hit it. To do so, the gladiator must see the attacker and be wielding a melee weapon."
        ],
        "features": [
            "Brave. The gladiator has advantage on saving throws against being frightened.",
            "Brute. A melee weapon deals one extra die of its damage when the gladiator hits with it (included in the attack)."
        ],
        "Actions": [
            "Multiattack. The gladiator makes three melee attacks or two ranged attacks.",
            "Spear.Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. and range 20/60 ft., one target.Hit: 11 (2d6 + 4) piercing damage, or 13 (2d8 + 4) piercing damage if used with two hands to make a melee attack.",
            "Shield Bash.Melee Weapon Attack: +7 to hit, reach 5 ft., one creature.Hit: 9 (2d4 + 4) bludgeoning damage. If the target is a Medium or smaller creature, it must succeed on a DC 15 Strength saving throw or be knocked prone."
        ]
    },
    "gnoll": {
        "name": "Gnoll",
        "type": "Medium humanoid (Gnoll)",
        "alignment": "chaotic evil",
        "Armor Class": "15 (hide armor, shield)",
        "Hit Points": "22 (5d8)",
        "Speed": "30 ft.",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Gnoll",
        "Challenge": "1/2 (100 XP)",
        "STR": "14 (+2)",
        "DEX": "12 (+1)",
        "CON": "11 (+0)",
        "INT": "6 (-2)",
        "WIS": "10 (+0)",
        "CHA": "7 (-2)",
        "features": [
            "Rampage. When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 4 (1d4 + 2) piercing damage.",
            "Spear.Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target.Hit: 5 (1d6 + 2) piercing damage, or 6 (1d8 + 2) piercing damage if used with two hands to make a melee attack.",
            "Longbow.Ranged Weapon Attack: +3 to hit, range 150/600 ft., one target.Hit: 5 (1d8 + 1) piercing damage."
        ]
    },
    "gnoll-fang-of-yeenoghu": {
        "name": "Gnoll Fang of Yeenoghu",
        "type": "Medium fiend (Gnoll)",
        "alignment": "chaotic evil",
        "Armor Class": "14 (hide armor)",
        "Hit Points": "65 (10d8 + 20)",
        "Speed": "30 ft.",
        "Saving Throws": "Con +4, Wis +2, Cha +3",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Abyssal, Gnoll",
        "Challenge": "4 (1100 XP)",
        "STR": "17 (+3)",
        "DEX": "15 (+2)",
        "CON": "15 (+2)",
        "INT": "10 (+0)",
        "WIS": "11 (+0)",
        "CHA": "13 (+1)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "gnoll-pack-lord": {
        "name": "Gnoll Pack Lord",
        "type": "Medium humanoid (Gnoll)",
        "alignment": "chaotic evil",
        "Armor Class": "15 (chain shirt)",
        "Hit Points": "49 (9d8 + 9)",
        "Speed": "30 ft.",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Gnoll",
        "Challenge": "2 (450 XP)",
        "STR": "16 (+3)",
        "DEX": "14 (+2)",
        "CON": "13 (+1)",
        "INT": "8 (-1)",
        "WIS": "11 (+0)",
        "CHA": "9 (-1)",
        "features": [
            "Rampage. When the gnoll reduces a creature to 0 hit points with a melee attack on its turn, the gnoll can take a bonus action to move up to half its speed and make a bite attack."
        ],
        "Actions": [
            "Multiattack. The gnoll makes two attacks, either with its glaive or its longbow, and uses its Incite Rampage if it can.",
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one creature.Hit: 5 (1d4 + 3) piercing damage.",
            "Glaive.Melee Weapon Attack: +5 to hit, reach 10 ft., one target.Hit: 8 (1d10 + 3) slashing damage.",
            "Longbow.Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target.Hit: 6 (1d8 + 2) piercing damage.",
            "Incite Rampage (Recharge 5-6). One creature the gnoll can see within 30 feet of it can use its reaction to make a melee attack if it can hear the gnoll and has the Rampage trait."
        ]
    },
    "goat": {
        "name": "Goat",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "10",
        "Hit Points": "4 (1d8)",
        "Speed": "40 ft.",
        "Senses": "passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "12 (+1)",
        "DEX": "10 (+0)",
        "CON": "11 (+0)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "5 (-3)",
        "features": [
            "Charge. If the goat moves at least 20 feet straight toward a target and then hits it with a ram attack on the same turn, the target takes an extra 2 (1d4) bludgeoning damage. If the target is a creature, it must succeed on a DC 10 Strength saving throw or be knocked prone.",
            "Sure-Footed. The goat has advantage on Strength and Dexterity saving throws made against effects that would knock it prone."
        ],
        "Actions": [
            "Ram.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 3 (1d4 + 1) bludgeoning damage."
        ]
    },
    "goblin": {
        "name": "Goblin",
        "type": "Small humanoid (Goblinoid)",
        "alignment": "neutral evil",
        "Armor Class": "15 (leather armor, shield)",
        "Hit Points": "7 (2d6)",
        "Speed": "30 ft.",
        "Skills": "Stealth +6",
        "Senses": "darkvision 60 ft., passive Perception 9",
        "Languages": "Common, Goblin",
        "Challenge": "1/4 (50 XP)",
        "STR": "8 (-1)",
        "DEX": "14 (+2)",
        "CON": "10 (+0)",
        "INT": "10 (+0)",
        "WIS": "8 (-1)",
        "CHA": "8 (-1)",
        "features": [
            "Nimble Escape. The goblin can take the Disengage or Hide action as a bonus action on each of its turns."
        ],
        "Actions": [
            "Scimitar.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) slashing damage.",
            "Shortbow.Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target.Hit: 5 (1d6 + 2) piercing damage."
        ]
    },
    "goblin-boss": {
        "name": "Goblin Boss",
        "type": "Small humanoid (Goblinoid)",
        "alignment": "neutral evil",
        "Armor Class": "17 (chain shirt, shield)",
        "Hit Points": "21 (6d6)",
        "Speed": "30 ft.",
        "Skills": "Stealth +6",
        "Senses": "darkvision 60 ft., passive Perception 9",
        "Languages": "Common, Goblin",
        "Challenge": "1 (200 XP)",
        "STR": "10 (+0)",
        "DEX": "14 (+2)",
        "CON": "10 (+0)",
        "INT": "10 (+0)",
        "WIS": "8 (-1)",
        "CHA": "10 (+0)",
        "Reactions": [
            "Redirect Attack. When a creature the goblin can see targets it with an attack, the goblin chooses another goblin within 5 feet of it. The two goblins swap places, and the chosen goblin becomes the target instead."
        ],
        "features": [
            "Nimble Escape. The goblin can take the Disengage or Hide action as a bonus action on each of its turns."
        ],
        "Actions": [
            "Multiattack. The goblin makes two attacks with its scimitar. The second attack has disadvantage.",
            "Scimitar.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) slashing damage.",
            "Javelin.Melee or Ranged Weapon Attack: +2 to hit, reach 5 ft. or range 30/120 ft., one target.Hit: 3 (1d6) piercing damage."
        ]
    },
    "gold-dragon-wyrmling": {
        "name": "Gold Dragon Wyrmling",
        "type": "Medium dragon (Metallic)",
        "alignment": "lawful good",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "60 (8d8 + 24)",
        "Speed": "30 ft., fly 60 ft., swim 30 ft.",
        "Saving Throws": "Dex +4, Con +5, Wis +2, Cha +5",
        "Skills": "Perception +4, Stealth +4",
        "Damage Immunities": "fire",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 14",
        "Languages": "Draconic",
        "Challenge": "3 (700 XP)",
        "STR": "19 (+4)",
        "DEX": "14 (+2)",
        "CON": "17 (+3)",
        "INT": "14 (+2)",
        "WIS": "11 (+0)",
        "CHA": "16 (+3)",
        "features": [
            "Amphibious. The dragon can breathe air and water."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 9 (1d10 + 4) piercing damage.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.",
            "Fire Breath. The dragon exhales fire in a 15-foot cone. Each creature in that area must make a DC 13 Dexterity saving throw, taking 22 (4d10) fire damage on a failed save, or half as much damage on a successful one.",
            "Weakening Breath. The dragon exhales gas in a 15-foot cone. Each creature in that area must succeed on a DC 13 Strength saving throw or have disadvantage on Strength-based attack rolls, Strength checks, and Strength saving throws for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        ]
    },
    "gorgon": {
        "name": "Gorgon",
        "type": "Large monstrosity",
        "alignment": "unaligned",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "114 (12d10 + 48)",
        "Speed": "40 ft.",
        "Skills": "Perception +4",
        "Condition Immunities": "petrified",
        "Senses": "darkvision 60 ft., passive Perception 14",
        "Languages": "\u2014",
        "Challenge": "5 (1800 XP)",
        "STR": "20 (+5)",
        "DEX": "11 (+0)",
        "CON": "18 (+4)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Trampling Charge. If the gorgon moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 16 Strength saving throw or be knocked prone. If the target is prone, the gorgon can make one attack with its hooves against it as a bonus action."
        ],
        "Actions": [
            "Gore.Melee Weapon Attack: +8 to hit, reach 5 ft., one target.Hit: 18 (2d12 + 5) piercing damage.",
            "Hooves.Melee Weapon Attack: +8 to hit, reach 5 ft., one target.Hit: 16 (2d10 + 5) bludgeoning damage.",
            "Petrifying Breath (Recharge 5-6). The gorgon exhales petrifying gas in a 30-foot cone. Each creature in that area must succeed on a DC 13 Constitution saving throw. On a failed save, a target begins to turn to stone and is restrained. The restrained target must repeat the saving throw at the end of its next turn. On a success, the effect ends on the target. On a failure, the target is petrified until freed by thegreater restorationspell or other magic."
        ]
    },
    "gray-ooze": {
        "name": "Gray Ooze",
        "type": "Medium ooze",
        "alignment": "unaligned",
        "Armor Class": "8",
        "Hit Points": "22 (3d8 + 9)",
        "Speed": "10 ft., climb 10 ft.",
        "Skills": "Stealth +2",
        "Damage Resistances": "acid, cold, fire",
        "Condition Immunities": "blinded, charmed, deafened, exhaustion, frightened, prone",
        "Senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 8",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "12 (+1)",
        "DEX": "6 (-2)",
        "CON": "16 (+3)",
        "INT": "1 (-5)",
        "WIS": "6 (-2)",
        "CHA": "2 (-4)",
        "features": [
            "Amorphous. The ooze can move through a space as narrow as 1 inch wide without squeezing.",
            "Corrode Metal. Any nonmagical weapon made of metal that hits the ooze corrodes. After dealing damage, the weapon takes a permanent and cumulative -1 penalty to damage rolls. If its penalty drops to -5, the weapon is destroyed. Nonmagical ammunition made of metal that hits the ooze is destroyed after dealing damage.",
            "False Appearance. While the ooze remains motionless, it is indistinguishable from an oily pool or wet rock."
        ],
        "Actions": [
            "Pseudopod.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 4 (1d6 + 1) bludgeoning damage plus 7 (2d6) acid damage, and if the target is wearing nonmagical metal armor, its armor is partly corroded and takes a permanent and cumulative -1 penalty to the AC it offers. The armor is destroyed if the penalty reduces its AC to 10."
        ]
    },
    "green-dragon-wyrmling": {
        "name": "Green Dragon Wyrmling",
        "type": "Medium dragon (Chromatic)",
        "alignment": "lawful evil",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "38 (7d8 + 7)",
        "Speed": "30 ft., fly 60 ft., swim 30 ft.",
        "Saving Throws": "Dex +3, Con +3, Wis +2, Cha +3",
        "Skills": "Perception +4, Stealth +3",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 14",
        "Languages": "Draconic",
        "Challenge": "2 (450 XP)",
        "STR": "15 (+2)",
        "DEX": "12 (+1)",
        "CON": "13 (+1)",
        "INT": "14 (+2)",
        "WIS": "11 (+0)",
        "CHA": "13 (+1)",
        "features": [
            "Amphibious. The dragon can breathe air and water."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 7 (1d10 + 2) piercing damage plus 3 (1d6) poison damage.",
            "Poison Breath (Recharge 5-6). The dragon exhales poisonous gas in a 15-foot cone. Each creature in that area must make a DC 11 Constitution saving throw, taking 21 (6d6) poison damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "green-hag": {
        "name": "Green Hag",
        "type": "Medium fey",
        "alignment": "neutral evil",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "82 (11d8 + 33)",
        "Speed": "30 ft.",
        "Skills": "Arcana +3, Deception +4, Perception +4, Stealth +3",
        "Senses": "darkvision 60 ft., passive Perception 14",
        "Languages": "Common, Draconic, Sylvan",
        "Challenge": "3 (700 XP)",
        "STR": "18 (+4)",
        "DEX": "12 (+1)",
        "CON": "16 (+3)",
        "INT": "13 (+1)",
        "WIS": "14 (+2)",
        "CHA": "14 (+2)",
        "features": [
            "Amphibious. The hag can breathe air and water.",
            "Innate Spellcasting. The hag's innate spellcasting ability is Charisma (spell save DC 12). She can innately cast the following spells, requiring no material components:",
            "Mimicry. The hag can mimic animal sounds and humanoid voices. A creature that hears the sounds can tell they are imitations with a successful DC 14 Wisdom (Insight) check."
        ],
        "Actions": [
            "Claws.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 13 (2d8 + 4) slashing damage.",
            "Illusory Appearance. The hag covers herself and anything she is wearing or carrying with a magical illusion that makes her look like another creature of her general size and humanoid shape. The illusion ends if the hag takes a bonus action to end it or if she dies. The changes wrought by this effect fail to hold up to physical inspection. For example, the hag could appear to have smooth skin, but someone touching her would feel her rough flesh. Otherwise, a creature must take an action to visually inspect the illusion and succeed on a DC 20 Intelligence (Investigation) check to discern that the hag is disguised.",
            "Invisible Passage. The hag magically turns invisible until she attacks or casts a spell, or until her concentration ends (as if concentrating on a spell). While invisible, she leaves no physical evidence of her passage, so she can be tracked only by magic. Any equipment she wears or carries is invisible with her."
        ]
    },
    "griffon": {
        "name": "Griffon",
        "type": "Large monstrosity",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "59 (7d10 + 21)",
        "Speed": "30 ft., fly 80 ft.",
        "Skills": "Perception +5",
        "Senses": "darkvision 60 ft., passive Perception 15",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "18 (+4)",
        "DEX": "15 (+2)",
        "CON": "16 (+3)",
        "INT": "2 (-4)",
        "WIS": "13 (+1)",
        "CHA": "8 (-1)",
        "features": [
            "Keen Sight. The griffon has advantage on Wisdom (Perception) checks that rely on sight."
        ],
        "Actions": [
            "Multiattack. The griffon makes two attacks: one with its beak and one with its claws.",
            "Beak.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 8 (1d8 + 4) piercing damage.",
            "Claws.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) slashing damage."
        ]
    },
    "grimlock": {
        "name": "Grimlock",
        "type": "Medium humanoid (Grimlock)",
        "alignment": "neutral evil",
        "Armor Class": "11",
        "Hit Points": "11 (2d8 + 2)",
        "Speed": "30 ft.",
        "Skills": "Athletics +5, Perception +3, Stealth +3",
        "Condition Immunities": "blinded",
        "Senses": "blindsight 30 ft. or 10 ft. while deafened (blind beyond this radius), passive Perception 13",
        "Languages": "Undercommon",
        "Challenge": "1/4 (50 XP)",
        "STR": "16 (+3)",
        "DEX": "12 (+1)",
        "CON": "12 (+1)",
        "INT": "9 (-1)",
        "WIS": "8 (-1)",
        "CHA": "6 (-2)",
        "features": [
            "Blind Senses. The grimlock can't use its blindsight while deafened and unable to smell.",
            "Keen Hearing and Smell. The grimlock has advantage on Wisdom (Perception) checks that rely on hearing or smell.",
            "Stone Camouflage. The grimlock has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."
        ],
        "Actions": [
            "Spiked Bone Club.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 5 (1d4 + 3) bludgeoning damage plus 2 (1d4) piercing damage."
        ]
    },
    "guard": {
        "name": "Guard",
        "type": "Medium humanoid (any race)",
        "alignment": "any alignment",
        "Armor Class": "16 (chain shirt, shield)",
        "Hit Points": "11 (2d8 + 2)",
        "Speed": "30 ft.",
        "Skills": "Perception +2",
        "Senses": "passive Perception 12",
        "Languages": "any one language (usually Common)",
        "Challenge": "1/8 (25 XP)",
        "STR": "13 (+1)",
        "DEX": "12 (+1)",
        "CON": "12 (+1)",
        "INT": "10 (+0)",
        "WIS": "11 (+0)",
        "CHA": "10 (+0)",
        "features": [],
        "Actions": [
            "Spear.Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target.Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack."
        ]
    },
    "guardian-naga": {
        "name": "Guardian Naga",
        "type": "Large monstrosity",
        "alignment": "lawful good",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "127 (15d10 + 45)",
        "Speed": "40 ft.",
        "Saving Throws": "Dex +8, Con +7, Int +7, Wis +8, Cha +8",
        "Damage Immunities": "poison",
        "Condition Immunities": "charmed, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 14",
        "Languages": "Celestial, Common",
        "Challenge": "10 (5900 XP)",
        "STR": "19 (+4)",
        "DEX": "18 (+4)",
        "CON": "16 (+3)",
        "INT": "16 (+3)",
        "WIS": "19 (+4)",
        "CHA": "18 (+4)",
        "features": [
            "Rejuvenation. If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only awishspell can prevent this trait from functioning.",
            "Spellcasting. The naga is an 11th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 16, +8 to hit with spell attacks), and it needs only verbal components to cast its spells. It has the following cleric spells prepared:"
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +8 to hit, reach 10 ft., one creature.Hit: 8 (1d8 + 4) piercing damage, and the target must make a DC 15 Constitution saving throw, taking 45 (10d8) poison damage on a failed save, or half as much damage on a successful one.",
            "Spit Poison.Ranged Weapon Attack: +8 to hit, range 15/30 ft., one creature.Hit: The target must make a DC 15 Constitution saving throw, taking 45 (10d8) poison damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "gynosphinx": {
        "name": "Gynosphinx",
        "type": "Large monstrosity",
        "alignment": "lawful neutral",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "136 (16d10 + 48)",
        "Speed": "40 ft., fly 60 ft.",
        "Skills": "Arcana +12, History +12, Perception +8, Religion +8",
        "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "psychic",
        "Condition Immunities": "charmed, frightened",
        "Senses": "truesight 120 ft., passive Perception 18",
        "Languages": "Common, Sphinx",
        "Challenge": "11 (7200 XP)",
        "STR": "18 (+4)",
        "DEX": "15 (+2)",
        "CON": "16 (+3)",
        "INT": "18 (+4)",
        "WIS": "18 (+4)",
        "CHA": "18 (+4)",
        "Legendary actions": [
            "The sphinx can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The sphinx regains spent legendary actions at the start of its turn.",
            "Claw Attack. The sphinx makes one claw attack.",
            "Teleport (Costs 2 Actions). The sphinx magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see.",
            "Cast a Spell (Costs 3 Actions). The sphinx casts a spell from its list of prepared spells, using a spell slot as normal."
        ],
        "features": [
            "Inscrutable. The sphinx is immune to any effect that would sense its emotions or read its thoughts, as well as any divination spell that it refuses. Wisdom (Insight) checks made to ascertain the sphinx's intentions or sincerity have disadvantage.",
            "Magic Weapons. The sphinx's weapon attacks are magical.",
            "Spellcasting. The sphinx is a 9th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 16, +8 to hit with spell attacks). It requires no material components to cast its spells. The sphinx has the following wizard spells prepared:"
        ],
        "Actions": [
            "Multiattack. The sphinx makes two claw attacks.",
            "Claw.Melee Weapon Attack: +8 to hit, reach 5 ft., one target.Hit: 13 (2d8 + 4) slashing damage."
        ]
    },
    "half-red-dragon-veteran": {
        "name": "Half-Red Dragon Veteran",
        "type": "Medium humanoid (Human)",
        "alignment": "any alignment",
        "Armor Class": "18 (plate)",
        "Hit Points": "65 (10d8 + 20)",
        "Speed": "30 ft.",
        "Skills": "Athletics +5, Perception +2",
        "Damage Resistances": "fire",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 12",
        "Languages": "Common, Draconic",
        "Challenge": "5 (1800 XP)",
        "STR": "16 (+3)",
        "DEX": "13 (+1)",
        "CON": "14 (+2)",
        "INT": "10 (+0)",
        "WIS": "11 (+0)",
        "CHA": "10 (+0)",
        "features": [],
        "Actions": [
            "Multiattack. The veteran makes two longsword attacks. If it has a shortsword drawn, it can also make a shortsword attack.",
            "Longsword.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands.",
            "Shortsword.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 6 (1d6 + 3) piercing damage.",
            "Heavy Crossbow.Ranged Weapon Attack: +3 to hit, range 100/400 ft., one target.Hit: 6 (1d10 + 1) piercing damage.",
            "Fire. Breath (Recharge. 5-6). The veteran exhales fire in a 15-foot cone. Each creature in that area must make a DC 15 Dexterity saving throw, taking 24 (7d6) fire damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "harpy": {
        "name": "Harpy",
        "type": "Medium monstrosity",
        "alignment": "chaotic evil",
        "Armor Class": "11",
        "Hit Points": "38 (7d8 + 7)",
        "Speed": "20 ft., fly 40 ft.",
        "Senses": "passive Perception 10",
        "Languages": "Common",
        "Challenge": "1 (200 XP)",
        "STR": "12 (+1)",
        "DEX": "13 (+1)",
        "CON": "12 (+1)",
        "INT": "7 (-2)",
        "WIS": "10 (+0)",
        "CHA": "13 (+1)",
        "features": [],
        "Actions": [
            "Multiattack. The harpy makes two attacks: one with its claws and one with its club.",
            "Claws.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 6 (2d4 + 1) slashing damage.",
            "Club.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 3 (1d4 + 1) bludgeoning damage.",
            "Luring Song. The harpy sings a magical melody. Every humanoid and giant within 300 feet of the harpy that can hear the song must succeed on a DC 11 Wisdom saving throw or be charmed until the song ends. The harpy must take a bonus action on its subsequent turns to continue singing. It can stop singing at any time. The song ends if the harpy is incapacitated. While charmed by the harpy, a target is incapacitated and ignores the songs of other harpies. If the charmed target is more than 5 feet away from the harpy, the target must move on its turn toward the harpy by the most direct route. It doesn't avoid opportunity attacks, but before moving into damaging terrain, such as lava or a pit, and whenever it takes damage from a source other than the harpy, a target can repeat the saving throw. A creature can also repeat the saving throw at the end of each of its turns. If a creature's saving throw is successful, the effect ends on it. A target that successfully saves is immune to this harpy's song for the next 24 hours."
        ]
    },
    "hawk": {
        "name": "Hawk",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "13",
        "Hit Points": "1 (1d4 - 1)",
        "Speed": "10 ft., fly 60 ft.",
        "Skills": "Perception +4",
        "Senses": "passive Perception 14",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "5 (-3)",
        "DEX": "16 (+3)",
        "CON": "8 (-1)",
        "INT": "2 (-4)",
        "WIS": "14 (+2)",
        "CHA": "6 (-2)",
        "features": [
            "Keen Sight. The hawk has advantage on Wisdom (Perception) checks that rely on sight."
        ],
        "Actions": [
            "Talons.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 1 slashing damage."
        ]
    },
    "hezrou": {
        "name": "Hezrou",
        "type": "Large fiend (Demon)",
        "alignment": "chaotic evil",
        "Armor Class": "16 (natural armor)",
        "Hit Points": "136 (13d10 + 65)",
        "Speed": "30 ft.",
        "Saving Throws": "Str +7, Con +8, Wis +4",
        "Damage Resistances": "cold, fire, lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 120 ft., passive Perception 11",
        "Languages": "Abyssal, telepathy 120 ft.",
        "Challenge": "8 (3900 XP)",
        "STR": "19 (+4)",
        "DEX": "17 (+3)",
        "CON": "20 (+5)",
        "INT": "5 (-3)",
        "WIS": "12 (+1)",
        "CHA": "13 (+1)",
        "features": [
            "Magic Resistance. The hezrou has advantage on saving throws against spells and other magical effects.",
            "Stench. Any creature that starts its turn within 10 feet of the hezrou must succeed on a DC 14 Constitution saving throw or be poisoned until the start of its next turn. On a successful saving throw, the creature is immune to the hezrou's stench for 24 hours."
        ],
        "Actions": [
            "Multiattack. The hezrou makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 15 (2d10 + 4) piercing damage.",
            "Claw.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) slashing damage."
        ]
    },
    "hill-giant": {
        "name": "Hill Giant",
        "type": "Huge giant",
        "alignment": "chaotic evil",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "105 (10d12 + 40)",
        "Speed": "40 ft.",
        "Skills": "Perception +2",
        "Senses": "passive Perception 12",
        "Languages": "Giant",
        "Challenge": "5 (1800 XP)",
        "STR": "21 (+5)",
        "DEX": "8 (-1)",
        "CON": "19 (+4)",
        "INT": "5 (-3)",
        "WIS": "9 (-1)",
        "CHA": "6 (-2)",
        "features": [],
        "Actions": [
            "Multiattack. The giant makes two greatclub attacks.",
            "Greatclub.Melee Weapon Attack: +8 to hit, reach 10 ft., one target.Hit: 18 (3d8 + 5) bludgeoning damage.",
            "Rock.Ranged Weapon Attack: +8 to hit, range 60/240 ft., one target.Hit: 21 (3d10 + 5) bludgeoning damage."
        ]
    },
    "hippogriff": {
        "name": "Hippogriff",
        "type": "Large monstrosity",
        "alignment": "unaligned",
        "Armor Class": "11",
        "Hit Points": "19 (3d10 + 3)",
        "Speed": "40 ft., fly 60 ft.",
        "Skills": "Perception +5",
        "Senses": "passive Perception 15",
        "Languages": "\u2014",
        "Challenge": "1 (200 XP)",
        "STR": "17 (+3)",
        "DEX": "13 (+1)",
        "CON": "13 (+1)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "8 (-1)",
        "features": [
            "Keen Sight. The hippogriff has advantage on Wisdom (Perception) checks that rely on sight."
        ],
        "Actions": [
            "Multiattack. The hippogriff makes two attacks: one with its beak and one with its claws.",
            "Beak.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 8 (1d10 + 3) piercing damage.",
            "Claws.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) slashing damage."
        ]
    },
    "hobgoblin": {
        "name": "Hobgoblin",
        "type": "Medium humanoid (Goblinoid)",
        "alignment": "lawful evil",
        "Armor Class": "18 (chain mail, shield)",
        "Hit Points": "11 (2d8 + 2)",
        "Speed": "30 ft.",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Common, Goblin",
        "Challenge": "1/2 (100 XP)",
        "STR": "13 (+1)",
        "DEX": "12 (+1)",
        "CON": "12 (+1)",
        "INT": "10 (+0)",
        "WIS": "10 (+0)",
        "CHA": "9 (-1)",
        "features": [
            "Martial Advantage. Once per turn, the hobgoblin can deal an extra 7 (2d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the hobgoblin that isn't incapacitated."
        ],
        "Actions": [
            "Longsword.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 5 (1d8 + 1) slashing damage, or 6 (1d10 + 1) slashing damage if used with two hands.",
            "Longbow.Ranged Weapon Attack: +3 to hit, range 150/600 ft., one target.Hit: 5 (1d8 + 1) piercing damage."
        ]
    },
    "hobgoblin-captain": {
        "name": "Hobgoblin Captain",
        "type": "Medium humanoid (Goblinoid)",
        "alignment": "lawful evil",
        "Armor Class": "17 (half plate)",
        "Hit Points": "39 (6d8 + 12)",
        "Speed": "30 ft.",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Common, Goblin",
        "Challenge": "3 (700 XP)",
        "STR": "15 (+2)",
        "DEX": "14 (+2)",
        "CON": "14 (+2)",
        "INT": "12 (+1)",
        "WIS": "10 (+0)",
        "CHA": "13 (+1)",
        "features": [
            "Martial Advantage. Once per turn, the hobgoblin can deal an extra 10 (3d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the hobgoblin that isn't incapacitated."
        ],
        "Actions": [
            "Multiattack. The hobgoblin makes two greatsword attacks.",
            "Greatsword.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 9 (2d6 + 2) piercing damage.",
            "Javelin.Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target.Hit: 5 (1d6 + 2) piercing damage.",
            "Leadership (Recharges after a Short or Long Rest). For 1 minute, the hobgoblin can utter a special command or warning whenever a nonhostile creature that it can see within 30 feet of it makes an attack roll or a saving throw. The creature can add a d4 to its roll provided it can hear and understand the hobgoblin. A creature can benefit from only one Leadership die at a time. This effect ends if the hobgoblin is incapacitated."
        ]
    },
    "hobgoblin-warlord": {
        "name": "Hobgoblin Warlord",
        "type": "Medium humanoid (Goblinoid)",
        "alignment": "lawful evil",
        "Armor Class": "20 (plate, shield)",
        "Hit Points": "97 (13d8 + 39)",
        "Speed": "30 ft.",
        "Saving Throws": "Int +5, Wis +3, Cha +5",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Common, Goblin",
        "Challenge": "6 (2300 XP)",
        "STR": "16 (+3)",
        "DEX": "14 (+2)",
        "CON": "16 (+3)",
        "INT": "14 (+2)",
        "WIS": "11 (+0)",
        "CHA": "15 (+2)",
        "Reactions": [
            "Parry. The hobgoblin adds 3 to its AC against one melee attack that would hit it. To do so, the hobgoblin must see the attacker and be wielding a melee weapon."
        ],
        "features": [
            "Martial Advantage. Once per turn, the hobgoblin can deal an extra 14 (4d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the hobgoblin that isn't incapacitated."
        ],
        "Actions": [
            "Multiattack. The hobgoblin makes three melee attacks. Alternatively, it can make two ranged attacks with its javelins.",
            "Longsword.Melee Weapon Attack: +9 to hit, reach 5 ft., one target.Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands.",
            "Shield Bash.Melee Weapon Attack: +9 to hit, reach 5 ft., one creature.Hit: 5 (1d4 + 3) bludgeoning damage. If the target is Large or smaller, it must succeed on a DC 14 Strength saving throw or be knocked prone.",
            "Javelin.Melee or Ranged Weapon Attack: +9 to hit, reach 5 ft. or range 30/120 ft., one target.Hit: 6 (1d6 + 3) piercing damage.",
            "Leadership (Recharges after a Short or Long Rest). For 1 minute, the hobgoblin can utter a special command or warning whenever a nonhostile creature that it can see within 30 feet of it makes an attack roll or a saving throw. The creature can add a d4 to its roll provided it can hear and understand the hobgoblin. A creature can benefit from only one Leadership die at a time. This effect ends if the hobgoblin is incapacitated."
        ]
    },
    "homunculus": {
        "name": "Homunculus",
        "type": "Tiny construct",
        "alignment": "neutral",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "5 (2d4)",
        "Speed": "20 ft., fly 40 ft.",
        "Damage Immunities": "poison",
        "Condition Immunities": "charmed, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "understands the languages of its creator but can't speak",
        "Challenge": "0 (10 XP)",
        "STR": "4 (-3)",
        "DEX": "15 (+2)",
        "CON": "11 (+0)",
        "INT": "10 (+0)",
        "WIS": "10 (+0)",
        "CHA": "7 (-2)",
        "features": [
            "Telepathic Bond. While the homunculus is on the same plane of existence as its master, it can magically convey what it senses to its master, and the two can communicate telepathically."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 1 piercing damage, and the target must succeed on a DC 10 Constitution saving throw or be poisoned for 1 minute. If the saving throw fails by 5 or more, the target is instead poisoned for 5 (1d10) minutes and unconscious while poisoned in this way."
        ]
    },
    "horned-devil": {
        "name": "Horned Devil",
        "type": "Large fiend (Devil)",
        "alignment": "lawful evil",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "178 (17d10 + 85)",
        "Speed": "20 ft., fly 60 ft.",
        "Saving Throws": "Str +10, Dex +7, Wis +7, Cha +7",
        "Damage Resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks not made with silvered weapons",
        "Damage Immunities": "fire, poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 120 ft., passive Perception 13",
        "Languages": "Infernal, telepathy 120 ft.",
        "Challenge": "11 (7200 XP)",
        "STR": "22 (+6)",
        "DEX": "17 (+3)",
        "CON": "21 (+5)",
        "INT": "12 (+1)",
        "WIS": "16 (+3)",
        "CHA": "17 (+3)",
        "features": [
            "Devil's Sight. Magical darkness doesn't impede the devil's darkvision.",
            "Magic Resistance. The devil has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack. The devil makes three melee attacks: two with its fork and one with its tail. It can use Hurl Flame in place of any melee attack.",
            "Fork.Melee Weapon Attack: +10 to hit, reach 10 ft., one target.Hit: 15 (2d8 + 6) piercing damage.",
            "Tail.Melee Weapon Attack: +10 to hit, reach 10 ft., one target.Hit: 10 (1d8 + 6) piercing damage. If the target is a creature other than an undead or a construct, it must succeed on a DC 17 Constitution saving throw or lose 10 (3d6) hit points at the start of each of its turns due to an infernal wound. Each time the devil hits the wounded target with this attack, the damage dealt by the wound increases by 10 (3d6). Any creature can take an action to stanch the wound with a successful DC 12 Wisdom (Medicine) check. The wound also closes if the target receives magical healing.",
            "Hurl Flame.Ranged Spell Attack: +7 to hit, range 150 ft., one target.Hit: 14 (4d6) fire damage. If the target is a flammable object that isn't being worn or carried, it also catches fire."
        ]
    },
    "hunter-shark": {
        "name": "Hunter Shark",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "45 (6d10 + 12)",
        "Speed": "0 ft., swim 40 ft.",
        "Skills": "Perception +2",
        "Senses": "blindsight 30 ft., passive Perception 12",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "18 (+4)",
        "DEX": "13 (+1)",
        "CON": "15 (+2)",
        "INT": "1 (-5)",
        "WIS": "10 (+0)",
        "CHA": "4 (-3)",
        "features": [
            "Blood Frenzy. The shark has advantage on melee attack rolls against any creature that doesn't have all its hit points.",
            "Water Breathing. The shark can breathe only underwater."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 13 (2d8 + 4) piercing damage."
        ]
    },
    "hydra": {
        "name": "Hydra",
        "type": "Huge monstrosity",
        "alignment": "unaligned",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "172 (15d12 + 75)",
        "Speed": "30 ft., swim 30 ft.",
        "Skills": "Perception +6",
        "Senses": "darkvision 60 ft., passive Perception 16",
        "Languages": "\u2014",
        "Challenge": "8 (3900 XP)",
        "STR": "20 (+5)",
        "DEX": "12 (+1)",
        "CON": "20 (+5)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "7 (-2)",
        "features": [
            "Hold Breath. The hydra can hold its breath for 1 hour.",
            "Multiple Heads. The hydra has five heads. While it has more than one head, the hydra has advantage on saving throws against being blinded, charmed, deafened, frightened, stunned, and knocked unconscious. Whenever the hydra takes 25 or more damage in a single turn, one of its heads dies. If all its heads die, the hydra dies. At the end of its turn, it grows two heads for each of its heads that died since its last turn, unless it has taken fire damage since its last turn. The hydra regains 10 hit points for each head regrown in this way.",
            "Reactive Heads. For each head the hydra has beyond one, it gets an extra reaction that can be used only for opportunity attacks.",
            "Wakeful. While the hydra sleeps, at least one of its heads is awake."
        ],
        "Actions": [
            "Multiattack. The hydra makes as many bite attacks as it has heads.",
            "Bite.Melee Weapon Attack: +8 to hit, reach 10 ft., one target.Hit: 10 (1d10 + 5) piercing damage."
        ]
    },
    "hyena": {
        "name": "Hyena",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "11",
        "Hit Points": "5 (1d8 + 1)",
        "Speed": "50 ft.",
        "Skills": "Perception +3",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "11 (+0)",
        "DEX": "13 (+1)",
        "CON": "12 (+1)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "5 (-3)",
        "features": [
            "Pack Tactics. The hyena has advantage on an attack roll against a creature if at least one of the hyena's allies is within 5 feet of the creature and the ally isn't incapacitated."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +2 to hit, reach 5 ft., one target.Hit: 3 (1d6) piercing damage."
        ]
    },
    "ice-devil": {
        "name": "Ice Devil",
        "type": "Large fiend (Devil)",
        "alignment": "lawful evil",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "180 (19d10 + 76)",
        "Speed": "40 ft.",
        "Saving Throws": "Dex +7, Con +9, Wis +7, Cha +9",
        "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered",
        "Damage Immunities": "cold, fire, poison",
        "Condition Immunities": "poisoned",
        "Senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 12",
        "Languages": "Infernal, telepathy 120 ft.",
        "Challenge": "14 (11500 XP)",
        "STR": "21 (+5)",
        "DEX": "14 (+2)",
        "CON": "18 (+4)",
        "INT": "18 (+4)",
        "WIS": "15 (+2)",
        "CHA": "18 (+4)",
        "features": [
            "Devil's Sight. Magical darkness doesn't impede the devil's darkvision.",
            "Magic Resistance. The devil has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack. The devil makes three attacks: one with its bite, one with its claws, and one with its tail.",
            "Bite.Melee Weapon Attack: +10 to hit, reach 5 ft., one target.Hit: 12 (2d6 + 5) piercing damage plus 10 (3d6) cold damage.",
            "Claws.Melee Weapon Attack: +10 to hit, reach 5 ft., one target.Hit: 10 (2d4 + 5) slashing damage plus 10 (3d6) cold damage.",
            "Tail.Melee Weapon Attack: +10 to hit, reach 10 ft., one target.Hit: 12 (2d6 + 5) bludgeoning damage plus 10 (3d6) cold damage.",
            "Wall of Ice (Recharge 6). The devil magically forms an opaque wall of ice on a solid surface it can see within 60 feet of it. The wall is 1 foot thick and up to 30 feet long and 10 feet high, or it's a hemispherical dome up to 20 feet in diameter. When the wall appears, each creature in its space is pushed out of it by the shortest route. The creature chooses which side of the wall to end up on, unless the creature is incapacitated. The creature then makes a DC 17 Dexterity saving throw, taking 35 (10d6) cold damage on a failed save, or half as much damage on a successful one. The wall lasts for 1 minute or until the devil is incapacitated or dies. The wall can be damaged and breached; each 10-foot section has AC 5, 30 hit points, vulnerability to fire damage, and immunity to acid, cold, necrotic, poison, and psychic damage. If a section is destroyed, it leaves behind a sheet of frigid air in the space the wall occupied. Whenever a creature finishes moving through the frigid air on a turn, willingly or otherwise, the creature must make a DC 17 Constitution saving throw, taking 17 (5d6) cold damage on a failed save, or half as much damage on a successful one. The frigid air dissipates when the rest of the wall vanishes."
        ]
    },
    "ice-mephit": {
        "name": "Ice Mephit",
        "type": "Small elemental",
        "alignment": "neutral evil",
        "Armor Class": "11",
        "Hit Points": "21 (6d6)",
        "Speed": "30 ft., fly 30 ft.",
        "Skills": "Perception +2, Stealth +3",
        "Damage Vulnerabilities": "bludgeoning, fire",
        "Damage Immunities": "cold, poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 60 ft., passive Perception 12",
        "Languages": "Aquan, Auran",
        "Challenge": "1/2 (100 XP)",
        "STR": "7 (-2)",
        "DEX": "13 (+1)",
        "CON": "10 (+0)",
        "INT": "9 (-1)",
        "WIS": "11 (+0)",
        "CHA": "12 (+1)",
        "features": [
            "Death Burst. When the mephit dies, it explodes in a burst of jagged ice. Each creature within 5 feet of it must make a DC 10 Dexterity saving throw, taking 4 (1d8) slashing damage on a failed save, or half as much damage on a successful one.",
            "False Appearance. While the mephit remains motionless, it is indistinguishable from an ordinary shard of ice.",
            "Innate Spellcasting (1/Day). The mephit can innately castfog cloud, requiring no material components. Its innate spellcasting ability is Charisma."
        ],
        "Actions": [
            "Claws.Melee Weapon Attack: +3 to hit, reach 5 ft., one creature.Hit: 3 (1d4 + 1) slashing damage plus 2 (1d4) cold damage.",
            "Frost Breath (Recharge 6). The mephit exhales a 15-foot cone of cold air. Each creature in that area must succeed on a DC 10 Dexterity saving throw, taking 5 (2d4) cold damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "imp": {
        "name": "Imp",
        "type": "Tiny fiend (Devil",
        "alignment": "Shapechanger), lawful evil",
        "Armor Class": "13",
        "Hit Points": "10 (3d4 + 3)",
        "Speed": "20 ft., fly 40 ft.",
        "Skills": "Deception +4, Insight +3, Persuasion +4, Stealth +5",
        "Damage Resistances": "cold; bludgeoning, piercing, and slashing from nonmagical attacks not made with silvered weapons",
        "Damage Immunities": "fire, poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 120 ft., passive Perception 11",
        "Languages": "Infernal, Common",
        "Challenge": "1 (200 XP)",
        "STR": "6 (-2)",
        "DEX": "17 (+3)",
        "CON": "13 (+1)",
        "INT": "11 (+0)",
        "WIS": "12 (+1)",
        "CHA": "14 (+2)",
        "features": [
            "Shapechanger. The imp can use its action to polymorph into a beast form that resembles a rat (speed 20 ft.), a raven (20 ft., fly 60 ft.), or a spider (20 ft., climb 20 ft.), or back into its true form. Its statistics are the same in each form, except for the speed changes noted. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.",
            "Devil's Sight. Magical darkness doesn't impede the imp's darkvision.",
            "Magic Resistance. The imp has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Sting (Bite in Beast Form).Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 5 (1d4 + 3) piercing damage, and the target must make on a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one.",
            "Invisibility. The imp magically turns invisible until it attacks or until its concentration ends (as if concentrating on a spell). Any equipment the imp wears or carries is invisible with it."
        ]
    },
    "intellect-devourer": {
        "name": "Intellect Devourer",
        "type": "Tiny aberration",
        "alignment": "lawful evil",
        "Armor Class": "12",
        "Hit Points": "21 (6d4 + 6)",
        "Speed": "40 ft.",
        "Skills": "Perception +2, Stealth +4",
        "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "Condition Immunities": "blinded",
        "Senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 12",
        "Languages": "understands Deep Speech but can 't speak, telepathy 60 ft.",
        "Challenge": "2 (450 XP)",
        "STR": "6 (-2)",
        "DEX": "14 (+2)",
        "CON": "13 (+1)",
        "INT": "12 (+1)",
        "WIS": "11 (+0)",
        "CHA": "10 (+0)",
        "features": [
            "Detect Sentience. The intellect devourer can sense the presence and location of any creature within 300 feet of it that has an Intelligence of 3 or higher, regardless of interposing barriers, unless the creature is protected by amind blankspell."
        ],
        "Actions": [
            "Multiattack. The intellect devourer makes one attack with its claws and uses Devour Intellect.",
            "Claws.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 7 (2d4 + 2) slashing damage.",
            "Devour Intellect. The intellect devourer targets one creature it can see within 10 feet of it that has a brain. The target must succeed on a DC 12 Intelligence saving throw against this magic or take 11 (2d10) psychic damage. Also on a failure, roll 3d6: If the total equals or exceeds the target's Intelligence score, that score is reduced to 0. The target is stunned until it regains at least one point of Intelligence.",
            "Body Thief. The intellect devourer initiates an Intelligence contest with an incapacitated humanoid within 5 feet of it. If it wins the contest, the intellect devourer magically consumes the target's brain, teleports into the target's skull, and takes control of the target's body. While inside a creature, the intellect devourer has total cover against attacks and other effects originating outs ide its host. The intellect devourer retains its Intelligence, Wisdom, and Charisma scores, as well as its understanding of Deep Speech, its telepathy, and its traits. It otherwise adopts the target's statistics. It knows everything the creature knew, including spells and languages. If the host body drops to 0 hit points, the intellect devourer must leave it. Aprotection from evil and goodspell cast on the body drives the intellect devourer out. The intellect devourer is also forced out if the target regains its devoured brain by means of awish. By spending 5 feet of its movement, the intellect devourer can voluntarily leave the body, teleporting to the nearest unoccupied space within 5 feet of it. The body then dies, unless its brain is restored within 1 round."
        ]
    },
    "invisible-stalker": {
        "name": "Invisible Stalker",
        "type": "Medium elemental",
        "alignment": "neutral",
        "Armor Class": "14",
        "Hit Points": "104 (16d8 + 32)",
        "Speed": "50 ft., fly 50 ft. (hover)",
        "Skills": "Perception +8, Stealth +10",
        "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "poison",
        "Condition Immunities": "exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious",
        "Senses": "darkvision 60 ft., passive Perception 18",
        "Languages": "Auran, understands Common but doesn't speak it",
        "Challenge": "6 (2300 XP)",
        "STR": "16 (+3)",
        "DEX": "19 (+4)",
        "CON": "14 (+2)",
        "INT": "10 (+0)",
        "WIS": "15 (+2)",
        "CHA": "11 (+0)",
        "features": [
            "Invisibility. The stalker is invisible.",
            "Faultless Tracker. The stalker is given a quarry by its summoner. The stalker knows the direction and distance to its quarry as long as the two of them are on the same plane of existence. The stalker also knows the location of its summoner."
        ],
        "Actions": [
            "Multiattack. The stalker makes two slam attacks.",
            "Slam.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) bludgeoning damage."
        ]
    },
    "iron-golem": {
        "name": "Iron Golem",
        "type": "Large construct",
        "alignment": "unaligned",
        "Armor Class": "20 (natural armor)",
        "Hit Points": "210 (20d10 + 100)",
        "Speed": "30 ft.",
        "Damage Immunities": "fire, poison, psychic; bludgeoning, piercing, and slashing from nonmagical attacks that aren't adamantine",
        "Condition Immunities": "charmed, exhaustion, frightened, paralyzed, petrified, poisoned",
        "Senses": "darkvision 120 ft., passive Perception 10",
        "Languages": "understands the languages of its creator but can't speak",
        "Challenge": "16 (15000 XP)",
        "STR": "24 (+7)",
        "DEX": "9 (-1)",
        "CON": "20 (+5)",
        "INT": "3 (-4)",
        "WIS": "11 (+0)",
        "CHA": "1 (-5)",
        "features": [
            "Fire Absorption. Whenever the golem is subjected to fire damage, it takes no damage and instead regains a number of hit points equal to the fire damage dealt.",
            "Immutable Form. The golem is immune to any spell or effect that would alter its form.",
            "Magic Resistance. The golem has advantage on saving throws against spells and other magical effects.",
            "Magic Weapons. The golem's weapon attacks are magical."
        ],
        "Actions": [
            "Multiattack. The golem makes two melee attacks.",
            "Slam.Melee Weapon Attack: +13 to hit, reach 5 ft., one target.Hit: 20 (3d8 + 7) bludgeoning damage.",
            "Sword.Melee Weapon Attack: +13 to hit, reach 10 ft., one target.Hit: 23 (3d10 + 7) slashing damage.",
            "Poison Breath (Recharge 6). The golem exhales poisonous gas in a 15-foot cone. Each creature in that area must make a DC 19 Constitution saving throw, taking 45 (10d8) poison damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "jackal": {
        "name": "Jackal",
        "type": "Small beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "3 (1d6)",
        "Speed": "40 ft.",
        "Skills": "Perception +3",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "8 (-1)",
        "DEX": "15 (+2)",
        "CON": "11 (+0)",
        "INT": "3 (-4)",
        "WIS": "12 (+1)",
        "CHA": "6 (-2)",
        "features": [
            "Keen Hearing and Smell. The jackal has advantage on Wisdom (Perception) checks that rely on hearing or smell.",
            "Pack Tactics. The jackal has advantage on an attack roll against a creature if at least one of the jackal's allies is within 5 feet of the creature and the ally isn't incapacitated."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +1 to hit, reach 5 ft., one target.Hit: 1 (1d4 - 1) piercing damage."
        ]
    },
    "killer-whale": {
        "name": "Killer Whale",
        "type": "Huge beast",
        "alignment": "unaligned",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "90 (12d12 + 12)",
        "Speed": "0 ft., swim 60 ft.",
        "Skills": "Perception +3",
        "Senses": "blindsight 120 ft., passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "3 (700 XP)",
        "STR": "19 (+4)",
        "DEX": "10 (+0)",
        "CON": "13 (+1)",
        "INT": "3 (-4)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Echolocation. The whale can't use its blindsight while deafened.",
            "Hold Breath. The whale can hold its breath for 30 minutes.",
            "Keen Hearing. The whale has advantage on Wisdom (Perception) checks that rely on hearing."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 21 (5d6 + 4) piercing damage."
        ]
    },
    "knight": {
        "name": "Knight",
        "type": "Medium humanoid (any race)",
        "alignment": "any alignment",
        "Armor Class": "18 (plate)",
        "Hit Points": "52 (8d8 + 16)",
        "Speed": "30 ft.",
        "Saving Throws": "Con +4, Wis +2",
        "Senses": "passive Perception 10",
        "Languages": "any one language (usually Common)",
        "Challenge": "3 (700 XP)",
        "STR": "16 (+3)",
        "DEX": "11 (+0)",
        "CON": "14 (+2)",
        "INT": "11 (+0)",
        "WIS": "11 (+0)",
        "CHA": "15 (+2)",
        "Reactions": [
            "Parry. The knight adds 2 to its AC against one melee attack that would hit it. To do so, the knight must see the attacker and be wielding a melee weapon."
        ],
        "features": [
            "Brave. The knight has advantage on saving throws against being frightened."
        ],
        "Actions": [
            "Multiattack. The knight makes two melee attacks.",
            "Greatsword.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) slashing damage.",
            "Heavy Crossbow.Ranged Weapon Attack: +2 to hit, range 100/400 ft., one target.Hit: 5 (1d10) piercing damage.",
            "Leadership (Recharges after a Short or Long Rest). For 1 minute, the knight can utter a special command or warning whenever a nonhostile creature that it can see within 30 feet of it makes an attack roll or a saving throw. The creature can add a d4 to its roll provided it can hear and understand the knight. A creature can benefit from only one Leadership die at a time. This effect ends if the knight is incapacitated."
        ]
    },
    "kobold": {
        "name": "Kobold",
        "type": "Small humanoid (Kobold)",
        "alignment": "lawful evil",
        "Armor Class": "12",
        "Hit Points": "5 (2d6 - 2)",
        "Speed": "30 ft.",
        "Senses": "darkvision 60 ft., passive Perception 8",
        "Languages": "Common, Draconic",
        "Challenge": "1/8 (25 XP)",
        "STR": "7 (-2)",
        "DEX": "15 (+2)",
        "CON": "9 (-1)",
        "INT": "8 (-1)",
        "WIS": "7 (-2)",
        "CHA": "8 (-1)",
        "features": [
            "Sunlight Sensitivity. While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.",
            "Pack Tactics. The kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 feet of the creature and the ally isn't incapacitated."
        ],
        "Actions": [
            "Dagger.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 4 (1d4 + 2) piercing damage.",
            "Sling.Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target.Hit: 4 (1d4 + 2) bludgeoning damage."
        ]
    },
    "kraken": {
        "name": "Kraken",
        "type": "Gargantuan monstrosity (Titan)",
        "alignment": "chaotic evil",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "472 (27d20 + 189)",
        "Speed": "20 ft., swim 60 ft.",
        "Saving Throws": "Str +17, Dex +7, Con +14, Int +13, Wis +11",
        "Damage Immunities": "lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Condition Immunities": "frightened, paralyzed",
        "Senses": "truesight 120 ft., passive Perception 14",
        "Languages": "understands Abyssal, Celestial, Infernal, and Primordial but can't speak, telepathy 120 ft.",
        "Challenge": "23 (50000 XP)",
        "STR": "30 (+10)",
        "DEX": "11 (+0)",
        "CON": "25 (+7)",
        "INT": "22 (+6)",
        "WIS": "18 (+4)",
        "CHA": "20 (+5)",
        "Legendary actions": [
            "The kraken can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The kraken regains spent legendary actions at the start of its turn.",
            "Tentacle Attack or Fling. The kraken makes one tentacle attack or uses its Fling.",
            "Lightning Storm (Costs 2 Actions). The kraken uses Lightning Storm.",
            "Ink Cloud (Costs 3 Actions). While underwater, the kraken expels an ink cloud in a 60-foot radius. The cloud spreads around corners, and that area is heavily obscured to creatures other than the kraken. Each creature other than the kraken that ends its turn there must succeed on a DC 23 Constitution saving throw, taking 16 (3d10) poison damage on a failed save, or half as much damage on a successful one. A strong current disperses the cloud, which otherwise disappears at the end of the kraken's next turn."
        ],
        "features": [
            "Amphibious. The kraken can breathe air and water.",
            "Freedom of Movement. The kraken ignores difficult terrain, and magical effects can't reduce its speed or cause it to be restrained. It can spend 5 feet of movement to escape from nonmagical restraints or being grappled.",
            "Siege Monster. The kraken deals double damage to objects and structures."
        ],
        "Actions": [
            "Multiattack. The kraken makes three tentacle attacks, each of which it can replace with one use of Fling.",
            "Bite.Melee Weapon Attack: +17 to hit, reach 5 ft., one target.Hit: 23 (3d8 + 10) piercing damage. If the target is a Large or smaller creature grappled by the kraken, that creature is swallowed, and the grapple ends. While swallowed, the creature is blinded and restrained, it has total cover against attacks and other effects outside the kraken, and it takes 42 (12d6) acid damage at the start of each of the kraken's turns. If the kraken takes 50 damage or more on a single turn from a creature inside it, the kraken must succeed on a DC 25 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall prone in a space within 10 feet of the kraken. If the kraken dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 15 feet of movement, exiting prone.",
            "Tentacle.Melee Weapon Attack: +17 to hit, reach 30 ft., one target.Hit: 20 (3d6 + 10) bludgeoning damage, and the target is grappled (escape DC 18). Until this grapple ends, the target is restrained. The kraken has ten tentacles, each of which can grapple one target.",
            "Fling. One Large or smaller object held or creature grappled by the kraken is thrown up to 60 feet in a random direction and knocked prone. If a thrown target strikes a solid surface, the target takes 3 (1d6) bludgeoning damage for every 10 feet it was thrown. If the target is thrown at another creature, that creature must succeed on a DC 18 Dexterity saving throw or take the same damage and be knocked prone.",
            "Lightning Storm. The kraken magically creates three bolts of lightning, each of which can strike a target the kraken can see within 120 feet of it. A target must make a DC 23 Dexterity saving throw, taking 22 (4d10) lightning damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "lamia": {
        "name": "Lamia",
        "type": "Large monstrosity",
        "alignment": "chaotic evil",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "97 (13d10 + 26)",
        "Speed": "30 ft.",
        "Skills": "Deception +7, Insight +4, Stealth +3",
        "Senses": "darkvision 60 ft., passive Perception 12",
        "Languages": "Abyssal, Common",
        "Challenge": "4 (1100 XP)",
        "STR": "16 (+3)",
        "DEX": "13 (+1)",
        "CON": "15 (+2)",
        "INT": "14 (+2)",
        "WIS": "15 (+2)",
        "CHA": "16 (+3)",
        "features": [
            "Innate Spellcasting. The lamia's innate spellcasting ability is Charisma (spell save DC 13). It can innately cast the following spells, requiring no material components."
        ],
        "Actions": [
            "Multiattack. The lamia makes two attacks: one with its claws and one with its dagger or Intoxicating Touch.",
            "Claws.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 14 (2d10 + 3) slashing damage.",
            "Dagger.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 5 (1d4 + 3) piercing damage.",
            "Intoxicating Touch.Melee Spell Attack: +5 to hit, reach 5 ft., one creature.Hit: The target is magically cursed for 1 hour. Until the curse ends, the target has disadvantage on Wisdom saving throws and all ability checks."
        ]
    },
    "lemure": {
        "name": "Lemure",
        "type": "Medium fiend (Devil)",
        "alignment": "lawful evil",
        "Armor Class": "7",
        "Hit Points": "13 (3d8)",
        "Speed": "15 ft.",
        "Damage Resistances": "cold",
        "Damage Immunities": "fire, poison",
        "Condition Immunities": "charmed, frightened, poisoned",
        "Senses": "darkvision 120 ft., passive Perception 10",
        "Languages": "understands Infernal but can't speak",
        "Challenge": "0 (10 XP)",
        "STR": "10 (+0)",
        "DEX": "5 (-3)",
        "CON": "11 (+0)",
        "INT": "1 (-5)",
        "WIS": "11 (+0)",
        "CHA": "3 (-4)",
        "features": [
            "Devil's Sight. Magical darkness doesn't impede the lemure's darkvision.",
            "Hellish Rejuvenation. A lemure that dies in the Nine Hells comes back to life with all its hit points in 1d10 days unless it is killed by a good-aligned creature with ablessspell cast on that creature or its remains are sprinkled with holy water."
        ],
        "Actions": [
            "Fist.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 2 (1d4) bludgeoning damage."
        ]
    },
    "lich": {
        "name": "Lich",
        "type": "Medium undead",
        "alignment": "any evil alignment",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "135 (18d8 + 54)",
        "Speed": "30 ft.",
        "Saving Throws": "Con +10, Int +12, Wis +9",
        "Skills": "Arcana +19, History +12, Insight +9, Perception +9",
        "Damage Resistances": "cold, lightning, necrotic",
        "Damage Immunities": "poison; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Condition Immunities": "charmed, exhaustion, frightened, paralyzed, poisoned",
        "Senses": "truesight 120 ft., passive Perception 19",
        "Languages": "Common plus up to five other languages",
        "Challenge": "21 (33000 XP)",
        "STR": "11 (+0)",
        "DEX": "16 (+3)",
        "CON": "16 (+3)",
        "INT": "20 (+5)",
        "WIS": "14 (+2)",
        "CHA": "16 (+3)",
        "Legendary actions": [
            "The lich can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The lich regains spent legendary actions at the start of its turn.",
            "Cantrip. The lich casts a cantrip.",
            "Paralyzing Touch (Costs 2 Actions). The lich uses its Paralyzing Touch.",
            "Frightening Gaze (Costs 2 Actions). The lich fixes its gaze on one creature it can see within 10 feet of it. The target must succeed on a DC 18 Wisdom saving throw against this magic or become frightened for 1 minute. The frightened target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a target's saving throw is successful or the effect ends for it, the target is immune to the lich's gaze for the next 24 hours.",
            "Disrupt Life (Costs 3 Actions). Each non\u2010undead creature within 20 feet of the lich must make a DC 18 Constitution saving throw against this magic, taking 21 (6d6) necrotic damage on a failed save, or half as much damage on a successful one."
        ],
        "features": [
            "Legendary Resistance (3/Day). If the lich fails a saving throw, it can choose to succeed instead.",
            "Rejuvenation. If it has a phylactery, a destroyed lich gains a new body in 1d10 days, regaining all its hit points and becoming active again. The new body appears within 5 feet of the phylactery.",
            "Spellcasting. The lich is an 18th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 20, +12 to hit with spell attacks). The lich has the following wizard spells prepared:",
            "Turn Resistance. The lich has advantage on saving throws against any effect that turns undead."
        ],
        "Actions": [
            "Paralyzing Touch.Melee Spell Attack: +12 to hit, reach 5 ft., one creature.Hit: 10 (3d6) cold damage. The target must succeed on a DC 18 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        ]
    },
    "lizard": {
        "name": "Lizard",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "10",
        "Hit Points": "2 (1d4)",
        "Speed": "20 ft., climb 20 ft.",
        "Senses": "darkvision 30 ft., passive Perception 9",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "2 (-4)",
        "DEX": "11 (+0)",
        "CON": "10 (+0)",
        "INT": "1 (-5)",
        "WIS": "8 (-1)",
        "CHA": "3 (-4)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +0 to hit, reach 5 ft., one target.Hit: 1 piercing damage."
        ]
    },
    "lizardfolk": {
        "name": "Lizardfolk",
        "type": "Medium humanoid (Lizardfolk)",
        "alignment": "neutral",
        "Armor Class": "15 (natural armor, shield)",
        "Hit Points": "22 (4d8 + 4)",
        "Speed": "30 ft., swim 30 ft.",
        "Skills": "Perception +3, Stealth +4, Survival +5",
        "Senses": "passive Perception 13",
        "Languages": "Draconic",
        "Challenge": "1/2 (100 XP)",
        "STR": "15 (+2)",
        "DEX": "10 (+0)",
        "CON": "13 (+1)",
        "INT": "7 (-2)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Hold Breath. The lizardfolk can hold its breath for 15 minutes."
        ],
        "Actions": [
            "Multiattack. The lizardfolk makes two melee attacks, each one with a different weapon.",
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) piercing damage.",
            "Heavy Club.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) bludgeoning damage.",
            "Javelin.Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target.Hit: 5 (1d6 + 2) piercing damage.",
            "Spiked Shield.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) piercing damage."
        ]
    },
    "lizardfolk-shaman": {
        "name": "Lizardfolk Shaman",
        "type": "Medium humanoid (Lizardfolk)",
        "alignment": "neutral",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "27 (5d8 + 5)",
        "Speed": "30 ft., swim 30 ft.",
        "Skills": "Perception +4, Stealth +4, Survival +6",
        "Senses": "passive Perception 14",
        "Languages": "Draconic",
        "Challenge": "2 (450 XP)",
        "STR": "15 (+2)",
        "DEX": "10 (+0)",
        "CON": "13 (+1)",
        "INT": "10 (+0)",
        "WIS": "15 (+2)",
        "CHA": "8 (-1)",
        "features": [
            "Hold Breath. The lizardfolk can hold its breath for 15 minutes.",
            "Spellcasting (Lizardfolk Form Only). The lizardfolk is a 5th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). The lizardfolk has the following druid spells prepared:"
        ],
        "Actions": [
            "Multiattack (Lizardfolk Form Only). The lizardfolk makes two attacks: one with its bite and one with its claws.",
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) piercing damage, or 7 (1d10 + 2) piercing damage in crocodile form. If the lizardfolk is in crocodile form and the target is a Large or smaller creature, the target is grappled (escape DC 12). Until this grapple ends, the target is restrained, and the lizardfolk can't bite another target. If the lizardfolk reverts to its true form, the grapple ends.",
            "Claws (Lizardfolk Form Only).Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 4 (1d4 + 2) slashing damage.",
            "Change Shape (Recharges after a Short or Long Rest). The lizardfolk magically polymorphs into a crocodile, remaining in that form for up to 1 hour. It can revert to its true form as a bonus action. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies."
        ]
    },
    "mage": {
        "name": "Mage",
        "type": "Medium humanoid (any race)",
        "alignment": "any alignment",
        "Armor Class": "12 (15 with",
        "Hit Points": "40 (9d8)",
        "Speed": "30 ft.",
        "Saving Throws": "Int +6, Wis +4",
        "Skills": "Arcana +6, History +6",
        "Senses": "passive Perception 11",
        "Languages": "any four languages",
        "Challenge": "6 (2300 XP)",
        "STR": "9 (-1)",
        "DEX": "14 (+2)",
        "CON": "11 (+0)",
        "INT": "17 (+3)",
        "WIS": "12 (+1)",
        "CHA": "11 (+0)",
        "features": [
            "Spellcasting. The mage is a 9th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 14, +6 to hit with spell attacks). The mage has the following wizard spells prepared:"
        ],
        "Actions": [
            "Dagger.Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target.Hit: 4 (1d4 + 2) piercing damage."
        ]
    },
    "magma-mephit": {
        "name": "Magma Mephit",
        "type": "Small elemental",
        "alignment": "neutral evil",
        "Armor Class": "11",
        "Hit Points": "22 (5d6 + 5)",
        "Speed": "30 ft., fly 30 ft.",
        "Skills": "Stealth +3",
        "Damage Vulnerabilities": "cold",
        "Damage Immunities": "fire, poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Ignan, Terran",
        "Challenge": "1/2 (100 XP)",
        "STR": "8 (-1)",
        "DEX": "12 (+1)",
        "CON": "12 (+1)",
        "INT": "7 (-2)",
        "WIS": "10 (+0)",
        "CHA": "10 (+0)",
        "features": [
            "Death Burst. When the mephit dies, it explodes in a burst of lava. Each creature within 5 feet of it must make a DC 11 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on a successful one.",
            "False Appearance. While the mephit remains motionless, it is indistinguishable from an ordinary mound of magma.",
            "Innate Spellcasting (1/Day). The mephit can innately castheat metal(spell save DC 10), requiring no material components. Its innate spellcasting ability is Charisma."
        ],
        "Actions": [
            "Claws.Melee Weapon Attack: +3 to hit, reach 5 ft., one creature.Hit: 3 (1d4 + 1) slashing damage plus 2 (1d4) fire damage.",
            "Fire Breath (Recharge 6). The mephit exhales a 15-foot cone of fire. Each creature in that area must make a DC 11 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "magmin": {
        "name": "Magmin",
        "type": "Small elemental",
        "alignment": "chaotic neutral",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "9 (2d6 + 2)",
        "Speed": "30 ft.",
        "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "fire",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Ignan",
        "Challenge": "1/2 (100 XP)",
        "STR": "7 (-2)",
        "DEX": "15 (+2)",
        "CON": "12 (+1)",
        "INT": "8 (-1)",
        "WIS": "11 (+0)",
        "CHA": "10 (+0)",
        "features": [
            "Death Burst. When the magmin dies, it explodes in a burst of fire and magma. Each creature within 10 feet of it must make a DC 11 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on a successful one. Flammable objects that aren't being worn or carried in that area are ignited.",
            "Ignited Illumination. As a bonus action, the magmin can set itself ablaze or extinguish its flames. While ablaze, the magmin sheds bright light in a 10-foot radius and dim light for an additional 10 feet."
        ],
        "Actions": [
            "Touch.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 7 (2d6) fire damage. If the target is a creature or a flammable object, it ignites. Until a creature takes an action to douse the fire, the target takes 3 (1d6) fire damage at the end of each of its turns."
        ]
    },
    "mammoth": {
        "name": "Mammoth",
        "type": "Huge beast",
        "alignment": "unaligned",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "126 (11d12 + 55)",
        "Speed": "40 ft.",
        "Senses": "passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "6 (2300 XP)",
        "STR": "24 (+7)",
        "DEX": "9 (-1)",
        "CON": "21 (+5)",
        "INT": "3 (-4)",
        "WIS": "11 (+0)",
        "CHA": "6 (-2)",
        "features": [
            "Trampling Charge. If the mammoth moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 18 Strength saving throw or be knocked prone. If the target is prone, the mammoth can make one stomp attack against it as a bonus action."
        ],
        "Actions": [
            "Gore.Melee Weapon Attack: +10 to hit, reach 10 ft., one target.Hit: 25 (4d8 + 7) piercing damage.",
            "Stomp.Melee Weapon Attack: +10 to hit, reach 5 ft., one prone creature.Hit: 29 (4d10 + 7) bludgeoning damage."
        ]
    },
    "manticore": {
        "name": "Manticore",
        "type": "Large monstrosity",
        "alignment": "lawful evil",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "68 (8d10 + 24)",
        "Speed": "30 ft., fly 50 ft.",
        "Senses": "darkvision 60 ft., passive Perception 11",
        "Languages": "Common",
        "Challenge": "3 (700 XP)",
        "STR": "17 (+3)",
        "DEX": "16 (+3)",
        "CON": "17 (+3)",
        "INT": "7 (-2)",
        "WIS": "12 (+1)",
        "CHA": "8 (-1)",
        "features": [
            "Tail Spike Regrowth. The manticore has twenty-four tail spikes. Used spikes regrow when the manticore finishes a long rest."
        ],
        "Actions": [
            "Multiattack. The manticore makes three attacks: one with its bite and two with its claws or three with its tail spikes.",
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 7 (1d8 + 3) piercing damage.",
            "Claw.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 6 (1d6 + 3) slashing damage.",
            "Tail Spike.Ranged Weapon Attack: +5 to hit, range 100/200 ft., one target.Hit: 7 (1d8 + 3) piercing damage."
        ]
    },
    "marilith": {
        "name": "Marilith",
        "type": "Large fiend (Demon)",
        "alignment": "chaotic evil",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "189 (18d10 + 90)",
        "Speed": "40 ft.",
        "Saving Throws": "Str +9, Con +10, Wis +8, Cha +10",
        "Damage Resistances": "cold, fire, lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "truesight 120 ft., passive Perception 13",
        "Languages": "Abyssal, telepathy 120 ft.",
        "Challenge": "16 (15000 XP)",
        "STR": "18 (+4)",
        "DEX": "20 (+5)",
        "CON": "20 (+5)",
        "INT": "18 (+4)",
        "WIS": "16 (+3)",
        "CHA": "20 (+5)",
        "Reactions": [
            "Parry. The marilith adds 5 to its AC against one melee attack that would hit it. To do so, the marilith must see the attacker and be wielding a melee weapon."
        ],
        "features": [
            "Magic Resistance. The marilith has advantage on saving throws against spells and other magical effects.",
            "Magic Weapons. The marilith's weapon attacks are magical.",
            "Reactive. The marilith can take one reaction on every turn in a combat."
        ],
        "Actions": [
            "Multiattack. The marilith makes seven attacks: six with its longswords and one with its tail.",
            "Longsword.Melee Weapon Attack: +9 to hit, reach 5 ft., one target.Hit: 13 (2d8 + 4) slashing damage.",
            "Tail.Melee Weapon Attack: +9 to hit, reach 10 ft., one creature.Hit: 15 (2d10 + 4) bludgeoning damage. If the target is Medium or smaller, it is grappled (escape DC 19). Until this grapple ends, the target is restrained, the marilith can automatically hit the target with its tail, and the marilith can't make tail attacks against other targets.",
            "Teleport. The marilith magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see."
        ]
    },
    "mastiff": {
        "name": "Mastiff",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "5 (1d8 + 1)",
        "Speed": "40 ft.",
        "Skills": "Perception +3",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "1/8 (25 XP)",
        "STR": "13 (+1)",
        "DEX": "14 (+2)",
        "CON": "12 (+1)",
        "INT": "3 (-4)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Keen Hearing and Smell. The mastiff has advantage on Wisdom (Perception) checks that rely on hearing or smell."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 4 (1d6 + 1) piercing damage. If the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone."
        ]
    },
    "medusa": {
        "name": "Medusa",
        "type": "Medium monstrosity",
        "alignment": "lawful evil",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "127 (17d8 + 51)",
        "Speed": "30 ft.",
        "Skills": "Deception +5, Insight +4, Perception +4, Stealth +5",
        "Senses": "darkvision 60 ft., passive Perception 14",
        "Languages": "Common",
        "Challenge": "6 (2300 XP)",
        "STR": "10 (+0)",
        "DEX": "15 (+2)",
        "CON": "16 (+3)",
        "INT": "12 (+1)",
        "WIS": "13 (+1)",
        "CHA": "15 (+2)",
        "features": [
            "Petrifying Gaze. When a creature that can see the medusa's eyes starts its turn within 30 feet of the medusa, the medusa can force it to make a DC 14 Constitution saving throw if the medusa isn't incapacitated and can see the creature. If the saving throw fails by 5 or more, the creature is instantly petrified. Otherwise, a creature that fails the save begins to turn to stone and is restrained. The restrained creature must repeat the saving throw at the end of its next turn, becoming petrified on a failure or ending the effect on a success. The petrification lasts until the creature is freed by thegreater restorationspell or other magic. Unless surprised, a creature can avert its eyes to avoid the saving throw at the start of its turn. If the creature does so, it can't see the medusa until the start of its next turn, when it can avert its eyes again. If the creature looks at the medusa in the meantime, it must immediately make the save. If the medusa sees itself reflected on a polished surface within 30 feet of it and in an area of bright light, the medusa is, due to its curse, affected by its own gaze."
        ],
        "Actions": [
            "Multiattack. The medusa makes either three melee attacks -one with its snake hair and two with its shortsword- or two ranged attacks with its longbow.",
            "Snake Hair.Melee Weapon Attack: +5 to hit, reach 5 ft., one creature.Hit: 4 (1d4 + 2) piercing damage plus 14 (4d6) poison damage.",
            "Shortsword.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) piercing damage.",
            "Longbow.Ranged Weapon Attack: +5 to hit, range 150/600 ft., one target.Hit: 6 (1d8 + 2) piercing damage plus 7 (2d6) poison damage."
        ]
    },
    "merfolk": {
        "name": "Merfolk",
        "type": "Medium humanoid (Merfolk)",
        "alignment": "neutral",
        "Armor Class": "11",
        "Hit Points": "11 (2d8 + 2)",
        "Speed": "10 ft., swim 40 ft.",
        "Skills": "Perception +2",
        "Senses": "passive Perception 12",
        "Languages": "Aquan, Common",
        "Challenge": "1/8 (25 XP)",
        "STR": "10 (+0)",
        "DEX": "13 (+1)",
        "CON": "12 (+1)",
        "INT": "11 (+0)",
        "WIS": "11 (+0)",
        "CHA": "12 (+1)",
        "features": [
            "Amphibious. The merfolk can breathe air and water."
        ],
        "Actions": [
            "Spear.Melee or Ranged Weapon Attack: +2 to hit, reach 5 ft. or range 20/60 ft., one target.Hit: 3 (1d6) piercing damage, or 4 (1d8) piercing damage if used with two hands to make a melee attack."
        ]
    },
    "merrow": {
        "name": "Merrow",
        "type": "Large monstrosity",
        "alignment": "chaotic evil",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "45 (6d10 + 12)",
        "Speed": "10 ft., swim 40 ft.",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Abyssal, Aquan",
        "Challenge": "2 (450 XP)",
        "STR": "18 (+4)",
        "DEX": "10 (+0)",
        "CON": "15 (+2)",
        "INT": "8 (-1)",
        "WIS": "10 (+0)",
        "CHA": "9 (-1)",
        "features": [
            "Amphibious. The merrow can breathe air and water."
        ],
        "Actions": [
            "Multiattack. The merrow makes two attacks: one with its bite and one with its claws or harpoon.",
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 8 (1d8 + 4) piercing damage.",
            "Claws.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 9 (2d4 + 4) slashing damage.",
            "Harpoon.Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target.Hit: 11 (2d6 + 4) piercing damage. If the target is a Huge or smaller creature, it must succeed on a Strength contest against the merrow or be pulled up to 20 feet toward the merrow."
        ]
    },
    "mezzoloth": {
        "name": "Mezzoloth",
        "type": "Medium fiend (Yugoloth)",
        "alignment": "neutral evil",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "75 (10d8 + 30)",
        "Speed": "40 ft.",
        "Skills": "Perception +3",
        "Damage Resistances": "cold, fire, lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "acid, poison",
        "Condition Immunities": "poisoned",
        "Senses": "blindsight 60 ft., darkvision 60 ft., passive Perception 13",
        "Languages": "Abyssal, Infernal, telepathy 60 ft.",
        "Challenge": "5 (1800 XP)",
        "STR": "18 (+4)",
        "DEX": "11 (+0)",
        "CON": "16 (+3)",
        "INT": "7 (-2)",
        "WIS": "10 (+0)",
        "CHA": "11 (+0)",
        "features": [
            "Innate Spellcasting. The mezzoloth's innate spellcasting ability is Charisma (spell save DC 11). The mezzoloth can innately cast the following spells, requiring no material components:",
            "Magic Resistance. The mezzoloth has advantage on saving throws against spells and other magical effects.",
            "Magic Weapons. The mezzoloth's weapon attacks are magical."
        ],
        "Actions": [
            "Multiattack. The mezzoloth makes two attacks: one with its claws and one with its trident.",
            "Claws.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 9 (2d4 + 4) slashing damage.",
            "Trident.Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 20/60 ft., one target.Hit: 7 (1d6 + 4) piercing damage, or 8 (1d8 + 4) piercing damage when held with two claws and used to make a melee attack.",
            "Teleport. The mezzoloth magically teleports, along with any equipment it is wearing or carrying, up to 60 feet to an unoccupied space it can see."
        ]
    },
    "mimic": {
        "name": "Mimic",
        "type": "Medium monstrosity (Shapechanger)",
        "alignment": "neutral",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "58 (9d8 + 18)",
        "Speed": "15 ft.",
        "Skills": "Stealth +5",
        "Damage Immunities": "acid",
        "Condition Immunities": "prone",
        "Senses": "darkvision 60 ft., passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "17 (+3)",
        "DEX": "12 (+1)",
        "CON": "15 (+2)",
        "INT": "5 (-3)",
        "WIS": "13 (+1)",
        "CHA": "8 (-1)",
        "features": [
            "Shapechanger. The mimic can use its action to polymorph into an object or back into its true, amorphous form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.",
            "Adhesive (Object Form Only). The mimic adheres to anything that touches it. A Huge or smaller creature adhered to the mimic is also grappled by it (escape DC 13). Ability checks made to escape this grapple have disadvantage.",
            "False Appearance (Object Form Only). While the mimic remains motionless, it is indistinguishable from an ordinary object.",
            "Grappler. The mimic has advantage on attack rolls against any creature grappled by it."
        ],
        "Actions": [
            "Pseudopod.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 7 (1d8 + 3) bludgeoning damage. If the mimic is in object form, the target is subjected to its Adhesive trait.",
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 7 (1d8 + 3) piercing damage plus 4 (1d8) acid damage."
        ]
    },
    "minotaur": {
        "name": "Minotaur",
        "type": "Large monstrosity",
        "alignment": "chaotic evil",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "76 (9d10 + 27)",
        "Speed": "40 ft.",
        "Skills": "Perception +7",
        "Senses": "darkvision 60 ft., passive Perception 17",
        "Languages": "Abyssal",
        "Challenge": "3 (700 XP)",
        "STR": "18 (+4)",
        "DEX": "11 (+0)",
        "CON": "16 (+3)",
        "INT": "6 (-2)",
        "WIS": "16 (+3)",
        "CHA": "9 (-1)",
        "features": [
            "Charge. If the minotaur moves at least 10 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 9 (2d8) piercing damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or be pushed up to 10 feet away and knocked prone.",
            "Labyrinthine Recall. The minotaur can perfectly recall any path it has traveled.",
            "Reckless. At the start of its turn, the minotaur can gain advantage on all melee weapon attack rolls it makes during that turn, but attack rolls against it have advantage until the start of its next turn."
        ],
        "Actions": [
            "Greataxe.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 17 (2d12 + 4) slashing damage.",
            "Gore.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 13 (2d8 + 4) piercing damage."
        ]
    },
    "minotaur-skeleton": {
        "name": "Minotaur Skeleton",
        "type": "Large undead",
        "alignment": "lawful evil",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "67 (9d10 + 18)",
        "Speed": "40 ft.",
        "Damage Vulnerabilities": "bludgeoning",
        "Damage Immunities": "poison",
        "Condition Immunities": "exhaustion, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 9",
        "Languages": "understands Abyssal but can't speak",
        "Challenge": "2 (450 XP)",
        "STR": "18 (+4)",
        "DEX": "11 (+0)",
        "CON": "15 (+2)",
        "INT": "6 (-2)",
        "WIS": "8 (-1)",
        "CHA": "5 (-3)",
        "features": [
            "Charge. If the skeleton moves at least 10 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 9 (2d8) piercing damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or be pushed up to 10 feet away and knocked prone."
        ],
        "Actions": [
            "Greataxe.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 17 (2d12 + 4) slashing damage.",
            "Gore.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 13 (2d8 + 4) piercing damage."
        ]
    },
    "mule": {
        "name": "Mule",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "10",
        "Hit Points": "11 (2d8 + 2)",
        "Speed": "40 ft.",
        "Senses": "passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/8 (25 XP)",
        "STR": "14 (+2)",
        "DEX": "10 (+0)",
        "CON": "13 (+1)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "5 (-3)",
        "features": [
            "Beast of Burden. The mule is considered to be a Large animal for the purpose of determining its carrying capacity.",
            "Sure-Footed. The mule has advantage on Strength and Dexterity saving throws made against effects that would knock it prone."
        ],
        "Actions": [
            "Hooves.Melee Weapon Attack: +2 to hit, reach 5 ft., one target.Hit: 4 (1d4 + 2) bludgeoning damage."
        ]
    },
    "mummy": {
        "name": "Mummy",
        "type": "Medium undead",
        "alignment": "lawful evil",
        "Armor Class": "11 (natural armor)",
        "Hit Points": "58 (9d8 + 18)",
        "Speed": "20 ft.",
        "Saving Throws": "Wis +2",
        "Damage Vulnerabilities": "fire",
        "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "necrotic, poison",
        "Condition Immunities": "charmed, exhaustion, frightened, paralyzed, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "the languages it knew in life",
        "Challenge": "3 (700 XP)",
        "STR": "16 (+3)",
        "DEX": "8 (-1)",
        "CON": "15 (+2)",
        "INT": "6 (-2)",
        "WIS": "10 (+0)",
        "CHA": "12 (+1)",
        "features": [],
        "Actions": [
            "Multiattack. The mummy can use its Dreadful Glare and makes one attack with its rotting fist.",
            "Rotting Fist.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) bludgeoning damage plus 10 (3d6) necrotic damage. If the target is a creature, it must succeed on a DC 12 Constitution saving throw or be cursed with mummy rot. The cursed target can't regain hit points, and its hit point maximum decreases by 10 (3d6) for every 24 hours that elapse. If the curse reduces the target's hit point maximum to 0, the target dies, and its body turns to dust. The curse lasts until removed by theremove cursespell or other magic.",
            "Dreadful Glare. The mummy targets one creature it can see within 60 feet of it. If the target can see the mummy, it must succeed on a DC 11 Wisdom saving throw against this magic or become frightened until the end of the mummy's next turn. If the target fails the saving throw by 5 or more, it is also paralyzed for the same duration. A target that succeeds on the saving throw is immune to the Dreadful Glare of all mummies (but not mummy lords) for the next 24 hours."
        ]
    },
    "mummy-lord": {
        "name": "Mummy Lord",
        "type": "Medium undead",
        "alignment": "lawful evil",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "97 (13d8 + 39)",
        "Speed": "20 ft.",
        "Saving Throws": "Con +8, Int +5, Wis +9, Cha +8",
        "Skills": "History +5, Religion +5",
        "Damage Vulnerabilities": "fire",
        "Damage Immunities": "necrotic, poison; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Condition Immunities": "charmed, exhaustion, frightened, paralyzed, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 14",
        "Languages": "the languages it knew in life",
        "Challenge": "15 (13000 XP)",
        "STR": "18 (+4)",
        "DEX": "10 (+0)",
        "CON": "17 (+3)",
        "INT": "11 (+0)",
        "WIS": "18 (+4)",
        "CHA": "16 (+3)",
        "Legendary actions": [
            "The mummy lord can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The mummy lord regains spent legendary actions at the start of its turn.",
            "Attack. The mummy lord makes one attack with its rotting fist or uses its Dreadful Glare.",
            "Blinding Dust. Blinding dust and sand swirls magically around the mummy lord. Each creature within 5 feet of the mummy lord must succeed on a DC 16 Constitution saving throw or be blinded until the end of the creature's next turn.",
            "Blasphemous Word (Costs 2 Actions). The mummy lord utters a blasphemous word. Each non-undead creature within 10 feet of the mummy lord that can hear the magical utterance must succeed on a DC 16 Constitution saving throw or be stunned until the end of the mummy lord's next turn.",
            "Channel Negative Energy (Costs 2 Actions). The mummy lord magically unleashes negative energy. Creatures within 60 feet of the mummy lord, including ones behind barriers and around corners, can't regain hit points until the end of the mummy lord's next turn.",
            "Whirlwind of Sand (Costs 2 Actions). The mummy lord magically transforms into a whirlwind of sand, moves up to 60 feet, and reverts to its normal form. While in whirlwind form, the mummy lord is immune to all damage, and it can't be grappled, petrified, knocked prone, restrained, or stunned. Equipment worn or carried by the mummy lord remain in its possession."
        ],
        "features": [
            "Magic Resistance. The mummy lord has advantage on saving throws against spells and other magical effects.",
            "Rejuvenation. A destroyed mummy lord gains a new body in 24 hours if its heart is intact, regaining all its hit points and becoming active again. The new body appears within 5 feet of the mummy lord's heart.",
            "Spellcasting. The mummy lord is a 10th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 17, +9 to hit with spell attacks). The mummy lord has the following cleric spells prepared:"
        ],
        "Actions": [
            "Multiattack. The mummy can use its Dreadful Glare and makes one attack with its rotting fist.",
            "Rotting Fist.Melee Weapon Attack: +9 to hit, reach 5 ft., one target.Hit: 14 (3d6 + 4) bludgeoning damage plus 21 (6d6) necrotic damage. If the target is a creature, it must succeed on a DC 16 Constitution saving throw or be cursed with mummy rot. The cursed target can't regain hit points, and its hit point maximum decreases by 10 (3d6) for every 24 hours that elapse. If the curse reduces the target's hit point maximum to 0, the target dies, and its body turns to dust. The curse lasts until removed by theremove cursespell or other magic.",
            "Dreadful Glare. The mummy lord targets one creature it can see within 60 feet of it. If the target can see the mummy lord, it must succeed on a DC 16 Wisdom saving throw against this magic or become frightened until the end of the mummy's next turn. If the target fails the saving throw by 5 or more, it is also paralyzed for the same duration. A target that succeeds on the saving throw is immune to the Dreadful Glare of all mummies and mummy lords for the next 24 hours."
        ]
    },
    "myconid-adult": {
        "name": "Myconid adult",
        "type": "Medium plant",
        "alignment": "lawful neutral",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "22 (4d8 + 4)",
        "Speed": "20 ft.",
        "Senses": "darkvision 120 ft., passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "10 (+0)",
        "DEX": "10 (+0)",
        "CON": "12 (+1)",
        "INT": "10 (+0)",
        "WIS": "13 (+1)",
        "CHA": "7 (-2)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "myconid-sovereign": {
        "name": "Myconid Sovereign",
        "type": "Large plant",
        "alignment": "lawful neutral",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "60 (8d10 + 16)",
        "Speed": "30 ft.",
        "Senses": "darkvision 120 ft., passive Perception 12",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "12 (+1)",
        "DEX": "10 (+0)",
        "CON": "14 (+2)",
        "INT": "13 (+1)",
        "WIS": "15 (+2)",
        "CHA": "10 (+0)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "myconid-sprout": {
        "name": "Myconid sprout",
        "type": "Small plant",
        "alignment": "lawful neutral",
        "Armor Class": "10",
        "Hit Points": "7 (2d6)",
        "Speed": "10 ft.",
        "Senses": "darkvision 120 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "8 (-1)",
        "DEX": "10 (+0)",
        "CON": "10 (+0)",
        "INT": "8 (-1)",
        "WIS": "11 (+0)",
        "CHA": "5 (-3)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "nalfeshnee": {
        "name": "Nalfeshnee",
        "type": "Large fiend (Demon)",
        "alignment": "chaotic evil",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "184 (16d10 + 96)",
        "Speed": "20 ft., fly 30 ft.",
        "Saving Throws": "Con +11, Int +9, Wis +6, Cha +7",
        "Damage Resistances": "cold, fire, lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "truesight 120 ft., passive Perception 11",
        "Languages": "Abyssal, telepathy 120 ft.",
        "Challenge": "13 (10000 XP)",
        "STR": "21 (+5)",
        "DEX": "10 (+0)",
        "CON": "22 (+6)",
        "INT": "19 (+4)",
        "WIS": "12 (+1)",
        "CHA": "15 (+2)",
        "features": [
            "Magic Resistance. The nalfeshnee has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack. The nalfeshnee uses Horror Nimbus if it can. It then makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +10 to hit, reach 5 ft., one target.Hit: 32 (5d10 + 5) piercing damage.",
            "Claw.Melee Weapon Attack: +10 to hit, reach 10 ft., one target.Hit: 15 (3d6 + 5) slashing damage.",
            "Horror Nimbus (Recharge 5-6). The nalfeshnee magically emits scintillating, multicolored light. Each creature within 15 feet of the nalfeshnee that can see the light must succeed on a DC 15 Wisdom saving throw or be frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the nalfeshnee's Horror Nimbus for the next 24 hours.",
            "Teleport. The nalfeshnee magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see."
        ]
    },
    "noble": {
        "name": "Noble",
        "type": "Medium humanoid (any race)",
        "alignment": "any alignment",
        "Armor Class": "15 (breastplate)",
        "Hit Points": "9 (2d8)",
        "Speed": "30 ft.",
        "Skills": "Deception +5, Insight +4, Persuasion +5",
        "Senses": "passive Perception 12",
        "Languages": "any two languages",
        "Challenge": "1/8 (25 XP)",
        "STR": "11 (+0)",
        "DEX": "12 (+1)",
        "CON": "11 (+0)",
        "INT": "12 (+1)",
        "WIS": "14 (+2)",
        "CHA": "16 (+3)",
        "Reactions": [
            "Parry. The noble adds 2 to its AC against one melee attack that would hit it. To do so, the noble must see the attacker and be wielding a melee weapon."
        ],
        "features": [],
        "Actions": [
            "Rapier.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 5 (1d8 + 1) piercing damage."
        ]
    },
    "ochre-jelly": {
        "name": "Ochre Jelly",
        "type": "Large ooze",
        "alignment": "unaligned",
        "Armor Class": "8",
        "Hit Points": "45 (6d10 + 12)",
        "Speed": "10 ft., climb 10 ft.",
        "Damage Resistances": "acid",
        "Damage Immunities": "lightning, slashing",
        "Condition Immunities": "blinded, charmed, deafened, exhaustion, frightened, prone",
        "Senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 8",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "15 (+2)",
        "DEX": "6 (-2)",
        "CON": "14 (+2)",
        "INT": "2 (-4)",
        "WIS": "6 (-2)",
        "CHA": "1 (-5)",
        "Reactions": [
            "Split. When a jelly that is Medium or larger is subjected to lightning or slashing damage, it splits into two new jellies if it has at least 10 hit points. Each new jelly has hit points equal to half the original jelly's, rounded down. New jellies are one size smaller than the original jelly."
        ],
        "features": [
            "Amorphous. The jelly can move through a space as narrow as 1 inch wide without squeezing.",
            "Spider Climb. The jelly can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
        ],
        "Actions": [
            "Pseudopod.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 9 (2d6 + 2) bludgeoning damage plus 3 (1d6) acid damage."
        ]
    },
    "octopus": {
        "name": "Octopus",
        "type": "Small beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "3 (1d6)",
        "Speed": "5 ft., swim 30 ft.",
        "Skills": "Perception +2, Stealth +4",
        "Senses": "darkvision 30 ft., passive Perception 12",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "4 (-3)",
        "DEX": "15 (+2)",
        "CON": "11 (+0)",
        "INT": "3 (-4)",
        "WIS": "10 (+0)",
        "CHA": "4 (-3)",
        "features": [
            "Hold Breath. While out of water, the octopus can hold its breath for 30 minutes.",
            "Underwater Camouflage. The octopus has advantage on Dexterity (Stealth) checks made while underwater.",
            "Water Breathing. The octopus can breathe only underwater."
        ],
        "Actions": [
            "Tentacles.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 1 bludgeoning damage, and the target is grappled (escape DC 10). Until this grapple ends, the octopus can't use its tentacles on another target.",
            "Ink Cloud (Recharges after a Short or Long Rest). A 5-foot-radius cloud of ink extends all around the octopus if it is underwater. The area is heavily obscured for 1 minute, although a significant current can disperse the ink. After releasing the ink, the octopus can use the Dash action as a bonus action."
        ]
    },
    "ogre": {
        "name": "Ogre",
        "type": "Large giant",
        "alignment": "chaotic evil",
        "Armor Class": "11 (hide armor)",
        "Hit Points": "59 (7d10 + 21)",
        "Speed": "40 ft.",
        "Senses": "darkvision 60 ft., passive Perception 8",
        "Languages": "Common, Giant",
        "Challenge": "2 (450 XP)",
        "STR": "19 (+4)",
        "DEX": "8 (-1)",
        "CON": "16 (+3)",
        "INT": "5 (-3)",
        "WIS": "7 (-2)",
        "CHA": "7 (-2)",
        "features": [],
        "Actions": [
            "Greatclub.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 13 (2d8 + 4) bludgeoning damage.",
            "Javelin.Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 30/120 ft., one target.Hit: 11 (2d6 + 4) piercing damage."
        ]
    },
    "ogre-zombie": {
        "name": "Ogre Zombie",
        "type": "Large undead",
        "alignment": "neutral evil",
        "Armor Class": "8",
        "Hit Points": "85 (9d10 + 36)",
        "Speed": "30 ft.",
        "Saving Throws": "Wis +0",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 60 ft., passive Perception 8",
        "Languages": "understands Common and Giant but can't speak",
        "Challenge": "2 (450 XP)",
        "STR": "19 (+4)",
        "DEX": "6 (-2)",
        "CON": "18 (+4)",
        "INT": "3 (-4)",
        "WIS": "6 (-2)",
        "CHA": "5 (-3)",
        "features": [
            "Undead Fortitude. If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie drops to 1 hit point instead."
        ],
        "Actions": [
            "Morningstar.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 13 (2d8 + 4) bludgeoning damage."
        ]
    },
    "oni": {
        "name": "Oni",
        "type": "Large giant",
        "alignment": "lawful evil",
        "Armor Class": "16 (chain mail)",
        "Hit Points": "110 (13d10 + 39)",
        "Speed": "30 ft., fly 30 ft.",
        "Saving Throws": "Dex +3, Con +6, Wis +4, Cha +5",
        "Skills": "Arcana +5, Deception +8, Perception +4",
        "Senses": "darkvision 60 ft., passive Perception 14",
        "Languages": "Common, Giant",
        "Challenge": "7 (2900 XP)",
        "STR": "19 (+4)",
        "DEX": "11 (+0)",
        "CON": "16 (+3)",
        "INT": "14 (+2)",
        "WIS": "12 (+1)",
        "CHA": "15 (+2)",
        "features": [
            "Innate Spellcasting. The oni's innate spellcasting ability is Charisma (spell save DC 13). The oni can innately cast the following spells, requiring no material components:",
            "Magic Weapons. The oni's weapon attacks are magical.",
            "Regeneration. The oni regains 10 hit points at the start of its turn if it has at least 1 hit point."
        ],
        "Actions": [
            "Multiattack. The oni makes two attacks, either with its claws or its glaive.",
            "Claw (Oni Form Only).Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 8 (1d8 + 4) slashing damage.",
            "Glaive.Melee Weapon Attack: +7 to hit, reach 10 ft., one target.Hit: 15 (2d10 + 4) slashing damage, or 9 (1d10 + 4) slashing damage in Small or Medium form.",
            "Change Shape. The oni magically polymorphs into a Small or Medium humanoid, into a Large giant, or back into its true form. Other than its size, its statistics are the same in each form. The only equipment that is transformed is its glaive, which shrinks so that it can be wielded in humanoid form. If the oni dies, it reverts to its true form, and its glaive reverts to its normal size."
        ]
    },
    "orc": {
        "name": "Orc",
        "type": "Medium humanoid (Orc)",
        "alignment": "chaotic evil",
        "Armor Class": "13 (hide armor)",
        "Hit Points": "15 (2d8 + 6)",
        "Speed": "30 ft.",
        "Skills": "Intimidation +2",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Common, Orc",
        "Challenge": "1/2 (100 XP)",
        "STR": "16 (+3)",
        "DEX": "12 (+1)",
        "CON": "16 (+3)",
        "INT": "7 (-2)",
        "WIS": "11 (+0)",
        "CHA": "10 (+0)",
        "features": [
            "Aggressive. As a bonus action, the orc can move up to its speed toward a hostile creature that it can see."
        ],
        "Actions": [
            "Greataxe.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 9 (1d12 + 3) slashing damage.",
            "Javelin.Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 30/120 ft., one target.Hit: 6 (1d6 + 3) piercing damage."
        ]
    },
    "orog": {
        "name": "Orog",
        "type": "Medium humanoid (Orc)",
        "alignment": "chaotic evil",
        "Armor Class": "18 (plate)",
        "Hit Points": "42 (5d8 + 20)",
        "Speed": "30 ft.",
        "Skills": "Intimidation +5, Survival +2",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Common, Orc",
        "Challenge": "2 (450 XP)",
        "STR": "18 (+4)",
        "DEX": "12 (+1)",
        "CON": "18 (+4)",
        "INT": "12 (+1)",
        "WIS": "11 (+0)",
        "CHA": "12 (+1)",
        "features": [
            "Aggressive. As a bonus action, the orog can move up to its speed toward a hostile creature that it can see."
        ],
        "Actions": [
            "Multiattack. The orog makes two greataxe attacks.",
            "Greataxe.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 10 (1d12 + 4) slashing damage.",
            "Javelin.Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 30/120 ft., one target.Hit: 7 (1d6 + 4) piercing damage."
        ]
    },
    "otyugh": {
        "name": "Otyugh",
        "type": "Large aberration",
        "alignment": "neutral",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "114 (12d10 + 48)",
        "Speed": "30 ft.",
        "Saving Throws": "Con +7",
        "Senses": "darkvision 120 ft., passive Perception 11",
        "Languages": "Otyugh",
        "Challenge": "5 (1800 XP)",
        "STR": "16 (+3)",
        "DEX": "11 (+0)",
        "CON": "19 (+4)",
        "INT": "6 (-2)",
        "WIS": "13 (+1)",
        "CHA": "6 (-2)",
        "features": [
            "Limited Telepathy. The otyugh can magically transmit simple messages and images to any creature within 120 feet of it that can understand a language. This form of telepathy doesn't allow the receiving creature to telepathically respond."
        ],
        "Actions": [
            "Multiattack. The otyugh makes three attacks: one with its bite and two with its tentacles.",
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 12 (2d8 + 3) piercing damage. If the target is a creature, it must succeed on a DC 15 Constitution saving throw against disease or become poisoned until the disease is cured. Every 24 hours that elapse, the target must repeat the saving throw, reducing its hit point maximum by 5 (1d10) on a failure. The disease is cured on a success. The target dies if the disease reduces its hit point maximum to 0. This reduction to the target's hit point maximum lasts until the disease is cured.",
            "Tentacle.Melee Weapon Attack: +6 to hit, reach 10 ft., one target.Hit: 7 (1d8 + 3) bludgeoning damage plus 4 (1d8) piercing damage. If the target is Medium or smaller, it is grappled (escape DC 13) and restrained until the grapple ends. The otyugh has two tentacles, each of which can grapple one target.",
            "Tentacle Slam. The otyugh slams creatures grappled by it into each other or a solid surface. Each creature must succeed on a DC 14 Constitution saving throw or take 10 (2d6 + 3) bludgeoning damage and be stunned until the end of the otyugh's next turn. On a successful save, the target takes half the bludgeoning damage and isn't stunned."
        ]
    },
    "owl": {
        "name": "Owl",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "11",
        "Hit Points": "1 (1d4 - 1)",
        "Speed": "5 ft., fly 60 ft.",
        "Skills": "Perception +3, Stealth +3",
        "Senses": "darkvision 120 ft., passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "3 (-4)",
        "DEX": "13 (+1)",
        "CON": "8 (-1)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Flyby. The owl doesn't provoke opportunity attacks when it flies out of an enemy's reach.",
            "Keen Hearing and Sight. The owl has advantage on Wisdom (Perception) checks that rely on hearing or sight."
        ],
        "Actions": [
            "Talons.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 1 slashing damage."
        ]
    },
    "owlbear": {
        "name": "Owlbear",
        "type": "Large monstrosity",
        "alignment": "unaligned",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "59 (7d10 + 21)",
        "Speed": "40 ft.",
        "Skills": "Perception +3",
        "Senses": "darkvision 60 ft., passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "3 (700 XP)",
        "STR": "20 (+5)",
        "DEX": "12 (+1)",
        "CON": "17 (+3)",
        "INT": "3 (-4)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Keen Sight and Smell. The owlbear has advantage on Wisdom (Perception) checks that rely on sight or smell."
        ],
        "Actions": [
            "Multiattack. The owlbear makes two attacks: one with its beak and one with its claws.",
            "Beak.Melee Weapon Attack: +7 to hit, reach 5 ft., one creature.Hit: 10 (1d10 + 5) piercing damage.",
            "Claws.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 14 (2d8 + 5) slashing damage."
        ]
    },
    "pegasus": {
        "name": "Pegasus",
        "type": "Large celestial",
        "alignment": "chaotic good",
        "Armor Class": "12",
        "Hit Points": "59 (7d10 + 21)",
        "Speed": "60 ft., fly 90 ft.",
        "Saving Throws": "Dex +4, Wis +4, Cha +3",
        "Skills": "Perception +6",
        "Senses": "passive Perception 16",
        "Languages": "understands Celestial, Common, Elvish, and Sylvan but can't speak",
        "Challenge": "2 (450 XP)",
        "STR": "18 (+4)",
        "DEX": "15 (+2)",
        "CON": "16 (+3)",
        "INT": "10 (+0)",
        "WIS": "15 (+2)",
        "CHA": "13 (+1)",
        "features": [],
        "Actions": [
            "Hooves.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) bludgeoning damage."
        ]
    },
    "pentadrone": {
        "name": "Pentadrone",
        "type": "Large construct",
        "alignment": "lawful neutral",
        "Armor Class": "16 (natural armor)",
        "Hit Points": "32 (5d10 + 5)",
        "Speed": "40 ft.",
        "Skills": "Perception +4",
        "Senses": "truesight 120 ft., passive Perception 14",
        "Languages": "Madron",
        "Challenge": "2 (450 XP)",
        "STR": "15 (+2)",
        "DEX": "14 (+2)",
        "CON": "12 (+1)",
        "INT": "10 (+0)",
        "WIS": "10 (+0)",
        "CHA": "13 (+1)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "peryton": {
        "name": "Peryton",
        "type": "Medium monstrosity",
        "alignment": "chaotic evil",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "33 (6d8 + 6)",
        "Speed": "20 ft., fly 60 ft.",
        "Skills": "Perception +5",
        "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "Senses": "passive Perception 15",
        "Languages": "understands Common and Elvish but can't speak",
        "Challenge": "2 (450 XP)",
        "STR": "16 (+3)",
        "DEX": "12 (+1)",
        "CON": "13 (+1)",
        "INT": "9 (-1)",
        "WIS": "12 (+1)",
        "CHA": "10 (+0)",
        "features": [
            "Dive Attack. If the peryton is flying and dives at least 30 feet straight toward a target and then hits it with a melee weapon attack, the attack deals an extra 9 (2d8) damage to the target.",
            "Flyby. The peryton doesn't provoke an opportunity attack when it flies out of an enemy's reach.",
            "Keen Sight and Smell. The peryton has advantage on Wisdom (Perception) checks that rely on sight or smell."
        ],
        "Actions": [
            "Multiattack. The peryton makes one gore attack and one talon attack.",
            "Gore.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 7 (1d8 + 3) piercing damage.",
            "Talons.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 8 (2d4 + 3) piercing damage."
        ]
    },
    "pirate": {
        "features": []
    },
    "pixie": {
        "name": "Pixie",
        "type": "Tiny fey",
        "alignment": "neutral good",
        "Armor Class": "15",
        "Hit Points": "1 (1d4 - 1)",
        "Speed": "10 ft., fly 30 ft.",
        "Skills": "Perception +4, Stealth +7",
        "Senses": "passive Perception 14",
        "Languages": "Sylvan",
        "Challenge": "1/4 (50 XP)",
        "STR": "2 (-4)",
        "DEX": "20 (+5)",
        "CON": "8 (-1)",
        "INT": "10 (+0)",
        "WIS": "14 (+2)",
        "CHA": "15 (+2)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "planetar": {
        "name": "Planetar",
        "type": "Large celestial",
        "alignment": "lawful good",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "200 (16d10 + 112)",
        "Speed": "40 ft., fly 120 ft.",
        "Saving Throws": "Con +12, Wis +11, Cha +12",
        "Skills": "Perception +11",
        "Damage Resistances": "radiant; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Condition Immunities": "charmed, exhaustion, frightened",
        "Senses": "truesight 120 ft., passive Perception 21",
        "Languages": "all, telepathy 120 ft.",
        "Challenge": "16 (15000 XP)",
        "STR": "24 (+7)",
        "DEX": "20 (+5)",
        "CON": "24 (+7)",
        "INT": "19 (+4)",
        "WIS": "22 (+6)",
        "CHA": "25 (+7)",
        "features": [
            "Angelic Weapons. The planetar's weapon attacks are magical. When the planetar hits with any weapon, the weapon deals an extra 5d8 radiant damage (included in the attack).",
            "Divine Awareness. The planetar knows if it hears a lie.",
            "Innate Spellcasting. The planetar's spellcasting ability is Charisma (spell save DC 20). The planetar can innately cast the following spells, requiring no material components:",
            "Magic Resistance. The planetar has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack. The planetar makes two melee attacks.",
            "Greatsword.Melee Weapon Attack: +12 to hit, reach 5 ft., one target.Hit: 21 (4d6 + 7) slashing damage plus 22 (5d8) radiant damage.",
            "Healing Touch (4/Day). The planetar touches another creature. The target magically regains 30 (6d8 + 3) hit points and is freed from any curse, disease, poison, blindness, or deafness."
        ]
    },
    "plesiosaurus": {
        "name": "Plesiosaurus",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "68 (8d10 + 24)",
        "Speed": "20 ft., swim 40 ft.",
        "Skills": "Perception +3, Stealth +4",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "18 (+4)",
        "DEX": "15 (+2)",
        "CON": "16 (+3)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "5 (-3)",
        "features": [
            "Hold Breath. The plesiosaurus can hold its breath for 1 hour."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +6 to hit, reach 10 ft., one target.Hit: 14 (3d6 + 4) piercing damage."
        ]
    },
    "poisonous-snake": {
        "name": "Poisonous Snake",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "13",
        "Hit Points": "2 (1d4)",
        "Speed": "30 ft., swim 30 ft.",
        "Senses": "blindsight 10 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/8 (25 XP)",
        "STR": "2 (-4)",
        "DEX": "16 (+3)",
        "CON": "11 (+0)",
        "INT": "1 (-5)",
        "WIS": "10 (+0)",
        "CHA": "3 (-4)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 1 piercing damage, and the target must make a DC 10 Constitution saving throw, taking 5 (2d4) poison damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "polar-bear": {
        "name": "Polar Bear",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "42 (5d10 + 15)",
        "Speed": "40 ft., swim 30 ft.",
        "Skills": "Perception +3",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "20 (+5)",
        "DEX": "10 (+0)",
        "CON": "16 (+3)",
        "INT": "2 (-4)",
        "WIS": "13 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Keen Smell. The bear has advantage on Wisdom (Perception) checks that rely on smell."
        ],
        "Actions": [
            "Multiattack. The bear makes two attacks: one with its bite and one with its claws.",
            "Bite.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 9 (1d8 + 5) piercing damage.",
            "Claws.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 12 (2d6 + 5) slashing damage."
        ]
    },
    "pony": {
        "name": "Pony",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "10",
        "Hit Points": "11 (2d8 + 2)",
        "Speed": "40 ft.",
        "Senses": "passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/8 (25 XP)",
        "STR": "15 (+2)",
        "DEX": "10 (+0)",
        "CON": "13 (+1)",
        "INT": "2 (-4)",
        "WIS": "11 (+0)",
        "CHA": "7 (-2)",
        "features": [],
        "Actions": [
            "Hooves.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 7 (2d4 + 2) bludgeoning damage."
        ]
    },
    "priest": {
        "name": "Priest",
        "type": "Medium humanoid (any race)",
        "alignment": "any alignment",
        "Armor Class": "13 (chain shirt)",
        "Hit Points": "27 (5d8 + 5)",
        "Speed": "30 ft.",
        "Skills": "Medicine +7, Persuasion +3, Religion +5",
        "Senses": "passive Perception 13",
        "Languages": "any two languages",
        "Challenge": "2 (450 XP)",
        "STR": "10 (+0)",
        "DEX": "10 (+0)",
        "CON": "12 (+1)",
        "INT": "13 (+1)",
        "WIS": "16 (+3)",
        "CHA": "13 (+1)",
        "features": [
            "Divine Eminence. As a bonus action, the priest can expend a spell slot to cause its melee weapon attacks to magically deal an extra 10 (3d6) radiant damage to a target on a hit. This benefit lasts until the end of the turn. If the priest expends a spell slot of 2nd level or higher, the extra damage increases by 1d6 for each level above 1st.",
            "Spellcasting. The priest is a 5th-level spellcaster. Its spellcasting ability is Wisdom (spell save DC 13, +5 to hit with spell attacks). The priest has the following cleric spells prepared:"
        ],
        "Actions": [
            "Mace.Melee Weapon Attack: +2 to hit, reach 5 ft., one target.Hit: 3 (1d6) bludgeoning damage."
        ]
    },
    "pseudodragon": {
        "name": "Pseudodragon",
        "type": "Tiny dragon",
        "alignment": "neutral good",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "7 (2d4 + 2)",
        "Speed": "15 ft., fly 60 ft.",
        "Skills": "Perception +3, Stealth +4",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 13",
        "Languages": "understands Common and Draconic but can't speak",
        "Challenge": "1/4 (50 XP)",
        "STR": "6 (-2)",
        "DEX": "15 (+2)",
        "CON": "13 (+1)",
        "INT": "10 (+0)",
        "WIS": "12 (+1)",
        "CHA": "10 (+0)",
        "features": [
            "Keen Senses. The pseudodragon has advantage on Wisdom (Perception) checks that rely on sight, hearing, or smell.",
            "Magic Resistance. The pseudodragon has advantage on saving throws against spells and other magical effects.",
            "Limited Telepathy. The pseudodragon can magically communicate simple ideas, emotions, and images telepathically with any creature within 100 feet of it that can understand a language."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 4 (1d4 + 2) piercing damage.",
            "Sting.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 4 (1d4 + 2) piercing damage, and the target must succeed on a DC 11 Constitution saving throw or become poisoned for 1 hour. If the saving throw fails by 5 or more, the target falls unconscious for the same duration, or until it takes damage or another creature uses an action to shake it awake."
        ]
    },
    "pterydactyl": {
        "features": []
    },
    "purple-worm": {
        "name": "Purple Worm",
        "type": "Gargantuan monstrosity",
        "alignment": "unaligned",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "247 (15d20 + 90)",
        "Speed": "50 ft., burrow 30 ft.",
        "Saving Throws": "Con +11, Wis +4",
        "Senses": "blindsight 30 ft., tremorsense 60 ft., passive Perception 9",
        "Languages": "\u2014",
        "Challenge": "15 (13000 XP)",
        "STR": "28 (+9)",
        "DEX": "7 (-2)",
        "CON": "22 (+6)",
        "INT": "1 (-5)",
        "WIS": "8 (-1)",
        "CHA": "4 (-3)",
        "features": [
            "Tunneler. The worm can burrow through solid rock at half its burrow speed and leaves a 10-foot-diameter tunnel in its wake."
        ],
        "Actions": [
            "Multiattack. The worm makes two attacks: one with its bite and one with its stinger.",
            "Bite.Melee Weapon Attack: +14 to hit, reach 10 ft., one target.Hit: 22 (3d8 + 9) piercing damage. If the target is a Large or smaller creature, it must succeed on a DC 19 Dexterity saving throw or be swallowed by the worm. A swallowed creature is blinded and restrained, it has total cover against attacks and other effects outside the worm, and it takes 21 (6d6) acid damage at the start of each of the worm's turns. If the worm takes 30 damage or more on a single turn from a creature inside it, the worm must succeed on a DC 21 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall prone in a space within 10 feet of the worm. If the worm dies, a swallowed creature is no longer restrained by it and can escape from the corpse by using 20 feet of movement, exiting prone.",
            "Tail Stinger.Melee Weapon Attack: +14 to hit, reach 10 ft., one creature.Hit: 19 (3d6 + 9) piercing damage, and the target must make a DC 19 Constitution saving throw, taking 42 (12d6) poison damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "quasit": {
        "name": "Quasit",
        "type": "Tiny Fiend (Demon",
        "alignment": "Shapechanger), chaotic evil",
        "Armor Class": "13",
        "Hit Points": "7 (3d4)",
        "Speed": "40 ft.",
        "Skills": "Stealth +5",
        "Damage Resistances": "cold, fire, lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 120 ft., passive Perception 10",
        "Languages": "Abyssal, Common",
        "Challenge": "1 (200 XP)",
        "STR": "5 (-3)",
        "DEX": "17 (+3)",
        "CON": "10 (+0)",
        "INT": "7 (-2)",
        "WIS": "10 (+0)",
        "CHA": "10 (+0)",
        "features": [
            "Shapechanger. The quasit can use its action to polymorph into a beast form that resembles a bat (speed 10 ft. fly 40 ft.), a centipede (40 ft., climb 40 ft.), or a toad (40 ft., swim 40 ft.), or back into its true form. Its statistics are the same in each form, except for the speed changes noted. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.",
            "Magic Resistance. The quasit has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Claws (Bite in Beast Form).Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d4 + 3) piercing damage, and the target must succeed on a DC 10 Constitution saving throw or take 5 (2d4) poison damage and become poisoned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.",
            "Scare (1/Day). One creature of the quasit's choice within 20 feet of it must succeed on a DC 10 Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the end of each of its turns, with disadvantage if the quasit is within line of sight, ending the effect on itself on a success.",
            "Invisibility. The quasit magically turns invisible until it attacks or uses Scare, or until its concentration ends (as if concentrating on a spell). Any equipment the quasit wears or carries is invisible with it."
        ]
    },
    "quipper": {
        "name": "Quipper",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "13",
        "Hit Points": "1 (1d4 - 1)",
        "Speed": "0 ft., swim 40 ft.",
        "Senses": "darkvision 60 ft., passive Perception 8",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "2 (-4)",
        "DEX": "16 (+3)",
        "CON": "9 (-1)",
        "INT": "1 (-5)",
        "WIS": "7 (-2)",
        "CHA": "2 (-4)",
        "features": [
            "Blood Frenzy. The quipper has advantage on melee attack rolls against any creature that doesn't have all its hit points.",
            "Water Breathing. The quipper can breathe only underwater."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 1 piercing damage."
        ]
    },
    "rakshasa": {
        "name": "Rakshasa",
        "type": "Medium fiend",
        "alignment": "lawful evil",
        "Armor Class": "16 (natural armor)",
        "Hit Points": "110 (13d8 + 52)",
        "Speed": "40 ft.",
        "Skills": "Deception +10, Insight +8",
        "Damage Vulnerabilities": "piercing from magic weapons wielded by good creatures",
        "Damage Immunities": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "Senses": "darkvision 60 ft., passive Perception 13",
        "Languages": "Common, Infernal",
        "Challenge": "13 (10000 XP)",
        "STR": "14 (+2)",
        "DEX": "17 (+3)",
        "CON": "18 (+4)",
        "INT": "13 (+1)",
        "WIS": "16 (+3)",
        "CHA": "20 (+5)",
        "features": [
            "Limited Magic Immunity. The rakshasa can't be affected or detected by spells of 6th level or lower unless it wishes to be. It has advantage on saving throws against all other spells and magical effects.",
            "Innate Spellcasting. The rakshasa's innate spellcasting ability is Charisma (spell save DC 18, +10 to hit with spell attacks). The rakshasa can innately cast the following spells, requiring no material components:"
        ],
        "Actions": [
            "Multiattack. The rakshasa makes two claw attacks.",
            "Claw.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 9 (2d6 + 2) slashing damage, and the target is cursed if it is a creature. The magical curse takes effect whenever the target takes a short or long rest, filling the target's thoughts with horrible images and dreams. The cursed target gains no benefit from finishing a short or long rest. The curse lasts until it is lifted by aremove cursespell or similar magic."
        ]
    },
    "rat": {
        "name": "Rat",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "10",
        "Hit Points": "1 (1d4 - 1)",
        "Speed": "20 ft.",
        "Senses": "darkvision 30 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "2 (-4)",
        "DEX": "11 (+0)",
        "CON": "9 (-1)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "4 (-3)",
        "features": [
            "Keen Smell. The rat has advantage on Wisdom (Perception) checks that rely on smell."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +0 to hit, reach 5 ft., one target.Hit: 1 piercing damage."
        ]
    },
    "raven": {
        "name": "Raven",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "1 (1d4 - 1)",
        "Speed": "10 ft., fly 50 ft.",
        "Skills": "Perception +3",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "2 (-4)",
        "DEX": "14 (+2)",
        "CON": "8 (-1)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "6 (-2)",
        "features": [
            "Mimicry. The raven can mimic simple sounds it has heard, such as a person whispering, a baby crying, or an animal chittering. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check."
        ],
        "Actions": [
            "Beak.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 1 piercing damage."
        ]
    },
    "red-dragon-wyrmling": {
        "name": "Red Dragon Wyrmling",
        "type": "Medium dragon (Chromatic)",
        "alignment": "chaotic evil",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "75 (10d8 + 30)",
        "Speed": "30 ft., climb 30 ft., fly 60 ft.",
        "Saving Throws": "Dex +2, Con +5, Wis +2, Cha +4",
        "Skills": "Perception +4, Stealth +2",
        "Damage Immunities": "fire",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 14",
        "Languages": "Draconic",
        "Challenge": "4 (1100 XP)",
        "STR": "19 (+4)",
        "DEX": "10 (+0)",
        "CON": "17 (+3)",
        "INT": "12 (+1)",
        "WIS": "11 (+0)",
        "CHA": "15 (+2)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 9 (1d10 + 4) piercing damage plus 3 (1d6) fire damage.",
            "Fire Breath (Recharge 5-6). The dragon exhales fire in a 15-foot cone. Each creature in that area must make a DC 13 Dexterity saving throw, taking 24 (7d6) fire damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "reef-shark": {
        "name": "Reef Shark",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "22 (4d8 + 4)",
        "Speed": "0 ft., swim 40 ft.",
        "Skills": "Perception +2",
        "Senses": "blindsight 30 ft., passive Perception 12",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "14 (+2)",
        "DEX": "13 (+1)",
        "CON": "13 (+1)",
        "INT": "1 (-5)",
        "WIS": "10 (+0)",
        "CHA": "4 (-3)",
        "features": [
            "Pack Tactics. The shark has advantage on an attack roll against a creature if at least one of the shark's allies is within 5 feet of the creature and the ally isn't incapacitated.",
            "Water Breathing. The shark can breathe only underwater."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 6 (1d8 + 2) piercing damage."
        ]
    },
    "remorhaz": {
        "name": "Remorhaz",
        "type": "Huge monstrosity",
        "alignment": "unaligned",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "195 (17d12 + 85)",
        "Speed": "30 ft., burrow 20 ft.",
        "Damage Immunities": "cold, fire",
        "Senses": "darkvision 60 ft., tremorsense 60 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "11 (7200 XP)",
        "STR": "24 (+7)",
        "DEX": "13 (+1)",
        "CON": "21 (+5)",
        "INT": "4 (-3)",
        "WIS": "10 (+0)",
        "CHA": "5 (-3)",
        "features": [
            "Heated Body. A creature that touches the remorhaz or hits it with a melee attack while within 5 feet of it takes 10 (3d6) fire damage."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +11 to hit, reach 10 ft., one target.Hit: 40 (6d10 + 7) piercing damage plus 10 (3d6) fire damage. If the target is a creature, it is grappled (escape DC 17). Until this grapple ends, the target is restrained, and the remorhaz can't bite another target.",
            "Swallow. The remorhaz makes one bite attack against a Medium or smaller creature it is grappling. If the attack hits, that creature takes the bite's damage and is swallowed, and the grapple ends. While swallowed, the creature is blinded and restrained, it has total cover against attacks and other effects outside the remorhaz, and it takes 21 (6d6) acid damage at the start of each of the remorhaz's turns. If the remorhaz takes 30 damage or more on a single turn from a creature inside it, the remorhaz must succeed on a DC 15 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall prone in a space within 10 feet of the remorhaz. If the remorhaz dies, a swallowed creature is no longer restrained by it and can escape from the corpse using 15 feet of movement, exiting prone."
        ]
    },
    "rhinoceros": {
        "name": "Rhinoceros",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "11 (natural armor)",
        "Hit Points": "45 (6d10 + 12)",
        "Speed": "40 ft.",
        "Senses": "passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "21 (+5)",
        "DEX": "8 (-1)",
        "CON": "15 (+2)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "6 (-2)",
        "features": [
            "Charge. If the rhinoceros moves at least 20 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 9 (2d8) bludgeoning damage. If the target is a creature, it must succeed on a DC 15 Strength saving throw or be knocked prone."
        ],
        "Actions": [
            "Gore.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 14 (2d8 + 5) bludgeoning damage."
        ]
    },
    "riding-horse": {
        "name": "Riding Horse",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "10",
        "Hit Points": "13 (2d10 + 2)",
        "Speed": "60 ft.",
        "Senses": "passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "16 (+3)",
        "DEX": "10 (+0)",
        "CON": "12 (+1)",
        "INT": "2 (-4)",
        "WIS": "11 (+0)",
        "CHA": "7 (-2)",
        "features": [],
        "Actions": [
            "Hooves.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 8 (2d4 + 3) bludgeoning damage."
        ]
    },
    "roc": {
        "name": "Roc",
        "type": "Gargantuan monstrosity",
        "alignment": "unaligned",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "248 (16d20 + 80)",
        "Speed": "20 ft., fly 120 ft.",
        "Saving Throws": "Dex +4, Con +9, Wis +4, Cha +3",
        "Skills": "Perception +4",
        "Senses": "passive Perception 14",
        "Languages": "\u2014",
        "Challenge": "11 (7200 XP)",
        "STR": "28 (+9)",
        "DEX": "10 (+0)",
        "CON": "20 (+5)",
        "INT": "3 (-4)",
        "WIS": "10 (+0)",
        "CHA": "9 (-1)",
        "features": [
            "Keen Sight. The roc has advantage on Wisdom (Perception) checks that rely on sight."
        ],
        "Actions": [
            "Multiattack. The roc makes two attacks: one with its beak and one with its talons.",
            "Beak.Melee Weapon Attack: +13 to hit, reach 10 ft., one target.Hit: 27 (4d8 + 9) piercing damage.",
            "Talons.Melee Weapon Attack: +13 to hit, reach 5 ft., one target.Hit: 23 (4d6 + 9) slashing damage, and the target is grappled (escape DC 19). Until this grapple ends, the target is restrained, and the roc can't use its talons on another target."
        ]
    },
    "roper": {
        "name": "Roper",
        "type": "Large monstrosity",
        "alignment": "neutral evil",
        "Armor Class": "20 (natural armor)",
        "Hit Points": "93 (11d10 + 33)",
        "Speed": "10 ft., climb 10 ft.",
        "Skills": "Perception +6, Stealth +5",
        "Senses": "darkvision 60 ft., passive Perception 16",
        "Languages": "\u2014",
        "Challenge": "5 (1800 XP)",
        "STR": "18 (+4)",
        "DEX": "8 (-1)",
        "CON": "17 (+3)",
        "INT": "7 (-2)",
        "WIS": "16 (+3)",
        "CHA": "6 (-2)",
        "features": [
            "False Appearance. While the roper remains motionless, it is indistinguishable from a normal cave formation, such as a stalagmite.",
            "Grasping Tendrils. The roper can have up to six tendrils at a time. Each tendril can be attacked (AC 20; 10 hit points; immunity to poison and psychic damage). Destroying a tendril deals no damage to the roper, which can extrude a replacement tendril on its next turn. A tendril can also be broken if a creature takes an action and succeeds on a DC 15 Strength check against it.",
            "Spider Climb. The roper can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check."
        ],
        "Actions": [
            "Multiattack. The roper makes four attacks with its tendrils, uses Reel, and makes one attack with its bite.",
            "Bite.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 22 (4d8 + 4) piercing damage.",
            "Tendril.Melee Weapon Attack: +7 to hit, reach 50 ft., one creature.Hit: The target is grappled (escape DC 15). Until the grapple ends, the target is restrained and has disadvantage on Strength checks and Strength saving throws, and the roper can't use the same tendril on another target.",
            "Reel. The roper pulls each creature grappled by it up to 25 feet straight toward it."
        ]
    },
    "rug-of-smothering": {
        "name": "Rug of Smothering",
        "type": "Large construct",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "33 (6d10)",
        "Speed": "10 ft.",
        "Damage Immunities": "poison, psychic",
        "Condition Immunities": "blinded, charmed, deafened, frightened, paralyzed, petrified, poisoned",
        "Senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 6",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "17 (+3)",
        "DEX": "14 (+2)",
        "CON": "10 (+0)",
        "INT": "1 (-5)",
        "WIS": "3 (-4)",
        "CHA": "1 (-5)",
        "features": [
            "Antimagic Susceptibility. The rug is incapacitated while in the area of anantimagic field. If targeted bydispel magic, the rug must succeed on a Constitution saving throw against the caster's spell save DC or fall unconscious for 1 minute.",
            "Damage Transfer. While it is grappling a creature, the rug takes only half the damage dealt to it, and the creature grappled by the rug takes the other half.",
            "False Appearance. While the rug remains motionless, it is indistinguishable from a normal rug."
        ],
        "Actions": [
            "Smother.Melee Weapon Attack: +5 to hit, reach 5 ft., one Medium or smaller creature.Hit: The creature is grappled (escape DC 13). Until this grapple ends, the target is restrained, blinded, and at risk of suffocating, and the rug can't smother another target. In addition, at the start of each of the target's turns, the target takes 10 (2d6 + 3) bludgeoning damage."
        ]
    },
    "rust-monster": {
        "name": "Rust Monster",
        "type": "Medium monstrosity",
        "alignment": "unaligned",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "27 (5d8 + 5)",
        "Speed": "40 ft",
        "Senses": "darkvision 60 ft., passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "13 (+1)",
        "DEX": "12 (+1)",
        "CON": "13 (+1)",
        "INT": "2 (-4)",
        "WIS": "13 (+1)",
        "CHA": "6 (-2)",
        "features": [
            "Iron Scent. The rust monster can pinpoint, by scent, the location of ferrous metal within 30 feet of it.",
            "Rust Metal. Any nonmagical weapon made of metal that hits the rust monster corrodes. After dealing damage, the weapon takes a permanent and cumulative -1 penalty to damage rolls. If its penalty drops to -5, the weapon is destroyed. Nonmagical ammunition made of metal that hits the rust monster is destroyed after dealing damage."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 5 (1d8 + 1) piercing damage.",
            "Antennae. The rust monster corrodes a nonmagical ferrous metal object it can see within 5 feet of it. If the object isn't being worn or carried, the touch destroys a 1-foot cube of it. If the object is being worn or carried by a creature, the creature can make a DC 11 Dexterity saving throw to avoid the rust monster's touch. If the object touched is either metal armor or a metal shield being worn or carried, its takes a permanent and cumulative -1 penalty to the AC it offers. Armor reduced to an AC of 10 or a shield that drops to a +0 bonus is destroyed. If the object touched is a held metal weapon, it rusts as described in the Rust Metal trait."
        ]
    },
    "saber-toothed-tiger": {
        "name": "Saber-Toothed Tiger",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "52 (7d10 + 14)",
        "Speed": "40 ft.",
        "Skills": "Perception +3, Stealth +6",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "18 (+4)",
        "DEX": "14 (+2)",
        "CON": "15 (+2)",
        "INT": "3 (-4)",
        "WIS": "12 (+1)",
        "CHA": "8 (-1)",
        "features": [
            "Keen Smell. The tiger has advantage on Wisdom (Perception) checks that rely on smell.",
            "Pounce. If the tiger moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 14 Strength saving throw or be knocked prone. If the target is prone, the tiger can make one bite attack against it as a bonus action."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 10 (1d10 + 5) piercing damage.",
            "Claw.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 12 (2d6 + 5) slashing damage."
        ]
    },
    "sahuagin": {
        "name": "Sahuagin",
        "type": "Medium humanoid (Sahuagin)",
        "alignment": "lawful evil",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "22 (4d8 + 4)",
        "Speed": "30 ft., swim 40 ft.",
        "Skills": "Perception +5",
        "Senses": "darkvision 120 ft., passive Perception 15",
        "Languages": "Sahuagin",
        "Challenge": "1/2 (100 XP)",
        "STR": "13 (+1)",
        "DEX": "11 (+0)",
        "CON": "12 (+1)",
        "INT": "12 (+1)",
        "WIS": "13 (+1)",
        "CHA": "9 (-1)",
        "features": [
            "Blood Frenzy. The sahuagin has advantage on melee attack rolls against any creature that doesn't have all its hit points.",
            "Limited Amphibiousness. The sahuagin can breathe air and water, but it needs to be submerged at least once every 4 hours to avoid suffocating.",
            "Shark Telepathy. The sahuagin can magically command any shark within 120 feet of it, using a limited telepathy."
        ],
        "Actions": [
            "Multiattack. The sahuagin makes two melee attacks: one with its bite and one with its claws or spear.",
            "Bite.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 3 (1d4 + 1) piercing damage.",
            "Claws.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 3 (1d4 + 1) slashing damage.",
            "Spear.Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target.Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack."
        ]
    },
    "sahuagin-baron": {
        "name": "Sahuagin Baron",
        "type": "Large humanoid (Sahuagin)",
        "alignment": "lawful evil",
        "Armor Class": "16 (breastplate)",
        "Hit Points": "76 (9d10 + 27)",
        "Speed": "30 ft., swim 50 ft.",
        "Saving Throws": "Dex +5, Con +6, Int +5, Wis +4",
        "Skills": "Perception +7",
        "Senses": "darkvision 120 ft., passive Perception 17",
        "Languages": "Sahuagin",
        "Challenge": "5 (1800 XP)",
        "STR": "19 (+4)",
        "DEX": "15 (+2)",
        "CON": "16 (+3)",
        "INT": "14 (+2)",
        "WIS": "13 (+1)",
        "CHA": "17 (+3)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "sahuagin-priestess": {
        "name": "Sahuagin Priestess",
        "type": "Medium humanoid (Sahuagin)",
        "alignment": "lawful evil",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "33 (6d8 + 6)",
        "Speed": "30 ft., swim 40 ft.",
        "Skills": "Perception +6, Religion +3",
        "Senses": "darkvision 120 ft., passive Perception 16",
        "Languages": "Sahuagin",
        "Challenge": "2 (450 XP)",
        "STR": "13 (+1)",
        "DEX": "11 (+0)",
        "CON": "12 (+1)",
        "INT": "12 (+1)",
        "WIS": "14 (+2)",
        "CHA": "13 (+1)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "salamander": {
        "name": "Salamander",
        "type": "Large elemental",
        "alignment": "neutral evil",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "90 (12d10 + 24)",
        "Speed": "30 ft.",
        "Damage Vulnerabilities": "cold",
        "Damage Resistances": "bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "fire",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Ignan",
        "Challenge": "5 (1800 XP)",
        "STR": "18 (+4)",
        "DEX": "14 (+2)",
        "CON": "15 (+2)",
        "INT": "11 (+0)",
        "WIS": "10 (+0)",
        "CHA": "12 (+1)",
        "features": [
            "Heated Body. A creature that touches the salamander or hits it with a melee attack while within 5 feet of it takes 7 (2d6) fire damage.",
            "Heated Weapons. Any metal melee weapon the salamander wields deals an extra 3 (1d6) fire damage on a hit (included in the attack)."
        ],
        "Actions": [
            "Multiattack. The salamander makes two attacks: one with its spear and one with its tail.",
            "Spear.Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 20 ft./60 ft., one target.Hit: 11 (2d6 + 4) piercing damage, or 13 (2d8 + 4) piercing damage if used with two hands to make a melee attack, plus 3 (1d6) fire damage.",
            "Tail.Melee Weapon Attack: +7 to hit, reach 10 ft., one target.Hit: 11 (2d6 + 4) bludgeoning damage plus 7 (2d6) fire damage, and the target is grappled (escape DC 14). Until this grapple ends, the target is restrained, the salamander can automatically hit the target with its tail, and the salamander can't make tail attacks against other targets."
        ]
    },
    "satyr": {
        "name": "Satyr",
        "type": "Medium fey",
        "alignment": "chaotic neutral",
        "Armor Class": "14 (leather armor)",
        "Hit Points": "31 (7d8)",
        "Speed": "40 ft.",
        "Skills": "Perception +2, Performance +6, Stealth +5",
        "Senses": "passive Perception 12",
        "Languages": "Common, Elvish, Sylvan",
        "Challenge": "1/2 (100 XP)",
        "STR": "12 (+1)",
        "DEX": "16 (+3)",
        "CON": "11 (+0)",
        "INT": "12 (+1)",
        "WIS": "10 (+0)",
        "CHA": "14 (+2)",
        "features": [
            "Magic Resistance. The satyr has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Ram.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 6 (2d4 + 1) bludgeoning damage.",
            "Shortsword.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 6 (1d6 + 3) piercing damage.",
            "Shortbow.Ranged Weapon Attack: +5 to hit, range 80/320 ft., one target.Hit: 6 (1d6 + 3) piercing damage."
        ]
    },
    "scorpion": {
        "name": "Scorpion",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "11 (natural armor)",
        "Hit Points": "1 (1d4 - 1)",
        "Speed": "10 ft.",
        "Senses": "blindsight 10 ft., passive Perception 9",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "2 (-4)",
        "DEX": "11 (+0)",
        "CON": "8 (-1)",
        "INT": "1 (-5)",
        "WIS": "8 (-1)",
        "CHA": "2 (-4)",
        "features": [],
        "Actions": [
            "Sting.Melee Weapon Attack: +2 to hit, reach 5 ft., one creature.Hit: 1 piercing damage, and the target must make a DC 9 Constitution saving throw, taking 4 (1d8) poison damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "scout": {
        "name": "Scout",
        "type": "Medium humanoid (any race)",
        "alignment": "any alignment",
        "Armor Class": "13 (leather armor)",
        "Hit Points": "16 (3d8 + 3)",
        "Speed": "30 ft.",
        "Skills": "Nature +4, Perception +5, Stealth +6, Survival +5",
        "Senses": "passive Perception 15",
        "Languages": "any one language (usually Common)",
        "Challenge": "1/2 (100 XP)",
        "STR": "11 (+0)",
        "DEX": "14 (+2)",
        "CON": "12 (+1)",
        "INT": "11 (+0)",
        "WIS": "13 (+1)",
        "CHA": "11 (+0)",
        "features": [
            "Keen Hearing and Sight. The scout has advantage on Wisdom (Perception) checks that rely on hearing or sight."
        ],
        "Actions": [
            "Multiattack. The scout makes two melee attacks or two ranged attacks.",
            "Shortsword.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) piercing damage.",
            "Longbow.Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target.Hit: 6 (1d8 + 2) piercing damage."
        ]
    },
    "sea-hag": {
        "name": "Sea Hag",
        "type": "Medium fey",
        "alignment": "chaotic evil",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "52 (7d8 + 21)",
        "Speed": "30 ft., swim 40 ft.",
        "Senses": "darkvision 60 ft., passive Perception 11",
        "Languages": "Aquan, Common, Giant",
        "Challenge": "2 (450 XP)",
        "STR": "16 (+3)",
        "DEX": "13 (+1)",
        "CON": "16 (+3)",
        "INT": "12 (+1)",
        "WIS": "12 (+1)",
        "CHA": "13 (+1)",
        "features": [
            "Amphibious. The hag can breathe air and water.",
            "Horrific Appearance. Any humanoid that starts its turn within 30 feet of the hag and can see the hag's true form must make a DC 11 Wisdom saving throw. On a failed save, the creature is frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, with disadvantage if the hag is within line of sight, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the hag's Horrific Appearance for the next 24 hours. Unless the target is surprised or the revelation of the hag's true form is sudden, the target can avert its eyes and avoid making the initial saving throw. Until the start of its next turn, a creature that averts its eyes has disadvantage on attack rolls against the hag."
        ],
        "Actions": [
            "Claws.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) slashing damage.",
            "Death Glare. The hag targets one frightened creature she can see within 30 feet of her. If the target can see the hag, it must succeed on a DC 11 Wisdom saving throw against this magic or drop to 0 hit points.",
            "Illusory Appearance. The hag covers herself and anything she is wearing or carrying with a magical illusion that makes her look like an ugly creature of her general size and humanoid shape. The effect ends if the hag takes a bonus action to end it or if she dies. The changes wrought by this effect fail to hold up to physical inspection. For example, the hag could appear to have no claws, but someone touching her hand might feel the claws. Otherwise, a creature must take an action to visually inspect the illusion and succeed on a DC 16 Intelligence (Investigation) check to discern that the hag is disguised."
        ]
    },
    "sea-horse": {
        "features": [
            "Water Breathing. The sea horse can breathe only underwater."
        ],
        "name": "Sea Horse",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "11",
        "Hit Points": "1 (1d4 - 1)",
        "Speed": "0 ft., swim 20 ft.",
        "Senses": "passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "0 (0 XP)",
        "STR": "1 (-5)",
        "DEX": "12 (+1)",
        "CON": "8 (-1)",
        "INT": "1 (-5)",
        "WIS": "10 (+0)",
        "CHA": "2 (-4)"
    },
    "shadow": {
        "name": "Shadow",
        "type": "Medium undead",
        "alignment": "chaotic evil",
        "Armor Class": "12",
        "Hit Points": "16 (3d8 + 3)",
        "Speed": "40 ft.",
        "Skills": "Stealth +4 (+6 in dim light or darkness)",
        "Damage Vulnerabilities": "radiant",
        "Damage Resistances": "acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "necrotic, poison",
        "Condition Immunities": "exhaustion, frightened, grappled, paralyzed, petrified, poisoned, prone, restrained",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "6 (-2)",
        "DEX": "14 (+2)",
        "CON": "13 (+1)",
        "INT": "6 (-2)",
        "WIS": "10 (+0)",
        "CHA": "8 (-1)",
        "features": [
            "Amorphous. The shadow can move through a space as narrow as 1 inch wide without squeezing.",
            "Shadow Stealth. While in dim light or darkness, the shadow can take the Hide action as a bonus action.",
            "Sunlight Weakness. While in sunlight, the shadow has disadvantage on attack rolls, ability checks, and saving throws."
        ],
        "Actions": [
            "Strength Drain.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 9 (2d6 + 2) necrotic damage, and the target's Strength score is reduced by 1d4. The target dies if this reduces its Strength to 0. Otherwise, the reduction lasts until the target finishes a short or long rest. If a non-evil humanoid dies from this attack, a new shadow rises from the corpse 1d4 hours later."
        ]
    },
    "shambling-mound": {
        "name": "Shambling Mound",
        "type": "Large plant",
        "alignment": "unaligned",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "136 (16d10 + 48)",
        "Speed": "20 ft., swim 20 ft.",
        "Skills": "Stealth +2",
        "Damage Resistances": "cold, fire",
        "Damage Immunities": "lightning",
        "Condition Immunities": "blinded, deafened, exhaustion",
        "Senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "5 (1800 XP)",
        "STR": "18 (+4)",
        "DEX": "8 (-1)",
        "CON": "16 (+3)",
        "INT": "5 (-3)",
        "WIS": "10 (+0)",
        "CHA": "5 (-3)",
        "features": [
            "Lightning Absorption. Whenever the shambling mound is subjected to lightning damage, it takes no damage and regains a number of hit points equal to the lightning damage dealt."
        ],
        "Actions": [
            "Multiattack. The shambling mound makes two slam attacks. If both attacks hit a Medium or smaller target, the target is grappled (escape DC 14), and the shambling mound uses its Engulf on it.",
            "Slam.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 13 (2d8 + 4) bludgeoning damage.",
            "Engulf. The shambling mound engulfs a Medium or smaller creature grappled by it. The engulfed target is blinded, restrained, and unable to breathe, and it must succeed on a DC 14 Constitution saving throw at the start of each of the mound's turns or take 13 (2d8 + 4) bludgeoning damage. If the mound moves, the engulfed target moves with it. The mound can have only one creature engulfed at a time."
        ]
    },
    "shield-guardian": {
        "name": "Shield Guardian",
        "type": "Large construct",
        "alignment": "unaligned",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "142 (15d10 + 60)",
        "Speed": "30 ft.",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 10",
        "Damage Immunities": "poison",
        "Condition Immunities": "charmed, exhaustion, frightened, paralyzed, poisoned",
        "Languages": "understands commands given in any language but can't speak",
        "Challenge": "7 (2900 XP)",
        "STR": "18 (+4)",
        "DEX": "8 (-1)",
        "CON": "18 (+4)",
        "INT": "7 (-2)",
        "WIS": "10 (+0)",
        "CHA": "3 (-4)",
        "Reactions": [
            "Shield. When a creature makes an attack against the wearer of the guardian's amulet, the guardian grants a +2 bonus to the wearer's AC if the guardian is within 5 feet of the wearer."
        ],
        "features": [
            "Bound. The shield guardian is magically bound to an amulet. As long as the guardian and its amulet are on the same plane of existence, the amulet's wearer can telepathically call the guardian to travel to it, and the guardian knows the distance and direction to the amulet. If the guardian is within 60 feet of the amulet's wearer, half of any damage the wearer takes (rounded up) is transferred to the guardian.",
            "Regeneration. The shield guardian regains 10 hit points at the start of its turn if it has at least 1 hit point.",
            "Spell Storing. A spellcaster who wears the shield guardian's amulet can cause the guardian to store one spell of 4th level or lower. To do so, the wearer must cast the spell on the guardian. The spell has no effect but is stored within the guardian. When commanded to do so by the wearer or when a situation arises that was predefined by the spellcaster, the guardian casts the stored spell with any parameters set by the original caster, requiring no components. When the spell is cast or a new spell is stored, any previously stored spell is lost."
        ],
        "Actions": [
            "Multiattack. The guardian makes two fist attacks.",
            "Fist.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) bludgeoning damage."
        ]
    },
    "shrieker": {
        "features": [
            "False Appearance. While the shrieker remains motionless, it is indistinguishable from an ordinary fungus.",
            "Shriek. When bright light or a creature is within 30 feet of the shrieker, it emits a shriek audible within 300 feet of it. The shrieker continues to shriek until the disturbance moves out of range and for 1d4 of the shrieker's turns afterward."
        ],
        "name": "Shrieker",
        "type": "Medium plant",
        "alignment": "unaligned",
        "Armor Class": "5",
        "Hit Points": "13 (3d8)",
        "Speed": "0 ft.",
        "Condition Immunities": "blinded, deafened, frightened",
        "Senses": "blindsight 30 ft. (blind beyond this radius), passive Perception 6",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "1 (-5)",
        "DEX": "1 (-5)",
        "CON": "10 (+0)",
        "INT": "1 (-5)",
        "WIS": "3 (-4)",
        "CHA": "1 (-5)"
    },
    "silver-dragon-wyrmling": {
        "name": "Silver Dragon Wyrmling",
        "type": "Medium dragon (Metallic)",
        "alignment": "lawful good",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "45 (6d8 + 18)",
        "Speed": "30 ft., fly 60 ft.",
        "Saving Throws": "Dex +2, Con +5, Wis +2, Cha +4",
        "Skills": "Perception +4, Stealth +2",
        "Damage Immunities": "cold",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 14",
        "Languages": "Draconic",
        "Challenge": "2 (450 XP)",
        "STR": "19 (+4)",
        "DEX": "10 (+0)",
        "CON": "17 (+3)",
        "INT": "12 (+1)",
        "WIS": "11 (+0)",
        "CHA": "15 (+2)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 9 (1d10 + 4) piercing damage.",
            "Breath Weapons (Recharge 5-6). The dragon uses one of the following breath weapons.",
            "Cold Breath. The dragon exhales an icy blast in a 15-foot cone. Each creature in that area must make a DC 13 Constitution saving throw, taking 18 (4d8) cold damage on a failed save, or half as much damage on a successful one.",
            "Paralyzing Breath. The dragon exhales paralyzing gas in a 15-foot cone. Each creature in that area must succeed on a DC 13 Constitution saving throw or be paralyzed for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        ]
    },
    "skeleton": {
        "name": "Skeleton",
        "type": "Medium undead",
        "alignment": "lawful evil",
        "Armor Class": "13 (armor scraps)",
        "Hit Points": "13 (2d8 + 4)",
        "Speed": "30 ft.",
        "Damage Vulnerabilities": "bludgeoning",
        "Damage Immunities": "poison",
        "Condition Immunities": "exhaustion, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 9",
        "Languages": "understands the languages it knew in life but can't speak",
        "Challenge": "1/4 (50 XP)",
        "STR": "10 (+0)",
        "DEX": "14 (+2)",
        "CON": "15 (+2)",
        "INT": "6 (-2)",
        "WIS": "8 (-1)",
        "CHA": "5 (-3)",
        "features": [],
        "Actions": [
            "Shortsword.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) piercing damage.",
            "Shortbow.Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target.Hit: 5 (1d6 + 2) piercing damage."
        ]
    },
    "solar": {
        "name": "Solar",
        "type": "Large celestial",
        "alignment": "lawful good",
        "Armor Class": "21 (natural armor)",
        "Hit Points": "243 (18d10 + 144)",
        "Speed": "50 ft., fly 150 ft.",
        "Saving Throws": "Int +14, Wis +14, Cha +17",
        "Skills": "Perception +14",
        "Damage Resistances": "radiant; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "necrotic, poison",
        "Condition Immunities": "charmed, exhaustion, frightened, poisoned",
        "Senses": "truesight 120 ft., passive Perception 24",
        "Languages": "all, telepathy 120 ft.",
        "Challenge": "21 (33000 XP)",
        "STR": "26 (+8)",
        "DEX": "22 (+6)",
        "CON": "26 (+8)",
        "INT": "25 (+7)",
        "WIS": "25 (+7)",
        "CHA": "30 (+10)",
        "Legendary actions": [
            "The solar can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The solar regains spent legendary actions at the start of its turn.",
            "Teleport. The solar magically teleports, along with any equipment it is wearing or carrying, up to 120 feet to an unoccupied space it can see.",
            "Searing Burst (Costs 2 Actions). The solar emits magical, divine energy. Each creature of its choice in a 10-foot radius must make a DC 23 Dexterity saving throw, taking 14 (4d6) fire damage plus 14 (4d6) radiant damage on a failed save, or half as much damage on a successful one.",
            "Blinding Gaze (Costs 3 Actions). The solar targets one creature it can see within 30 feet of it. If the target can see it, the target must succeed on a DC 15 Constitution saving throw or be blinded until magic such as thelesser restorationspell removes the blindness."
        ],
        "features": [
            "Angelic Weapons. The solar's weapon attacks are magical. When the solar hits with any weapon, the weapon deals an extra 6d8 radiant damage (included in the attack).",
            "Divine Awareness. The solar knows if it hears a lie.",
            "Innate Spellcasting. The solar's spellcasting ability is Charisma (spell save DC 25). It can innately cast the following spells, requiring no material components:",
            "Magic Resistance. The solar has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack. The solar makes two greatsword attacks.",
            "Greatsword.Melee Weapon Attack: +15 to hit, reach 5 ft., one target.Hit: 22 (4d6 + 8) slashing damage plus 27 (6d8) radiant damage.",
            "Slaying Longbow.Ranged Weapon Attack: +13 to hit, range 150/600 ft., one target.Hit: 15 (2d8 + 6) piercing damage plus 27 (6d8) radiant damage. If the target is a creature that has 100 hit points or fewer, it must succeed on a DC 15 Constitution saving throw or die.",
            "Flying Sword. The solar releases its greatsword to hover magically in an unoccupied space within 5 feet of it. If the solar can see the sword, the solar can mentally command it as a bonus action to fly up to 50 feet and either make one attack against a target or return to the solar's hands. If the hovering sword is targeted by any effect, the solar is considered to be holding it. The hovering sword falls if the solar dies.",
            "Healing Touch (4/Day). The solar touches another creature. The target magically regains 40 (8d8 + 4) hit points and is freed from any curse, disease, poison, blindness, or deafness."
        ]
    },
    "specter": {
        "name": "Specter",
        "type": "Medium undead",
        "alignment": "chaotic evil",
        "Armor Class": "12",
        "Hit Points": "22 (5d8)",
        "Speed": "0 ft., fly 50 ft. (hover)",
        "Damage Resistances": "acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "necrotic, poison",
        "Condition Immunities": "charmed, exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "understands the languages it knew in life but can't speak",
        "Challenge": "1 (200 XP)",
        "STR": "1 (-5)",
        "DEX": "14 (+2)",
        "CON": "11 (+0)",
        "INT": "10 (+0)",
        "WIS": "10 (+0)",
        "CHA": "11 (+0)",
        "features": [
            "Incorporeal Movement. The specter can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.",
            "Sunlight Sensitivity. While in sunlight, the specter has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
        ],
        "Actions": [
            "Life Drain.Melee Spell Attack: +4 to hit, reach 5 ft., one creature.Hit: 10 (3d6) necrotic damage. The target must succeed on a DC 10 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the creature finishes a long rest. The target dies if this effect reduces its hit point maximum to 0."
        ]
    },
    "spider": {
        "name": "Spider",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "1 (1d4 - 1)",
        "Speed": "20 ft., climb 20 ft.",
        "Skills": "Stealth +4",
        "Senses": "darkvision 30 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "2 (-4)",
        "DEX": "14 (+2)",
        "CON": "8 (-1)",
        "INT": "1 (-5)",
        "WIS": "10 (+0)",
        "CHA": "2 (-4)",
        "features": [
            "Spider Climb. The spider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.",
            "Web Sense. While in contact with a web, the spider knows the exact location of any other creature in contact with the same web.",
            "Web Walker. The spider ignores movement restrictions caused by webbing."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 1 piercing damage, and the target must succeed on a DC 9 Constitution saving throw or take 2 (1d4) poison damage."
        ]
    },
    "spirit-naga": {
        "name": "Spirit Naga",
        "type": "Large monstrosity",
        "alignment": "chaotic evil",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "75 (10d10 + 20)",
        "Speed": "40 ft.",
        "Saving Throws": "Dex +6, Con +5, Wis +5, Cha +6",
        "Damage Immunities": "poison",
        "Condition Immunities": "charmed, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 12",
        "Languages": "Abyssal, Common",
        "Challenge": "8 (3900 XP)",
        "STR": "18 (+4)",
        "DEX": "17 (+3)",
        "CON": "14 (+2)",
        "INT": "16 (+3)",
        "WIS": "15 (+2)",
        "CHA": "16 (+3)",
        "features": [
            "Rejuvenation. If it dies, the naga returns to life in 1d6 days and regains all its hit points. Only awishspell can prevent this trait from functioning.",
            "Spellcasting. The naga is a 10th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 14, +6 to hit with spell attacks), and it needs only verbal components to cast its spells. It has the following wizard spells prepared:"
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +7 to hit, reach 10 ft., one creature.Hit: 7 (1d6 + 4) piercing damage, and the target must make a DC 13 Constitution saving throw, taking 31 (7d8) poison damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "sprite": {
        "name": "Sprite",
        "type": "Tiny fey",
        "alignment": "neutral good",
        "Armor Class": "15 (leather armor)",
        "Hit Points": "2 (1d4)",
        "Speed": "10 ft., fly 40 ft.",
        "Skills": "Perception +3, Stealth +8",
        "Senses": "passive Perception 13",
        "Languages": "Common, Elvish, Sylvan",
        "Challenge": "1/4 (50 XP)",
        "STR": "3 (-4)",
        "DEX": "18 (+4)",
        "CON": "10 (+0)",
        "INT": "14 (+2)",
        "WIS": "13 (+1)",
        "CHA": "11 (+0)",
        "features": [],
        "Actions": [
            "Longsword.Melee Weapon Attack: +2 to hit, reach 5 ft., one target.Hit: 1 slashing damage.",
            "Shortbow.Ranged Weapon Attack: +6 to hit, range 40/160 ft., one target.Hit: 1 piercing damage, and the target must succeed on a DC 10 Constitution saving throw or become poisoned for 1 minute. If its saving throw result is 5 or lower, the poisoned target falls unconscious for the same duration, or until it takes damage or another creature takes an action to shake it awake.",
            "Heart Sight. The sprite touches a creature and magically knows the creature's current emotional state. If the target fails a DC 10 Charisma saving throw, the sprite also knows the creature's alignment. Celestials, fiends, and undead automatically fail the saving throw.",
            "Invisibility. The sprite magically turns invisible until it attacks or casts a spell, or until its concentration ends (as if concentrating on a spell). Any equipment the sprite wears or carries is invisible with it."
        ]
    },
    "spy": {
        "name": "Spy",
        "type": "Medium humanoid (any race)",
        "alignment": "any alignment",
        "Armor Class": "12",
        "Hit Points": "27 (6d8)",
        "Speed": "30 ft.",
        "Skills": "Deception +5, Insight +4, Investigation +5, Perception +6, Persuasion +5, Sleight of Hand +4, Stealth +4",
        "Senses": "passive Perception 16",
        "Languages": "any two languages",
        "Challenge": "1 (200 XP)",
        "STR": "10 (+0)",
        "DEX": "15 (+2)",
        "CON": "10 (+0)",
        "INT": "12 (+1)",
        "WIS": "14 (+2)",
        "CHA": "16 (+3)",
        "features": [
            "Cunning Action. On each of its turns, the spy can use a bonus action to take the Dash, Disengage, or Hide action.",
            "Sneak Attack (1/Turn). The spy deals an extra 7 (2d6) damage when it hits a target with a weapon attack and has advantage on the attack roll, or when the target is within 5 feet of an ally of the spy that isn't incapacitated and the spy doesn't have disadvantage on the attack roll."
        ],
        "Actions": [
            "Multiattack. The spy makes two melee attacks.",
            "Shortsword.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) piercing damage.",
            "Hand Crossbow.Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target.Hit: 5 (1d6 + 2) piercing damage."
        ]
    },
    "steam-mephit": {
        "name": "Steam Mephit",
        "type": "Small elemental",
        "alignment": "neutral evil",
        "Armor Class": "10",
        "Hit Points": "21 (6d6)",
        "Speed": "30 ft., fly 30 ft.",
        "Damage Immunities": "fire, poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Aquan, Ignan",
        "Challenge": "1/4 (50 XP)",
        "STR": "5 (-3)",
        "DEX": "11 (+0)",
        "CON": "10 (+0)",
        "INT": "11 (+0)",
        "WIS": "10 (+0)",
        "CHA": "12 (+1)",
        "features": [
            "Death Burst. When the mephit dies, it explodes in a cloud of steam. Each creature within 5 feet of the mephit must succeed on a DC 10 Dexterity saving throw or take 4 (1d8) fire damage.",
            "Innate Spellcasting (1/Day). The mephit can innately castblur, requiring no material components. Its innate spellcasting ability is Charisma."
        ],
        "Actions": [
            "Claws.Melee Weapon Attack: +2 to hit, reach 5 ft., one creature.Hit: 2 (1d4) slashing damage plus 2 (1d4) fire damage.",
            "Steam Breath (Recharge 6). The mephit exhales a 15-foot cone of scalding steam. Each creature in that area must succeed on a DC 10 Dexterity saving throw, taking 4 (1d8) fire damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "stirge": {
        "name": "Stirge",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "2 (1d4)",
        "Speed": "10 ft., fly 40 ft.",
        "Senses": "darkvision 60 ft., passive Perception 9",
        "Languages": "\u2014",
        "Challenge": "1/8 (25 XP)",
        "STR": "4 (-3)",
        "DEX": "16 (+3)",
        "CON": "11 (+0)",
        "INT": "2 (-4)",
        "WIS": "8 (-1)",
        "CHA": "6 (-2)",
        "features": [],
        "Actions": [
            "Blood Drain.Melee Weapon Attack: +5 to hit, reach 5 ft., one creature.Hit: 5 (1d4 + 3) piercing damage, and the stirge attaches to the target. While attached, the stirge doesn't attack. Instead, at the start of each of the stirge's turns, the target loses 5 (1d4 + 3) hit points due to blood loss. The stirge can detach itself by spending 5 feet of its movement. It does so after it drains 10 hit points of blood from the target or the target dies. A creature, including the target, can use its action to detach the stirge."
        ]
    },
    "stone-giant": {
        "name": "Stone Giant",
        "type": "Huge giant",
        "alignment": "neutral",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "126 (11d12 + 55)",
        "Speed": "40 ft.",
        "Saving Throws": "Dex +5, Con +8, Wis +4",
        "Skills": "Athletics +12, Perception +4",
        "Senses": "darkvision 60 ft., passive Perception 14",
        "Languages": "Giant",
        "Challenge": "7 (2900 XP)",
        "STR": "23 (+6)",
        "DEX": "15 (+2)",
        "CON": "20 (+5)",
        "INT": "10 (+0)",
        "WIS": "12 (+1)",
        "CHA": "9 (-1)",
        "Reactions": [
            "Rock Catching. If a rock or similar object is hurled at the giant, the giant can, with a successful DC 10 Dexterity saving throw, catch the missile and take no bludgeoning damage from it."
        ],
        "features": [
            "Stone Camouflage. The giant has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."
        ],
        "Actions": [
            "Multiattack. The giant makes two greatclub attacks.",
            "Greatclub.Melee Weapon Attack: +9 to hit, reach 15 ft., one target.Hit: 19 (3d8 + 6) bludgeoning damage.",
            "Rock.Ranged Weapon Attack: +9 to hit, range 60/240 ft., one target.Hit: 28 (4d10 + 6) bludgeoning damage. If the target is a creature, it must succeed on a DC 17 Strength saving throw or be knocked prone."
        ]
    },
    "stone-golem": {
        "name": "Stone Golem",
        "type": "Large construct",
        "alignment": "unaligned",
        "Armor Class": "17 (natural armor)",
        "Hit Points": "178 (17d10 + 85)",
        "Speed": "30 ft.",
        "Damage Immunities": "poison, psychic; bludgeoning, piercing, and slashing from nonmagical attacks that aren't adamantine",
        "Condition Immunities": "charmed, exhaustion, frightened, paralyzed, petrified, poisoned",
        "Senses": "darkvision 120 ft., passive Perception 10",
        "Languages": "understands the languages of its creator but can't speak",
        "Challenge": "10 (5900 XP)",
        "STR": "22 (+6)",
        "DEX": "9 (-1)",
        "CON": "20 (+5)",
        "INT": "3 (-4)",
        "WIS": "11 (+0)",
        "CHA": "1 (-5)",
        "features": [
            "Immutable Form. The golem is immune to any spell or effect that would alter its form.",
            "Magic Resistance. The golem has advantage on saving throws against spells and other magical effects.",
            "Magic Weapons. The golem's weapon attacks are magical."
        ],
        "Actions": [
            "Multiattack. The golem makes two slam attacks.",
            "Slam.Melee Weapon Attack: +10 to hit, reach 5 ft., one target.Hit: 19 (3d8 + 6) bludgeoning damage.",
            "Slow (Recharge 5-6). The golem targets one or more creatures it can see within 10 feet of it. Each target must make a DC 17 Wisdom saving throw against this magic. On a failed save, a target can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the target can take either an action or a bonus action on its turn, not both. These effects last for 1 minute. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."
        ]
    },
    "storm-giant": {
        "name": "Storm Giant",
        "type": "Huge giant",
        "alignment": "chaotic good",
        "Armor Class": "16 (scale mail)",
        "Hit Points": "230 (20d12 + 100)",
        "Speed": "50 ft., swim 50 ft.",
        "Saving Throws": "Str +14, Con +10, Wis +9, Cha +9",
        "Skills": "Arcana +8, Athletics +14, History +8, Perception +9",
        "Damage Resistances": "cold",
        "Damage Immunities": "lightning, thunder",
        "Senses": "passive Perception 19",
        "Languages": "Common, Giant",
        "Challenge": "13 (10000 XP)",
        "STR": "29 (+9)",
        "DEX": "14 (+2)",
        "CON": "20 (+5)",
        "INT": "16 (+3)",
        "WIS": "18 (+4)",
        "CHA": "18 (+4)",
        "features": [
            "Amphibious. The giant can breathe air and water.",
            "Innate Spellcasting. The giant's innate spellcasting ability is Charisma (spell save DC 17). It can innately cast the following spells, requiring no material components:"
        ],
        "Actions": [
            "Multiattack. The giant makes two greatsword attacks.",
            "Greatsword.Melee Weapon Attack: +14 to hit, reach 10 ft., one target.Hit: 30 (6d6 + 9) slashing damage.",
            "Rock.Ranged Weapon Attack: +14 to hit, range 60/240 ft., one target.Hit: 35 (4d12 + 9) bludgeoning damage.",
            "Lightning Strike (Recharge 5-6). The giant hurls a magical lightning bolt at a point it can see within 500 feet of it. Each creature within 10 feet of that point must make a DC 17 Dexterity saving throw, taking 54 (12d8) lightning damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "incubus": {
        "features": []
    },
    "swarm-of-bats": {
        "name": "Swarm of Bats",
        "type": "Medium Swarm of Tiny Beasts",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "22 (5d8)",
        "Speed": "0 ft., fly 30 ft.",
        "Damage Resistances": "bludgeoning, piercing, slashing",
        "Condition Immunities": "charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned",
        "Senses": "blindsight 60 ft., passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "5 (-3)",
        "DEX": "15 (+2)",
        "CON": "10 (+0)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "4 (-3)",
        "features": [
            "Echolocation. The swarm can't use its blindsight while deafened.",
            "Keen Hearing. The swarm has advantage on Wisdom (Perception) checks that rely on hearing.",
            "Swarm. The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny bat. The swarm can't regain hit points or gain temporary hit points."
        ],
        "Actions": [
            "Bites.Melee Weapon Attack: +4 to hit, reach 0 ft., one creature in the swarm's space.Hit: 5 (2d4) piercing damage, or 2 (1d4) piercing damage if the swarm has half of its hit points or fewer."
        ]
    },
    "swarm-of-bees": {
        "features": []
    },
    "swarm-of-centipedes": {
        "features": []
    },
    "swarm-of-insects": {
        "name": "Swarm of Insects",
        "type": "Medium Swarm of Tiny Beasts",
        "alignment": "unaligned",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "22 (5d8)",
        "Speed": "20 ft., climb 20 ft.",
        "Damage Resistances": "bludgeoning, piercing, slashing",
        "Condition Immunities": "charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned",
        "Senses": "blindsight 10 ft., passive Perception 8",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "3 (-4)",
        "DEX": "13 (+1)",
        "CON": "10 (+0)",
        "INT": "1 (-5)",
        "WIS": "7 (-2)",
        "CHA": "1 (-5)",
        "features": [
            "Swarm. The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny insect. The swarm can't regain hit points or gain temporary hit points."
        ],
        "Actions": [
            "Bites.Melee Weapon Attack: +3 to hit, reach 0 ft., one target in the swarm's space.Hit: 10 (4d4) piercing damage, or 5 (2d4) piercing damage if the swarm has half of its hit points or fewer."
        ]
    },
    "swarm-of-poisonous-snakes": {
        "name": "Swarm of Poisonous Snakes",
        "type": "Medium Swarm of Tiny Beasts",
        "alignment": "unaligned",
        "Armor Class": "14",
        "Hit Points": "36 (8d8)",
        "Speed": "30 ft., swim 30 ft.",
        "Damage Resistances": "bludgeoning, piercing, slashing",
        "Condition Immunities": "charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned",
        "Senses": "blindsight 10 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "2 (450 XP)",
        "STR": "8 (-1)",
        "DEX": "18 (+4)",
        "CON": "11 (+0)",
        "INT": "1 (-5)",
        "WIS": "10 (+0)",
        "CHA": "3 (-4)",
        "features": [
            "Swarm. The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny snake. The swarm can't regain hit points or gain temporary hit points."
        ],
        "Actions": [
            "Bites.Melee Weapon Attack: +6 to hit, reach 0 ft., one creature in the swarm's space.Hit: 7 (2d6) piercing damage, or 3 (1d6) piercing damage if the swarm has half of its hit points or fewer. The target must make a DC 10 Constitution saving throw, taking 14 (4d6) poison damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "swarm-of-quippers": {
        "name": "Swarm of Quippers",
        "type": "Medium Swarm of Tiny Beasts",
        "alignment": "unaligned",
        "Armor Class": "13",
        "Hit Points": "28 (8d8 - 8)",
        "Speed": "0 ft., swim 40 ft.",
        "Damage Resistances": "bludgeoning, piercing, slashing",
        "Condition Immunities": "charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned",
        "Senses": "darkvision 60 ft., passive Perception 8",
        "Languages": "\u2014",
        "Challenge": "1 (200 XP)",
        "STR": "13 (+1)",
        "DEX": "16 (+3)",
        "CON": "9 (-1)",
        "INT": "1 (-5)",
        "WIS": "7 (-2)",
        "CHA": "2 (-4)",
        "features": [
            "Blood Frenzy. The swarm has advantage on melee attack rolls against any creature that doesn't have all its hit points.",
            "Swarm. The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny quipper. The swarm can't regain hit points or gain temporary hit points.",
            "Water Breathing. The swarm can breathe only underwater."
        ],
        "Actions": [
            "Bites.Melee Weapon Attack: +5 to hit, reach 0 ft., one creature in the swarm's space.Hit: 14 (4d6) piercing damage, or 7 (2d6) piercing damage if the swarm has half of its hit points or fewer."
        ]
    },
    "swarm-of-rats": {
        "name": "Swarm of Rats",
        "type": "Medium Swarm of Tiny Beasts",
        "alignment": "unaligned",
        "Armor Class": "10",
        "Hit Points": "24 (7d8 - 7)",
        "Speed": "30 ft.",
        "Damage Resistances": "bludgeoning, piercing, slashing",
        "Condition Immunities": "charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned",
        "Senses": "darkvision 30 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "9 (-1)",
        "DEX": "11 (+0)",
        "CON": "9 (-1)",
        "INT": "2 (-4)",
        "WIS": "10 (+0)",
        "CHA": "3 (-4)",
        "features": [
            "Keen Smell. The swarm has advantage on Wisdom (Perception) checks that rely on smell.",
            "Swarm. The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny rat. The swarm can't regain hit points or gain temporary hit points."
        ],
        "Actions": [
            "Bites.Melee Weapon Attack: +2 to hit, reach 0 ft., one target in the swarm's space.Hit: 7 (2d6) piercing damage, or 3 (1d6) piercing damage if the swarm has half of its hit points or fewer."
        ]
    },
    "swarm-of-ravens": {
        "name": "Swarm of Ravens",
        "type": "Medium Swarm of Tiny Beasts",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "24 (7d8 - 7)",
        "Speed": "10 ft., fly 50 ft.",
        "Skills": "Perception +5",
        "Damage Resistances": "bludgeoning, piercing, slashing",
        "Condition Immunities": "charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned",
        "Senses": "passive Perception 15",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "6 (-2)",
        "DEX": "14 (+2)",
        "CON": "8 (-1)",
        "INT": "3 (-4)",
        "WIS": "12 (+1)",
        "CHA": "6 (-2)",
        "features": [
            "Swarm. The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny raven. The swarm can't regain hit points or gain temporary hit points."
        ],
        "Actions": [
            "Beaks.Melee Weapon Attack: +4 to hit, reach 5 ft., one target in the swarm's space.Hit: 7 (2d6) piercing damage, or 3 (1d6) piercing damage if the swarm has half of its hit points or fewer."
        ]
    },
    "swarm-of-spiders": {
        "features": []
    },
    "swarm-of-wasps": {
        "features": []
    },
    "tarrasque": {
        "name": "Tarrasque",
        "type": "Gargantuan monstrosity (Titan)",
        "alignment": "unaligned",
        "Armor Class": "25 (natural armor)",
        "Hit Points": "676 (33d20 + 330)",
        "Speed": "40 ft.",
        "Saving Throws": "Int +5, Wis +9, Cha +9",
        "Damage Immunities": "fire, poison; bludgeoning, piercing and slashing from nonmagical attacks",
        "Condition Immunities": "charmed, frightened, paralyzed, poisoned",
        "Senses": "blindsight 120 ft., passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "30 (155000 XP)",
        "STR": "30 (+10)",
        "DEX": "11 (+0)",
        "CON": "30 (+10)",
        "INT": "3 (-4)",
        "WIS": "11 (+0)",
        "CHA": "11 (+0)",
        "Legendary actions": [
            "The tarrasque can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The tarrasque regains spent legendary actions at the start of its turn.",
            "Attack. The tarrasque makes one claw attack or tail attack.",
            "Move. The tarrasque moves up to half its speed.",
            "Chomp (Costs 2 Actions). The tarrasque makes one bite attack or uses its Swallow."
        ],
        "features": [
            "Legendary Resistance (3/Day). If the tarrasque fails a saving throw, it can choose to succeed instead.",
            "Magic Resistance. The tarrasque has advantage on saving throws against spells and other magical effects.",
            "Reflective Carapace. Any time the tarrasque is targeted by amagic missilespell, a line spell, or a spell that requires a ranged attack roll, roll a d6. On a 1 to 5, the tarrasque is unaffected. On a 6, the tarrasque is unaffected, and the effect is reflected back at the caster as though it originated from the tarrasque, turning the caster into the target.",
            "Siege Monster. The tarrasque deals double damage to objects and structures."
        ],
        "Actions": [
            "Multiattack. The tarrasque can use its Frightful Presence. It then makes five attacks: one with its bite, two with its claws, one with its horns, and one with its tail. It can use its Swallow instead of its bite.",
            "Bite.Melee Weapon Attack: +19 to hit, reach 10 ft., one target.Hit: 36 (4d12 + 10) piercing damage. If the target is a creature, it is grappled (escape DC 20). Until this grapple ends, the target is restrained, and the tarrasque can't bite another target.",
            "Claw.Melee Weapon Attack: +19 to hit, reach 15 ft., one target.Hit: 28 (4d8 + 10) stashing damage.",
            "Horns.Melee Weapon Attack: +19 to hit, reach 10 ft., one target.Hit: 32 (4d10 + 10) piercing damage.",
            "Tail.Melee Weapon Attack: +19 to hit, reach 20 ft., one target.Hit: 24 (4d6 + 10) bludgeoning damage. If the target is a creature, it must succeed on a DC 20 Strength saving throw or be knocked prone.",
            "Frightful Presence. Each creature of the tarrasque's choice within 120 feet of it and aware of it must succeed on a DC 17 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, with disadvantage if the tarrasque is within line of sight, ending the effect on itself on a success. If a creature's saving throw Is successful or the effect ends for it, the creature is immune to the tarrasque's Frightful Presence for the next 24 hours.",
            "Swallow. The tarrasque makes one bite attack against a Large or smaller creature it is grappling. If the attack hits, the target takes the bite's damage, the target is swallowed, and the grapple ends. While swallowed, the creature is blinded and restrained, it has total cover against attacks and other effects outside the tarrasque, and it takes bO (I6d6) acid damage at the start of each of the tarrasque's turns. If the tarrasque takes 60 damage or more on a single turn from a creature inside it, the tarrasque must succeed on a DC 30 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall prone in a space within 10 feet of the tarrasque. If the tarrasque dies, a swallowed creature is no longer restrained by it and can escape from the corpse by using 30 feet of movement, exiting prone."
        ]
    },
    "thug": {
        "name": "Thug",
        "type": "Medium humanoid (any race)",
        "alignment": "any non-good alignment",
        "Armor Class": "11 (leather armor)",
        "Hit Points": "32 (5d8 + 10)",
        "Speed": "30 ft.",
        "Skills": "Intimidation +2",
        "Senses": "passive Perception 10",
        "Languages": "any one language (usually Common)",
        "Challenge": "1/2 (100 XP)",
        "STR": "15 (+2)",
        "DEX": "11 (+0)",
        "CON": "14 (+2)",
        "INT": "10 (+0)",
        "WIS": "10 (+0)",
        "CHA": "11 (+0)",
        "features": [
            "Pack Tactics. The thug has advantage on an attack roll against a creature if at least one of the thug's allies is within 5 feet of the creature and the ally isn't incapacitated."
        ],
        "Actions": [
            "Multiattack. The thug makes two melee attacks.",
            "Mace.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 5 (1d6 + 2) bludgeoning damage.",
            "Heavy Crossbow.Ranged Weapon Attack: +2 to hit, range 100/400 ft., one target.Hit: 5 (1d10) piercing damage."
        ]
    },
    "tiger": {
        "name": "Tiger",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "12",
        "Hit Points": "37 (5d10 + 10)",
        "Speed": "40 ft.",
        "Skills": "Perception +3, Stealth +6",
        "Senses": "darkvision 60 ft., passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "1 (200 XP)",
        "STR": "17 (+3)",
        "DEX": "15 (+2)",
        "CON": "14 (+2)",
        "INT": "3 (-4)",
        "WIS": "12 (+1)",
        "CHA": "8 (-1)",
        "features": [
            "Keen Smell. The tiger has advantage on Wisdom (Perception) checks that rely on smell.",
            "Pounce. If the tiger moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone. If the target is prone, the tiger can make one bite attack against it as a bonus action."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 8 (1d10 + 3) piercing damage.",
            "Claw.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 7 (1d8 + 3) slashing damage."
        ]
    },
    "treant": {
        "name": "Treant",
        "type": "Huge plant",
        "alignment": "chaotic good",
        "Armor Class": "16 (natural armor)",
        "Hit Points": "138 (12d12 + 60)",
        "Speed": "30 ft.",
        "Damage Resistances": "bludgeoning, piercing",
        "Damage Vulnerabilities": "fire",
        "Senses": "passive Perception 13",
        "Languages": "Common, Druidic, Elvish, Sylvan",
        "Challenge": "9 (5000 XP)",
        "STR": "23 (+6)",
        "DEX": "8 (-1)",
        "CON": "21 (+5)",
        "INT": "12 (+1)",
        "WIS": "16 (+3)",
        "CHA": "12 (+1)",
        "features": [
            "False Appearance. While the treant remains motionless, it is indistinguishable from a normal tree.",
            "Siege Monster. The treant deals double damage to objects and structures."
        ],
        "Actions": [
            "Multiattack. The treant makes two slam attacks.",
            "Slam.Melee Weapon Attack: +10 to hit, reach 5 ft., one target.Hit: 16 (3d6 + 6) bludgeoning damage.",
            "Rock.Ranged Weapon Attack: +10 to hit, range 60/180 ft., one target.Hit: 28 (4d10 + 6) bludgeoning damage.",
            "Animate Trees (1/Day). The treant magically animates one or two trees it can see within 60 feet of it. These trees have the same statistics as a treant, except they have Intelligence and Charisma scores of 1, they can't speak, and they have only the Slam action option. An animated tree acts as an ally of the treant. The tree remains animate for 1 day or until it dies; until the treant dies or is more than 120 feet from the tree; or until the treant takes a bonus action to turn it back into an inanimate tree. The tree then takes root if possible."
        ]
    },
    "tribal-warrior": {
        "name": "Tribal Warrior",
        "type": "Medium humanoid (any race)",
        "alignment": "any alignment",
        "Armor Class": "12 (hide armor)",
        "Hit Points": "11 (2d8 + 2)",
        "Speed": "30 ft.",
        "Senses": "passive Perception 10",
        "Languages": "any one language",
        "Challenge": "1/8 (25 XP)",
        "STR": "13 (+1)",
        "DEX": "11 (+0)",
        "CON": "12 (+1)",
        "INT": "8 (-1)",
        "WIS": "11 (+0)",
        "CHA": "8 (-1)",
        "features": [
            "Pack Tactics. The warrior has advantage on an attack roll against a creature if at least one of the warrior's allies is within 5 feet of the creature and the ally isn't incapacitated."
        ],
        "Actions": [
            "Spear.Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft. or range 20/60 ft., one target.Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack."
        ]
    },
    "triceratops": {
        "name": "Triceratops",
        "type": "Huge beast",
        "alignment": "unaligned",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "95 (10d12 + 30)",
        "Speed": "50 ft.",
        "Senses": "passive Perception 10",
        "Languages": "\u2014",
        "Challenge": "5 (1800 XP)",
        "STR": "22 (+6)",
        "DEX": "9 (-1)",
        "CON": "17 (+3)",
        "INT": "2 (-4)",
        "WIS": "11 (+0)",
        "CHA": "5 (-3)",
        "features": [
            "Trampling Charge. If the triceratops moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 13 Strength saving throw or be knocked prone. If the target is prone, the triceratops can make one stomp attack against it as a bonus action."
        ],
        "Actions": [
            "Gore.Melee Weapon Attack: +9 to hit, reach 5 ft., one target.Hit: 24 (4d8 + 6) piercing damage.",
            "Stomp.Melee Weapon Attack: +9 to hit, reach 5 ft., one prone creature.Hit: 22 (3d10 + 6) bludgeoning damage"
        ]
    },
    "troglodyte": {
        "name": "Troglodyte",
        "type": "Medium humanoid (Troglodyte)",
        "alignment": "chaotic evil",
        "Armor Class": "11 (natural armor)",
        "Hit Points": "13 (2d8 + 4)",
        "Speed": "30 ft.",
        "Skills": "Stealth +2",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Troglodyte",
        "Challenge": "1/4 (50 XP)",
        "STR": "14 (+2)",
        "DEX": "10 (+0)",
        "CON": "14 (+2)",
        "INT": "6 (-2)",
        "WIS": "10 (+0)",
        "CHA": "6 (-2)",
        "features": [
            "Chameleon Skin. The troglodyte has advantage on Dexterity (Stealth) checks made to hide.",
            "Stench. Any creature other than a troglodyte that starts its turn within 5 feet of the troglodyte must succeed on a DC 12 Constitution saving throw or be poisoned until the start of the creature's next turn. On a successful saving throw, the creature is immune to the stench of all troglodytes for 1 hour.",
            "Sunlight Sensitivity. While in sunlight, the troglodyte has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
        ],
        "Actions": [
            "Multiattack. The troglodyte makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 4 (1d4 + 2) piercing damage.",
            "Claw.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 4 (1d4 + 2) slashing damage."
        ]
    },
    "troll": {
        "name": "Troll",
        "type": "Large giant",
        "alignment": "chaotic evil",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "84 (8d10 + 40)",
        "Speed": "30 ft.",
        "Skills": "Perception +2",
        "Senses": "darkvision 60 ft., passive Perception 12",
        "Languages": "Giant",
        "Challenge": "5 (1800 XP)",
        "STR": "18 (+4)",
        "DEX": "13 (+1)",
        "CON": "20 (+5)",
        "INT": "7 (-2)",
        "WIS": "9 (-1)",
        "CHA": "7 (-2)",
        "features": [
            "Keen Smell. The troll has advantage on Wisdom (Perception) checks that rely on smell.",
            "Regeneration. The troll regains 10 hit points at the start of its turn. If the troll takes acid or fire damage, this trait doesn't function at the start of the troll's next turn. The troll dies only if it starts its turn with 0 hit points and doesn't regenerate."
        ],
        "Actions": [
            "Multiattack. The troll makes three attacks: one with its bite and two with its claws.",
            "Bite.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 7 (1d6 + 4) piercing damage.",
            "Claw.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) slashing damage."
        ]
    },
    "tyrannosaurus-rex": {
        "name": "Tyrannosaurus Rex",
        "type": "Huge beast",
        "alignment": "unaligned",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "136 (13d12 + 52)",
        "Speed": "50 ft.",
        "Skills": "Perception +4",
        "Senses": "passive Perception 14",
        "Languages": "\u2014",
        "Challenge": "8 (3900 XP)",
        "STR": "25 (+7)",
        "DEX": "10 (+0)",
        "CON": "19 (+4)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "9 (-1)",
        "features": [],
        "Actions": [
            "Multiattack. The tyrannosaurus makes two attacks: one with its bite and one with its tail. It can't make both attacks against the same target.",
            "Bite.Melee Weapon Attack: +10 to hit, reach 10 ft., one target.Hit: 33 (4d12 + 7) piercing damage. If the target is a Medium or smaller creature, it is grappled (escape DC 17). Until this grapple ends, the target is restrained, and the tyrannosaurus can't bite another target.",
            "Tail.Melee Weapon Attack: +10 to hit, reach 10 ft., one target.Hit: 20 (3d8 + 7) bludgeoning damage."
        ]
    },
    "ultroloth": {
        "name": "Ultroloth",
        "type": "Medium fiend (Yugoloth)",
        "alignment": "neutral evil",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "153 (18d8 + 72)",
        "Speed": "30 ft., fly 60 ft.",
        "Skills": "Intimidation +9, Perception +7, Stealth +8",
        "Damage Resistances": "cold, fire, lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "acid, poison",
        "Condition Immunities": "charmed, frightened, poisoned",
        "Senses": "truesight 120 ft., passive Perception 17",
        "Languages": "Abyssal, Infernal, telepathy 120 ft.",
        "Challenge": "13 (10000 XP)",
        "STR": "16 (+3)",
        "DEX": "16 (+3)",
        "CON": "18 (+4)",
        "INT": "18 (+4)",
        "WIS": "15 (+2)",
        "CHA": "19 (+4)",
        "features": [],
        "Actions": [
            "This full creature's stat block is not available (not OGL)."
        ]
    },
    "umber-hulk": {
        "name": "Umber Hulk",
        "type": "Large monstrosity",
        "alignment": "chaotic evil",
        "Armor Class": "18 (natural armor)",
        "Hit Points": "93 (11d10 + 33)",
        "Speed": "30 ft., burrow 20 ft.",
        "Senses": "darkvision 120 ft., tremorsense 60 ft., passive Perception 10",
        "Languages": "Umber Hulk",
        "Challenge": "5 (1800 XP)",
        "STR": "20 (+5)",
        "DEX": "13 (+1)",
        "CON": "16 (+3)",
        "INT": "9 (-1)",
        "WIS": "10 (+0)",
        "CHA": "10 (+0)",
        "features": [
            "Confusing Caze. When a creature starts its turn within 30 feet of the umber hulk and is able to see the umber hulk's eyes, the umber hulk can magically force it to make a DC 15 Charisma saving throw, unless the umber hulk is incapacitated. On a failed saving throw, the creature can't take reactions until the start of its next turn and rolls a d8 to determine what it does during that turn. On a 1 to 4, the creature does nothing. On a 5 or 6, the creature takes no action but uses all its movement to move in a random direction. On a 7 or 8, the creature makes one melee attack against a random creature, or it does nothing if no creature is within reach. Unless surprised, a creature can avert its eyes to avoid the saving throw at the start of its turn. If the creature does so, it can't see the umber hulk until the start of its next turn, when it can avert its eyes again. If the creature looks at the umber hulk in the meantime, it must immediately make the save.",
            "Tunneler. The umber hulk can burrow through solid rock at half its burrowing speed and leaves a 5 foot-wide, 8-foot-high tunnel in its wake."
        ],
        "Actions": [
            "Multiattack. The umber hulk makes three attacks: two with its claws and one with its mandibles.",
            "Claw.Melee Weapon Attack: +8 to hit, reach 5 ft., one target.Hit: 9 (1d8 + 5) slashing damage.",
            "Mandibles.Melee Weapon Attack: +8 to hit, reach 5 ft., one target.Hit: 14 (2d8 + 5) slashing damage."
        ]
    },
    "unicorn": {
        "name": "Unicorn",
        "type": "Large celestial",
        "alignment": "lawful good",
        "Armor Class": "12",
        "Hit Points": "67 (9d10 + 18)",
        "Speed": "50 ft.",
        "Damage Immunities": "poison",
        "Condition Immunities": "charmed, paralyzed, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 13",
        "Languages": "Celestial, Elvish, Sylvan, telepathy 60 ft.",
        "Challenge": "5 (1800 XP)",
        "STR": "18 (+4)",
        "DEX": "14 (+2)",
        "CON": "15 (+2)",
        "INT": "11 (+0)",
        "WIS": "17 (+3)",
        "CHA": "16 (+3)",
        "Legendary actions": [
            "The unicorn can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The unicorn regains spent legendary actions at the start of its turn.",
            "Hooves. The unicorn makes one attack with its hooves.",
            "Shimmering Shield (Costs 2 Actions). The unicorn creates a shimmering, magical field around itself or another creature it can see within 60 feet of it. The target gains a +2 bonus to AC until the end of the unicorn's next turn.",
            "Heal Self (Costs 3 Actions). The unicorn magically regains 11 (2d8 + 2) hit points."
        ],
        "features": [
            "Charge. If the unicorn moves at least 20 feet straight toward a target and then hits it with a horn attack on the same turn, the target takes an extra 9 (2d8) piercing damage. If the target is a creature, it must succeed on a DC 15 Strength saving throw or be knocked prone.",
            "Innate Spellcasting. The unicorn's innate spellcasting ability is Charisma (spell save DC 14). The unicorn can innately cast the following spells, requiring no components:",
            "Magic Resistance. The unicorn has advantage on saving throws against spells and other magical effects.",
            "Magic Weapons. The unicorn's weapon attacks are magical."
        ],
        "Actions": [
            "Multiattack. The unicorn makes two attacks: one with its hooves and one with its horn.",
            "Hooves.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) bludgeoning damage.",
            "Horn.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 8 (1d8 + 4) piercing damage.",
            "Healing Touch (3/Day). The unicorn touches another creature with its horn. The target magically regains 11 (2d8 + 2) hit points. In addition, the touch removes all diseases and neutralizes all poisons afflicting the target.",
            "Teleport (1/Day). The unicorn magically teleports itself and up to three willing creatures it can see within 5 feet of it, along with any equipment they are wearing or carrying, to a location the unicorn is familiar with, up to 1 mile away."
        ]
    },
    "vampire": {
        "name": "Vampire",
        "type": "Medium undead (Shapechanger)",
        "alignment": "lawful evil",
        "Armor Class": "16 (natural armor)",
        "Hit Points": "144 (17d8 + 68)",
        "Speed": "30 ft.",
        "Saving Throws": "Dex +9, Wis +7, Cha +9",
        "Skills": "Perception +7, Stealth +9",
        "Damage Resistances": "necrotic; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Senses": "darkvision 120 ft., passive Perception 17",
        "Languages": "the languages it knew in life",
        "Challenge": "13 (10000 XP)",
        "STR": "18 (+4)",
        "DEX": "18 (+4)",
        "CON": "18 (+4)",
        "INT": "17 (+3)",
        "WIS": "15 (+2)",
        "CHA": "18 (+4)",
        "Legendary actions": [
            "The vampire can take 3 legendary actions, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The vampire regains spent legendary actions at the start of its turn.",
            "Move. The vampire moves up to its speed without provoking opportunity attacks.",
            "Unarmed Strike. The vampire makes one unarmed strike.",
            "Bite (Costs 2 Actions). The vampire makes one bite attack."
        ],
        "features": [
            "Shapechanger. If the vampire isn't in sunlight or running water, it can use its action to polymorph into a Tiny bat or a Medium cloud of mist, or back into its true form. While in bat form, the vampire can't speak, its walking speed is 5 feet, and it has a flying speed of 30 feet. Its statistics, other than its size and speed, are unchanged. Anything it is wearing transforms with it, but nothing it is carrying does. It reverts to its true form if it dies. While in mist form, the vampire can't take any actions, speak, or manipulate objects. It is weightless, has a flying speed of 20 feet, can hover, and can enter a hostile creature's space and stop there. In addition, if air can pass through a space, the mist can do so without squeezing, and it can't pass through water. It has advantage on Strength, Dexterity, and Constitution saving throws, and it is immune to all nonmagical damage, except the damage it takes from sunlight.",
            "Legendary Resistance (3/Day). If the vampire fails a saving throw, it can choose to succeed instead.",
            "Misty Escape. When it drops to 0 hit points outside its resting place, the vampire transforms into a cloud of mist (as in the Shapechanger trait) instead of falling unconscious, provided that it isn't in sunlight or running water. If it can't transform, it is destroyed. While it has 0 hit points in mist form, it can't revert to its vampire form, and it must reach its resting place within 2 hours or be destroyed. Once in its resting place, it reverts to its vampire form. It is then paralyzed until it regains at least 1 hit point. After spending 1 hour in its resting place with 0 hit points, it regains 1 hit point.",
            "Regeneration. The vampire regains 20 hit points at the start of its turn if it has at least 1 hit point and isn't in sunlight or running water. If the vampire takes radiant damage or damage from holy water, this trait doesn't function at the start of the vampire's next turn.",
            "Spider Climb. The vampire can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.",
            "Vampire Weaknesses. The vampire has the following flaws:",
            "Forbiddance. The vampire can't enter a residence without an invitation from one of the occupants.",
            "Harmed by Running Water. The vampire takes 20 acid damage if it ends its turn in running water.",
            "Stake to the Heart. If a piercing weapon made of wood is driven into the vampire's heart while the vampire is incapacitated in its resting place, the vampire is paralyzed until the stake is removed.",
            "Sunlight Hypersensitivity. The vampire takes 20 radiant damage when it starts its turn in sunlight. While in sunlight, it has disadvantage on attack rolls and ability checks."
        ],
        "Actions": [
            "Multiattack (Vampire Form Only). The vampire makes two attacks, only one of which can be a bite attack.",
            "Unarmed Strike (Vampire Form Only).Melee Weapon Attack: +9 to hit, reach 5 ft., one creature.Hit: 8 (1d8 + 4) bludgeoning damage. Instead of dealing damage, the vampire can grapple the target (escape DC 18).",
            "Bite (Bat or Vampire Form Only).Melee Weapon Attack: +9 to hit, reach 5 ft., one willing creature, or a creature that is grappled by the vampire, incapacitated, or restrained.Hit: 7 (1d6 + 4) piercing damage plus 10 (3d6) necrotic damage. The target's hit point maximum is reduced by an amount equal to the necrotic damage taken, and the vampire regains hit points equal to that amount. The reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0. A humanoid slain in this way and then buried in the ground rises the following night as a vampire spawn under the vampire's control.",
            "Charm. The vampire targets one humanoid it can see within 30 feet of it. If the target can see the vampire, the target must succeed on a DC 17 Wisdom saving throw against this magic or be charmed by the vampire. The charmed target regards the vampire as a trusted friend to be heeded and protected. Although the target isn't under the vampire's control, it takes the vampire's requests or actions in the most favorable way it can, and it is a willing target for the vampire's bit attack. Each time the vampire or the vampire's companions do anything harmful to the target, it can repeat the saving throw, ending the effect on itself on a success. Otherwise, the effect lasts 24 hours or until the vampire is destroyed, is on a different plane of existence than the target, or takes a bonus action to end the effect.",
            "Children ofthe Night (1/Day). The vampire magically calls 2d4 swarms of bats or rats, provided that the sun isn't up. While outdoors, the vampire can call 3d6 wolves instead. The called creatures arrive in 1d4 rounds, acting as allies of the vampire and obeying its spoken commands. The beasts remain for 1 hour, until the vampire dies, or until the vampire dismisses them as a bonus action."
        ]
    },
    "vampire-spawn": {
        "name": "Vampire Spawn",
        "type": "Medium undead",
        "alignment": "neutral evil",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "82 (11d8 + 33)",
        "Speed": "30 ft.",
        "Saving Throws": "Dex +6, Wis +3",
        "Skills": "Perception +3, Stealth +6",
        "Damage Resistances": "necrotic; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Senses": "darkvision 60 ft., passive Perception 13",
        "Languages": "the languages it knew in life",
        "Challenge": "5 (1800 XP)",
        "STR": "16 (+3)",
        "DEX": "16 (+3)",
        "CON": "16 (+3)",
        "INT": "11 (+0)",
        "WIS": "10 (+0)",
        "CHA": "12 (+1)",
        "features": [
            "Regeneration. The vampire regains 10 hit points at the start of its turn if it has at least 1 hit point and isn't in sunlight or running water. If the vampire takes radiant damage or damage from holy water, this trait doesn't function at the start of the vampire's next turn.",
            "Spider Climb. The vampire can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.",
            "Vampire Weaknesses. The vampire has the following flaws:",
            "Forbiddance. The vampire can't enter a residence without an invitation from one of the occupants.",
            "Harmed by Running Water. The vampire takes 20 acid damage when it ends its turn in running water.",
            "Stake to the Heart. The vampire is destroyed if a piercing weapon made of wood is driven into its heart while it is incapacitated in its resting place.",
            "Sunlight Hypersensitivity. The vampire takes 20 radiant damage when it starts its turn in sunlight. While in sunlight, it has disadvantage on attack rolls and ability checks."
        ],
        "Actions": [
            "Multiattack. The vampire makes two attacks, only one of which can be a bite attack.",
            "Claws.Melee Weapon Attack: +6 to hit, reach 5 ft., one creature.Hit: 8 (2d4 + 3) slashing damage. Instead of dealing damage, the vampire can grapple the target (escape DC 13).",
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one willing creature, or a creature that is grappled by the vampire, incapacitated, or restrained.Hit: 6 (1d6 + 3) piercing damage plus 7 (2d6) necrotic damage. The target's hit point maximum is reduced by an amount equal to the necrotic damage taken, and the vampire regains hit points equal to that amount. The reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0."
        ]
    },
    "veteran": {
        "name": "Veteran",
        "type": "Medium humanoid (any race)",
        "alignment": "any alignment",
        "Armor Class": "17 (splint)",
        "Hit Points": "58 (9d8 + 18)",
        "Speed": "30 ft.",
        "Skills": "Athletics +5, Perception +2",
        "Senses": "passive Perception 12",
        "Languages": "any one language (usually Common)",
        "Challenge": "3 (700 XP)",
        "STR": "16 (+3)",
        "DEX": "13 (+1)",
        "CON": "14 (+2)",
        "INT": "10 (+0)",
        "WIS": "11 (+0)",
        "CHA": "10 (+0)",
        "features": [],
        "Actions": [
            "Multiattack. The veteran makes two longsword attacks. If it has a shortsword drawn, it can also make a shortsword attack.",
            "Longsword.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands.",
            "Shortsword.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 6 (1d6 + 3) piercing damage.",
            "Heavy Crossbow.Ranged Weapon Attack: +3 to hit, range 100/400 ft., one target.Hit: 6 (1d10 + 1) piercing damage."
        ]
    },
    "violet-fungus": {
        "name": "Violet Fungus",
        "type": "Medium plant",
        "alignment": "unaligned",
        "Armor Class": "5",
        "Hit Points": "18 (4d8)",
        "Speed": "5 ft.",
        "Condition Immunities": "blinded, deafened, frightened",
        "Senses": "blindsight 30 ft. (blind beyond this radius), passive Perception 6",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "3 (-4)",
        "DEX": "1 (-5)",
        "CON": "10 (+0)",
        "INT": "1 (-5)",
        "WIS": "3 (-4)",
        "CHA": "1 (-5)",
        "features": [
            "False Appearance. While the violet fungus remains motionless, it is indistinguishable from an ordinary fungus."
        ],
        "Actions": [
            "Multiattack. The fungus makes 1d4 Rotting Touch attacks.",
            "Rotting Touch.Melee Weapon Attack: +2 to hit, reach 10 ft., one creature.Hit: 4 (1d8) necrotic damage."
        ]
    },
    "vrock": {
        "name": "Vrock",
        "type": "Large fiend (Demon)",
        "alignment": "chaotic evil",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "104 (11d10 + 44)",
        "Speed": "40 ft., fly 60 ft.",
        "Saving Throws": "Dex +5, Wis +4, Cha +2",
        "Damage Resistances": "cold, fire, lightning; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 120 ft., passive Perception 11",
        "Languages": "Abyssal, telepathy 120 ft.",
        "Challenge": "6 (2300 XP)",
        "STR": "17 (+3)",
        "DEX": "15 (+2)",
        "CON": "18 (+4)",
        "INT": "8 (-1)",
        "WIS": "13 (+1)",
        "CHA": "8 (-1)",
        "features": [
            "Magic Resistance. The vrock has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack. The vrock makes two attacks: one with its beak and one with its talons.",
            "Beak.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) piercing damage.",
            "Talons.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 14 (2d10 + 3) slashing damage.",
            "Spores (Recharge 6). A 15-foot-radius cloud of toxic spores extends out from the vrock. The spores spread around corners. Each creature in that area must succeed on a DC 14 Constitution saving throw or become poisoned. While poisoned in this way, a target takes 5 (1d10) poison damage at the start of each of its turns. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. Emptying a vial of holy water on the target also ends the effect on it.",
            "Stunning Screech (1/Day). The vrock emits a horrific screech. Each creature within 20 feet of it that can hear it and that isn't a demon must succeed on a DC 14 Constitution saving throw or be stunned until the end of the vrock's next turn."
        ]
    },
    "vulture": {
        "name": "Vulture",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "10",
        "Hit Points": "5 (1d8 + 1)",
        "Speed": "10 ft., fly 50 ft.",
        "Skills": "Perception +3",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "7 (-2)",
        "DEX": "10 (+0)",
        "CON": "13 (+1)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "4 (-3)",
        "features": [
            "Keen Sight and Smell. The vulture has advantage on Wisdom (Perception) checks that rely on sight or smell.",
            "Pack Tactics. The vulture has advantage on an attack roll against a creature if at least one of the vulture's allies is within 5 feet of the creature and the ally isn't incapacitated."
        ],
        "Actions": [
            "Beak.Melee Weapon Attack: +2 to hit, reach 5 ft., one target.Hit: 2 (1d4) piercing damage."
        ]
    },
    "warhorse": {
        "name": "Warhorse",
        "type": "Large beast",
        "alignment": "unaligned",
        "Armor Class": "11",
        "Hit Points": "19 (3d10 + 3)",
        "Speed": "60 ft.",
        "Senses": "passive Perception 11",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "18 (+4)",
        "DEX": "12 (+1)",
        "CON": "13 (+1)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Trampling Charge. If the horse moves at least 20 feet straight toward a creature and then hits it with a hooves attack on the same turn, that target must succeed on a DC 14 Strength saving throw or be knocked prone. If the target is prone, the horse can make another attack with its hooves against it as a bonus action."
        ],
        "Actions": [
            "Hooves.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) bludgeoning damage."
        ]
    },
    "warhorse-skeleton": {
        "name": "Warhorse Skeleton",
        "type": "Large undead",
        "alignment": "lawful evil",
        "Armor Class": "13 (barding scraps)",
        "Hit Points": "22 (3d10 + 6)",
        "Speed": "60 ft.",
        "Damage Vulnerabilities": "bludgeoning",
        "Damage Immunities": "poison",
        "Condition Immunities": "exhaustion, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 9",
        "Languages": "\u2014",
        "Challenge": "1/2 (100 XP)",
        "STR": "18 (+4)",
        "DEX": "12 (+1)",
        "CON": "15 (+2)",
        "INT": "2 (-4)",
        "WIS": "8 (-1)",
        "CHA": "5 (-3)",
        "features": [],
        "Actions": [
            "Hooves.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) bludgeoning damage."
        ]
    },
    "water-elemental": {
        "name": "Water Elemental",
        "type": "Large elemental",
        "alignment": "neutral",
        "Armor Class": "14 (natural armor)",
        "Hit Points": "114 (12d10 + 48)",
        "Speed": "30 ft., swim 90 ft.",
        "Damage Resistances": "acid; bludgeoning, piercing, and slashing from nonmagical attacks",
        "Damage Immunities": "poison",
        "Condition Immunities": "exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained, unconscious",
        "Senses": "darkvision 60 ft., passive Perception 10",
        "Languages": "Aquan",
        "Challenge": "5 (1800 XP)",
        "STR": "18 (+4)",
        "DEX": "14 (+2)",
        "CON": "18 (+4)",
        "INT": "5 (-3)",
        "WIS": "10 (+0)",
        "CHA": "8 (-1)",
        "features": [
            "Water Form. The elemental can enter a hostile creature's space and stop there. It can move through a space as narrow as 1 inch wide without squeezing.",
            "Freeze. If the elemental takes cold damage, it partially freezes; its speed is reduced by 20 feet until the end of its next turn."
        ],
        "Actions": [
            "Multiattack. The elemental makes two slam attacks.",
            "Slam.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 13 (2d8 + 4) bludgeoning damage.",
            "Whelm (Recharge 4-6). Each creature in the elemental's space must make a DC 15 Strength saving throw. On a failure, a target takes 13 (2d8 + 4) bludgeoning damage. If it is Large or smaller, it is also grappled (escape DC 14). Until this grapple ends, the target is restrained and unable to breathe unless it can breathe water. If the saving throw is successful, the target is pushed out of the elemental's space. The elemental can grapple one Large creature or up to two Medium or smaller creatures at one time. At the start of each of the elemental's turns, each target grappled by it takes 13 (2d8 + 4) bludgeoning damage. A creature within 5 feet of the elemental can pull a creature or object out of it by taking an action to make a DC 14 Strength check and succeeding."
        ]
    },
    "weasel": {
        "name": "Weasel",
        "type": "Tiny beast",
        "alignment": "unaligned",
        "Armor Class": "13",
        "Hit Points": "1 (1d4 - 1)",
        "Speed": "30 ft.",
        "Skills": "Perception +3, Stealth +5",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "0 (10 XP)",
        "STR": "3 (-4)",
        "DEX": "16 (+3)",
        "CON": "8 (-1)",
        "INT": "2 (-4)",
        "WIS": "12 (+1)",
        "CHA": "3 (-4)",
        "features": [
            "Keen Hearing and Smell. The weasel has advantage on Wisdom (Perception) checks that rely on hearing or smell."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 1 piercing damage."
        ]
    },
    "werebear": {
        "name": "Werebear",
        "type": "Medium humanoid (Human",
        "alignment": "Shapechanger), neutral good",
        "Armor Class": "10 in humanoid form, 11 (natural armor) in bear and hybrid form",
        "Hit Points": "135 (18d8 + 54)",
        "Speed": "30 ft. (40 ft., climb 30 ft. in bear or hybrid form)",
        "Skills": "Perception +7",
        "Damage Immunities": "bludgeoning, piercing, and slashing from nonmagical attacks not made with silvered weapons",
        "Senses": "passive Perception 17",
        "Languages": "Common (can't speak in bear form)",
        "Challenge": "5 (1800 XP)",
        "STR": "19 (+4)",
        "DEX": "10 (+0)",
        "CON": "17 (+3)",
        "INT": "11 (+0)",
        "WIS": "12 (+1)",
        "CHA": "12 (+1)",
        "features": [
            "Shapechanger. The werebear can use its action to polymorph into a Large bear-humanoid hybrid or into a Large bear, or back into its true form, which is humanoid. Its statistics, other than its size and AC, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.",
            "Keen Smell. The werebear has advantage on Wisdom (Perception) checks that rely on smell."
        ],
        "Actions": [
            "Multiattack. In bear form, the werebear makes two claw attacks. In humanoid form, it makes two greataxe attacks. In hybrid form, it can attack like a bear or a humanoid.",
            "Bite (Bear or Hybrid Form Only).Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 15 (2d10 + 4) piercing damage. If the target is a humanoid, it must succeed on a DC 14 Constitution saving throw or be cursed with werebear lycanthropy.",
            "Claw (Bear or Hybrid Form Only).Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 13 (2d8 + 4) slashing damage.",
            "Greataxe (Humanoid or Hybrid Form Only).Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 10 (1d12 + 4) slashing damage."
        ]
    },
    "wereboar": {
        "name": "Wereboar",
        "type": "Medium humanoid (Human",
        "alignment": "Shapechanger), neutral evil",
        "Armor Class": "10 in humanoid form, 11 (natural armor) in boar or hybrid form",
        "Hit Points": "78 (12d8 + 24)",
        "Speed": "30 ft. (40 ft. in boar form)",
        "Skills": "Perception +2",
        "Damage Immunities": "bludgeoning, piercing, and slashing damage from nonmagical attacks that aren't silvered",
        "Senses": "passive Perception 12",
        "Languages": "Common (can't speak in boar form)",
        "Challenge": "4 (1100 XP)",
        "STR": "17 (+3)",
        "DEX": "10 (+0)",
        "CON": "15 (+2)",
        "INT": "10 (+0)",
        "WIS": "11 (+0)",
        "CHA": "8 (-1)",
        "features": [
            "Shapechanger. The wereboar can use its action to polymorph into a boar-humanoid hybrid or into a boar, or back into its true form, which is humanoid. Its statistics, other than its AC, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.",
            "Charge (Boar or Hybrid Form Only). If the wereboar moves at least 15 feet straight toward a target and then hits it with its tusks on the same turn, the target takes an extra 7 (2d6) slashing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone.",
            "Relentless (Recharges after a Short or Long Rest). If the wereboar takes 14 damage or less that would reduce it to 0 hit points, it is reduced to 1 hit point instead."
        ],
        "Actions": [
            "Multiattack (Humanoid or Hybrid Form Only). The wereboar makes two attacks, only one of which can be with its tusks.",
            "Maul (Humanoid or Hybrid Form Only).Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) bludgeoning damage.",
            "Tusks (Boar or Hybrid Form Only).Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) slashing damage. If the target is a humanoid, it must succeed on a DC 12 Constitution saving throw or be cursed with wereboar lycanthropy."
        ]
    },
    "wererat": {
        "name": "Wererat",
        "type": "Medium humanoid (Human",
        "alignment": "Shapechanger), lawful evil",
        "Armor Class": "12",
        "Hit Points": "33 (6d8 + 6)",
        "Speed": "30 ft.",
        "Skills": "Perception +2, Stealth +4",
        "Damage Immunities": "bludgeoning, piercing, and slashing from nonmagical attacks not made with silvered weapons",
        "Senses": "darkvision 60 ft. (rat form only), passive Perception 12",
        "Languages": "Common (can't speak in rat form)",
        "Challenge": "2 (450 XP)",
        "STR": "10 (+0)",
        "DEX": "15 (+2)",
        "CON": "12 (+1)",
        "INT": "11 (+0)",
        "WIS": "10 (+0)",
        "CHA": "8 (-1)",
        "features": [
            "Shapechanger. The wererat can use its action to polymorph into a rat-humanoid hybrid or into a giant rat, or back into its true form, which is humanoid. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.",
            "Keen Smell. The wererat has advantage on Wisdom (Perception) checks that rely on smell."
        ],
        "Actions": [
            "Multiattack (Humanoid or Hybrid Form Only). The wererat makes two attacks, only one of which can be a bite.",
            "Bite (Rat or Hybrid Form Only).Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 4 (1d4 + 2) piercing damage. If the target is a humanoid, it must succeed on a DC 11 Constitution saving throw or be cursed with wererat lycanthropy.",
            "Shortsword (Humanoid or Hybrid Form Only).Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 5 (1d6 + 2) piercing damage.",
            "Hand Crossbow (Humanoid or Hybrid Form Only).Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target.Hit: 5 (1d6 + 2) piercing damage."
        ]
    },
    "weretiger": {
        "name": "Weretiger",
        "type": "Medium humanoid (Human",
        "alignment": "Shapechanger), neutral",
        "Armor Class": "12",
        "Hit Points": "120 (16d8 + 48)",
        "Speed": "30 ft. (40 ft. in tiger form)",
        "Skills": "Perception +5, Stealth +4",
        "Damage Immunities": "bludgeoning, piercing, and slashing from nonmagical attacks not made with silvered weapons",
        "Senses": "darkvision 60 ft., passive Perception 15",
        "Languages": "Common (can't speak in tiger form)",
        "Challenge": "4 (1100 XP)",
        "STR": "17 (+3)",
        "DEX": "15 (+2)",
        "CON": "16 (+3)",
        "INT": "10 (+0)",
        "WIS": "13 (+1)",
        "CHA": "11 (+0)",
        "features": [
            "Shapechanger. The weretiger can use its action to polymorph into a tiger-humanoid hybrid or into a tiger, or back into its true form, which is humanoid. Its statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.",
            "Keen Hearing and Smell. The weretiger has advantage on Wisdom (Perception) checks that rely on hearing or smell.",
            "Pounce (Tiger or Hybrid Form Only). If the weretiger moves at least 15 feet straight toward a creature and then hits it with a claw attack on the same turn, that target must succeed on a DC 14 Strength saving throw or be knocked prone. If the target is prone, the weretiger can make one bite attack against it as a bonus action."
        ],
        "Actions": [
            "Multiattack (Humanoid or Hybrid Form Only). In humanoid form, the weretiger makes two scimitar attacks or two longbow attacks. In hybrid form, it can attack like a humanoid or make two claw attacks.",
            "Bite (Tiger or Hybrid Form Only).Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 8 (1d10 + 3) piercing damage. If the target is a humanoid, it must succeed on a DC 13 Constitution saving throw or be cursed with weretiger lycanthropy.",
            "Claw (Tiger or Hybrid Form Only).Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 7 (1d8 + 3) slashing damage.",
            "Scimitar (Humanoid or Hybrid Form Only).Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 6 (1d6 + 3) slashing damage.",
            "Longbow (Humanoid or Hybrid Form Only).Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target.Hit: 6 (1d8 + 2) piercing damage."
        ]
    },
    "werewolf": {
        "name": "Werewolf",
        "type": "Medium humanoid (Human",
        "alignment": "Shapechanger), chaotic evil",
        "Armor Class": "11 in humanoid form, 12 (natural armor) in wolf or hybrid form",
        "Hit Points": "58 (9d8 + 18)",
        "Speed": "30 ft. (40 ft. in wolf form)",
        "Skills": "Perception +4, Stealth +3",
        "Damage Immunities": "bludgeoning, piercing, and slashing damage from nonmagical attacks that aren't silvered",
        "Senses": "passive Perception 14",
        "Languages": "Common (can't speak in wolf form)",
        "Challenge": "3 (700 XP)",
        "STR": "15 (+2)",
        "DEX": "13 (+1)",
        "CON": "14 (+2)",
        "INT": "10 (+0)",
        "WIS": "11 (+0)",
        "CHA": "10 (+0)",
        "features": [
            "Shapechanger. The werewolf can use its action to polymorph into a wolf-humanoid hybrid or into a wolf, or back into its true form, which is humanoid. Its statistics, other than its AC, are the same in each form. Any equipment it is wearing or carrying isn't transformed. It reverts to its true form if it dies.",
            "Keen Hearing and Smell. The werewolf has advantage on Wisdom (Perception) checks that rely on hearing or smell."
        ],
        "Actions": [
            "Multiattack (Humanoid or Hybrid Form Only). The werewolf makes two attacks: two with its spear (humanoid form) or one with its bite and one with its claws (hybrid form).",
            "Bite (Wolf or Hybrid Form Only).Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 6 (1d8 + 2) piercing damage. If the target is a humanoid, it must succeed on a DC 12 Constitution saving throw or be cursed with werewolf lycanthropy.",
            "Claws (Hybrid Form Only).Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 7 (2d4 + 2) slashing damage.",
            "Spear (Humanoid Form Only).Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one creature.Hit: 5 (1d6 + 2) piercing damage, or 6 (1d8 + 2) piercing damage if used with two hands to make a melee attack."
        ]
    },
    "white-dragon-wyrmling": {
        "name": "White Dragon Wyrmling",
        "type": "Medium dragon (Chromatic)",
        "alignment": "chaotic evil",
        "Armor Class": "16 (natural armor)",
        "Hit Points": "32 (5d8 + 10)",
        "Speed": "30 ft., burrow 15 ft., fly 60 ft., swim 30 ft.",
        "Saving Throws": "Dex +2, Con +4, Wis +2, Cha +2",
        "Skills": "Perception +4, Stealth +2",
        "Damage Immunities": "cold",
        "Senses": "blindsight 10 ft., darkvision 60 ft., passive Perception 14",
        "Languages": "Draconic",
        "Challenge": "2 (450 XP)",
        "STR": "14 (+2)",
        "DEX": "10 (+0)",
        "CON": "14 (+2)",
        "INT": "5 (-3)",
        "WIS": "10 (+0)",
        "CHA": "11 (+0)",
        "features": [],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 7 (1d10 + 2) piercing damage plus 2 (1d4) cold damage.",
            "Cold Breath (Recharge 5-6). The dragon exhales an icy blast of hail in a 15-foot cone. Each creature in that area must make a DC 12 Constitution saving throw, taking 22 (5d8) cold damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "wight": {
        "name": "Wight",
        "type": "Medium undead",
        "alignment": "neutral evil",
        "Armor Class": "14 (studded leather)",
        "Hit Points": "45 (6d8 + 18)",
        "Speed": "30 ft.",
        "Skills": "Perception +3, Stealth +4",
        "Damage Resistances": "necrotic; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered",
        "Damage Immunities": "poison",
        "Condition Immunities": "exhaustion, poisoned",
        "Senses": "darkvision 60 ft., passive Perception 13",
        "Languages": "the languages it knew in life",
        "Challenge": "3 (700 XP)",
        "STR": "15 (+2)",
        "DEX": "14 (+2)",
        "CON": "16 (+3)",
        "INT": "10 (+0)",
        "WIS": "13 (+1)",
        "CHA": "15 (+2)",
        "features": [
            "Sunlight Sensitivity. While in sunlight, the wight has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
        ],
        "Actions": [
            "Multiattack. The wight makes two longsword attacks or two longbow attacks. It can use its Life Drain in place of one longsword attack.",
            "Life Drain.Melee Weapon Attack: +4 to hit, reach 5 ft., one creature.Hit: 5 (1d6 + 2) necrotic damage. The target must succeed on a DC 13 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0. A humanoid slain by this attack rises 24 hours later as a zombie under the wight's control, unless the humanoid is restored to life or its body is destroyed. The wight can have no more than twelve zombies under its control at one time.",
            "Longsword.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 6 (1d8 + 2) slashing damage, or 7 (1d10 + 2) slashing damage if used with two hands.",
            "Longbow.Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target.Hit: 6 (1d8 + 2) piercing damage."
        ]
    },
    "will-o'-wisp": {
        "features": []
    },
    "winter-wolf": {
        "name": "Winter Wolf",
        "type": "Large monstrosity",
        "alignment": "neutral evil",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "75 (10d10 + 20)",
        "Speed": "50 ft.",
        "Skills": "Perception +5, Stealth +3",
        "Damage Immunities": "cold",
        "Senses": "passive Perception 15",
        "Languages": "Common, Giant, Winter Wolf",
        "Challenge": "3 (700 XP)",
        "STR": "18 (+4)",
        "DEX": "13 (+1)",
        "CON": "14 (+2)",
        "INT": "7 (-2)",
        "WIS": "12 (+1)",
        "CHA": "8 (-1)",
        "features": [
            "Keen Hearing and Smell. The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell.",
            "Pack Tactics. The wolf has advantage on an attack roll against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally isn't incapacitated.",
            "Snow Camouflage. The wolf has advantage on Dexterity (Stealth) checks made to hide in snowy terrain."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) piercing damage. If the target is a creature, it must succeed on a DC 14 Strength saving throw or be knocked prone.",
            "Cold Breath (Recharge 5-6). The wolf exhales a blast of freezing wind in a 15-foot cone. Each creature in that area must make a DC 12 Dexterity saving throw, taking 18 (4d8) cold damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "wolf": {
        "name": "Wolf",
        "type": "Medium beast",
        "alignment": "unaligned",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "11 (2d8 + 2)",
        "Speed": "40 ft.",
        "Skills": "Perception +3, Stealth +4",
        "Senses": "passive Perception 13",
        "Languages": "\u2014",
        "Challenge": "1/4 (50 XP)",
        "STR": "12 (+1)",
        "DEX": "15 (+2)",
        "CON": "12 (+1)",
        "INT": "3 (-4)",
        "WIS": "12 (+1)",
        "CHA": "6 (-2)",
        "features": [
            "Keen Hearing and Smell. The wolf has advantage on Wisdom (Perception) checks that rely on hearing or smell.",
            "Pack Tactics. The wolf has advantage on attack rolls against a creature if at least one of the wolf's allies is within 5 feet of the creature and the ally isn't incapacitated."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +4 to hit, reach 5 ft., one target.Hit: 7 (2d4 + 2) piercing damage. If the target is a creature, it must succeed on a DC 11 Strength saving throw or be knocked prone."
        ]
    },
    "worg": {
        "name": "Worg",
        "type": "Large monstrosity",
        "alignment": "neutral evil",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "26 (4d10 + 4)",
        "Speed": "50 ft.",
        "Skills": "Perception +4",
        "Senses": "darkvision 60 ft., passive Perception 14",
        "Languages": "Goblin, Worg",
        "Challenge": "1/2 (100 XP)",
        "STR": "16 (+3)",
        "DEX": "13 (+1)",
        "CON": "13 (+1)",
        "INT": "7 (-2)",
        "WIS": "11 (+0)",
        "CHA": "8 (-1)",
        "features": [
            "Keen Hearing and Smell. The worg has advantage on Wisdom (Perception) checks that rely on hearing or smell."
        ],
        "Actions": [
            "Bite.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) piercing damage. If the target is a creature, it must succeed on a DC 13 Strength saving throw or be knocked prone."
        ]
    },
    "wraith": {
        "name": "Wraith",
        "type": "Medium undead",
        "alignment": "neutral evil",
        "Armor Class": "13",
        "Hit Points": "67 (9d8 + 27)",
        "Speed": "0 ft., fly 60 ft. (hover)",
        "Damage Resistances": "acid, cold, fire, lightning, thunder; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered",
        "Damage Immunities": "necrotic, poison",
        "Condition Immunities": "charmed, exhaustion, grappled, paralyzed, petrified, poisoned, prone, restrained",
        "Senses": "darkvision 60 ft., passive Perception 12",
        "Languages": "the languages it knew in life",
        "Challenge": "5 (1800 XP)",
        "STR": "6 (-2)",
        "DEX": "16 (+3)",
        "CON": "16 (+3)",
        "INT": "12 (+1)",
        "WIS": "14 (+2)",
        "CHA": "15 (+2)",
        "features": [
            "Incorporeal Movement. The wraith can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.",
            "Sunlight Sensitivity. While in sunlight, the wraith has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight."
        ],
        "Actions": [
            "Life Drain.Melee Weapon Attack: +6 to hit, reach 5 ft., one creature.Hit: 21 (4d8 + 3) necrotic damage. The target must succeed on a DC 14 Constitution saving throw or its hit point maximum is reduced by an amount equal to the damage taken. This reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0.",
            "Create Specter. The wraith targets a humanoid within 10 feet of it that has been dead for no longer than 1 minute and died violently. The target's spirit rises as a specter in the space of its corpse or in the nearest unoccupied space. The specter is under the wraith's control. The wraith can have no more than seven specters under its control at one time."
        ]
    },
    "wyvern": {
        "name": "Wyvern",
        "type": "Large dragon",
        "alignment": "unaligned",
        "Armor Class": "13 (natural armor)",
        "Hit Points": "110 (13d10 + 39)",
        "Speed": "20 ft., fly 80 ft.",
        "Skills": "Perception +4",
        "Senses": "darkvision 60 ft., passive Perception 14",
        "Languages": "\u2014",
        "Challenge": "6 (2300 XP)",
        "STR": "19 (+4)",
        "DEX": "10 (+0)",
        "CON": "16 (+3)",
        "INT": "5 (-3)",
        "WIS": "12 (+1)",
        "CHA": "6 (-2)",
        "features": [],
        "Actions": [
            "Multiattack. The wyvern makes two attacks: one with its bite and one with its stinger. While flying, it can use its claws in place of one other attack.",
            "Bite.Melee Weapon Attack: +7 to hit, reach 10 ft., one creature.Hit: 11 (2d6 + 4) piercing damage.",
            "Claws.Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 13 (2d8 + 4) slashing damage.",
            "Stinger.Melee Weapon Attack: +7 to hit, reach 10 ft., one creature.Hit: 11 (2d6 + 4) piercing damage. The target must make a DC 15 Constitution saving throw, taking 24 (7d6) poison damage on a failed save, or half as much damage on a successful one."
        ]
    },
    "xorn": {
        "name": "Xorn",
        "type": "Medium elemental",
        "alignment": "neutral",
        "Armor Class": "19 (natural armor)",
        "Hit Points": "73 (7d8 + 42)",
        "Speed": "20 ft., burrow 20 ft.",
        "Skills": "Perception +6, Stealth +3",
        "Damage Resistances": "piercing and slashing from nonmagical attacks that aren't adamantine",
        "Senses": "darkvision 60 ft., tremorsense 60 ft., passive Perception 16",
        "Languages": "Terran",
        "Challenge": "5 (1800 XP)",
        "STR": "17 (+3)",
        "DEX": "10 (+0)",
        "CON": "22 (+6)",
        "INT": "11 (+0)",
        "WIS": "10 (+0)",
        "CHA": "11 (+0)",
        "features": [
            "Earth Glide. The xorn can burrow through nonmagical, unworked earth and stone. While doing so, the xorn doesn't disturb the material it moves through.",
            "Stone Camouflage. The xorn has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.",
            "Treasure Sense. The xorn can pinpoint, by scent, the location of precious metals and stones, such as coins and gems, within 60 feet of it."
        ],
        "Actions": [
            "Multiattack. The xorn makes three claw attacks and one bite attack.",
            "Claw.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 6 (1d6 + 3) slashing damage.",
            "Bite.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 13 (3d6 + 3) piercing damage."
        ]
    },
    "yeti": {
        "name": "Yeti",
        "type": "Large monstrosity",
        "alignment": "chaotic evil",
        "Armor Class": "12 (natural armor)",
        "Hit Points": "51 (6d10 + 18)",
        "Speed": "40 ft., climb 40 ft.",
        "Skills": "Perception +3, Stealth +3",
        "Damage Immunities": "cold",
        "Senses": "darkvision 60 ft., passive Perception 13",
        "Languages": "Yeti",
        "Challenge": "3 (700 XP)",
        "STR": "18 (+4)",
        "DEX": "13 (+1)",
        "CON": "16 (+3)",
        "INT": "8 (-1)",
        "WIS": "12 (+1)",
        "CHA": "7 (-2)",
        "features": [
            "Fear of Fire. If the yeti takes fire damage, it has disadvantage on attack rolls and ability checks until the end of its next turn.",
            "Keen Smell. The yeti has advantage on Wisdom (Perception) checks that rely on smell.",
            "Snow Camouflage. The yeti has advantage on Dexterity (Stealth) checks made to hide in snowy terrain."
        ],
        "Actions": [
            "Multiattack. The yeti can use its Chilling Gaze and makes two claw attacks.",
            "Claw.Melee Weapon Attack: +6 to hit, reach 5 ft., one target.Hit: 7 (1d6 + 4) slashing damage plus 3 (1d6) cold damage.",
            "Chilling Gaze. The yeti targets one creature it can see within 30 feet of it. If the target can see the yeti, the target must succeed on a DC 13 Constitution saving throw against this magic or take 10 (3d6) cold damage and then be paralyzed for 1 minute, unless it is immune to cold damage. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If the target's saving throw is successful, or if the effect ends on it, the target is immune to the Chilling Gaze of all yetis (but not abominable yetis) for 1 hour."
        ]
    },
    "yuan-ti-abomination": {
        "name": "Yuan-ti Abomination",
        "type": "Large monstrosity (Shapechanger",
        "alignment": "Yuan-ti), neutral evil",
        "Armor Class": "15 (natural armor)",
        "Hit Points": "127 (15d10 + 45)",
        "Speed": "40 ft.",
        "Skills": "Perception +5, Stealth +6",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 60 ft., passive Perception 15",
        "Languages": "Abyssal, Common, Draconic",
        "Challenge": "7 (2900 XP)",
        "STR": "19 (+4)",
        "DEX": "16 (+3)",
        "CON": "17 (+3)",
        "INT": "17 (+3)",
        "WIS": "15 (+2)",
        "CHA": "18 (+4)",
        "features": [
            "Shapechanger. The yuan-ti can use its action to polymorph into a Large snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It doesn't change form if it dies.",
            "Innate Spellcasting (Abomination Form Only). The yuan-ti's innate spellcasting ability is Charisma (spell save DC 15). The yuan-ti can innately cast the following spells, requiring no material components:",
            "Magic Resistance. The yuan-ti has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack (Abomination Form Only). The yuan-ti makes two ranged attacks or three melee attacks, but can use its bite and constrict attacks only once each.",
            "Bite.Melee Weapon Attack: +7 to hit, reach 5 ft., one creature.Hit: 7 (1d6 + 4) piercing damage plus 10 (3d6) poison damage.",
            "Constrict.Melee Weapon Attack: +7 to hit, reach 10 ft., one target.Hit: 11 (2d6 + 4) bludgeoning damage, and the target is grappled (escape DC 14). Until this grapple ends, the target is restrained, and the yuan-ti can't constrict another target.",
            "Scimitar (Abomination Form Only).Melee Weapon Attack: +7 to hit, reach 5 ft., one target.Hit: 11 (2d6 + 4) slashing damage.",
            "Longbow (Abomination Form Only).Ranged Weapon Attack: +6 to hit, range 150/600 ft., one target.Hit: 12 (2d8 + 3) piercing damage plus 10 (3d6) poison damage."
        ]
    },
    "yuan-ti-malison": {
        "name": "Yuan-ti Malison",
        "type": "Medium monstrosity (Shapechanger",
        "alignment": "Yuan-ti), neutral evil",
        "Armor Class": "12",
        "Hit Points": "66 (12d8 + 12)",
        "Speed": "30 ft.",
        "Skills": "Deception +5, Stealth +4",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 60 ft., passive Perception 11",
        "Languages": "Abyssal, Common, Draconic",
        "Challenge": "3 (700 XP)",
        "STR": "16 (+3)",
        "DEX": "14 (+2)",
        "CON": "13 (+1)",
        "INT": "14 (+2)",
        "WIS": "12 (+1)",
        "CHA": "16 (+3)",
        "features": [
            "Shapechanger. The yuan-ti can use its action to polymorph into a Medium snake, or back into its true form. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed. It doesn't change form if it dies.",
            "Innate Spellcasting (Yuan-ti Form Only). The yuan-ti's innate spellcasting ability is Charisma (spell save DC 13). The yuan-ti can innately cast the following spells, requiring no material components:",
            "Magic Resistance. The yuan-ti has advantage on saving throws against spells and other magical effects.",
            "Malison Type. The yuan-ti has one of the following types:"
        ],
        "Actions": [
            "Multiattack (Yuan-ti Form Only). The yuan-ti makes two ranged attacks or two melee attacks, but can constrict only once.",
            "Bite (Snake Form Only).Melee Weapon Attack: +5 to hit, reach 5 ft., one creature.Hit: 5 (1d4 + 3) piercing damage plus 7 (2d6) poison damage.",
            "Constrict.Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 10 (2d6 + 3) bludgeoning damage, and the target is grappled (escape DC 13). Until this grapple ends, the target is restrained, and the yuan-ti can't constrict another target.",
            "Scimitar (Yuan-ti Form Only).Melee Weapon Attack: +5 to hit, reach 5 ft., one target.Hit: 6 (1d6 + 3) slashing damage.",
            "Longbow (Yuan-ti Form Only).Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target.Hit: 6 (1d8 + 2) piercing damage."
        ]
    },
    "yuan-ti-pureblood": {
        "name": "Yuan-ti Pureblood",
        "type": "Medium humanoid (Yuan-ti)",
        "alignment": "neutral evil",
        "Armor Class": "11",
        "Hit Points": "40 (9d8)",
        "Speed": "30 ft.",
        "Skills": "Deception +6, Perception +3, Stealth +3",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 60 ft., passive Perception 13",
        "Languages": "Abyssal, Common, Draconic",
        "Challenge": "1 (200 XP)",
        "STR": "11 (+0)",
        "DEX": "12 (+1)",
        "CON": "11 (+0)",
        "INT": "13 (+1)",
        "WIS": "12 (+1)",
        "CHA": "14 (+2)",
        "features": [
            "Innate Spellcasting. The yuan-ti's spellcasting ability is Charisma (spell save DC 12). The yuan-ti can innately cast the following spells, requiring no material components:",
            "Magic Resistance. The yuan-ti has advantage on saving throws against spells and other magical effects."
        ],
        "Actions": [
            "Multiattack. The yuan-ti makes two melee attacks.",
            "Scimitar.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 4 (1d6 + 1) slashing damage.",
            "Shortbow.Ranged Weapon Attack: +3 to hit, range 80/320 ft., one target.Hit: 4 (1d6 + 1) piercing damage plus 7 (2d6) poison damage."
        ]
    },
    "zombie": {
        "name": "Zombie",
        "type": "Medium undead",
        "alignment": "neutral evil",
        "Armor Class": "8",
        "Hit Points": "22 (3d8 + 9)",
        "Speed": "20 ft.",
        "Saving Throws": "Wis +0",
        "Damage Immunities": "poison",
        "Condition Immunities": "poisoned",
        "Senses": "darkvision 60 ft., passive Perception 8",
        "Languages": "understands the languages it knew in life but can't speak",
        "Challenge": "1/4 (50 XP)",
        "STR": "13 (+1)",
        "DEX": "6 (-2)",
        "CON": "16 (+3)",
        "INT": "3 (-4)",
        "WIS": "6 (-2)",
        "CHA": "5 (-3)",
        "features": [
            "Undead Fortitude. If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie drops to 1 hit point instead."
        ],
        "Actions": [
            "Slam.Melee Weapon Attack: +3 to hit, reach 5 ft., one target.Hit: 4 (1d6 + 1) bludgeoning damage."
        ]
    }
}