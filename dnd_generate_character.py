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
from dnd_character_print import *


# Clear the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


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
        self.weapons = []
        self.combat = {}
        self.spells = {
            "spellcasting" : "",
            "preparation" : "",
            "spellcasting modifier" : "",
            "attack modifier" : 0,
            "save dc" : 0,
            'slots' : {}
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
    character.character_class["Current Level Chart"] = {}
    character.character_class["Current Level Chart"][character.profile['level']] = dnd_classes[character_class]["Level Chart"][character.profile['level']]
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
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['1st Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['2nd Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['3rd Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['4th Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['5th Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['6th Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['7th Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['8th Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['9th Level Spell Slots']
    # else:
    #     # character.character_class["Level Chart"][character.profile['level']] = dnd_classes[character_class]["Level Chart"][character.profile['level']]

    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['1st Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['2nd Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['3rd Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['4th Level Spell Slots'],
    #     dnd_classes[character_class]['Level Chart'][character.profile['level']]['5th Level Spell Slots']

    character.spells['slots'] = {}
    
    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['1st Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['1st Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']["All Class Spells"]['1st Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['1st Level Spell Slots']
            }
    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['2nd Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['2nd Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']["All Class Spells"]['2nd Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['2nd Level Spell Slots']
            }
    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['3rd Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['3rd Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']["All Class Spells"]['3rd Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['3rd Level Spell Slots']
            }

    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['4th Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['4th Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']["All Class Spells"]['4th Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['4th Level Spell Slots']
            }

    if dnd_classes[character_class]['Level Chart'][character.profile['level']]['5th Level Spell Slots'] != '-':
        if character_class == 'Paladin':
            character.spells['slots']['5th Level'] = {
                'known spells' : dnd_classes[character_class]['Spells']["All Class Spells"]['5th Level'],
                'number able to cast' : dnd_classes[character_class]['Level Chart'][character.profile['level']]['5th Level Spell Slots']
            }

    if character_class != 'Paladin' and character_class != 'Ranger' :
        if dnd_classes[character_class]['Level Chart'][character.profile['level']]['6th Level Spell Slots'] != '-':
            character.spells['slots']['6th Level'] = dnd_classes[character_class]['Spells']["All Class Spells"]['6th Level']

        if dnd_classes[character_class]['Level Chart'][character.profile['level']]['7th Level Spell Slots'] != '-':
            character.spells['slots']['7th Level'] = dnd_classes[character_class]['Spells']["All Class Spells"]['7th Level']

        if dnd_classes[character_class]['Level Chart'][character.profile['level']]['8th Level Spell Slots'] != '-':
            character.spells['slots']['8th Level'] = dnd_classes[character_class]['Spells']["All Class Spells"]['8th Level']

        if dnd_classes[character_class]['Level Chart'][character.profile['level']]['9th Level Spell Slots'] != '-':
            character.spells['slots']['9th Level'] = dnd_classes[character_class]['Spells']["All Class Spells"]['9th Level']




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
            character.capabilities['attributes'][attribute]['spellcasting modifier'] = True
        else:
            character.capabilities['attributes'][attribute]['spellcasting modifier'] = False
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



    character.spells['spellcasting'] = dnd_classes[character_class]['Spells']["Spellcasting"]
    character.spells['preparation'] = dnd_classes[character_class]['Spells']["Preparation"]
    character.spells['spellcasting modifier'] = dnd_classes[character_class]['Spells']["Spellcasting Modifier"]

    # This needs to be beneath the spells and attributes section
    # Spell Attack Modifier = Your Spellcasting Ability Modifier + Your Proficiency Bonus
    character.spells['attack modifier'] = character.capabilities['attributes'][str(dnd_classes[character_class]['Spells']["Spellcasting Modifier"]).lower()]['modifier'] + character.profile['proficiency bonus']

    # Spell Save DC = 8 + Your Spellcasting Ability Modifier + Your Proficiency Bonus
    character.spells['save dc'] = 8 + character.spells['attack modifier']

    # character.spells['spellcasting focus'] = 'answer' #need to calculate, need to get stat attribtes first
    #!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!



    character.capabilities['skills'] = dnd_skills

    
    randomly_chosen_skills = choose_random_proficiency_skill(dnd_classes,character_class)
    
    # Assigns proficiency to skills based on the randomly chosen skills list
    for skill in dnd_skills:
        if character.capabilities['skills'][skill]['related attribute'] == 'strength':
            character.capabilities['skills'][skill]['total'] = character.capabilities['attributes']['strength']['modifier']
        elif character.capabilities['skills'][skill]['related attribute'] == 'dexterity':
            character.capabilities['skills'][skill]['total'] = character.capabilities['attributes']['dexterity']['modifier']
        elif character.capabilities['skills'][skill]['related attribute'] == 'constitution':
            character.capabilities['skills'][skill]['total'] = character.capabilities['attributes']['constitution']['modifier']
        elif character.capabilities['skills'][skill]['related attribute'] == 'intelligence':
            character.capabilities['skills'][skill]['total'] = character.capabilities['attributes']['intelligence']['modifier']
        elif character.capabilities['skills'][skill]['related attribute'] == 'wisdom':
            character.capabilities['skills'][skill]['total'] = character.capabilities['attributes']['wisdom']['modifier']
        elif character.capabilities['skills'][skill]['related attribute'] == 'charisma':
            character.capabilities['skills'][skill]['total'] = character.capabilities['attributes']['charisma']['modifier']

        # Randomly adds proficiency to a skill if it is in the randomly chosen proficiency skills list
        for choose_skill in randomly_chosen_skills: 
            if skill == choose_skill:
                character.capabilities['skills'][skill]['proficiency'] = True
                character.capabilities['skills'][skill]['total'] += character.profile['proficiency bonus']

        # Calculates passive perception
        if skill == 'perception':
            if character.capabilities['skills'][skill]['proficiency'] == True:
                character.capabilities['physical']['passive perception'] = 10 + character.capabilities['skills']['perception']['total'] + character.profile['proficiency bonus']
            else:
                character.capabilities['physical']['passive perception'] = 10 + character.capabilities['skills']['perception']['total']





    character.capabilities['combat'] = {}
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
        character.weapons.append(generate_random_weapon(weapon_list))

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
        print_inventory(character.weapons, 'Weapons')

        print(f"Combat :")
        print_character(character.combat)

        print(f"Spells :")
        print_character(character.spells)

