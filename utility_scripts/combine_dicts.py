#! /usr/bin/env python3

import json
from dnd_monster_update import *
from dnd_monsters import *

# Merge dnd_monsters_update into dnd_monsters
for key, sub_dict in dnd_monsters_update.items():
    if key in dnd_monsters:
        dnd_monsters[key].update(sub_dict)
    else:
        dnd_monsters[key] = sub_dict

# Now, dnd_monsters contains the merged data
print(dnd_monsters)

with open('./dnd_monsters_united.py', 'w') as json_file:
    json.dump(dnd_monsters, json_file, indent=4)

    