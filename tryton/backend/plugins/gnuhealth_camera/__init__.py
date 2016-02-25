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



def set_media(data, frame):
    #Store the frame in a container
    rc, container = cv2.imencode(".png",frame)
    container = bytearray(container)
    document_model = data['model']
    rpc.execute(
        'model', document_model, 'write',
        data['ids'],
        {'photo':container}, rpc.CONTEXT)

def take_pic(data):

    """ Allow only one record
    """

    if (len(data['ids']) == 0):
        warning(
            _('Please choose one record associated to this picture / video'),
            _('You need to select a record !'),
        )
        return

    if (len(data['ids']) > 1):
        warning(
            _('Please choose only one record for this picture / video'),
            _('Multiple records selectd !'),
        )
        return

    # Open the webcam device
    cap = cv2.VideoCapture(0)
    document_model = data['model']

    while(True):
        # Grab the frames
        try:
            rc, frame = cap.read()
        except:
            break
            
        # Display the resulting frame
        cv2.imshow('== GNU Health Camera ==',frame)

        keypressed = cv2.waitKey(1)
        if  keypressed == ord(' '):

            # Make a backup copy  
            cv2.imwrite('/tmp/gnuhealth_snapshot.png',frame)              

            # call set media   
            set_media(data, frame)            

        if keypressed == ord('q'):
            break        


    #Cleanup 
    cap.release()
    cv2.destroyAllWindows()

    # Reload the form
    a = Form(document_model, res_id=data['ids'][0], mode=['form'])
    a.sig_reload(test_modified=False)

def get_plugins(model):
    return [
        (_('Take a picture'), take_pic),
        ]
