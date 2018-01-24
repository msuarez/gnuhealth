#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
#
#    Thalamus, the GNU Health Federation Message and Authentication Server
#
#                  Thalamus is part of the GNU Health project
#
##############################################################################
#
#    Copyright (C) 2008 - 2018 Luis Falcon <lfalcon@gnusolidario.org>
#    Copyright (C) 2008 - 2018 GNU Solidario <health@gnusolidario.org>
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

from setuptools import setup, find_packages

long_desc = open('README.rst').read()

lic = open('LICENSE').read()

version = open('version').read().strip()

setup(name='thalamus',
    version=version,
    description = 'The GNU Health Federation Message and Authentication Server',
    keywords='health API REST',
    long_description = long_desc,
    platforms='any',
    author='GNU Solidario',
    author_email='health@gnusolidario.org',
    url='http://health.gnu.org',
    download_url='http://ftp.gnu.org/gnu/health',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        ],
    license=lic,
    install_requires = [
        "flask", 
        "flask_httpauth",
        "flask_restful",
        "flask_pymongo",
        "bcrypt",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
 )      

