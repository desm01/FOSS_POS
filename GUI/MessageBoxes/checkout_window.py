import gi
gi.require_version("Gtk", "3.0")
import sys
import os
sys.path.append(os.path.abspath('./Objects'))
import item as Item

from gi.repository import Gtk

class checkout_window(Gtk.Dialog):
    def __init__(self, checkout_text):
        Gtk.Dialog.__init__(self, title = "Checkout")

        self.add_buttons(
            Gtk.STOCK_OK, Gtk.ResponseType.OK
        )

        self.set_default_size(250, 250)

        label = Gtk.Label(label = checkout_text)

        box = self.get_content_area()
        box.add(label)
        self.show_all()

