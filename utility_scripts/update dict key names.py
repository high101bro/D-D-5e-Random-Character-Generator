#! /usr/bin/env python3
import json

from dnd_monsters import *

# Create a new dictionary to store the updated data
new_dnd_monsters = {}

# Iterate through the original dictionary
for key, value in dnd_monsters.items():
    # Extract the "Name" sub-key value
    new_key = value.get("Name")
    
    # Add the entry to the new dictionary with the updated key
    new_dnd_monsters[new_key] = value

# Now, new_dnd_monsters contains the updated data
print(new_dnd_monsters)

file_path = "new_dnd_monsters.py"

# Write the dictionary to a JSON file
with open(file_path, "w") as json_file:
    json.dump(new_dnd_monsters, json_file, indent=4)
