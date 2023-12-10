#! /usr/bin/env python3 
import readline

# Sample inventory data (with mixed casing)
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "Apricot": 3,
    "carrot": 15,
    "Cabbage": 6,
    "grape": 12,
    "Lettuce": 7,
    "peach": 9,
    "plum": 4,
    "Watermelon": 2,
    "tomato": 11,
    "Onion": 5,
    "Strawberry": 6,
    "Potato": 10,
    "kiwi": 3,
    "Mango": 5,
    "pear": 7,
    "Cherry": 4,
    "zucchini": 9,
    "EggPlant": 5,
    "BlueBerry": 12,
    "spinach": 8,
    "Pineapple": 4,
    "radish": 6,
    "Raspberry": 3,
    "GrapeFruit": 4,
    "Cucumber": 7,
    "pumpkin": 5,
    "lemon": 8,
    "lime": 7,
    "ripe avocado": 4,
    "guava": 3,
    "strudel": 2,
    "broccoli": 6,
    "pea": 10,
    "artichoke": 3,
    "asparagus": 4,
    "cantaloupe": 3,
    "fig": 5,
    "kale": 6,
    "papaya": 4,
    "radicchio": 3,
    "shallot": 2,
    "tangerine": 7,
    "turnip": 4,
}
def autocomplete_inventory(text, state):
    text = text.lower()
    options = [key for key in inventory.keys() if text in key.lower()]
    if state < len(options):
        return options[state]
    else:
        return None

# Set the autocomplete function
readline.set_completer(autocomplete_inventory)
readline.parse_and_bind("tab: complete")

while True:
    user_input = input("Enter an item from your inventory: ")
    user_input = user_input.lower()  # Convert user input to lowercase
    
    # Check if the entered item (in lowercase) is in the inventory
    if user_input in inventory:
        print(f"You have {inventory[user_input]} {user_input}(s) in your inventory.")
    else:
        print(f"{user_input} is not in your inventory. Please enter a valid item.")
