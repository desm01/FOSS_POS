class Staff:

    def __init__(self, name, date_of_birth, gender, employee_type, passcode):
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.employee_type = employee_type
        self.passcode = passcode

    def __del__(self):
        print("Employee Destroyed")

    def change_name(self, new_name):
        self.name = new_name

    def change_gender(self, new_gender):
        self.gender = new_gender

    def change_employee_type(self, new_employee_type):
        self.employee_type = new_employee_type

    def print_details(self):
        print("Name: " + self.name)
        print("Date Of Birth: " + self.date_of_birth)
        print("Gender: " + self.gender)
        print("Employee Type: " + self.employee_type)


