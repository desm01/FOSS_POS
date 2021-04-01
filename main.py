import gi

from Objects.item import Item

from Objects.staff import Staff

from Functions.checkout import checkout

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
        self.Box_For_Buttons = Gtk.Box()
        self.intialise_buttons()
        self.add(self.Box_For_Buttons)

    def intialise_buttons(self):
        for item in itemList:
            button = Gtk.Button(label = item.name)
            button.connect("clicked", self.add_to_total, item)
            self.Box_For_Buttons.pack_start(button, True, True, 0)

        checkout_button = Gtk.Button(label = "Checkout")
        checkout_button.connect("clicked", self.checkout)
        self.Box_For_Buttons.pack_start(checkout_button, True, True, 0)

    def checkout(self, button_event):
        checkout(itemList)

    def add_to_total(self, button_event, item):
        print(item.name)
        print(item.price)

window = mainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
window.set_size_request(800,400)
Gtk.main()

