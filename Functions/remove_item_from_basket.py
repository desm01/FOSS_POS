
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Functions.add_item_to_total import add_to_total

def remove_item_from_basket(self, item_to_remove):
    for item in self.current_basket:
        if item == item_to_remove:
            self.current_basket.remove(item)
            break

        #   Re-render ListBox
    clear_list_box(self)

    basket = self.current_basket.copy()
    self.current_basket.clear()
    self.total = 0

    for item in basket:
        add_to_total("", self, item)


def clear_list_box(self):
    for item in self.list_box:
        self.list_box.remove(item)
        
    label = Gtk.Label(label = "Current Basket:")
    self.total = 0
    self.list_box.add(label)
    self.show_all()