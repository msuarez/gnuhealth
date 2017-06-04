#!/usr/bin/env python
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from argparse import ArgumentParser
from urllib.parse import urlparse
import unittest
import sys
import datetime

from dateutil.relativedelta import relativedelta
import caldav
import vobject
from proteus import config, Model, Wizard


def activate_module(name, config):
    Module = Model.get('ir.module')
    module, = Module.find([('name', '=', name)])
    if module.state != 'activated':
        Module.install([module.id], config.context)
        Wizard('ir.module.activate_upgrade').execute('upgrade')


def configure_user(login, config):
    User = Model.get('res.user')
    users = User.find([('login', '=', login)])
    email = '%s@example.com' % login
    if not users:
        User(login=login, name=login, email=email).save()
    else:
        user, = users
        user.email = email
        user.save()


def create_calendar(login, user, config):
    Calendar = Model.get('calendar.calendar')
    User = Model.get('res.user')
    current_user, = User.find([('login', '=', login)])
    main_user, = User.find([('login', '=', user)])
    for calendar in Calendar.find([('owner', '=', login)]):
        calendar.write_users.append(User(main_user.id))
        calendar.save()
        calendar.delete()
    calendar = Calendar(name=login, owner=current_user)
    if login != 'bar':
        calendar.read_users.append(main_user)
    calendar.save()


class TestCase(unittest.TestCase):

    def setUp(self):
        self.client = caldav.DAVClient(URL)
        self.principal = caldav.Principal(self.client, URL)
        self.calendar, = [x for x in self.principal.calendars()
            if x.url.path.endswith(user)]

    def test0010calendar(self):
        'Test calendar'
        calendar, _ = self.principal.calendars()

    def test0020create_event(self):
        'Create event'
        ical = vobject.iCalendar()
        vevent = ical.add('vevent')
        vevent.add('summary')
        vevent.summary.value = 'Test event'
        vevent.add('dtstart')
        vevent.dtstart.value = (datetime.datetime.now()
            + relativedelta(months=1))
        vevent.add('dtend')
        vevent.dtend.value = datetime.datetime.now() + relativedelta(months=1,
            hours=1)
        caldav.Event(self.client, data=ical.serialize(),
            parent=self.calendar).save()

    def test0030search_event(self):
        'Search date'
        events = self.calendar.date_search(datetime.datetime.now(),
            datetime.datetime.now() + relativedelta(months=2))
        self.assertEqual(len(events), 1)
        events = self.calendar.date_search(
            datetime.datetime.now() - relativedelta(months=1),
            datetime.datetime.now())
        self.assertEqual(len(events), 0)

    def test0040get_event(self):
        'Get event'
        event = self.calendar.events()[0]
        event.load()
        self.assertEqual(event.url, self.calendar.event(event.id).url)

    def test0050create_event_attendee(self):
        'Create event with attendee'
        ical = vobject.iCalendar()
        vevent = ical.add('vevent')
        vevent.add('summary')
        vevent.summary.value = 'Test event with attendee'
        vevent.add('dtstart')
        vevent.dtstart.value = datetime.datetime.now() + relativedelta(days=10)
        vevent.add('dtend')
        vevent.dtend.value = datetime.datetime.now() + relativedelta(days=10,
            hours=4)
        vevent.add('organizer')
        vevent.organizer.value = '%s@example.com' % user
        attendees = []
        for name in ('foo', 'bar'):
            attendee = vobject.base.ContentLine('ATTENDEE', [], '')
            attendee.partstat_param = 'TENTATIVE'
            attendee.value = 'MAILTO:%s@example.com' % name
            attendees.append(attendee)
        vevent.attendee_list = attendees
        caldav.Event(self.client, data=ical.serialize(),
            parent=self.calendar).save()

        Event = Model.get('calendar.event')
        owner_event, = Event.find([
                ('calendar.owner.email', '=', '%s@example.com' % user),
                ('summary', '=', vevent.summary.value),
                ])
        attendee_event, = Event.find([
                ('calendar.owner.email', '=', 'foo@example.com'),
                ])
        self.assertEqual(attendee_event.uuid, owner_event.uuid)

    def test0060update_attendee_status(self):
        'Update status of attendee'
        for event in self.calendar.events():
            event.load()
            value = event.instance.vevent.summary.value
            if value == 'Test event with attendee':
                break
        for attendee in event.instance.vevent.attendee_list:
            attendee.partstat_param = 'accepted'
        event.save()

        Event = Model.get('calendar.event')
        attendee_event, = Event.find([
                ('calendar.owner.email', '=', 'foo@example.com'),
                ])
        for attendee in attendee_event.attendees:
            self.assertEqual(attendee.status, 'accepted')

    def test0070delete_attendee(self):
        'Delete attendee'
        for event in self.calendar.events():
            event.load()
            value = event.instance.vevent.summary.value
            if value == 'Test event with attendee':
                break
        event.instance.vevent.attendee_list = []
        event.save()

        Event = Model.get('calendar.event')
        self.assertEqual(Event.find([
                    ('calendar.owner.email', '=', 'foo@example.com'),
                    ]), [])

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--xmlrpc', dest='xmlrpc', metavar='URL',
        help='use trytond XML-RPC at URL')
    parser.add_argument('--url', dest='url', metavar='URL',
        help='use calendar at URL')
    options = parser.parse_args()
    config = config.set_xmlrpc(options.xmlrpc)
    xmlrpc_user = urlparse(options.xmlrpc).username
    user = urlparse(options.url).username
    assert xmlrpc_user == user
    assert user != 'foo'
    activate_module('calendar', config)
    configure_user(user, config)
    configure_user('foo', config)
    configure_user('bar', config)
    create_calendar(user, user, config)
    create_calendar('foo', user, config)
    create_calendar('bar', user, config)
    URL = options.url
    unittest.main(argv=sys.argv[:1])
