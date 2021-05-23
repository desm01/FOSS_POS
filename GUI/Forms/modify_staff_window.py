import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Functions.modify_staff import modify_staff_member

class modify_staff_member_window(Gtk.Window):
    def __init__(self, staff, parent):
        Gtk.Window.__init__(self, title = "Modify Staff Member")

        self.set_border_width(25)

        self.fullscreen()

        box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)
        
        name_label = Gtk.Label(label = "New Passcode:")
        self.passcode_entry = Gtk.Entry()
        self.passcode_entry.set_text(staff.passcode)

        gender_label = Gtk.Label(label = "Gender:")
        self.gender_entry = Gtk.Entry()
        self.gender_entry.set_text(staff.gender)

        employee_type_label = Gtk.Label(label = "Employee Type:")
        self.employee_type_entry = Gtk.Entry()
        self.employee_type_entry.set_text(staff.employee_type)


        submit_button = Gtk.Button("Submit")
        submit_button.connect("clicked", self.on_click, staff, parent)

        back_button = Gtk.Button("Back")
        back_button.connect("clicked", self.back_handler)

        box.pack_start(name_label, True, True, 0)
        box.pack_start(self.passcode_entry, True, True, 0)

        box.pack_start(gender_label, True, True, 0)
        box.pack_start(self.gender_entry, True, True, 0)

        box.pack_start(employee_type_label, True, True, 0)
        box.pack_start(self.employee_type_entry, True, True, 0)

        hBox = Gtk.Box()
        hBox.pack_start(back_button, True, True, 25)
        hBox.pack_start(submit_button, True, True, 25)

        box.pack_start(hBox, True, True, 10)

        self.add(box)

        self.show_all()


    def back_handler(self, button_event):
        self.destroy()

    def on_click(self, button_event, old_staff, parent):
        modify_staff_member(self, old_staff, parent)
