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
    
    staffList.append(staff1)
    staffList.append(staff2)
    staffList.append(staff3)

    open_file = open(file_name, "wb")
    pickle.dump(staffList, open_file)
    open_file.close()

    print("Storing staff")