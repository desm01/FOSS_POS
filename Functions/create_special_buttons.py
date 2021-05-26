import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Functions.remove_item_from_basket import clear_list_box
from Functions.checkout import checkout

from Objects.button import Button
from Objects.alert import alert_messagebox

from GUI.Forms.add_item_window import add_item_window
from GUI.Forms.show_buttons_window import show_buttons_window
from GUI.Forms.sign_on_screen import sign_on_screen

from GUI.Forms.settings_window import settings_window
from GUI.Forms.show_items_in_basket import show_items_in_basket

def create_special_buttons(self):
    create_sign_on_button(self)
    create_checkout_button(self)
    create_modify_button(self)
    create_add_item_button(self)
    create_remove_from_basket_button(self)
    create_clear_basket_button(self)
    create_settings_button(self)

def create_clear_basket_button(self):
    clear_basket_button = Button("Clear Basket", clear_basket_handler, self)
    self.Special_Buttons_Box.add(clear_basket_button.button)

def create_remove_from_basket_button(self):
    remove_from_basket_button = Button("Remove From Basket", remove_from_basket_handler, self)
    self.Special_Buttons_Box.add(remove_from_basket_button.button)


def create_settings_button(self):
    setting_button = Button("Settings", settings_handler, self)
    self.Special_Buttons_Box.add(setting_button.button)


def create_sign_on_button(self):
    sign_on_button = Button("Sign On", sign_on_handler, self)
    self.Special_Buttons_Box.add(sign_on_button.button)


def create_modify_button(self):
    modify_button = Button("Modify Item", modify_button_handler, self)
    self.Special_Buttons_Box.add(modify_button.button)


def create_checkout_button(self):
    checkout_button = Button("Checkout", checkout_handler, self)
    self.Special_Buttons_Box.add(checkout_button.button)

def create_add_item_button(self):
    add_item_button = Button("Add New Item", add_new_item_handler, self)
    self.Special_Buttons_Box.add(add_item_button.button)


def clear_basket_handler(button_event, self):
    if len(self.current_basket) == 0:
        alert_messagebox("Sorry, your basket is empty")
           # window.show_all()

    else:
        clear_list_box(self)
        self.current_basket.clear()
        self.render_form()

def settings_handler(button_event, self):
    self.settings_window = settings_window(self)
    self.settings_window.show_all()
    self.settings_window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)

def sign_on_handler(button_event, self):
    self.sign_on_screen = sign_on_screen(self)
    self.sign_on_screen.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
    self.sign_on_screen.show_all()

def modify_button_handler(button_event, self):
    self.modify_window = show_buttons_window(self)
    self.modify_window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
    self.modify_window.show_all()

def add_new_item_handler(button_event, self):
    self.add_item_window = add_item_window(self, self.list_of_items)
    self.add_item_window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
    self.add_item_window.show_all()

def remove_from_basket_handler(button_event, self):
    show_items_in_basket(self, self.current_basket)
        
def checkout_handler(button_event, self):
    if self.sign_on:
        checkout(self.current_basket)
         #   new_purchase = Purchase(current_basket, self.staff_member, self.staff_member)
            
        clear_list_box(self)
        self.current_basket.clear()
    else:
        alert_messagebox("You are not signed on yet")
