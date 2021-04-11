import gi
gi.require_version("Gtk", "3.0")
import math
from gi.repository import Gtk

from GUI.modify_staff_window import modify_staff_member_window

class show_staff_window(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Show Staff Members")
        
        self.fullscreen()
        
        self.box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)

        label = Gtk.Label(label = "Select the member of staff you wish to modify")
        self.set_up_buttons(parent)

        self.add(self.box)

        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.resize(200,150)

        self.show_all()
    
    def set_up_buttons(self, parent):

        number_of_rows_to_create = len(parent.list_of_staff)
        number_of_rows_to_create = math.ceil(number_of_rows_to_create / 5)

        item_counter = 0

        for row in range (0, number_of_rows_to_create):
            new_row = Gtk.Box()
            new_row.set_homogeneous(True)
            for i in range(0,5):
                if item_counter == len(parent.list_of_staff):
                    break
                button = Gtk.Button(label = parent.list_of_staff[item_counter].name)
                button.connect("clicked", self.on_click, parent.list_of_staff [item_counter], parent )

                new_row.pack_start(button, True, True, 0)
                item_counter = item_counter + 1

            self.box.pack_start(new_row, True, True, 0)


        
        self.show_all()

    def on_click(self, button_event, staff, parent):
        window = modify_staff_member_window(staff, parent)
        window.show_all()
        window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.destroy()