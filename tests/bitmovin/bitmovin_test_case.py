import unittest
import logging
import sys
from tests import utils


class BitmovinTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.utils = utils
        self.settings = self.utils.get_settings()
        if not self.settings or not isinstance(self.settings, dict):
            raise Exception('Unable to load settings')
        self.api_key = self.settings.get('apiKey')
        if not self.api_key or not isinstance(self.api_key, str):
            raise Exception('Unable to load apiKey from settings')
        self.prepare_logger()

    def prepare_logger(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s')
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
