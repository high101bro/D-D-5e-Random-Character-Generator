#! /usr/bin/env python3



import numpy as np
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()



# Initialize the grid and path start column
grid_size = 100
path_width = 5  # Define path_width here
middle_start = grid_size // 2
path_start_col = random.randint(middle_start - 5, middle_start + 5)

def update_path_start_col(path_start_col, grid_size, path_width):
    path_start_col += random.choice([-1, 0, 1])
    return max(0, min(path_start_col, grid_size - path_width))


####################################################################################################
# Colors
####################################################################################################

def get_color_code(color_name):
    colors = {
        "Black_FG": "\033[30m",
        "Red_FG": "\033[31m",
        "Green_FG": "\033[32m",
        "Yellow_FG": "\033[33m",
        "Blue_FG": "\033[34m",
        "Magenta_FG": "\033[35m",
        "Cyan_FG": "\033[36m",
        "White_FG": "\033[37m",
        "Brown_FG": "\033[33m",
        "Dark_Green_FG": "\033[32m",
        "Black_BG": "\033[40m",
        "Red_BG": "\033[41m",
        "Green_BG": "\033[42m",
        "Yellow_BG": "\033[43m",
        "Blue_BG": "\033[44m",
        "Magenta_BG": "\033[45m",
        "Cyan_BG": "\033[46m",
        "White_BG": "\033[47m",
        "Brown_BG": "\033[43m",
        "Dark_Green_BG": "\033[42m",
        "Reset": "\033[0m",
        "Bold Text": "\033[1m",
        "Underline": "\033[4m",
        "Reverse (Swap Foreground and Background)": "\033[7m",
        "Blink Slow": "\033[5m", #(often synonymous with flashing, but not all terminals support rapid blinking)
        "Blink Rapid": "\033[6m", #(not widely supported)
        "Italic": "\033[3m", #(not universally supported across all terminals)
        "Dim": "\033[2m",
        "Hidden (Conceal)": "\033[8m",
        "Strikethrough": "\033[9m", #(not universally supported)
        "Reset Bold/Dim": "\033[22m",
        "Reset Underline": "\033[24m",
        "Reset Blink": "\033[25m",
        "Reset Reverse": "\033[27m",
        "Reset Hidden": "\033[28m",
        "Reset All": "\033[0m",
        'Cyan': "\033[96m", #"\033[106m",   # Light cyan for characters
        'Red': "\033[91m",   # Light red for monsters
        'Green': "\033[92m",  # Light green for trees
        'Blue': "\033[94m",  # Light blue for the river
        'Brown': "\033[93m"  # Brown for the tree trunk (added color)
        
        # Add more colors as needed
    }
    return colors.get(color_name, "\033[97m")  # Default to white

####################################################################################################
# Symbols
####################################################################################################

