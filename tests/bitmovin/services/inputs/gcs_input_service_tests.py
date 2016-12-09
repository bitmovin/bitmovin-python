import unittest
from bitmovin import Bitmovin, Response, GCSInput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class GCSInputTests(BitmovinTestCase):

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

    def test_create_gcs_input(self):
        (sample_input, sample_files) = self._get_sample_gcs_input()
        input_resource_response = self.bitmovin.inputs.GCS.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_gcs_inputs(sample_input, input_resource_response.resource)

    def test_retrieve_gcs_input(self):
        (sample_input, sample_files) = self._get_sample_gcs_input()
        created_input_response = self.bitmovin.inputs.GCS.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_gcs_inputs(sample_input, created_input_response.resource)

        retrieved_input_response = self.bitmovin.inputs.GCS.retrieve(created_input_response.resource.id)
        self.assertIsNotNone(retrieved_input_response)
        self.assertIsNotNone(retrieved_input_response.resource)
        self._compare_gcs_inputs(created_input_response.resource, retrieved_input_response.resource)

    def test_delete_gcs_input(self):
        (sample_input, sample_files) = self._get_sample_gcs_input()
        created_input_response = self.bitmovin.inputs.GCS.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_gcs_inputs(sample_input, created_input_response.resource)

        deleted_minimal_resource = self.bitmovin.inputs.GCS.delete(created_input_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.inputs.GCS.retrieve(created_input_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving input after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_gcs_inputs(self):
        (sample_input, sample_files) = self._get_sample_gcs_input()
        created_input_response = self.bitmovin.inputs.GCS.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_gcs_inputs(sample_input, created_input_response.resource)

        inputs = self.bitmovin.inputs.GCS.list()
        self.assertIsNotNone(inputs)
        self.assertIsNotNone(inputs.resource)
        self.assertIsNotNone(inputs.response)
        self.assertIsInstance(inputs.resource, list)
        self.assertIsInstance(inputs.response, Response)
        self.assertGreater(inputs.resource.__sizeof__(), 1)

    def test_retrieve_gcs_input_custom_data(self):
        (sample_input, sample_files) = self._get_sample_gcs_input()
        sample_input.customData = '<pre>my custom data</pre>'
        created_input_response = self.bitmovin.inputs.GCS.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_gcs_inputs(sample_input, created_input_response.resource)

        custom_data_response = self.bitmovin.inputs.GCS.retrieve_custom_data(created_input_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_input.customData, custom_data.customData)

    def _compare_gcs_inputs(self, first: GCSInput, second: GCSInput):
        """

        :param first: GCSInput
        :param second: GCSInput
        :return: bool
        """
        self.assertEqual(first.bucketName, second.bucketName)
        self.assertEqual(first.cloudRegion, second.cloudRegion)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)

    def _get_sample_gcs_input(self):
        gcs_input_settings = self.settings.get('sampleObjects').get('inputs').get('gcs')\
            .get('90fde3ac-3791-478f-bc29-0ebad279c1c4')
        files = gcs_input_settings.get('files')
        gcs_input = GCSInput(
            access_key=gcs_input_settings.get('accessKey'),
            secret_key=gcs_input_settings.get('secretKey'),
            bucket_name=gcs_input_settings.get('bucketName'),
            cloud_region=gcs_input_settings.get('cloudRegion'),
            name='Sample GCS Input'
        )
        self.assertIsNotNone(gcs_input.accessKey)
        self.assertIsNotNone(gcs_input.secretKey)
        self.assertIsNotNone(gcs_input.bucketName)
        self.assertIsNotNone(gcs_input.cloudRegion)
        return gcs_input, files


if __name__ == '__main__':
    unittest.main()
