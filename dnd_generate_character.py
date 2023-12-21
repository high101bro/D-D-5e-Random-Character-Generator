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
from dnd_helper import *
from dnd_spells import *
from chatgpt_dall_e import *

item_list = [generate_item_list() for _ in range(10)]
weapon_list = [generate_weapon_list() for _ in range(10)]


class Character():
    def __init__(self):
        self.profile = {}
        self.memory = {}
        self.character_race = {}
        self.character_class = {}
        self.description = {}
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
        self.attributes = {
            'strength' : {},
            'dexterity' : {},
            'constitution' : {},
            'intelligence' : {},
            'wisdom' : {},
            'charisma' : {}
        }
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
            "Spells Known" : {
                "Slots" : {},
            },
            "Selected Spells" : []
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
def generate_characters(character, character_number, character_level=1, character_race='Human', character_class='Fighter', method='Automated'):

    character.profile['character number'] = character_number
    character.profile['created'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%S"))
    character.profile['name'] = {}
    character.profile['name']['first'] = random.choice(first_names)
    character.profile['name']['last'] = random.choice(last_names)
    character.profile['name']['full'] = f"{character.profile['name']['first']} {character.profile['name']['last']}"
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

    character.description = {}

    character.description['race'] = str(character_race)

    character.description['class'] = str(character_class)
    

    # Age
    character_age_ranges = {
        'Elf': (18, 701),
        'Dwarf': (18, 401),
        'Dragonborn': (18, 81),
        'Gnome': (18, 351),
        'Half-Elf': (18, 181),
        'Half-Orc': (18, 71),
        'Halfling': (18, 151),
        'Human': (18, 81),
        'Tiefling': (18, 81),
    }
    if method == 'Automated' or method == 'Guided':
        character.description['age'] = random.randint(character_age_ranges[character_race][0], character_age_ranges[character_race][1])
    elif method == 'Manual':
        character.description['age'] = terminalmenu_quick_select([str(num) for num in range(character_age_ranges[character_race][0], character_age_ranges[character_race][1])], f'[{character_race}] Select an age:')


    # Gender
    if method == 'Automated' or method == 'Guided':
        character.description['gender'] = str(random.choice(list(['Male','Female','Unknown'])))
    elif method == 'Manual':
        character.description['gender'] = terminalmenu_quick_select(['Male', 'Female', 'Hermaphrodite', 'Non-Binary', 'Transgender', 'Unknown', 'Other', 'None'], f'[{character_race}] Select a gender:')


    # Height
    character_height_ranges = {
        'Elf': (60, 73),
        'Dwarf': (48, 59),
        'Dragonborn': (66, 79),
        'Gnome': (35, 43),
        'Half-Elf': (62, 75),
        'Half-Orc': (58, 73),
        'Halfling': (18, 151),
        'Human': (56, 79),
        'Tiefling': (57, 74),
    }
    if method == 'Automated' or method == 'Guided':
        character.description['height'] = random.randint(character_height_ranges[character_race][0], character_height_ranges[character_race][1])
    elif method == 'Manual':
        character.description['height'] = terminalmenu_quick_select([str(num) for num in range(character_height_ranges[character_race][0], character_height_ranges[character_race][1])], f'[{character_race}] Select a height in inches:')


    # Weight
    character_weight_ranges = {
        'Elf': (100, 146),
        'Dwarf': (130, 181),
        'Dragonborn': (220, 321),
        'Gnome': (35, 43),
        'Half-Elf': (110, 161),
        'Half-Orc': (140, 251),
        'Halfling': (35, 46),
        'Human': (155, 241),
        'Tiefling': (110, 191),
    }
    if method == 'Automated' or method == 'Guided':
        character.description['weight'] = random.randint(character_weight_ranges[character_race][0], character_weight_ranges[character_race][1])
    elif method == 'Manual':
        character.description['weight'] = terminalmenu_quick_select([str(num) for num in range(character_weight_ranges[character_race][0],character_weight_ranges[character_race][1])], f'[{character_race}] Select a weight in pounds:')


    # Skin variations
    character_skin_type_variations = {
       'Dwarf': [
            "Rough and weathered with prominent scars - Dwarves often bear rough and weathered skin marked by prominent scars from their underground conflicts.",
            "Leathery with a rugged texture - The skin of many dwarves is leathery and rugged in texture, a testament to their resilient nature.",
            "Lightly freckled and adorned with age spots - Some dwarves have skin lightly freckled and adorned with age spots, reflecting their wisdom and experience.",
            "Olive-toned with a natural resilience - Dwarves often have olive-toned skin, which showcases their natural resilience and hardiness.",
            "Tanned and hardened from labor - Dwarves who engage in laborious work often have tanned and hardened skin, embodying their industrious spirit.",
            "Mottled with birthmarks and character - Mottled skin with birthmarks adds character to some dwarves, enhancing their unique appearance.",
            "Rugged with a hint of earthiness - The skin of certain dwarves is rugged with a hint of earthiness, reflecting their deep connection to the earth.",
            "Smooth yet marked by years of toil - Some dwarves possess smooth skin marked by years of toil, embodying their dedication to craftsmanship."
        ],
        'Elf': [
            "Ethereal with a subtle glow - Elves often have ethereal skin with a subtle glow, reminiscent of their connection to the mystical world.",
            "Radiant and sun-kissed - Elves who spend time in the sun may have radiant and sun-kissed skin, reflecting their love for the outdoors.",
            "Ebony with an alluring mystique - A rare few elves boast ebony skin with an alluring mystique, adding to their enigmatic charm.",
            "Translucent with delicate veins showing - Some elves have translucent skin with delicate veins showing, hinting at their otherworldly nature.",
            "Silver sheen that shimmers under moonlight - The skin of certain elves has a silver sheen that shimmers under moonlight, enhancing their enchanting beauty.",
            "Dappled like moonlight through leaves - Dappled skin patterns resembling moonlight filtering through leaves are characteristic of some elves.",
            "Lavender-hued with a touch of magic - Lavender-hued skin with a touch of magic is common among elves, symbolizing their mystical heritage.",
            "Exquisite and otherworldly - The skin of elves is often described as exquisite and otherworldly, captivating those who behold it."
        ],
        'Halfling': [
            "Light and youthful with a touch of innocence - Halflings often have light and youthful skin with a touch of innocence, embodying their cheerful nature.",
            "Peachy complexion that's inviting - A peachy complexion is common among halflings, adding to their inviting and friendly demeanor.",
            "Rosy cheeks that add charm - Many halflings have rosy cheeks that add charm and warmth to their appearance.",
            "Light freckles across the nose like constellations - Light freckles across the nose of some halflings resemble constellations, enhancing their endearing charm.",
            "Sunkissed and always ready for the beach - Halflings who enjoy beach life often have sunkissed skin, reflecting their love for the coastal lifestyle.",
            "Smooth and flawless, a canvas of beauty - The skin of some halflings is smooth and flawless, serving as a canvas of natural beauty.",
            "Warm and inviting with a touch of character - Warm and inviting skin with a touch of character is characteristic of halflings, making them approachable.",
            "Bronzed with the allure of outdoor adventures - Halflings who embark on outdoor adventures often have bronzed skin, emphasizing their adventurous spirit."
        ],
        'Human': [
            "Versatile and ever-changing in tones - Human skin exhibits a wide range of tones, making them versatile and adaptable in appearance.",
            "Olive complexion that adapts to surroundings - Some humans have an olive complexion that adapts to their surroundings, reflecting their versatility.",
            "Freckled or blemished with a story to tell - Freckles or blemishes on human skin often tell stories of their life experiences and adventures.",
            "Dusky and kissed by the sun - A dusky complexion kissed by the sun is common among humans who spend time outdoors, reflecting their active lifestyles.",
            "Golden tan from tropical origins - Humans from tropical regions often have a golden tan, symbolizing their origins in exotic locales.",
            "Rich brown adorned with cultural symbols - Rich brown skin adorned with cultural symbols is characteristic of many humans, reflecting their heritage.",
            "Smooth and even-toned with personality - The skin of some humans is smooth and even-toned, carrying the marks of their unique personality.",
            "Almond-toned with a healthy and radiant glow - Almond-toned skin with a healthy and radiant glow is a striking trait of certain humans."
        ],
        'Dragonborn': [
            "Scales with intricate engravings - Dragonborn often bear scales with intricate engravings that tell stories of their lineage and heritage.",
            "Vibrant scales that mesmerize - Vibrant and eye-catching scales are common among dragonborn, mesmerizing those who behold them.",
            "Iridescent scales that shimmer with magic - Some dragonborn have iridescent scales that shimmer with a touch of magic, reflecting their mystical nature.",
            "Metallic with ornate patterns and designs - Metallic scales with ornate patterns and designs are characteristic of many dragonborn, showcasing their elegance.",
            "Prismatic scales that change colors in the light - Dragonborn with prismatic scales can change colors in the light, creating a captivating spectacle.",
            "Dark scales with a molten sheen like lava - Dark scales with a molten sheen resembling lava are a unique trait of certain dragonborn.",
            "Gem-like scales that shine brilliantly - Gem-like scales that shine brilliantly under the light are a striking feature of some dragonborn.",
            "Crystalline scales with a translucent, ethereal quality - Crystalline scales with a translucent, ethereal quality add an otherworldly dimension to certain dragonborn."
        ],
        'Gnome': [
            "Fair with rosy cheeks and a mischievous twinkle - Gnomes often have fair skin with rosy cheeks and a mischievous twinkle in their eyes, reflecting their playful nature.",
            "Light green with an earthy and whimsical charm - Light green skin with an earthy and whimsical charm is characteristic of many gnomes, emphasizing their connection to nature.",
            "Freckled or spotted like the night sky - Freckled or spotted skin resembling the night sky is a unique trait of some gnomes, adding to their distinctive appearance.",
            "Porcelain with a hint of greenish tint - Porcelain skin with a hint of greenish tint is common among gnomes, symbolizing their affinity for the natural world.",
            "Sparkling skin with tiny, reflective particles like stars - Gnomes often have skin that sparkles with tiny, reflective particles, akin to stars in the night sky.",
            "Tanned and speckled from gardening and exploration - Gnomes who enjoy gardening and exploration often have tanned skin speckled with adventure.",
            "Terracotta-toned from living in clay-based homes - Terracotta-toned skin resulting from living in clay-based homes is characteristic of certain gnomes, reflecting their craftsmanship.",
            "Pale lavender with an otherworldly sheen - Pale lavender skin with an otherworldly sheen is a unique feature of some gnomes, hinting at their magical inclinations."
        ],
        'Half-Elf': [
            "Human-like skin tones with a touch of elven grace - Half-elves often have skin tones resembling humans but with a touch of elven grace and allure.",
            "Elven-like fair or dusky complexion that enchants - Half-elves may possess elven-like fair or dusky complexions that enchant those who meet them.",
            "Translucent with faintly visible veins, hinting at magic - Some half-elves have translucent skin with faintly visible veins, hinting at their magical heritage.",
            "Muted and ethereal with a delicate, otherworldly glow - Muted and ethereal skin tones with a delicate glow are characteristic of some half-elves.",
            "Bronzed and vibrant from a diverse heritage - Half-elves with diverse heritages often have bronzed and vibrant skin, reflecting their multicultural backgrounds.",
            "Olive-toned with a touch of elven grace and allure - Half-elves may have olive-toned skin with a touch of elven grace and allure, captivating those they meet.",
            "Honeyed complexion with a timeless and captivating appeal - A honeyed complexion with a timeless and captivating appeal is a striking trait of certain half-elves.",
            "Elven-like fair with a celestial radiance that mesmerizes - Half-elves with elven-like fair skin often radiate a celestial and mesmerizing aura."
        ],
        'Half-Orc': [
            "Tanned and weathered from life's challenges - Half-orcs often have tanned and weathered skin, reflecting the challenges they've faced in life.",
            "Greenish-gray with prominent orcish features - Skin that is greenish-gray with prominent orcish features is characteristic of many half-orcs, showcasing their heritage.",
            "Ashen with scars from countless battles - Ashen skin with scars from countless battles highlights the fierce and battle-hardened nature of some half-orcs.",
            "Dark and rugged from a nomadic and adventurous lifestyle - A dark and rugged complexion from a nomadic and adventurous lifestyle is characteristic of some half-orcs, reflecting their resourcefulness.",
            "Grayish-blue with a mysterious and intriguing aura - Some half-orcs possess a grayish-blue complexion with a mysterious aura, adding to their enigmatic presence.",
            "Olive-toned with prominent tusks that tell stories - Olive-toned skin with prominent tusks that tell stories of their heritage is a distinctive feature of certain half-orcs.",
            "Earthy brown with orcish tattoos that symbolize their past - Earthy brown skin adorned with orcish tattoos that symbolize their past and experiences.",
            "Mottled green and gray with tribal markings of honor and identity - Mottled green and gray skin with tribal markings that represent honor and identity among their people.",
        ],
        'Tiefling': [
            "Skin that hints at their infernal heritage - Their skin bears subtle signs of their infernal heritage, with a hint of otherworldly texture.",
            "Marks and patterns that evoke their fiendish nature - Intricate marks and patterns on their skin evoke their fiendish nature, each telling a story of their lineage.",
            "Infernal symbols and designs etched into their flesh - Etched into their flesh are infernal symbols and designs, showcasing their connection to the planes of darkness.",
            "Charred and smoky, an embodiment of an eerie presence - Their skin appears charred and smoky, giving them an eerie and unsettling presence.",
            "Subtle glowing runes and fiery veins beneath the skin - Subtle glowing runes and fiery veins run beneath their skin, creating an otherworldly aura.",
            "Crimson with smoldering patches that command attention - Their skin is crimson with smoldering patches that command attention wherever they go.",
            "Amethyst-toned with obsidian accents that exude elegance - Their amethyst-toned skin is adorned with obsidian accents, exuding an air of dark elegance.",
            "Fiery red or dark maroon with an infernal allure - Their skin is fiery red or dark maroon, exuding an infernal allure that draws both fascination and fear.",
        ],    
    }
    if method == 'Automated' or method == 'Guided':
        character.description['skin_type'] = random.choice(character_skin_type_variations[character_race])
    elif method == 'Manual':
        character.description['skin_type'] = terminalmenu_quick_select(character_skin_type_variations[character_race], f'[{character_race}] Select a skin type variation:')

    character_skin_color_variations = {
        'Dwarf': [
            'Fair with a ruddy complexion - Dwarves often have fair skin with a healthy, rosy complexion, which can be attributed to their hardy lifestyle.',
            'Tanned from working outdoors - Dwarves who work outdoors often develop a tan from exposure to the elements, showcasing their ruggedness.',
            'Weathered and leathery - The skin of some dwarves becomes weathered and leathery due to their underground life and enduring harsh conditions.',
            'Lightly freckled with a healthy glow - Light freckles can adorn the skin of certain dwarves, giving them a youthful and healthy appearance.',
            'Porcelain with a touch of rosy hue - Some dwarves possess porcelain-like skin with a subtle rosy hue, adding to their distinctive charm.'
        ],
        'Elf': [
            'Pale with a slight bluish tint - Elves often have pale skin with a delicate bluish tint, reminiscent of moonlight and their connection to the night sky.',
            'Sun-kissed bronze - Elves who spend time in the sun may acquire a sun-kissed bronze complexion, reflecting their active outdoor lifestyle.',
            'Deep ebony, almost black - A rare few elves boast deep ebony skin, almost black in color, which enhances their mystique and allure.',
            'Alabaster with an ethereal glow - Some elves possess alabaster skin with an ethereal, radiant glow, emphasizing their otherworldly beauty.',
            'Translucent with visible veins - Certain elves have translucent skin with visible veins, hinting at their ethereal and mystical nature.'
        ],
        'Halfling': [
            'Light tan - Halflings often have a light tan complexion, which adds to their friendly and approachable appearance.',
            'Peachy complexion - A peachy complexion is common among halflings, contributing to their warm and inviting demeanor.',
            'Rosy cheeks - Many halflings have rosy cheeks, giving them a perpetually cheerful and youthful look.',
            'Light freckles across the nose - Light freckles may adorn the noses of some halflings, enhancing their endearing charm.',
            'Sunkissed and beach-ready - Halflings who frequent beaches may acquire a sunkissed complexion, reflecting their love for coastal living.'
        ],
        'Human': [
            'Varied tones from pale to dark - Humans exhibit a wide range of skin tones, varying from pale to dark, showcasing their diversity.',
            'Olive complexion - Some humans have an olive complexion, often associated with regions with abundant sunlight and warm climates.',
            'Freckled or blemished - Freckles or blemishes can be present on the skin of certain humans, highlighting their unique features.',
            'Dusky and sun-kissed - A dusky and sun-kissed complexion is common among humans who spend time outdoors, reflecting their adventurous spirit.',
            'Golden tan from tropical origins - Humans from tropical regions may have a golden tan, symbolizing their connection to exotic locales.'
        ],
        'Dragonborn': [
            'Metallic scales in various colors - Dragonborn often bear metallic scales in a range of colors, reflecting their draconic heritage and individuality.',
            'Vibrant chromatic scales - Some dragonborn boast vibrant chromatic scales, radiating the power of their dragon ancestry.',
            'Iridescent or pearlescent scales - Iridescent or pearlescent scales adorn the skin of certain dragonborn, creating a captivating and ever-changing appearance.',
            'Metallic with intricate patterns - Dragonborn may have metallic scales with intricate patterns, emphasizing their regal and ornate nature.',
            'Prismatic scales that change color - Rare dragonborn possess prismatic scales that change color, adding to their enigmatic allure.'
        ],
        'Gnome': [
            'Fair with rosy cheeks - Gnomes often have fair skin with rosy cheeks, lending them a perpetually cheerful and youthful appearance.',
            'Light green or earthy tones - Skin with light green or earthy tones is characteristic of gnomes, reflecting their affinity for nature.',
            'Freckled or spotted - Freckles or spots may adorn the skin of some gnomes, adding to their whimsical charm.',
            'Porcelain with a greenish tint - Porcelain-like skin with a subtle greenish tint is common among gnomes, enhancing their unique beauty.',
            'Sparkling skin with tiny reflective particles - The skin of certain gnomes sparkles with tiny reflective particles, giving them a magical and enchanting aura.'
        ],
        'Half-Elf': [
            'Human-like skin tones - Half-elves often have skin tones resembling those of humans, showcasing their mixed heritage.',
            'Elven-like fair or dusky complexion - Half-elves can possess fair or dusky complexions reminiscent of their elven ancestry.',
            'Translucent with faintly visible veins - Some half-elves have translucent skin with faintly visible veins, highlighting their unique blend of human and elven traits.',
            'Muted and ethereal with a faint glow - A muted and ethereal complexion with a faint glow is characteristic of certain half-elves, emphasizing their enchanting beauty.',
            'Bronzed and vibrant from diverse heritage - Half-elves may have a bronzed and vibrant complexion, reflecting their diverse cultural heritage.'
        ],
        'Half-Orc': [
            'Tanned or weathered - Half-orcs often have tanned or weathered skin, showcasing their resilience and endurance in harsh environments.',
            'Greenish-gray with orcish features - Skin with a greenish-gray hue and orcish features is common among half-orcs, emphasizing their orc ancestry.',
            'Ashen with scars from battles - Ashen skin with scars from battles highlights the fierce and battle-hardened nature of some half-orcs.',
            'Dark and rugged from a nomadic lifestyle - A dark and rugged complexion from a nomadic lifestyle is characteristic of certain half-orcs, reflecting their resourcefulness.',
            'Grayish-blue with a mysterious aura - Some half-orcs possess a grayish-blue complexion with a mysterious aura, adding to their enigmatic presence.'
        ],
        'Tiefling': [
            'Fiery red or dark maroon - Tieflings often have fiery red or dark maroon skin, emphasizing their infernal lineage and striking appearance.',
            'Deep blue or purple - Skin in deep blue or purple hues is characteristic of some tieflings, adding to their mystique.',
            'Ashen gray with infernal markings - Ashen gray skin adorned with infernal markings is a distinctive feature of certain tieflings, hinting at their dark and enigmatic nature.',
            'Charcoal black with subtle glowing runes - Charcoal black skin with subtle glowing runes is common among tieflings, enhancing their mystical and sinister aura.',
            'Ebony with fiery veins beneath the skin - Ebony skin with fiery veins beneath the surface is a striking trait of some tieflings, highlighting their connection to the infernal realm.'
        ]
    }
    if method == 'Automated' or method == 'Guided':
        character.description['skin_color'] = random.choice(character_skin_color_variations[character_race])
    elif method == 'Manual':
        character.description['skin_color'] = terminalmenu_quick_select(character_skin_color_variations[character_race], f'[{character_race}] Select a skin color variation:')


    # Race-specific skin scents
    character_skin_scent_variations = {
        "Dwarf": [
            "Earthy and mineral-like - Dwarves often carry a faint aroma reminiscent of the earth and minerals from their underground dwellings.",
            "Hints of stone and metal - A subtle scent of stone and metal clings to dwarves, reflecting their affinity for crafting and mining.",
            "Faint aroma of ale and herbs - Some dwarves exude a faint fragrance of ale and herbs, a testament to their love for hearty brews and herbal remedies.",
            "Subtle scent of underground caverns - Dwarves may have a subtle aroma that evokes the essence of the underground caverns they call home."
        ],
        "Elf": [
            "A delicate hint of flowers and forest - Elves carry a delicate scent that captures the essence of flowers and the forest, a testament to their deep connection to nature.",
            "Earthy and woody with a touch of moss - Some elves exude an earthy and woody fragrance, often accompanied by a touch of moss, reflecting their affinity for the woods.",
            "Subtle fragrance of elven magic - A faint fragrance of elven magic surrounds some elves, hinting at their mystical abilities and ancient knowledge.",
            "Whiff of ancient forests and starlight - Elves may carry a captivating scent reminiscent of ancient forests and the soft glow of starlight."
        ],
        "Halfling": [
            "Warm and comforting like a bakery - Halflings often carry a warm and comforting scent, reminiscent of a bakery filled with freshly baked bread and pastries.",
            "Hint of freshly baked bread and pastries - Some halflings exude the delightful fragrance of freshly baked bread and pastries, making them even more endearing.",
            "Aromatic blend of spices and herbs - Aromatic spices and herbs contribute to the pleasant scent of halflings, reflecting their culinary expertise.",
            "Subtle scent of home-cooked meals - The subtle aroma of home-cooked meals surrounds some halflings, evoking a sense of warmth and hospitality."
        ],
        "Human": [
            "Varied scents depending on region - Humans carry scents that vary depending on their region of origin, reflecting the diverse environments they inhabit.",
            "Hint of salt and sea breeze (coastal) - Coastal humans may carry a hint of salt and the invigorating aroma of sea breeze.",
            "Earthy aroma of farmlands (rural) - Humans from rural areas often exude an earthy fragrance reminiscent of fertile farmlands.",
            "Mixture of spices and street food (urban) - Urban humans may carry a complex scent composed of various spices and the enticing aroma of street food."
        ],
        "Dragonborn": [
            "Metallic and faintly smoky - Dragonborn often carry a metallic scent with a faint smoky undertone, hinting at their draconic heritage.",
            "Subtle hint of dragon's breath - Some dragonborn exude a subtle scent reminiscent of dragon's breath, adding to their mystique.",
            "Faint odor of scales and heat - A faint aroma of scales and heat surrounds dragonborn, reflecting their innate connection to dragons.",
            "Mysterious scent of draconic ancestry - Dragonborn may carry a mysterious scent that hints at their ancient draconic ancestry and power."
        ],
        "Gnome": [
            "Fresh and earthy like a garden - Gnomes often carry a fresh and earthy scent akin to a flourishing garden, reflecting their love for nature.",
            "Aromatic blend of flowers and herbs - An aromatic blend of flowers and herbs contributes to the delightful scent of gnomes, showcasing their affinity for botany.",
            "Hint of tinkering and mechanical oils - Some gnomes exude a subtle scent of tinkering and mechanical oils, a testament to their inventive nature.",
            "Subtle scent of magical experiments - The subtle aroma of magical experiments surrounds some gnomes, emphasizing their curiosity and magical prowess."
        ],
        "Half-Elf": [
            "A mixture of human and elven scents - Half-elves carry a blend of scents, combining the earthy with a faint hint of magic, reflecting their dual heritage.",
            "Earthy with a faint hint of magic - Some half-elves exude an earthy scent with a subtle undertone of magic, showcasing their connection to both worlds.",
            "Subtle fragrance of diverse heritage - A subtle fragrance surrounds some half-elves, reflecting their diverse heritage and rich cultural background.",
            "Aroma of nature and diplomacy - Half-elves may carry an aroma that evokes nature and diplomacy, capturing their appreciation for the natural world and diplomatic pursuits."
        ],
        "Half-Orc": [
            "Musky and primal - Half-orcs often carry a musky and primal scent, reflecting their rugged and warrior-like nature.",
            "Hints of sweat and ruggedness - Some half-orcs exude scents reminiscent of sweat and ruggedness, reflecting their physical prowess and determination.",
            "Faint scent of warrior's resolve - A faint scent of warrior's resolve surrounds some half-orcs, emphasizing their indomitable spirit in the face of challenges.",
            "Earthy with a touch of orcish strength - Half-orcs may carry an earthy scent with a touch of orcish strength, highlighting their tenacity and heritage."
        ],
        "Tiefling": [
            "Fiery and slightly smoky - Tieflings often carry a fiery and slightly smoky scent, reflecting their infernal lineage and enigmatic presence.",
            "Hint of infernal brimstone - Some tieflings exude a hint of infernal brimstone, adding to their mysterious and otherworldly aura.",
            "Faint scent of otherworldly origins - A faint scent of otherworldly origins surrounds tieflings, hinting at their connection to realms beyond the mortal plane.",
            "Sulfuric aroma with an edge of darkness - Tieflings may carry a sulfuric aroma with an edge of darkness, emphasizing their unique and captivating nature."
        ]
    }

    # Assign a race-specific skin scent
    if method == "Automated" or method == "Guided":
        character.description["skin_scent"] = random.choice(character_skin_scent_variations[character_race])
    elif method == "Manual":
        character.description["skin_scent"] = terminalmenu_quick_select(character_skin_scent_variations[character_race], f"[{character_race}] Select a skin scent:")

    # Race-specific skin defects
    character_skin_defect_variations = {
        "Dwarf": [
            "None - Dwarves typically have resilient and unblemished skin.",
            "Battle scars from underground conflicts - Some dwarves bear battle scars that tell tales of their bravery in subterranean battles.",
            "Burn marks from working with hot metals - Dwarves may have burn marks from their skilled craftsmanship with hot metals.",
            "Piercings adorned with gemstones - Some dwarves sport piercings adorned with precious gemstones, adding a touch of elegance to their appearance."
        ],
        "Elf": [
            "None - Elves often possess flawless and ethereal skin.",
            "Subtle scars from elven battles - A few elves bear subtle scars as reminders of their ancient battles fought in defense of their realms.",
            "Faint burns from magical mishaps - Some elves have faint burns resulting from their delicate work with powerful magics.",
            "Elegant ear and facial piercings - Elves may choose to wear elegant ear and facial piercings that enhance their already graceful features."
        ],
        "Halfling": [
            "None - Halflings typically have charming and blemish-free skin.",
            "Playful scars from adventurous endeavors - Some halflings sport playful scars acquired during their adventurous and lighthearted pursuits.",
            "Slight burns from culinary mishaps - A few halflings bear slight burns from their culinary experiments and love for cooking.",
            "Delicate and charming piercings - Halflings may wear delicate and charming piercings that match their affable and cheerful nature."
        ],
        "Human": [
            "None - Humans have a diverse range of skin appearances, often free from significant defects.",
            "Scars from various life experiences - Some humans carry scars that tell stories of their diverse life experiences and adventures.",
            "Burn marks from everyday accidents - A few humans may have burn marks from everyday accidents and mishaps.",
            "Trendy and fashionable piercings - Humans may opt for trendy and fashionable piercings that suit their ever-evolving style and trends."
        ],
        "Dragonborn": [
            "None - Dragonborn often have resilient scales that protect their skin.",
            "Battle scars that highlight their strength - Some dragonborn bear battle scars that serve as badges of honor, highlighting their formidable strength.",
            "Heat-resistant scales prevent burns - Dragonborn's heat-resistant scales protect them from burns, even in extreme environments.",
            "Unique and symbolic piercings - A few dragonborn choose unique and symbolic piercings that reflect their draconic heritage and individuality."
        ],
        "Gnome": [
            "None - Gnomes typically have skin free from defects.",
            "Intriguing scars from mechanical experiments - Some gnomes sport intriguing scars acquired during their mechanical experiments and inventions.",
            "Occasional burns from tinkering with gadgets - A few gnomes have occasional burns from their tinkering and experimentation with gadgets.",
            "Mechanical-themed piercings - Gnomes may wear piercings with mechanical-themed designs that reflect their love for invention and technology."
        ],
        "Half-Elf": [
            "None - Half-elves often have a blend of human and elven features, resulting in harmonious and unblemished skin.",
            "Subtle scars from diplomatic negotiations - A few half-elves bear subtle scars as reminders of their diplomatic endeavors and negotiations.",
            "Faint burns from magical training - Some half-elves have faint burns resulting from their training in both human and elven magic.",
            "Piercings that reflect their heritage - Half-elves may choose piercings that reflect their mixed heritage, blending elements of both human and elven cultures."
        ],
        "Half-Orc": [
            "None - Half-orcs typically have rugged and battle-hardened skin, free from significant defects.",
            "Battle scars that showcase their prowess - Some half-orcs bear battle scars that serve as badges of honor, showcasing their martial prowess.",
            "Scars from enduring harsh environments - A few half-orcs have scars acquired while enduring the challenges of harsh environments.",
            "Rugged and fierce piercings - Half-orcs may wear piercings that complement their rugged and fierce appearance, reflecting their indomitable spirit."
        ],
        "Tiefling": [
            "None - Tieflings often have unique infernal features that are not considered defects.",
            "Infernal markings that are not defects - Some tieflings bear infernal markings that are considered unique and integral to their infernal heritage.",
            "Burns with a mystical and sinister aura - A few tieflings may have burns that exude a mystical and sinister aura, enhancing their enigmatic presence.",
            "Dark and alluring piercings - Tieflings may opt for dark and alluring piercings that accentuate their mysterious and captivating nature."
        ],
    }

    # Assign a race-specific skin defect
    if method == "Automated" or method == "Guided":
        character.description["skin_defect"] = random.choice(character_skin_defect_variations[character_race])
    elif method == "Manual":
        character.description["skin_defect"] = terminalmenu_quick_select(character_skin_defect_variations[character_race], f"[{character_race}] Select a skin defect:")

    # Race-specific eye shapes
    character_eye_shape_variations = {
        "Dwarf": [
            "None - Dwarves often have distinctive angular eyes that emphasize their craftsmanship and precision.",
            "Almond-shaped - Some dwarves possess almond-shaped eyes, hinting at their keen observation skills.",
            "Round - Round eyes that exude warmth and approachability, often seen in friendly dwarves.",
            "Oval - Oval-shaped eyes that convey a sense of practicality and adaptability.",
            "Distinctly angular - Rarely, a dwarf may have eyes that are distinctly angular, symbolizing their unique character."
        ],
        "Elf": [
            "None - Elves often have gracefully elongated eyes that enhance their ethereal beauty.",
            "Almond-shaped - Some elves possess almond-shaped eyes that emphasize their graceful features.",
            "Round - Round eyes that exude an air of innocence and wonder, often seen in youthful elves.",
            "Oval - Oval-shaped eyes that convey a sense of serenity and tranquility.",
            "Gracefully elongated - Rarely, an elf may have eyes that are elegantly tapered, marking them as exceptional."
        ],
        "Halfling": [
            "None - Halflings typically have bright and twinkling eyes that reflect their joyful nature.",
            "Almond-shaped - Some halflings possess almond-shaped eyes that accentuate their mischievous charm.",
            "Round - Round eyes that exude warmth and friendliness, often seen in amicable halflings.",
            "Oval - Oval-shaped eyes that convey a sense of curiosity and open-mindedness.",
            "Bright and twinkling - Rarely, a halfling's eyes may literally twinkle with merriment, a sign of their joyful spirit."
        ],
        "Human": [
            "None - Humans have a wide range of eye shapes, but many have expressive and varied eyes that reflect their diverse nature.",
            "Almond-shaped - Some humans possess almond-shaped eyes that convey a sense of focus and determination.",
            "Round - Round eyes that express a wide range of emotions and are known for their versatility.",
            "Oval - Oval-shaped eyes that reflect adaptability and an open-hearted nature.",
            "Expressive and varied - Rarely, a human's eyes may be exceptionally expressive and varied, showcasing their rich inner world."
        ],
        "Dragonborn": [
            "None - Dragonborn often have serpentine and fierce eyes that emphasize their draconic heritage.",
            "Almond-shaped - Some dragonborn possess almond-shaped eyes that evoke the look of ancient dragons.",
            "Round - Round eyes that exude an air of strength and command, often seen in dragonborn leaders.",
            "Oval - Oval-shaped eyes that convey a sense of mystique and enigma.",
            "Serpentine and fierce - Rarely, a dragonborn may have eyes that are distinctly serpentine, signifying their extraordinary lineage."
        ],
        "Gnome": [
            "None - Gnomes often have playful and curious eyes that reflect their inquisitive nature.",
            "Almond-shaped - Some gnomes possess almond-shaped eyes that hint at their keen intellect.",
            "Round - Round eyes that express a sense of wonder and excitement, often seen in imaginative gnomes.",
            "Oval - Oval-shaped eyes that convey a sense of fascination and innovation.",
            "Playful and curious - Rarely, a gnome's eyes may radiate an aura of boundless playfulness and curiosity, marking them as particularly inventive."
        ],
        "Half-Elf": [
            "None - Half-elves possess a mix of human and elven features, often resulting in elegantly tapered eyes.",
            "Almond-shaped - Some half-elves possess almond-shaped eyes that emphasize their charismatic presence.",
            "Round - Round eyes that captivate with their warmth and charm, often seen in sociable half-elves.",
            "Oval - Oval-shaped eyes that convey a sense of adaptability and grace.",
            "Elegantly tapered - Rarely, a half-elf's eyes may be elegantly tapered, showcasing their unique blend of human and elven qualities."
        ],
        "Half-Orc": [
            "None - Half-orcs typically have intensely focused eyes that reveal their strength and determination.",
            "Almond-shaped - Some half-orcs possess almond-shaped eyes that emphasize their fierce and unyielding spirit.",
            "Round - Round eyes that express a sense of resilience and unwavering resolve, often seen in determined half-orcs.",
            "Oval - Oval-shaped eyes that convey a sense of adaptability and versatility.",
            "Intensely focused - Rarely, a half-orc's eyes may be exceptionally focused, signifying their indomitable will."
        ],
        "Tiefling": [
            "None - Tieflings often have mysteriously alluring eyes that hint at their infernal heritage.",
            "Almond-shaped - Some tieflings possess almond-shaped eyes that convey a sense of allure and beguilement.",
            "Round - Round eyes that captivate with their hypnotic charm, often seen in beguiling tieflings.",
            "Oval - Oval-shaped eyes that convey a sense of mystery and enchantment.",
            "Mysteriously alluring - Rarely, a tiefling's eyes may exude an irresistibly mysterious and alluring aura, marking them as truly extraordinary."
        ]
    }

    # Assign a race-specific eye shape
    if method == "Automated" or method == "Guided":
        character.description["eye_shape"] = random.choice(character_eye_shape_variations[character_race])
    elif method == "Manual":
        character.description["eye_shape"] = terminalmenu_quick_select(character_eye_shape_variations[character_race], f"[{character_race}] Select an eye shape:")

    # Race-specific eye sizes
    character_eye_size_variations = {
        "Dwarf": [
            "None - Dwarves often have smaller, intense eyes that focus on craftsmanship and detail.",
            "Small and intense - Their small eyes are keen and intense, often scrutinizing their surroundings.",
            "Medium and steady - Medium-sized eyes that exude a sense of reliability and determination.",
            "Large and observant - Some dwarves possess large, observant eyes, allowing them to notice every detail.",
            "Otherworldly proportions - Rarely, a dwarf may have eyes of unusual size, hinting at an exceptional heritage."
        ],
        "Elf": [
            "None - Elves often have smaller, graceful eyes that express their ethereal beauty.",
            "Small and graceful - Small eyes with an elegant and graceful appearance, reflecting their elven nature.",
            "Medium and expressive - Medium-sized eyes that are highly expressive and captivating.",
            "Large and enchanting - Some elves possess large, enchanting eyes that draw others in with their charm.",
            "Eyes like ancient stars - Rarely, an elf may have eyes that resemble ancient stars, marking them as extraordinary."
        ],
        "Halfling": [
            "None - Halflings typically have small, mischievous eyes that sparkle with laughter.",
            "Small and mischievous - Small eyes that convey a mischievous spirit, often accompanied by a knowing glint.",
            "Medium and welcoming - Medium-sized eyes that are warm and welcoming, making others feel at ease.",
            "Large and inviting - Some halflings have large, inviting eyes that radiate friendliness and goodwill.",
            "Eyes that sparkle with laughter - Rarely, a halfling's eyes may literally sparkle with laughter, a sign of their joyful nature."
        ],
        "Human": [
            "None - Humans have a wide range of eye sizes, but many have medium-sized eyes that adapt to various situations.",
            "Small and versatile - Small eyes that adapt easily to different circumstances and convey versatility.",
            "Medium and adaptable - Medium-sized eyes that reflect an ability to adapt and connect with others.",
            "Large and soulful - Some humans possess large, soulful eyes that express deep emotions and empathy.",
            "Eyes that reflect a world of emotions - Rarely, a human's eyes may seem to reflect the entire spectrum of human emotions."
        ],
        "Dragonborn": [
            "None - Dragonborn often have medium-sized eyes that reflect their fierce and commanding nature.",
            "Small and fierce - Small eyes that exude fierceness and intensity, often seen in dragonborn warriors.",
            "Medium and commanding - Medium-sized eyes that command attention and respect.",
            "Large and intimidating - Some dragonborn have large, intimidating eyes that strike fear into their foes.",
            "Eyes that radiate draconic power - Rarely, a dragonborn may possess eyes that seem to radiate the power of their dragon ancestry."
        ],
        "Gnome": [
            "None - Gnomes often have small, inquisitive eyes that hint at their curiosity and inventiveness.",
            "Small and inquisitive - Small eyes that reflect an insatiable curiosity, always seeking to explore and discover.",
            "Medium and curious - Medium-sized eyes that are naturally curious and eager to learn new things.",
            "Large and wonder-filled - Some gnomes have large, wonder-filled eyes that are filled with amazement and awe.",
            "Eyes that hold the secrets of invention - Rarely, a gnome's eyes may seem to hold the secrets of their ingenious inventions."
        ],
        "Half-Elf": [
            "None - Half-elves possess a mix of human and elven features, often resulting in medium-sized, captivating eyes.",
            "Small and alluring - Small eyes with an alluring quality, drawing others in with their charm.",
            "Medium and captivating - Medium-sized eyes that captivate those who gaze into them, reflecting charisma.",
            "Large and charismatic - Some half-elves have large, charismatic eyes that convey a magnetic presence.",
            "Eyes that bridge two worlds - Rarely, a half-elf's eyes may seem to bridge the gap between human and elven worlds, signifying their unique heritage."
        ],
        "Half-Orc": [
            "None - Half-orcs typically have medium-sized, determined eyes that reveal their strength and resilience.",
            "Small and focused - Small eyes that focus intensely on their goals, often seen in determined half-orcs.",
            "Medium and determined - Medium-sized eyes that convey unwavering determination and resolve.",
            "Large and unyielding - Some half-orcs possess large, unyielding eyes that intimidate their adversaries.",
            "Eyes that reveal strength and resilience - Rarely, a half-orc's eyes may seem to reveal the very essence of their strength and resilience."
        ],
        "Tiefling": [
            "None - Tieflings often have medium-sized, enigmatic eyes that hint at their infernal heritage.",
            "Small and enigmatic - Small eyes that carry an air of mystery, often seen in beguiling tieflings.",
            "Medium and beguiling - Medium-sized eyes that beguile and captivate with their charm.",
            "Large and hypnotic - Some tieflings have large, hypnotic eyes that enchant those who meet their gaze.",
            "Eyes that hint at infernal power - Rarely, a tiefling's eyes may seem to crackle with the power of their infernal ancestry."
        ]
    }

    # Assign a race-specific eye size
    if method == "Automated" or method == "Guided":
        character.description["eye_size"] = random.choice(character_eye_size_variations[character_race])
    elif method == "Manual":
        character.description["eye_size"] = terminalmenu_quick_select(character_eye_size_variations[character_race], f"[{character_race}] Select an eye size:")

    # Race-specific eye colors
    character_eye_color_variations = {
        "Dwarf": [
            "Brown - Deep, earthy brown eyes common among dwarves, reflecting their connection to the underground world.",
            "Gray - Gray eyes with a steely and determined gaze, often seen in seasoned dwarven warriors.",
            "Blue - Bright blue eyes that sparkle like precious gemstones, a sign of dwarven craftsmanship.",
            "Green - Green eyes with a hint of forest magic, indicating a connection to the natural world.",
            "Hazel - Hazel eyes that change color in different lighting, mirroring the adaptable nature of dwarves.",
            "Amber - Amber-colored eyes with a warm, inviting glow, symbolizing dwarven hospitality."
        ],
        "Elf": [
            "Blue - Azure blue eyes that reflect the serene skies of elven homelands, denoting a deep connection to nature.",
            "Green - Emerald green eyes, vibrant and full of life, representing an affinity for the elven forests.",
            "Gray - Silver-gray eyes, reminiscent of moonlight, signifying an elf's mystical heritage.",
            "Hazel - Hazel eyes that shift like the changing seasons, reflecting the timeless nature of elves.",
            "Amber - Amber eyes with a gentle radiance, symbolizing the wisdom and agelessness of elves.",
            "Violet - Rare violet eyes, a mark of elven nobility and a connection to ancient elven bloodlines."
        ],
        "Halfling": [
            "Brown - Warm brown eyes, welcoming and friendly, commonly found in halflings who value community.",
            "Gray - Gray eyes with a mischievous glint, hinting at a halfling's love for adventure and humor.",
            "Green - Green eyes that reflect the agricultural lifestyle of halflings, tied to their love of food and nature.",
            "Blue - Blue eyes with a twinkle of curiosity, representing a halfling's inquisitive nature.",
            "Hazel - Hazel eyes that mirror the warmth of a hobbit's home and hearth, symbolizing comfort.",
            "Amber - Amber eyes with a cheerful glow, signifying a halfling's love for simple pleasures and celebrations."
        ],
        "Human": [
            "Brown - Common brown eyes, reflecting the diversity of human appearances and earthy connections.",
            "Blue - Bright blue eyes, symbolizing the limitless potential and boundless dreams of humanity.",
            "Green - Green eyes that mirror a human's adaptability and connection to the natural world.",
            "Gray - Gray eyes that speak of human wisdom and experience, often seen in elders.",
            "Hazel - Hazel eyes that capture the multifaceted nature of humanity, showcasing versatility."
        ],
        "Dragonborn": [
            "Red - Fiery red eyes, representing the inner strength and determination of dragonborn warriors.",
            "Gold - Shimmering gold eyes that reflect a noble and honorable nature, common among gold dragonborn.",
            "Silver - Silver eyes with an air of wisdom, signifying the ancient knowledge held by silver dragonborn.",
            "Blue - Deep blue eyes like sapphires, denoting a dragonborn's connection to water and the sea.",
            "Green - Green eyes that embody the vitality and rejuvenation of nature, often seen in green dragonborn.",
            "Bronze - Bronze eyes with a regal bearing, symbolizing the leadership of bronze dragonborn."
        ],
        "Gnome": [
            "Brown - Warm brown eyes that reflect a gnome's love for the earth and nature's bounty.",
            "Blue - Bright blue eyes that shimmer like a clear sky, symbolizing a gnome's boundless curiosity.",
            "Green - Green eyes with a hint of mischief, mirroring a gnome's playful and imaginative spirit.",
            "Gray - Silver-gray eyes with an otherworldly glint, indicating a gnome's connection to the Feywild.",
            "Hazel - Hazel eyes that change with a gnome's emotions, showcasing their vibrant personalities.",
            "Amber - Amber eyes that exude warmth and charm, symbolizing a gnome's love for laughter and joy."
        ],
        "Half-Elf": [
            "Brown - Brown eyes that blend human and elven traits, representing the duality of half-elves.",
            "Blue - Bright blue eyes that reflect a half-elf's longing for adventure and discovery.",
            "Green - Green eyes with a touch of elven grace, signifying their affinity for the natural world.",
            "Gray - Silver-gray eyes that hint at a half-elf's elven lineage and inherent mystique.",
            "Hazel - Hazel eyes that capture the versatility and adaptability of half-elves."
        ],
        "Half-Orc": [
            "Brown - Brown eyes with a determined gaze, symbolizing the resilience and strength of half-orcs.",
            "Blue - Bright blue eyes that mirror a half-orc's capacity for loyalty and camaraderie.",
            "Green - Green eyes that reflect a half-orc's connection to nature and primal instincts.",
            "Gray - Silver-gray eyes with an air of mystery, hinting at a half-orc's untamed nature.",
            "Hazel - Hazel eyes that capture the multifaceted personalities of half-orcs."
        ],
        "Tiefling": [
            "Red - Fiery red eyes that evoke the infernal heritage and inner passion of tieflings.",
            "Black - Deep black eyes that exude an enigmatic aura, symbolizing a tiefling's inner darkness.",
            "Purple - Royal purple eyes with an otherworldly beauty, often seen in tieflings of noble lineage.",
            "Blue - Sapphire blue eyes that reflect a tiefling's mystical potential and affinity for magic.",
            "Green - Green eyes with a touch of the otherworldly, denoting a tiefling's connection to the planes."
        ]
    }

    # Assign a race-specific eye color
    if method == "Automated" or method == "Guided":
        character.description["eye_color"] = random.choice(character_eye_color_variations[character_race])
    elif method == "Manual":
        character.description["eye_color"] = terminalmenu_quick_select(character_eye_color_variations[character_race], f"[{character_race}] Select an eye color:")


    if method == "Automated" or method == "Guided":
        character.description["eye_brows"] = random.choice(['None','Short','Medium','Long', 'Thin', 'Bushy', 'Other'])
    elif method == "Manual":
        character.description["eye_brows"] = terminalmenu_quick_select(['Short','Medium','Long', 'Thin', 'Bushy', 'Other'], f"[{character_race}] Select an eye brows:")



    # Combine race-common eye features and eye sight conditions
    character_eye_features_variations = [
        "Small Scar - A minor scar near the eye",
        "Medium Scar - A noticeable scar near the eye",
        "Large Scar - A prominent scar near the eye",
        "Single Piercing - A single piercing near the eye",
        "Multiple Piercings - Multiple piercings near the eye",
        "Normal - Typical eye appearance with no distinctive features",
        "Slightly smaller than normal - The eye appears slightly smaller than average",
        "Slightly larger than normal - The eye appears slightly larger than average",
        "Going Blind - Vision impairment or deterioration",
        "Cataracts - Clouding of the eye's natural lens",
        "Eye Patch - Wearing an eye patch to cover or protect the eye",
        "Cock-eyed - Cross-eyed or misaligned eyes",
        "Lazy Eye - A condition where one eye is weaker or misaligned",
        "Missing an Eye - One eye is entirely absent",
        "Scarred - Eyes have visible scars",
        "Pierced - Eyes have piercings",
        "Wrinkled - The skin around the eyes is wrinkled",
        "Bloodshot - Redness in the whites of the eyes",
        "Freckled - Eyes have freckles or spots",
        "Worn - The eyes appear tired or aged",
        "Bright - Eyes are unusually bright and expressive",
        "Dull - Eyes lack luster and seem uninterested",
        "Wide-set - Eyes are spaced further apart than usual",
        "Close-set - Eyes are positioned closer together than usual",
        "Almond-shaped - Eyes have an elongated, almond-like shape",
        "Round - Eyes are perfectly round in shape",
        "Slanted - Eyes have a slanted or tilted appearance",
        "Hooded - The upper eyelids droop over the eyes",
        "Deep-set - Eyes are deeply recessed in the eye sockets",
        "Other - Unusual or unique eye features not listed"
    ]

    # Assign a combined race-common eye feature and eye sight condition
    if method == "Automated" or method == "Guided":
        character.description["eye_feature"] = random.choice(character_eye_features_variations)
    elif method == "Manual":
        selected_feature = terminalmenu_quick_select(character_eye_features_variations, f"[{character_race}] Select an eye feature or sight condition:")
        character.description["eye_feature"] = selected_feature
    
    
    character_race_nose_variations = {
        'Dwarf': [
            'A sturdy, broad nose that matches their robust stature',
            'A slightly upturned nose with a hint of mischief',
            'A snub nose that reflects their practical nature',
            'A prominent and well-defined nose with character',
            'A nose that has seen its fair share of battles'
        ],
        'Elf': [
            'A gracefully pointed nose that adds to their ethereal beauty',
            'A delicate nose with a refined, aristocratic appearance',
            'A nose that complements their elven grace and elegance',
            'A slender and aquiline nose that hints at their elven heritage',
            'A nose with a slight upturn, giving them an air of mystique'
        ],
        'Halfling': [
            'A cute button nose that enhances their charm',
            'A small, slightly upturned nose that exudes playfulness',
            'A perky and friendly nose that matches their warm personality',
            'A nose that reflects their love for food and laughter',
            'A nose with just the right amount of mischievousness'
        ],
        'Human': [
            'A versatile nose with a shape that varies from individual to individual',
            'A nose that reflects their diverse human heritage',
            'A nose that tells a unique story of their life experiences',
            'A nose that adapts to the environment and culture they belong to',
            'A nose that reflects the richness of human diversity'
        ],
        'Dragonborn': [
            'A dragon-like snout that showcases their draconic ancestry',
            'A nose with a slight ridge, reminiscent of dragon scales',
            'A nose with a faintly reptilian appearance, hinting at their lineage',
            'A nose with a fierce and commanding presence, like a dragon',
            'A nose that bears the marks of their dragonblood lineage'
        ],
        'Gnome': [
            'A cute and slightly upturned nose that adds to their whimsy',
            'A nose that reflects their curiosity and inquisitive nature',
            'A nose that tells stories of their tinkering and inventiveness',
            'A nose with a playful and mischievous charm',
            'A nose that matches their love for all things imaginative'
        ],
        'Half-Elf': [
            'A balanced nose that combines human and elven features harmoniously',
            'A nose with a subtle elven point, reflecting their dual heritage',
            'A nose that hints at their diplomatic and versatile nature',
            'A nose that bridges the gap between two worlds, both human and elven',
            'A nose that showcases their unique blend of characteristics'
        ],
        'Half-Orc': [
            'A strong and rugged nose that reveals their orcish strength',
            'A nose with prominent features, reflecting their resilience',
            'A nose that bears the marks of their harsh and adventurous lifestyle',
            'A nose that reflects their orcish determination and endurance',
            'A nose that reveals their strength and unyielding spirit'
        ],
        'Tiefling': [
            'A nose with subtle, infernal features that hint at their fiendish heritage',
            'A nose with intriguing marks and patterns that reflect their lineage',
            'A nose with infernal symbols etched into their flesh, showcasing their connection to darkness',
            'A nose with an eerie presence, charred and smoky in appearance',
            'A nose that commands attention, with smoldering patches and an infernal allure'
        ]
    }
    if method == "Automated" or method == "Guided":
        character.description["nose_shape"] = random.choice(character_race_nose_variations[character_race])
    elif method == "Manual":
        character.description["nose_shape"] = terminalmenu_quick_select(character_race_nose_variations[character_race], f"[{character_race}] Select a nose shape:")


    character_race_chin_variations = {
        "Dwarf": [
            "A sturdy and square jawline that matches their robust build",
            "A slightly upturned chin with a hint of determination",
            "A broad and well-defined chin that reflects their practical nature",
            "A prominent and square chin with character",
            "A chin that has seen its fair share of battles",
            "A rugged chin adorned with intricate dwarven runes"
        ],
        "Elf": [
            "A gracefully pointed chin that adds to their ethereal beauty",
            "A delicate chin with a refined, aristocratic appearance",
            "A chin that complements their elven grace and elegance",
            "A slender and tapered chin that hints at their elven heritage",
            "A chin with a slight upward curve, giving them an air of mystique",
            "An elven chin marked by delicate tattoos that tell their story"
        ],
        "Halfling": [
            "A cute and dimpled chin that enhances their charm",
            "A small and rounded chin that exudes playfulness",
            "A perky and friendly chin that matches their warm personality",
            "A chin that reflects their love for food and laughter",
            "A chin with just the right amount of mischievousness",
            "A halfling chin adorned with tiny, handcrafted trinkets"
        ],
        "Human": [
            "A versatile chin with a shape that varies from individual to individual",
            "A chin that reflects their diverse human heritage",
            "A chin that tells a unique story of their life experiences",
            "A chin that adapts to the environment and culture they belong to",
            "A chin that reflects the richness of human diversity",
            "A human chin with scars and markings from their adventures"
        ],
        "Dragonborn": [
            "A dragon-like jawline that showcases their draconic ancestry",
            "A chin with a slight ridge, reminiscent of dragon scales",
            "A chin with a faintly reptilian appearance, hinting at their lineage",
            "A chin with a fierce and commanding presence, like a dragon",
            "A chin that bears the marks of their dragonblood lineage",
            "A dragonborn chin with iridescent scales that shimmer in the light"
        ],
        "Gnome": [
            "A cute and slightly upturned chin that adds to their whimsy",
            "A chin that reflects their curiosity and inquisitive nature",
            "A chin that tells stories of their tinkering and inventiveness",
            "A chin with a playful and mischievous charm",
            "A chin that matches their love for all things imaginative",
            "A gnome's chin adorned with tiny, tinkling bells"
        ],
        "Half-Elf": [
            "A balanced chin that combines human and elven features harmoniously",
            "A chin with a subtle elven point, reflecting their dual heritage",
            "A chin that hints at their diplomatic and versatile nature",
            "A chin that bridges the gap between two worlds, both human and elven",
            "A chin that showcases their unique blend of characteristics",
            "A half-elf chin marked with delicate elven patterns"
        ],
        "Half-Orc": [
            "A strong and rugged chin that reveals their orcish strength",
            "A chin with prominent features, reflecting their resilience",
            "A chin that bears the marks of their harsh and adventurous lifestyle",
            "A chin that reflects their orcish determination and endurance",
            "A chin that reveals their strength and unyielding spirit",
            "A half-orc chin adorned with tribal tattoos that symbolize honor and courage"
        ],
        "Tiefling": [
            "A chin with subtle, infernal features that hint at their fiendish heritage",
            "A chin with intriguing marks and patterns that reflect their lineage",
            "A chin with infernal symbols etched into their flesh, showcasing their connection to darkness",
            "A chin with an eerie presence, charred and smoky in appearance",
            "A chin that commands attention, with smoldering patches and an infernal allure",
            "A tiefling chin adorned with intricate infernal engravings"
        ]
    }

    if method == "Automated" or method == "Guided":
        character.description["chin_shape"] = random.choice(character_race_chin_variations[character_race])
    elif method == "Manual":
        character.description["chin_shape"] = terminalmenu_quick_select(character_race_chin_variations[character_race], f"[{character_race}] Select a chin shape:")


    character_race_chin_features_variations = {
        "Dwarf": [
            "A rugged chin with battle scars from underground conflicts",
            "A leathery chin with burn marks from working with hot metals",
            "A chin adorned with piercings adorned with gemstones",
            "A chin with unique features that showcase their dwarven heritage",
            "A dwarf's chin marked with ancient runes of protection"
        ],
        "Elf": [
            "A chin with subtle scars from elven battles",
            "A chin with faint burns from magical mishaps",
            "A chin with elegant ear and facial piercings",
            "A chin with unique features that reflect their elven grace",
            "An elf's chin adorned with delicate silver filigree"
        ],
        "Halfling": [
            "A playful chin with scars from adventurous endeavors",
            "A chin with slight burns from culinary mishaps",
            "A chin adorned with delicate and charming piercings",
            "A chin with unique features that match their warm personality",
            "A halfling's chin marked with lucky charms and symbols"
        ],
        "Human": [
            "A chin with scars from various life experiences",
            "A chin with burn marks from everyday accidents",
            "A chin adorned with trendy and fashionable piercings",
            "A chin with unique features that reflect their diverse human background",
            "A human's chin with tribal markings of their heritage"
        ],
        "Dragonborn": [
            "A chin with battle scars that highlight their strength",
            "A chin with heat-resistant scales that prevent burns",
            "A chin adorned with unique and symbolic piercings",
            "A chin with features that showcase their draconic power",
            "A dragonborn's chin marked with the emblem of their clan"
        ],
        "Gnome": [
            "A chin with intriguing scars from mechanical experiments",
            "A chin with occasional burns from tinkering with gadgets",
            "A chin adorned with mechanical-themed piercings",
            "A chin with unique features that reflect their inventive spirit",
            "A gnome's chin decorated with tiny, functional gears"
        ],
        "Half-Elf": [
            "A chin with subtle scars from diplomatic negotiations",
            "A chin with faint burns from magical training",
            "A chin adorned with piercings that reflect their heritage",
            "A chin with unique features that bridge their human and elven lineage",
            "A half-elf's chin etched with symbols of harmony"
        ],
        "Half-Orc": [
            "A chin with battle scars that showcase their prowess",
            "A chin with scars from enduring harsh environments",
            "A chin adorned with rugged and fierce piercings",
            "A chin with unique features that reveal their strength and resilience",
            "A half-orc's chin marked with tribal tattoos of honor"
        ],
        "Tiefling": [
            "A chin with infernal markings that are not defects",
            "A chin with burns with a mystical and sinister aura",
            "A chin adorned with dark and alluring piercings",
            "A chin with unique features that hint at their infernal power",
            "A tiefling's chin engraved with infernal sigils"
        ]
    }

    if method == "Automated" or method == "Guided":
        character.description["chin_features"] = random.choice(character_race_chin_features_variations[character_race])
    elif method == "Manual":
        character.description["chin_features"] = terminalmenu_quick_select(character_race_chin_features_variations[character_race], f"[{character_race}] Select chin features:")


    character_race_ear_shape_variations = {
        'Dwarf': [
            'Sturdy, round ears that match their robust stature',
            'Slightly pointed ears with a hint of mischief',
            'Small, flat ears that reflect their practical nature',
            'Prominent and well-defined ears with character',
            'Ears that have seen their fair share of battles'
        ],
        'Elf': [
            'Gracefully pointed ears that add to their ethereal beauty',
            'Delicate ears with a refined, aristocratic appearance',
            'Ears that complement their elven grace and elegance',
            'Slender and elongated ears that hint at their elven heritage',
            'Ears with a slight point, giving them an air of mystique'
        ],
        'Halfling': [
            'Cute, round ears that enhance their charm',
            'Small, slightly pointed ears that exude playfulness',
            'Perky and friendly ears that match their warm personality',
            'Ears that reflect their love for food and laughter',
            'Ears with just the right amount of mischievousness'
        ],
        'Human': [
            'Versatile ears with a shape that varies from individual to individual',
            'Ears that reflect their diverse human heritage',
            'Ears that tell a unique story of their life experiences',
            'Ears that adapt to the environment and culture they belong to',
            'Ears that reflect the richness of human diversity'
        ],
        'Dragonborn': [
            'Dragon-like ears that showcase their draconic ancestry',
            'Ears with a slight ridge, reminiscent of dragon scales',
            'Ears with a faintly reptilian appearance, hinting at their lineage',
            'Ears with a fierce and commanding presence, like a dragon',
            'Ears that bear the marks of their dragonblood lineage'
        ],
        'Gnome': [
            'Cute and slightly pointed ears that add to their whimsy',
            'Ears that reflect their curiosity and inquisitive nature',
            'Ears that tell stories of their tinkering and inventiveness',
            'Ears with a playful and mischievous charm',
            'Ears that match their love for all things imaginative'
        ],
        'Half-Elf': [
            'Balanced ears that combine human and elven features harmoniously',
            'Ears with a subtle elven point, reflecting their dual heritage',
            'Ears that hint at their diplomatic and versatile nature',
            'Ears that bridge the gap between two worlds, both human and elven',
            'Ears that showcase their unique blend of characteristics'
        ],
        'Half-Orc': [
            'Strong and rugged ears that reveal their orcish strength',
            'Ears with prominent features, reflecting their resilience',
            'Ears that bear the marks of their harsh and adventurous lifestyle',
            'Ears that reflect their orcish determination and endurance',
            'Ears that reveal their strength and unyielding spirit'
        ],
        'Tiefling': [
            'Ears with subtle, infernal features that hint at their fiendish heritage',
            'Ears with intriguing marks and patterns that reflect their lineage',
            'Ears with infernal symbols etched into their flesh, showcasing their connection to darkness',
            'Ears with an eerie presence, charred and smoky in appearance',
            'Ears that command attention, with smoldering patches and an infernal allure'
        ]
    }

    if method == "Automated" or method == "Guided":
        character.description["ear_shape"] = random.choice(character_race_ear_shape_variations[character_race])
    elif method == "Manual":
        character.description["ear_shape"] = terminalmenu_quick_select(character_race_ear_shape_variations[character_race], f"[{character_race}] Select ear shape:")


    character_race_ear_size_variations = {
        'Dwarf': [
            'Small, compact ears that match their sturdy build',
            'Moderate-sized ears with a practical and functional appearance',
            'Slightly larger ears that add character to their face',
            'Ears with a rugged and weathered appearance',
            'Ears that are proportionate to their robust stature'
        ],
        'Elf': [
            'Elongated and elegant ears that enhance their ethereal beauty',
            'Moderate-sized ears with a refined and graceful appearance',
            'Ears that are in perfect harmony with their elven features',
            'Slender and pointed ears that hint at their elven heritage',
            'Graceful ears that complement their mystical allure'
        ],
        'Halfling': [
            'Small and cute ears that add to their charm',
            'Moderate-sized ears that exude a warm and friendly vibe',
            'Slightly larger ears that enhance their playful personality',
            'Ears that reflect their love for food and laughter',
            'Ears with a perfect balance of size and mischievousness'
        ],
        'Human': [
            'Versatile ears with a size that varies from individual to individual',
            'Ears that adapt to their diverse human heritage',
            'Ears that reflect their unique life experiences',
            'Moderate-sized ears that suit their cultural surroundings',
            'Ears that showcase the diversity of human appearances'
        ],
        'Dragonborn': [
            'Ears that are proportionate to their dragon-like features',
            'Moderate-sized ears with a hint of dragon ancestry',
            'Ears with a slightly reptilian appearance, matching their lineage',
            'Ears that convey a sense of strength and command',
            'Ears that bear the marks of their dragonblood heritage'
        ],
        'Gnome': [
            'Small and whimsical ears that add to their charm',
            'Moderate-sized ears that reflect their inquisitive nature',
            'Ears that tell tales of their tinkering and inventive spirit',
            'Ears with a playful and mischievous appearance',
            'Ears that match their love for imaginative endeavors'
        ],
        'Half-Elf': [
            'Ears that strike a balance between human and elven proportions',
            'Moderate-sized ears with a subtle elven elegance',
            'Ears that hint at their diplomatic and versatile nature',
            'Ears that bridge the gap between their two worlds',
            'Ears that showcase their unique blend of features'
        ],
        'Half-Orc': [
            'Ears that are proportionate to their rugged and robust appearance',
            'Moderate-sized ears with prominent features',
            'Ears that bear the marks of their adventurous lifestyle',
            'Ears that reflect their orcish determination and resilience',
            'Ears that reveal their strength and endurance'
        ],
        'Tiefling': [
            'Ears with subtle, infernal features that hint at their fiendish heritage',
            'Moderate-sized ears with intriguing marks and patterns',
            'Ears with infernal symbols etched into their flesh',
            'Ears with an eerie presence, charred and smoky in appearance',
            'Ears that command attention, with smoldering patches and an infernal allure'
        ]
    }

    if method == "Automated" or method == "Guided":
        character.description["ear_size"] = random.choice(character_race_ear_size_variations[character_race])
    elif method == "Manual":
        character.description["ear_size"] = terminalmenu_quick_select(character_race_ear_size_variations[character_race], f"[{character_race}] Select ear size:")


    character_race_ear_type_variations = {
        'Dwarf': [
            'Square ears: Matching their sturdy build and practical nature.',
            'Pointed ears: A hint of mischief in their otherwise robust appearance.',
            'Normal ears: Unassuming and functional.',
            'Small ears: Compact and efficient for their needs.'
        ],
        'Elf': [
            'Pointed ears: A defining feature of their ethereal beauty.',
            'Narrow ears: Adding to their graceful and delicate appearance.',
            'Protruding ears & earlobes: Unique among elves, with distinct features.',
            'Normal ears: In harmony with their overall elven grace.'
        ],
        'Halfling': [
            'Protruding ears & earlobes: Adding to their charm and friendliness.',
            'Attached ears & earlobes: Reflecting their warm and inviting nature.',
            'Normal ears: Unassuming but still radiating warmth.'
        ],
        'Human': [
            'Normal ears: Versatile and adaptable, like the humans themselves.',
            'Protruding ears & earlobes: With a touch of individuality.',
            'Attached ears & earlobes: Reflecting their diverse human heritage.'
        ],
        'Dragonborn': [
            'Normal ears: Functional and practical, like their draconic ancestry.',
            'Protruding ears & earlobes: With a hint of dragon-like distinction.',
            'Attached ears & earlobes: Reflecting their unique dragonblood lineage.'
        ],
        'Gnome': [
            'Small ears: Perfectly suited for their inquisitive and imaginative minds.',
            'Big ears: Adding to their whimsy and wonder-filled appearance.',
            'Folded ears: A distinctive feature among gnomes, folding neatly.',
            'Normal ears: Functional but still holding a hint of curiosity.'
        ],
        'Half-Elf': [
            'Normal ears: Combining human and elven characteristics seamlessly.',
            'Protruding ears & earlobes: A touch of elven charm in their appearance.',
            'Attached ears & earlobes: Reflecting their dual heritage.'
        ],
        'Half-Orc': [
            'Normal ears: Functional and resilient, like their rugged lifestyle.',
            'Protruding ears & earlobes: Adding character and strength to their look.',
            'Attached ears & earlobes: Reflecting their orcish features.'
        ],
        'Tiefling': [
            'Normal ears: A subtle feature in contrast to their more striking traits.',
            'Protruding ears & earlobes: With an eerie, infernal presence.',
            'Attached ears & earlobes: Reflecting their connection to darkness.'
        ]
    }

    if method == "Automated" or method == "Guided":
        character.description["ear_type"] = random.choice(character_race_ear_type_variations[character_race])
    elif method == "Manual":
        character.description["ear_type"] = terminalmenu_quick_select(character_race_ear_type_variations[character_race], f"[{character_race}] Select ear type:")


    character_race_hair_variations = {
        'Dwarf': [
            "Black - A deep black that matches the color of their sturdy beards",
            "Brown - A rich brown, like the earth they often work with",
            "Gray - A distinguished gray that comes with age and wisdom",
            "Red - A fiery red that reflects their passionate nature",
            "Other - Various unique colors seen among dwarves"
        ],
        'Elf': [
            "Black - Ebony black, contrasting beautifully with their fair skin",
            "Brown - A natural brown, blending seamlessly with their woodland surroundings",
            "Blonde - Golden blonde, shimmering like the sun-kissed leaves of the forest",
            "Other - Elves may have unique hair colors influenced by their magical heritage"
        ],
        'Halfling': [
            "Brown - A warm brown, much like their inviting personalities",
            "Blonde - A cheerful blonde, reflecting their sunny disposition",
            "Auburn - Auburn hair with a touch of mischief",
            "Other - Halflings often sport various delightful hair colors"
        ],
        'Human': [
            "Black - A common black color seen among humans",
            "Brown - A classic brown that suits a wide range of humans",
            "Blonde - A bright blonde, reflecting their diversity",
            "Red - Vibrant red hair that adds character to their appearance",
            "Other - Humans exhibit diverse hair colors based on their regions and cultures"
        ],
        'Dragonborn': [
            "Red - Fiery red, reminiscent of their draconic ancestors",
            "Gold - Shimmering gold, symbolizing their noble lineage",
            "Blue - A deep blue, resembling the color of the open sky",
            "Other - Dragonborn may have unique hair colors influenced by their dragon heritage"
        ],
        'Gnome': [
            "Brown - A rich brown, complementing their earthy demeanor",
            "Green - Green hair, reflecting their connection to nature",
            "Blue - Vibrant blue, showcasing their whimsical personalities",
            "Other - Gnomes often have colorful and imaginative hair"
        ],
        'Half-Elf': [
            "Brown - A natural brown, bridging their human and elven heritage",
            "Blonde - Blonde hair that adds to their ethereal charm",
            "Silver - Silver hair, hinting at their elven lineage",
            "Other - Half-elves may have unique hair colors influenced by their mixed ancestry"
        ],
        'Half-Orc': [
            "Black - Deep black hair that complements their orcish strength",
            "Brown - A rugged brown, reflecting their resilience",
            "Gray - Gray hair, earned from enduring life’s challenges",
            "Other - Half-orcs may have hair colors influenced by their orc heritage"
        ],
        'Tiefling': [
            "Red - Fiery red, matching their infernal bloodline",
            "Black - Jet black hair with a touch of darkness",
            "Purple - Royal purple, hinting at their mystical nature",
            "Other - Tieflings may have hair colors influenced by their infernal lineage"
        ]
    }

    if method == 'Automated' or method == 'Guided':
        character.description['hair_color'] = random.choice(character_race_hair_variations[character_race])
    elif method == 'Manual':
        character.description['hair_color'] = terminalmenu_quick_select(character_race_hair_variations[character_race], f'[{character_race}] Select a hair color:')


    character_race_hair_types = {
        'Dwarf': [
            "Bald - Dwarves are often known for their bald heads, emphasizing their beards.",
            "Short and sturdy - Dwarves typically have short, sturdy hair that's easy to maintain.",
            "Medium and well-kept - Some Dwarves prefer medium-length hair, well-groomed and adorned with accessories.",
            "Long and braided - Long, braided beards are a common choice for Dwarves, often decorated with beads and charms.",
            "Bald - Dwarves often have little to no hair, emphasizing their focus on craftsmanship.",
            "Thick and wiry - Dwarven hair is known for its thickness and toughness, often styled in practical ways.",
            "Braided and adorned with gems - Some Dwarves braid their hair and decorate it with precious gems as a symbol of their wealth.",
            "Short and practical - Dwarves prefer short and practical haircuts that don't interfere with their work.",
            "Other - Dwarves may have unique hairstyles that reflect their individuality."
        ],
        'Elf': [
            "Bald - Elves are rarely bald, as their longevity ensures they retain their hair throughout their lives.",
            "Short and elegant - Elves often have short, elegant hair that complements their graceful appearance.",
            "Medium and flowing - Many Elves prefer medium-length hair that flows like a cascade of silk.",
            "Long and enchanting - Long, flowing hair is a hallmark of Elven beauty, often adorned with flowers and gems.",
            "Silky and flowing - Elven hair is often silky and flows like fine strands of silk, accentuating their ethereal beauty.",
            "Long and adorned with natural elements - Elves sometimes adorn their hair with leaves, flowers, or subtle magical enhancements.",
            "Tied in intricate patterns - Elven hairstyles can be intricate, with delicate braids and knots.",
            "Shimmering and vibrant - Elf hair can have a shimmering quality, reflecting the light with an otherworldly glow.",
            "Other - Elves may experiment with unique, magical hairstyles that reflect their connection to nature and magic."
        ],
        'Halfling': [
            "Bald - Some Halflings may sport a bald head, which can be quite charming.",
            "Short and playful - Short and playful hairstyles are common among Halflings, reflecting their cheerful nature.",
            "Medium and inviting - Medium-length hair is often inviting and adds to their friendly demeanor.",
            "Long and carefree - A few Halflings choose to grow their hair long, embracing a carefree style.",
            "Curly and playful - Halfling hair is often curly and full of bounce, reflecting their playful nature.",
            "Tied with colorful ribbons - Halflings like to tie their hair with colorful ribbons as a mark of joy and celebration.",
            "Short and practical - Many Halflings keep their hair short for convenience, but it's always well-groomed.",
            "Thick and inviting - Halfling hair can be thick and inviting, making them look warm and welcoming.",
            "Other - Halflings may have unconventional hairstyles that set them apart from others."
        ],
        'Human': [
            "Bald - Baldness is a natural part of aging for many Humans.",
            "Short and versatile - Short hairstyles are practical and versatile for Humans from all walks of life.",
            "Medium and trendy - Medium-length hair is often chosen by fashionable Humans, adapting to various trends.",
            "Long and expressive - Long hair allows Humans to express themselves, whether through styling or color.",
            "Varied styles - Human hair comes in a wide range of styles, reflecting their diversity and adaptability.",
            "Long and flowing - Some humans prefer long, flowing hair, often seen as a symbol of beauty.",
            "Short and practical - Others opt for shorter, practical hairstyles suitable for their daily activities.",
            "Braided and adorned - Human hair can be braided and adorned with jewelry for special occasions.",
            "Other - Humans come in all varieties, and their hairstyles can be as diverse as their personalities."
        ],
        'Dragonborn': [
            "Bald - Some Dragonborn may choose to be bald, embracing their unique appearance.",
            "Short and fierce - Short hair exudes a fierce and powerful aura, complementing their dragon heritage.",
            "Medium and commanding - Medium-length hair can command attention and respect among Dragonborn.",
            "Long and regal - Long, flowing hair symbolizes regal authority and majesty for Dragonborn leaders.",
            "Scales instead of hair - Dragonborn often have scales instead of traditional hair, which can vary in color and texture.",
            "Sparse and functional - Some Dragonborn keep their scales sparse and functional, focusing on their draconic features.",
            "Feathered crest - A few Dragonborn sport a feathered crest on their heads, reminiscent of their dragon ancestors.",
            "Flaming mane - In rare cases, a Dragonborn's 'hair' may appear like a mane of flickering flames.",
            "Other - Dragonborn may have distinct, scaled hairstyles that reflect their draconic lineage."
        ],
        'Gnome': [
            "Bald - Gnomes, with their unique sense of humor, may occasionally go bald just for fun.",
            "Short and whimsical - Short, whimsical hairstyles are common among Gnomes, showcasing their playful spirit.",
            "Medium and inventive - Medium-length hair offers a canvas for inventive Gnomish hairstyles, often incorporating gadgets.",
            "Long and creative - Some Gnomes embrace long, creative hairstyles that serve as a conversation starter.",
            "Vibrant and colorful - Gnome hair comes in a riot of vibrant colors, often reflecting their cheerful personalities.",
            "Wild and untamed - Gnomes embrace their wild side, allowing their hair to grow in every direction.",
            "Braided with tinkering tools - Some Gnomes incorporate tiny tinkering tools into their braided hair.",
            "Short and spiky - Gnomes who prefer practicality opt for short and spiky hairstyles that match their inventiveness.",
            "Other - Gnomes love experimenting, and their hairstyles can range from quirky to unconventional."
        ],
        'Half-Elf': [
            "Bald - Like Elves, Half-Elves rarely go bald due to their Elven heritage.",
            "Short and enchanting - Short, enchanting hairstyles are favored by Half-Elves, emphasizing their charisma.",
            "Medium and captivating - Medium-length hair enhances the captivating allure of Half-Elves.",
            "Long and graceful - Long, graceful hair adds an extra layer of charm and elegance to Half-Elves.",
            "Blending of styles - Half-Elves often combine human and elven hair traditions, creating unique and beautiful hairstyles.",
            "Wavy and enchanting - Half-Elven hair is often wavy and enchanting, capturing the attention of others.",
            "Elaborate braids - Some Half-Elves enjoy elaborate braids that blend both human and elven aesthetics.",
            "Subtle magical glimmer - A faint magical glimmer can sometimes be seen in a Half-Elf's hair, a testament to their dual heritage.",
            "Other - Half-Elves may adopt hairstyles that blend their human and elven traits, creating a unique look."
        ],
        'Half-Orc': [
            "Bald - Some Half-Orcs may have bald heads, showcasing their rugged appearance.",
            "Short and focused - Short, focused hairstyles emphasize the determined nature of Half-Orcs.",
            "Medium and determined - Medium-length hair complements the unwavering resolve of many Half-Orcs.",
            "Long and unyielding - Long, unyielding hair represents the unbreakable spirit of certain Half-Orcs.",
            "Practical and rugged - Half-Orcs usually keep their hair practical and rugged, reflecting their no-nonsense approach to life.",
            "Tribal and adorned - Some Half-Orcs adorn their hair with tribal ornaments and symbols that signify their heritage.",
            "Short and fierce - Short, spiky hair is common among Half-Orcs, giving them a fierce appearance.",
            "Mohawk with tribal paint - A few Half-Orcs sport a mohawk hairstyle with tribal paint markings on their scalp.",
            "Other - Half-Orcs may have distinctive hairstyles that reflect their individuality."
        ],
        'Tiefling': [
            "Bald - A few Tieflings may sport a bald head, highlighting their unique features.",
            "Short and enigmatic - Short, enigmatic hairstyles add to the mysterious allure of Tieflings.",
            "Medium and beguiling - Medium-length hair is often chosen by Tieflings to enhance their beguiling charm.",
            "Long and hypnotic - Long, flowing hair can be mesmerizing on a Tiefling, drawing attention to their infernal beauty.",
            "Fiery and striking - Tiefling hair can be fiery red, with streaks of orange or maroon, making them truly stand out.",
            "Infernal patterns - Some Tieflings have intricate patterns in their hair, resembling runes or flames.",
            "Black as the abyss - Others have hair as dark as the abyss, with an otherworldly sheen.",
            "Smoky tendrils - Tiefling hair can appear like smoky tendrils, adding an eerie and mysterious allure.",
            "Other - Tieflings often experiment with hair designs that reflect their infernal heritage."
        ]
    }

    # Update the character's hair type based on the selected method.
    if method == 'Automated' or method == 'Guided':
        character.description['hair_type'] = random.choice(character_race_hair_types[character_race])
    elif method == 'Manual':
        character.description['hair_type'] = terminalmenu_quick_select(character_race_hair_types[character_race], f'[{character_race}] Select a hair type:')


    character_race_hair_styles = {
        'Dwarf': [
            "Bald - Dwarves often sport bald heads, emphasizing their rugged features.",
            "Short - Short, well-trimmed hair is common among Dwarves for practicality.",
            "Medium - Some Dwarves prefer medium-length hair, neatly groomed.",
            "Long - Uncommon but not unheard of, Dwarves with long hair are distinctive.",
            "Bun - Neatly tied buns are a traditional choice for Dwarven women.",
            "Braid - Braided hair, often adorned with metal clasps, is a symbol of Dwarven craftsmanship.",
            "Ponytail - Tied-back ponytails are favored by Dwarves who value utility.",
            "Dreadlocks - Rare but distinctive, Dwarves with dreadlocks are known for their unique style.",
            "Topknot - A topknot hairstyle signifies authority and respect among Dwarves.",
            "Wild - Some Dwarves embrace a wild and untamed hairdo, reflecting their adventurous spirit.",
            "Stone-carved Patterns - Dwarves may etch intricate patterns into their hair, resembling stone carvings.",
            "Gem-Adorned Braids - Dwarves occasionally weave precious gems into their braids for added flair.",
            "Molten Metal Highlights - Some Dwarves add streaks of molten metal to their hair, symbolizing their craftsmanship.",
        ],
        'Elf': [
            "Bald - Some Elves prefer a bald look, highlighting their graceful features.",
            "Short - Short, delicate hairstyles are favored by many Elves.",
            "Medium - Medium-length hair with graceful waves is common among Elves.",
            "Long - Long, flowing locks are a hallmark of Elven beauty.",
            "Bun - Elven buns are intricate and adorned with natural elements like flowers.",
            "Braid - Elven braids are artistic and often incorporate leaves or vines.",
            "Ponytail - Elven ponytails are elegant and designed to look effortless.",
            "Dreadlocks - Rare among Elves, dreadlocks are worn by those who embrace a unique style.",
            "Wind-swept - Elves may style their hair to appear as if it's always caught in a gentle breeze.",
            "Elaborate Updo - Elven updos are a display of artistry, adorned with intricate designs.",
            "Moonlight Glow - Some Elves enhance their hair to emit a soft, moonlight-like glow, creating an ethereal effect.",
            "Nature's Harmony - Elven hairstyles may incorporate natural elements like leaves, flowers, and small birds' nests.",
            "Starry Constellations - Elven hair artistry may feature intricate patterns resembling celestial constellations.",
        ],
        'Halfling': [
            "Bald - Some Halflings prefer a bald look for ease of maintenance.",
            "Short - Short, tidy hair is common among Halflings.",
            "Medium - Medium-length hair is often seen among Halflings.",
            "Long - Long hair is a bit unusual but not unheard of among Halflings.",
            "Ponytail - Practical and charming, Halfling ponytails are common.",
            "Bun - Halfling buns are cozy and often decorated with small accessories.",
            "Braid - Braided hair is popular among Halfling adventurers for its convenience.",
            "Pigtails - Pigtails are a playful choice for some Halfling women.",
            "Messy - Halflings who embrace a messy hairstyle exude a carefree spirit.",
            "Wavy - Some Halflings prefer a wavy hairdo, adding a touch of elegance.",
            "Hobbiton Curls - Halflings from certain regions may sport distinctive curls reminiscent of their homeland.",
            "Garden Blossoms - Halflings may adorn their hair with tiny, living blossoms that bloom and change with the seasons.",
            "Traveler's Braids - Halflings who've embarked on many journeys may weave tokens of their adventures into their braids.",
        ],
        'Human': [
            "Bald - Some Humans opt for a bald look, embracing their natural appearance.",
            "Short - Short, versatile hair is common among Humans.",
            "Medium - Medium-length hair is a classic choice for many Humans.",
            "Long - Long, flowing hair is popular among both men and women.",
            "Ponytail - Ponytails are practical and common among Human adventurers.",
            "Bun - Buns are elegant and suitable for formal occasions.",
            "Braid - Braids are a practical choice for Human warriors and travelers.",
            "Pigtails - Pigtails are a playful hairstyle favored by some Human women.",
            "Curls - Curly hair adds a touch of charm and sophistication to some Human styles.",
            "Afro - An afro hairstyle showcases diversity and pride in heritage among Humans.",
            "Regal Crown - Some Humans with noble lineage may sport a hairstyle that resembles a royal crown.",
            "Tribal Warrior's Braids - Humans from tribal cultures may wear intricate warrior-inspired braids adorned with feathers and beads.",
            "Navigator's Knots - Seafaring Humans may have hair styled into intricate knots symbolizing their maritime expertise.",
        ],
        'Dragonborn': [
            "Bald - Some Dragonborn choose to keep their heads bald, focusing on their scales.",
            "Short - Short hair is practical for Dragonborn, complementing their unique appearance.",
            "Medium - Medium-length hair can provide a striking contrast to their scales.",
            "Long - Long hair is rare among Dragonborn but can make a bold statement.",
            "Ponytail - Dragonborn ponytails are sturdy and efficient in battle.",
            "Bun - Buns are practical for Dragonborn who prefer a tidy appearance.",
            "Braid - Braided hair can be adorned with decorative scales, showcasing their heritage.",
            "Pigtails - Uncommon but distinctive, Dragonborn pigtails draw attention.",
            "Spikes - Dragonborn who desire an edgier look may sport spiked hair.",
            "Flames - Some Dragonborn style their hair to resemble flickering flames, a tribute to their draconic nature.",
            "Crystal Embellishments - Dragonborn may add crystal-like extensions to their hair, creating a shimmering effect.",
            "Elemental Flow - Dragonborn with elemental ancestry may have hair that appears to flow like water, flicker like fire, or sway like the wind.",
            "Scale Braids - Dragonborn warriors may incorporate tiny, intricately woven scales into their braids, representing their battles.",
        ],
        'Gnome': [
            "Bald - Some Gnomes embrace a bald look, focusing on their unique facial features.",
            "Short - Short, quirky hairstyles are common among Gnomes.",
            "Medium - Medium-length hair offers Gnomes room for creative styles.",
            "Long - Long, whimsical hair is favored by adventurous Gnomes.",
            "Ponytail - Gnome ponytails are often adorned with tiny accessories or tinkering tools.",
            "Bun - Buns are practical for Gnomes who value functionality in their style.",
            "Braid - Braided hair can incorporate small gadgets and charms, showcasing their inventiveness.",
            "Pigtails - Pigtails are a playful choice for many Gnome women.",
            "Corkscrew Curls - Gnomes with corkscrew curls showcase their unique sense of style.",
            "Glowing - Some Gnomes experiment with hair that faintly glows in the dark for a whimsical effect.",
            "Mechanical Wires - Inventive Gnomes may weave tiny, functional mechanical wires into their hair, creating moving parts.",
            "Gnome Garden - Gnomes with an affinity for nature may cultivate small plants and flowers in their hair, forming a miniature garden.",
            "Clockwork Hairpins - Gnomes interested in timekeeping may wear hairpins that resemble miniature clocks, complete with ticking mechanisms.",
        ],
        'Half-Elf': [
            "Bald - Some Half-Elves embrace a bald look, emphasizing their elven and human features.",
            "Short - Short, graceful hairstyles are common among Half-Elves.",
            "Medium - Medium-length hair with an elegant touch is a favorite among many Half-Elves.",
            "Long - Long, flowing hair blends elven and human beauty seamlessly.",
            "Ponytail - Half-Elven ponytails are versatile and adapt well to various occasions.",
            "Bun - Buns are a classic choice for Half-Elves, often adorned with elven motifs.",
            "Braid - Elven-style braids or human-inspired braids offer diverse choices.",
            "Pigtails - Pigtails are a playful and charming option for some Half-Elven women.",
            "Flowing Waves - Half-Elves with wavy hair exude an enchanting aura.",
            "Fringe - Some Half-Elves opt for a stylish fringe that adds a touch of mystery to their look.",
            "Faerie Lights - Half-Elves may add shimmering, colorful lights to their hair, reminiscent of faerie magic.",
            "Dual Braids - Half-Elves of mixed heritage may weave dual braids, symbolizing their dual lineage.",
            "Celtic Knots - Half-Elves inspired by ancient cultures may have their hair styled in intricate Celtic knots.",
        ],
        'Half-Orc': [
            "Bald - Some Half-Orcs prefer a bald look, emphasizing their orcish and human traits.",
            "Short - Short, practical hair is common among Half-Orcs.",
            "Medium - Medium-length hair is often favored by Half-Orcs, easy to maintain.",
            "Long - Long hair is unusual but not unheard of among Half-Orcs.",
            "Ponytail - Half-Orc ponytails are robust and complement their rugged appearance.",
            "Bun - Buns are a practical choice for Half-Orcs who value functionality.",
            "Braid - Braided hair can be adorned with tribal decorations, showcasing their heritage.",
            "Pigtails - Pigtails are a distinctive choice for some Half-Orc women.",
            "Wild Mohawk - Half-Orcs who dare to be bold may sport a wild mohawk.",
            "Tribal Patterns - Some Half-Orcs incorporate tribal patterns into their hair, symbolizing their roots.",
            "War Paint Streaks - Half-Orc warriors may paint colorful streaks across their hair, indicating their victories.",
            "Orcish Totems - Some Half-Orcs incorporate small totemic charms and trinkets into their hair, each with a symbolic meaning.",
            "Battle Scars - Battle-hardened Half-Orcs may have their hair shaped to accentuate their scars and combat prowess.",
        ],
        'Tiefling': [
            "Bald - Some Tieflings embrace a bald look, emphasizing their infernal features.",
            "Short - Short, stylish hair is a popular choice among Tieflings.",
            "Medium - Medium-length hair offers Tieflings room for unique and fiery styles.",
            "Long - Long, dramatic hair complements the allure of Tiefling charm.",
            "Ponytail - Tiefling ponytails are often adorned with infernal trinkets or charms.",
            "Bun - Buns are practical for Tieflings who value both style and function.",
            "Braid - Infernal-inspired braids showcase their fiendish heritage with flair.",
            "Pigtails - Pigtails with a touch of infernal flair are a captivating choice for some Tiefling women.",
            "Fiery Waves - Tieflings with fiery waves in their hair embody their infernal nature.",
            "Serpentine - Some Tieflings style their hair to resemble serpentine scales, a nod to their lineage.",
            "Infernal Glyphs - Tieflings may have arcane glyphs etched into their hair, glowing with infernal energy.",
            "Cursed Veil - Some Tieflings drape their hair in a diaphanous veil that appears to be cursed and billows with ethereal darkness.",
            "Abyssal Tentacles - Adventurous Tieflings may braid tentacle-like extensions into their hair, invoking the Abyss.",
        ]
    }

    if method == 'Automated' or method == 'Guided':
        character.description['hair_style'] = random.choice(character_race_hair_styles[character_race])
    elif method == 'Manual':
        character.description['hair_style'] = terminalmenu_quick_select(character_race_hair_styles[character_race], f'[{character_race}] Select a hair style:')


    character_race_facial_hair = {
        'Dwarf': [
            "None - Dwarves often have clean-shaven faces, prioritizing practicality.",
            "Beard - Full, lush beards are a common sight among Dwarven men.",
            "Mustache - A well-groomed mustache is a symbol of Dwarven pride.",
            "Goatee - Some Dwarves prefer a goatee to add a touch of style.",
            "Chinstrap - A chinstrap beard is a distinctive choice among Dwarves.",
            "Soul Patch - A small soul patch beneath the lower lip is stylish for some.",
            "Scruff - Rugged scruff is practical for Dwarves who value function over style.",
            "Other - Dwarves may have unique facial hair styles reflecting their individuality.",
        ],
        'Elf': [
            "None - Many Elves have smooth, clean-shaven faces that emphasize their grace.",
            "Beard - Some Elven men sport subtle beards, well-kept and elegant.",
            "Mustache - An exquisite mustache is favored by a few stylish Elves.",
            "Goatee - A goatee adds a touch of sophistication to some Elven faces.",
            "Chinstrap - Elven chinstrap beards are often finely crafted and artistic.",
            "Soul Patch - A small soul patch beneath the lower lip can be a charming choice.",
            "Scruff - Rugged scruff is rare among Elves but may suit those who embrace a more natural look.",
            "Other - Elves may have unique facial hair styles reflecting their individuality and culture.",
        ],
        'Halfling': [
            "None - Halflings often have smooth, clean-shaven faces that radiate friendliness.",
            "Beard - Some Halfling men sport small, neat beards for a touch of charm.",
            "Mustache - A dashing mustache is favored by a few stylish Halflings.",
            "Goatee - A goatee adds a touch of character to some Halfling faces.",
            "Chinstrap - Halfling chinstrap beards are playful and charming.",
            "Soul Patch - A small soul patch beneath the lower lip can be endearing for some.",
            "Scruff - Casual scruff is a practical choice for Halflings who value simplicity.",
            "Other - Halflings may have unique facial hair styles reflecting their individuality and love for good food.",
        ],
        'Human': [
            "None - Humans often have diverse and ever-changing facial hair styles.",
            "Beard - Beards come in all shapes and sizes among Human men.",
            "Mustache - A well-groomed mustache is a classic choice for some Human men.",
            "Goatee - A goatee adds a touch of style to many Human faces.",
            "Chinstrap - A chinstrap beard is a bold choice for some Human men.",
            "Soul Patch - A small soul patch beneath the lower lip is a trendy choice for some.",
            "Scruff - Casual scruff is a versatile and common style among Humans.",
            "Other - Humans have a wide range of facial hair styles reflecting their diverse cultures and preferences.",
        ],
        'Dragonborn': [
            "None - Many Dragonborn prefer to emphasize their unique scales over facial hair.",
            "Beard - Some Dragonborn have short, well-kept beards that complement their distinctive features.",
            "Mustache - A carefully groomed mustache is a sign of refinement among some Dragonborn.",
            "Goatee - A goatee can add a touch of style to Dragonborn faces.",
            "Chinstrap - A chinstrap beard can enhance the fierce appearance of some Dragonborn.",
            "Soul Patch - A small soul patch beneath the lower lip can be a bold choice for some Dragonborn.",
            "Scruff - Rugged scruff is practical for Dragonborn who value function over style.",
            "Other - Dragonborn may have unique facial hair styles that incorporate their draconic heritage.",
        ],
        'Gnome': [
            "None - Gnomes often have smooth, clean-shaven faces that emphasize their inquisitive expressions.",
            "Beard - Some Gnomes sport small, neatly groomed beards that reflect their love of tinkering.",
            "Mustache - A whimsical mustache is favored by a few stylish Gnomes.",
            "Goatee - A goatee adds a touch of character to some Gnomish faces.",
            "Chinstrap - Gnomish chinstrap beards are often adorned with tiny mechanical accessories.",
            "Soul Patch - A small soul patch beneath the lower lip can be a charming choice for some Gnomes.",
            "Scruff - Casual scruff is practical for Gnomes who value functionality in their style.",
            "Other - Gnomes may have unique facial hair styles reflecting their inventiveness and curiosity.",
        ],
        'Half-Elf': [
            "None - Half-Elves often have smooth, clean-shaven faces that reflect their dual heritage.",
            "Beard - Some Half-Elven men sport subtle beards that blend human and elven beauty.",
            "Mustache - An elegant mustache is a classic choice for some Half-Elves.",
            "Goatee - A goatee adds a touch of sophistication to Half-Elven faces.",
            "Chinstrap - Half-Elven chinstrap beards can be a symbol of their mixed heritage.",
            "Soul Patch - A small soul patch beneath the lower lip can be a charming choice for some Half-Elves.",
            "Scruff - Rugged scruff can reflect the adventurous spirit of some Half-Elves.",
            "Other - Half-Elves may have unique facial hair styles that bridge their two worlds.",
        ],
        'Half-Orc': [
            "None - Many Half-Orcs prefer to keep their faces clean-shaven, showcasing their orcish features.",
            "Beard - Some Half-Orcs sport short, robust beards that emphasize their rugged appearance.",
            "Mustache - A well-groomed mustache can add character to some Half-Orc faces.",
            "Goatee - A goatee is a stylish choice for some Half-Orcs.",
            "Chinstrap - Half-Orc chinstrap beards are bold and reflect their strong presence.",
            "Soul Patch - A small soul patch beneath the lower lip can be a distinctive choice for some.",
            "Scruff - Rugged scruff is practical and complements the toughness of Half-Orcs.",
            "Other - Half-Orcs may have unique facial hair styles that reflect their individuality and orcish heritage.",
        ],
        'Tiefling': [
            "None - Tieflings often prefer to keep their faces clean-shaven, emphasizing their infernal features.",
            "Beard - Some Tieflings sport short, well-groomed beards that contrast with their fiendish traits.",
            "Mustache - A carefully groomed mustache is a symbol of refinement among some Tieflings.",
            "Goatee - A goatee adds a touch of style to Tiefling faces.",
            "Chinstrap - Tiefling chinstrap beards can enhance their enigmatic appearance.",
            "Soul Patch - A small soul patch beneath the lower lip can be an intriguing choice for some Tieflings.",
            "Scruff - Rugged scruff is practical for Tieflings who value function over style.",
            "Other - Tieflings may have unique facial hair styles that incorporate their infernal lineage.",
        ]
    }

    if method == 'Automated' or method == 'Guided':
        character.description['facial_hair'] = random.choice(character_race_facial_hair[character_race])
    elif method == 'Manual':
        character.description['facial_hair'] = terminalmenu_quick_select(character_race_facial_hair[character_race], f'[{character_race}] Select a facial hair style:')


    character_race_facial_features = {
        'Dwarf': [
            "None - Dwarves often have sturdy, feature-rich faces.",
            "Scar - Battle scars are common among Dwarves, displaying their resilience.",
            "Tattoo - Dwarves may bear tattoos with clan symbols or personal meanings.",
            "Piercing - Facial piercings, such as beard rings, are a Dwarven tradition.",
            "Other - Dwarves may have unique facial features reflecting their individuality.",
        ],
        'Elf': [
            "None - Elves have naturally graceful and enchanting facial features.",
            "Scar - Subtle scars from elven battles may add character to their beauty.",
            "Tattoo - Elven tattoos are elegant and often symbolize their connection to nature.",
            "Piercing - Delicate facial piercings, like ear cuffs, are favored by Elves.",
            "Other - Elves may have exotic facial features reflecting their ethereal nature.",
        ],
        'Halfling': [
            "None - Halflings possess charming and inviting facial features.",
            "Scar - Playful scars from adventurous endeavors may grace their faces.",
            "Tattoo - Halflings may have small, whimsical tattoos that tell stories.",
            "Piercing - Cheek or nose piercings add to their mischievous charm.",
            "Other - Halflings may have unique facial features reflecting their joyful spirits.",
        ],
        'Human': [
            "None - Humans have diverse facial features that reflect their varied backgrounds.",
            "Scar - Scars from life experiences may be visible, each with its own story.",
            "Tattoo - Tattoos representing cultural affiliations or personal beliefs are common.",
            "Piercing - Humans may have a wide range of facial piercings for self-expression.",
            "Other - Humans have unique facial features reflecting their individuality and culture.",
        ],
        'Dragonborn': [
            "None - Dragonborn have distinctive reptilian features.",
            "Scar - Battle scars may highlight their strength and resilience.",
            "Tattoo - Intricate tattoos resembling dragon scales are a common choice.",
            "Piercing - Dragonborn piercings often incorporate gemstones and metals.",
            "Other - Dragonborn may have facial features that reflect their draconic ancestry.",
        ],
        'Gnome': [
            "None - Gnomes have whimsical and expressive facial features.",
            "Scar - Scars from mechanical experiments may add character to their faces.",
            "Tattoo - Gnomes may have tattoos inspired by their inventions or adventures.",
            "Piercing - Facial piercings with mechanical motifs showcase their inventiveness.",
            "Other - Gnomes may have eccentric facial features reflecting their creative minds.",
        ],
        'Half-Elf': [
            "None - Half-Elves possess a harmonious blend of elven and human features.",
            "Scar - Subtle scars from diplomatic negotiations or adventures may be visible.",
            "Tattoo - Elven-inspired tattoos with delicate designs often grace their faces.",
            "Piercing - Half-Elves may have piercings that symbolize their mixed heritage.",
            "Other - Half-Elves may have unique facial features reflecting their diverse lineage.",
        ],
        'Half-Orc': [
            "None - Half-Orcs have a blend of orcish and human features.",
            "Scar - Battle scars from life's challenges may add character to their faces.",
            "Tattoo - Tattoos with tribal motifs are common among Half-Orcs.",
            "Piercing - Bold facial piercings are favored by some Half-Orcs.",
            "Other - Half-Orcs may have unconventional facial features reflecting their individuality.",
        ],
        'Tiefling': [
            "None - Tieflings often have infernal features that set them apart.",
            "Scar - Subtle infernal markings may add an eerie charm to their faces.",
            "Tattoo - Infernal-inspired tattoos with dark designs are a common choice.",
            "Piercing - Piercings with an infernal edge showcase their fiendish heritage.",
            "Other - Tieflings may have unique facial features reflecting their infernal lineage.",
        ]
    }

    if method == 'Automated' or method == 'Guided':
        character.description['facial_features'] = random.choice(character_race_facial_features[character_race])
    elif method == 'Manual':
        character.description['facial_features'] = terminalmenu_quick_select(character_race_facial_features[character_race], f'[{character_race}] Select a facial feature:')


    character_race_body_types = {
        'Dwarf': [
            "Stocky and sturdy, reflecting Dwarven resilience.",
            "Compact and strong, ideal for underground life.",
            "Solid and well-built, showcasing Dwarven craftsmanship.",
            "Robust and stout, a common Dwarven physique.",
        ],
        'Elf': [
            "Graceful and slender, embodying Elven elegance.",
            "Lean and lithe, ideal for agile movements.",
            "Delicate and ethereal, a hallmark of Elven beauty.",
            "Svelte and slender, common among Elves.",
        ],
        'Halfling': [
            "Petite and charming, a typical Halfling stature.",
            "Small and agile, perfect for nimble adventurers.",
            "Compact and dexterous, fitting for Halfling wanderers.",
            "Tiny yet agile, reflecting Halfling versatility.",
        ],
        'Human': [
            "Varied and diverse, reflecting the breadth of humanity.",
            "Adaptable and versatile, suited to various lifestyles.",
            "Average and typical, representing the human norm.",
            "Well-rounded and adaptable, common among humans.",
        ],
        'Dragonborn': [
            "Powerful and imposing, showcasing their draconic heritage.",
            "Majestic and strong, echoing their dragon-like presence.",
            "Sturdy and resilient, reflecting their reptilian ancestry.",
            "Impressive and muscular, a common Dragonborn physique.",
        ],
        'Gnome': [
            "Small and spry, ideal for Gnomish inventors.",
            "Compact and nimble, suitable for tinkering and exploration.",
            "Energetic and compact, typical of Gnome adventurers.",
            "Tiny yet lively, reflecting Gnomish enthusiasm.",
        ],
        'Half-Elf': [
            "A blend of human and Elven features, balanced and graceful.",
            "Flexible and adaptable, embodying the best of both worlds.",
            "Elegant and versatile, common among Half-Elves.",
            "Well-proportioned and charismatic, a typical Half-Elven physique.",
        ],
        'Half-Orc': [
            "Robust and strong, showcasing their orcish heritage.",
            "Tough and resilient, ideal for surviving in harsh conditions.",
            "Brawny and muscular, common among Half-Orcs.",
            "Powerful and imposing, a typical Half-Orc stature.",
        ],
        'Tiefling': [
            "Sleek and alluring, reflecting their infernal charm.",
            "Graceful and exotic, embodying their fiendish allure.",
            "Elegant and striking, common among Tieflings.",
            "Sensual and charismatic, a typical Tiefling physique.",
        ]
    }

    if method == 'Automated' or method == 'Guided':
        character.description['body_type'] = random.choice(character_race_body_types[character_race])
    elif method == 'Manual':
        character.description['body_type'] = terminalmenu_quick_select(character_race_body_types[character_race], f'[{character_race}] Select a body type:')


    character_race_tattoo_locations = {
        'Dwarf': [
            "None - Dwarves typically prefer unadorned skin to showcase their ruggedness.",
            "Left Arm - Dwarves sometimes display intricate tattoos on their left arm, signifying their clan.",
            "Right Arm - Right arm tattoos are common among Dwarves, often depicting ancestral symbols.",
            "Both Arms - Dwarves who value tradition may have tattoos on both arms, connecting to their heritage.",
            "Left Leg - Some Dwarves choose to ink their left leg with stories of their adventures.",
            "Right Leg - Right leg tattoos are favored by Dwarven warriors to display their prowess.",
            "Both Legs - Rare but striking, Dwarves with tattoos on both legs are known for their unique style.",
            "Chest - Dwarves who wish to keep their tattoos private may choose their chest as a canvas.",
            "Back - Dwarven back tattoos often feature grand tales of their people's history.",
            "Other - Dwarves may have unconventional tattoo locations reflecting their individuality and experiences.",
        ],
        'Elf': [
            "None - Many Elves prefer unadorned skin to maintain their natural beauty.",
            "Left Arm - Elven left arm tattoos may be delicate and represent their connection to nature.",
            "Right Arm - Right arm tattoos among Elves often depict artistic symbols and elven script.",
            "Both Arms - Some Elves choose to have tattoos on both arms, showcasing their heritage.",
            "Left Leg - Elven left leg tattoos can depict scenes from their woodland homes.",
            "Right Leg - Right leg tattoos are favored by Elven warriors, telling tales of their battles.",
            "Both Legs - Rare but enchanting, Elves with tattoos on both legs are known for their unique style.",
            "Chest - Elven chest tattoos may remain hidden, reserved for special occasions.",
            "Back - Elven back tattoos often feature intricate designs inspired by nature and magic.",
            "Other - Elves may have exotic tattoo locations that reflect their individuality and culture.",
        ],
        'Halfling': [
            "None - Halflings often prefer unadorned skin, emphasizing their cheerful personalities.",
            "Left Arm - Halfling left arm tattoos may be whimsical and reflect their love for adventure.",
            "Right Arm - Right arm tattoos among Halflings often feature symbols of luck and happiness.",
            "Both Arms - Some Halflings choose to have tattoos on both arms, celebrating their joyous nature.",
            "Left Leg - Halfling left leg tattoos may depict scenes from their homely Shires.",
            "Right Leg - Right leg tattoos are favored by adventurous Halflings, telling stories of their journeys.",
            "Both Legs - Rare but delightful, Halflings with tattoos on both legs are known for their unique style.",
            "Chest - Halfling chest tattoos may remain hidden beneath their clothing, revealing their secrets only to loved ones.",
            "Back - Halfling back tattoos often feature charming designs inspired by the simple pleasures of life.",
            "Other - Halflings may have unconventional tattoo locations reflecting their individuality and hobbies.",
        ],
        'Human': [
            "None - Humans often embrace unadorned skin, emphasizing their diverse backgrounds.",
            "Left Arm - Human left arm tattoos may symbolize their personal beliefs and values.",
            "Right Arm - Right arm tattoos among Humans often depict important life events or milestones.",
            "Both Arms - Some Humans choose to have tattoos on both arms, representing their multifaceted nature.",
            "Left Leg - Human left leg tattoos can be a canvas for artistic expression and self-discovery.",
            "Right Leg - Right leg tattoos are favored by Human adventurers, each telling a unique tale.",
            "Both Legs - Rare but intriguing, Humans with tattoos on both legs are known for their unique style.",
            "Chest - Human chest tattoos may remain hidden beneath their clothing, reserved for special occasions.",
            "Back - Human back tattoos often feature diverse designs that reflect their life experiences.",
            "Other - Humans may have exotic tattoo locations reflecting their diverse cultures and journeys.",
        ],
        'Dragonborn': [
            "None - Dragonborn often prioritize the grandeur of their scales over tattoos.",
            "Left Arm - Dragonborn left arm tattoos may depict their draconic heritage and clan affiliations.",
            "Right Arm - Right arm tattoos among Dragonborn often feature intricate patterns inspired by dragons.",
            "Both Arms - Some Dragonborn choose to have tattoos on both arms, celebrating their lineage.",
            "Left Leg - Dragonborn left leg tattoos can represent their personal journeys and adventures.",
            "Right Leg - Right leg tattoos are favored by Dragonborn warriors, displaying their valor.",
            "Both Legs - Rare but striking, Dragonborn with tattoos on both legs are known for their unique style.",
            "Chest - Dragonborn chest tattoos may remain hidden beneath their scales, only revealed in moments of vulnerability.",
            "Back - Dragonborn back tattoos often feature designs that honor their dragon ancestors.",
            "Other - Dragonborn may have unconventional tattoo locations that incorporate their unique scales and features.",
        ],
        'Gnome': [
            "None - Gnomes often prioritize their quirky nature over tattoos.",
            "Left Arm - Gnome left arm tattoos may depict tiny mechanical wonders and gadgets.",
            "Right Arm - Right arm tattoos among Gnomes often feature playful designs and tinkering tools.",
            "Both Arms - Some Gnomes choose to have tattoos on both arms, showcasing their inventive spirit.",
            "Left Leg - Gnome left leg tattoos can incorporate whimsical scenes from their creative minds.",
            "Right Leg - Right leg tattoos are favored by adventurous Gnomes, often displaying their love for exploration.",
            "Both Legs - Rare but fascinating, Gnomes with tattoos on both legs are known for their unique style.",
            "Chest - Gnome chest tattoos may remain hidden beneath their clothing, only revealed when curiosity strikes.",
            "Back - Gnome back tattoos often feature intricate designs inspired by their mechanical inventions.",
            "Other - Gnomes may have unconventional tattoo locations reflecting their inventiveness and sense of wonder.",
        ],
        'Half-Elf': [
            "None - Half-Elves often choose to embrace their mixed heritage with unadorned skin.",
            "Left Arm - Half-Elven left arm tattoos may blend elven and human symbols in harmony.",
            "Right Arm - Right arm tattoos among Half-Elves often depict their personal journeys and experiences.",
            "Both Arms - Some Half-Elves choose to have tattoos on both arms, symbolizing their dual nature.",
            "Left Leg - Half-Elven left leg tattoos can tell the story of their diverse heritage.",
            "Right Leg - Right leg tattoos are favored by Half-Elven adventurers, each marking a significant chapter.",
            "Both Legs - Rare but enchanting, Half-Elves with tattoos on both legs are known for their unique style.",
            "Chest - Half-Elven chest tattoos may remain hidden beneath their clothing, revealed only in intimate moments.",
            "Back - Half-Elven back tattoos often feature elegant designs that honor their elven and human backgrounds.",
            "Other - Half-Elves may have exotic tattoo locations that blend the essence of both worlds they hail from.",
        ],
        'Half-Orc': [
            "None - Half-Orcs often value their rugged appearance and prefer unadorned skin.",
            "Left Arm - Half-Orc left arm tattoos may depict tribal symbols and stories of their orcish heritage.",
            "Right Arm - Right arm tattoos among Half-Orcs often feature scars from battles and challenges faced.",
            "Both Arms - Some Half-Orcs choose to have tattoos on both arms, showcasing their diverse experiences.",
            "Left Leg - Half-Orc left leg tattoos can tell tales of their nomadic and adventurous lifestyle.",
            "Right Leg - Right leg tattoos are favored by Half-Orc warriors, displaying their prowess.",
            "Both Legs - Rare but captivating, Half-Orcs with tattoos on both legs are known for their unique style.",
            "Chest - Half-Orc chest tattoos may remain hidden beneath their clothing, revealed only to those they trust.",
            "Back - Half-Orc back tattoos often feature tribal designs that honor their orcish roots.",
            "Other - Half-Orcs may have unconventional tattoo locations reflecting their individuality and culture.",
        ],
        'Tiefling': [
            "None - Tieflings often embrace their infernal heritage and may prefer unadorned skin.",
            "Left Arm - Tiefling left arm tattoos may depict fiendish symbols and infernal designs.",
            "Right Arm - Right arm tattoos among Tieflings often feature arcane runes and mystical patterns.",
            "Both Arms - Some Tieflings choose to have tattoos on both arms, reflecting their otherworldly nature.",
            "Left Leg - Tiefling left leg tattoos can incorporate eerie scenes from their infernal lineage.",
            "Right Leg - Right leg tattoos are favored by Tiefling adventurers, displaying their supernatural charm.",
            "Both Legs - Rare but mesmerizing, Tieflings with tattoos on both legs are known for their unique style.",
            "Chest - Tiefling chest tattoos may remain hidden beneath their clothing, revealed only when they desire.",
            "Back - Tiefling back tattoos often feature designs that evoke the essence of their infernal ancestry.",
            "Other - Tieflings may have exotic tattoo locations that reflect their infernal power and enigmatic aura.",
        ]
    }
    if method == 'Automated' or method == 'Guided':
        character.description['tattoo_location'] = random.choice(character_race_tattoo_locations[character_race])
    elif method == 'Manual':
        character.description['tattoo_location'] = terminalmenu_quick_select(character_race_tattoo_locations[character_race], f'[{character_race}] Select a tattoo location:')

    # character.description['tattoo_pattern'] = str(random.choice(list(['None','Tribal','Mural','Faces','Words','Dates','Strip','Triangle','Square','Other'])))
    # character.description['tattoo_amount'] = str(random.choice(list(['None','Few','Some','Many','Other'])))
    # character.description['tattoo_density'] = str(random.choice(list(['None','Sparse','Normal','Dense','Other'])))
    # character.description['tattoo_texture'] = str(random.choice(list(['None','Soft','Rough','Other'])))
    # character.description['tattoo_coverage'] = str(random.choice(list(['None','Partial','Full','Other'])))
 
    character_race_clothing_styles = {
        'Dwarf': [
            "Practical and durable clothing suited for underground work.",
            "Embellished with intricate patterns and metallic accents.",
            "Warm and cozy attire, often adorned with fur or leather.",
            "Robust and earth-toned garments that reflect their craftsmanship.",
            "Traditional and functional clothing with a touch of elegance."
        ],
        'Elf': [
            "Elegant and ethereal robes inspired by nature's beauty.",
            "Light and flowing fabrics in earthy and pastel tones.",
            "Delicate and finely woven attire adorned with elven symbols.",
            "Elaborate and regal clothing fit for elven nobility.",
            "Glamorous and enchanting ensembles that capture starlight."
        ],
        'Halfling': [
            "Comfortable and colorful clothing perfect for festivities.",
            "Practical and well-fitting attire suitable for adventures.",
            "Bright and cheerful outfits reflecting their optimistic nature.",
            "Casual wear designed for relaxation and enjoyment.",
            "Dapper and stylish garments for social gatherings."
        ],
        'Human': [
            "Diverse clothing styles influenced by regional cultures.",
            "Adaptable attire for various roles in society.",
            "Fashionable and trendy outfits following the latest trends.",
            "Mix of traditional and modern clothing reflecting heritage.",
            "Sophisticated business attire for professionals."
        ],
        'Dragonborn': [
            "Armor-like clothing reminiscent of their dragon ancestors.",
            "Intricately designed outfits with draconic motifs.",
            "Sleek and metallic fabrics that reflect their power.",
            "Bold and fierce ensembles symbolizing their heritage.",
            "Unique attire adorned with scales and fiery patterns."
        ],
        'Gnome': [
            "Quirky and inventive clothing with functional gadgets.",
            "Bright and whimsical outfits that showcase their creativity.",
            "Playful attire inspired by their love for tinkering.",
            "Robes adorned with gears and mechanical-themed accessories.",
            "Colorful and eccentric garments for a lively appearance."
        ],
        'Half-Elf': [
            "A blend of human and elven styles for a graceful look.",
            "Versatile and adaptable clothing for their diverse heritage.",
            "Elegant robes with subtle elven motifs and embroidery.",
            "Modern attire with a touch of elven charm.",
            "Sleek and stylish outfits reflecting their charisma."
        ],
        'Half-Orc': [
            "Practical and durable clothing suited for rough environments.",
            "Tribal attire adorned with orcish symbols and patterns.",
            "Functional and battle-ready outfits for survival.",
            "Rugged and weathered garments showcasing their strength.",
            "Simple and utilitarian clothing with an orcish touch."
        ],
        'Tiefling': [
            "Fiery and dramatic clothing reflecting their infernal heritage.",
            "Dark and mysterious ensembles with infernal symbols.",
            "Extravagant outfits with intricate designs and accents.",
            "Elegant attire that exudes an aura of darkness and allure.",
            "Bold and seductive clothing that commands attention."
        ]
    }

    if method == 'Automated' or method == 'Guided':
        character.description['clothing_style'] = random.choice(character_race_clothing_styles[character_race])
    elif method == 'Manual':
        character.description['clothing_style'] = terminalmenu_quick_select(character_race_clothing_styles[character_race], f'[{character_race}] Select a clothing style:')

    # character.description['clothing_color'] = str(random.choice(list(['White','Black','Brown','Red','Yellow','Green','Blue','Purple','Orange','Pink','Gray','Other'])))
    # character.description['clothing_pattern'] = str(random.choice(list(['None','Strip','Triangle','Square','Other'])))
    # character.description['clothing_material'] = str(random.choice(list(['None','Cotton','Leather','Silk','Other'])))
    # character.description['clothing_fit'] = str(random.choice(list(['None','Loose','Tight','Other'])))
    # character.description['clothing_length'] = str(random.choice(list(['None','Short','Medium','Long','Other'])))
    # character.description['clothing_coverage'] = str(random.choice(list(['None','Partial','Full','Other'])))
    
    character_race_accessories = {
        'Dwarf': [
            "None - Dwarves often value simplicity and functionality in their attire.",
            "Dwarven Helm - A sturdy helmet adorned with intricate engravings.",
            "Beard Rings - Decorative rings woven into their magnificent beards.",
            "Bracelet of Stone - A bracelet made from polished gemstones.",
            "Belt Buckle - Elaborate belt buckles with Dwarven craftsmanship.",
            "Necklace of Clan - A necklace displaying the emblem of their clan.",
            "Copper Earrings - Earrings shaped like miniature pickaxes or hammers.",
            "Pocket Watch - An ornate pocket watch passed down through generations.",
            "Other - Dwarves may wear unique accessories that reflect their individuality.",
        ],
        'Elf': [
            "None - Elves often embrace a natural and unadorned look.",
            "Elven Circlet - A delicate circlet adorned with leaves and gems.",
            "Ear Cuffs - Decorative ear cuffs that highlight their pointed ears.",
            "Necklace of the Forest - A necklace featuring a miniature forest scene.",
            "Bracelet of Leaves - Bracelets made from intricately woven leaves.",
            "Crystal Pendant - A pendant with a sparkling crystal as its centerpiece.",
            "Moonstone Earrings - Earrings crafted from shimmering moonstones.",
            "Hairpin - Ornate hairpins that hold back their flowing locks.",
            "Other - Elves may have exotic accessories that reflect their connection to nature.",
        ],
        'Halfling': [
            "None - Halflings often prefer a simple and unassuming style.",
            "Hat with Feather - A hat adorned with a colorful feather for flair.",
            "Suspenders - Stylish suspenders that add charm to their outfits.",
            "Lucky Charm Bracelet - A bracelet with an assortment of lucky charms.",
            "Rings of Laughter - Rings engraved with jokes and humorous phrases.",
            "Earrings of Mischief - Earrings shaped like playful symbols.",
            "Necklace of Hearth - A necklace featuring a tiny hearth as a pendant.",
            "Beaded Anklet - Anklets made from colorful beads and trinkets.",
            "Other - Halflings may wear accessories that reflect their jovial nature.",
        ],
        'Human': [
            "None - Humans have diverse styles, and many prefer a clean and unadorned look.",
            "Stylish Hat - A fashionable hat that complements their attire.",
            "Sunglasses - Sleek sunglasses that add a touch of mystery.",
            "Elegant Earrings - Earrings that match their formal or casual outfits.",
            "Statement Necklace - A bold necklace that draws attention.",
            "Bracelet Stack - Multiple bracelets that create a trendy layered look.",
            "Signet Ring - A ring with a family crest or personal emblem.",
            "Classic Watch - A timeless wristwatch that's both functional and stylish.",
            "Other - Humans may wear a wide range of accessories based on their individual tastes.",
        ],
        'Dragonborn': [
            "None - Dragonborn often prioritize their scales as their most distinctive feature.",
            "Scale Amulet - An amulet crafted from a piece of their own scales.",
            "Flame-Embossed Gauntlets - Gauntlets with intricate flame designs.",
            "Dragon Claw Necklace - A necklace featuring a dragon claw pendant.",
            "Serpentine Bracelet - Bracelets made to resemble twisting serpent scales.",
            "Scale-Ring Belt - A belt adorned with miniature dragon scales as decorations.",
            "Dragon Eye Earrings - Earrings shaped like the mesmerizing eyes of a dragon.",
            "Fire-Breather's Medallion - A medallion representing their fire-breathing heritage.",
            "Other - Dragonborn may have accessories that pay homage to their draconic lineage.",
        ],
        'Gnome': [
            "None - Gnomes often prioritize practicality over extravagant accessories.",
            "Inventor's Goggles - Goggles with various lenses and gadgets attached.",
            "Mechanical Bracelet - A bracelet with small moving gears and cogs.",
            "Gnomey Scarf - A scarf with vibrant colors and eccentric patterns.",
            "Steampunk Earrings - Earrings inspired by steampunk machinery.",
            "Pocket Watch - A pocket watch with multiple dials and functions.",
            "Ring of Invention - Rings with compartments for tiny tools and gadgets.",
            "Magical Amulet - An amulet that occasionally emits magical sparks.",
            "Other - Gnomes may wear accessories that reflect their love for tinkering and innovation.",
        ],
        'Half-Elf': [
            "None - Half-Elves often blend their human and elven styles harmoniously.",
            "Elven Brooch - A brooch with intricate elven designs.",
            "Subtle Earrings - Earrings that complement their elegant appearance.",
            "Harmonious Necklace - A necklace symbolizing their mixed heritage.",
            "Dual-Tone Bracelet - Bracelets that combine human and elven elements.",
            "Charm Bracelet - A bracelet adorned with charms from both worlds.",
            "Half-Elven Ring - A ring that bridges the gap between two cultures.",
            "Earcuff - Earcuffs that enhance the beauty of their elven ears.",
            "Other - Half-Elves may wear accessories that celebrate their unique heritage.",
        ],
        'Half-Orc': [
            "None - Half-Orcs often favor simplicity and practicality in their attire.",
            "Tribal Necklace - A necklace with tribal symbols and totems.",
            "Battle-Scarred Gauntlets - Gauntlets that bear the marks of numerous battles.",
            "Ear Tusk Earrings - Earrings fashioned from orcish tusks.",
            "Orcish Bone Bracelet - Bracelets made from carved orcish bones.",
            "Rugged Belt Buckle - Belt buckles that represent their strength and resilience.",
            "Tribal Rings - Rings with tribal patterns and orcish motifs.",
            "Tattoo Choker - A choker adorned with tribal tattoo designs.",
            "Other - Half-Orcs may wear accessories that honor their orcish heritage and life experiences.",
        ],
        'Tiefling': [
            "None - Tieflings often let their infernal features take center stage.",
            "Infernal Horned Headpiece - A headpiece adorned with decorative horns.",
            "Fiery Eyepatch - An eyepatch with an enchanting fiery motif.",
            "Demon Tail Belt - A belt with a tail-like extension that wraps around the waist.",
            "Infernal Cuff - Cuffs with intricate infernal markings and patterns.",
            "Infernal Claw Ring - Rings shaped like fiendish claws with dark gemstones.",
            "Tiefling Tail Ring - Rings designed to resemble their unique tails.",
            "Sulfurous Earrings - Earrings that emit a faint sulfuric aroma.",
            "Other - Tieflings may have accessories that embrace their infernal nature with flair.",
        ]
    }

    if method == 'Automated' or method == 'Guided':
        character.description['accessories'] = random.choice(character_race_accessories[character_race])
    elif method == 'Manual':
        character.description['accessories'] = terminalmenu_quick_select(character_race_accessories[character_race], f'[{character_race}] Select an accessory:')

    # character.description['head_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    # character.description['neck_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    # character.description['arm_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    # character.description['hand_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    # character.description['finger_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    # character.description['leg_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    # character.description['foot_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    # character.description['body_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    # character.description['back_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    # character.description['waist_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    # character.description['shoulder_gear'] = str(random.choice(list(['None','Metal Armor','Leather Pad','Cloth','Bare','Other'])))
    
    character_race_voices = {
        'Dwarf': [
            "Deep - Dwarves often have deep, resonant voices that echo in stone tunnels.",
            "Gruff - A rough and sturdy voice is common among Dwarves.",
            "Commanding - Dwarves often command attention with their authoritative voices.",
            "Rich - Dwarves' voices are rich and melodic, like the sound of a hearty laugh.",
            "Melodic - Dwarves' melodic voices are reminiscent of their mining songs.",
            "Rumbling - Some Dwarves have voices that rumble like distant thunder.",
        ],
        'Elf': [
            "Melodic - Elves have melodic voices, resembling the gentle flow of a woodland stream.",
            "Ethereal - Elven voices sound almost otherworldly, as if touched by magic.",
            "Graceful - Elves speak with grace and elegance, their words like a dance.",
            "Enchanting - Elven voices can enchant and captivate those who listen.",
            "Whispering - Elves often speak in soft, soothing tones, like a breeze through leaves.",
            "Mystical - Some Elves have voices that carry an air of ancient mysticism.",
        ],
        'Halfling': [
            "Cheerful - Halflings have cheerful and friendly voices that warm the heart.",
            "Light - Halfling voices are light and pleasant, like a soothing breeze.",
            "Welcoming - Halflings often sound welcoming and inviting to strangers.",
            "Joyful - Halflings' voices are filled with joy and laughter.",
            "Gentle - Halfling voices are gentle and soothing, like a lullaby.",
            "Merry - Some Halflings have voices that convey a perpetual sense of merriment.",
        ],
        'Human': [
            "Versatile - Humans have a wide range of voices, adapting to their surroundings.",
            "Clear - Human voices are often clear and easily understood by others.",
            "Expressive - Humans use their voices to express a diverse range of emotions.",
            "Adaptable - Human voices can change tone and style to fit different situations.",
            "Resonant - Human voices can be resonant and authoritative, commanding attention.",
            "Magnetic - Some humans have voices that draw people in, making them memorable.",
        ],
        'Dragonborn': [
            "Thunderous - Dragonborn voices can be thunderous and imposing.",
            "Resonant - Dragonborn voices resonate with power and authority.",
            "Serpentine - Some Dragonborn have a hissing quality to their voices.",
            "Majestic - Dragonborn voices are majestic, like the roar of a dragon.",
            "Haunting - Dragonborn voices can be haunting and unforgettable.",
            "Regal - Some Dragonborn have voices that exude a regal and noble demeanor.",
        ],
        'Gnome': [
            "Curious - Gnomes often have curious and inquisitive voices.",
            "Whimsical - Gnomes' voices can sound whimsical and filled with wonder.",
            "Playful - Gnomes speak in a playful and light-hearted manner.",
            "Inventive - Gnomes' voices reflect their inventive and creative nature.",
            "Lively - Gnomes' voices are lively and filled with energy, like a perpetual giggle.",
            "Eccentric - Some Gnomes have voices that are delightfully eccentric and quirky.",
        ],
        'Half-Elf': [
            "Harmonious - Half-Elves often have harmonious voices that blend two worlds.",
            "Elegant - Half-Elven voices are elegant and pleasing to the ear.",
            "Diplomatic - Half-Elves have diplomatic voices, soothing conflicts with words.",
            "Captivating - Half-Elves' voices can captivate and hold the listener's attention.",
            "Harmonizing - Half-Elves' voices harmonize effortlessly with music and nature.",
            "Soulful - Some Half-Elves have voices that convey deep emotions and empathy.",
        ],
        'Half-Orc': [
            "Strong - Half-Orcs have strong and resonant voices that command respect.",
            "Gritty - Half-Orc voices have a gritty quality, reflecting their toughness.",
            "Commanding - Half-Orcs speak with authority and determination.",
            "Intense - Half-Orc voices can convey intensity and focus.",
            "Thunderous - Half-Orc voices can be thunderous and intimidating.",
            "Unyielding - Some Half-Orcs have voices that exude unwavering resolve.",
        ],
        'Tiefling': [
            "Sultry - Tiefling voices can be sultry and seductive, hinting at infernal charm.",
            "Haunting - Tiefling voices have a haunting quality, leaving a lasting impression.",
            "Enigmatic - Tieflings often speak in enigmatic tones, revealing little but hinting at much.",
            "Commanding - Tieflings have commanding voices, demanding attention and respect.",
            "Eerie - Tiefling voices can be eerie and unsettling, like a whispered secret.",
            "Alluring - Some Tieflings have voices that draw others in, like a beguiling spell.",
        ]
    }

    if method == 'Automated' or method == 'Guided':
        character.description['voice'] = random.choice(character_race_voices[character_race])
    elif method == 'Manual':
        character.description['voice'] = terminalmenu_quick_select(character_race_voices[character_race], f'[{character_race}] Select a voice:')


    character_race_mannerisms = {
        'Dwarf': [
            "None - Dwarves often maintain a stoic and unflappable demeanor.",
            "Gruff - Dwarves may have a gruff and blunt manner of speaking.",
            "Resolute - Dwarves exhibit unwavering determination and resolve.",
            "Stoic - Dwarves tend to remain composed and unemotional in challenging situations.",
            "Cautious - Dwarves are known for their careful and methodical approach to problems.",
            "Proud - Some Dwarves express pride in their heritage and achievements.",
            "Loyal - Dwarves often show steadfast loyalty to their companions and clans.",
            "Determined - Dwarves have a reputation for their strong sense of purpose and commitment.",
            "Gregarious - Some Dwarves are surprisingly outgoing and enjoy socializing.",
            "Honest - Dwarves value honesty and straightforwardness in their interactions.",
        ],
        'Elf': [
            "None - Elves often exhibit serene and composed mannerisms.",
            "Graceful - Elves move with a graceful and fluid elegance.",
            "Ethereal - Some Elves give off an otherworldly and ethereal aura in their actions.",
            "Enigmatic - Elves can appear mysterious and enigmatic to outsiders.",
            "Gentle - Elves handle delicate objects or creatures with exceptional care.",
            "Nurturing - Some elves exhibit a nurturing and protective nature towards others.",
            "Reflective - Elves frequently pause to reflect on their surroundings and experiences.",
            "Distant - Elves may appear distant, lost in introspective thought.",
            "Playful - Elves often engage in playful and lighthearted gestures.",
            "Mysterious - Some Elves maintain an air of mystery and intrigue.",
        ],
        'Halfling': [
            "None - Halflings are known for their carefree and easygoing demeanor.",
            "Bubbly - Halflings frequently display cheerful and bubbly mannerisms.",
            "Playful - Halflings engage in playful antics and light-hearted gestures.",
            "Friendly - Halflings are naturally sociable and exude friendliness.",
            "Adventurous - Halflings express a sense of wanderlust and curiosity.",
            "Curious - Halflings have a knack for exploring and inquisitiveness.",
            "Helpful - Halflings are eager to lend a helping hand to others in need.",
            "Jovial - Halflings frequently share jokes and laughter with companions.",
            "Careful - Some Halflings exhibit a cautious and safety-conscious nature.",
            "Optimistic - Halflings maintain a positive outlook on life and its challenges.",
        ],
        'Human': [
            "None - Humans display a wide range of mannerisms, making it hard to pinpoint common traits.",
            "Adaptable - Humans are known for their ability to adapt their mannerisms to various situations.",
            "Expressive - Humans often convey their emotions through expressive gestures and expressions.",
            "Diverse - Humans' mannerisms can vary greatly depending on their cultural background.",
            "Confident - Some humans carry themselves with a confident and self-assured demeanor.",
            "Inquisitive - Humans frequently ask questions and seek knowledge.",
            "Humble - Some humans maintain humility and modesty in their interactions.",
            "Empathetic - Humans often show empathy and understanding towards others.",
            "Resilient - Humans exhibit a resilient and enduring nature in the face of adversity.",
            "Diplomatic - Some humans excel in diplomacy and conflict resolution.",
        ],
        'Dragonborn': [
            "None - Dragonborn often have minimal overt mannerisms.",
            "Commanding - Dragonborn may have a commanding presence and demeanor.",
            "Regal - Dragonborn exhibit regal and dignified mannerisms.",
            "Draconic - Some Dragonborn subtly incorporate reptilian traits into their actions.",
            "Noble - Some dragonborn carry themselves with a noble and aristocratic air.",
            "Proud - Dragonborn often express pride in their draconic heritage and lineage.",
            "Honorable - Many dragonborn adhere to a strong code of honor and ethics.",
            "Fierce - Dragonborn warriors may exhibit fierce and determined demeanor in battle.",
            "Respectful - Dragonborn show respect and courtesy in their interactions.",
            "Majestic - Dragonborn may move with a majestic and awe-inspiring grace.",
        ],
        'Gnome': [
            "None - Gnomes can be whimsical and unpredictable, often defying traditional mannerisms.",
            "Curious - Gnomes frequently display curiosity through inquisitive gestures and expressions.",
            "Eccentric - Gnomes enthusiastically embrace eccentric and quirky mannerisms.",
            "Inventive - Gnomes sometimes incorporate tinkering or gadget-related gestures.",
            "Animated - Gnomes are animated and lively in their interactions and movements.",
            "Mischievous - Some gnomes enjoy playful pranks and tricks on others.",
            "Adventurous - Gnomes express a desire for adventure and discovery.",
            "Enthusiastic - Gnomes often show enthusiasm for their hobbies and interests.",
            "Whimsical - Gnomes maintain a whimsical and imaginative outlook on life.",
            "Inventive - Gnomes might incorporate inventive and mechanical gestures.",
        ],
        'Half-Elf': [
            "None - Half-Elves exhibit a wide range of mannerisms, influenced by both human and elven heritage.",
            "Graceful - Half-Elves frequently display graceful and harmonious gestures.",
            "Charming - Half-Elves use charm and charisma to great effect in their interactions.",
            "Adaptable - Half-Elves can adapt their mannerisms to fit various social situations.",
            "Empathetic - Half-Elves are empathetic and attuned to others' emotions and needs.",
            "Diplomatic - Some half-elves excel in diplomacy and conflict resolution.",
            "Sociable - Half-Elves are naturally sociable and enjoy social gatherings.",
            "Mysterious - Half-Elves may maintain an air of mystery and intrigue.",
            "Confident - Half-Elves often carry themselves with confidence and self-assuredness.",
            "Elegant - Half-Elves exhibit elegant and refined manners in formal settings.",
        ],
        'Half-Orc': [
            "None - Half-Orcs often have straightforward and practical mannerisms.",
            "Fierce - Half-Orcs may display fierce and determined demeanor in their actions.",
            "Resilient - Half-Orcs often convey resilience and unyielding nature.",
            "Tribal - Half-Orcs might incorporate tribal or orcish traits into their mannerisms.",
            "Stern - Some half-orcs have a stern and no-nonsense approach.",
            "Loyal - Half-Orcs often express unwavering loyalty to their companions.",
            "Tenacious - Half-Orcs may exhibit tenacity and persistence in their endeavors.",
            "Vigilant - Half-Orcs tend to be vigilant and alert in their surroundings.",
            "Gentle - In rare cases, Half-Orcs may display a gentle and nurturing demeanor.",
            "Mysterious - Some Half-Orcs maintain an air of mystery and intrigue about them.",
        ],
        'Tiefling': [
            "None - Tieflings often have a wide range of mannerisms, influenced by their infernal heritage.",
            "Seductive - Tieflings may exhibit seductive and alluring gestures and expressions.",
            "Enigmatic - Tieflings often have an enigmatic and mysterious demeanor.",
            "Infernal - Tieflings might incorporate subtle infernal traits into their actions.",
            "Charismatic - Many tieflings possess a natural charisma that shines through their mannerisms.",
            "Sultry - Some tieflings exude a sultry and captivating aura.",
            "Confident - Tieflings may carry themselves with confidence and self-assuredness.",
            "Magnetic - Tieflings often draw attention with their magnetic and captivating presence.",
            "Playful - Some tieflings enjoy playful and mischievous interactions with others.",
            "Fierce - Tieflings may exhibit fierce and determined demeanor when faced with challenges.",
        ]
    }

    if method == 'Automated' or method == 'Guided':
        character.description['mannerisms'] = random.choice(character_race_mannerisms[character_race])
    elif method == 'Manual':
        character.description['mannerisms'] = terminalmenu_quick_select(character_race_mannerisms[character_race], f'[{character_race}] Select mannerisms:')


    character_race_personalities = {
        'Dwarf': [
            "Resilient and steadfast - Dwarves are known for their unwavering determination.",
            "Traditional and loyal - Dwarves hold deep respect for their heritage and kin.",
            "Courageous and valiant - Dwarves are fearless in the face of danger.",
            "Practical and no-nonsense - Dwarves prefer straightforward solutions.",
            "Hospitable and jovial - Dwarves enjoy good company and hearty celebrations.",
            "Stubborn and unyielding - Dwarves can be hard to sway once their minds are made up.",
            "Honest and trustworthy - Dwarves value honesty and loyalty above all else.",
            "Proud and honorable - Dwarves take pride in their accomplishments and reputations.",
        ],
        'Elf': [
            "Graceful and ethereal - Elves move with a natural elegance and poise.",
            "Mystical and enigmatic - Elves are deeply connected to the world's magic.",
            "Adventurous and curious - Elves have an insatiable thirst for knowledge.",
            "Free-spirited and independent - Elves value their freedom and individuality.",
            "Reserved and contemplative - Elves often ponder the mysteries of existence.",
            "Tolerant and diplomatic - Elves seek harmony and understanding with others.",
            "Nurturing and protective - Elves are fiercely protective of their forests and kin.",
            "Elegant and refined - Elves appreciate art, culture, and refinement.",
        ],
        'Halfling': [
            "Friendly and affable - Halflings make friends easily and love socializing.",
            "Playful and mischievous - Halflings enjoy pranks and lighthearted humor.",
            "Adaptable and resourceful - Halflings can find solutions in tight spots.",
            "Optimistic and carefree - Halflings embrace life's joys and adventures.",
            "Caring and compassionate - Halflings help those in need without hesitation.",
            "Trustworthy and reliable - Halflings are true to their word and dependable.",
            "Courageous and fearless - Halflings face danger with a fearless spirit.",
            "Family-oriented and protective - Halflings cherish their families above all.",
        ],
        'Human': [
            "Versatile and adaptable - Humans can thrive in diverse environments.",
            "Ambitious and driven - Humans often set lofty goals for themselves.",
            "Inquisitive and open-minded - Humans are eager to explore new ideas.",
            "Empathetic and compassionate - Humans show kindness to those in need.",
            "Diverse and multicultural - Humans embrace various cultures and traditions.",
            "Brave and valiant - Humans stand up for justice and protect the vulnerable.",
            "Innovative and creative - Humans push the boundaries of knowledge and invention.",
            "Charismatic and persuasive - Humans excel in leadership and diplomacy.",
        ],
        'Dragonborn': [
            "Proud and honorable - Dragonborn value their draconic heritage and reputation.",
            "Noble and regal - Dragonborn exude a dignified and commanding presence.",
            "Fierce and determined - Dragonborn face challenges with unwavering resolve.",
            "Loyal and devoted - Dragonborn are fiercely loyal to their allies and clans.",
            "Disciplined and organized - Dragonborn maintain structured societies and traditions.",
            "Respectful of authority - Dragonborn adhere to hierarchy and leadership.",
            "Resilient and unyielding - Dragonborn persevere through adversity.",
            "Honest and direct - Dragonborn value straightforward communication.",
        ],
        'Gnome': [
            "Curious and inventive - Gnomes have a natural aptitude for tinkering and innovation.",
            "Playful and whimsical - Gnomes bring joy and humor to everyday life.",
            "Eccentric and quirky - Gnomes embrace their unique quirks and interests.",
            "Supportive and nurturing - Gnomes provide encouragement to those they care about.",
            "Optimistic and hopeful - Gnomes believe in the potential for positive change.",
            "Resourceful and adaptable - Gnomes find creative solutions to problems.",
            "Empathetic and understanding - Gnomes listen and offer comfort to others.",
            "Friendly and welcoming - Gnomes love making new friends and connections.",
        ],
        'Half-Elf': [
            "Adaptable and flexible - Half-Elves blend the best qualities of humans and elves.",
            "Diplomatic and peace-loving - Half-Elves seek harmony and cooperation.",
            "Charming and charismatic - Half-Elves have a magnetic presence and charm.",
            "Talented and versatile - Half-Elves excel in a wide range of skills and abilities.",
            "Compassionate and empathetic - Half-Elves understand and connect with others.",
            "Inquisitive and open-minded - Half-Elves eagerly explore different perspectives.",
            "Free-spirited and independent - Half-Elves value personal freedom and expression.",
            "Nurturing and protective - Half-Elves show unwavering support for their loved ones.",
        ],
        'Half-Orc': [
            "Strong and resilient - Half-Orcs endure hardships with determination.",
            "Brave and fearless - Half-Orcs face danger head-on without hesitation.",
            "Honorable and loyal - Half-Orcs uphold their commitments and values.",
            "Pragmatic and resourceful - Half-Orcs find practical solutions to challenges.",
            "Independent and self-reliant - Half-Orcs value personal strength and autonomy.",
            "Fierce and passionate - Half-Orcs express their emotions openly and boldly.",
            "Humble and down-to-earth - Half-Orcs don't seek glory or recognition.",
            "Protective and caring - Half-Orcs fiercely defend their loved ones and communities.",
        ],
        'Tiefling': [
            "Mysterious and enigmatic - Tieflings often possess an air of intrigue.",
            "Charismatic and alluring - Tieflings have a natural magnetism and charm.",
            "Ambitious and driven - Tieflings set ambitious goals for themselves.",
            "Independent and self-reliant - Tieflings value their individuality and freedom.",
            "Resilient and adaptable - Tieflings endure challenges and emerge stronger.",
            "Passionate and intense - Tieflings express their emotions with intensity.",
            "Sly and cunning - Tieflings are quick-witted and clever in their pursuits.",
            "Empathetic and compassionate - Tieflings help those in need and show kindness.",
        ]
    }

    if method == 'Automated' or method == 'Guided':
        character.description['personality'] = random.choice(character_race_personalities[character_race])
    elif method == 'Manual':
        character.description['personality'] = terminalmenu_quick_select(character_race_personalities[character_race], f'[{character_race}] Select a personality trait:')


    # Background
    character.background = {}
    if method == 'Automated':
        character_automated_background_selected = terminalmenu_quick_select(["Use random pre-built template","Create random background from others"], f'[{character_race}] Select a background:')
        if character_automated_background_selected == "Use random pre-built template":
            character.background['name'] = random.choice(list(dnd_backgrounds.keys()))
            character.background = dnd_backgrounds[character.background['name']]    
        elif character_automated_background_selected == "Create random background from others":
            randomly_generated_background = generate_random_background(dnd_backgrounds)
            character.background['name'] = randomly_generated_background["Name"]
            character.background = randomly_generated_background
    elif method == 'Guided':
        character.background['name'] = terminalmenu_quick_select(sorted(list(dnd_backgrounds.keys())), f'[{character_race}] Select a background:')
        character.background = dnd_backgrounds[character.background['name']]
    elif method == 'Manual':
        character.background = {}
        character.background['Name']                = terminalmenu_quick_select(sorted(list(set(dnd_backgrounds.keys()))), f'[{character_race}] Select a background name:')
        character.background['Source']              = "Manually Selected"
        character.background['Details']             = terminalmenu_quick_select(sorted(list(set([dnd_backgrounds[background]["Details"]  for background in dnd_backgrounds]))), f'[{character_race}] Select background details:')
        character.background['Features']            = terminalmenu_quick_select(sorted(list(set([dnd_backgrounds[background]["Features"] for background in dnd_backgrounds]))), f'[{character_race}] Select background features:')
        character.background['Skill Proficiencies'] = terminalmenu_quick_select(sorted(list(set([', '.join(dnd_backgrounds[background]["Skill Proficiencies"]).lower() for background in dnd_backgrounds]))), f'[{character_race}] Select background skill proficiencies:')
        character.background['Tool Proficiencies']  = terminalmenu_quick_select(sorted(list(set([', '.join(dnd_backgrounds[background]["Tool Proficiencies"])  for background in dnd_backgrounds]))), f'[{character_race}] Select background tool proficiencies:')
        character.background['Languages']           = terminalmenu_quick_select(sorted(list(set([', '.join(dnd_backgrounds[background]["Languages"]) for background in dnd_backgrounds]))), f'[{character_race}] Select background languages:')
        character.background['Equipment']           = terminalmenu_quick_select(sorted(list(set([dnd_backgrounds[background]["Equipment"] for background in dnd_backgrounds]))), f'[{character_race}] Select background equipment:')
        character.background['Roleplaying Suggestions'] = {}

        character_background_persontality_trait_list = []
        for background in dnd_backgrounds:
            character_background_persontality_trait_list.append(dnd_backgrounds[background]["Roleplaying Suggestions"]["Personality Trait"])
        character_background_persontality_trait_list = list(set(character_background_persontality_trait_list))
        character.background['Roleplaying Suggestions']["Personality Trait"] = terminalmenu_quick_select(sorted(list(character_background_persontality_trait_list)), f'[{character_race}] Select a background suggested roleplaying ideal:')
        
        character_background_ideal_list = []
        for background in dnd_backgrounds:
            character_background_ideal_list.append(dnd_backgrounds[background]["Roleplaying Suggestions"]["Ideal"])
        character_background_ideal_list = list(set(character_background_ideal_list))
        character.background['Roleplaying Suggestions']["Ideal"] = terminalmenu_quick_select(sorted(list(character_background_ideal_list)), f'[{character_race}] Select a background suggested roleplaying ideal:')
        
        character_background_bond_list = []
        for background in dnd_backgrounds:
            character_background_bond_list.append(dnd_backgrounds[background]["Roleplaying Suggestions"]["Bond"])
        character_background_bond_list = list(set(character_background_bond_list))
        character.background['Roleplaying Suggestions']["Bond"]  = terminalmenu_quick_select(sorted(list(character_background_bond_list)), f'[{character_race}] Select a background suggested roleplaying ideal:')
        
        character_background_flaw_list = []
        for background in dnd_backgrounds:
            character_background_flaw_list.append(dnd_backgrounds[background]["Roleplaying Suggestions"]["Flaw"])
        character_background_flaw_list = list(set(character_background_flaw_list))
        character.background['Roleplaying Suggestions']["Flaw"]  = terminalmenu_quick_select(sorted(list(character_background_flaw_list)), f'[{character_race}] Select a background suggested roleplaying ideal:')
            
        




    # Level Chart
    character.level_chart = dnd_classes[character_class]["Level Chart"]

    # character.profile['all_armor_proficiencies'] = []
    # character.profile['all_weapon_proficiencies'] = []
    # character.profile['all_tools_proficiencies'] = []
    # character.profile['all_languages'] = list(character.character_race['Proficiencies']['languages']) + list(character.character_class['Proficiencies']['Languages'])


    # Spellcasting
    if character_class == "Barbarian":
        # Not a native spell caster
        character.spells['Cantrips Known'] = "None"
        character.spells['Spells Known'] = "None"


    elif character_class == "Fighter":
        # Not a native spell caster
        character.spells['Cantrips Known'] = "None"
        character.spells['Spells Known'] = "None"


    elif character_class == "Monk":
        # Not a native spell caster
        character.spells['Cantrips Known'] = "None"
        character.spells['Spells Known'] = "None"


    elif character_class == "Rogue":
        # Not a native spell caster
        character.spells['Cantrips Known'] = "None"
        character.spells['Spells Known'] = "None"   


    elif character_class == "Bard":
        spell_levels = ['Cantrips','1st','2nd','3rd','4th','5th','6th','7th','8th','9th']

        character.spells['Cantrips Known'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']
        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Spells Known']
        character.spells['Spells Known']["Slots"] = {}

        for spell_level in spell_levels:
            if spell_level == 'Cantrips':
                
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : f"Can cast {character.spells['Cantrips Known']} known Cantrips unlimiited times",
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)
                
                chosen_temp_list = []
                for each in range(1,character.spells['Cantrips Known'] + 1):
                    choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)

            else:
                if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                    character.spells['Spells Known']["Slots"][spell_level] = {
                        "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                        "Known Spells" : {}
                    }
                    for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                        character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                    chosen_temp_list = []
                    for each in range(1,int(dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level]) + 1):
                        choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


    elif character_class == "Cleric":
        spell_levels = ['Cantrips','1st','2nd','3rd','4th','5th','6th','7th','8th','9th']

        character.spells['Cantrips Known'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']
        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = "Clerics have access to all their spells, but can change them daily with preparation"
        character.spells['Spells Known']["Slots"] = {}

        for spell_level in spell_levels:
            if spell_level == 'Cantrips':
                
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : f"Can cast {character.spells['Cantrips Known']} known Cantrips unlimiited times",
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)
                
                chosen_temp_list = []
                for each in range(1,character.spells['Cantrips Known'] + 1):
                    choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)

            else:
                if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                    character.spells['Spells Known']["Slots"][spell_level] = {
                        "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                        "Known Spells" : {}
                    }
                    for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                        character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                    chosen_temp_list = []
                    for each in range(1,int(dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level]) + 1):
                        choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


    elif character_class == "Druid":
        spell_levels = ['Cantrips','1st','2nd','3rd','4th','5th','6th','7th','8th','9th']

        character.spells['Cantrips Known'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']
        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = "Clerics have access to all their spells, but can change them daily with preparationXXXXXXXXXXXXXXXXXXXXXXXXXX"
        character.spells['Spells Known']["Slots"] = {}

        for spell_level in spell_levels:
            if spell_level == 'Cantrips':
                
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : f"Can cast {character.spells['Cantrips Known']} known Cantrips unlimiited times",
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)
                
                chosen_temp_list = []
                for each in range(1,character.spells['Cantrips Known'] + 1):
                    choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


            else:
                if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                    character.spells['Spells Known']["Slots"][spell_level] = {
                        "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                        "Known Spells" : {}
                    }
                    for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                        character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                    chosen_temp_list = []
                    for each in range(1,int(dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level]) + 1):
                        choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


    elif character_class == "Sorcerer":
        spell_levels = ['Cantrips','1st','2nd','3rd','4th','5th','6th','7th','8th','9th']

        character.spells['Cantrips Known'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']
        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Spells Known']
        character.spells['Spells Known']["Slots"] = {}

        for spell_level in spell_levels:
            if spell_level == 'Cantrips':
                
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : f"Can cast {character.spells['Cantrips Known']} known Cantrips unlimiited times",
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)
                
                chosen_temp_list = []
                for each in range(1,character.spells['Cantrips Known'] + 1):
                    choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


            else:
                if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                    character.spells['Spells Known']["Slots"][spell_level] = {
                        "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                        "Known Spells" : {}
                    }
                    for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                        character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                    chosen_temp_list = []
                    for each in range(1,int(dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level]) + 1):
                        choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


    elif character_class == "Wizard":
        spell_levels = ['Cantrips','1st','2nd','3rd','4th','5th','6th','7th','8th','9th']

        character.spells['Cantrips Known'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']
        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = "Clerics have access to all their spells, but can change them daily with preparationXXXXXXXXXXXXXXXXXXXXXXXXXX"
        character.spells['Spells Known']["Slots"] = {}

        for spell_level in spell_levels:
            if spell_level == 'Cantrips':
                
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : f"Can cast {character.spells['Cantrips Known']} known Cantrips unlimiited times",
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)
                
                chosen_temp_list = []
                for each in range(1,character.spells['Cantrips Known'] + 1):
                    choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)

            else:
                if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                    character.spells['Spells Known']["Slots"][spell_level] = {
                        "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                        "Known Spells" : {}
                    }
                    for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                        character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                    chosen_temp_list = []
                    for each in range(1,int(dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level]) + 1):
                        choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


    elif character_class == "Paladin":
        spell_levels = ['1st','2nd','3rd','4th','5th']

        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = "Clerics have access to all their spells, but can change them daily with preparationXXXXXXXXXXXXXXXXXXXXXXXXXX"
        character.spells['Spells Known']["Slots"] = {}

        character.spells['Cantrips Known'] = "None"
        character.spells['Spells Known']["Slots"]["Cantrips"] = {
            "Able To Cast" : "None",
            "Known Spells" : "None"
        }

        for spell_level in spell_levels:
            if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                chosen_temp_list = []
                for each in range(1,int(dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level]) + 1):
                    choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


    elif character_class == "Ranger":
        spell_levels = ['1st','2nd','3rd','4th','5th']

        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = "Clerics have access to all their spells, but can change them daily with preparationXXXXXXXXXXXXXXXXXXXXXXXXXX"
        character.spells['Spells Known']["Slots"] = {}

        character.spells['Cantrips Known'] = "None"
        character.spells['Spells Known']["Slots"]["Cantrips"] = {
            "Able To Cast" : "None",
            "Known Spells" : "None"
        }

        for spell_level in spell_levels:
            if dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level] != '-': 
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level],
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                chosen_temp_list = []
                for each in range(1,int(dnd_classes[character_class]['Level Chart'][character.profile['level']][spell_level]) + 1):
                    choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)


    elif character_class == "Warlock":
        # Warlock's primary ranged spell is Eldritch Blast, which they get for free at level 1
        character.spells["Selected Spells"].append('Eldritch Blast')
        character.spells['Cantrips Known'] = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Cantrips Known']
        character.spells['Spells Known'] = {}
        character.spells['Spells Known']['Total'] = "Clerics have access to all their spells, but can change them daily with preparationXXXXXXXXXXXXXXXXXXXXXXXXXX"
        character.spells['Spells Known']["Slots"] = {}

        spell_level = 'Cantrips'
        character.spells['Spells Known']["Slots"][spell_level] = {
            "Able To Cast" : f"Can cast {character.spells['Cantrips Known']} known Cantrips unlimiited times",
            "Known Spells" : {}
        }
        for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
            character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)
        
        chosen_temp_list = ['Eldritch Blast']
        for each in range(1,character.spells['Cantrips Known'] + 1):
            choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)

        #This is how many spells a warlock knows at at each level of any given spell level
        # Coincidently, the number of 1st level spells you can ever now is also your total number of known spells...
        # level : [5th, 4th, 3rd, 2nd, 1st]
        # warlock_known_vs_slot_level = {
        #     20 : [12, 14, 15, 15, 15],
        #     19 : [11, 13, 15, 15, 15],
        #     18 : [10, 12, 14, 15, 14],
        #     17 : [ 9, 11, 13, 15, 14],
        #     16 : [ 8, 10, 12, 14, 13],
        #     15 : [ 7,  9, 11, 13, 13],
        #     14 : [ 6,  8, 10, 12, 12],
        #     13 : [ 5,  7,  9, 11, 12],
        #     12 : [ 4,  6,  8, 10, 11],
        #     11 : [ 3,  5,  7,  9, 11],
        #     10 : [ 2,  4,  6,  8, 10],
        #      9 : [ 1,  3,  5,  7, 10],
        #      8 : [ 0,  2,  4,  6,  9],
        #      7 : [ 0,  1,  3,  5,  8],
        #      6 : [ 0,  0,  2,  4,  7],
        #      5 : [ 0,  0,  1,  3,  6],
        #      4 : [ 0,  0,  0,  2,  5],
        #      3 : [ 0,  0,  0,  1,  4],
        #      2 : [ 0,  0,  0,  0,  3],
        #      1 : [ 0,  0,  0,  0,  2],
        # }
        # This dictionary is an even distribution of the spells that a Warlock is able to know per each level - not the max.
        # This is purely used to generate a relatively "balanced" character when auto creating characters.
        # level : [1st, 2nd, 3rd, 4th, 5th]
        warlock_slots_generic_distribution = {
            20 : [ 3,  3,  3,  3,  3],
            19 : [ 3,  3,  3,  3,  3],
            18 : [ 2,  3,  3,  3,  3],
            17 : [ 2,  3,  3,  3,  3],
            16 : [ 2,  2,  3,  3,  3],
            15 : [ 2,  2,  3,  3,  3],
            14 : [ 2,  2,  2,  3,  3],
            13 : [ 2,  2,  2,  3,  3],
            12 : [ 2,  2,  2,  2,  3],
            11 : [ 2,  2,  2,  2,  3],
            10 : [ 2,  2,  2,  2,  2],
             9 : [ 2,  2,  2,  3,  1],
             8 : [ 2,  2,  3,  2,  0],
             7 : [ 2,  2,  3,  1,  0],
             6 : [ 2,  3,  2,  0,  0],
             5 : [ 2,  3,  1,  0,  0],
             4 : [ 3,  2,  0,  0,  0],
             3 : [ 3,  1,  0,  0,  0],
             2 : [ 3,  0,  0,  0,  0],
             1 : [ 2,  0,  0,  0,  0],
        }
        # spells_count_to_learn = dnd_classes[character_class]['Level Chart'][character.profile['level']]['Spells Known'] #ex: returns 6 known for level 5
        for index,spell_index in enumerate(warlock_slots_generic_distribution[character.profile['level']]): #ex: returns 2,3,1,0,0 (for 5th Level)
            if index == 0:
                spell_level = "1st"
            elif index == 1:
                spell_level = "2nd"
            elif index == 2:
                spell_level = "3rd"
            elif index == 3:
                spell_level = "4th"
            elif index == 4:
                spell_level = "5th"

            if spell_index > 0:
                character.spells['Spells Known']["Slots"][spell_level] = {
                    "Able To Cast" : f"Can cast {dnd_classes[character_class]['Level Chart'][character.profile['level']]['Spell Slots']} from any of their known spells.",
                    "Known Spells" : {}
                }
                for spell in dnd_classes[character_class]['Spells']["All Class Spells"][spell_level]:
                    character.spells['Spells Known']["Slots"][spell_level]['Known Spells'][spell] = dnd_spells.get(spell_level).get(spell)

                warlock_slots_generic_distribution_limit = spell_index # ex: for level 5, [2,3,1,0,0] the first iteration [1st level spells] will have a limit of 2 spells, second iteration [2d level spells] will have 3 spells, etc
                chosen_temp_list = []
                for num in range(1,spell_index + 1):
                    if warlock_slots_generic_distribution_limit > 0:
                        warlock_slots_generic_distribution_limit -= 1                       
                        choose_random_spell(character, dnd_classes[character_class]['Spells']["All Class Spells"][spell_level], chosen_temp_list)
                  
                
        print_character(character.spells)

 
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


    for attribute in character.attributes:
        character.attributes[attribute]['base'] = new_roles[attribute]
        
        try:
            character.attributes[attribute]['race_bonus'] = dnd_races[character_race]['Ability Score Increase'][attribute]
        except:
            character.attributes[attribute]['race_bonus'] = 0

        if attribute == str(dnd_classes[character_class]['Spells']["Spellcasting Modifier"]).lower():
            character.attributes[attribute]["Spellcasting Modifier"] = True
        else:
            character.attributes[attribute]["Spellcasting Modifier"] = False
        
        character.attributes[attribute]['total'] =  character.attributes[attribute]['base'] + character.attributes[attribute]['race_bonus']
        character.attributes[attribute]['modifier'] = (character.attributes[attribute]['total'] - 10) // 2
        
        if attribute.lower() in str(dnd_classes[character_class]["Proficiencies"]["Saving Throws"]).lower():
            character.attributes[attribute]['saving_throw'] = character.attributes[attribute]['modifier'] + character.profile['proficiency bonus']
        else:
            character.attributes[attribute]['saving_throw'] = character.attributes[attribute]['modifier'] #No proficiency bons


    character.capabilities['physical'] = {}
    character.capabilities['physical']['carry capacity'] = character.attributes['strength']['total'] * 15
    character.capabilities['physical']['push pull lift'] = character.attributes['strength']['total'] * 30
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
        character.spells["Attack Modifier"] = character.attributes[str(dnd_classes[character_class]['Spells']["Spellcasting Modifier"]).lower()]['modifier'] + character.profile['proficiency bonus']

        # Spell Save DC = 8 + Your Spellcasting Ability Modifier + Your Proficiency Bonus
        character.spells["Save DC"] = 8 + character.spells["Attack Modifier"]

    # character.spells['spellcasting focus'] = 'answer' #need to calculate, need to get stat attribtes first




    # Class Features
    # character_feautres = []
    for Level in range(1,character_level + 1):
        for Feature in dnd_classes[character_class]["Level Chart"][Level]["Features"]:
            if Feature == "-":
                pass
            else:
                character.features[Feature] = dnd_classes[character_class]["Features"][Feature]


    # Skills
    character.skills = dnd_skills
    randomly_chosen_skills = choose_random_proficiency_skill(dnd_classes,character_class)
    
    # Assigns proficiency to skills based on the randomly chosen skills list
    for skill in dnd_skills:
        if character.skills[skill]['Related Attribute'] == 'strength':
            character.skills[skill]['total'] = character.attributes['strength']['modifier']
        elif character.skills[skill]['Related Attribute'] == 'dexterity':
            character.skills[skill]['total'] = character.attributes['dexterity']['modifier']
        elif character.skills[skill]['Related Attribute'] == 'constitution':
            character.skills[skill]['total'] = character.attributes['constitution']['modifier']
        elif character.skills[skill]['Related Attribute'] == 'intelligence':
            character.skills[skill]['total'] = character.attributes['intelligence']['modifier']
        elif character.skills[skill]['Related Attribute'] == 'wisdom':
            character.skills[skill]['total'] = character.attributes['wisdom']['modifier']
        elif character.skills[skill]['Related Attribute'] == 'charisma':
            character.skills[skill]['total'] = character.attributes['charisma']['modifier']

        # Randomly adds proficiency to a skill if it is in the randomly chosen proficiency skills list
        for choose_skill in randomly_chosen_skills: 
            if skill == choose_skill:
                character.skills[skill]['proficiency'] = True
                character.skills[skill]['total'] += character.profile['proficiency bonus']

        # Calculates passive perception
        if skill == 'perception':
            if character.skills[skill]['proficiency'] == True:
                character.capabilities['physical']['passive perception'] = 10 + character.skills['perception']['total'] + character.profile['proficiency bonus']
            else:
                character.capabilities['physical']['passive perception'] = 10 + character.skills['perception']['total']





    character.capabilities['combat'] = {}
    character.capabilities['combat']['initiative'] = {}
    character.capabilities['combat']['initiative']['normal'] = character.attributes['dexterity']['modifier']
    character.capabilities['combat']['initiative']['temporary'] = 0 #placeholder
    character.capabilities['combat']['initiative']['total'] = character.capabilities['combat']['initiative']['normal'] + character.capabilities['combat']['initiative']['temporary']
    character.capabilities['combat']['armor_class'] = 10 + character.attributes['dexterity']['modifier']
    character.capabilities['combat']['hit_points'] = {}
    character.capabilities['combat']['hit_points']['damage_resistence'] = 0
    character.capabilities['combat']['hit_points']['false_life'] = 0
    character.capabilities['combat']['hit_points']['temp_hit_points'] = 0


    character_hp_calc_total = 0
    # add full level 1 hit die hp
    character_hp_calc_total += int(character.character_class["Hit Die"].split('d')[1]) + int(character.attributes['constitution']['modifier'])
    for level in range(2,int(character.profile['level'] + 1)): # starts at level 2, because level 1 is added in full up above
        val = random.randint(1, int(character.character_class["Hit Die"].split('d')[1])) + int(character.attributes['constitution']['modifier'])
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


    create_chatgpt_dall_e_image = terminalmenu_quick_select(['No','Yes'], f"[{character_race}] Have ChatGTP use DALL-E to generate a character image? ")
    if create_chatgpt_dall_e_image == 'No':
        pass
    elif create_chatgpt_dall_e_image == 'Yes':
        while True:
            verify = input(f"Let's verify this request as it costs money. Type 'yes' to submit, 'no' to abort. ")
            if verify == 'yes':
                image_size = terminalmenu_quick_select(['1024x1024', '1024x1792', '1792x1024'], f'[{character_race}] Select an image size:')
                image_style = terminalmenu_quick_select(['Abstract Art','Anime', 'Cartoon', 'Impressionism', 'Oil Painting', 'Pixel Art', 'Realistic', 'Sketch ', 'Surrealism','Watercolor'], f'[{character_race}] Select an image style:')
                dall_e_model = terminalmenu_quick_select(['dall-e-2','dall-e-3'], f'[{character_race}] Select an DALLE-E modle:')
                if dall_e_model == 'dall-e-2':
                    number_of_images = terminalmenu_quick_select([1,2,3,4,5,6,7,8,9,10], f'[{character_race}] DALL-E 2 supports mulipli images:')