utf8_symbols = {
    'menu': '\u2630',            # ☰
    'heart': '\u2665',           # ♥
    'square': '\u25A0',          # ■
    'circle': '\u25CF',          # ●
    'triangle_up': '\u25B2',     # ▲
    'triangle_down': '\u25BC',   # ▼
    'clover': '\u2663',          # ♣
    'cloud': '\u2601',           # ☁
    'smiley_face': '\u263A',     # ☺
    'sad_face': '\u2639',        # ☹
    'person': '\u263A',          # ☺ (generic human symbol)
    'girl': '\u2640',            # ♀
    'boy': '\u2642',             # ♂
    'star': '\u2605',            # ★
    'check_mark': '\u2713',      # ✓
    'cross_mark': '\u2717',      # ✗
    'music_note': '\u266B',      # ♫
    'sun': '\u2600',             # ☀
    'moon': '\u263D',            # ☽
    'umbrella': '\u2602',        # ☂
    'snowflake': '\u2744',       # ❄
    'telephone': '\u260E',       # ☎
    'hourglass': '\u231B',       # ⌛
    'warning': '\u26A0',         # ⚠
    'plane': '\u2708',           # ✈
    'anchor': '\u2693',          # ⚓
    'yin_yang': '\u262F',        # ☯
    'peace': '\u262E',           # ☮
    'biohazard': '\u2623',       # ☣
    'radiation': '\u2622',       # ☢
    'skull_crossbones': '\u2620',# ☠
    'recycle': '\u267B',         # ♻
    'wheelchair': '\u267F',      # ♿
    'infinity': '\u221E',        # ∞
    'lightning': '\u26A1',       # ⚡
    'sword': '\u2694',  # ⚔ Crossed swords
    'wizard': '\u1F9D9',  # 🧙 Wizard
    'dragon': '\u1F409',  # 🐉 Dragon
    'castle': '\u1F3F0',  # 🏰 Castle
    'scroll': '\u1F4DC',  # 📜 Scroll
    'potion': '\u1F9EA',  # 🧪 Potion
    'crystal_ball': '\u1F52E',  # 🔮 Crystal ball
    'dagger': '\u1F5E1',  # 🗡 Dagger
    'shield': '\u1F6E1',  # 🛡 Shield
    'bow_and_arrow': '\u1F3F9',  # 🏹 Bow and arrow
    'magic_wand': '\u1FA84',  # 🪄 Magic wand
    'axe': '\u1FA93',  # 🪓 Axe
    'book_spell': '\u1F4D6',  # 📖 Open book (for spellbook)
    'treasure_chest': '\u1F9F0',  # 🧰 Treasure chest
    'gem_stone': '\u1F48E',  # 💎 Gem stone
    'goblin': '\u1F47A',  # 👺 Goblin
    'elf': '\u1F9DD',  # 🧝 Elf
    'dwarf': '\u1F9DF',  # 🧟 Dwarf
    'ghost': '\u1F47B',  # 👻 Ghost
    'skull': '\u1F480',  # 💀 Skull
    'mushroom': '\u1F344',  # 🍄 Mushroom (for foraging or magical herbs)
    'campfire': '\u1F3D4',  # 🏔 Snow-capped mountain (for adventure terrain)
    'mountain': '\u26F0',  # ⛰ Mountain (for quest locations)
    'map': '\u1F5FA',  # 🗺 World map
    'compass': '\u1F9ED',  # 🧭 Compass (for navigation)
    'spyglass': '\u1F50D',  # 🔍 Spyglass (for exploration)
    'coins': '\u1FA99',  # 🪙 Coins (for treasure and currency)
    'crown': '\u1F451',  # 👑 Crown (for royalty or high-value treasure)
    'key': '\u1F511',  # 🔑 Key (for unlocking treasures or doors)
    'door': '\u1F6AA',  # 🚪 Door (for dungeons or buildings)
    'monster': '\u1F9DF',  # 🧟 Monster or undead creature
    'spell': '\u2728',  # ✨ Sparkles (to represent magic or spells)
    'flame': '\u1F525',  # 🔥 Flame (for fire spells or campfires)
    'tree': '\u1F333',  # 🌳 Tree (for forests and nature)
    'fish': '\u1F41F',  # 🐟 Fish (for water creatures or food)
    'tent': '\u1F3D5',  # 🏕 Tent (for camping or temporary shelter)
    'horse': '\u1F40E',  # 🐎 Horse (for mounts and travel)
    'boat': '\u1F6A3',  # 🚣 Boat (for water travel)
    'anchor': '\u2693',  # ⚓ Anchor (for nautical themes)
    'sword_shield': '\u2694',  # ⚔ Sword and shield (for combat and warriors)
    'wizard_hat': '\u1F9D9',
    # 'fire': '\uFire',            # 🔥
    # 'leaf': '\uLeaf',            # 🍃
    # 'flower': '\uFlower',        # 🌸
    # 'star_half': '\uStar Half',  # ⭐
    # 'star_outline': '\uStar Outline',  # 🌟
    # 'gear': '\uGear',            # ⚙
    # 'atom': '\uAtom',            # ⚛
    # 'magnifying_glass': '\uMagnifying Glass',  # 🔍
    # 'light_bulb': '\uLight Bulb',# 💡
    # 'pencil': '\uPencil',        # ✏
    # 'hammer_wrench': '\uHammer and Wrench',  # 🔨
    # 'shield': '\uShield',        # 🛡
    # 'key': '\uKey',              # 🔑
    # 'lock': '\uLock',            # 🔒
    # 'lock_open': '\uLock Open',  # 🔓
    # 'envelope': '\uEnvelope',    # ✉
    # 'pushpin': '\uPushpin',      # 📌
    # 'battery_full': '\uBattery Full',  # 🔋
    # 'battery_empty': '\uBattery Empty',  # 🔌
    # 'globe': '\uGlobe',          # 🌍
    # 'compass': '\uCompass',      # 🧭
    # 'map': '\uMap',              # 🗺
    # 'book': '\uBook',            # 📖
    # 'calendar': '\uCalendar',    # 📅
    # 'clock': '\uCclock',         # ⏰
    # 'hourglass_flowing': '\uHourglass Flowing Sand',  # ⏳
    # 'flag': '\uFlag',            # 🏁
    # 'trophy': '\uTrophy',        # 🏆
    # 'medal': '\uMedal',          # 🏅
    # 'scales': '\uScales',        # ⚖
}

