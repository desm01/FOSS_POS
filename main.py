import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from GUI import build_main_form
        
window = build_main_form

window.build_main_form()


Gtk.main()

