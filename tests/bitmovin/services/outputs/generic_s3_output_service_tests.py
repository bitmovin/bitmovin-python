import unittest
import json
from bitmovin import Bitmovin, Response, GenericS3Output, S3SignatureVersion
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase

class GenericS3OutputTests(BitmovinTestCase):

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

    def test_create_generic_s3_output(self):
        sample_output = self._get_sample_generic_s3_output()
        output_resource_response = self.bitmovin.outputs.GenericS3.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_generic_s3_outputs(sample_output, output_resource_response.resource)

    def test_create_generic_s3_output_without_name(self):
        sample_output = self._get_sample_generic_s3_output()
        sample_output.name = None
        output_resource_response = self.bitmovin.outputs.GenericS3.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_generic_s3_outputs(sample_output, output_resource_response.resource)

    def test_create_generic_s3_output_sigv2(self):
        sample_output = self._get_sample_generic_s3_output()
        sample_output.signatureVersion = S3SignatureVersion.S3_V2
        output_resource_response = self.bitmovin.outputs.GenericS3.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_generic_s3_outputs(sample_output, output_resource_response.resource)

    def test_create_generic_s3_output_sigv4(self):
        sample_output = self._get_sample_generic_s3_output()
        sample_output.signatureVersion = S3SignatureVersion.S3_V4
        output_resource_response = self.bitmovin.outputs.GenericS3.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_generic_s3_outputs(sample_output, output_resource_response.resource)
        
    def test_create_generic_s3_output_ssl_true(self):
        sample_output = self._get_sample_generic_s3_output()
        sample_output.ssl = True
        output_resource_response = self.bitmovin.outputs.GenericS3.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_generic_s3_outputs(sample_output, output_resource_response.resource)
        
    def test_create_generic_s3_output_ssl_false(self):
        sample_output = self._get_sample_generic_s3_output()
        sample_output.ssl = False
        output_resource_response = self.bitmovin.outputs.GenericS3.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_generic_s3_outputs(sample_output, output_resource_response.resource)        

    def test_retrieve_generic_s3_output(self):
        sample_output = self._get_sample_generic_s3_output()
        created_output_response = self.bitmovin.outputs.GenericS3.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_generic_s3_outputs(sample_output, created_output_response.resource)

        retrieved_output_response = self.bitmovin.outputs.GenericS3.retrieve(created_output_response.resource.id)
        self.assertIsNotNone(retrieved_output_response)
        self.assertIsNotNone(retrieved_output_response.resource)
        self._compare_generic_s3_outputs(created_output_response.resource, retrieved_output_response.resource)

    def test_delete_generic_s3_output(self):
        sample_output = self._get_sample_generic_s3_output()
        created_output_response = self.bitmovin.outputs.GenericS3.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_generic_s3_outputs(sample_output, created_output_response.resource)

        deleted_minimal_resource = self.bitmovin.outputs.GenericS3.delete(created_output_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.outputs.GenericS3.retrieve(created_output_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving output after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_generic_s3_outputs(self):
        sample_output = self._get_sample_generic_s3_output()
        created_output_response = self.bitmovin.outputs.GenericS3.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_generic_s3_outputs(sample_output, created_output_response.resource)

        outputs = self.bitmovin.outputs.GenericS3.list()
        self.assertIsNotNone(outputs)
        self.assertIsNotNone(outputs.resource)
        self.assertIsNotNone(outputs.response)
        self.assertIsInstance(outputs.resource, list)
        self.assertIsInstance(outputs.response, Response)
        self.assertGreater(outputs.resource.__sizeof__(), 1)

    def test_retrieve_generic_s3_output_custom_data(self):
        sample_output = self._get_sample_generic_s3_output()
        sample_output.customData = '<pre>my custom data</pre>'
        created_output_response = self.bitmovin.outputs.GenericS3.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_generic_s3_outputs(sample_output, created_output_response.resource)

        custom_data_response = self.bitmovin.outputs.GenericS3.retrieve_custom_data(created_output_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_output.customData, json.loads(custom_data.customData))

    def _compare_generic_s3_outputs(self, first: GenericS3Output, second: GenericS3Output):
        """

        :param first: GenericS3Output
        :param second: GenericS3Output
        :return: bool
        """
        self.assertEqual(first.bucketName, second.bucketName)
        self.assertEqual(first.host, second.host)
        self.assertEqual(first.port, second.port)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.signatureVersion, second.signatureVersion)
        self.assertEqual(first.ssl, second.ssl)

    def _get_sample_generic_s3_output(self):
        generic_s3_output_settings = self.settings.get('sampleObjects').get('outputs').get('generic-s3')\
            .get('dacae039-286b-46a3-8bae-70aae50b33c2')
        generic_s3_output = GenericS3Output(
            access_key=generic_s3_output_settings.get('accessKey'),
            secret_key=generic_s3_output_settings.get('secretKey'),
            bucket_name=generic_s3_output_settings.get('bucketName'),
            host=generic_s3_output_settings.get('host'),
            port=generic_s3_output_settings.get('port'),
            name='Sample S3 Output'
        )
        self.assertIsNotNone(generic_s3_output.accessKey)
        self.assertIsNotNone(generic_s3_output.secretKey)
        self.assertIsNotNone(generic_s3_output.bucketName)
        self.assertIsNotNone(generic_s3_output.host)
        self.assertIsNotNone(generic_s3_output.port)
        return generic_s3_output


if __name__ == '__main__':
    unittest.main()
