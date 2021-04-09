import gi
gi.require_version("Gtk", "3.0")

from Objects.item import Item
from GUI.MessageBoxes.alert_messagebox import alert_messagebox
from Functions.check_if_item_is_correct import check_if_new_item_is_correct
from Storage.store_items import store_items

from gi.repository import Gtk

class modify_button_window(Gtk.Window):
    def __init__(self, parent, item):
        Gtk.Window.__init__(self, title = "Change Price")

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
        box.pack_start(submit_button, True, True, 0)

        self.add(box)

    def submit_handler(self, button_event, parent, item):
        try:
            new_name = self.name_entry.get_text()
            new_price = float (self.price_entry.get_text())
            new_quantity = float(self.quantity_entry.get_text())
            new_plu_number = float(self.plu_number_entry.get_text())
            new_item_type = self.item_type_entry.get_text()
            new_category = self.item_type_category_entry.get_text()

            new_item = Item(new_name, new_price, new_quantity, new_plu_number, new_item_type, new_category)
        
            if check_if_new_item_is_correct(new_item) == True:
                item.update(new_item)
                store_items(parent.list_of_items)


            else:
                dialog = alert_messagebox("Error, the fields have been incorrectly filled out")
                response = dialog.run()
                dialog.destroy()


        except:
            dialog = alert_messagebox("Error, the items have been incorrectly formated")
            response = dialog.run()
            dialog.destroy()


        

        
        self.destroy()
