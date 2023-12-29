#! /usr/bin/env python3

import readline
import random
from chatgpt import query_chatgpt
from my_secrets import openai_key
import pickle_handler
from simple_term_menu import TerminalMenu
import string, os, json
from dnd_towns_and_cities import *

def clear(): # DUPLICATE, DELETE ME LATER ONE I REORGANIZE MY CODE
    os.system('cls' if os.name == 'nt' else 'clear')

def terminalmenu_quick_select(list,title): # DUPLICATE, DELETE ME LATER ONE I REORGANIZE MY CODE
    terminal_menu = TerminalMenu(list,title=title)
    terminal_menu_index = terminal_menu.show()
    return list[terminal_menu_index]

def print_character(dictionary, spaces=2, padding_value=35): # DUPLICATE, DELETE ME LATER ONE I REORGANIZE MY CODE
    try:
        for key, value in dictionary.items():
            if isinstance(value, dict):  # Check if value is a nested dictionary
                print(f"\n{' ' * spaces}{key} :")
                print_character(value, spaces + 2)  # recursively call the function to handle nested dictionary
            elif isinstance(value, list):  
                print(f"{' ' * spaces}{key} :")
                list_space = spaces -1
                for v in value:
                    print(f"{' ' * (padding_value + list_space)}- {v}")
                print_character(value, spaces + 2)  # recursively call the function to handle nested dictionary
            else:
                padding = padding_value - spaces
                print(f"{' ' * spaces}{f'{key:<{padding}}'} : {value}")  # print key-value pair if value is not a nested dictionary
    except:
        print(f"{' ' * spaces}")

clear()

# directory_path = "./save_states/conversations"
# file_extension = ".pkl"

# # Get list of files in the directory
# files_in_directory = os.listdir(directory_path)

# # Filter out files with the specified file extension
# pickle_files = [file for file in files_in_directory if file.endswith(file_extension)]

# if pickle_files:
#     print("Previous save states detected:")
#     # for index, pickle_file in enumerate(pickle_files):
#     #     print(f"{index + 1}. {pickle_file}")

#     print("\n\033[91mSelect a file to load or start a new conversation:\033[0m")
    
#     # Add option to start a new conversation
#     menu_options = pickle_files + ['Start new conversation']
#     menu = TerminalMenu(menu_options)
#     selected_index = menu.show()

#     if selected_index < len(pickle_files):
#         # User selected a pickle file
#         selected_file = pickle_files[selected_index]
#         character_memory = pickle_handler.load_pkl_file(selected_file, directory_path)
#     else:
#         # User selected 'Start new conversation'
#         character_memory = {
#             "Description": "This is a description",
#             "Background": "This is a background",
#             "Attributes": "This is an attribute",
#         }
#         clear()
# else:
#     print("No previous save states found.")
#     # Additional code to start a new conversation


npc_salutations = [
    "What do you want to talk about?",
    "Greetings, traveler!",
    "Well met, adventurer.",
    "Hail and well met!",
    "Good day to you.",
    "Ah, a new face in these parts!",
    "Welcome, welcome!",
    "Salutations, esteemed guest.",
    "Ahoy there!",
    "Good to see a new face around here.",
    "Blessings upon you.",
    "A hearty hello to you!",
    "May the winds be at your back.",
    "Ah, what brings you here today?",
    "Welcome to our humble abode.",
    "A pleasure to make your acquaintance.",
    "Ho there, wanderer!",
    "Greetings and salutations!",
    "Peace be upon you.",
    "Fortune favor you.",
    "Welcome, brave soul."
]

npc_follow_up_statements = [
    "Can I help you with anything else?",
    "Is there something else you're interested in?",
    "Do you have any other questions?",
    "Anything more I can do for you?",
    "Is there anything else you need?",
    "Would you like to know about something else?",
    "Any other inquiries or needs?",
    "Do you seek further assistance?",
    "Is there more you wish to ask?",
    "Anything else on your mind?",
    "Need more information on anything?",
    "Can I provide any additional help?",
    "Would you like any other guidance?",
    "Is there more you'd like to explore?",
    "Need assistance with something else?",
    "Any other matters to address?",
    "Would you like to inquire about something else?",
    "Can I be of further service?",
    "Is there anything else I can assist with?",
    "Do you have further questions?"
]



