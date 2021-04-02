import gi
gi.require_version("Gtk", "3.0")

from Objects.item import Item
from Objects.staff import Staff

from gi.repository import Gtk

class settings_window(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Settings")
