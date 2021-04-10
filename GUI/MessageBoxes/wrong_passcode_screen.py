import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class wrong_passcode_screen(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Wrong Passcode")

        self.fullscreen()

        box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)

        label = Gtk.Label(label = "The passcode you have entered is incorrect")
        button = Gtk.Button(label = "Okay")
        button.connect("clicked", self.on_click)    
        
        box.pack_start(label, True, True, 0)
        box.pack_start(button, True, True, 0)


        self.add(box)
        self.show_all()

    def on_click(self, button_event):
        self.destroy()
        