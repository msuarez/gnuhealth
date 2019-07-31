#!/usr/bin/env python3
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
    url='http://www.gnuhealth.org',
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
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        ],
    platforms='any',
    license='GPL v3+',
    python_requires='>=3.6,<4',
    install_requires=[
        'pycairo',
        "python-dateutil",
        'PyGObject',
        ],
    extras_require={
        'calendar': ['GooCalendar>=0.5'],
        },
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
