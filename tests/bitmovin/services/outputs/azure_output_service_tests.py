import unittest
from bitmovin import Bitmovin, Response, AzureOutput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class AzureOutputTests(BitmovinTestCase):

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

    def test_create_azure_output(self):
        sample_output = self._get_sample_azure_output()
        output_resource_response = self.bitmovin.outputs.Azure.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_azure_outputs(sample_output, output_resource_response.resource)

    def test_retrieve_azure_output(self):
        sample_output = self._get_sample_azure_output()
        created_output_response = self.bitmovin.outputs.Azure.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_azure_outputs(sample_output, created_output_response.resource)

        retrieved_output_response = self.bitmovin.outputs.Azure.retrieve(created_output_response.resource.id)
        self.assertIsNotNone(retrieved_output_response)
        self.assertIsNotNone(retrieved_output_response.resource)
        self._compare_azure_outputs(created_output_response.resource, retrieved_output_response.resource)

    def test_delete_azure_output(self):
        sample_output = self._get_sample_azure_output()
        created_output_response = self.bitmovin.outputs.Azure.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_azure_outputs(sample_output, created_output_response.resource)

        deleted_minimal_resource = self.bitmovin.outputs.Azure.delete(created_output_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.outputs.Azure.retrieve(created_output_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving output after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_azure_outputs(self):
        sample_output = self._get_sample_azure_output()
        created_output_response = self.bitmovin.outputs.Azure.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_azure_outputs(sample_output, created_output_response.resource)

        outputs = self.bitmovin.outputs.Azure.list()
        self.assertIsNotNone(outputs)
        self.assertIsNotNone(outputs.resource)
        self.assertIsNotNone(outputs.response)
        self.assertIsInstance(outputs.resource, list)
        self.assertIsInstance(outputs.response, Response)
        self.assertGreater(outputs.resource.__sizeof__(), 1)

    def test_retrieve_azure_output_custom_data(self):
        sample_output = self._get_sample_azure_output()
        sample_output.customData = '<pre>my custom data</pre>'
        created_output_response = self.bitmovin.outputs.Azure.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_azure_outputs(sample_output, created_output_response.resource)

        custom_data_response = self.bitmovin.outputs.Azure.retrieve_custom_data(created_output_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_output.customData, custom_data.customData)

    def _compare_azure_outputs(self, first: AzureOutput, second: AzureOutput):
        """

        :param first: AzureOutput
        :param second: AzureOutput
        :return: bool
        """
        self.assertEqual(first.container, second.container)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)

    def _get_sample_azure_output(self):
        azure_output_settings = self.settings.get('sampleObjects').get('outputs').get('azure')\
            .get('2e8fdc76-61a6-4502-a4d4-e4039a5cf7b8')
        azure_output = AzureOutput(
            account_name=azure_output_settings.get('accountName'),
            account_key=azure_output_settings.get('accountKey'),
            container=azure_output_settings.get('container'),
            name='Sample Azure Output'
        )
        self.assertIsNotNone(azure_output.accountName)
        self.assertIsNotNone(azure_output.accountKey)
        self.assertIsNotNone(azure_output.container)
        return azure_output


if __name__ == '__main__':
    unittest.main()
