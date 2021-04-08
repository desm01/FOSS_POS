import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Queries.show_records_for_staff_member import show_records_for_staff_member

class show_records_for_staff(Gtk.Window):
    def __init__(self, staff_member):
        Gtk.Window.__init__(self, title = "Staff Records")

        scrolled_window = Gtk.ScrolledWindow()
        self.set_border_width(10)
        list_box = Gtk.ListBox()

        records = show_records_for_staff_member(staff_member)

        if len(records) == 0:
            label = Gtk.Label(label = staff_member.name + " has no records")
            list_box.add(label)

        else:
            for record in records:
                label = Gtk.Label(label = record.details())
                list_box.add(label)

        scrolled_window.add(list_box)
        self.add(scrolled_window)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_size_request(700,400)
        self.show_all()