

def check_if_item_is_correct(new_item):
    if len(new_item.name) < 1 or len(new_item.price) < 1 or len(new_item.quantity) < 1 or len(new_item.plu_number) < 1 or len(new_item.item_type) < 1 or len(new_item.item_category) < 1:
        return False
    else:
        return True

def check_if_format_is_correct(self, new_item):
    try:
        price = float(new_item.price)
        plu_number = float(new_item.plu_number)
        quantity = float(new_item.quantity)
        return True
    except:
        return False

def check_if_new_item_is_valid(self, new_item):
        
    fields_are_filled_in = self.check_if_all_fields_are_filled_in(new_item)
    fields_are_correctly_formatted = self.check_if_format_is_correct(self, new_item) 

    if fields_are_filled_in and fields_are_correctly_formatted:
        return True
    else:
        return False