import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def create_total_box(self):
        # Create List Box
        # Add Label
    self.list_box = Gtk.ListBox(hexpand = True, vexpand = True)
    lbl = Gtk.Label(label = "Current Basket")
    self.list_box.prepend(lbl)
        
    # Add ListBox to Column

    self.Total_Box.add(self.list_box)

    # Make Column scrollable
    self.scroll_bar = Gtk.ScrolledWindow()
    self.scroll_bar.add(self.Total_Box.box)