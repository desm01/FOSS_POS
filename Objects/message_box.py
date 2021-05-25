import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class message_box:

    def __init__(self, new_text):
        self.dialog = Gtk.MessageDialog(
        message_type = Gtk.MessageType.INFO,
        buttons = Gtk.ButtonsType.YES_NO, 
        text = new_text
    )

    
