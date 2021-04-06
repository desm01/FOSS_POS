

def check_if_fields_are_filled_in(new_item):
    if len(new_item.name) < 1 or len(new_item.itemType) < 1 or len(new_item.category) < 1:
        return False
    else:
        return True

def check_if_format_is_correct(new_item):
    try:
        price = float(new_item.price)
        plu_number = float(new_item.pluNumber)
        quantity = float(new_item.quanitity)
        return True
    except:
        return False

def check_if_new_item_is_correct(new_item):
        
    fields_are_filled_in = check_if_fields_are_filled_in(new_item)
    fields_are_correctly_formatted = check_if_format_is_correct(new_item) 

    if fields_are_filled_in and fields_are_correctly_formatted:
        return True
    else:
        return False