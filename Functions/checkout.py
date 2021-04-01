import sys
import os
sys.path.append(os.path.abspath('./Objects'))
import item as Item

from GUI.checkout_window import checkout_window


def checkout(item_list):
    if (len(item_list) == 0):
            return "Nothing in basket"

    else:
        checkout_text = format_text_for_checkout(item_list)
        display_checkout(checkout_text)
        
def format_text_for_checkout(item_list):
    list_of_items = ""
    total_cost_of_items = 0

    for item in item_list:
        list_of_items += "\n" + item.name
        total_cost_of_items += item.price

    string = list_of_items + "\n\n" + str (total_cost_of_items)
    return string

def display_checkout(checkout_text):
    dialog = checkout_window(checkout_text)
    response = dialog.run()
    dialog.destroy()