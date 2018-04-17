# SUBJECT TO CHANGE

# PPA 2 - Team 1

Software Testing and QA - CSE 4283 - Spring 2018

Professional Practice Assignment 2 - Team 1

[![Coverage Status](https://coveralls.io/repos/github/drbyron-github-classroom/ppa-2-sw-testing-qa-spring-2018-team-1/badge.svg)](https://coveralls.io/github/drbyron-github-classroom/ppa-2-sw-testing-qa-spring-2018-team-1)
[![Build Status](https://travis-ci.org/drbyron-github-classroom/ppa-2-sw-testing-qa-spring-2018-team-1.svg?branch=master)](https://travis-ci.org/drbyron-github-classroom/ppa-2-sw-testing-qa-spring-2018-team-1)

## Getting Started
We are going to be working with: 

| Program                                                                     | Version |
| --------------------------------------------------------------------------- | :-----: |
| [Windows](https://www.microsoft.com/en-us/software-download/windows10)      | 10      | 
| [Python](https://www.python.org/)                                           | 3.6.3   |
| [virtualenvwrapper-win](https://pypi.python.org/pypi/virtualenvwrapper-win) | 1.2.5   |
| [pytest](https://docs.pytest.org/en/latest/)                                | 3.4.0   |

### Install python
Download [Python 3.6.3](https://www.python.org/downloads/release/python-363/) and follow 
the on screen instructions leaving all of the settings as default.

### Installing and setting up virtualenv and installing requirements
We will be using a virtual environment to make things a bit easier.  Python 3 ships with 
support for this (see: `python -m venv -h`), but we are using 
[virtualenvwrapper-win](https://pypi.python.org/pypi/virtualenvwrapper-win) rather than 
directly using the venv package.


**_The following steps assume you have cloned the repo using your preferred method of git 
and navigated to the directory that it is located in_**

``` bash
#install virtualenvwrapper-win using pip
pip install virtualenvwrapper-win

#make a new virtual environment
mkvirtualenv --python=C:\\path\\to\\python3.6\\python.exe -a C:\\path\\to\\ppa-2-sw-testing-qa-spring-2018-team-1 -r requirements.txt ppa-2

```

All of the requirements to run this project will be installed when you create the new virtual 
environment using requirements.txt

The virtual environment will automatically activate when you create it.

### Reference commands:
``` bash
#activate the virtualenv
workon ppa-1

#updating requirements
pip install -r requirements.txt

#leave the virtualenv
deactivate
```

### Running Tests

Use the following command to run the test suite and generate a coverage report:

``` bash
# in the project root:
pytest --pyargs app
```

pytest will automatically discover all tests that follow their naming convention 
(see [here](https://docs.pytest.org/en/latest/goodpractices.html#test-discovery)).