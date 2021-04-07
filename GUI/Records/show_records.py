import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from Storage.get_records import get_records
import datetime


class show_records(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "View Records")


        Box_For_Options = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)

        show_all_records_button = Gtk.Button(label = "Show All")
        show_all_records_button.connect("clicked", self.show_all_records)

        show_records_for_today_button = Gtk.Button(label = "Todays Records")
        show_records_for_today_button.connect("clicked", self.show_records_for_today)

        show_records_for_staff_member_button = Gtk.Button(label = "Search By Staff")
        show_records_for_staff_member_button.connect("clicked", self.show_records_for_staff_member)

        show_records_for_specific_date = Gtk.Button(label = "Search By Date")
        show_records_for_specific_date.connect("clicked", self.show_records_for_specific_date)

        show_records_for_specific_item = Gtk.Button(label = "Search By Item")
        show_records_for_specific_item.connect("clicked", self.show_records_for_specific_item)

        show_records_for_specific_category = Gtk.Button(label = "Search By Category")
        show_records_for_specific_category.connect("clicked", self.show_records_for_specific_category)

        Box_For_Options.pack_start(show_all_records_button, True, True, 0)
        Box_For_Options.pack_start(show_records_for_today_button, True, True, 0)
        Box_For_Options.pack_start(show_records_for_staff_member_button, True, True, 0)
        Box_For_Options.pack_start(show_records_for_specific_date, True, True, 0)
        Box_For_Options.pack_start(show_records_for_specific_item, True, True, 0)
        Box_For_Options.pack_start(show_records_for_specific_category, True, True, 0)

        self.add(Box_For_Options)
    

    def show_all_records(self):
        print("showing all records")

    def show_records_for_today(self):
        print("showing todays records")

    def show_records_for_staff_member(self):
        print("showing records for staff member")

    def show_records_for_specific_date(self):
        print("Shpwing for specifig date")

    def show_records_for_specific_item(self):
        print("showing for specific item")

    def show_records_for_specific_category(self):
        print("showing for specific category")



        '''

            //  Coming soon.

        '''
