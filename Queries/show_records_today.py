from Storage.get_records import get_records
import datetime

def show_records_today():
    list_of_records = get_records()
    length_of_records = len(list_of_records) -1
    todays_date = datetime.date.today()

    list_of_records_to_return = []

    for i in range (length_of_records, -1, -1):
        if list_of_records[i].date_time.date() == todays_date:
            list_of_records_to_return.append(list_of_records[i])
        
        if list_of_records[i].date_time.date() < todays_date:
            break

    return list_of_records_to_return