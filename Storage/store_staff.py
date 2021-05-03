from Objects.staff import Staff
import pickle


def store_staff(list_of_staff):
    file_name = "staff_dump.pkl"
    open_file = open(file_name, "wb")
    pickle.dump(list_of_staff, open_file)
    open_file.close()

    print("Storing Staff")

def default_store_staff():
    file_name = "staff_dump.pkl"

    staffList = []

    staff1 = Staff("Des", '2001/02/26', "male", "Boss", "0000")
    staff2 = Staff("Alex", "1998/12/21", "male", "Assistant", "0001")
    staff3 = Staff("Liv", "1997/10/08", "female", "Co-boss", "0002")
    staff4 = Staff("Charles", "1972-12-01", "male", "janitor", "0001")
    staff5 = Staff("Ada", "1998-02-21", "female", "System Admin", "9999")
    staff6 = Staff("Alan", "1996-02-12", "male", "Accountant", "0001")
    staff7 = Staff("Ludwig", "1921-10-01", "male", "Co-Boss", "0111")

    
    staffList.append(staff1)
    staffList.append(staff2)
    staffList.append(staff3)
    staffList.append(staff4)
    staffList.append(staff5)
    staffList.append(staff6)
    staffList.append(staff7)

    open_file = open(file_name, "wb")
    pickle.dump(staffList, open_file)
    open_file.close()

    print("Storing staff")