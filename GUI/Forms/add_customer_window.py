
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Functions.add_new_customer import add_new_customer



class add_customer_window(Gtk.Window):

    def __init__(self, item_list):
        Gtk.Window.__init__(self, title = "Add Customer",)
        
    
        self.list_of_items = []
        self.list_of_items += item_list
        self.fullscreen()
       
        

        box = Gtk.Box(spacing = 10, orientation = Gtk.Orientation.VERTICAL)

        self.set_border_width(25)

        name_label = Gtk.Label(label = "Name:")
        self.name_entry = Gtk.Entry()

        address_label = Gtk.Label(label = "Address:")
        self.address_entry = Gtk.Entry()

        postcode_label = Gtk.Label(label = "Postcode:")
        self.postcode_entry = Gtk.Entry()

        date_of_birth_label = Gtk.Label(label = "Date Of Birth:")
        self.date_of_birth_entry = Gtk.Entry()

        email_address_label = Gtk.Label(label = "Email Address:")
        self.email_entry = Gtk.Entry()

        phone_number_label = Gtk.Label(label = "Phone Number:")
        self.phone_number_entry = Gtk.Entry()
        
        hBox = Gtk.Box()

        
        if len (item_list) == 0:
            back_button = Gtk.Button(label = "Back")
            back_button.connect("clicked", self.back_handler)
            hBox.pack_start(back_button, True, True, 0)

        submit_button = Gtk.Button(label = "Submit")
        submit_button.connect("clicked", self.submit_handler, self.list_of_items)

        box.pack_start(name_label, True, True, 0)
        box.pack_start(self.name_entry, True, True, 0)
        box.pack_start(address_label, True, True, 0)
        box.pack_start(self.address_entry, True, True, 0)
        box.pack_start(date_of_birth_label, True, True, 0)
        box.pack_start(self.date_of_birth_entry, True, True, 0)
        box.pack_start(email_address_label, True, True, 0)
        box.pack_start(self.email_entry, True, True, 0)
        box.pack_start(phone_number_label, True, True, 0)
        box.pack_start(self.phone_number_entry, True, True, 0)

      
        hBox.pack_start(submit_button, True, True, 0)

        box.pack_start(hBox, True, True, 0)

        self.add(box)


    def back_handler(self, button_event):
        self.destroy()

    def submit_handler(self, button_event, list_of_items):
        add_new_customer(self, list_of_items)

        