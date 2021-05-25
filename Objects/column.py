import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Column:

    def __init__(self, orientation):
        self.box = Gtk.Box(spacing = 0, orientation = orientation)

    def add(self, item):
        self.box.pack_start(item, True, True, 0)