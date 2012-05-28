#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

import re
from setuptools import setup

info = eval(open('__tryton__.py').read())
major_version, minor_version = 2, 4

requires = []
for dep in info.get('depends', []):
    if dep.startswith('health'):
        requires.append('trytond_%s == %s' %
            (dep, info.get('version')))
    elif not re.match(r'(ir|res|workflow|webdav)(\W|$)', dep):
        requires.append('trytond_%s >= %s.%s, < %s.%s' %
            (dep, major_version, minor_version, major_version,
                minor_version + 1))
requires.append('trytond >= %s.%s, < %s.%s' %
    (major_version, minor_version, major_version, minor_version + 1))

setup(name='trytond_health_mdg6',
    version=info.get('version', '0.0.1'),
    description=info.get('description', ''),
    author=info.get('author', ''),
    author_email=info.get('email', ''),
    url=info.get('website', ''),
    download_url='http://ftp.gnu.org/gnu/health/',
    package_dir={'trytond.modules.health_mdg6': '.'},
    packages=[
        'trytond.modules.health_mdg6',
        ],
    package_data={
        'trytond.modules.health_mdg6': info.get('xml', []) \
            + info.get('translation', []) \
            + ['report/*.odt', 'icons/*.svg'],

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
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        ],
    license='GPL-3',
    install_requires=requires,
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    health_mdg6 = trytond.modules.health_mdg6
    """,
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
    )
