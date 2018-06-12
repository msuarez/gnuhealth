# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import vobject
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urlparse
from sql.functions import Extract
from sql.conditionals import Coalesce
from sql.aggregate import Max

from pywebdav.lib.errors import DAV_NotFound, DAV_Forbidden
from trytond.tools import reduce_ids, grouped_slice
from trytond.cache import Cache
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta

__all__ = ['Collection']

CALDAV_NS = 'urn:ietf:params:xml:ns:caldav'


def _comp_filter_domain(dtstart, dtend):
    return ['OR',
        [
            ['OR',
                [('dtstart', '<=', dtstart),
                    ('dtend', '>=', dtstart)],
                [('dtstart', '<=', dtend),
                    ('dtend', '>=', dtend)],
                [('dtstart', '>=', dtstart),
                    ('dtend', '<=', dtend)],
                [('dtstart', '>=', dtstart),
                    ('dtstart', '<=', dtend),
                    ('dtend', '=', None)]],
            ('parent', '=', None),
            ('rdates', '=', None),
            ('rrules', '=', None),
            ('exdates', '=', None),
            ('exrules', '=', None),
            ('occurences', '=', None),
            ],
        [  # TODO manage better recurring event
            ('parent', '=', None),
            ('dtstart', '<=', dtend),
            ['OR',
                ('rdates', '!=', None),
                ('rrules', '!=', None),
                ('exdates', '!=', None),
                ('exrules', '!=', None),
                ('occurences', '!=', None),
                ]
            ]]


