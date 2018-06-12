# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import urllib.parse
import urllib.request, urllib.parse, urllib.error
import string
import xml.dom.minidom
from pywebdav.lib import propfind
from pywebdav.lib.errors import DAV_NotFound, DAV_Error, DAV_Forbidden
from pywebdav.lib.utils import get_uriparentpath
from pywebdav.lib.constants import DAV_VERSION_1, DAV_VERSION_2
from trytond.modules.webdav.protocol import TrytonDAVInterface, LOCAL, \
        WebDAVAuthRequestHandler
from trytond.pool import Pool
from trytond.transaction import Transaction

domimpl = xml.dom.minidom.getDOMImplementation()

TrytonDAVInterface.PROPS['urn:ietf:params:xml:ns:caldav'] = (
    'calendar-description',
    'calendar-data',
    'calendar-home-set',
    'calendar-user-address-set',
    'schedule-inbox-URL',
    'schedule-outbox-URL',
    )
TrytonDAVInterface.PROPS['DAV:'] = tuple(list(TrytonDAVInterface.PROPS['DAV:'])
    + ['principal-collection-set'])
TrytonDAVInterface.M_NS['urn:ietf:params:xml:ns:caldav'] = '_get_caldav'
DAV_VERSION_1['version'] += ',calendar-access,calendar-schedule'
DAV_VERSION_2['version'] += ',calendar-access,calendar-schedule'

_mk_prop_response = propfind.PROPFIND.mk_prop_response


def mk_prop_response(self, uri, good_props, bad_props, doc):
    res = _mk_prop_response(self, uri, good_props, bad_props, doc)
    if not isinstance(uri, str):
        uri = uri.decode()
    parent_uri = get_uriparentpath(uri and uri.strip('/') or '')
    if not parent_uri:
        return res
    dbname, parent_uri = TrytonDAVInterface.get_dburi(parent_uri)
    if parent_uri in ('Calendars', 'Calendars/'):
        ad = doc.createElement('calendar')
        ad.setAttribute('xmlns', 'urn:ietf:params:xml:ns:caldav')
        # Disable groupdav attribute for iPhone
        # vc = doc.createElement('vevent-collection')
        # vc.setAttribute('xmlns', 'http://groupdav.org/')
        cols = res.getElementsByTagName('D:collection')
        if cols:
            cols[0].parentNode.appendChild(ad)
            # cols[0].parentNode.appendChild(vc)
    return res

propfind.PROPFIND.mk_prop_response = mk_prop_response


def _get_caldav_calendar_description(self, uri):
    dbname, dburi = self._get_dburi(uri)
    if not dbname:
        raise DAV_NotFound
    pool = Pool(Transaction().database.name)
    try:
        Collection = pool.get('webdav.collection')
    except KeyError:
        raise DAV_NotFound
    if not getattr(Collection, 'get_calendar_description', None):
        raise DAV_NotFound
    try:
        res = Collection.get_calendar_description(dburi, cache=LOCAL.cache)
    except DAV_Error as exception:
        self._log_exception(exception)
        raise
    except Exception as exception:
        self._log_exception(exception)
        raise DAV_Error(500)
    return res

TrytonDAVInterface._get_caldav_calendar_description = \
    _get_caldav_calendar_description


def _get_caldav_calendar_data(self, uri):
    dbname, dburi = self._get_dburi(uri)
    if not dbname:
        raise DAV_NotFound
    pool = Pool(Transaction().database.name)
    try:
        Collection = pool.get('webdav.collection')
    except KeyError:
        raise DAV_NotFound
    if not getattr(Collection, 'get_calendar_data', None):
        raise DAV_NotFound
    try:
        res = Collection.get_calendar_data(dburi, cache=LOCAL.cache)
    except DAV_Error as exception:
        self._log_exception(exception)
        raise
    except Exception as exception:
        self._log_exception(exception)
        raise DAV_Error(500)
    return res

TrytonDAVInterface._get_caldav_calendar_data = _get_caldav_calendar_data


def _get_caldav_calendar_home_set(self, uri):
    dbname, dburi = self._get_dburi(uri)
    if not dbname:
        raise DAV_NotFound
    pool = Pool(Transaction().database.name)
    try:
        Collection = pool.get('webdav.collection')
    except KeyError:
        raise DAV_NotFound
    if not getattr(Collection, 'get_calendar_home_set', None):
        raise DAV_NotFound
    try:
        res = Collection.get_calendar_home_set(dburi, cache=LOCAL.cache)
    except DAV_Error as exception:
        self._log_exception(exception)
        raise
    except Exception as exception:
        self._log_exception(exception)
        raise DAV_Error(500)
    uparts = list(urllib.parse.urlsplit(uri))
    uparts[2] = urllib.parse.quote(dbname + res)
    doc = domimpl.createDocument(None, 'href', None)
    href = doc.documentElement
    href.tagName = 'D:href'
    # iPhone doesn't handle "http" in href
    # huri = doc.createTextNode(urlparse.urlunsplit(uparts))
    huri = doc.createTextNode(urllib.parse.quote('/' + dbname + res))
    href.appendChild(huri)
    return href

TrytonDAVInterface._get_caldav_calendar_home_set = \
    _get_caldav_calendar_home_set


