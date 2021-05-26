import gi

import math

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

from Storage.get_items import get_items
from Storage.get_staff import get_staff


from Functions.create_total_box import create_total_box
from Functions.create_item_buttons import create_item_buttons
from Functions.add_item_to_total import add_to_total
from Functions.create_special_buttons import create_special_buttons

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

        self.list_of_items = get_items()
        self.list_of_staff = get_staff()

        self.render_form()


    def fetch_items_and_staff(self):
        self.list_of_items = get_items()
        self.list_of_staff = get_staff()
       

    def render_form(self):
        try:
            self.grid.destroy()
        except:
            print("Grid Not Made")
        self.grid = Gtk.Grid()

  

        self.Special_Buttons_Box = Column(Gtk.Orientation.VERTICAL)
        self.Total_Box = Column(Gtk.Orientation.VERTICAL)
        self.PLU_Box = Column(Gtk.Orientation.VERTICAL)
  

        self.populate_special_button_column()
        self.populate_total_column()
        self.populate_PLU_column()

        self.grid.add(self.Special_Buttons_Box.box)
        self.grid.attach_next_to(self.scroll_bar, self.Special_Buttons_Box.box, Gtk.PositionType.RIGHT, 1,1)
        self.grid.attach_next_to(self.PLU_Box.box, self.scroll_bar, Gtk.PositionType.RIGHT, 1, 1)
    

        self.add(self.grid)
        
        self.show_all()

    def populate_special_button_column(self):
        create_special_buttons(self)

        

    def populate_total_column(self):
        create_total_box(self)




    def populate_PLU_column(self):
        plu_box = create_item_buttons(self, add_to_total)
        self.PLU_Box.add(plu_box)

    
            