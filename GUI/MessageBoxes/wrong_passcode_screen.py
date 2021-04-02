import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class wrong_passcode_screen(Gtk.Dialog):
    def __init__(self):
        Gtk.Dialog.__init__(self, title = "Wrong Passcode")

        self.add_buttons(
            Gtk.STOCK_OK, Gtk.ResponseType.OK
        )

        label = Gtk.Label(label = "The passcode you have entered is incorrect")
        
        self.set_default_size(250, 250)
        box = self.get_content_area()
        box.add(label)
        self.show_all()
        