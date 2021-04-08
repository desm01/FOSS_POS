import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Queries.show_all_records import show_all_records

class show_all_records_window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Showing All Records")

        scrolled_window = Gtk.ScrolledWindow()

        self.set_border_width(10)

        list_box = Gtk.ListBox()

        records = show_all_records()

        for record in records:
            label = Gtk.Label(label = record.details())
            list_box.add(label)

        scrolled_window.add(list_box)
        self.add(scrolled_window)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_size_request(700,400)
        self.show_all()