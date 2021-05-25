import gi

import math

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

from Storage.get_items import get_items
from Storage.get_staff import get_staff

from Functions.checkout import checkout

from Functions.initalise_buttons import initalise_buttons
from Functions.remove_item_from_basket import clear_list_box
from Functions.add_item_to_total import add_to_total


from Objects.column import Column
from Objects.button import Button
from Objects.alert import alert_messagebox


from GUI.Forms.add_item_window import add_item_window
from GUI.Forms.show_buttons_window import show_buttons_window
from GUI.Forms.sign_on_screen import sign_on_screen

from GUI.Forms.settings_window import settings_window
from GUI.Forms.show_items_in_basket import show_items_in_basket


class build_main_form(Gtk.Window):
    def __init__(self):
        
        Gtk.Window.__init__(self, title = "EPOS Software")
        
 


        self.current_basket = []
        self.sign_on = False

        self.total = 0
        self.fullscreen()

        self.render_form()


       

    def render_form(self):
        try:
            self.grid.destroy()
        except:
            print("Grid Not Made")
        self.grid = Gtk.Grid()

        self.list_of_items = get_items()
        self.list_of_staff = get_staff()

        self.Special_Buttons_Box = Column(Gtk.Orientation.VERTICAL)
        self.Total_Box = Column(Gtk.Orientation.VERTICAL)
        self.PLU_Box = Column(Gtk.Orientation.VERTICAL)
  

        self.populate_box_for_special_button()
        self.populate_total_box()
        self.populate_PLU_box()

        self.grid.add(self.Special_Buttons_Box.box)
        self.grid.attach_next_to(self.scroll_bar, self.Special_Buttons_Box.box, Gtk.PositionType.RIGHT, 1,1)
        self.grid.attach_next_to(self.PLU_Box.box, self.scroll_bar, Gtk.PositionType.RIGHT, 1, 1)
    

        self.add(self.grid)
        
        self.show_all()

    def populate_box_for_special_button(self):
        self.create_sign_on_button()
        self.create_checkout_button()
        self.create_modify_button()
        self.create_add_item_button()
        self.create_remove_from_basket_button()
        self.create_clear_basket_button()
        self.create_settings_button()

    def create_clear_basket_button(self):
        clear_basket_button = Button("Clear Basket", self.clear_basket_handler)
        self.Special_Buttons_Box.add(clear_basket_button.button)

    def create_remove_from_basket_button(self):
        remove_from_basket_button = Button("Remove From Basket", self.remove_from_basket_handler)
        self.Special_Buttons_Box.add(remove_from_basket_button.button)


    def create_settings_button(self):
        setting_button = Button("Settings", self.settings_handler)
        self.Special_Buttons_Box.add(setting_button.button)


    def create_sign_on_button(self):
        sign_on_button = Button("Sign On", self.sign_on_handler)
        self.Special_Buttons_Box.add(sign_on_button.button)


    def create_modify_button(self):
        modify_button = Button("Modify Item", self.modify_button_handler)
        self.Special_Buttons_Box.add(modify_button.button)


    def create_checkout_button(self):
        checkout_button = Button("Checkout", self.checkout_handler)
        self.Special_Buttons_Box.add(checkout_button.button)

    def create_add_item_button(self):
        add_item_button = Button("Add New Item", self.add_new_item_handler)
        self.Special_Buttons_Box.add(add_item_button.button)

    def populate_total_box(self):

        # Create List Box
        # Add Label
        self.list_box = Gtk.ListBox(hexpand = True, vexpand = True)
        lbl = Gtk.Label(label = "Current Basket")
        self.list_box.prepend(lbl)
        
        # Add ListBox to Column

        self.Total_Box.add(self.list_box)

        # Make Column scrollable
        self.scroll_bar = Gtk.ScrolledWindow()
        self.scroll_bar.add(self.Total_Box.box)


    def populate_PLU_box(self):
        self.PLU_Box.add(initalise_buttons(self, add_to_total))

    def clear_basket_handler(self, button_event):
        if len(self.current_basket) == 0:
            alert_messagebox("Sorry, your basket is empty")
           # window.show_all()

        else:

            clear_list_box(self)
            self.current_basket.clear()
            self.re_render_form()

    def settings_handler(self, button_event):
        self.settings_window = settings_window(self)
        self.settings_window.show_all()
        self.settings_window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)

    def sign_on_handler(self, button_event):
        self.sign_on_screen = sign_on_screen(self)
        self.sign_on_screen.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.sign_on_screen.show_all()

    def modify_button_handler(self, button_event):
        self.modify_window = show_buttons_window(self)
        self.modify_window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.modify_window.show_all()

    def add_new_item_handler(self, button_event):
        self.add_item_window = add_item_window(self, self.list_of_items)
        self.add_item_window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.add_item_window.show_all()

    def remove_from_basket_handler(self, button_event):
        show_items_in_basket(self, self.current_basket)
        
    def checkout_handler(self, button_event):
        if self.sign_on:
            checkout( self.current_basket)
         #   new_purchase = Purchase(current_basket, self.staff_member, self.staff_member)
            
            clear_list_box(self)
            self.current_basket.clear()
        else:
            alert_messagebox("You are not signed on yet")
            

