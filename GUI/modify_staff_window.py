import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Objects.staff import Staff
from Storage.store_staff import store_staff

from GUI.MessageBoxes.alert_messagebox import alert_messagebox

class modify_staff_member_window(Gtk.Window):
    def __init__(self, staff, parent):
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
        submit_button.connect("clicked", self.on_click, staff, parent)

        box.pack_start(name_label, True, True, 0)
        box.pack_start(self.name_entry, True, True, 0)

        box.pack_start(gender_label, True, True, 0)
        box.pack_start(self.gender_entry, True, True, 0)

        box.pack_start(employee_type_label, True, True, 0)
        box.pack_start(self.employee_type_entry, True, True, 0)

        box.pack_start(submit_button, True, True, 0)

        self.add(box)

        self.show_all()


    def check_if_string_is_valid(self, name, gender, employee_type):
        if len(name) < 1 or len(gender) < 1 or len(employee_type) < 1:
            return False
        else:
            return True

    def on_click(self, button_event, old_staff, parent):
        new_name = self.name_entry.get_text()
        new_gender = self.gender_entry.get_text()
        new_employee_type = self.employee_type_entry.get_text()

        if self.check_if_string_is_valid(new_name, new_gender, new_employee_type):
            old_staff.update_details(new_name, new_gender, new_employee_type)
            store_staff(parent.list_of_staff)
            self.destroy()
        else:
            dialog = alert_messagebox("Error, all fields must be filled in")
            response = dialog.run()
            dialog.destroy()
