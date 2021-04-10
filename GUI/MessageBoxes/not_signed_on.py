import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class not_signed_on(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Error")

        self.fullscreen()
        

        label = Gtk.Label(label = "You are not signed on yet")

        button = Gtk.Button(label = "Okay")
        button.connect("clicked", self.on_click)

        box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)

        box.pack_start(label, True, True, 0)
        box.pack_start(button, True, True, 0)

        self.add(box)
        self.show_all()

    def on_click(self, button_event):
        self.destroy()