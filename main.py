import gi

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


'''
Setting up some dummy data
'''
staff1 = Staff("Des", '2001/02/26', "male", "Boss", "0000")
staff2 = Staff("Alex", "1998/12/21", "male", "Assistant", "0001")
staff3 = Staff("Liv", "1997/10/08", "female", "Co-boss", "0002")

item1 = Item("Coke", 1.29, 24, 1000001, "Drink", "Soft Drink")
item2 = Item("Sprite", 1.09, 30, 1000002, "Drink", "Soft Drink")
item3 = Item("Red Bull", 1.59, 4, 1000003, "Drink", "Energy Drink")
item4 = Item("Mars Bar", 0.79, 12, 100004, "Food", "Candy")

current_basket = []

staffList = []
staffList.append(staff1)
staffList.append(staff2)
staffList.append(staff3)

itemList = []
itemList.append(item1)
itemList.append(item2)
itemList.append(item3)
itemList.append(item4)


class mainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "EPOS Software")

        self.grid = Gtk.Grid()

        self.list_of_items = itemList
        self.list_of_staff = staffList

        self.sign_on = False

        self.Box_For_Item_Buttons = Gtk.Box()
        
        
        self.Box_For_Special_Buttons = Gtk.Box()

        self.Box_For_Total = Gtk.Box()
        
        self.list_box = Gtk.ListBox()
        lbl = Gtk.Label(label = "Current Basket")
        self.list_box.prepend(lbl)
        
        self.Box_For_Total.add(self.list_box)

        self.intialise_buttons()

        self.grid.add(self.Box_For_Item_Buttons)

        self.grid.add(self.Box_For_Special_Buttons )

        self.grid.attach_next_to(self.Box_For_Total, self.Box_For_Special_Buttons, Gtk.PositionType.BOTTOM, 2 ,2 )

        self.add(self.grid)


    def intialise_buttons(self):
        for item in itemList:
            button = Gtk.Button(label = item.name)
            button.connect("clicked", self.add_to_total, item)
            self.Box_For_Item_Buttons.pack_start(button, True, True, 0)

        self.initalise_sign_on_button()
        self.initalise_modify_button()
        self.initalise_add_item_button()
        self.initalise_checkout_button()
        self.initalise_settings_button()

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
        self.add_item_window = add_item_window(self, itemList)
        self.add_item_window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.add_item_window.show_all()

    def user_has_signed_on(self, staff_member, entered_code):
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
        label = Gtk.Label(item_to_be_added )
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


window = mainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
window.set_size_request(800,400)
Gtk.main()