####################################################################################################
# Trees
####################################################################################################

def place_trees(grid, grid_size, num_trees, tree_density):
    for _ in range(num_trees):
        tree_row = random.randint(0, grid_size - 1)
        tree_col = random.randint(0, grid_size - 1)
        # Place the tree trunk
        grid[tree_row, tree_col] = f"{get_color_code('Brown')}[TT]{reset_color}"  # Tree trunk in brown
        radius = random.randint(1, tree_density)  # Radius of the tree circle based on tree_density
        for dy in range(-radius, radius + 1):
            for dx in range(-radius, radius + 1):
                if dy**2 + dx**2 <= radius**2:
                    new_row = tree_row + dy
                    new_col = tree_col + dx
                    if 0 <= new_row < grid_size and 0 <= new_col < grid_size and (new_row, new_col) != (tree_row, tree_col):
                        # Place the green part of the tree, avoiding the trunk
                        grid[new_row, new_col] = f"{get_color_code('Green')}[Tr]{reset_color}"


####################################################################################################
# Lakes
####################################################################################################

def place_lake(grid, grid_size):
    chance = random.randint(1,100)
    if chance > 25:
        river_color = get_color_code('Blue')
        path_directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # Up, Left, Right, Down
        river_row = random.randint(0, grid_size - 1)
        river_col = random.randint(0, grid_size - 1)
        river_size = random.choice([2,2,2,2,3,3,3,3,4,4,4,5,5,6,7,8])
        for _ in range(grid_size * river_size):  # Make the river longer by changing the multiplier
            grid[river_row, river_col] = f"{river_color}[Wt]{reset_color}"
            path_direction = random.choice(path_directions)
            river_row += path_direction[0]
            river_col += path_direction[1]
            river_row = max(0, min(river_row, grid_size - 1))
            river_col = max(0, min(river_col, grid_size - 1))

####################################################################################################
# Rivers
####################################################################################################

