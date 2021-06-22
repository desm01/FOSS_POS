from Objects.item import Item
from Objects.alert import alert_messagebox
from Functions.add_new_item import check_if_new_item_is_correct
from Storage.store_items import store_items
from Functions.remove_item_from_basket import clear_list_box

def modify_item(self, parent, item):
    try:
        new_name = self.name_entry.get_text()
        new_price = float (self.price_entry.get_text())
        new_quantity = float(self.quantity_entry.get_text())
        new_plu_number = float(self.plu_number_entry.get_text())
        new_item_type = self.item_type_entry.get_text()
        new_category = self.item_type_category_entry.get_text()

        new_item = Item(new_name, new_price, new_quantity, new_plu_number, new_item_type, new_category)
        
        if check_if_new_item_is_correct(new_item) == True:
            item.update(new_item)
            store_items(parent.list_of_items)
            parent.render_form()


        else:
            dialog = alert_messagebox("Error, the fields have been incorrectly filled out")
            response = dialog.run()
            dialog.destroy()


    except:
        alert_messagebox("Error, the items have been incorrectly formated")

    clear_list_box(parent)
    self.destroy()