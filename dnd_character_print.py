#! /usr/bin/env python3
from dnd_helper import *

def print_character(dictionary, spaces=2, padding_value=35):
    try:
        for key, value in dictionary.items():
            if isinstance(value, dict):  # Check if value is a nested dictionary
                print(f"{' ' * spaces}{key} :")
                print_character(value, spaces + 2)  # recursively call the function to handle nested dictionary
            elif isinstance(value, list):  
                print(f"{' ' * spaces}{key} :")
                list_space = spaces + 2
                for v in value:
                    print(f"{' ' * list_space}{v} :")
                print_character(value, spaces + 2)  # recursively call the function to handle nested dictionary
            else:
                padding = padding_value - spaces
                print(f"{' ' * spaces}{f'{key:<{padding}}'} : {value}")  # print key-value pair if value is not a nested dictionary
    except:
        # print(f"{' ' * spaces}None")
        print(f"{' ' * spaces}")


def print_inventory(dictionary, name, padding_value=35):
    for index, item in enumerate(dictionary):
        print(f"  {name} #{index + 1}:")
        for value in item.keys():
            print(f"    {f'{value:<{padding_value - 4}}'} : {item[value]}")

