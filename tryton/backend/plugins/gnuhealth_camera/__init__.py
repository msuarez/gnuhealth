# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2016 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2016 GNU Solidario <health@gnusolidario.org>
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import tryton.rpc as rpc
from tryton.common import RPCExecute, warning, message
from tryton.gui.window.form import Form
import gettext
import numpy as np
import cv2

_ = gettext.gettext


def take_pic(data):

    document_model = data['model']

    """ Allow only one record
    """

    if (len(data['ids']) > 1):
        warning(
            _('Please choose only one record associated to this picture'),
            _('Multiple records selected !'),
        )
        return

    # Open the webcam device
    cap = cv2.VideoCapture(0)

    while(True):
        # Grab the frames
        try:
            rc, frame = cap.read()
        except:
            break
            
        # Display the resulting frame
        cv2.imshow('== GNU Health Camera ==',frame)

        if cv2.waitKey(1) == ord('q'):
            #Store the frame in a container
            rc, container = cv2.imencode(".png",frame)
            
            #Save a backup copy
            cv2.imwrite('/tmp/gnuhealth_snapshot.png',frame)

            break        


    #Cleanup 
    cap.release()
    cv2.destroyAllWindows()

def get_plugins(model):
    return [
        (_('Take a picture'), take_pic),
        ]
