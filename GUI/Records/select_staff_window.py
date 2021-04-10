import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Storage.get_staff import get_staff
from GUI.Records.show_records_for_staff import show_records_for_staff

class select_staff_window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Which Member Of Staff?")
        
        self.box_for_search = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)

        self.box_for_search_box = Gtk.Box()
            
        label = Gtk.Label(label ="Enter Staff Member Name")

        self.entry = Gtk.Entry()

        submit_button = Gtk.Button(label = "Submit")
        submit_button.connect("clicked", self.search_handler)

        self.box_for_search_box.pack_start(self.entry, True, True, 0)
        self.box_for_search_box.pack_start(submit_button, True, True, 0)

        self.box_for_search.pack_start(label, True, True, 0)
        self.box_for_search.pack_start(self.box_for_search_box, True, True, 0)

        

        self.box_for_staff = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)
        self.generate_buttons()
        self.box_for_search.pack_start(self.box_for_staff, True, True, 0)

        self.add(self.box_for_search)

        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
       # self.set_size_request(700,400)
        self.show_all()

    def search_handler(self, button_event):
        self.box_for_staff.destroy()
        entered_name = self.entry.get_text()

        for staff in self.list_of_staff:
            if staff.name == entered_name:
                button = Gtk.Button(label = staff.name)
                button.connect("clicked", self.on_click_handler, staff)
              #  box_for_staff.pack_start(button, True, True, 0)

                self.box_for_search.pack_start(button, True, True, 0)
        self.show_all() 

    def generate_buttons(self):
        self.list_of_staff = get_staff()

        for staff in self.list_of_staff:
            button = Gtk.Button(label = staff.name)
            button.connect("clicked", self.on_click_handler, staff)

            self.box_for_staff.pack_start(button, True, True, 0)

    def on_click_handler(self, button_event, staff_member):
        show_records_for_staff(staff_member)
