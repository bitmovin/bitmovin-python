import unittest
import json
from bitmovin import Bitmovin, Response, HTTPInput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class HTTPInputTests(BitmovinTestCase):

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

    def test_create_http_input(self):
        (sample_input, sample_files) = self._get_sample_http_input()
        input_resource_response = self.bitmovin.inputs.HTTP.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_http_inputs(sample_input, input_resource_response.resource)

    def test_create_http_input_without_name(self):
        (sample_input, sample_files) = self._get_sample_http_input()
        sample_input.name = None
        input_resource_response = self.bitmovin.inputs.HTTP.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_http_inputs(sample_input, input_resource_response.resource)

    def test_create_http_input_credentials(self):
        (sample_input, sample_files) = self._get_sample_http_input()
        sample_input.username = 'bitmovin-testuser-python'
        sample_input.password = 'bitmovin-testuser-python'
        input_resource_response = self.bitmovin.inputs.HTTP.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_http_inputs(sample_input, input_resource_response.resource)

    def test_retrieve_http_input(self):
        (sample_input, sample_files) = self._get_sample_http_input()
        created_input_response = self.bitmovin.inputs.HTTP.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_http_inputs(sample_input, created_input_response.resource)

        retrieved_input_response = self.bitmovin.inputs.HTTP.retrieve(created_input_response.resource.id)
        self.assertIsNotNone(retrieved_input_response)
        self.assertIsNotNone(retrieved_input_response.resource)
        self._compare_http_inputs(created_input_response.resource, retrieved_input_response.resource)

    def test_delete_http_input(self):
        (sample_input, sample_files) = self._get_sample_http_input()
        created_input_response = self.bitmovin.inputs.HTTP.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_http_inputs(sample_input, created_input_response.resource)

        deleted_minimal_resource = self.bitmovin.inputs.HTTP.delete(created_input_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.inputs.HTTP.retrieve(created_input_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving input after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_http_inputs(self):
        (sample_input, sample_files) = self._get_sample_http_input()
        created_input_response = self.bitmovin.inputs.HTTP.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_http_inputs(sample_input, created_input_response.resource)

        inputs = self.bitmovin.inputs.HTTP.list()
        self.assertIsNotNone(inputs)
        self.assertIsNotNone(inputs.resource)
        self.assertIsNotNone(inputs.response)
        self.assertIsInstance(inputs.resource, list)
        self.assertIsInstance(inputs.response, Response)
        self.assertGreater(inputs.resource.__sizeof__(), 1)

    def test_retrieve_http_input_custom_data(self):
        (sample_input, sample_files) = self._get_sample_http_input()
        sample_input.customData = '<pre>my custom data</pre>'
        created_input_response = self.bitmovin.inputs.HTTP.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_http_inputs(sample_input, created_input_response.resource)

        custom_data_response = self.bitmovin.inputs.HTTP.retrieve_custom_data(created_input_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_input.customData, json.loads(custom_data.customData))

    def _compare_http_inputs(self, first: HTTPInput, second: HTTPInput):
        """

        :param first: HTTPInput
        :param second: HTTPInput
        :return: bool
        """
        self.assertEqual(first.host, second.host)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.name, second.name)

    def _get_sample_http_input(self):
        http_input_settings = self.settings.get('sampleObjects').get('inputs').get('http')\
            .get('4fa9fec1-b75e-4e2c-a01b-6e0cb7e3cf3e')
        files = http_input_settings.get('files')
        http_input = HTTPInput(
            host=http_input_settings.get('host'),
            name='Sample HTTP input'
        )
        self.assertIsNotNone(http_input.host)
        return http_input, files


if __name__ == '__main__':
    unittest.main()