def conversation_with_npc(
        character_names=None,
        npc_name=None,
        npc_race=None,
        npc_class=None,
        npc_background=None,
        npc_salutations=npc_salutations,
        npc_follow_up_statements=npc_follow_up_statements,
        born_and_raised=None,
        current_residence=None,
        places_visited=None,
    ):

    import os
    import pickle
    from simple_term_menu import TerminalMenu

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    # Assuming pickle_handler is a module with a function to load pickle files
    # import pickle_handler 

    directory_path = "./save_states/conversations"
    file_extension = ".pkl"

    # Function to prompt for character details and filter files
    def filter_files_by_character(files, name, race, clazz):
        return [file for file in files if all(x in file for x in [name, race, clazz])]

    # Get list of files in the directory
    files_in_directory = os.listdir(directory_path)

    # Filter out files with the specified file extension
    pickle_files = [file for file in files_in_directory if file.endswith(file_extension)]

    # Filter files based on character details
    filtered_files = filter_files_by_character(pickle_files, npc_name, npc_race, npc_class)

    if filtered_files:
        print("Matching save states found:")
        menu_options = filtered_files + ['Start new conversation']
        menu = TerminalMenu(menu_options)
        selected_index = menu.show()

        if selected_index < len(filtered_files):
            selected_file = filtered_files[selected_index]
            character_memory = pickle_handler.load_pkl_file(selected_file, directory_path)
        else:
            character_memory = {
            }
            clear()

    else:
        print("No matching save states found. Starting a new conversation.")
        character_memory = {
            "Background": [npc_background],
            "Born_And_Raised": [dnd_towns_and_cities[born_and_raised].copy()],
            "Current_Residence": [dnd_towns_and_cities[current_residence].copy()],
            "Places_Visited": [", ".join(places_visited)],
        }
        clear()


    def ensure_punctuation(s, default_punctuation='.'):
        if s and s[-1] not in string.punctuation:
            s += default_punctuation
        return s


    def conversation_with_npc_using_chatgpt(topic, memory):
        if topic == None:
            character_memory[character_topic_response.title()] = []
            character_topic_memory = character_memory[character_topic_response.title()]
        else:
            if topic not in character_memory.keys():
                new_topic = f"{character_topic_response.title()}_{topic}"
                character_memory[new_topic] = []
                character_topic_memory = character_memory[new_topic]

                character_speaking = terminalmenu_quick_select(character_names, f"Who's speaking? ")
                character_says = f"{character_speaking}: Asks about '{character_topic_response.title()}' and '{topic}'."
                print(character_says)
                character_topic_memory.append(character_says)
                pickle_handler.save_dnd_state(f"{npc_name} the {npc_race} {npc_class}", character_memory, "./save_states/conversations")
                relevant_character_knowledge = memory
                character_says = f"""
Take on the persona of a DnD 5e chararcter that is a {npc_race} {npc_class} who {npc_background}.
Converstaion History:
{character_topic_memory}
Relavant character knowledge:
{relevant_character_knowledge}
Be brief and prefix response with "{npc_race} {npc_class}: "
"""
                chatgpt_npc_response = query_chatgpt(openai_key, character_says)
                print(chatgpt_npc_response)
                character_topic_memory.append(str(chatgpt_npc_response))
                pickle_handler.save_dnd_state(f"{npc_name} the {npc_race} {npc_class}", character_memory, "./save_states/conversations")

            else:
                character_memory[topic] = memory
                character_topic_memory = character_memory[topic]

        continue_chat = True
        while continue_chat == True:
            print(f"Let's start a new conversation.")
            character_speaking = terminalmenu_quick_select(character_names, f"Who's speaking? ")
            if character_speaking == "Exit":
                character_says = f"Okay, goodbye."
                character_says = character_says.capitalize()
                character_says = ensure_punctuation(character_says)
                if len(character_names) == 1:
                    character_says = f"{character_names[0]}: {character_says}"
                else:
                    character_says = f"The Party: {character_says}"

                character_topic_memory.append(character_says)
                continue_chat = False
                break 

            character_says = input(f"{character_speaking}: ")
            if character_says.lower() == '' or character_says.lower() == None:
                pass
            else:
                character_says = character_says.capitalize()
                character_says = ensure_punctuation(character_says)

                character_says = f"{character_speaking}: {character_says}"
                character_topic_memory.append(character_says)
                pickle_handler.save_dnd_state(f"{npc_name} the {npc_race} {npc_class}", character_memory, "./save_states/conversations")

                character_says = f"""
Take on the persona of a DnD 5e chararcter that is a {npc_race} {npc_class} who {npc_background}.
Converstaion History:
{character_topic_memory}
Be brief and prefix response with "{npc_race} {npc_class}: "
"""
                chatgpt_npc_response = query_chatgpt(openai_key, character_says)
                print(chatgpt_npc_response)
                character_topic_memory.append(chatgpt_npc_response)
                pickle_handler.save_dnd_state(f"{npc_name} the {npc_race} {npc_class}", character_memory, "./save_states/conversations")



    continue_converstation = True
    converstaion_count = 0
    while continue_converstation == True:

        def memory_recall(text, state):
            text_lower = text.lower()
            options = [key for key in character_memory.keys() if text_lower in key.lower()]
            if state < len(options):
                return options[state]
            else:
                return None
            
        readline.set_completer(memory_recall)
        readline.parse_and_bind("tab: complete")


        while True:
            clear()
            character_speaking = terminalmenu_quick_select(character_names, f"Who's speaking? ")

            if character_speaking == "Exit":
                continue_converstation = False
                break
            if converstaion_count == 0:
                print(f"{npc_name}: {random.choice(npc_salutations)} What do you want to talk about?")
            else:
                print(f"{npc_name}: {random.choice(npc_follow_up_statements)}")
            print()
            print(f"Tab completion is supported to explore what the character knows or any previous converstaions.")
            print()

            character_topic_response = input(f"Use [Tab] or enter new Topic: ")
            character_topic_response = character_topic_response.lower()
            
            # Check if the entered item (in lowercase) is in the inventory
            lowercase_keys = [key.lower() for key in character_memory.keys()]
            # print(type(character_topic_response))
            if str(character_topic_response) not in lowercase_keys:
                clear()
                print(f"{npc_name}: I don't know anything about '{character_topic_response.title()}'...")
                print(f"Type 'exit' to quit the converstaion.")
                print()
                new_topic_response = terminalmenu_quick_select(['No','Yes'], f"Do you want to start a new converstaion about this?")
                if new_topic_response == "No":
                    pass
                elif new_topic_response == "Yes":
                    conversation_with_npc_using_chatgpt(topic=None,memory=None)

            elif character_topic_response in lowercase_keys:
                # clear()
                print(f"Recalling memory of conversation...\n")
                # Find the original key with matching lowercase version
                matching_key = list(character_memory.keys())[lowercase_keys.index(character_topic_response)]
                for exchange in character_memory[matching_key]:
                    if isinstance(exchange,dict):
                        topic = terminalmenu_quick_select(list(exchange.keys()), f"{matching_key} - What do you want to ask about? ")
                        memory = relevant_character_knowledge = character_memory[matching_key][0][topic]
                    else:
                        print(f"{exchange}")
                        print()
                        topic = matching_key
                        memory = character_memory[matching_key]
                conversation_with_npc_using_chatgpt(topic,memory)

                break
            else:
                print(f"[-] The character has no recollection of {character_topic_response}.")

if __name__ == '__main__':
    conversation_with_npc()