import unittest
import json
from bitmovin import Bitmovin, Response, Encoding, CloudRegion
from bitmovin.errors import BitmovinApiError
from bitmovin.resources.enums.encoding_status_values import EncodingStatusValues
from tests.bitmovin import BitmovinTestCase


class EncodingTests(BitmovinTestCase):

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

    def test_create_encoding(self):
        sample_encoding = self._get_sample_encoding()
        encoding_resource_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        self.assertIsNotNone(encoding_resource_response)
        self.assertIsNotNone(encoding_resource_response.resource)
        self.assertIsNotNone(encoding_resource_response.resource.id)
        self._compare_encodings(sample_encoding, encoding_resource_response.resource)

    def test_create_encoding_with_infrastructure(self):
        sample_infrastructure = self.utils.get_sample_infrastructure()
        self.assertIsNotNone(sample_infrastructure.cloudRegion)
        self.assertIsNotNone(sample_infrastructure.infrastructureId)

        sample_encoding = self._get_sample_encoding(CloudRegion.EXTERNAL, infrastructure=sample_infrastructure)
        encoding_resource_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        self.assertIsNotNone(encoding_resource_response)
        self.assertIsNotNone(encoding_resource_response.resource)
        self.assertIsNotNone(encoding_resource_response.resource.id)
        self._compare_encodings(sample_encoding, encoding_resource_response.resource)

        infrastructure_response = encoding_resource_response.resource.infrastructure
        self.assertIsNotNone(infrastructure_response)
        self.assertIsNotNone(infrastructure_response.infrastructureId)
        self.assertIsNotNone(infrastructure_response.cloudRegion)
        self.assertEqual(sample_infrastructure.cloudRegion, infrastructure_response.cloudRegion)
        self.assertEqual(sample_infrastructure.infrastructureId, infrastructure_response.infrastructureId)

    def test_retrieve_encoding(self):
        sample_encoding = self._get_sample_encoding()
        created_encoding_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        self.assertIsNotNone(created_encoding_response)
        self.assertIsNotNone(created_encoding_response.resource)
        self.assertIsNotNone(created_encoding_response.resource.id)
        self._compare_encodings(sample_encoding, created_encoding_response.resource)

        retrieved_encoding_response = self.bitmovin.encodings.Encoding.retrieve(created_encoding_response.resource.id)
        self.assertIsNotNone(retrieved_encoding_response)
        self.assertIsNotNone(retrieved_encoding_response.resource)
        self._compare_encodings(created_encoding_response.resource, retrieved_encoding_response.resource)

    def test_delete_encoding(self):
        sample_encoding = self._get_sample_encoding()
        created_encoding_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        self.assertIsNotNone(created_encoding_response)
        self.assertIsNotNone(created_encoding_response.resource)
        self.assertIsNotNone(created_encoding_response.resource.id)
        self._compare_encodings(sample_encoding, created_encoding_response.resource)

        deleted_minimal_resource = self.bitmovin.encodings.Encoding.delete(created_encoding_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.encodings.Encoding.retrieve(created_encoding_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving encoding after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_get_encoding_status(self):
        sample_encoding = self._get_sample_encoding()
        created_encoding_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        self.assertIsNotNone(created_encoding_response)
        self.assertIsNotNone(created_encoding_response.resource)
        self.assertIsNotNone(created_encoding_response.resource.id)
        self._compare_encodings(sample_encoding, created_encoding_response.resource)

        encoding_status = self.bitmovin.encodings.Encoding.status(created_encoding_response.resource.id)
        self.assertIsNotNone(encoding_status)
        self.assertEqual(encoding_status.resource.status, EncodingStatusValues.CREATED.value)

    def test_list_encodings(self):
        sample_encoding = self._get_sample_encoding()
        created_encoding_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        self.assertIsNotNone(created_encoding_response)
        self.assertIsNotNone(created_encoding_response.resource)
        self.assertIsNotNone(created_encoding_response.resource.id)
        self._compare_encodings(sample_encoding, created_encoding_response.resource)

        encodings = self.bitmovin.encodings.Encoding.list()
        self.assertIsNotNone(encodings)
        self.assertIsNotNone(encodings.resource)
        self.assertIsNotNone(encodings.response)
        self.assertIsInstance(encodings.resource, list)
        self.assertIsInstance(encodings.response, Response)
        self.assertGreater(encodings.resource.__sizeof__(), 1)

    def test_get_encodings_by_status(self):
        sample_encoding = self._get_sample_encoding()
        created_encoding_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        self.assertIsNotNone(created_encoding_response)
        self.assertIsNotNone(created_encoding_response.resource)
        self.assertIsNotNone(created_encoding_response.resource.id)
        self._compare_encodings(sample_encoding, created_encoding_response.resource)

        encodings = self.bitmovin.encodings.Encoding.filter_by_status(status=EncodingStatusValues.CREATED)
        self.assertIsNotNone(encodings)
        self.assertIsNotNone(encodings.resource)
        self.assertIsNotNone(encodings.response)
        self.assertIsInstance(encodings.resource, list)
        self.assertIsInstance(encodings.response, Response)
        self.assertGreater(encodings.resource.__sizeof__(), 1)

    @unittest.skip("not yet implemented in bitmovin-python")
    def test_retrieve_encoding_live_details(self):
        sample_encoding = self._get_sample_encoding()
        created_encoding_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        self.assertIsNotNone(created_encoding_response)
        self.assertIsNotNone(created_encoding_response.resource)
        self.assertIsNotNone(created_encoding_response.resource.id)
        self._compare_encodings(sample_encoding, created_encoding_response.resource)

        retrieved_encoding_live_details_response = \
            self.bitmovin.encodings.Encoding.retrieve_live(created_encoding_response.resource.id)

    def test_retrieve_encoding_custom_data(self):
        sample_encoding = self._get_sample_encoding()
        sample_encoding.customData = '<pre>my custom data</pre>'
        created_encoding_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        self.assertIsNotNone(created_encoding_response)
        self.assertIsNotNone(created_encoding_response.resource)
        self.assertIsNotNone(created_encoding_response.resource.id)
        self._compare_encodings(sample_encoding, created_encoding_response.resource)

        custom_data_response = self.bitmovin.encodings.Encoding.retrieve_custom_data(
            id_=created_encoding_response.resource.id)

        custom_data = custom_data_response.resource
        self.assertEqual(sample_encoding.customData, json.loads(custom_data.customData))

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

    def _get_sample_encoding(self, cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1, infrastructure=None):
        encoding = Encoding(name='Sample Encoding bitmovin-python',
                            description='Sample encoding used in bitmovin-python API client tests',
                            cloud_region=cloud_region,
                            infrastructure=infrastructure)
        self.assertIsNotNone(encoding.name)
        self.assertIsNotNone(encoding.description)
        self.assertIsNotNone(encoding.cloudRegion)
        return encoding



if __name__ == '__main__':
    unittest.main()