def place_river(grid, grid_size):
    direction = random.choice(['25% Horizontal', 'None' '75% Horizontal', 'None','Horizontal', 'None','Diagonal Backslash', 'None', 'Diagonal Forwardslash', 'None'])

    if direction in ['25% Horizontal', '75% Horizontal']:
        river_color = get_color_code('Blue')
        river_width = random.randint(4, 7)  # Width of the river (2 to 5 squares)
        
        if direction == '25%':
            river_start = grid_size // 4  # Starting column of the river (25% of the grid)
        else:
            river_start = (grid_size * 3) // 4  # Starting column of the river (75% of the grid)

        # Initialize the river path as a list of points
        river_path = [(0, river_start)]

        # Create a wiggling path for the river
        for row in range(1, grid_size):
            prev_col = river_path[-1][1]
            next_col = prev_col + random.choice([-1, 0, 1])
            next_col = max(0, min(next_col, grid_size - 1))
            river_path.append((row, next_col))

        # Fill the river path in the grid
        for row, col in river_path:
            for w in range(river_width):
                if 0 <= col + w < grid_size:
                    grid[row, col + w] = f"{river_color}[Wt]{reset_color}"
    
    elif direction == 'Horizontal':
        river_color = get_color_code('Blue')
        river_width = random.randint(4, 7)  # Width of the river (2 to 5 squares)
        river_start = random.randint(0, grid_size - river_width)  # Starting row of the river

        # Initialize the river path as a list of points
        river_path = [(river_start, 0)]

        # Create a wiggling path for the river
        for col in range(1, grid_size):
            prev_row = river_path[-1][0]
            next_row = prev_row + random.choice([-1, 0, 1])
            next_row = max(0, min(next_row, grid_size - 1))
            river_path.append((next_row, col))

        # Fill the river path in the grid
        for row, col in river_path:
            for w in range(river_width):
                if 0 <= row + w < grid_size:
                    grid[row + w, col] = f"{river_color}[Wt]{reset_color}"

    elif direction == 'Diagonal Backslash':
        river_color = get_color_code('Blue')
        river_width = random.randint(4, 7)  # Width of the river (2 to 5 squares)

        # Initialize the river path as a list of points
        river_path = []

        # Create a more diagonal path for the river
        col = random.randint(0,25)  # Start from the left edge
        for row in range(grid_size):
            col += random.choice([-2,-1,0,1,2,3])  # More diagonal movement in the column position
            col = max(0, min(col, grid_size - river_width))  # Ensure it doesn't go out of bounds
            river_path.append((row, col))

        # Fill the river path in the grid
        for row, col in river_path:
            for w in range(river_width):
                if 0 <= col + w < grid_size:
                    grid[row, col + w] = f"{river_color}[Wt]{reset_color}"
    elif direction == 'Diagonal Forwardslash':
        river_color = get_color_code('Blue')
        river_width = random.randint(4, 7)  # Width of the river (2 to 5 squares)

        # Initialize the river path as a list of points
        river_path = []

        # Create a more diagonal path for the river
        col = random.randint(grid_size-25,grid_size)  # Start from the left edge
        for row in range(grid_size):
            col -= random.choice([-2,-1,0,1,2,3])  # More diagonal movement in the column position
            col = max(0, min(col, grid_size - river_width))  # Ensure it doesn't go out of bounds
            river_path.append((row, col))

        # Fill the river path in the grid
        for row, col in river_path:
            for w in range(river_width):
                if 0 <= col + w < grid_size:
                    grid[row, col + w] = f"{river_color}[Wt]{reset_color}"        
    elif direction == 'None':
        pass


####################################################################################################
# Boulder
####################################################################################################

def place_boulders(grid, grid_size, num_boulders):
    boulder_color = "\033[97m"  # White for boulders, can change color if desired
    for _ in range(num_boulders):
        while True:
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)
            if grid[row, col] == f"{empty_area_color}[  ]{reset_color}":  # Check if spot is empty
                grid[row, col] = f"{boulder_color}[Rk]{reset_color}"
                break


####################################################################################################
# Graveyard
####################################################################################################

def is_area_free_for_graveyard(grid, start_row, start_col, width, height, grid_size):
    """ Check if the specified area in the grid is free for a graveyard. """
    if start_row + height > grid_size or start_col + width > grid_size:
        return False  # Out of grid bounds

    for r in range(start_row, start_row + height):
        for c in range(start_col, start_col + width):
            if grid[r, c] != f"{empty_area_color}[  ]{reset_color}":
                return False  # Spot already occupied
    return True

def place_graveyard(grid, grid_size):
    chance = random.randint(1,100)
    if chance > 75:
        max_attempts = 100  # Limit attempts to find a location

        for _ in range(max_attempts):
            graveyard_width = random.randint(4, 8)
            graveyard_height = random.randint(4, 6)
            graveyard_row = random.randint(0, grid_size - graveyard_height)
            graveyard_col = random.randint(0, grid_size - graveyard_width)

            if is_area_free_for_graveyard(grid, graveyard_row, graveyard_col, graveyard_width, graveyard_height, grid_size):
                # Place the graveyard
                for r in range(graveyard_height):
                    for c in range(graveyard_width):
                        grid[graveyard_row + r, graveyard_col + c] = f"{get_color_code('White_BG')}{get_color_code('Dim')}[Gr]{reset_color}"
                break  # Exit loop after placing the graveyard


# ####################################################################################################
# # Town
# ####################################################################################################
# def place_town(grid, grid_size):
#     town_color = get_color_code('Cyan')  # Define a color for the town buildings
#     num_buildings = random.randint(0, 3)  # Number of buildings in the town

#     # Store centers of the existing buildings
#     building_centers = []

#     for _ in range(num_buildings):
#         building_width = random.randint(2, 4)
#         building_height = random.randint(2, 4)

