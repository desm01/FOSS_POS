import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class alert_messagebox(Gtk.Dialog):
    def __init__(self, text_to_display):
        Gtk.Dialog.__init__(self, title = "ALERT")

        self.add_buttons(
            Gtk.STOCK_OK, Gtk.ResponseType.OK
        )

        label = Gtk.Label(label = text_to_display)

        self.set_default_size(250,250)
        box = self.get_content_area()
        box.add(label)
        self.show_all()