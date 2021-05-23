from Functions.display_checkout import display_checkout

from Storage.store_customers import store_new_customer
from Objects.customer import Customer
from Objects.item import Item

import datetime
import re

def add_new_customer(self, list_of_items):
    customer_name = self.name_entry.get_text()
    address = self.address_entry.get_text()
    postcode = self.postcode_entry.get_text()
    date_of_birth = self.date_of_birth_entry.get_text()
    email_address = self.email_entry.get_text()
    phone_number = self.phone_number_entry.get_text()

    if check_date_of_birth(date_of_birth):
        if check_phone_number_is_correct(phone_number):

            new_customer = Customer(customer_name, address, postcode, date_of_birth, email_address, phone_number)
            store_new_customer(new_customer)
                
            print(list_of_items)

            if len(list_of_items) > 0:
                display_checkout(list_of_items)
                    

    self.destroy()

def check_date_of_birth(date_of_birth):
    try:
        datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
        return True
    except ValueError:
        return False
            #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
            

def check_phone_number_is_correct(phone_number):

    for i in range (0, len(phone_number)):
        if not re.match("[0-9]", phone_number[i]):
            return False
        return True 
