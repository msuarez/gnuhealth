# This file is part of GNU Health.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from gi.repository import GObject, Gtk


class CellRendererToggle(Gtk.CellRendererToggle):
    pass


GObject.type_register(CellRendererToggle)
