import re
from types import resolve_bases
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Functions.display_checkout import display_checkout

from Objects.alert import alert_messagebox
from Objects.message_box import message_box

from GUI.Forms.add_customer_window import add_customer_window
from GUI.Forms.select_customer_window import select_customer_window


def dialog(text):
    dialog = message_box(text).dialog
    response = dialog.run()
    dialog.destroy()
    return response



def checkout(item_list):
    response = dialog("Does the customer have an account?")
    
    if response == Gtk.ResponseType.YES:
        select_customer_window(item_list)
    else:
     
        response = dialog("Does the customer wish to register an account?")
        if response == Gtk.ResponseType.YES:
            add_customer_window(item_list)
        else:
            display_checkout(item_list)


