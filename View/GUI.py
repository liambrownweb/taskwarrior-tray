'''
Created on Feb 10, 2013

@author: Liam Brown
'''
import pygtk, gtk, os
from Subsystem import Defaults
pygtk.require('2.0')
from gtk import gdk
from Model import Notes

class gui(gtk.Window):
    _visible = False
    _controller = None
    _stay_open = False

    def show(self):
        self.present()
        self._visible=True

    def tray_activate(self, something):
        if (self._visible):
            self.hide()
            self._visible=False
        else:
            self.present()
            self._visible=True

    def gui_activate(self):
        gtk.main()

    def addController(self, controller):
        self._controller = controller

class Main(gui):
    _text_window = None

    def __init__(self):
        super(Main, self).__init__()
        self.connect('delete-event', self.on_delete_event)
        self.set_title("Quick Capture")
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_default_size(400,10)
        self.set_geometry_hints(min_width=320, min_height=100)
        icon = os.path.join(Defaults.prog_root_dir,"Img/logo-tray.xpm")
        self.set_icon_from_file(icon)
        box1 = gtk.VBox(gtk.FALSE, 0)
        self.add(box1)
        box1.show()

        box2 = gtk.VBox(gtk.FALSE, 10)
        box2.set_border_width(10)
        box1.pack_start(box2, gtk.TRUE, gtk.TRUE, 0)
        box2.show()
        table = gtk.Table(2, 3, gtk.FALSE)
        table.set_row_spacing(0, 2)
        table.set_col_spacing(0, 2)
        box2.pack_start(table, gtk.TRUE, gtk.TRUE, 0)
        table.show()
        # Create the GtkText widget
        self._text_window = gtk.Entry(50)
        self._text_window.set_editable(gtk.TRUE)
        self._text_window.connect("activate", self.on_ok_event)
        #frame = gtk.Frame()
        #frame.add(self._text_window)
        table.attach(self._text_window, 0, 1, 0, 1,
        gtk.EXPAND | gtk.SHRINK | gtk.FILL,
        gtk.EXPAND | gtk.SHRINK | gtk.FILL, 0, 0)
        self._text_window.show()
        button_box = gtk.HButtonBox()
        okbutton = gtk.Button("OK")
        okbutton.connect("clicked", self.on_ok_event)
        cancelbutton = gtk.Button("Cancel")
        cancelbutton.connect("clicked", self.on_cancel_event)
        button_box.add(okbutton)
        button_box.add(cancelbutton)
        box2.pack_end(button_box, gtk.FALSE, gtk.FALSE)
        okbutton.show()
        pixbuf = gdk.pixbuf_new_from_file_at_size(icon,25,25)
        statusicon = gtk.StatusIcon()
        statusicon = gtk.status_icon_new_from_pixbuf(pixbuf)
        statusicon.connect("activate",self.tray_activate)
        self.show_all()
        self.hide()

    def on_delete_event(self, widget, event):
        self.hide()
        return True

    def on_ok_event(self, widget):
        text_buffer = self._text_window.get_buffer()
        #text_start = text_buffer.get_start_iter()
        #text_end = text_buffer.get_end_iter()
        #contents = text_buffer.get_text(text_start, text_end)
        contents = text_buffer.get_text()
        result = self._controller.store({'type':Notes.Note, 'contents':contents})
        if result == None or not self._stay_open:
            self.hide()
        else:
            self.display(result)

    def display(self, result):
        pass

    def on_cancel_event(self, widget):
        self.hide()

if __name__ == "__main__":
    Main()
