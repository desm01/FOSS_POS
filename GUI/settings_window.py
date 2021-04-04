from pickle import TRUE
import gi
gi.require_version("Gtk", "3.0")

from Objects.item import Item
from Objects.staff import Staff

from GUI.add_staff_member_window import add_staff_member_window
from GUI.show_staff_window import show_staff_window

from Storage.store_items import default_store_items

from gi.repository import Gtk

class settings_window(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Settings")

        box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)


        add_staff_button = Gtk.Button(label = "Add Staff Member")
        add_staff_button.connect("clicked", self.add_staff_handler, parent)

        modify_staff_button = Gtk.Button(label = "Modify Staff Member")
        modify_staff_button.connect("clicked", self.modify_staff_handler, parent)

        view_records_button = Gtk.Button(label = "View Records")
        view_records_button.connect("clicked", self.view_records_handler)

        restore_items_button = Gtk.Button(label = "Restore Items")
        restore_items_button.connect("clicked", self.restore_handler, parent)


        box.pack_start(add_staff_button, True, True, 0)
        box.pack_start(modify_staff_button, True, True, 0)
        box.pack_start(view_records_button, True, True, 0)
        box.pack_start(restore_items_button, True, True, 0)

        self.add(box)

    def view_records_handler(self, button_event):
        print("records")
    
    def add_staff_handler(self, button_event, parent):
        window = add_staff_member_window(parent)
        window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        window.show_all()
        self.destroy()

    def modify_staff_handler(self, button_event, parent):
        window = show_staff_window(parent)
        window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        window.show_all()

        self.destroy()

    def restore_handler(self, button_event, parent):
        default_store_items()
        self.destroy()
        parent.restart()
