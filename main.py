from Storage.get_staff import get_staff
import gi
import math

from Storage.store_items import store_items
from Storage.get_items import get_items

from Objects.purchase import Purchase
from Objects.item import Item
from Objects.staff import Staff

from Functions.checkout import checkout

from GUI.add_item_window import add_item_window
from GUI.show_buttons_window import show_buttons_window
from GUI.sign_on_screen import sign_on_screen
from GUI.MessageBoxes.wrong_passcode_screen import wrong_passcode_screen
from GUI.MessageBoxes.not_signed_on import not_signed_on
from GUI.settings_window import settings_window

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

current_basket = []


class mainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "EPOS Software")
        

        self.initalise_form()

       
       


    def initalise_form(self):
        
        self.grid = Gtk.Grid()

        self.list_of_items = get_items()
        self.list_of_staff = get_staff()

        self.sign_on = False


        
        self.Box_For_Special_Buttons = Gtk.Box()

        self.Box_For_Total = Gtk.Box()
        
        self.list_box = Gtk.ListBox()
        lbl = Gtk.Label(label = "Current Basket")
        self.list_box.prepend(lbl)
        
        self.Box_For_Total.add(self.list_box)

        self.Box_For_Buttons = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)

        number_of_rows_to_create = len(self.list_of_items) / 5
        number_of_rows_to_create = math.ceil(number_of_rows_to_create)

        item_counter = 0
        
        for row in range (0, number_of_rows_to_create):
            new_row = Gtk.Box()
            for i in range(0,5):
                if item_counter == len(self.list_of_items):
                    break
                button = Gtk.Button(label = self.list_of_items[item_counter].name)
                button.connect("clicked", self.add_to_total, self.list_of_items[item_counter])

                new_row.pack_start(button, True, True, 0)
                item_counter = item_counter + 1

            self.Box_For_Buttons.pack_start(new_row, True, True, 0)
                

        self.initalise_sign_on_button()
        self.initalise_modify_button()
        self.initalise_add_item_button()
        self.initalise_checkout_button()
        self.initalise_settings_button()


        self.grid.add(self.Box_For_Buttons)

        self.grid.add(self.Box_For_Special_Buttons )

        self.grid.attach_next_to(self.Box_For_Total, self.Box_For_Special_Buttons, Gtk.PositionType.BOTTOM, 1 ,1 )

        self.add(self.grid)


    def initalise_settings_button(self):
        setting_button = Gtk.Button(label = "Settings")
        setting_button.connect("clicked", self.settings_handler)
        self.Box_For_Special_Buttons.pack_start(setting_button, True, True, 0)


    def initalise_sign_on_button(self):
        sign_on_button = Gtk.Button(label = "Sign On")
        sign_on_button.connect("clicked", self.sign_on_handler)
        self.Box_For_Special_Buttons.pack_start(sign_on_button, True, True, 0)

    def initalise_modify_button(self):
        modify_button = Gtk.Button(label = "Modify Item")
        modify_button.connect("clicked", self.modify_button_handler)
        self.Box_For_Special_Buttons.add(modify_button)

    def initalise_checkout_button(self):
        checkout_button = Gtk.Button(label = "Checkout")
        checkout_button.connect("clicked", self.checkout_handler)
        self.Box_For_Special_Buttons.pack_start(checkout_button, True, True, 0)

    def initalise_add_item_button(self):
        add_item_button = Gtk.Button(label = "Add New Item")
        add_item_button.connect("clicked", self.add_new_item_handler)
        self.Box_For_Special_Buttons.pack_start(add_item_button, True, True, 0)

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
            dialog = wrong_passcode_screen()
            response = dialog.run()
            dialog.destroy()
        

    def checkout_handler(self, button_event):

        if self.sign_on:
            checkout(current_basket)
            new_purchase = Purchase(current_basket, self.staff_member, self.staff_member)
           # new_purchase.record_item()
            
            self.clear_list_box()
            current_basket.clear()
        else:
            dialog = not_signed_on()
            response = dialog.run()
            dialog.destroy()

    def clear_list_box(self):
        for item in self.list_box:
            self.list_box.remove(item)
        
        label = Gtk.Label(label = "Current Basket:")
        self.list_box.add(label)
        self.show_all()

    def add_to_list_box(self, item_to_be_added):
        label = Gtk.Label(label = item_to_be_added )
        self.list_box.insert(label, -1)
        self.show_all()

    def add_to_total(self, button_event, item):
        if self.sign_on:
            current_basket.append(item)
            item_details = str(item.price) + "  " + item.name
            self.add_to_list_box(item_details)
 
        else:
            dialog = not_signed_on()
            response = dialog.run()
            dialog.destroy()

    def render_buttons(self):
        new_item = self.list_of_items[len(self.list_of_items) - 1]
        new_button = Gtk.Button(label = new_item.name)
        new_button.connect("clicked", self.add_to_total, new_item )

        store_items(self.list_of_items)

        self.grid.destroy()
        #self.Box_For_Buttons = Gtk.Box()
        self.initalise_form() #.pack_start(new_button, True, True, 0)
        self.show_all()
      #  self.destroy()

    def restart(self):
        self.destroy()
        start_program()


def start_program():
    window = mainWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
    window.set_size_request(800,400)
    Gtk.main()


start_program()