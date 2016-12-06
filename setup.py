import sys
from setuptools import setup, find_packages
from bitmovin.package_information import NAME, VERSION

__name__ = NAME
__version__ = VERSION
__description__ = 'Python wrapper for the bitmovin API'
__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.com>'
__email__ = 'dominic.miglar@bitmovin.com'
__license__ = 'Unlicense'


if sys.version_info.major < 3 or sys.version_info.minor < 3:
    sys.exit('Sorry, Python versions older than 3.3 are not supported.')


setup(name=__name__,
      version=__version__,
      description=__description__,
      author=__author__,
      author_email=__email__,
      license=__license__,
      packages=find_packages(exclude=['tests.*', 'tests']),
      install_requires=['requests==2.11.1', 'typing==3.5.2.2'],
      include_package_data=True,
      url='https://www.github.com/bitmovin/bitmovin-python/',
      zip_safe=False)
