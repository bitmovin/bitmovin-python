import unittest

from bitmovin import Bitmovin, Encoding, CloudRegion
from tests.bitmovin import BitmovinTestCase


class EncodingCloudRegionTests(BitmovinTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def setUp(self):
        super().setUp()
        self.bitmovin = Bitmovin(self.api_key)
        self.assertIsNotNone(self.bitmovin)
        self.assertTrue(isinstance(self.bitmovin, Bitmovin))

    def tearDown(self):
        super().tearDown()

    def test_create_encoding_cloud_region_auto(self):
        sample_encoding = self._get_sample_encoding()
        sample_encoding.cloudRegion = CloudRegion.AUTO

        encoding_resource_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        self.assertIsNotNone(encoding_resource_response)
        self.assertIsNotNone(encoding_resource_response.resource)
        self.assertIsNotNone(encoding_resource_response.resource.id)
        self.assertEqual(first=CloudRegion.AUTO, second=encoding_resource_response.resource.cloudRegion)
        self._compare_encodings(sample_encoding, encoding_resource_response.resource)

    def _compare_encodings(self, first: Encoding, second: Encoding):
        """

        :param first: Encoding
        :param second: Encoding
        :return: bool
        """
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.encoderVersion, second.encoderVersion)
        self.assertEqual(first.cloudRegion, second.cloudRegion)
        return True

    def _get_sample_encoding(self):
        encoding = Encoding(name='Sample Encoding bitmovin-python',
                            description='Sample encoding used in bitmovin-python API client tests',
                            cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)
        self.assertIsNotNone(encoding.name)
        self.assertIsNotNone(encoding.description)
        self.assertIsNotNone(encoding.cloudRegion)
        return encoding



if __name__ == '__main__':
    unittest.main()
