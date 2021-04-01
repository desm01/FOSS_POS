import gi
gi.require_version("Gtk", "3.0")

import sys
import os
sys.path.append(os.path.abspath('./Objects'))
import item as Item

from gi.repository import Gtk


class add_item_window(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Add New Item")



