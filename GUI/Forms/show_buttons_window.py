from os import terminal_size
import gi
gi.require_version("Gtk", "3.0")

from Objects.item import Item

from gi.repository import Gtk

from Functions.initalise_buttons import initalise_buttons

from GUI.Forms.modify_button_window import modify_button_window

class show_buttons_window(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Current Items")
        self.main_box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)
        label = Gtk.Label(label = "Select the item you wish to modify")
        self.main_box.pack_start(label, True, True, 0)

        self.fullscreen()
        self.set_up_buttons(parent)

    def set_up_buttons(self, parent):
        self.add(initalise_buttons(parent, self.on_button_click))
        
        self.show_all()

        
    def on_button_click(self, event, parent, item):
        window = modify_button_window(parent, item)
        window.show_all()
        window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)

        self.destroy()