#         if building_centers:
#             # Choose a random building and place the new one within 5-10 squares
#             ref_building = random.choice(building_centers)
#             distance = random.randint(5, 10)
#             direction = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
#             town_row = max(0, min(ref_building[0] + direction[0] * distance, grid_size - building_height))
#             town_col = max(0, min(ref_building[1] + direction[1] * distance, grid_size - building_width))
#         else:
#             # Randomly choose a starting location for the first building
#             town_row = random.randint(0, grid_size - building_height)
#             town_col = random.randint(0, grid_size - building_width)

#         # Place each building in the town
#         for r in range(building_height):
#             for c in range(building_width):
#                 new_row = town_row + r
#                 new_col = town_col + c
#                 grid[new_row, new_col] = f"{town_color}[Bl]{reset_color}"

#         # Add the center of the new building to building_centers
#         building_centers.append((town_row + building_height // 2, town_col + building_width // 2))


####################################################################################################
# Town with potential wall 
####################################################################################################

def is_suitable_for_building(grid, start_row, start_col, width, height, grid_size, buffer=1):
    """ Check if the specified area in the grid is free for a building, including a buffer zone. """
    for r in range(start_row - buffer, start_row + height + buffer):
        for c in range(start_col - buffer, start_col + width + buffer):
            if 0 <= r < grid_size and 0 <= c < grid_size:
                if grid[r, c] != f"{empty_area_color}[  ]{reset_color}":
                    return False  # Spot already occupied or too close to another building
    return True

