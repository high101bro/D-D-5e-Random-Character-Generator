#! /usr/bin/env python3

# character = {
#     'profile' : {
        # 'name' : {
        #     'first' : "",
        #     'last' : ""

#     'items' : {
#         'armor' : {
#             'name' : "",
#             'class' : 0,
#             'type' : "",
#             'stealth' : "",
#             'strength' : 0,
#             'properties' : [],
#             'description' : "",
#         },
#         'tools' : [],
#         'items' : [],
#     },
# }
# print(character)

import random, os, datetime
from dnd_lists import *
from dnd_races import *
from dnd_classes import *
from dnd_backgrounds import *
from dnd_random_generation import *
from dnd_helper import *
from dnd_spells import *

item_list = [generate_item_list() for _ in range(10)]
weapon_list = [generate_weapon_list() for _ in range(10)]


class Character():
    def __init__(self):
        self.profile = {}
        self.character_race = {}
        self.character_class = {}
        self.description = {
            'age' : 0,
            'height' : 0,
            'weight' : 0,
            'skin_color' : "None",
            'description' : "None",
            'eye_color' : "None",
            'ear_type' : "None",
            'hair_color' : "None",
            'hair_type' : "None",
            'hair_length' : "None",
            'hair_style' : "None",
            'facial_hair' : "None",
            'facial_hair_color' : "None",
            'body_type' : "None",
            'body_shape' : "None",
            'body_features' : "None",
            'clothing' : "None",
            'accessories' : "None",
            'voice' : "None",
            'mannerisms' : "None",
            'personality' : "None",
        }
        self.background = {}

        #         'traits' : {
        #             'personality' : [],
        #             'feats' : [],
        #             'ideals' : [],
        #             'bonds' : [],
        #             'flaws' : []
        #         },
        #         'all_proficiencies' : [],
        #         'all_languages' : []
        self.level_chart = {}
        self.attributes = {}
        self.capabilities = {}
        self.skills = {}
        self.features = {}
        self.money = {
            'cp' : 0,
            'sp' : 0,
            'ep' : 0,
            'gp' : 0,
            'pp' : 0
        }
        self.items = []
        self.armor = []
        self.weapons = {}
        self.combat = {}
        self.spells = {
            "Spellcasting" : "",
            "Preparation" : "",
            "Spellcasting Modifier" : "",
            "Attack Modifier" : 0,
            "Save DC" : 0,
            "Slots" : {}
        }
    def to_dict(self):
        return {
            'profile' : self.profile,
            'character_race' : self.character_race,
            'character_class' : self.character_class,
            'description' : self.description,
            'background' : self.background,
            'level_chart' : self.level_chart,
            'attributes' : self.attributes,
            'capabilities' : self.capabilities,
            'skills' : self.skills,
            'features' : self.features,
            'money' : self.money,
            'items' : self.items,
            'armor' : self.armor,
            'weapons' : self.weapons,
            'combat' : self.combat,
            'spells' : self.spells,
        }

