import sys
import os
from setuptools import setup, Command

NAME = "gnu_health_fhir"

with open("README.md") as readme:
    README = readme.read()
    README_TYPE = "text/markdown"

with open(os.path.join(NAME, "VERSION")) as version:
    VERSION = version.readlines()[0].strip()

with open("requirements.txt") as requirements:
    REQUIREMENTS = [line.rstrip() for line in requirements if line != "\n"]

setup(
    name="gnu_health_fhir",
    version=VERSION,
    description="Provides FHIR interface to GNU Health.",
    long_description=README,
    long_description_content_type=README_TYPE,
    url="https://github.com/teffalump/gnu_health_fhir",
    author="teffalump",
    author_email="chris@teffalump.com",
    packages=["gnu_health_fhir"],
    install_requires=REQUIREMENTS,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
