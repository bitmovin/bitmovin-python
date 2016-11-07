import unittest
from bitmovin import Bitmovin
from tests.utils import get_settings


class BitmovinTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def setUp(self):
        super().setUp()
        self.settings = get_settings()
        if not self.settings or not isinstance(self.settings, dict):
            raise Exception('Unable to load settings')
        self.api_key = self.settings.get('apiKey')
        if not self.api_key or not isinstance(self.api_key, str):
            raise Exception('Unable to load apiKey from settings')

    def tearDown(self):
        super().tearDown()

    def test_init(self):
        bitmovin = Bitmovin(self.api_key)
        self.assertIsNotNone(bitmovin)
        self.assertTrue(isinstance(bitmovin, Bitmovin))

if __name__ == '__main__':
    unittest.main()
