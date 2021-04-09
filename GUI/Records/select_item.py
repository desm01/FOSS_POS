import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Storage.get_items import get_items
from GUI.Records.show_records_where_item_window import show_records_where_item_window

class select_item(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Select Item To View Records")
        
        list_of_items = get_items()
        list_box = Gtk.Box(spacing = 0,  orientation = Gtk.Orientation.VERTICAL)

        for item in list_of_items:
            button = Gtk.Button(label = item.name)
            button.connect("clicked", self.on_click, item)
            list_box.pack_start(button, True, True, 0)

        self.add(list_box)

        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_size_request(700,400)
        self.show_all()

    def on_click(self, button_event, item):
        win = show_records_where_item_window(item)