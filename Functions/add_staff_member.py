from Storage.store_staff import store_staff
from Objects.staff import Staff

def add_staff_member(self, parent):
        
    name = self.name_entry.get_text()
    date_of_birth = self.date_of_birth_entry.get_text()
    gender = self.gender_entry.get_text()
    employee_type = self.employee_type_entry.get_text()
    passcode = self.passcode_entry.get_text()

    new_staff_member = Staff(name, date_of_birth, gender, employee_type, passcode)

    parent.list_of_staff.append(new_staff_member)

    store_staff(parent.list_of_staff)

    self.destroy()