# from openai import OpenAI
# client = OpenAI()

# response = client.images.create_variation(
#   image=open("image_edit_original.png", "rb"),
#   n=2,
#   size="1024x1024"
# )

# image_url = response.data[0].url                



                description = description=character.description.copy()
                del description['race']
                del description['class']
                del description['gender']
                del description['age']
                del description['skin_scent']
                del description['voice']
                del description['mannerisms']
                del description['personality']

                generate_character_image(
                    description=description, 
                    character_race=character_race, 
                    character_class=character_class, 
                    character_name=character.profile['name']['full'],
                    character_gender=character.description['gender'],
                    character_age=character.description['age'],
                    background_name=character.background['Name'],
                    background_features=character.background['Features'],
                    background_equipment=character.background['Equipment'],
                    image_style=image_style, 
                    image_size=image_size,
                    dall_e_model=dall_e_model,
                    number_of_images=number_of_images,
                )
                break
            elif verify == 'no':
                break
            else:
                print(f"Invalid input. Type in exactly 'yes' or 'no' to proceed.")

    return character



# def display_character(characters):
#     # Print Character to screen
#     for index, character in enumerate(characters):
#         print(f"==================================================")
#         print(f"Character #{index + 1}")
#         print(f"==================================================")

#         print(f"Profile :")
#         print_character(character.profile)

#         print(f"Race :")
#         print_character(character.character_race)

#         print(f"Class :")
#         print_character(character.character_class)

#         print(f"Level Chart :")
#         print_character(character.level_chart)

#         print(f"Description :")
#         print_character(character.description)

#         print(f"Background :")
#         print_character(character.background)

#         print(f"Attributes :")
#         print_character(character.attributes)

#         print(f"Capabilties :")
#         print_character(character.capabilities)

#         print(f"Skills :")
#         print_character(character.skills)

#         print(f"Features :")
#         print_character(character.features)

#         print(f"Money :")
#         print_character(character.items)

#         print(f"Items :")
#         print_inventory(character.items, 'Items')

#         print(f"Armor :")
#         print_inventory(character.armor, 'Armor')

#         print(f"Weapons :")
#         print_character(character.weapons)

#         print(f"Combat :")
#         print_character(character.combat)

#         print(f"Spells :")
#         print_character(character.spells)

