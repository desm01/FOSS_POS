from os import terminal_size
import gi
gi.require_version("Gtk", "3.0")

from Objects.item import Item

from gi.repository import Gtk

import math

class show_item_window(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Current Items")
        self.main_box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)
        label = Gtk.Label(label = "Select the item you wish to delete")
        self.main_box.pack_start(label, True, True, 0)

        self.fullscreen()
        self.set_up_buttons(parent)
        self.add(self.main_box)

    def set_up_buttons(self, parent):

        number_of_rows_to_create = len(parent.list_of_items)
        number_of_rows_to_create = math.ceil(number_of_rows_to_create / 5)

        item_counter = 0

        for row in range (0, number_of_rows_to_create):
            new_row = Gtk.Box()
            new_row.set_homogeneous(True)
            for i in range(0,5):
                if item_counter == len(parent.list_of_items):
                    break
                button = Gtk.Button(label = parent.list_of_items[item_counter].name)
                button.connect("clicked", self.on_button_click, parent, parent.list_of_items[item_counter], self )

                new_row.pack_start(button, True, True, 0)
                item_counter = item_counter + 1

            self.main_box.pack_start(new_row, True, True, 0)


        
        self.show_all()

        
    def on_button_click(button, event, parent, item, self):
        
        parent.list_of_items.remove(item)
        item.make_invisible()
        parent.render_buttons()
        self.destroy()