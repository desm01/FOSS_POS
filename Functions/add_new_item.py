from Objects.item import Item
from Storage.store_items import store_items

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

def add_new_item(self, parent):
    name = self.name_entry.get_text()
    price = float (self.price_entry.get_text())
    quantity = float(self.quantity_entry.get_text())
    plu_number = float(self.plu_number_entry.get_text())
    item_type = self.item_type_entry.get_text()
    item_category = self.item_type_category_entry.get_text()

    if (check_if_item_already_exists( parent, name)):
        print("Item already exists")
        
    else:
        new_item = Item(name, price, quantity, plu_number, item_type, item_category)
        if check_if_new_item_is_correct(new_item):
            parent.list_of_items.append(new_item)

            store_items(parent.list_of_items)

            parent.render_form()



            

    self.destroy()


def check_if_item_already_exists( parent, name_of_item):
    for item in parent.list_of_items:
        if name_of_item == item.name:
            return True

    return False