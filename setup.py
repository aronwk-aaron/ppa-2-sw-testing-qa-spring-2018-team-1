#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='app',
    version='1.0.0',
    description='For doing various things',
    long_description=__doc__,
    author='',
    author_email='',
    license='MIT',
    url='https://github.com/drbyron-github-classroom/ppa-2-sw-testing-qa-spring-2018-team-1',
    packages=find_packages(),
    install_requires=[
        'click',
        'Flask',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
