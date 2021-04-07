import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from Storage.get_records import get_records
import datetime

class show_records(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "View Records")

        '''

            //  Coming soon.

        '''