def _get_caldav_calendar_user_address_set(self, uri):
    dbname, dburi = self._get_dburi(uri)
    if not dbname:
        raise DAV_NotFound
    pool = Pool(Transaction().database.name)
    try:
        Collection = pool.get('webdav.collection')
    except KeyError:
        raise DAV_NotFound
    if not getattr(Collection, 'get_calendar_user_address_set', None):
        raise DAV_NotFound
    try:
        res = Collection.get_calendar_user_address_set(
            dburi, cache=LOCAL.cache)
    except DAV_Error as exception:
        self._log_exception(exception)
        raise
    except Exception as exception:
        self._log_exception(exception)
        raise DAV_Error(500)
    doc = domimpl.createDocument(None, 'href', None)
    href = doc.documentElement
    href.tagName = 'D:href'
    huri = doc.createTextNode('MAILTO:' + res)
    href.appendChild(huri)
    return href

TrytonDAVInterface._get_caldav_calendar_user_address_set = \
    _get_caldav_calendar_user_address_set


def _get_caldav_schedule_inbox_URL(self, uri):
    dbname, dburi = self._get_dburi(uri)
    if not dbname:
        raise DAV_NotFound
    pool = Pool(Transaction().database.name)
    try:
        Collection = pool.get('webdav.collection')
    except KeyError:
        raise DAV_NotFound
    if not getattr(Collection, 'get_schedule_inbox_URL', None):
        raise DAV_NotFound
    try:
        res = Collection.get_schedule_inbox_URL(dburi, cache=LOCAL.cache)
    except DAV_Error as exception:
        self._log_exception(exception)
        raise
    except Exception as exception:
        self._log_exception(exception)
        raise DAV_Error(500)
    uparts = list(urllib.parse.urlsplit(uri))
    uparts[2] = urllib.parse.quote(dbname + res)
    doc = domimpl.createDocument(None, 'href', None)
    href = doc.documentElement
    href.tagName = 'D:href'
    huri = doc.createTextNode(urllib.parse.urlunsplit(uparts))
    href.appendChild(huri)
    return href

TrytonDAVInterface._get_caldav_schedule_inbox_URL = \
    _get_caldav_schedule_inbox_URL


def _get_caldav_schedule_outbox_URL(self, uri):
    dbname, dburi = self._get_dburi(uri)
    if not dbname:
        raise DAV_NotFound
    pool = Pool(Transaction().database.name)
    try:
        Collection = pool.get('webdav.collection')
    except KeyError:
        raise DAV_NotFound
    if not getattr(Collection, 'get_schedule_outbox_URL', None):
        raise DAV_NotFound
    try:
        res = Collection.get_schedule_outbox_URL(dburi, cache=LOCAL.cache)
    except DAV_Error as exception:
        self._log_exception(exception)
        raise
    except Exception as exception:
        self._log_exception(exception)
        raise DAV_Error(500)
    uparts = list(urllib.parse.urlsplit(uri))
    uparts[2] = urllib.parse.quote(dbname + res)
    doc = domimpl.createDocument(None, 'href', None)
    href = doc.documentElement
    href.tagName = 'D:href'
    huri = doc.createTextNode(urllib.parse.urlunsplit(uparts))
    href.appendChild(huri)
    return href

TrytonDAVInterface._get_caldav_schedule_outbox_URL = \
    _get_caldav_schedule_outbox_URL

_prev_get_dav_principal_collection_set = hasattr(TrytonDAVInterface,
        '_get_dav_principal_collection_set') and \
                TrytonDAVInterface._get_dav_principal_collection_set or None


def _get_dav_principal_collection_set(self, uri):
    dbname, dburi = self._get_dburi(uri)
    if dburi.startswith('Calendars'):
        uparts = list(urllib.parse.urlsplit(uri.decode()))
        uparts[2] = urllib.parse.quote(dbname + '/Calendars/')
        doc = domimpl.createDocument(None, 'href', None)
        href = doc.documentElement
        href.tagName = 'D:href'
        huri = doc.createTextNode(urllib.parse.urlunsplit(uparts))
        href.appendChild(huri)
        return href
    if _prev_get_dav_principal_collection_set:
        return _prev_get_dav_principal_collection_set(self, uri)
    raise DAV_NotFound

TrytonDAVInterface._get_dav_principal_collection_set = \
    _get_dav_principal_collection_set


def _get_caldav_post(self, uri, body, contenttype=''):
    dbname, dburi = self._get_dburi(uri)
    if not dbname:
        raise DAV_Forbidden
    pool = Pool(Transaction().database.name)
    Calendar = pool.get('calendar.calendar')
    if not getattr(Calendar, 'post', None):
        raise DAV_NotFound
    try:
        res = Calendar.post(dburi, body)
    except DAV_Error as exception:
        self._log_exception(exception)
        raise
    except Exception as exception:
        self._log_exception(exception)
        raise DAV_Error(500)
    return res

TrytonDAVInterface._get_caldav_post = _get_caldav_post

_prev_do_POST = WebDAVAuthRequestHandler.do_POST


def do_POST(self):
    dc = self.IFACE_CLASS

    uri = urllib.parse.urljoin(self.get_baseuri(dc), self.path)
    uri = urllib.parse.unquote(uri)

    dbname, dburi = TrytonDAVInterface.get_dburi(uri)
    if dburi.startswith('Calendars'):
        # read the body
        body = None
        if 'Content-Length' in self.headers:
            l = self.headers['Content-Length']
            body = self.rfile.read(int(l))
        ct = None
        if 'Content-Type' in self.headers:
            ct = self.headers['Content-Type']

        try:
            DATA = '%s\n' % dc._get_caldav_post(uri, body, ct)
        except DAV_Error as exception:
            ec, _ = exception
            return self.send_status(ec)
        self.send_body(DATA, 200, 'OK', 'OK')
        return
    return _prev_do_POST(self)

WebDAVAuthRequestHandler.do_POST = do_POST
