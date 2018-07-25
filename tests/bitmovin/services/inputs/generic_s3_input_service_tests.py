import unittest
import json
from bitmovin import Bitmovin, Response, GenericS3Input, S3SignatureVersion
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class GenericS3InputTests(BitmovinTestCase):

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

    def test_create_generic_s3_input(self):
        (sample_input, sample_files) = self._get_sample_generic_s3_input()
        input_resource_response = self.bitmovin.inputs.GenericS3.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_generic_s3_inputs(sample_input, input_resource_response.resource)

    def test_create_generic_s3_input_without_name(self):
        (sample_input, sample_files) = self._get_sample_generic_s3_input()
        sample_input.name = None
        input_resource_response = self.bitmovin.inputs.GenericS3.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_generic_s3_inputs(sample_input, input_resource_response.resource)
        
    def test_create_generic_s3_input_sigv2(self):
        (sample_input, sample_files) = self._get_sample_generic_s3_input()
        sample_input.signatureVersion = S3SignatureVersion.S3_V2
        input_resource_response = self.bitmovin.inputs.GenericS3.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_generic_s3_inputs(sample_input, input_resource_response.resource)
              
    def test_create_generic_s3_input_sigv4(self):
        (sample_input, sample_files) = self._get_sample_generic_s3_input()
        sample_input.signatureVersion = S3SignatureVersion.S3_V4
        input_resource_response = self.bitmovin.inputs.GenericS3.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_generic_s3_inputs(sample_input, input_resource_response.resource)
        
    def test_create_generic_s3_input_ssl_true(self):
        (sample_input, sample_files) = self._get_sample_generic_s3_input()
        sample_input.ssl = True
        input_resource_response = self.bitmovin.inputs.GenericS3.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_generic_s3_inputs(sample_input, input_resource_response.resource)
        
    def test_create_generic_s3_input_ssl_false(self):
        (sample_input, sample_files) = self._get_sample_generic_s3_input()
        sample_input.ssl = False
        sample_input.signatureVersion = S3SignatureVersion.S3_V2
        input_resource_response = self.bitmovin.inputs.GenericS3.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_generic_s3_inputs(sample_input, input_resource_response.resource)               

    def test_retrieve_generic_s3_input(self):
        (sample_input, sample_files) = self._get_sample_generic_s3_input()
        created_input_response = self.bitmovin.inputs.GenericS3.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_generic_s3_inputs(sample_input, created_input_response.resource)

        retrieved_input_response = self.bitmovin.inputs.GenericS3.retrieve(created_input_response.resource.id)
        self.assertIsNotNone(retrieved_input_response)
        self.assertIsNotNone(retrieved_input_response.resource)
        self._compare_generic_s3_inputs(created_input_response.resource, retrieved_input_response.resource)

    def test_delete_generic_s3_input(self):
        (sample_input, sample_files) = self._get_sample_generic_s3_input()
        created_input_response = self.bitmovin.inputs.GenericS3.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_generic_s3_inputs(sample_input, created_input_response.resource)

        deleted_minimal_resource = self.bitmovin.inputs.GenericS3.delete(created_input_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.inputs.GenericS3.retrieve(created_input_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving input after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_generic_s3_inputs(self):
        (sample_input, sample_files) = self._get_sample_generic_s3_input()
        created_input_response = self.bitmovin.inputs.GenericS3.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_generic_s3_inputs(sample_input, created_input_response.resource)

        inputs = self.bitmovin.inputs.GenericS3.list()
        self.assertIsNotNone(inputs)
        self.assertIsNotNone(inputs.resource)
        self.assertIsNotNone(inputs.response)
        self.assertIsInstance(inputs.resource, list)
        self.assertIsInstance(inputs.response, Response)
        self.assertGreater(inputs.resource.__sizeof__(), 1)

    def test_retrieve_generic_s3_input_custom_data(self):
        (sample_input, sample_files) = self._get_sample_generic_s3_input()
        sample_input.customData = '<pre>my custom data</pre>'
        created_input_response = self.bitmovin.inputs.GenericS3.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_generic_s3_inputs(sample_input, created_input_response.resource)

        custom_data_response = self.bitmovin.inputs.GenericS3.retrieve_custom_data(created_input_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_input.customData, json.loads(custom_data.customData))

    def _compare_generic_s3_inputs(self, first: GenericS3Input, second: GenericS3Input):
        """

        :param first: GenericS3Input
        :param second: GenericS3Input
        :return: bool
        """
        self.assertEqual(first.bucketName, second.bucketName)
        self.assertEqual(first.host, second.host)
        self.assertEqual(first.port, second.port)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.signatureVersion, second.signatureVersion)
        self.assertEqual(first.ssl, second.ssl)
        

    def _get_sample_generic_s3_input(self):
        generic_s3_input_settings = self.settings.get('sampleObjects').get('inputs').get('generic-s3')\
            .get('dacae039-286b-46a3-8bae-70aae50b33c2')
        files = generic_s3_input_settings.get('files')
        generic_s3_input = GenericS3Input(
            access_key=generic_s3_input_settings.get('accessKey'),
            secret_key=generic_s3_input_settings.get('secretKey'),
            bucket_name=generic_s3_input_settings.get('bucketName'),
            host=generic_s3_input_settings.get('host'),
            port=generic_s3_input_settings.get('port'),
            name='Sample S3 Input'
        )
        self.assertIsNotNone(generic_s3_input.accessKey)
        self.assertIsNotNone(generic_s3_input.secretKey)
        self.assertIsNotNone(generic_s3_input.bucketName)
        self.assertIsNotNone(generic_s3_input.host)
        self.assertIsNotNone(generic_s3_input.port)
        return generic_s3_input, files


if __name__ == '__main__':
    unittest.main()
