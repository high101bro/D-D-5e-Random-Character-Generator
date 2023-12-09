#! /usr/bin/env python3

import os
import pickle


def find_pkl_files(directory='./save_states'):
    return [file for file in os.listdir(directory) if file.endswith('.pkl')]

def load_pkl_file(file_path, directory='./save_states'):
    with open(f"{directory}/{file_path}", 'rb') as file:
        return pickle.load(file)

def select_and_load_pkl(directory="./save_states"):
    pkl_files = find_pkl_files(directory)
    if not pkl_files:
        print("No .pkl files found in the current directory.")
        return None

    print("Found the following .pkl files:")
    for i, file in enumerate(pkl_files, 1):
        print(f"{i}. {file}")

    choice = int(input("Enter the number of the file you want to load: ")) - 1
    if 0 <= choice < len(pkl_files):
        return load_pkl_file(pkl_files[choice], directory)
    else:
        print("Invalid selection.")
        return None

def save_dnd_state(name, save_this, directory='./save_states'):
    # Serializing the list of objects
    with open(f"{directory}/{name}.pkl", 'wb') as outp:  # Writing in binary mode
        pickle.dump(save_this, outp, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    data = select_and_load_pkl()
    if data is not None:
        print("Data loaded from file:", data)