class Collection(metaclass=PoolMeta):
    __name__ = "webdav.collection"
    _event_cache = Cache('webdav_collection.event')

    @staticmethod
    def calendar(uri, ics=False):
        '''
        Return the calendar id in the uri
        '''
        Calendar = Pool().get('calendar.calendar')

        if uri and uri.startswith('Calendars/'):
            calendar, uri = (uri[10:].split('/', 1) + [None])[0:2]
            if ics:
                if calendar.endswith('.ics'):
                    calendar = calendar[:-4]
                else:
                    return None
            return Calendar.get_name(calendar)

    @classmethod
    def event(cls, uri, calendar_id=False):
        '''
        Return the event id in the uri
        '''
        Event = Pool().get('calendar.event')

        key = (uri, calendar_id)
        event_id = cls._event_cache.get(key, default=-1)
        if event_id != -1:
            return event_id
        else:
            event_id = None
        if uri and uri.startswith('Calendars/'):
            calendar, event_uri = (uri[10:].split('/', 1) + [None])[0:2]
            if not calendar_id:
                calendar_id = cls.calendar(uri)
                if not calendar_id:
                    return None
            events = Event.search([
                    ('calendar', '=', calendar_id),
                    ('uuid', '=', event_uri[:-4]),
                    ('parent', '=', None),
                    ], limit=1)
            if events:
                event_id = events[0].id
        cls._event_cache.set(key, event_id)
        return event_id

    @staticmethod
    def _caldav_filter_domain_calendar(filter):
        '''
        Return a domain for caldav filter on calendar
        '''
        if not filter:
            return []
        if filter.localName == 'principal-property-search':
            return [('id', '=', 0)]
        return [('id', '=', 0)]

    @classmethod
    def _caldav_filter_domain_event(cls, filter):
        '''
        Return a domain for caldav filter on event
        '''
        res = []
        if not filter:
            return []
        if filter.localName == 'principal-property-search':
            return [('id', '=', 0)]
        elif filter.localName == 'calendar-query':
            result = []
            calendar_filter = None
            for e in filter.childNodes:
                if e.nodeType == e.TEXT_NODE:
                    continue
                if e.localName == 'filter':
                    calendar_filter = e
                    break
            if calendar_filter is None:
                return []
            for vcalendar_filter in calendar_filter.childNodes:
                if vcalendar_filter.nodeType == vcalendar_filter.TEXT_NODE:
                    continue
                if vcalendar_filter.getAttribute('name') != 'VCALENDAR':
                    return [('id', '=', 0)]
                vevent_filter = None
                for vevent_filter in vcalendar_filter.childNodes:
                    if vevent_filter.nodeType == vevent_filter.TEXT_NODE:
                        vevent_filter = None
                        continue
                    if vevent_filter.localName == 'comp-filter':
                        if vevent_filter.getAttribute('name') != 'VEVENT':
                            vevent_filter = None
                            continue
                        for comp_filter in vevent_filter.childNodes:
                            if comp_filter.localName != 'time-range':
                                continue
                            start = comp_filter.getAttribute('start')
                            if start:
                                start = vobject.icalendar.stringToDateTime(start)
                                end = comp_filter.getAttribute('end')
                            if end:
                                end = vobject.icalendar.stringToDateTime(end)

                            result.append(_comp_filter_domain(start, end))
                        break
                if vevent_filter is None:
                    return [('id', '=', 0)]
                break
            return result
        elif filter.localName == 'calendar-multiget':
            ids = []
            for e in filter.childNodes:
                if e.nodeType == e.TEXT_NODE:
                    continue
                if e.localName == 'href':
                    if not e.firstChild:
                        continue
                    uri = urlparse(e.firstChild.data).path
                    dbname, uri = (uri.lstrip('/').split('/', 1) + [None])[0:2]

                    if not dbname:
                        continue
                    dbname == urllib.parse.unquote_plus(dbname)
                    if dbname != Transaction().database.name:
                        continue
                    if uri:
                        uri = urllib.parse.unquote_plus(uri)
                    event_id = cls.event(uri)
                    if event_id:
                        ids.append(event_id)
            return [('id', 'in', ids)]
        return res

    @classmethod
    def get_childs(cls, uri, filter=None, cache=None):
        pool = Pool()
        Calendar = pool.get('calendar.calendar')
        Event = pool.get('calendar.event')

        if uri in ('Calendars', 'Calendars/'):
            domain = cls._caldav_filter_domain_calendar(filter)
            domain = [['OR',
                    ('owner', '=', Transaction().user),
                    ('read_users', '=', Transaction().user),
                    ],
                domain]
            calendars = Calendar.search(domain)
            if cache is not None:
                cache.setdefault('_calendar', {})
                cache['_calendar'].setdefault(Calendar.__name__, {})
                for calendar in calendars:
                    cache['_calendar'][Calendar.__name__][calendar.id] = {}
            return ([x.name for x in calendars]
                + [x.name + '.ics' for x in calendars])
        if uri and uri.startswith('Calendars/'):
            calendar_id = cls.calendar(uri)
            if calendar_id and not (uri[10:].split('/', 1) + [None])[1]:
                domain = cls._caldav_filter_domain_event(filter)
                events = Event.search([
                        ('calendar', '=', calendar_id),
                        domain,
                        ])
                if cache is not None:
                    cache.setdefault('_calendar', {})
                    cache['_calendar'].setdefault(Event.__name__, {})
                    for event in events:
                        cache['_calendar'][Event.__name__][event.id] = {}
                return [x.uuid + '.ics' for x in events]
            return []
        childs = super(Collection, cls).get_childs(uri, filter=filter,
            cache=cache)
        if not uri and not filter:
            childs.append('Calendars')
        elif not uri and filter:
            if filter.localName == 'principal-property-search':
                childs.append('Calendars')
        return childs

    @classmethod
    def get_resourcetype(cls, uri, cache=None):
        from pywebdav.lib.constants import COLLECTION, OBJECT
        if uri in ('Calendars', 'Calendars/'):
            return COLLECTION
        calendar_id = cls.calendar(uri)
        if calendar_id:
            if not (uri[10:].split('/', 1) + [None])[1]:
                return COLLECTION
            return OBJECT
        elif cls.calendar(uri, ics=True):
            return OBJECT
        return super(Collection, cls).get_resourcetype(uri, cache=cache)

    @classmethod
    def get_displayname(cls, uri, cache=None):
        Calendar = Pool().get('calendar.calendar')
        if uri in ('Calendars', 'Calendars/'):
            return 'Calendars'
        calendar_id = cls.calendar(uri)
        if calendar_id:
            if not (uri[10:].split('/', 1) + [None])[1]:
                return Calendar(calendar_id).rec_name
            return uri.split('/')[-1]
        elif cls.calendar(uri, ics=True):
            return uri.split('/')[-1]
        return super(Collection, cls).get_displayname(uri, cache=cache)

    @classmethod
    def get_contenttype(cls, uri, cache=None):
        if cls.event(uri) \
                or cls.calendar(uri, ics=True):
            return 'text/calendar'
        return super(Collection, cls).get_contenttype(uri, cache=cache)

    @classmethod
    def get_creationdate(cls, uri, cache=None):
        Calendar = Pool().get('calendar.calendar')
        Event = Pool().get('calendar.event')
        calendar = Calendar.__table__()
        event = Event.__table__()

        calendar_id = cls.calendar(uri)
        if not calendar_id:
            calendar_id = cls.calendar(uri, ics=True)
        if calendar_id:
            if not (uri[10:].split('/', 1) + [None])[1]:
                if cache is not None:
                    cache.setdefault('_calendar', {})
                    cache['_calendar'].setdefault(Calendar.__name__, {})
                    ids = list(cache['_calendar'][Calendar.__name__].keys())
                    if calendar_id not in ids:
                        ids.append(calendar_id)
                    elif 'creationdate' in cache['_calendar'][
                            Calendar.__name__][calendar_id]:
                        return cache['_calendar'][Calendar.__name__][
                            calendar_id]['creationdate']
                else:
                    ids = [calendar_id]
                res = None
                cursor = Transaction().connection.cursor()
                for sub_ids in grouped_slice(ids):
                    red_sql = reduce_ids(calendar.id, sub_ids)
                    cursor.execute(*calendar.select(calendar.id,
                            Extract('EPOCH', calendar.create_date),
                            where=red_sql))
                    for calendar_id2, date in cursor.fetchall():
                        if calendar_id2 == calendar_id:
                            res = date
                        if cache is not None:
                            cache['_calendar'][Calendar.__name__]\
                                .setdefault(calendar_id2, {})
                            cache['_calendar'][Calendar.__name__][
                                calendar_id2]['creationdate'] = date
                if res is not None:
                    return res
            else:
                event_id = cls.event(uri, calendar_id=calendar_id)
                if event_id:
                    if cache is not None:
                        cache.setdefault('_calendar', {})
                        cache['_calendar'].setdefault(Event.__name__, {})
                        ids = list(cache['_calendar'][Event.__name__].keys())
                        if event_id not in ids:
                            ids.append(event_id)
                        elif 'creationdate' in cache['_calendar'][
                                Event.__name__][event_id]:
                            return cache['_calendar'][Event.__name__][
                                event_id]['creationdate']
                    else:
                        ids = [event_id]
                    res = None
                    cursor = Transaction().connection.cursor()
                    for sub_ids in grouped_slice(ids):
                        red_sql = reduce_ids(event.id, sub_ids)
                        cursor.execute(*event.select(event.id,
                                Extract('EPOCH', event.create_date),
                                where=red_sql))
                        for event_id2, date in cursor.fetchall():
                            if event_id2 == event_id:
                                res = date
                            if cache is not None:
                                cache['_calendar'][Event.__name__]\
                                    .setdefault(event_id2, {})
                                cache['_calendar'][Event.__name__][
                                    event_id2]['creationdate'] = date
                    if res is not None:
                        return res
        return super(Collection, cls).get_creationdate(uri, cache=cache)

    @classmethod
    def get_lastmodified(cls, uri, cache=None):
        pool = Pool()
        Calendar = pool.get('calendar.calendar')
        Event = pool.get('calendar.event')
        calendar = Calendar.__table__()
        event = Event.__table__()

        transaction = Transaction()
        cursor = transaction.connection.cursor()
        calendar_id = cls.calendar(uri)
        if calendar_id:
            if not (uri[10:].split('/', 1) + [None])[1]:
                if cache is not None:
                    cache.setdefault('_calendar', {})
                    cache['_calendar'].setdefault(Calendar.__name__, {})
                    ids = list(cache['_calendar'][Calendar.__name__].keys())
                    if calendar_id not in ids:
                        ids.append(calendar_id)
                    elif 'lastmodified' in cache['_calendar'][
                            Calendar.__name__][calendar_id]:
                        return cache['_calendar'][Calendar.__name__][
                            calendar_id]['lastmodified']
                else:
                    ids = [calendar_id]
                res = None
                for sub_ids in grouped_slice(ids):
                    red_sql = reduce_ids(calendar.id, sub_ids)
                    cursor.execute(*calendar.select(calendar.id,
                            Extract('EPOCH', Coalesce(calendar.write_date,
                                    calendar.create_date)),
                            where=red_sql))
                    for calendar_id2, date in cursor.fetchall():
                        if calendar_id2 == calendar_id:
                            res = date
                        if cache is not None:
                            cache['_calendar'][Calendar.__name__]\
                                .setdefault(calendar_id2, {})
                            cache['_calendar'][Calendar.__name__][
                                calendar_id2]['lastmodified'] = date
                if res is not None:
                    return res
            else:
                event_id = cls.event(uri, calendar_id=calendar_id)
                if event_id:
                    if cache is not None:
                        cache.setdefault('_calendar', {})
                        cache['_calendar'].setdefault(Event.__name__, {})
                        ids = list(cache['_calendar'][Event.__name__].keys())
                        if event_id not in ids:
                            ids.append(event_id)
                        elif 'lastmodified' in cache['_calendar'][
                                Event.__name__][event_id]:
                            return cache['_calendar'][Event.__name__][
                                event_id]['lastmodified']
                    else:
                        ids = [event_id]
                    res = None
                    # for sub_ids in grouped_slice(ids,
                    #        transaction.database.IN_MAX / 2):
                    for sub_ids in grouped_slice(ids):
                        red_id_sql = reduce_ids(event.id, sub_ids)
                        red_parent_sql = reduce_ids(event.parent, sub_ids)
                        cursor.execute(*event.select(
                                Coalesce(event.parent, event.id),
                                Max(Extract('EPOCH', Coalesce(event.write_date,
                                            event.create_date))),
                                where=red_id_sql | red_parent_sql,
                                group_by=(event.parent, event.id)))
                        for event_id2, date in cursor.fetchall():
                            if event_id2 == event_id:
                                res = date
                            if cache is not None:
                                cache['_calendar'][Event.__name__]\
                                    .setdefault(event_id2, {})
                                cache['_calendar'][Event.__name__][
                                    event_id2]['lastmodified'] = date
                    if res is not None:
                        return res
        calendar_ics_id = cls.calendar(uri, ics=True)
        if calendar_ics_id:
            if cache is not None:
                cache.setdefault('_calendar', {})
                cache['_calendar'].setdefault(Calendar.__name__, {})
                ids = list(cache['_calendar'][Calendar.__name__].keys())
                if calendar_ics_id not in ids:
                    ids.append(calendar_ics_id)
                elif 'lastmodified ics' in cache['_calendar'][
                        Calendar.__name__][calendar_ics_id]:
                    return cache['_calendar'][Calendar.__name__][
                        calendar_ics_id]['lastmodified ics']
            else:
                ids = [calendar_ics_id]
            res = None
            for sub_ids in grouped_slice(ids):
                red_sql = reduce_ids(event.calendar, sub_ids)
                cursor.execute(*event.select(event.calendar,
                        Max(Extract('EPOCH', Coalesce(event.write_date,
                                    event.create_date))),
                        where=red_sql,
                        group_by=event.calendar))
                for calendar_id2, date in cursor.fetchall():
                    if calendar_id2 == calendar_ics_id:
                        res = date
                    if cache is not None:
                        cache['_calendar'][Calendar.__name__]\
                            .setdefault(calendar_id2, {})
                        cache['_calendar'][Calendar.__name__][
                            calendar_id2]['lastmodified ics'] = date
            if res is not None:
                return res
        return super(Collection, cls).get_lastmodified(uri, cache=cache)

    @classmethod
    def get_data(cls, uri, cache=None):
        pool = Pool()
        Event = pool.get('calendar.event')
        Calendar = pool.get('calendar.calendar')

        calendar_id = cls.calendar(uri)
        if calendar_id:
            if not (uri[10:].split('/', 1) + [None])[1]:
                raise DAV_NotFound
            event_id = cls.event(uri, calendar_id=calendar_id)
            if not event_id:
                raise DAV_NotFound
            ical = Event(event_id).event2ical()
            return ical.serialize()
        calendar_ics_id = cls.calendar(uri, ics=True)
        if calendar_ics_id:
            ical = Calendar(calendar_ics_id).calendar2ical()
            return ical.serialize()
        return super(Collection, cls).get_data(uri, cache=cache)

    @classmethod
    def get_calendar_description(cls, uri, cache=None):
        Calendar = Pool().get('calendar.calendar')

        calendar_id = cls.calendar(uri)
        if calendar_id:
            if not (uri[10:].split('/', 1) + [None])[1]:
                if cache is not None:
                    cache.setdefault('_calendar', {})
                    cache['_calendar'].setdefault(Calendar.__name__, {})
                    ids = list(cache['_calendar'][Calendar.__name__].keys())
                    if calendar_id not in ids:
                        ids.append(calendar_id)
                    elif 'calendar_description' in cache['_calendar'][
                            Calendar.__name__][calendar_id]:
                        res = cache['_calendar'][Calendar.__name__][
                            calendar_id]['calendar_description']
                        if res is not None:
                            return res
                else:
                    ids = [calendar_id]
                res = None
                for calendar in Calendar.browse(ids):
                    if calendar.id == calendar_id:
                        res = calendar.description
                    if cache is not None:
                        cache['_calendar'][Calendar.__name__]\
                            .setdefault(calendar.id, {})
                        cache['_calendar'][Calendar.__name__][
                            calendar.id]['calendar_description'] = \
                                calendar.description
                if res is not None:
                    return res
        raise DAV_NotFound

    @classmethod
    def get_calendar_data(cls, uri, cache=None):
        return cls.get_data(uri, cache=cache)
        # return cls.get_data(uri, cache=cache).decode('utf-8')

    @staticmethod
    def get_calendar_home_set(uri, cache=None):
        return '/Calendars'

    @staticmethod
    def get_calendar_user_address_set(uri, cache=None):
        User = Pool().get('res.user')
        user = User(Transaction().user)
        if user.email:
            return user.email
        raise DAV_NotFound

    @staticmethod
    def get_schedule_inbox_URL(uri, cache=None):
        Calendar = Pool().get('calendar.calendar')
        user = Transaction().user

        calendars = Calendar.search([
            ('owner', '=', user),
            ], limit=1)
        if not calendars:
            # Sunbird failed with no value
            return '/Calendars'
        calendar, = calendars
        return '/Calendars/' + calendar.name

    @classmethod
    def get_schedule_outbox_URL(cls, uri, cache=None):
        return cls.get_schedule_inbox_URL(uri, cache=cache)

    @classmethod
    def put(cls, uri, data, content_type, cache=None):
        pool = Pool()
        Event = pool.get('calendar.event')
        Calendar = pool.get('calendar.calendar')

        calendar_id = cls.calendar(uri)
        if calendar_id:
            if not (uri[10:].split('/', 1) + [None])[1]:
                raise DAV_Forbidden
            event_id = cls.event(uri, calendar_id=calendar_id)
            if not event_id:
                ical = vobject.readOne(data)
                values = Event.ical2values(None, ical, calendar_id)
                event, = Event.create([values])
                calendar = Calendar(calendar_id)
                return (Transaction().database.name + '/Calendars/' +
                        calendar.name + '/' + event.uuid + '.ics')
            else:
                ical = vobject.readOne(data)
                values = Event.ical2values(event_id, ical, calendar_id)
                Event.write([Event(event_id)], values)
                return
        calendar_ics_id = cls.calendar(uri, ics=True)
        if calendar_ics_id:
            raise DAV_Forbidden
        return super(Collection, cls).put(uri, data, content_type)

    @classmethod
    def mkcol(cls, uri, cache=None):
        if uri and uri.startswith('Calendars/'):
            raise DAV_Forbidden
        return super(Collection, cls).mkcol(uri, cache=cache)

    @classmethod
    def rmcol(cls, uri, cache=None):
        Calendar = Pool().get('calendar.calendar')

        calendar_id = cls.calendar(uri)
        if calendar_id:
            if not (uri[10:].split('/', 1) + [None])[1]:
                try:
                    Calendar.delete([Calendar(calendar_id)])
                except Exception:
                    raise DAV_Forbidden
                return 200
            raise DAV_Forbidden
        return super(Collection, cls).rmcol(uri, cache=cache)

    @classmethod
    def rm(cls, uri, cache=None):
        Event = Pool().get('calendar.event')

        calendar_id = cls.calendar(uri)
        if calendar_id:
            if not (uri[10:].split('/', 1) + [None])[1]:
                return 403
            event_id = cls.event(uri, calendar_id=calendar_id)
            if event_id:
                try:
                    Event.delete([Event(event_id)])
                except Exception:
                    return 403
                return 200
            return 404
        calendar_ics_id = cls.calendar(uri, ics=True)
        if calendar_ics_id:
            return 403
        return super(Collection, cls).rm(uri, cache=cache)

    @classmethod
    def exists(cls, uri, cache=None):
        if uri in ('Calendars', 'Calendars/'):
            return 1
        calendar_id = cls.calendar(uri)
        if calendar_id:
            if not (uri[10:].split('/', 1) + [None])[1]:
                return 1
            if cls.event(uri, calendar_id=calendar_id):
                return 1
        calendar_ics_id = cls.calendar(uri, ics=True)
        if calendar_ics_id:
            return 1
        return super(Collection, cls).exists(uri, cache=cache)

    @classmethod
    def current_user_privilege_set(cls, uri, cache=None):
        '''
        Return the privileges of the current user for uri
        Privileges ares: create, read, write, delete
        '''
        Calendar = Pool().get('calendar.calendar')

        if uri in ('Calendars', 'Calendars/'):
            return ['create', 'read', 'write', 'delete']
        if uri and uri.startswith('Calendars/'):
            calendar_id = cls.calendar(uri)
            if calendar_id:
                calendar = Calendar(calendar_id)
                user = Transaction().user
                if user == calendar.owner.id:
                    return ['create', 'read', 'write', 'delete']
                res = []
                if user in (x.id for x in calendar.read_users):
                    res.append('read')
                if user in (x.id for x in calendar.write_users):
                    res.extend(['read', 'write', 'delete'])
                return res
            return []
        return super(Collection, cls).current_user_privilege_set(uri,
            cache=cache)
