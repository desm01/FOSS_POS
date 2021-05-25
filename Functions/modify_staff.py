from Objects.staff import Staff
from Storage.store_staff import store_staff

from Objects.alert import alert_messagebox

def check_if_string_is_valid(name, gender, employee_type):
    if len(name) < 1 or len(gender) < 1 or len(employee_type) < 1:
        return False
    else:
        return True


def modify_staff_member(self, old_staff, parent):

    new_passcode = self.passcode_entry.get_text()
    new_gender = self.gender_entry.get_text()
    new_employee_type = self.employee_type_entry.get_text()

    if check_if_string_is_valid(new_passcode, new_gender, new_employee_type):
        old_staff.update_details(new_passcode, new_gender, new_employee_type)
        store_staff(parent.list_of_staff)
        self.destroy()
    else:
        dialog = alert_messagebox("Error, all fields must be filled in")
        response = dialog.run()
        dialog.destroy()
