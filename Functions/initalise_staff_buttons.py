import math

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def initalise_staff_button(self, parent, event):
    self.box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)
    list_of_staff = parent.list_of_staff

    number_of_rows_to_create = len(list_of_staff)
    number_of_rows_to_create = math.ceil(number_of_rows_to_create / 5)

    item_counter = 0

    for row in range (0, number_of_rows_to_create):
        new_row = Gtk.Box()
        new_row.set_homogeneous(True)
        for i in range(0,5):
            if item_counter == len(list_of_staff):
                break
            button = Gtk.Button(label = list_of_staff[item_counter].name)
            button.connect("clicked", event, list_of_staff[item_counter], parent )

            new_row.pack_start(button, True, True, 0)
            item_counter = item_counter + 1

        self.box.pack_start(new_row, True, True, 0)