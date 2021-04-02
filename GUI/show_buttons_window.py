import gi
gi.require_version("Gtk", "3.0")

import sys
import os
sys.path.append(os.path.abspath('./Objects'))
import item as Item

from gi.repository import Gtk

from GUI.modify_button_window import modify_button_window

class show_buttons_window(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Current Items")
        self.box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)
        label = Gtk.Label(label = "Select the item you wish to modify")
        self.box.pack_start(label, True, True, 0)

        self.set_up_buttons(parent)
        self.add(self.box)

    def set_up_buttons(self, parent):
        for item in parent.list_of_items:
            button = Gtk.Button(item.name)
            button.connect("clicked", self.on_button_click, parent, item, self)
            self.box.pack_start(button, True, True, 0)

        self.show_all()

        
    def on_button_click(button, event, parent, item, self):
        window = modify_button_window(parent, item)
        window.show_all()
        window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)

        self.destroy()