def place_town_with_walls(grid, grid_size, num_buildings_range, building_width_range, building_height_range, generate_wall):
    buildings_created = 0
    town_color = get_color_code('Cyan')  # Define a color for the town buildings
    low, high = num_buildings_range
    num_buildings = random.randint(low, high)  # Number of buildings in the town
    wall_buffer = 5  # Distance between the buildings and the wall

    # Variables to track the boundaries of the town
    min_row, max_row = grid_size, 0
    min_col, max_col = grid_size, 0

    # Store centers of the existing buildings
    building_centers = []

    for _ in range(num_buildings):
        low, high = building_width_range
        building_width = random.randint(low, high)
        low, high = building_height_range
        building_height = random.randint(low, high)

        # Find a suitable location for the new building
        for _ in range(100):  # Limit attempts to avoid infinite loop
            is_location_found = False

            if building_centers:
                # Choose a location near an existing building but maintaining distance
                for _ in range(200):  # Inner loop to try different locations near existing buildings
                    ref_building = random.choice(building_centers)
                    distance = random.randint(3, 8)
                    direction = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
                    potential_row = ref_building[0] + direction[0] * distance
                    potential_col = ref_building[1] + direction[1] * distance
                    town_row = max(0, min(potential_row, grid_size - building_height))
                    town_col = max(0, min(potential_col, grid_size - building_width))

                    if is_suitable_for_building(grid, town_row, town_col, building_width, building_height, grid_size, buffer=2):
                        is_location_found = True
                        break
            else:
                # Randomly choose a starting location for the first building
                town_row = random.randint(0, grid_size - building_height)
                town_col = random.randint(0, grid_size - building_width)
                is_location_found = True

            if is_location_found:
                buildings_created += 1
                # Place each building in the town
                for r in range(building_height):
                    for c in range(building_width):
                        new_row = town_row + r
                        new_col = town_col + c
                        grid[new_row, new_col] = f"{town_color}[Bl]{reset_color}"

                        # Update town boundaries
                        min_row = min(min_row, new_row)
                        max_row = max(max_row, new_row)
                        min_col = min(min_col, new_col)
                        max_col = max(max_col, new_col)

                # Add the center of the new building to building_centers
                building_centers.append((town_row + building_height // 2, town_col + building_width // 2))
                break


    if generate_wall:
        # Place walls around the town
        wall1 = range(min_row - wall_buffer, max_row + wall_buffer + 1)
        wall2 = range(min_col - wall_buffer, max_col + wall_buffer + 1)
        for row in wall1:
            for col in wall2:
                if (row in [min_row - wall_buffer, max_row + wall_buffer] or col in [min_col - wall_buffer, max_col + wall_buffer]) and 0 <= row < grid_size and 0 <= col < grid_size:
                    if grid[row, col] == f"{empty_area_color}[  ]{reset_color}":
                        grid[row, col] = f"{get_color_code('Brown')}[Wl]{reset_color}"


####################################################################################################
# Bridges
####################################################################################################

def create_bridge():
    # Determine if the path crosses the river and place bridges
    for row in range(grid_size):
        for col in range(grid_size):
            if path_grid[row, col] and grid[row, col] == f"{get_color_code('Blue')}[Wt]{reset_color}":
                grid[row, col] = f"{get_color_code('Brown_FG')}[br]{reset_color}"


####################################################################################################
# Place Characters
####################################################################################################

def place_characters_in_formation(grid, center_row, center_col, characters):
    formations = [
        'V', 'inverted V', 'square', 'circle', 'vertical line', 'horizontal line', 'random',
        'spread out', 'leading', 'trailing', 'two groups vertical', 'two groups horizontal',
        'swiggle vertical', 'swiggle horizontal', 'box', 'carrot left', 'carrot right', 'two columns'
    ]
    formation = random.choice(formations)

    # Default offsets in case no formation matches
    offsets = [(random.randint(-3, 3), random.randint(-3, 3)) for _ in range(5)]

    if formation == 'V':
        offsets = [(0, 0), (-1, -1), (-2, -2), (-1, 1), (-2, 2)]
    elif formation == 'inverted V':
        offsets = [(0, 0), (1, -1), (2, -2), (1, 1), (2, 2)]
    # ... [existing formations] ...
    elif formation == 'spread out':
        offsets = [(0, 0), (-2, -2), (2, 2), (-2, 2), (2, -2)]
    elif formation == 'leading':
        offsets = [(0, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0)]
    elif formation == 'trailing':
        offsets = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
    elif formation == 'two groups vertical':
        offsets = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 3)]
    elif formation == 'two groups horizontal':
        offsets = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 3)]
    elif formation == 'swiggle vertical':
        offsets = [(0, 0), (1, 1), (2, 0), (3, 1), (4, 0)]
    elif formation == 'swiggle horizontal':
        offsets = [(0, 0), (1, -1), (1, 0), (1, 1), (1, 2)]
    elif formation == 'box':
        offsets = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2)]
    elif formation == 'carrot left':
        offsets = [(0, 0), (-1, -1), (-2, -2), (-3, -1), (-4, 0)]
    elif formation == 'carrot right':
        offsets = [(0, 0), (-1, 1), (-2, 2), (-3, 1), (-4, 0)]
    elif formation == 'two columns':
        offsets = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)]

    for char, info in characters.items():
        dy, dx = offsets.pop(0)
        info['Location'] = (center_row + dy, center_col + dx)
        if 0 <= info['Location'][0] < grid_size and 0 <= info['Location'][1] < grid_size:
            grid[info['Location'][0], info['Location'][1]] = f"{get_color_code(info['Color'])}[{info['Marker']}]{get_color_code('Reset All')}"

def is_location_freee(grid, row, col, grid_size):
    """ Check if a grid location is free. """
    return 0 <= row < grid_size and 0 <= col < grid_size and grid[row, col] == f"{empty_area_color}[  ]{reset_color}"

def place_characters_randomly(grid, grid_size, characters):
    for char, info in characters.items():
        while True:
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)
            if is_location_freee(grid, row, col, grid_size):
                grid[row, col] = f"{get_color_code(info['Color'])}[{info['Marker']}]{reset_color}"
                info['Location'] = (row, col)
                break

####################################################################################################
# Place Monsters
####################################################################################################

def is_location_free(grid, row, col):
    """ Check if a grid location is free. """
    return grid[row, col] == f"{empty_area_color}[  ]{reset_color}"

def place_monsters_in_clusters(grid, grid_size, monsters):
    # Determine a random starting point for the first monster
    start_row = random.randint(0, grid_size - 1)
    start_col = random.randint(0, grid_size - 1)

    for char, info in monsters.items():
        while True:
            # Generate row and column within 4 squares of the starting point
            row = random.randint(max(0, start_row - 4), min(grid_size - 1, start_row + 4))
            col = random.randint(max(0, start_col - 4), min(grid_size - 1, start_col + 4))
            if is_location_free(grid, row, col):
                grid[row, col] = f"{get_color_code(info['Color'])}[{info['Marker']}]{reset_color}"
                info['Location'] = (row, col)
                break

