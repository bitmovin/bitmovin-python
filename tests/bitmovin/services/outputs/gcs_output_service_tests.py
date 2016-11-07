import unittest
from bitmovin import Bitmovin, Response, GCSOutput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class GCSOutputTests(BitmovinTestCase):

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

    def test_create_gcs_output(self):
        sample_output = self._get_sample_gcs_output()
        output_resource_response = self.bitmovin.outputs.GCS.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_gcs_outputs(sample_output, output_resource_response.resource)

    def test_retrieve_gcs_output(self):
        sample_output = self._get_sample_gcs_output()
        created_output_response = self.bitmovin.outputs.GCS.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_gcs_outputs(sample_output, created_output_response.resource)

        retrieved_output_response = self.bitmovin.outputs.GCS.retrieve(created_output_response.resource.id)
        self.assertIsNotNone(retrieved_output_response)
        self.assertIsNotNone(retrieved_output_response.resource)
        self._compare_gcs_outputs(created_output_response.resource, retrieved_output_response.resource)

    def test_delete_gcs_output(self):
        sample_output = self._get_sample_gcs_output()
        created_output_response = self.bitmovin.outputs.GCS.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_gcs_outputs(sample_output, created_output_response.resource)

        deleted_minimal_resource = self.bitmovin.outputs.GCS.delete(created_output_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.outputs.GCS.retrieve(created_output_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving output after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_gcs_outputs(self):
        sample_output = self._get_sample_gcs_output()
        created_output_response = self.bitmovin.outputs.GCS.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_gcs_outputs(sample_output, created_output_response.resource)

        outputs = self.bitmovin.outputs.GCS.list()
        self.assertIsNotNone(outputs)
        self.assertIsNotNone(outputs.resource)
        self.assertIsNotNone(outputs.response)
        self.assertIsInstance(outputs.resource, list)
        self.assertIsInstance(outputs.response, Response)
        self.assertGreater(outputs.resource.__sizeof__(), 1)

    def test_retrieve_gcs_output_custom_data(self):
        sample_output = self._get_sample_gcs_output()
        sample_output.customData = '<pre>my custom data</pre>'
        created_output_response = self.bitmovin.outputs.GCS.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_gcs_outputs(sample_output, created_output_response.resource)

        custom_data_response = self.bitmovin.outputs.GCS.retrieve_custom_data(created_output_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_output.customData, custom_data.customData)

    def _compare_gcs_outputs(self, first: GCSOutput, second: GCSOutput):
        """

        :param first: GCSOutput
        :param second: GCSOutput
        :return: bool
        """
        self.assertEqual(first.bucketName, second.bucketName)
        self.assertEqual(first.cloudRegion, second.cloudRegion)

    def _get_sample_gcs_output(self):
        gcs_output_settings = self.settings.get('sampleObjects').get('outputs').get('gcs')\
            .get('c5d9cfcc-ac07-4bb8-a555-491af7b466ba')
        gcs_output = GCSOutput(
            access_key=gcs_output_settings.get('accessKey'),
            secret_key=gcs_output_settings.get('secretKey'),
            bucket_name=gcs_output_settings.get('bucketName'),
            cloud_region=gcs_output_settings.get('cloudRegion')
        )
        self.assertIsNotNone(gcs_output.accessKey)
        self.assertIsNotNone(gcs_output.secretKey)
        self.assertIsNotNone(gcs_output.bucketName)
        self.assertIsNotNone(gcs_output.cloudRegion)
        return gcs_output


if __name__ == '__main__':
    unittest.main()
