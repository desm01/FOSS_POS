from GUI.MessageBoxes.checkout_window import checkout_window

def display_checkout(item_list):
    if (len(item_list) == 0):
                return "Nothing in basket"

    else:
        checkout_text = format_text_for_checkout(item_list)
        run_checkout_window(checkout_text)

def format_text_for_checkout(item_list):
    list_of_items = ""
    total_cost_of_items = 0

    for item in item_list:
        list_of_items += "\n" + item.name
        total_cost_of_items += item.price

    string = list_of_items + "\n\n£" + "{:.2f}".format(total_cost_of_items)
    return string

def run_checkout_window(checkout_text):
    checkout_window(checkout_text)