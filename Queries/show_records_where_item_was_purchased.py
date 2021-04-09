from Storage.get_records import get_records

def show_records_where_item_was_purchased(item_to_look_for):
    
    list_of_purchases = get_records()
    list_of_purchases_to_return = []


    for record in list_of_purchases:
        for item in record.list_of_items:
            if item.name == item_to_look_for.name:
                list_of_purchases_to_return.append(record)
                break

    return list_of_purchases_to_return