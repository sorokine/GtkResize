'''
Created on Jan 28, 2013

@author: sorokine
'''

import pygtk
import gtk

class GtkResize(object):
    
    def __init__(self):
        self.temp_height = 0
        self.temp_width = 0

        gb = gtk.Builder()
        gb.add_from_file("gtk_resize.glade")
        gb.connect_signals({ "on_window_destroy" : gtk.main_quit })
        
        image1 = gtk.Image()
        image1.set_from_file("img.png")
        self.pixbuf = image1.get_pixbuf()
        image1.connect('expose-event', self.on_image_resize)    
        imgBox1 = gb.get_object("imgBox1")
        imgBox1.add(image1)
        
        image2 = gtk.Image()
        image2.set_from_file("img.png")
        imgBox2 = gb.get_object("imgBox2")
        imgBox2.add(image2)
        
        self.window = gb.get_object("window1")
        self.window.show_all()

    def on_image_resize(self, widget, event):
        allocation = widget.get_allocation()
        if self.temp_height != allocation.height or self.temp_width != allocation.width:
            self.temp_height = allocation.height
            self.temp_width = allocation.width
            pixbuf = self.pixbuf.scale_simple(allocation.width, allocation.height, gtk.gdk.INTERP_BILINEAR)
            widget.set_from_pixbuf(pixbuf)

if __name__ == "__main__":
    GtkResize()
    gtk.main()
    
    