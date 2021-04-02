import gi
gi.require_version("Gtk", "3.0")
import sys
import os
sys.path.append(os.path.abspath('./Objects'))
import staff as Staff

from gi.repository import Gtk

class sign_on_screen(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Sign On Screen")
        self.box = Gtk.Box()
        list_of_staff = parent.list_of_staff

        for staff in list_of_staff:
            self.create_buttons_for_staff(staff, parent)

        self.add(self.box)
        self.show_all()

    def create_buttons_for_staff(self, staff, parent):
        button = Gtk.Button(label = staff.name)
        button.connect("clicked", self.button_click_handler, staff, parent)
        self.box.pack_start(button, True, True, 0)
    
    def button_click_handler(event,self, staff, parent):
        parent.user_has_signed_on(staff)