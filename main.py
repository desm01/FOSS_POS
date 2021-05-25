import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from GUI import main_form
        
main_form.build_main_form()


Gtk.main()

