# coding: utf-8

from setuptools import setup, find_packages

NAME = 'bitmovin-python'
VERSION = '3.1.1alpha0'
DESCRIPTION = 'Python-Client which enables you to seamlessly integrate the Bitmovin API into your projects. Using this API client requires an active account.'
AUTHOR = 'Bitmovin Inc'
EMAIL = 'support@bitmovin.com'
URL = 'https://github.com/bitmovin/bitmovin-python'
LICENSE = 'MIT'

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ['urllib3 >= 1.15', 'six >= 1.10', 'certifi', 'python-dateutil', 'requests']

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(),
    include_package_data=True,
    license=LICENSE,
    keywords=['Bitmovin', 'Bitmovin API Reference'],
    install_requires=REQUIRES,
    long_description=DESCRIPTION,
)
