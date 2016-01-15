#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
#
#    GNU Health: The Free Health and Hospital Information System
#    Copyright (C) 2008-2016 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2011-2016 GNU Solidario <health@gnusolidario.org>
#    Copyright (C) 2015 CRS4
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

from setuptools import setup
import re
import os
import ConfigParser


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

config = ConfigParser.ConfigParser()
config.readfp(open('tryton.cfg'))
info = dict(config.items('tryton'))


for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()
major_version, minor_version = 3, 2

requires = ['python-sql >= 0.4', "hl7apy >= 1.1.2"]

for dep in info.get('depends', []):
    if dep.startswith('health'):
        requires.append('trytond_%s == %s' % (dep, info.get('version')))
    elif not re.match(r'(ir|res|webdav)(\W|$)', dep):
        requires.append('trytond_%s >= %s.%s, < %s.%s' % (dep, major_version, minor_version,
                                                          major_version, minor_version + 1))
requires.append('trytond >= %s.%s, < %s.%s' % (major_version, minor_version, major_version, minor_version + 1))

setup(
    name='hl7',
    version=info.get('version', '0.0.1'),
    description=info.get('description', 'GNU Health HL7 Module'),
    author=info.get('author', 'CRS4 - Healthcare Flows Group'),
    # author_email=info.get('email', 'health@gnusolidario.org'),
    url=info.get('website', 'http://www.crs4.it/healthcare-flows'),
    download_url='http://ftp.gnu.org/gnu/health/',
    package_dir={'trytond.modules.hl7': '.'},
    packages=[
        'trytond.modules.hl7',
        'trytond.modules.hl7.connection',
        'trytond.modules.hl7.tests',
        ],
    package_data={
        'trytond.modules.hl7': info.get('xml', [])
        + info.get('translation', [])
        + ['tryton.cfg', 'view/*.xml', 'doc/*.rst', 'locale/*.po', 'report/*.odt', 'icons/*.svg'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],
    license='GPL-3',
    install_requires=requires,
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    hl7 = trytond.modules.hl7
    """,
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
    )
