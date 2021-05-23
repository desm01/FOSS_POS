import gi
gi.require_version("Gtk", "3.0")

from Objects.staff import Staff

from GUI.Forms.passcode_screen import passcode_screen

from gi.repository import Gtk

import math

from Functions.initalise_staff_buttons import initalise_staff_button

class sign_on_screen(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Sign On Screen")
        
        self.fullscreen()
        self.box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)
        


        initalise_staff_button(self, parent, self.button_click_handler)

        self.add(self.box)
        self.show_all()

    
    def button_click_handler(self, button_event, staff, parent):

        self.passcode_screen = passcode_screen(parent, staff)
        self.passcode_screen.set_position(Gtk.WindowPosition.CENTER_ALWAYS)


    