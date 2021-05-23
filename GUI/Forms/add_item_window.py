from GUI.MessageBoxes.alert_messagebox import alert_messagebox
from Functions.add_new_item import add_new_item
import gi
gi.require_version("Gtk", "3.0")

from Objects.item import Item


from gi.repository import Gtk




class add_item_window(Gtk.Window):
    def __init__(self, parent, list_of_items):
        Gtk.Window.__init__(self, title = "Add New Item")
        box = Gtk.Box(spacing = 10, orientation = Gtk.Orientation.VERTICAL)
        
        self.set_border_width(25)

        self.fullscreen()

        name_label = Gtk.Label("Name:")
        self.name_entry = Gtk.Entry()

        price_label = Gtk.Label("Price:")
        self.price_entry = Gtk.Entry()

        quantity_label = Gtk.Label("Quantity:")
        self.quantity_entry = Gtk.Entry()

        plu_number_label = Gtk.Label("PLU Number:")
        self.plu_number_entry = Gtk.Entry()

        item_type_label = Gtk.Label("Item Type:")
        self.item_type_entry = Gtk.Entry()

        item_type_category_label = Gtk.Label("Category")
        self.item_type_category_entry = Gtk.Entry()

        submit_button = Gtk.Button(label = "Submit")
        submit_button.connect("clicked", self.submit_handler, parent, list_of_items)

        back_button = Gtk.Button(label = "Back")
        back_button.connect("clicked", self.back_handler)

        box.pack_start(name_label, True, True, 0)
        box.pack_start(self.name_entry, True, True, 0)
        box.pack_start(price_label, True, True, 0)
        box.pack_start(self.price_entry, True, True, 0)
        box.pack_start(quantity_label, True, True, 0)
        box.pack_start(self.quantity_entry, True, True, 0)
        box.pack_start(plu_number_label, True, True, 0)
        box.pack_start(self.plu_number_entry, True, True, 0)
        box.pack_start(item_type_label, True, True, 0)
        box.pack_start(self.item_type_entry, True, True, 0)
        box.pack_start(item_type_category_label, True, True, 0)
        box.pack_start(self.item_type_category_entry, True, True, 0)

        hBox = Gtk.Box()

        hBox.pack_start(back_button, True, True, 25)
        hBox.pack_start(submit_button, True, True, 25)

        box.pack_start(hBox, True, True, 10)

        self.add(box)

    def back_handler(self, button_event):
        self.destroy()

    def submit_handler(self,button_event, parent, list_of_items):
        add_new_item(self, parent)

            


