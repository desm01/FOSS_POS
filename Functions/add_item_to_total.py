import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Objects.alert import alert_messagebox

def add_to_list_box(self, item_to_be_added, total_details):
    total_label = Gtk.Label(label = total_details)

    if(len (self.list_box) > 2):

        list_of_labels = self.list_box.get_children()
        final_index = len(list_of_labels) - 1
        label_to_be_removed = list_of_labels[final_index]
            
        self.list_box.remove(label_to_be_removed)
            
        label = Gtk.Label(label = item_to_be_added )

        self.list_box.insert(label, -1)
        self.list_box.insert(total_label,-1 )
        self.show_all()
    else:
        label = Gtk.Label(label = item_to_be_added )
        self.list_box.insert(label, -1)
        self.list_box.insert(total_label, -1)
        self.show_all()


def add_to_total(button, self,item):
    if self.sign_on:
        self.current_basket.append(item)
        self.total = self.total + item.price

        total_details = "£" + "{:.2f}".format(self.total)
        item_details = str(item.price) + "  " + item.name
        add_to_list_box(self, item_details, total_details)

 
    else:
        alert_messagebox("You are not signed on yet")