import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class show_items_in_basket(Gtk.Window):
    def __init__(self, parent, current_basket):
        Gtk.Window.__init__(self, title = "Select Item To Remove From Basket")

        self.fullscreen()

        box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)

        if len(current_basket) == 0:
            label = Gtk.Label(label = "Sorry there are no items in the basket")
            box.pack_start(label, True, True, 0)

            back_button = Gtk.Button(label = "Back")
            back_button.connect("clicked", self.back_handler)

            box.pack_start(back_button, True, True, 0)

        else:
            for item in current_basket:
                button = Gtk.Button(label = item.name)
                button.connect("clicked", self.on_click, parent, item)
                box.pack_start(button, True, True, 0)

        self.add(box)

        self.show_all()

    def on_click(self, button_event, parent, item):
        parent.remove_from_basket(item)
        self.destroy()

    def back_handler(self, button_event):
        self.destroy()