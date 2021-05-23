from Objects.item import Item
from GUI.MessageBoxes.alert_messagebox import alert_messagebox
from Functions.add_new_item import check_if_new_item_is_correct
from Storage.store_items import store_items

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
            parent.render_buttons()


        else:
            dialog = alert_messagebox("Error, the fields have been incorrectly filled out")
            response = dialog.run()
            dialog.destroy()


    except:
        dialog = alert_messagebox("Error, the items have been incorrectly formated")
        response = dialog.run()
        dialog.destroy()

    self.destroy()