import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Objects.staff import Staff

class modify_staff_member_window(Gtk.Window):
    def __init__(self, staff):
        Gtk.Window.__init__(self, title = "Modify Staff Member")


        box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)
        
        name_label = Gtk.Label(label = "Name:")
        self.name_entry = Gtk.Entry()
        self.name_entry.set_text(staff.name)

        gender_label = Gtk.Label(label = "Gender:")
        self.gender_entry = Gtk.Entry()
        self.gender_entry.set_text(staff.gender)

        employee_type_label = Gtk.Label(label = "Employee Type:")
        self.employee_type_entry = Gtk.Entry()
        self.employee_type_entry.set_text(staff.employee_type)


        submit_button = Gtk.Button("Submit")
        submit_button.connect("clicked", self.on_click, staff)

        box.pack_start(name_label, True, True, 0)
        box.pack_start(self.name_entry, True, True, 0)

        box.pack_start(gender_label, True, True, 0)
        box.pack_start(self.gender_entry, True, True, 0)

        box.pack_start(employee_type_label, True, True, 0)
        box.pack_start(self.employee_type_entry, True, True, 0)

        box.pack_start(submit_button, True, True, 0)

        self.add(box)

        self.show_all()


    def on_click(self, button_event, old_staff):
        new_name = self.name_entry.get_text()
        new_gender = self.gender_entry.get_text()
        new_employee_type = self.employee_type_entry.get_text()

        old_staff.update_details(new_name, new_gender, new_employee_type)

        self.destroy()