import unittest

from bitmovin.bitmovin_object import BitmovinObject


class BitmovinObjectTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_bitmovin_object(self):
        bitmovin_object = BitmovinObject()
        self.assertTrue(isinstance(bitmovin_object, BitmovinObject))

if __name__ == '__main__':
    unittest.main()
