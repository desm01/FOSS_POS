import gi

import math

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

from Storage.store_items import store_items
from Storage.get_items import get_items
from Storage.get_staff import get_staff

from Functions.checkout import checkout


from GUI.MessageBoxes.alert_messagebox import alert_messagebox
from GUI.MessageBoxes.wrong_passcode_screen import wrong_passcode_screen
from GUI.MessageBoxes.not_signed_on import not_signed_on

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

        self.create_form()

    def create_form(self):

        self.list_of_items = get_items()
        self.list_of_staff = get_staff()

        self.grid = Gtk.Grid()

        self.Special_Buttons_Box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)
        self.Total_Box = Gtk.VBox()
        self.PLU_Box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)
  

        self.populate_box_for_special_button()
        self.populate_total_box()
        self.populate_PLU_box()
  
        self.render_form()
       

    def render_form(self):
        self.grid.add(self.Special_Buttons_Box)
        self.grid.attach_next_to(self.scroll_bar, self.Special_Buttons_Box, Gtk.PositionType.RIGHT, 1,1)
        self.grid.attach_next_to(self.PLU_Box, self.scroll_bar, Gtk.PositionType.RIGHT, 1, 1)
    

        self.add(self.grid)
        
        self.show_all()

    def populate_box_for_special_button(self):
        self.initalise_sign_on_button()
        self.initalise_checkout_button()
        self.initalise_modify_button()
        self.initalise_add_item_button()
        self.initalise_remove_from_basket_button()
        self.initalise_clear_basket_button()
        self.initalise_settings_button()

    def populate_total_box(self):
        self.list_box = Gtk.ListBox(hexpand = True, vexpand = True)
        lbl = Gtk.Label(label = "Current Basket")
        self.list_box.prepend(lbl)
        
        self.Total_Box.pack_start(self.list_box,1 ,1, 0)

        self.scroll_bar = Gtk.ScrolledWindow()
        self.scroll_bar.add(self.Total_Box)


    def populate_PLU_box(self):
        number_of_rows_to_create = len(self.list_of_items) / 5
        number_of_rows_to_create = math.ceil(number_of_rows_to_create)

        item_counter = 0
        
        for row in range (0, number_of_rows_to_create):
            new_row = Gtk.HBox()
            new_row.set_homogeneous(True)
        
            for i in range(0,5):
                if item_counter == len(self.list_of_items):
                    break

                button = Gtk.Button(label = self.list_of_items[item_counter].name, expand = True)
                button.connect("clicked", self.add_to_total, self.list_of_items[item_counter])
                
                new_row.pack_start(button, True, True, 0)
                item_counter = item_counter + 1

            self.PLU_Box.pack_start(new_row, True, True, 0)


    def initalise_clear_basket_button(self):
        clear_basket_button = Gtk.Button(label = "Clear Basket")
        clear_basket_button.connect("clicked", self.clear_basket_handler)
        self.Special_Buttons_Box.pack_start(clear_basket_button, True, True, 0)

    def initalise_remove_from_basket_button(self):
        remove_from_basket_button = Gtk.Button(label = "Remove From Basket")
        remove_from_basket_button.connect("clicked", self.remove_from_basket_handler)
        self.Special_Buttons_Box.pack_start(remove_from_basket_button, True, True, 0)


    def initalise_settings_button(self):
        setting_button = Gtk.Button(label = "Settings", expand = True)
        setting_button.connect("clicked", self.settings_handler)
        self.Special_Buttons_Box.pack_start(setting_button, True, True, 0)


    def initalise_sign_on_button(self):
        sign_on_button = Gtk.Button(label = "Sign On", expand = True)
        sign_on_button.connect("clicked", self.sign_on_handler)
        self.Special_Buttons_Box.pack_start(sign_on_button, True, True, 0)

    def initalise_modify_button(self):
        modify_button = Gtk.Button(label = "Modify Item", expand = True)
        modify_button.connect("clicked", self.modify_button_handler)
        self.Special_Buttons_Box.add(modify_button)

    def initalise_checkout_button(self):
        checkout_button = Gtk.Button(label = "Checkout", expand = True)
        checkout_button.connect("clicked", self.checkout_handler)
        self.Special_Buttons_Box.pack_start(checkout_button, True, True, 0)

    def initalise_add_item_button(self):
        add_item_button = Gtk.Button(label = "Add New Item", expand = True)
        add_item_button.connect("clicked", self.add_new_item_handler)
        self.Special_Buttons_Box.pack_start(add_item_button, True, True, 0)

    def render_buttons(self):
        new_item = self.list_of_items[len(self.list_of_items) - 1]
        new_button = Gtk.Button(label = new_item.name, expand = True)
        new_button.connect("clicked", self.add_to_total, new_item )

        store_items(self.list_of_items)
        '''
        self.grid.destroy()
    
        self.create_form() 
        self.show_all()
        '''
        self.re_render_form()

    def clear_basket_handler(self, button_event):
        if len(self.current_basket) == 0:
            window = alert_messagebox("Sorry, your basket is empty")
           # window.show_all()

        else:

            self.clear_list_box()
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

    def user_has_signed_on(self, staff_member, entered_code):
        self.staff_member = staff_member
        self.sign_on_screen.destroy()
        if staff_member.passcode == entered_code:
            self.sign_on = True
            self.current_user = staff_member
            print ("User: " + staff_member.name + " has signed on")
        else:
            wrong_passcode_screen()
            

    def remove_from_basket(self, item_to_remove):
        for item in self.current_basket:
            if item == item_to_remove:
                self.current_basket.remove(item)
                break

        self.render_list_box()

    def remove_from_basket_handler(self, button_event):
        show_items_in_basket(self, self.current_basket)
        

    def checkout_handler(self, button_event):

        if self.sign_on:
            checkout( self.current_basket)
         #   new_purchase = Purchase(current_basket, self.staff_member, self.staff_member)
            
            self.clear_list_box()
            self.current_basket.clear()
        else:
            not_signed_on()
            

    def render_list_box(self):
        self.clear_list_box()

        basket = self.current_basket.copy()
        self.current_basket.clear()
        self.total = 0

        for item in basket:
            self.add_to_total("", item)
        

    def clear_list_box(self):
        for item in self.list_box:
            self.list_box.remove(item)

        
        
        label = Gtk.Label(label = "Current Basket:")
        self.total = 0
        self.list_box.add(label)
        self.show_all()

    def add_to_list_box(self, item_to_be_added, total_details):
        total_label = Gtk.Label(label = total_details)

        if(len (self.list_box) > 2):

            list_of_labels = self.list_box.get_children()
            final_index = len(list_of_labels) - 1
            label_to_be_removed = list_of_labels[final_index]
            
            self.list_box.remove(label_to_be_removed)
            
            label = Gtk.Label(label = item_to_be_added )

            self.list_box.insert(label, -1)
            self.list_box.insert(total_label,-1 )
            self.show_all()
        else:
            label = Gtk.Label(label = item_to_be_added )
            self.list_box.insert(label, -1)
            self.list_box.insert(total_label, -1)
            self.show_all()


    def add_to_total(self, button_event, item):
        if self.sign_on:
            self.current_basket.append(item)
            self.total = self.total + item.price

            total_details = "£" + "{:.2f}".format(self.total)
            item_details = str(item.price) + "  " + item.name
            self.add_to_list_box(item_details, total_details)

 
        else:
            not_signed_on()


    def re_render_form(self):
        self.grid.destroy()
        self.create_form()