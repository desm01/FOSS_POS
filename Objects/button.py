import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Button:

    def __init__(self, button_label, event, list_of_parameters):

        self.button = Gtk.Button(label = button_label)
        self.button.connect("clicked", event, *list_of_parameters)


    # Overloaing constructor.   -> Used when no parameters are being passed into event.

    def __init__(self, button_label, event):
        self.button = Gtk.Button(label = button_label)
        self.button.connect("clicked", event)