import gi
gi.require_version("Gtk", "3.0")

from Objects.staff import Staff

from GUI.passcode_screen import passcode_screen

from gi.repository import Gtk

import math

class sign_on_screen(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Sign On Screen")
        
        self.fullscreen()
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
                button.connect("clicked", self.button_click_handler, list_of_staff[item_counter], parent )

                new_row.pack_start(button, True, True, 0)
                item_counter = item_counter + 1

            self.box.pack_start(new_row, True, True, 0)


     
     #   self.set_default_size(150, 200)
        self.add(self.box)
        self.show_all()

    
    def button_click_handler(self, button_event, staff, parent):

        self.passcode_screen = passcode_screen(parent, staff)
        self.passcode_screen.set_position(Gtk.WindowPosition.CENTER_ALWAYS)


    