# Create random character
def generate_characters(character, character_number, character_level=1, character_race='Human', character_class='Fighter'):

    character.profile['character number'] = character_number
    character.profile['created'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%S"))
    character.profile['name'] = {}
    character.profile['name']['first'] = random.choice(first_names)
    character.profile['name']['last'] = random.choice(last_names)
    character.profile['level'] = character_level
    character.profile['proficiency bonus'] = dnd_proficiency_bonus.get(character_level, '1')
    character.profile['experience'] = dnd_levels_exp.get(character_level, '1')    
    character.profile['alignment'] = random.choice(list(dnd_alignments))


    character.character_race = dnd_races[character_race]


    character.character_class["ASCII Art"] = dnd_classes[character_class]["ASCII Art"]
    character.character_class["Name"] = dnd_classes[character_class]["Name"]
    character.character_class["Description"] = dnd_classes[character_class]["Description"]
    character.character_class["Requirements"] = dnd_classes[character_class]["Requirements"]
    character.character_class["Hit Die"] = dnd_classes[character_class]["Hit Die"]
    character.character_class["Current Level Chart"] = {}
    character.character_class["Current Level Chart"][character_level] = dnd_classes[character_class]["Level Chart"][int(character_level)]
    character.character_class["Features"] = dnd_classes[character_class]["Features"]
    character.character_class["Attribute Priority"] = dnd_classes[character_class]["Attribute Priority"]
    character.character_class["Spells"] = dnd_classes[character_class]["Spells"]


    character.description['age'] = random.randint(18, 80)
    character.description['gender'] = str(random.choice(list(['Male','Female','Hermaphrodite','Non-Binary','Transgender','Unknown','Other','None'])))
    character.description['race'] = str(character_race)
    character.description['class'] = str(character_class)
    character.description['height'] = random.randint(60, 80)
    character.description['weight'] = random.randint(100, 300)

    character.description['skin_type'] = str(random.choice(list(['skin','skin and scales','skin and fur', 'skin and featthers',
                                                             'skin, scales, and fur', 'skin, scales, and feathers', 'skin, fur, and feathers',
                                                             'scales','scales and skin', 'scales and fur', 'scales and feathers',
                                                             'scales, skin, and fur', 'scales, skin, and feathers', 'scales, fur, and features'
                                                             'fur', 'fur and skin', 'fur and scales', 'fur and features',
                                                             'fur, skin, and scales', 'fur, skin, and feathers', 'fur, scales, and feathers',
                                                             'feathers', 'feathers and skin', 'feathers and scales', 'feathers and fur',
                                                             'feathers, skin, and scales', 'feathers, skin, and fur', 'feathers, scales, and fur',
                                                             'skin, scales, fur, and feathers','other', 'unknown'])))
    character.description['skin_color'] = str(random.choice(list(['White','Black','Brown','Red','Yellow','Green','Blue','Purple','Orange','Pink','Gray','Other'])))
    character.description['skin_texture'] = str(random.choice(list(['Smooth','Rough','Scales','Feathers','Other'])))
    character.description['skin_thickness'] = str(random.choice(list(['Thin','Thick','Other'])))
    character.description['skin_scent'] = str(random.choice(list(['None','Scentless','Scented','Good Smell','Bad Oder','Other'])))
    character.description['skin_defect'] = str(random.choice(list(['None','Scars','Burns','Piercings','Other'])))

    character.description['eye_shape'] = str(random.choice(list(['None','Almond','Round','Oval','Other'])))
    character.description['eye_size'] = str(random.choice(list(['None','Small','Medium','Large','Other'])))
    character.description['eye_color'] = str(random.choice(list(['White','Black','Brown','Red','Yellow','Green','Blue','Purple','Orange','Pink','Gray','Other'])))
    character.description['eye_lashes'] = str(random.choice(list(['None','Short','Medium','Long','Other'])))
    character.description['eye_brows'] = str(random.choice(list(['None','Short','Medium','Long','Other'])))
    character.description['eye_lids'] = str(random.choice(list(['None','Single','Double','Other'])))
    character.description['eye_features'] = str(random.choice(list(['None','Scar','Piercing','Other'])))
    character.description['eye_sight'] = str(random.choice(list(['None','Normal','Going Blind','Cataracts','Eye Patch','Missing an Eye','Other'])))
    
    character.description['nose_shape'] = str(random.choice(list(['None','Pointed','Flat','Wide','Other'])))
    character.description['nose_length'] = str(random.choice(list(['None','Short','Medium','Long','Other'])))
    character.description['nose_size'] = str(random.choice(list(['None','Small','Medium','Large','Other'])))
    character.description['nose_holes'] = str(random.choice(list(['None','Small','Medium','Large','Other'])))
    character.description['nose_bridge'] = str(random.choice(list(['None','Straight','Curved','Other'])))
    character.description['nose_tip'] = str(random.choice(list(['None','Round','Pointed','Other'])))
    character.description['nose_features'] = str(random.choice(list(['None','Scar','Piercing','Other']))) 

    character.description['chine_shape'] = str(random.choice(list(['None','Pointed','Flat','Wide','Other'])))
    character.description['chine_length'] = str(random.choice(list(['None','Short','Medium','Long','Other'])))
    character.description['chine_size'] = str(random.choice(list(['None','Small','Medium','Large','Other'])))
    character.description['chine_features'] = str(random.choice(list(['None','Scar','Piercing','Other'])))

    character.description['ear_shape'] = str(random.choice(list(['None','Pointed','Flat','Wide','Other'])))
    character.description['ear_size'] = str(random.choice(list(['None','Small','Medium','Large','Other'])))
    character.description['ear_features'] = str(random.choice(list(['None','Scar','Piercing','Other'])))
    character.description['ear_type'] = str(random.choice(list(['square', 'pointed', 'narrow', 'protruding, with a broad lobe, with an attached lobe',
                                                            'Normal ears','Protruding ears & earlobes','Attached ears & earlobes','Small','Big','Folded','Floppy'])))

    character.description['hair_color'] = str(random.choice(list(['White','Black','Brown','Red','Yellow','Green','Blue','Purple','Orange','Pink','Gray','Other'])))
    character.description['hair_type'] = str(random.choice(list(['Straight','Wavy','Curly','Kinky','Bald','Other'])))
    character.description['hair_length'] = str(random.choice(list(['Bald','Short','Medium','Long','Other'])))
    character.description['hair_thickness'] = str(random.choice(list(['Bald','Thin','Thick','Other'])))
    character.description['hair_part'] = str(random.choice(list(['None','Left','Right','Middle','Other'])))
    character.description['hair_bangs'] = str(random.choice(list(['None','Straight','Side Swept','Curly','Other'])))
    character.description['hair_style'] = str(random.choice(list(['Bald','Short','Medium','Long','Ponytail','Bun','Braid','Pigtails','Mohawk','Dreadlocks','Other'])))
    character.description['hair_scent'] = str(random.choice(list(['None','Scentless','Scented','Good Smell','Bad Oder','Other'])))

    character.description['facial_features'] = str(random.choice(list(['None','Scar','Tattoo','Piercing','Other'])))
    character.description['facial_hair'] = str(random.choice(list(['None','Beard','Mustache','Goatee','Chinstrap','Soul Patch','Scruff','Other'])))
    character.description['facial_hair_color'] = str(random.choice(list(['White','Black','Brown','Red','Yellow','Green','Blue','Purple','Orange','Pink','Gray','Other'])))

    character.description['body_type'] = str(random.choice(list(['Skinny','Slim','Average','Athletic','Muscular','Chubby','Fat','Other'])))
    character.description['body_color'] = str(random.choice(list(['White-ish','Black-ish','Brown-ish','Red-ish','Yellow-ish','Green-ish','Blue-ish','Purple-ish','Orange-ish','Pink-ish','Gray-ish','Other'])))
    character.description['body_shape'] = str(random.choice(list(['None','Thin','Average','Thick','Other'])))
    character.description['body_texture'] = str(random.choice(list(['None','Soft','Rough','Other'])))
    character.description['body_scent'] = str(random.choice(list(['None','Scentless','Scented','Other'])))
    character.description['body_features'] = str(random.choice(list(['None','Tattoo','Scar','Piercing','Missing Digit','Other'])))

    character.description['body_hair'] = str(random.choice(list(['None','Chest','Arms','Legs','Chest & Arms','Chest & Legs','Arms & Legs','All','Other'])))
    character.description['body_hair_color'] = str(random.choice(list(['White','Black','Brown','Red','Yellow','Green','Blue','Purple','Orange','Pink','Gray','Other'])))
    character.description['body_hair_length'] = str(random.choice(list(['None','Short','Medium','Long','Other'])))
    character.description['body_hair_style'] = str(random.choice(list(['None','Straight','Curly','Wavy', 'Shaved','Trimmed','Natural','Other'])))
    character.description['body_hair_density'] = str(random.choice(list(['None','Sparse','Normal','Dense','Other'])))
    character.description['body_hair_thickness'] = str(random.choice(list(['None','Thin','Thick','Other'])))
    character.description['body_hair_amount'] = str(random.choice(list(['None','Few','Some','Many','Other'])))
    character.description['body_hair_location'] = str(random.choice(list(['None','Chest','Arms','Legs','Chest & Arms','Chest & Legs','Arms & Legs','All','Other'])))
    character.description['body_hair_coverage'] = str(random.choice(list(['None','Partial','Full','Other'])))
    character.description['body_hair_texture'] = str(random.choice(list(['None','Soft','Coarse','Other'])))
    character.description['body_hair_sound'] = str(random.choice(list(['None','Silent','Noisy','Distracting','Other'])))

    character.description['tattoo_location'] = str(random.choice(list(['None','Left Arm','Right Arm','Both Arms','Left Leg', 'Right Leg', 'Both Legs','Chest','Back','Neck','Face','Full Body','Other'])))
    character.description['tattoo_pattern'] = str(random.choice(list(['None','Tribal','Mural','Faces','Words','Dates','Strip','Triangle','Square','Other'])))
    character.description['tattoo_amount'] = str(random.choice(list(['None','Few','Some','Many','Other'])))
    character.description['tattoo_density'] = str(random.choice(list(['None','Sparse','Normal','Dense','Other'])))
    character.description['tattoo_texture'] = str(random.choice(list(['None','Soft','Rough','Other'])))
    character.description['tattoo_coverage'] = str(random.choice(list(['None','Partial','Full','Other'])))
 
    character.description['clothing_style'] = str(random.choice(list(['None','Casual','Formal','Business','Athletic','Other'])))
    character.description['clothing_color'] = str(random.choice(list(['White','Black','Brown','Red','Yellow','Green','Blue','Purple','Orange','Pink','Gray','Other'])))
    character.description['clothing_pattern'] = str(random.choice(list(['None','Strip','Triangle','Square','Other'])))
    character.description['clothing_material'] = str(random.choice(list(['None','Cotton','Leather','Silk','Other'])))
    character.description['clothing_fit'] = str(random.choice(list(['None','Loose','Tight','Other'])))
    character.description['clothing_length'] = str(random.choice(list(['None','Short','Medium','Long','Other'])))
    character.description['clothing_coverage'] = str(random.choice(list(['None','Partial','Full','Other'])))
    
    character.description['accessories'] = str(random.choice(list(['None','Hat','Glasses','Earrings','Necklace','Bracelet','Ring','Watch','Other'])))
    character.description['head_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    character.description['neck_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    character.description['arm_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    character.description['hand_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    character.description['finger_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    character.description['leg_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    character.description['foot_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    character.description['body_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    character.description['back_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    character.description['waist_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    character.description['shoulder_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    
    character.description['voice'] = str(random.choice(list(['None','Deep','High','Smooth','Raspy','Other'])))
    character.description['mannerisms'] = str(random.choice(list(['None','Nervous','Confident','Calm','Other'])))
    character.description['personality'] = str(random.choice(list(['None','Introvert','Extrovert','Other'])))
   

    character.background = {}
    character.background['name'] = random.choice(list(dnd_backgrounds.keys()))
    character.background = dnd_backgrounds[character.background['name']]


    character.level_chart = dnd_classes[character_class]["Level Chart"]

    # probably not needed, it really just duplicates the info
    # character.profile['all_armor_proficiencies'] = []
    # character.profile['all_weapon_proficiencies'] = []
    # character.profile['all_tools_proficiencies'] = []
    # character.profile['all_languages'] = list(character.character_race['Proficiencies']['languages']) + list(character.character_class['Proficiencies']['Languages'])


    # # Adds spell slots by class
    # if character_class != 'Paladin' and character_class != 'Ranger' :
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['1st'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['2nd'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['3rd'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['4th'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['5th'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['6th'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['7th'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['8th'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['9th']
    # else:
    #     # character.character_class["Level Chart"][character.profile['level']] = dnd_classes[character_class]["Level Chart"][character.profile['level']]

    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['1st'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['2nd'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['3rd'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['4th'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['5th']


    def add_spell_levels(character_class,character):
        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = dnd_classes[character_class]['Spells']['Spells Known']
        if character_class in magic_classes:
            spell_levels = ['Cantrips','1st','2nd','3rd','4th','5th','6th','7th','8th','9th']
        elif character_class in half_magic_classes:
            spell_levels = ['1st','2nd','3rd','4th','5th']

        character.spells['Spells Known']["Slots"] = {}

        for spell_level in spell_levels:
            if spell_level == 'Cantrips':
                dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : f"Can cast {dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']} known Cantrips unlimiited times",
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)
                
            else:
                if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                    character.spells['Spells Known']["Slots"][spell_level] = {
                        "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                        "Known Spells" : {}
                    }
                    for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                        character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

            
    if character_class in magic_classes:
        character.spells['Cantrips Known'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']
        add_spell_levels(character_class,character)
    elif character_class in half_magic_classes:
        character.spells['Cantrips Known'] = "None"
        add_spell_levels(character_class,character)
    elif character_class in non_magic_classes:
        character.spells['Cantrips Known'] = "None"
        character.spells["Slots"] = "None"
        character.spells['Spells Known'] = "None"






    character.capabilities['attributes'] = {
        'strength' : {},
        'dexterity' : {},
        'constitution' : {},
        'intelligence' : {},
        'wisdom' : {},
        'charisma' : {}
    }

    new_roles = {
        'strength' : 0,
        'charisma' : 0,
        'constitution' : 0,
        'dexterity' : 0,
        'wisdom' : 0,
        'intelligence' : 0
    }

    generate_new_roles = generate_attribute_number()
    generate_new_roles = sorted(generate_new_roles, reverse=True)
    # Assigns role values in priority based on that listed in the dnd_classes
    for index, attribute in enumerate(dnd_classes[character_class]['Attribute Priority']):
        new_roles[attribute] = generate_new_roles[index]


    for attribute in character.capabilities['attributes']:
        character.capabilities['attributes'][attribute]['base'] = new_roles[attribute]
        
        try:
            character.capabilities['attributes'][attribute]['race_bonus'] = dnd_races[character_race]['Ability Score Increase'][attribute]
        except:
            character.capabilities['attributes'][attribute]['race_bonus'] = 0

        if attribute == str(dnd_classes[character_class]['Spells']["Spellcasting Modifier"]).lower():
            character.capabilities['attributes'][attribute]["Spellcasting Modifier"] = True
        else:
            character.capabilities['attributes'][attribute]["Spellcasting Modifier"] = False
        character.capabilities['attributes'][attribute]['total'] =  character.capabilities['attributes'][attribute]['base'] + character.capabilities['attributes'][attribute]['race_bonus']
        character.capabilities['attributes'][attribute]['modifier'] = (character.capabilities['attributes'][attribute]['total'] - 10) // 2
        for saving_throw in dnd_classes[character_class]["Proficiencies"]["Saving Throws"]:
            if attribute in str(saving_throw).lower():
                character.capabilities['attributes'][attribute]['saving_throw'] = character.capabilities['attributes'][attribute]['modifier'] + character.profile['proficiency bonus']


    character.capabilities['physical'] = {}
    character.capabilities['physical']['carry capacity'] = character.capabilities['attributes']['strength']['total'] * 15
    character.capabilities['physical']['push pull lift'] = character.capabilities['attributes']['strength']['total'] * 30
    character.capabilities['physical']['speed'] = dnd_races[character_race]['Traits']['Speed']['Ground']
    character.capabilities['physical']['vision'] = dnd_races[character_race]['Traits']['Vision']
    character.capabilities['physical']['dark vision'] = dnd_races[character_race]['Traits']['Vision']['Darkvision']["Possesses"]

    # Passive Perception is added after the skills section, as it's value depends on perception proficiency
    character.capabilities['physical']['passive perception'] = 0



    character.spells["Spellcasting"] = dnd_classes[character_class]['Spells']["Spellcasting"]
    character.spells["Preparation"] = dnd_classes[character_class]['Spells']["Preparation"]
    character.spells["Spellcasting Modifier"] = dnd_classes[character_class]['Spells']["Spellcasting Modifier"]

    if character_class not in non_magic_classes:
        # This needs to be beneath the spells and attributes section
        # Spell Attack Modifier = Your Spellcasting Ability Modifier + Your Proficiency Bonus
        character.spells["Attack Modifier"] = character.capabilities['attributes'][str(dnd_classes[character_class]['Spells']["Spellcasting Modifier"]).lower()]['modifier'] + character.profile['proficiency bonus']

        # Spell Save DC = 8 + Your Spellcasting Ability Modifier + Your Proficiency Bonus
        character.spells["Save DC"] = 8 + character.spells["Attack Modifier"]

    # character.spells['spellcasting focus'] = 'answer' #need to calculate, need to get stat attribtes first
    #!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!



    character.capabilities['Skills'] = dnd_skills

    
    randomly_chosen_skills = choose_random_proficiency_skill(dnd_classes,character_class)
    
    # Assigns proficiency to skills based on the randomly chosen skills list
    for skill in dnd_skills:
        if character.capabilities['Skills'][skill]['Related Attribute'] == 'strength':
            character.capabilities['Skills'][skill]['total'] = character.capabilities['attributes']['strength']['modifier']
        elif character.capabilities['Skills'][skill]['Related Attribute'] == 'dexterity':
            character.capabilities['Skills'][skill]['total'] = character.capabilities['attributes']['dexterity']['modifier']
        elif character.capabilities['Skills'][skill]['Related Attribute'] == 'constitution':
            character.capabilities['Skills'][skill]['total'] = character.capabilities['attributes']['constitution']['modifier']
        elif character.capabilities['Skills'][skill]['Related Attribute'] == 'intelligence':
            character.capabilities['Skills'][skill]['total'] = character.capabilities['attributes']['intelligence']['modifier']
        elif character.capabilities['Skills'][skill]['Related Attribute'] == 'wisdom':
            character.capabilities['Skills'][skill]['total'] = character.capabilities['attributes']['wisdom']['modifier']
        elif character.capabilities['Skills'][skill]['Related Attribute'] == 'charisma':
            character.capabilities['Skills'][skill]['total'] = character.capabilities['attributes']['charisma']['modifier']

        # Randomly adds proficiency to a skill if it is in the randomly chosen proficiency skills list
        for choose_skill in randomly_chosen_skills: 
            if skill == choose_skill:
                character.capabilities['Skills'][skill]['proficiency'] = True
                character.capabilities['Skills'][skill]['total'] += character.profile['proficiency bonus']

        # Calculates passive perception
        if skill == 'perception':
            if character.capabilities['Skills'][skill]['proficiency'] == True:
                character.capabilities['physical']['passive perception'] = 10 + character.capabilities['Skills']['perception']['total'] + character.profile['proficiency bonus']
            else:
                character.capabilities['physical']['passive perception'] = 10 + character.capabilities['Skills']['perception']['total']





    character.capabilities['combat'] = {}
    character.capabilities['combat']['initiative'] = {}
    character.capabilities['combat']['initiative']['normal'] = character.capabilities['attributes']['dexterity']['modifier']
    character.capabilities['combat']['initiative']['temporary'] = 0 #placeholder
    character.capabilities['combat']['initiative']['total'] = character.capabilities['combat']['initiative']['normal'] + character.capabilities['combat']['initiative']['temporary']
    character.capabilities['combat']['armor_class'] = 10 + character.capabilities['attributes']['dexterity']['modifier']
    character.capabilities['combat']['hit_points'] = {}
    character.capabilities['combat']['hit_points']['damage_resistence'] = 0
    character.capabilities['combat']['hit_points']['false_life'] = 0
    character.capabilities['combat']['hit_points']['temp_hit_points'] = 0


    character_hp_calc_total = 0
    # add full level 1 hit die hp
    character_hp_calc_total += int(character.character_class["Hit Die"].split('d')[1]) + int(character.capabilities['attributes']['constitution']['modifier'])
    for level in range(2,int(character.profile['level'] + 1)): # starts at level 2, because level 1 is added in full up above
        val = random.randint(1, int(character.character_class["Hit Die"].split('d')[1])) + int(character.capabilities['attributes']['constitution']['modifier'])
        character_hp_calc_total += val
    character.capabilities['combat']['hit_points']['total'] = character_hp_calc_total
    character.capabilities['combat']['hit_points']['current'] = character.capabilities['combat']['hit_points']['total']

# 'combat' : {
#     'initiative' : {
#         'modifier' : 0,
#         'total' : 0
#     },
#     'armor_class' : {
#         'temporary' : 0,
#         'total' : 0
#     },
#     'hit_points' : {
#         'damage_resistance' : 0,
#         'false_life' : 0,
#         'temp_hit_points' : 0,
#         'total' : 0
#     },
# }



    for i in range(1, random.randint(1,6)):
        character.items.append(generate_random_item(item_list))

    for i in range(1, random.randint(1,4)):
        ##### old way, when i just used a weapons_list
        # generated_weapon = generate_random_weapon(weapon_list)
        # character.weapons[generated_weapon['name']] = {}
        # character.weapons[generated_weapon['name']]['description'] = generated_weapon['description']
        # character.weapons[generated_weapon['name']]['damage_amount'] = generated_weapon['damage_amount']
        # character.weapons[generated_weapon['name']]['weapon_type'] = generated_weapon['damage_type']
        # character.weapons[generated_weapon['name']]['attack_type'] = generated_weapon['attack_type']
        # character.weapons[generated_weapon['name']]['attack_bonus'] = generated_weapon['attack_bonus']
        # character.weapons[generated_weapon['name']]['is_ranged'] = generated_weapon['is_ranged']
        # character.weapons[generated_weapon['name']]['range_low'] = generated_weapon['range_low']
        # character.weapons[generated_weapon['name']]['range_high'] = generated_weapon['range_high']
        # character.weapons[generated_weapon['name']]['amount'] = generated_weapon['amount']
        # character.weapons[generated_weapon['name']]['rarity'] = generated_weapon['rarity']
        # character.weapons[generated_weapon['name']]['material_components'] = generated_weapon['material_components']
        # character.weapons[generated_weapon['name']]['cost'] = generated_weapon['cost']
        # character.weapons[generated_weapon['name']]['weight'] = generated_weapon['weight']
        # character.weapons[generated_weapon['name']]['mundane_properties'] = generated_weapon['mundane_properties']
        # character.weapons[generated_weapon['name']]['is_magical'] = generated_weapon['is_magical']
        # character.weapons[generated_weapon['name']]['magical_type'] = generated_weapon['magical_type']

        #### new way, basing it off actual dnd_weapons list
        generated_weapon = random.choice(list(dnd_weapons.keys()))
        character.weapons[generated_weapon] = dnd_weapons.get(generated_weapon)



    return character



def display_character(characters):
    # Print Character to screen
    for index, character in enumerate(characters):
        print(f"==================================================")
        print(f"Character #{index + 1}")
        print(f"==================================================")

        print(f"Profile :")
        print_character(character.profile)

        print(f"Race :")
        print_character(character.character_race)

        print(f"Class :")
        print_character(character.character_class)

        print(f"Level Chart :")
        print_character(character.level_chart)

        print(f"Description :")
        print_character(character.description)

        print(f"Background :")
        print_character(character.background)

        print(f"Attributes :")
        print_character(character.attributes)

        print(f"Capabilties :")
        print_character(character.capabilities)

        print(f"Skills :")
        print_character(character.skills)

        print(f"Features :")
        print_character(character.features)

        print(f"Money :")
        print_character(character.items)

        print(f"Items :")
        print_inventory(character.items, 'Items')

        print(f"Armor :")
        print_inventory(character.armor, 'Armor')

        print(f"Weapons :")
        print_character(character.weapons)

        print(f"Combat :")
        print_character(character.combat)

        print(f"Spells :")
        print_character(character.spells)

