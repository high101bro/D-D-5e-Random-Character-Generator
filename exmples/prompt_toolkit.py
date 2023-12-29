#! /usr/bin/env python3


from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

colors_completer = WordCompleter(['red', 'green', 'blue', 'yellow'], ignore_case=True)

def get_color():
    color = prompt('Enter your favorite color: ', completer=colors_completer)
    print(f'You chose: {color}')

get_color()
