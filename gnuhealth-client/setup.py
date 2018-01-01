#!/usr/bin/env python
# This file if part of the GNU Health GTK Client.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from setuptools import setup, find_packages

long_desc = open('README.rst').read()

version = open('version').read().strip()

name = 'gnuhealth-client'

download_url = 'https://ftp.gnu.org/gnu/health'

setup(name=name,
    version=version,
    description='The GNU Health GTK client',
    long_description=long_desc,
    author='GNU Solidario',
    author_email='health@gnu.org',
    url='http://health.gnu.org',
    download_url=download_url,
    keywords='eHealth ERM HMIS LIMS',
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
    license='GPL v3',
    install_requires=[
        "python-dateutil",
        "chardet",
        ],
    extras_require={
        'cdecimal': ['cdecimal'],
        'calendar': ['GooCalendar'],
        },
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=2.7,<3',
)
