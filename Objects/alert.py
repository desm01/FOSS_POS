



import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class alert_messagebox(Gtk.Window):
    def __init__(self, text_to_display):
        Gtk.Window.__init__(self, title = "ALERT")

        self.fullscreen()

        label = Gtk.Label(label = text_to_display)
        okay_button = Gtk.Button(label = "Okay")
        okay_button.connect("clicked", self.on_click)

        box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)

        box.pack_start(label, True, True, 0)
        box.pack_start(okay_button, True, True, 0)

        self.add(box)

        self.show_all()

    def on_click(self, button_event):
        self.destroy()