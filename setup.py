# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import payroll
version = payroll.__version__

setup(
    name='Payroll Management System',
    version=version,
    author='Abhas Mittal',
    author_email='mittalabhas1@gmail.com',
    packages=[
        'payroll',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['payroll/manage.py'],
)
