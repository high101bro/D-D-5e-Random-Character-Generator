#! /usr/bin/env python3
monster_names = [
    "Aarakocra",
    "Aboleth",
    "Abominable Yeti",
    "Acolyte",
    "Adult Black Dragon",
    "Adult Blue Dracolich",
    "Adult Blue Dragon",
    "Adult Brass Dragon",
    "Adult Bronze Dragon",
    "Adult Copper Dragon",
    "Adult Gold Dragon",
    "Adult Green Dragon",
    "Adult Red Dragon",
    "Adult Silver Dragon",
    "Adult White Dragon",
    "Air Elemental",
    "Allosaurus",
    "Ancient Black Dragon",
    "Ancient Blue Dragon",
    "Ancient Brass Dragon",
    "Ancient Bronze Dragon",
    "Ancient Copper Dragon",
    "Ancient Gold Dragon",
    "Ancient Green Dragon",
    "Ancient Red Dragon",
    "Ancient Silver Dragon",
    "Ancient White Dragon",
    "Androsphinx",
    "Animated Armor",
    "Ankheg",
    "Ankylosaurus",
    "Ape",
    "Arcanaloth",
    "Archmage",
    "Assassin",
    "Awakened Shrub",
    "Awakened Tree",
    "Axe Beak",
    "Azer",
    "Baboon",
    "Badger",
    "Balor",
    "Bandit",
    "Bandit Captain",
    "Banshee",
    "Barbed Devil",
    "Barlgura",
    "Basilisk",
    "Bat",
    "Bearded Devil",
    "Behir",
    "Beholder",
    "Beholder Zombie",
    "Berserker",
    "Black Bear",
    "Black Dragon Wyrmling",
    "Black Pudding",
    "Blink Dog",
    "Blood Hawk",
    "Blue Dragon Wyrmling",
    "Blue Slaad",
    "Boar",
    "Bone Devil",
    "Bone Naga",
    "Brass Dragon Wyrmling",
    "Bronze Dragon Wyrmling",
    "Brown Bear",
    "Bugbear",
    "Bugbear Chief",
    "Bulette",
    "Bullywug",
    "Cambion",
    "Camel",
    "Carrion Crawler",
    "Cat",
    "Centaur",
    "Chain Devil",
    "Chasme",
    "Chimera",
    "Chuul",
    "Clay Golem",
    "Cloaker",
    "Cloud Giant",
    "Cockatrice",
    "Commoner",
    "Constrictor Snake",
    "Copper Dragon Wyrmling",
    "Couatl",
    "Crab",
    "Crawling Claw",
    "Crocodile",
    "Cult Fanatic",
    "Cultist",
    "Cyclops",
    "Dao",
    "Darkmantle",
    "Death Dog",
    "Death Knight",
    "Death Slaad",
    "Death Tyrant",
    "Deep Gnome (Svirfneblin)",
    "Deer",
    "Demilich",
    "Deva",
    "Dire Wolf",
    "Displacer Beast",
    "Djinni",
    "Doppelganger",
    "Draft Horse",
    "Dragon Turtle",
    "Dretch",
    "Drider",
    "Drow",
    "Drow Elite Warrior",
    "Drow Mage",
    "Drow Priestess of Lolth",
    "Druid",
    "Dryad",
    "Duergar",
    "Duodrone",
    "Dust Mephit",
    "Eagle",
    "Earth Elemental",
    "Efreeti",
    "Elephant",
    "Elk",
    "Empyrean",
    "Erinyes",
    "Ettercap",
    "Ettin",
    "Faerie Dragon",
    "Fire Elemental",
    "Fire Giant",
    "Fire Snake",
    "Flameskull",
    "Flesh Golem",
    "Flumph",
    "Flying Snake",
    "Flying Sword",
    "Fomorian",
    "Frog",
    "Frost Giant",
    "Galeb Duhr",
    "Gargoyle",
    "Gas Spore",
    "Gelatinous Cube",
    "Ghast",
    "Ghost",
    "Ghoul",
    "Giant Ape",
    "Giant Badger",
    "Giant Bat",
    "Giant Boar",
    "Giant Centipede",
    "Giant Constrictor Snake",
    "Giant Crab",
    "Giant Crocodile",
    "Giant Eagle",
    "Giant Elk",
    "Giant Fire Beetle",
    "Giant Frog",
    "Giant Goat",
    "Giant Hyena",
    "Giant Lizard",
    "Giant Octopus",
    "Giant Owl",
    "Giant Poisonous Snake",
    "Giant Rat",
    "Giant Scorpion",
    "Giant Sea Horse",
    "Giant Shark",
    "Giant Spider",
    "Giant Toad",
    "Giant Vulture",
    "Giant Wasp",
    "Giant Weasel",
    "Giant Wolf Spider",
    "Giant Hyena",
    "Giant Lizard",
    "Giant Octopus",
    "Giant Owl",
    "Giant Poisonous Snake",
    "Giant Rat",
    "Giant Scorpion",
    "Giant Sea Horse",
    "Giant Shark",
    "Giant Spider",
    "Giant Toad",
    "Giant Vulture",
    "Giant Wasp",
    "Giant Weasel",
    "Giant Wolf Spider",
    "Gibbering Mouther",
    "Glabrezu",
    "Gladiator",
    "Gnoll",
    "Gnoll Fang of Yeenoghu",
    "Gnoll Pack Lord",
    "Goat",
    "Goblin",
    "Goblin Boss",
    "Gold Dragon Wyrmling",
    "Gorgon",
    "Gray Ooze",
    "Green Dragon Wyrmling",
    "Green Hag",
    "Griffon",
    "Grimlock",
    "Guard",
    "Guardian Naga",
    "Gynosphinx",
    "Half-Red Dragon Veteran",
    "Harpy",
    "Hawk",
    "Hezrou",
    "Hill Giant",
    "Hippogriff",
    "Hobgoblin",
    "Hobgoblin Captain",
    "Hobgoblin Warlord",
    "Homunculus",
    "Horned Devil",
    "Hunter Shark",
    "Hydra",
    "Hyena",
    "Ice Devil",
    "Ice Mephit",
    "Imp",
    "Intellect Devourer",
    "Invisible Stalker",
    "Iron Golem",
    "Jackal",
    "Killer Whale",
    "Knight",
    "Kobold",
    "Kraken",
    "Lamia",
    "Lemure",
    "Lich",
    "Lizard",
    "Lizardfolk",
    "Lizardfolk Shaman",
    "Mage",
    "Magma Mephit",
    "Magmin",
    "Mammoth",
    "Manticore",
    "Marilith",
    "Mastiff",
    "Medusa",
    "Merfolk",
    "Merrow",
    "Mezzoloth",
    "Mimic",
    "Minotaur",
    "Minotaur Skeleton",
    "Mule",
    "Mummy",
    "Mummy Lord",
    "Myconid Adult",
    "Myconid Sovereign",
    "Myconid Sprout",
    "Nalfeshnee",
    "Noble",
    "Ochre Jelly",
    "Octopus",
    "Ogre",
    "Ogre Zombie",
    "Oni",
    "Orc",
    "Orog",
    "Otyugh",
    "Owl",
    "Owlbear",
    "Pegasus",
    "Pentadrone",
    "Peryton",
    "Pirate",
    "Pixie",
    "Planetar",
    "Plesiosaurus",
    "Poisonous Snake",
    "Polar Bear",
    "Pony",
    "Priest",
    "Pseudodragon",
    "Pterydactyl",
    "Purple Worm",
    "Quasit",
    "Quipper",
    "Rakshasa",
    "Rat",
    "Raven",
    "Red Dragon Wyrmling",
    "Reef Shark",
    "Remorhaz",
    "Rhinoceros",
    "Riding Horse",
    "Roc",
    "Roper",
    "Rug of Smothering",
    "Rust Monster",
    "Saber-Toothed Tiger",
    "Sahuagin",
    "Sahuagin Baron",
    "Sahuagin Priestess",
    "Salamander",
    "Satyr",
    "Scorpion",
    "Scout",
    "Sea Hag",
    "Sea Horse",
    "Shadow",
    "Shambling Mound",
    "Shield Guardian",
    "Shrieker",
    "Silver Dragon Wyrmling",
    "Skeleton",
    "Solar",
    "Specter",
    "Spider",
    "Spirit Naga",
    "Sprite",
    "Spy",
    "Steam Mephit",
    "Stirge",
    "Stone Giant",
    "Stone Golem",
    "Storm Giant",
    "Succubus/Incubus",
    "Swarm of Bats",
    "Swarm of Bees",
    "Swarm of Centipedes",
    "Swarm of Insects",
    "Swarm of Poisonous Snakes",
    "Swarm of Quippers",
    "Swarm of Rats",
    "Swarm of Ravens",
    "Swarm of Spiders",
    "Swarm of Wasps",
    "Tarrasque",
    "Thug",
    "Tiger",
    "Treant",
    "Tribal Warrior",
    "Triceratops",
    "Troglodyte",
    "Troll",
    "Tyrannosaurus Rex",
    "Ultroloth",
    "Umber Hulk",
    "Unicorn",
    "Vampire",
    "Vampire Spawn",
    "Veteran",
    "Violet Fungus",
    "Vrock",
    "Vulture",
    "Warhorse",
    "Warhorse Skeleton",
    "Water Elemental",
    "Weasel",
    "Werebear",
    "Wereboar",
    "Wererat",
    "Weretiger",
    "Werewolf",
    "White Dragon Wyrmling",
    "Wight",
    "Will-o'-Wisp",
    "Winter Wolf",
    "Wolf",
    "Worg",
    "Wraith",
    "Wyvern",
    "Xorn",
    "Yeti",
    "Yuan-ti Abomination",
    "Yuan-ti Malison",
    "Yuan-ti Pureblood",
    "Zombie",
]

