# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Bool, Eval

__all__ = ['User']


class User(metaclass=PoolMeta):
    __name__ = 'res.user'

    calendars = fields.One2Many('calendar.calendar', 'owner', 'Calendars')

    @classmethod
    def __setup__(cls):
        super(User, cls).__setup__()
        required = Bool(Eval('calendars'))
        if not cls.email.states.get('required'):
            cls.email.states['required'] = required
        else:
            cls.email.states['required'] = (
                cls.email.states['required'] | required)
        if 'calendars' not in cls.email.depends:
            cls.email.depends.append('calendars')
