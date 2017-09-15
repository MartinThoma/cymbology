#!/usr/bin/env python

import os
from os.path import exists
from setuptools import setup

ENCODING = 'utf-8'
PACKAGE_NAME = 'cymbology'

DESCRIPTION = 'financial identifier validation.'

local_directory = os.path.abspath(os.path.dirname(__file__))
version_path = os.path.join(local_directory, PACKAGE_NAME, '_version.py')

version_ns = {}
with open(version_path, 'r', encoding=ENCODING) as f:
    exec(f.read(), {}, version_ns)


def get_requirements(requirement_file):
    requirements = list(
        open(requirement_file, 'r',
             encoding=ENCODING).read().strip().split('\r\n'))
    return requirements


def get_read_me(file_name):
    return open(file_name).read() if exists(file_name) else DESCRIPTION


setup(
    name='PACKAGE_NAME',
    packages=[PACKAGE_NAME],
    description='financial identifier validation.',
    package_data={
        '': ['*.txt', '*.json'],
    },
    license='BSD',
    include_package_data=True,
    version=version_ns['__version__'],
    url='https://github.com/pmart123/cymbology',
    author='Philip Martin',
    author_email='philip.martin2007@gmail.com',
    extras_require={
        'develop': get_requirements('requirements-dev.txt'),
        'test': get_requirements('requirements-test.txt')
    },
    long_description=get_read_me('README.md'),
    zip_safe=False
)
