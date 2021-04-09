import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Queries.show_records_where_item_was_purchased import show_records_where_item_was_purchased

class show_records_where_item_window(Gtk.Window):
    def __init__(self, item):
        Gtk.Window.__init__(self, title = "Where Item Was Sold")

        scrolled_window = Gtk.ScrolledWindow()

        self.set_border_width(10)

        list_box = Gtk.ListBox()

        records = show_records_where_item_was_purchased(item)

        for record in records:
            label = Gtk.Label(label = record.details())
            list_box.add(label)

        scrolled_window.add(list_box)
        self.add(scrolled_window)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_size_request(700,400)
        self.show_all()
