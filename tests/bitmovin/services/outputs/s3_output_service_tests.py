import unittest
import json
from bitmovin import Bitmovin, Response, S3Output
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class S3OutputTests(BitmovinTestCase):

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

    def test_create_s3_output(self):
        sample_output = self._get_sample_s3_output()
        output_resource_response = self.bitmovin.outputs.S3.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_s3_outputs(sample_output, output_resource_response.resource)

    def test_create_s3_output_without_name(self):
        sample_output = self._get_sample_s3_output()
        sample_output.name = None
        output_resource_response = self.bitmovin.outputs.S3.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_s3_outputs(sample_output, output_resource_response.resource)

    def test_retrieve_s3_output(self):
        sample_output = self._get_sample_s3_output()
        created_output_response = self.bitmovin.outputs.S3.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_s3_outputs(sample_output, created_output_response.resource)

        retrieved_output_response = self.bitmovin.outputs.S3.retrieve(created_output_response.resource.id)
        self.assertIsNotNone(retrieved_output_response)
        self.assertIsNotNone(retrieved_output_response.resource)
        self._compare_s3_outputs(created_output_response.resource, retrieved_output_response.resource)

    def test_delete_s3_output(self):
        sample_output = self._get_sample_s3_output()
        created_output_response = self.bitmovin.outputs.S3.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_s3_outputs(sample_output, created_output_response.resource)

        deleted_minimal_resource = self.bitmovin.outputs.S3.delete(created_output_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.outputs.S3.retrieve(created_output_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving output after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_s3_outputs(self):
        sample_output = self._get_sample_s3_output()
        created_output_response = self.bitmovin.outputs.S3.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_s3_outputs(sample_output, created_output_response.resource)

        outputs = self.bitmovin.outputs.S3.list()
        self.assertIsNotNone(outputs)
        self.assertIsNotNone(outputs.resource)
        self.assertIsNotNone(outputs.response)
        self.assertIsInstance(outputs.resource, list)
        self.assertIsInstance(outputs.response, Response)
        self.assertGreater(outputs.resource.__sizeof__(), 1)

    def test_retrieve_s3_output_custom_data(self):
        sample_output = self._get_sample_s3_output()
        sample_output.customData = '<pre>my custom data</pre>'
        created_output_response = self.bitmovin.outputs.S3.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_s3_outputs(sample_output, created_output_response.resource)

        custom_data_response = self.bitmovin.outputs.S3.retrieve_custom_data(created_output_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_output.customData, json.loads(custom_data.customData))

    def _compare_s3_outputs(self, first: S3Output, second: S3Output):
        """

        :param first: S3Output
        :param second: S3Output
        :return: bool
        """
        self.assertEqual(first.bucketName, second.bucketName)
        self.assertEqual(first.cloudRegion, second.cloudRegion)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.md5MetaTag, second.md5MetaTag)

    def _get_sample_s3_output(self):
        s3_output_settings = self.settings.get('sampleObjects').get('outputs').get('s3')\
            .get('5eab19a4-f8bb-4729-b0ad-d8a25f9d1286')
        s3_output = S3Output(
            access_key=s3_output_settings.get('accessKey'),
            secret_key=s3_output_settings.get('secretKey'),
            bucket_name=s3_output_settings.get('bucketName'),
            cloud_region=s3_output_settings.get('cloudRegion'),
            name='Sample S3 Output',
            md5_meta_tag='x-amz-my-md5'
        )
        self.assertIsNotNone(s3_output.accessKey)
        self.assertIsNotNone(s3_output.secretKey)
        self.assertIsNotNone(s3_output.bucketName)
        self.assertIsNotNone(s3_output.cloudRegion)
        self.assertIsNotNone(s3_output.md5MetaTag)
        return s3_output


if __name__ == '__main__':
    unittest.main()
