import unittest
import json
from bitmovin import Bitmovin, Response, S3RoleBasedOutput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class S3RoleBasedOutputTests(BitmovinTestCase):

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
        output_resource_response = self.bitmovin.outputs.S3RoleBased.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_s3_outputs(sample_output, output_resource_response.resource)

    def test_create_s3_output_without_name(self):
        sample_output = self._get_sample_s3_output()
        sample_output.name = None
        output_resource_response = self.bitmovin.outputs.S3RoleBased.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_s3_outputs(sample_output, output_resource_response.resource)

    def test_retrieve_s3_output(self):
        sample_output = self._get_sample_s3_output()
        created_output_response = self.bitmovin.outputs.S3RoleBased.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_s3_outputs(sample_output, created_output_response.resource)

        retrieved_output_response = self.bitmovin.outputs.S3RoleBased.retrieve(created_output_response.resource.id)
        self.assertIsNotNone(retrieved_output_response)
        self.assertIsNotNone(retrieved_output_response.resource)
        self._compare_s3_outputs(created_output_response.resource, retrieved_output_response.resource)

    def test_delete_s3_output(self):
        sample_output = self._get_sample_s3_output()
        created_output_response = self.bitmovin.outputs.S3RoleBased.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_s3_outputs(sample_output, created_output_response.resource)

        deleted_minimal_resource = self.bitmovin.outputs.S3RoleBased.delete(created_output_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.outputs.S3RoleBased.retrieve(created_output_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving output after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_s3_outputs(self):
        sample_output = self._get_sample_s3_output()
        created_output_response = self.bitmovin.outputs.S3RoleBased.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_s3_outputs(sample_output, created_output_response.resource)

        outputs = self.bitmovin.outputs.S3RoleBased.list()
        self.assertIsNotNone(outputs)
        self.assertIsNotNone(outputs.resource)
        self.assertIsNotNone(outputs.response)
        self.assertIsInstance(outputs.resource, list)
        self.assertIsInstance(outputs.response, Response)
        self.assertGreater(outputs.resource.__sizeof__(), 1)

    def test_retrieve_s3_output_custom_data(self):
        sample_output = self._get_sample_s3_output()
        sample_output.customData = '<pre>my custom data</pre>'
        created_output_response = self.bitmovin.outputs.S3RoleBased.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_s3_outputs(sample_output, created_output_response.resource)

        custom_data_response = self.bitmovin.outputs.S3RoleBased.retrieve_custom_data(created_output_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_output.customData, json.loads(custom_data.customData))

    def _compare_s3_outputs(self, first: S3RoleBasedOutput, second: S3RoleBasedOutput):
        """

        :param first: S3RoleBasedOutput
        :param second: S3RoleBasedOutput
        :return: bool
        """
        self.assertEqual(first.bucketName, second.bucketName)
        self.assertEqual(first.cloudRegion, second.cloudRegion)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.md5MetaTag, second.md5MetaTag)

    def _get_sample_s3_output(self):
        s3_output = S3RoleBasedOutput(
            role_arn='arn:aws:iam::123456789012:role/OurS3AccessRole',
            bucket_name='my-bucket-name',
            cloud_region='EU_WEST_1',
            name='Sample S3 Output'
        )

        self.assertIsNotNone(s3_output.roleArn)
        self.assertIsNotNone(s3_output.bucketName)
        self.assertIsNotNone(s3_output.cloudRegion)

        return s3_output


if __name__ == '__main__':
    unittest.main()
