from Storage.get_records import get_records

def show_records_for_staff_member(staff_member):
    list_of_records = get_records()

    list_of_records_for_staff_member = []

    for record in list_of_records:
        if record.served_by.name == staff_member.name:
            list_of_records_for_staff_member.append(record)

    return list_of_records_for_staff_member