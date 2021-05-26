from os import terminal_size
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import math

from Objects.column import Column

from Functions.create_item_buttons import create_item_buttons

class show_item_window(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Current Items")
        self.main_box = Column(Gtk.Orientation.VERTICAL).box
        label = Gtk.Label(label = "Select the item you wish to delete")
        self.main_box.pack_start(label, True, True, 0)

        self.fullscreen()
        self.set_up_buttons(parent)
        self.add(self.main_box)

    def set_up_buttons(self, parent):

        buttons = create_item_buttons(parent, self.on_button_click)
        self.main_box.add(buttons)

        
        self.show_all()

        
    def on_button_click(self, event, parent, item):
        
        parent.list_of_items.remove(item)
        item.make_invisible()
        parent.render_form()
        self.destroy()