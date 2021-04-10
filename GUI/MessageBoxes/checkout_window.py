import gi
gi.require_version("Gtk", "3.0")

from Objects.item import Item

from gi.repository import Gtk

class checkout_window(Gtk.Window):
    def __init__(self, checkout_text):
        Gtk.Window.__init__(self, title = "Checkout")

        self.fullscreen()

        win = Gtk.ScrolledWindow()

        okay_button = Gtk.Button(label = "Okay")
        okay_button.connect("clicked", self.on_click)

        self.set_border_width(25)

        label = Gtk.Label(label = checkout_text)

        box = Gtk.Box(spacing = 30, orientation = Gtk.Orientation.VERTICAL)
        box.pack_start(label, True, True, 10)
        box.pack_start(okay_button, True, True, 10)

        win.add_with_viewport(box)

        self.add(win)
        self.show_all()

    def on_click(self, button_event):
        self.destroy()