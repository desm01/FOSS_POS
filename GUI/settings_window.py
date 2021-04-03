import gi
gi.require_version("Gtk", "3.0")

from Objects.item import Item
from Objects.staff import Staff

from gi.repository import Gtk

class settings_window(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Settings")

        box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)


        add_staff_button = Gtk.Button(label = "Add Staff Member")
        add_staff_button.connect("clicked", self.add_staff_handler)

        modify_staff_button = Gtk.Button(label = "Modify Staff Member")
        modify_staff_button.connect("clicked", self.modify_staff_handler)

        view_records_button = Gtk.Button(label = "View Records")
        view_records_button.connect("clicked", self.view_records_handler)


        box.pack_start(add_staff_button, True, True, 0)
        box.pack_start(modify_staff_button, True, True, 0)
        box.pack_start(view_records_button, True, True, 0)

        self.add(box)

    def view_records_handler(self, button_event):
        print("records")
    
    def add_staff_handler(self, button_event):
        print("Adding staff")

    def modify_staff_handler(self, button_event):
        print("Modify Staff")