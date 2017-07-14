#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    Copyright (C) 2011-2017 Luis Falcon <falcon@gnu.org>
#    Copyright (C) 2011 Cédric Krier

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
major_version, minor_version = 4, 2

requires = ['pytz']

for dep in info.get('depends', []):
    if dep.startswith('health'):
        requires.append('trytond_%s == %s' %
            (dep, info.get('version')))
    elif not re.match(r'(ir|res|webdav)(\W|$)', dep):
        requires.append('trytond_%s >= %s.%s, < %s.%s' %
            (dep, major_version, minor_version, major_version,
                minor_version + 1))
requires.append('trytond >= %s.%s, < %s.%s' %
    (major_version, minor_version, major_version, minor_version + 1))

setup(name='trytond_health_nursing',
    version=info.get('version', '0.0.1'),
    description=info.get('description', 'GNU Health nursing functionality package'),
    long_description=read('README'),
    author='GNU Solidario',
    author_email='health@gnusolidario.org',
    url='http://health.gnu.org',
    download_url='http://ftp.gnu.org/gnu/health/',
    package_dir={'trytond.modules.health_nursing': '.'},
    packages=[
        'trytond.modules.health_nursing',
        'trytond.modules.health_nursing.tests',
        'trytond.modules.health_nursing.report',
        ],

    package_data={
        'trytond.modules.health_nursing': info.get('xml', []) \
            + info.get('translation', []) \
            + ['tryton.cfg', 'view/*.xml', 'doc/*.rst', 'locale/*.po',
               'report/*.odt', 'icons/*.svg'],
        },

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        ],
    license='GPL-3',
    install_requires=requires,
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    health_nursing = trytond.modules.health_nursing
    """,
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
    )
