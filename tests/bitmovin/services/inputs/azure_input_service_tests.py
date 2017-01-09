import unittest
import json
from bitmovin import Bitmovin, Response, AzureInput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class AzureInputTests(BitmovinTestCase):

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

    def test_create_azure_input(self):
        (sample_input, sample_files) = self._get_sample_azure_input()
        input_resource_response = self.bitmovin.inputs.Azure.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_azure_inputs(sample_input, input_resource_response.resource)

    def test_create_azure_input_without_name(self):
        (sample_input, sample_files) = self._get_sample_azure_input()
        sample_input.name = None
        input_resource_response = self.bitmovin.inputs.Azure.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_azure_inputs(sample_input, input_resource_response.resource)

    def test_retrieve_azure_input(self):
        (sample_input, sample_files) = self._get_sample_azure_input()
        created_input_response = self.bitmovin.inputs.Azure.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_azure_inputs(sample_input, created_input_response.resource)

        retrieved_input_response = self.bitmovin.inputs.Azure.retrieve(created_input_response.resource.id)
        self.assertIsNotNone(retrieved_input_response)
        self.assertIsNotNone(retrieved_input_response.resource)
        self._compare_azure_inputs(created_input_response.resource, retrieved_input_response.resource)

    def test_delete_azure_input(self):
        (sample_input, sample_files) = self._get_sample_azure_input()
        created_input_response = self.bitmovin.inputs.Azure.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_azure_inputs(sample_input, created_input_response.resource)

        deleted_minimal_resource = self.bitmovin.inputs.Azure.delete(created_input_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.inputs.Azure.retrieve(created_input_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving input after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_azure_inputs(self):
        (sample_input, sample_files) = self._get_sample_azure_input()
        created_input_response = self.bitmovin.inputs.Azure.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_azure_inputs(sample_input, created_input_response.resource)

        inputs = self.bitmovin.inputs.Azure.list()
        self.assertIsNotNone(inputs)
        self.assertIsNotNone(inputs.resource)
        self.assertIsNotNone(inputs.response)
        self.assertIsInstance(inputs.resource, list)
        self.assertIsInstance(inputs.response, Response)
        self.assertGreater(inputs.resource.__sizeof__(), 1)

    def test_retrieve_azure_input_custom_data(self):
        (sample_input, sample_files) = self._get_sample_azure_input()
        sample_input.customData = '<pre>my custom data</pre>'
        created_input_response = self.bitmovin.inputs.Azure.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_azure_inputs(sample_input, created_input_response.resource)

        custom_data_response = self.bitmovin.inputs.Azure.retrieve_custom_data(created_input_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_input.customData, json.loads(custom_data.customData))

    def _compare_azure_inputs(self, first: AzureInput, second: AzureInput):
        """

        :param first: AzureInput
        :param second: AzureInput
        :return: bool
        """
        self.assertEqual(first.container, second.container)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)

    def _get_sample_azure_input(self):
        azure_input_settings = self.settings.get('sampleObjects').get('inputs').get('azure')\
            .get('bd6464c2-132d-4c2e-bfb5-05775b85a085')
        files = azure_input_settings.get('files')
        azure_input = AzureInput(
            account_name=azure_input_settings.get('accountName'),
            account_key=azure_input_settings.get('accountKey'),
            container=azure_input_settings.get('container'),
            name='Sample Azure input'
        )
        self.assertIsNotNone(azure_input.accountName)
        self.assertIsNotNone(azure_input.accountKey)
        self.assertIsNotNone(azure_input.container)
        return azure_input, files


if __name__ == '__main__':
    unittest.main()
