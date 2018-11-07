import sys
from setuptools import setup, find_packages

__name__ = 'bitmovin-python'
__version__ = '1.41.0'
__description__ = 'Python wrapper for the bitmovin API'
__author__ = 'Dominic Miglar <dominic.miglar@bitmovin.com>'
__email__ = 'dominic.miglar@bitmovin.com'
__license__ = 'Unlicense'


if sys.version_info.major < 3 or sys.version_info.minor < 4:
    sys.exit('Sorry, Python versions older than 3.4 are not supported.')


setup(name=__name__,
      version=__version__,
      description=__description__,
      author=__author__,
      author_email=__email__,
      license=__license__,
      packages=find_packages(exclude=['tests.*', 'tests']),
      install_requires=['requests', 'typing', 'tabulate'],
      include_package_data=True,
      url='https://www.github.com/bitmovin/bitmovin-python/',
      zip_safe=False)
