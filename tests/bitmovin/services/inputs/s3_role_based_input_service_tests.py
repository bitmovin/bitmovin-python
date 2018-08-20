import unittest
import json
from bitmovin import Bitmovin, Response, S3RoleBasedInput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class S3InputTests(BitmovinTestCase):

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

    def test_create_s3_input(self):
        sample_input = self._get_sample_s3_input()
        input_resource_response = self.bitmovin.inputs.S3RoleBased.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_s3_inputs(sample_input, input_resource_response.resource)

    def test_create_s3_input_without_name(self):
        sample_input = self._get_sample_s3_input()
        sample_input.name = None
        input_resource_response = self.bitmovin.inputs.S3RoleBased.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_s3_inputs(sample_input, input_resource_response.resource)

    def test_retrieve_s3_input(self):
        sample_input = self._get_sample_s3_input()
        created_input_response = self.bitmovin.inputs.S3RoleBased.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_s3_inputs(sample_input, created_input_response.resource)

        retrieved_input_response = self.bitmovin.inputs.S3RoleBased.retrieve(created_input_response.resource.id)
        self.assertIsNotNone(retrieved_input_response)
        self.assertIsNotNone(retrieved_input_response.resource)
        self._compare_s3_inputs(created_input_response.resource, retrieved_input_response.resource)

    def test_delete_s3_input(self):
        sample_input = self._get_sample_s3_input()
        created_input_response = self.bitmovin.inputs.S3RoleBased.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_s3_inputs(sample_input, created_input_response.resource)

        deleted_minimal_resource = self.bitmovin.inputs.S3RoleBased.delete(created_input_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.inputs.S3RoleBased.retrieve(created_input_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving input after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_s3_inputs(self):
        sample_input = self._get_sample_s3_input()
        created_input_response = self.bitmovin.inputs.S3RoleBased.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_s3_inputs(sample_input, created_input_response.resource)

        inputs = self.bitmovin.inputs.S3RoleBased.list()
        self.assertIsNotNone(inputs)
        self.assertIsNotNone(inputs.resource)
        self.assertIsNotNone(inputs.response)
        self.assertIsInstance(inputs.resource, list)
        self.assertIsInstance(inputs.response, Response)
        self.assertGreater(inputs.resource.__sizeof__(), 1)

    def test_retrieve_s3_input_custom_data(self):
        sample_input = self._get_sample_s3_input()
        sample_input.customData = '<pre>my custom data</pre>'
        created_input_response = self.bitmovin.inputs.S3RoleBased.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_s3_inputs(sample_input, created_input_response.resource)

        custom_data_response = self.bitmovin.inputs.S3RoleBased.retrieve_custom_data(created_input_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_input.customData, json.loads(custom_data.customData))

    def _compare_s3_inputs(self, first: S3RoleBasedInput, second: S3RoleBasedInput):
        """

        :param first: S3RoleBasedInput
        :param second: S3RoleBasedInput
        :return: bool
        """
        self.assertEqual(first.bucketName, second.bucketName)
        self.assertEqual(first.cloudRegion, second.cloudRegion)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)

    def _get_sample_s3_input(self):
        s3_input = S3RoleBasedInput(
            role_arn='arn:aws:iam::123456789012:role/OurS3AccessRole',
            bucket_name='my-bucket-name',
            cloud_region='EU_WEST_1',
            name='Sample S3 Input'
        )
        self.assertIsNotNone(s3_input.roleArn)
        self.assertIsNotNone(s3_input.bucketName)
        self.assertIsNotNone(s3_input.cloudRegion)
        return s3_input


if __name__ == '__main__':
    unittest.main()
