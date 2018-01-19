#  Copyright (C) 2017 - 2018 Luis Falcon <falcon@gnu.org>
#  Copyright (C) 2017 - 2018 GNU Solidario <health@gnusolidario.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

from tryton.config import GNUHEALTH_ICON
import gtk

class Activity():
    "GNU Health client Activity Logger"
    
    activity_window = gtk.Window()
    activity_window.set_default_size(500, 500)
    activity_window.set_title("Activity log - GNU Health ")
    activity_window.set_icon(GNUHEALTH_ICON)

    sw = gtk.ScrolledWindow()
    sw.set_policy(gtk.POLICY_AUTOMATIC, False)

    # TextView
    activity = gtk.TextView()
    sw.add(activity)
    
    # Make it read-only
    activity.set_editable(False) 
    textbuffer = activity.get_buffer()
    
    activity_window.add(sw)

