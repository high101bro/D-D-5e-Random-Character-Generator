#!/usr/bin/env python3

from simple_term_menu import TerminalMenu

# Example data
the_list = [1, 2, 3, 4]
the_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

def preview_item(menu_item):
    """
    Returns the preview string for the given menu item.
    """
    try:
        # Convert the menu item back to an integer to look it up in the_dict
        item = int(menu_item)
        return the_dict.get(item, "No preview available")
    except ValueError:
        return "Invalid item"

def main():
    terminal_menu = TerminalMenu(
        [str(item) for item in the_list],  # Convert items in the_list to strings for the menu
        preview_command=preview_item,  # Use preview_item function for previews
        preview_size=0.75
    )
    menu_entry_index = terminal_menu.show()

if __name__ == "__main__":
    main()
