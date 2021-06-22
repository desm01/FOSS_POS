from typing import List
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Button:

    def __init__(self, button_label, event, list_of_parameters = None):
        if list_of_parameters is None:
            self.button = Gtk.Button(label = button_label, expand = True)
            self.button.connect("clicked", event)
        else:
            if list_of_parameters is list:
                self.button = Gtk.Button(label = button_label, expand = True)
                self.button.connect("clicked", event, *list_of_parameters)
            else:
                self.button = Gtk.Button(label = button_label, expand = True)
                self.button.connect("clicked", event, list_of_parameters)


    # Overloaing constructor.   -> Used when no parameters are being passed into event.
'''
    def __init__(self, button_label, event):


'''