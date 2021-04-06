import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from Storage.get_records import get_records
import datetime

class show_records(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "View Records")

        self.text_view = Gtk.ListBox()
    

        list_of_items = get_records()

        self.get_todays_items(list_of_items)

        vBox = Gtk.VBox()
        vBox.pack_start(self.text_view, 1, 1, 0)

        swin = Gtk.ScrolledWindow()
        swin.add_with_viewport(vBox)

        self.add(swin)
        self.set_size_request(800,400)

        

    def get_todays_items(self, list_of_items):

        label = ""

        for i in range(len(list_of_items) - 1, -1, -1):

            date_of_sale = list_of_items[i].date_time.date()
            todays_date = datetime.datetime.now().date()

            if date_of_sale < todays_date:
                print("Breaking")
                break

            if (date_of_sale == todays_date):
                item = list_of_items[i].details()
                item_label = Gtk.Label(label = item)
                self.text_view.insert(item_label, -1)
            