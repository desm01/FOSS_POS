import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Functions.add_staff_member import add_staff_member

class add_staff_member_window(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Add New Staff Member")



        box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)

        self.set_border_width(25)

        self.fullscreen()

        name_label = Gtk.Label(label = "Name:")
        self.name_entry = Gtk.Entry()

        date_of_birth_label = Gtk.Label(label = "Date Of Birth:")
        self.date_of_birth_entry = Gtk.Entry()

        gender_label = Gtk.Label(label = "Gender:")
        self.gender_entry = Gtk.Entry()


        employee_type_label = Gtk.Label(label = "Employee Type:")
        self.employee_type_entry = Gtk.Entry()

        passcode_label = Gtk.Label(label = "Passcode:")
        self.passcode_entry = Gtk.Entry()

        back_button = Gtk.Button(label = "Back")
        back_button.connect("clicked", self.back_handler)

        submit_button = Gtk.Button("Submit")
        submit_button.connect("clicked", self.on_click, parent)

        box.pack_start(name_label, True, True, 0)
        box.pack_start(self.name_entry, True, True, 0)

        box.pack_start(date_of_birth_label, True, True, 0)
        box.pack_start(self.date_of_birth_entry, True, True, 0)

        box.pack_start(gender_label, True, True, 0)
        box.pack_start(self.gender_entry, True, True, 0)

        box.pack_start(employee_type_label, True, True, 0)
        box.pack_start(self.employee_type_entry, True, True, 0)

        box.pack_start(passcode_label, True, True, 0)
        box.pack_start(self.passcode_entry, True, True, 0)

        hBox = Gtk.Box()
        hBox.pack_start(back_button, True, True, 25)
        hBox.pack_start(submit_button, True, True, 25)

        box.pack_start(hBox, True, True, 10)

        self.add(box)

        self.show_all()

    def back_handler(self, button_event):
        self.destroy()

    def on_click(self, button_event, parent):
        add_staff_member(self, parent)

