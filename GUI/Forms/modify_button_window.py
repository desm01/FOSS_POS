import gi
gi.require_version("Gtk", "3.0")


from gi.repository import Gtk

from Functions.modify_item import modify_item


class modify_button_window(Gtk.Window):
    def __init__(self, parent, item):
        Gtk.Window.__init__(self, title = "Change Price")

        self.set_border_width(25)

        self.fullscreen()

        box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)
        
        name_label = Gtk.Label("Name:")
        self.name_entry = Gtk.Entry()
        self.name_entry.set_text(item.name)

        price_label = Gtk.Label("Price:")
        self.price_entry = Gtk.Entry()
        self.price_entry.set_text(str(item.price))

        quantity_label = Gtk.Label("Quantity:")
        self.quantity_entry = Gtk.Entry()
        self.quantity_entry.set_text(str(item.quanitity))

        plu_number_label = Gtk.Label("PLU Number:")
        self.plu_number_entry = Gtk.Entry()
        self.plu_number_entry.set_text(str(item.pluNumber))

        item_type_label = Gtk.Label("Item Type:")
        self.item_type_entry = Gtk.Entry()
        self.item_type_entry.set_text(item.itemType)

        item_type_category_label = Gtk.Label("Category")
        self.item_type_category_entry = Gtk.Entry()
        self.item_type_category_entry.set_text(item.category)

        submit_button = Gtk.Button(label = "Submit")
        submit_button.connect("clicked", self.submit_handler ,parent, item)

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

    def submit_handler(self, button_event, parent, item):
        modify_item(self, parent, item)


