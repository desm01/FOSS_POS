from GUI.Forms.add_customer_window import add_customer_window
from re import T
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Storage.get_customers import get_customers
from Functions.display_checkout import display_checkout


class select_customer_window(Gtk.Window):

    def __init__(self, item_list):
        Gtk.Window.__init__(self, title = "Select Customer")

        self.fullscreen()

        self.item_list = []
        self.item_list += item_list

        label = Gtk.Label(label = "Enter Email Address")

        self.email_entry = Gtk.Entry()

        self.box = Gtk.Box(spacing = 10, orientation = Gtk.Orientation.VERTICAL)

        self.box.pack_start(label, True, True, 0)

        search_button = Gtk.Button("Search")
        search_button.connect("clicked", self.search_handler)

        self.add_account_button()
        self.create_cancel_button()

        hBox = Gtk.Box()

        hBox.pack_start(self.email_entry, True, True, 0)
        hBox.pack_start(search_button, True, True, 0) 

        self.box.pack_start(hBox, True, True, 0)

        self.add(self.box)

        self.show_all()

    def search_handler(self, button_event):
        list_of_customers = get_customers()

        email_address = self.email_entry.get_text()

        for i in range(0, len(list_of_customers)):
            if list_of_customers[i].email_address == email_address:
                self.create_button(list_of_customers[i])
                break


    def create_button(self, customer):
        button = Gtk.Button(label = customer.name)
        button.connect("clicked", self.on_button_click, customer)

        self.box.pack_start(button, True, True, 0)
        self.show_all()

    def on_button_click(self, button_event, customer):
        display_checkout(self.item_list)
        self.destroy()

    def create_cancel_button(self):
        cancel_button = Gtk.Button(label = "Cancel")
        cancel_button.connect("clicked", self.cancel_handler)

        self.box.pack_start(cancel_button, True, True, 0)
    
    def cancel_handler(self, button_event):
        display_checkout(self.item_list)
        self.destroy()

    def add_account_button(self):
        add_account_button = Gtk.Button(label = "Add Customer")
        add_account_button.connect("clicked", self.add_account_button_handler)

        self.box.pack_start(add_account_button, True, True, 0)

    def add_account_button_handler(self, button_event):
        win = add_customer_window(self.item_list)
        win.show_all()
        self.destroy()
