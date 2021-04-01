import gi

from Objects.item import Item

from Objects.staff import Staff

from Functions.checkout import checkout
from GUI.add_item_window import add_item_window

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


'''
Setting up some dummy data
'''
staff1 = Staff("Des", '2001/02/26', "male", "Boss")
staff2 = Staff("Alex", "1998/12/21", "male", "Assistant")
staff3 = Staff("Liv", "1997/10/08", "female", "Co-boss")

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
        self.list_of_items = itemList
        self.Box_For_Buttons = Gtk.Box()
        self.intialise_buttons()
        self.add(self.Box_For_Buttons)

    def intialise_buttons(self):
        for item in itemList:
            button = Gtk.Button(label = item.name)
            button.connect("clicked", self.add_to_total, item)
            self.Box_For_Buttons.pack_start(button, True, True, 0)


        self.initalise_add_item_button()
        self.initalise_checkout_button()


    def initalise_checkout_button(self):
        checkout_button = Gtk.Button(label = "Checkout")
        checkout_button.connect("clicked", self.checkout_handler)
        self.Box_For_Buttons.pack_start(checkout_button, True, True, 0)

    def initalise_add_item_button(self):
        add_item_button = Gtk.Button(label = "Add New Item")
        add_item_button.connect("clicked", self.add_new_item_handler)
        self.Box_For_Buttons.pack_start(add_item_button, True, True, 0)

    def add_new_item_handler(self, button_event):
    
        self.add_item_window = add_item_window(self, itemList)

        self.add_item_window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)

        self.add_item_window.show_all()

        print(self.list_of_items)


    def render_buttons(self):
        new_item = self.list_of_items[len(self.list_of_items) - 1]
        new_button = Gtk.Button(label = new_item.name)
        new_button.connect("clicked", self.add_to_total, new_item )

        self.Box_For_Buttons.pack_start(new_button, True, True, 0)
        self.show_all()
        self.add_item_window.destroy()
        

    def checkout_handler(self, button_event):
        checkout(current_basket)
        current_basket.clear()

    def add_to_total(self, button_event, item):
        current_basket.append(item)

        print(item.name)
        print(item.price)

window = mainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
window.set_size_request(800,400)
Gtk.main()

