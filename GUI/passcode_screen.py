import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class passcode_screen(Gtk.Window):
    def __init__(self, parent, staff_member):
        Gtk.Window.__init__(self, title = "Enter Passcode")

        self.current_code = ""
        self.label = Gtk.Label("Current Code: " + self.current_code)

        Box_For_Top_Row = Gtk.Box()

        Box_For_Middle_Row = Gtk.Box()

        Box_For_Bottom_Row = Gtk.Box()
        Box_For_Zero = Gtk.Box()

        for i in range(0,10):
            button = Gtk.Button(label = str(i), expand = True)
            button.connect("clicked", self.on_click, parent)

            if i == 0:
                Box_For_Zero.pack_start(button, True, True, 0)
            
            if (i >= 1 and i <= 3 ):
                Box_For_Bottom_Row.pack_start(button, True, True, 0)

            if (i >= 4 and i <= 6):
                Box_For_Middle_Row.pack_start(button, True, True, 0)

            if (i >= 7 and i <= 9):
                Box_For_Top_Row.pack_start(button, True, True, 0)


        minus_button = Gtk.Button(label = "-", expand = True)
        minus_button.connect("clicked", self.minus_button_click, parent)

        Box_For_Zero.pack_start(minus_button, True, True, 0)



        submit_button = Gtk.Button(label = "Submit", expand = True)
        submit_button.connect("clicked", self.submit_handler, parent, staff_member)


        
        grid = Gtk.Grid()
        grid.add(self.label)
        grid.attach_next_to(Box_For_Top_Row, self.label, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(Box_For_Middle_Row, Box_For_Top_Row, Gtk.PositionType.BOTTOM, 1 , 1)
        grid.attach_next_to(Box_For_Bottom_Row, Box_For_Middle_Row, Gtk.PositionType.BOTTOM, 1 , 1)
        grid.attach_next_to(Box_For_Zero ,Box_For_Bottom_Row, Gtk.PositionType.BOTTOM, 1 , 1)
        grid.attach_next_to(submit_button, Box_For_Zero, Gtk.PositionType.BOTTOM, 1 ,1)
        self.resize(400,380)
        self.add(grid)
       
        self.show_all()

    def minus_button_click(self, button_event, parent):
        text = self.current_code
        text = text[:-1]
        self.label.set_text("Current Code: " + text)
        self.current_code = text

    def on_click(self, button_event, parent):
        text = self.current_code
        text += button_event.get_label()
        self.current_code = text

        self.label.set_text("Current Code: " + text)

    def submit_handler(self, button_event, parent, staff_member):
        parent.user_has_signed_on( staff_member, self.current_code)
        self.destroy() 

        

         