def generate_monsters(monster_counts):
    monsters = {}
    for monster_type, count in monster_counts.items():
        monster_group = {}
        for i in range(1, count + 1):
            key = f"{monster_type.lower()}_{str(i).zfill(2)}"
            monster_group[key] = {
                'Name': 'random name',  # Replace with actual name generation if needed
                'Marker': f"{monster_type[0].upper()}{i}",
                'Color': 'Red_BG'
            }
        monsters[monster_type.lower() + 's'] = monster_group
    return monsters


####################################################################################################
# Place Wildlife
####################################################################################################

def generate_wildlife(grid, grid_size, num_wildlife):
    for _ in range(num_wildlife):
        while True:
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)
            if grid[row, col] == f"{empty_area_color}[  ]{reset_color}":  # Check if spot is empty
                grid[row, col] = f"{get_color_code('Green_BG')}[WL]{reset_color}{reset_color}"
                break

####################################################################################################



# Colors
empty_area_color = "\033[100m"
path_color = "\033[43m"
town_color = "\033[106m" 
reset_color = "\033[0m"

# Create the initial grid with pre-generated path
grid = np.full((grid_size, grid_size), f"{empty_area_color}[  ]{reset_color}")
path_grid = np.zeros((grid_size, grid_size), dtype=bool)  # This will track the path
for row in range(grid_size):
    path_start_col = update_path_start_col(path_start_col, grid_size, path_width)
    for col in range(path_start_col, path_start_col + path_width):
        grid[row, col] = f"{path_color}[  ]{reset_color}"
        path_grid[row, col] = True  # Mark path cells

# Determine the center point of the path
center_row = grid_size // 2
center_col = path_start_col + path_width // 2


# Place boulders on the grid
num_boulders = random.randint(20, 40)
place_boulders(grid, grid_size, num_boulders)

num_wildlife = random.randint(20, 40)
generate_wildlife(grid, grid_size, num_wildlife)

# Place a graveyard on the grid
place_graveyard(grid, grid_size)

# Place lake
place_lake(grid, grid_size)

# Place river
place_river(grid, grid_size)

if random.choice([False,False,False,True]):
    place_town_with_walls(grid, grid_size, building_width_range=(4, 6), building_height_range=(4, 6), num_buildings_range=(15, 20), generate_wall=True)

if random.choice([False,False,False,True]):
    place_town_with_walls(grid, grid_size, building_width_range=(2, 5), building_height_range=(2, 5), num_buildings_range=(0, 3), generate_wall=False)

create_bridge

# Place trees
place_trees(grid, grid_size, random.randint(30,150), random.randint(1,3))  # Adjust 30 to the desired number of trees

# Place town
# place_town(grid, grid_size)


# Character information with their locations
characters = {
    'Druid': {
        'Name': 'Hippie', 
        'Marker': '01', 
        # 'Location': character_positions[0],
        'Color': 'Magenta_BG'
    },
    'Ranger': {
        'Name': 'Eragon', 
        'Marker': '02', 
        # 'Location': character_positions[1],
        'Color': 'Magenta_BG'
    },
    'Sorcerer': {
        'Name': 'Witcher', 
        'Marker': '03', 
        # 'Location': character_positions[2],
        'Color': 'Magenta_BG'
    },
    'Rogue': {
        'Name': 'Slyman', 
        'Marker': '04', 
        # 'Location': character_positions[3],
        'Color': 'Magenta_BG'
    },
    'Paladin': {
        'Name': 'Gunter', 
        'Marker': '05', 
        # 'Location': character_positions[4],
        'Color': 'Magenta_BG'
    }
}

place_characters_in_formation(grid, center_row, center_col, characters)



monster_counts = {'Zombie': 8, 'Skeleton': 4, 'Raptors1': 4, 'Raptors2': 4}  # Specify count for each monster type
monsters = generate_monsters(monster_counts)
for monster_type in monsters:
    place_monsters_in_clusters(grid, grid_size, monsters[monster_type])





create_bridge











# Format grid for display
grid_display = "\n".join(["".join(row) for row in grid])
print(grid_display)
