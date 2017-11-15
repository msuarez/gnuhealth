#!/usr/bin/env python

from setuptools import setup
import re
import os
import configparser


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding="UTF-8").read()


def get_require_version(name):
    if minor_version % 2:
        require = '%s >= %s.%s.dev0, < %s.%s'
    else:
        require = '%s >= %s.%s, < %s.%s'
    require %= (name, major_version, minor_version,
        major_version, minor_version + 1)
    return require

config = configparser.ConfigParser()
config.readfp(open('tryton.cfg'))
info = dict(config.items('tryton'))
for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()
version = info.get('version', '0.0.1')
major_version, minor_version, _ = version.split('.', 2)
major_version = int(major_version)
minor_version = int(minor_version)
name = 'trytond_calendar_webdav3'

if minor_version % 2:
    version = '%s.%s.dev0' % (major_version, minor_version)

requires = ['vobject >= 0.8.0', 'PyWebDAV3-GNUHealth >= 0.10.1', 
    'python-dateutil', 'pytz', 'python-sql >= 0.4']
    
for dep in info.get('depends', []):
    if not re.match(r'(ir|res)(\W|$)', dep):
        requires.append(get_require_version('trytond_%s' % dep))
requires.append(get_require_version('trytond'))

setup(name=name,
    version=version,
    description='CalDAV module for GNU Health and Python3',
    long_description=read('README'),
    author='GNU Solidario',
    author_email='health@gnusolidario.org',
    url='http://health.gnu.org',
    download_url='http://ftp.gnu.org/gnu/health/',
    keywords='GNUHealth calendar caldav',
    package_dir={'trytond.modules.calendar': '.'},
    packages=[
        'trytond.modules.calendar',
        'trytond.modules.calendar.tests',
        ],
    package_data={
        'trytond.modules.calendar': (info.get('xml', [])
            + ['tryton.cfg', 'view/*.xml', 'locale/*.po']),
        },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Legal Industry',
        'Intended Audience :: Manufacturing',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: Bulgarian',
        'Natural Language :: Catalan',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Czech',
        'Natural Language :: Dutch',
        'Natural Language :: English',
        'Natural Language :: French',
        'Natural Language :: German',
        'Natural Language :: Hungarian',
        'Natural Language :: Italian',
        'Natural Language :: Polish',
        'Natural Language :: Portuguese (Brazilian)',
        'Natural Language :: Russian',
        'Natural Language :: Slovenian',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Office/Business',
        ],
    license='GPL-3',
    install_requires=requires,
    extras_require={
        'test': ['caldav'],
        },
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    calendar = trytond.modules.calendar
    """,
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
    )
