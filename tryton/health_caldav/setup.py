#!/usr/bin/env python

from setuptools import setup
import re
import os
import configparser


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding="UTF-8").read()

config = configparser.ConfigParser()
config.readfp(open('tryton.cfg'))
info = dict(config.items('tryton'))

for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()
major_version, minor_version = 5, 0

requires = []

for dep in info.get('depends', []):
    if (dep == 'health'):
        requires.append('gnuhealth == %s' % (info.get('version')))

    elif dep.startswith('health_'):
        health_package = dep.split('_',1)[1]
        requires.append('gnuhealth_%s == %s' %
            (health_package, info.get('version')))
    else: 
        if not re.match(r'(ir|res|webdav)(\W|$)', dep):
            requires.append('trytond_%s >= %s.%s, < %s.%s' %
                (dep, major_version, minor_version, major_version,
                    minor_version + 1))


requires = ['PyWebDAV3-GNUHealth >= 0.10.1', 'gnuhealth_webdav3_server']
    

setup(name='gnuhealth_caldav',
    version=info.get('version', '0.0.1'),
    description='CalDAV package for GNU Health and Python3',
    long_description=read('README'),
    author='GNU Solidario',
    author_email='health@gnusolidario.org',
    url='https://www.gnuhealth.org',
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
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Legal Industry',
        'Intended Audience :: Manufacturing',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
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
