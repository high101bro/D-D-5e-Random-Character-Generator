#! /usr/bin/env python3

from simple_term_menu import TerminalMenu

xp_thresholds = {
    # xp thresholds by character level
    # indice 0 = easy, 1 = medium, 2 = hard, 3 = deadly
    1: [25, 50, 75, 100], 
    2: [50, 100, 150, 200], 
    3: [75, 150, 225, 400],
    4: [125, 250, 375, 500], 
    5: [250, 500, 750, 1100], 
    6: [300, 600, 900, 1400],
    7: [350, 750, 1100, 1700], 
    8: [450, 900, 1400, 2100], 
    9: [550, 1100, 1600, 2400],
    10: [600, 1200, 1900, 2800], 
    11: [800, 1600, 2400, 3600], 
    12: [1000, 2000, 3000, 4500],
    13: [1100, 2200, 3400, 5100], 
    14: [1250, 2500, 3800, 5700], 
    15: [1400, 2800, 4300, 6400],
    16: [1600, 3200, 4800, 7200], 
    17: [2000, 3900, 5900, 8800], 
    18: [2100, 4200, 6300, 9500],
    19: [2400, 4900, 7300, 10900], 
    20: [2800, 5700, 8500, 12700]
}

encounter_multipliers = {
    1 : 1,
    2 : 1.5,
    3 : 2,
    4 : 2,
    5 : 2,
    6 : 2,
    7 : 2.5,
    8 : 2.5,
    9 : 2.5,
    10 : 2.5,
    11 : 3,
    12 : 3,
    13 : 3,
    14 : 3,
    15 : 4,
    # 15 or higher is x4
}

encounter_difficulty = ['easy','medium','hard','deadly']

characters_in_battle = ['dan','lisa']

character_number = len(characters_in_battle)



print('Managing the Battle is under deverlopment...')
characters_on_the_battlefield = []
number_of_characters = int(input(f"How many characters? "))
class Character_in_battle():
    def __init__(self):
        self.name = ''
        self.cr = 0
        self.char_race = ''
        self.char_class = ''
        self.type = ''
        self.ac = 0
        self.hp = 0
        self.speed = 0
        self.initiative = 0
        self.str = 0
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wis = 0
        self.cha = 0
        self.attacks = {}
        self.attack_number = 1
dan = Character_in_battle()
dan.name = 'Elowen'
dan.cr = 2
dan.level = 2
dan.pb = 2
dan.char_race = 'elf'
dan.char_class = 'ranger'
dan.type = 'character'
dan.ac = 12+5+1
dan.hp = 20
dan.speed = 25
dan.initiative = '1d20 + dex'
dan.str = 2
dan.dex = 5
dan.con = 1
dan.int = 0
dan.wis = 2
dan.cha = -1
dan.attacks = {
    'long bow' : '1d20 + 1d8 + dex + pb',
    'rapier' : '1d20 + 1d8 + dex + pb',
}
dan.attack_number = 1

while True:
    # input(f"Enter the character name: ")
    dan = Character_in_battle()
    dan.name = 'dan'
    dan.ac = 17
    break
print(
    dan.name,
    dan.ac
)
print(dan)









encounter_menu_options = [
    "Automated",
    "Guided"
]
encounter_menu_selected = TerminalMenu(encounter_menu_options)
encounter_menu_selected_index = encounter_menu_selected.show()

if encounter_menu_options[encounter_menu_selected_index] == 'Automated':
    for char in range(1,character_number + 1):
        print(char)
if encounter_menu_options[encounter_menu_selected_index] == 'Guided':
    pass




# print(
#     xp_thresholds[1]
# )



