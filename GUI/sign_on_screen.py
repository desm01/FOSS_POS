import gi
gi.require_version("Gtk", "3.0")
import sys
import os
sys.path.append(os.path.abspath('./Objects'))
import staff as Staff

from gi.repository import Gtk

class sign_on_screen(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Sign On Screen")
