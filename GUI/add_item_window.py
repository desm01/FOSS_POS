from GUI.MessageBoxes.alert_messagebox import alert_messagebox
from Functions.check_if_item_is_correct import check_if_new_item_is_correct
import gi
gi.require_version("Gtk", "3.0")

from Objects.item import Item


from gi.repository import Gtk

from Storage.store_items import store_items


class add_item_window(Gtk.Window):
    def __init__(self, parent, list_of_items):
        Gtk.Window.__init__(self, title = "Add New Item")
        box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)
        
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

    def submit_handler(self,button_event, parent, list_of_items):

        
            name = self.name_entry.get_text()
            price = float (self.price_entry.get_text())
            quantity = float(self.quantity_entry.get_text())
            plu_number = float(self.plu_number_entry.get_text())
            item_type = self.item_type_entry.get_text()
            item_category = self.item_type_category_entry.get_text()

            if (self.check_if_item_already_exists( parent, name)):
                print("Item already exists")
        
            else:
                new_item = Item(name, price, quantity, plu_number, item_type, item_category)
                if check_if_new_item_is_correct(new_item):
                    parent.list_of_items.append(new_item)
                    parent.render_buttons()



            

            self.destroy()


    def check_if_item_already_exists(self, parent, name_of_item):
        for item in parent.list_of_items:
            if name_of_item == item.name:
                return True

        return False


