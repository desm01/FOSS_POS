from os import terminal_size
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import math

from Functions.initalise_buttons import initalise_buttons

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


        self.main_box.pack_start(initalise_buttons(parent, self.on_button_click), True, True, 0)

        
        self.show_all()

        
    def on_button_click(self, event, parent, item):
        
        parent.list_of_items.remove(item)
        item.make_invisible()
        parent.re_render_form()
        self.destroy()