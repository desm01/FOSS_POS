import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

from GUI.modify_staff_window import modify_staff_member_window

class show_staff_window(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self, title = "Show Staff Members")
        
        self.fullscreen()
        
        self.box = Gtk.Box(spacing = 0, orientation = Gtk.Orientation.VERTICAL)

        label = Gtk.Label(label = "Select the member of staff you wish to modify")
        self.set_up_buttons(parent)

        self.add(self.box)

        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.resize(200,150)

        self.show_all()
    
    def set_up_buttons(self, parent):
        for staff in parent.list_of_staff:
            button = Gtk.Button(label = staff.name)
            button.connect("clicked", self.on_click, staff, parent)

            self.box.pack_start(button, True, True, 0)

    def on_click(self, button_event, staff, parent):
        window = modify_staff_member_window(staff, parent)
        window.show_all()
        window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.destroy()