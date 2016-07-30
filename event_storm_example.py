#!/usr/bin/env python3

import logging

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk  # NOQA

from event_storm_squasher import delayed  # NOQA


@delayed(milliseconds=1000)
def set_tm_data_view(i):
    """The docstring of set_tm_data_view survives due to functools.wraps"""
    print("'set_tm_data_view' was called with:", i)

@delayed(milliseconds=2000)
def set_tm_data_view2(i):
    """The docstring of set_tm_data_view2 survives due to functools.wraps"""
    print("'set_tm_data_view2' was called with:", i)


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, unused_widget):
        logging.info("Calling set_tm_data_view 100 times...")
        for i in range(100):
            set_tm_data_view(i)
        logging.info("Calling set_tm_data_view2 200 times...")
        for i in range(200):
            set_tm_data_view2(i)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    win = MyWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()
