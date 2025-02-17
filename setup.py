#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

from setuptools import setup
import os
from os.path import join

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as history_file:
    history = history_file.read()


# Installed by pip install squid-py
# or pip install -e .
install_requirements = [
    'coloredlogs',
    'PyYAML>=4.2b1',
]

# Required to run setup.py:
setup_requirements = ['pytest-runner', ]

test_requirements = [
    'codacy-coverage',
    'coverage',
    'docker',
    'mccabe',
    'pylint',
    'pytest',
    'pytest-watch',
    'tox',
]

# Possibly required by developers of squid-py:
dev_requirements = [
    'bumpversion',
    'pkginfo',
    'twine',
    'watchdog',
]

docs_requirements = [
    'Sphinx',
    'sphinxcontrib-apidoc',
]

packages = []
for d, _, _ in os.walk('osmosis_on_premise_driver'):
    if os.path.exists(join(d, '__init__.py')):
        packages.append(d.replace(os.path.sep, '.'))

setup(
    author="marcojrfurtado",
    author_email='devops@oceanprotocol.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="💧 Osmosis On Premise Driver Implementation",
    extras_require={
        'test': test_requirements,
        'dev': dev_requirements + test_requirements + docs_requirements,
        'docs': docs_requirements,
    },
    install_requires=install_requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='osmosis-on-premise-driver-plus',
    name='osmosis-on-premise-driver-plus',
    packages=packages,
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/marcojrfurtado/osmosis-on-premise-driver-plus',
    version='0.0.6',
    zip_safe=False,
)