base = "https://www.aidedd.org/dnd/monstres.php?vo="
urls = []

for name in monster_names:
    name = name.lower().replace(' ','-')
    download = f"{base}{name}"
    urls.append(download)


import requests
from bs4 import BeautifulSoup
import json

def parse_monster(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    monster_info = {}
    current_section = 'features'  # Default section for items before 'Actions'
    monster_info[current_section] = []

    # Extracting the name
    name = soup.find('h1')
    if name:
        monster_info['name'] = name.get_text(strip=True)

    # Extracting type and alignment
    type_alignment = soup.select_one('.sansSerif .type')
    if type_alignment:
        monster_info['type'], monster_info['alignment'] = type_alignment.get_text(strip=True).split(',', 1)

    # Extracting other details like AC, HP, Speed
    for item in soup.select('.sansSerif > div.red > strong'):
        key = item.get_text(strip=True)
        value = item.next_sibling.strip()
        monster_info[key] = value

    # Extracting characteristics like STR, DEX, etc.
    for carac in soup.select('.sansSerif .carac'):
        key = carac.strong.get_text(strip=True)
        value = carac.get_text(strip=True).replace(key, '').strip()
        monster_info[key] = value

    # Extracting saving throws, skills, damage immunities, senses, languages, challenge rating
    text_divs = soup.select('.sansSerif > div:not(.carac):not(.red)')
    for div in text_divs:
        text = div.get_text(separator='|', strip=True).split('|')
        for t in text:
            if ':' in t:
                key, value = t.split(':', 1)
                monster_info[key.strip()] = value.strip()

    # Extracting features, actions, etc.
    for section in soup.select('.sansSerif > p, .sansSerif > div.rub'):
        section_title = section.get_text(strip=True)
        if section.name == 'div':
            if section_title == 'Actions':
                current_section = section_title
                monster_info[current_section] = []
            elif current_section != 'features':
                current_section = section_title
                monster_info[current_section] = []
        else:
            monster_info[current_section].append(section.get_text(strip=True))

    return monster_info


# url = "https://www.aidedd.org/dnd/monstres.php?vo=ancient-black-dragon"

# # Processing one page at a time
# response = requests.get(url)
# monster_data = parse_monster(response.content)

# # Displaying the data in a pretty JSON format
# print(json.dumps(monster_data, indent=4))


dnd_monsters = {}

# Process each URL
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Processing:  {url}")
        monster_name = url.split('/')[-1]  # Assuming the URL contains the monster's name at the end
        dnd_monsters[monster_name] = parse_monster(response.content)
    else:
        print(f"Issues with: {url}")

# Save dnd_monsters as a Python file
with open('dnd_monsters.py', 'w') as file:
    file.write('dnd_monsters = ' + json.dumps(dnd_monsters, indent=4))






# Download the files...
# import requests
# try:
#     # Send an HTTP GET request to the URL
#     response = requests.get(url)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Save the content to a file
#         with open(f"{name}.html", "wb") as file:
#             file.write(response.content)
#         print("Web page downloaded successfully.")
#     else:
#         print(f"Failed to download the web page. Status code: {response.status_code}")

# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")
