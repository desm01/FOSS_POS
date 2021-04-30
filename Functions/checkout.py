from types import resolve_bases
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Functions.display_checkout import display_checkout

from GUI.MessageBoxes.checkout_window import checkout_window
from GUI.add_customer_window import add_customer_window



def check_if_customer_has_account():
    dialog = Gtk.MessageDialog(
        message_type = Gtk.MessageType.INFO,
        buttons = Gtk.ButtonsType.YES_NO, 
        text = "Does the customer have an account?" 
    )

    response = dialog.run()
    dialog.destroy()
    return response


def ask_customer_to_make_account():
    dialog = Gtk.MessageDialog(
        message_type = Gtk.MessageType.INFO,
        buttons = Gtk.ButtonsType.YES_NO,
        text = "Does the customer wish to register an account?"
    )

    response = dialog.run()
    dialog.destroy()
    return response

def checkout(item_list):

    response = check_if_customer_has_account()

    
    if response == Gtk.ResponseType.YES:
        display_checkout(item_list)

        
    
    else:
     
        response = ask_customer_to_make_account()
        if response == Gtk.ResponseType.YES:
            win = add_customer_window(item_list)
            win.show_all()
        else:
            display_checkout(item_list)

        print("he")

