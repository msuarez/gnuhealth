"""GNU Health Calendar for WebDAV3

The package is the continuation of the CalDAV functionality
for the discontinued Tryton package.

It has been ported to Python 3 and GNU Health.

It contains the models to use Calendars in GNU Health HMIS.



"""

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
