#!/usr/bin/env python

from __future__ import absolute_import
from setuptools import setup, find_packages
from io import open

VERSION = open('VERSION', 'r', encoding='utf-8').read()
VERSION = VERSION.replace('\n', '')

CHANGES = open('doc/Changes', 'r', encoding='utf-8').read()

DOC = """

Port from Andrew Leech PyWebDAV3 library to Support GNU Health.

It has been tested under Tryton server and Python3.

Some of the clients known to work:

- Mozilla Thunderbird (Lightning)
- Cadaver
- Konqueror
- Evolution

Changes
=======

%s
""" % CHANGES

setup(name='PyWebDAV3-GNUHealth',
      description='WebDAV library for Python3 - GNU Health port',
      author='GNU Solidario',
      author_email='health@gnusolidario.org',
      download_url='http://ftp.gnu.org/gnu/health/',
      maintainer='GNU Health team',
      maintainer_email='health@gnusolidario.org',
      url='http://health.gnu.org',
      platforms=['Unix'],
      license='GPL v3',
      version=VERSION,
      long_description=DOC,
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        ],
      keywords=['webdav',
                'GNUHealth',
                'server',
                'dav',
                'standalone',
                'library',
                'gpl',
                'http',
                'rfc2518',
                'rfc 2518'
                ],
      packages=find_packages(),
      zip_safe=False,
      entry_points={
        'console_scripts': ['davserver = pywebdav.server.server:run']
        },
      )
