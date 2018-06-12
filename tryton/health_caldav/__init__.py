# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from . import caldav
from .webdav import *
from .calendar_ import *
from .res import *


def register():
    Pool.register(
        Collection,
        Calendar,
        ReadUser,
        WriteUser,
        Category,
        Location,
        Event,
        EventCategory,
        EventAlarm,
        EventAttendee,
        EventRDate,
        EventExDate,
        EventRRule,
        EventExRule,
        User,
        module='calendar', type_='model')
