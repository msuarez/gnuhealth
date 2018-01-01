#!/usr/bin/env python
# This file if part of the GNU Health GTK Client.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from setuptools import setup, find_packages
import os
import re


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

args = {}

try:
    from babel.messages import frontend as babel

    args['cmdclass'] = {
        'compile_catalog': babel.compile_catalog,
        'extract_messages': babel.extract_messages,
        'init_catalog': babel.init_catalog,
        'update_catalog': babel.update_catalog,
        }

    args['message_extractors'] = {
        'tryton': [
            ('**.py', 'python', None),
            ],
        }

except ImportError:
        pass

package_data = {
    'tryton': ['data/pixmaps/tryton/*.png',
        'data/pixmaps/tryton/*.svg',
        'data/locale/*/LC_MESSAGES/*.mo',
        'data/locale/*/LC_MESSAGES/*.po',
        ]
    }
data_files = []

version = open('version').read().strip()

lic = open('COPYRIGHT')

name = 'gnuhealth-client'

download_url = 'https://ftp.gnu.org/gnu/health'

dist = setup(name=name,
    version=version,
    description='GNU Health GTK client',
    long_description=read('README.rst'),
    author='GNU Solidario',
    author_email='health@gnu.org',
    url='http://health.gnu.org/',
    download_url=download_url,
    keywords='eHealth ERM HMIS LIMS',
    packages=find_packages(),
    package_data=package_data,
    data_files=data_files,
    scripts=['bin/gnuhealth-client'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: GTK',
        'Framework :: Tryton',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        ],
    platforms='any',
    license=lic,
    install_requires=[
        # "pygtk >= 2.6",
        "python-dateutil",
        "chardet",
        ],
    extras_require={
        'cdecimal': ['cdecimal'],
        'calendar': ['GooCalendar'],
        },
    zip_safe=False,
    **args
    )
