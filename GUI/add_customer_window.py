import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Storage.store_customers import add_new_customer
from Objects.customer import Customer
import datetime
import re


class add_customer_window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Add Customer")

        self.fullscreen()

        box = Gtk.Box(spacing = 10, orientation = Gtk.Orientation.VERTICAL)

        self.set_border_width(25)

        name_label = Gtk.Label(label = "Name:")
        self.name_entry = Gtk.Entry()

        address_label = Gtk.Label(label = "Address:")
        self.address_entry = Gtk.Entry()

        date_of_birth_label = Gtk.Label(label = "Date Of Birth:")
        self.date_of_birth_entry = Gtk.Entry()

        email_address_label = Gtk.Label(label = "Email Address:")
        self.email_entry = Gtk.Entry()

        phone_number_label = Gtk.Label(label = "Phone Number:")
        self.phone_number_entry = Gtk.Entry()

        back_button = Gtk.Button(label = "Back")
        back_button.connect("clicked", self.back_handler)

        submit_button = Gtk.Button(label = "Submit")
        submit_button.connect("clicked", self.submit_handler)

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

        hBox = Gtk.Box()

        hBox.pack_start(back_button, True, True, 0)
        hBox.pack_start(submit_button, True, True, 0)

        box.pack_start(hBox, True, True, 0)

        self.add(box)


    def back_handler(self, button_event):
        self.destroy()

    def submit_handler(self, button_event):

        customer_name = self.name_entry.get_text()
        address = self.address_entry.get_text()
        date_of_birth = self.date_of_birth_entry.get_text()
        email_address = self.email_entry.get_text()
        phone_number = self.phone_number_entry.get_text()

        if self.check_date_of_birth(date_of_birth):
            if self.check_phone_number_is_correct(phone_number):

                new_customer = Customer(customer_name, address, date_of_birth, email_address, phone_number)
                add_new_customer(new_customer)
                print("Submitting")

                self.destroy()

    def check_date_of_birth(self, date_of_birth):
        try:
            datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
            return True
        except ValueError:
            return False
            #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
            

    def check_phone_number_is_correct(self, phone_number):

        for i in range (0, len(phone_number)):
            if not re.match("[0-9]", phone_number[i]):
                return False
        return True 
