import math

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def create_item_buttons(parent, event):
    number_of_rows_to_create = len(parent.list_of_items)
    number_of_rows_to_create = math.ceil(number_of_rows_to_create / 5)

    main_box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)

    item_counter = 0

    for row in range (0, number_of_rows_to_create):
        new_row = Gtk.Box()
        new_row.set_homogeneous(True)
        for i in range(0,5):
            if item_counter == len(parent.list_of_items):
                break
            button = Gtk.Button(label = parent.list_of_items[item_counter].name)


            
            button.connect("clicked", event, parent, parent.list_of_items[item_counter] )

            new_row.pack_start(button, True, True, 0)
            item_counter = item_counter + 1

        main_box.pack_start(new_row, True, True, 0)
    
    return main_box
