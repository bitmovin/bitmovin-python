import unittest
import json
from bitmovin import Bitmovin, Response, AkamaiNetStorageOutput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class AkamaiNetStorageOutputTests(BitmovinTestCase):

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

    def test_create_akamai_net_storage_output(self):
        sample_output = self._get_sample_akamai_net_storage_output()
        output_resource_response = self.bitmovin.outputs.AkamaiNetStorage.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_akamai_net_storage_outputs(sample_output, output_resource_response.resource)

    def test_create_akamai_net_storage_output_without_name(self):
        sample_output = self._get_sample_akamai_net_storage_output()
        sample_output.name = None
        output_resource_response = self.bitmovin.outputs.AkamaiNetStorage.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_akamai_net_storage_outputs(sample_output, output_resource_response.resource)

    def test_retrieve_akamai_net_storage_output(self):
        sample_output = self._get_sample_akamai_net_storage_output()
        created_output_response = self.bitmovin.outputs.AkamaiNetStorage.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_akamai_net_storage_outputs(sample_output, created_output_response.resource)

        retrieved_output_response = self.bitmovin.outputs.AkamaiNetStorage.retrieve(created_output_response.resource.id)
        self.assertIsNotNone(retrieved_output_response)
        self.assertIsNotNone(retrieved_output_response.resource)
        self._compare_akamai_net_storage_outputs(created_output_response.resource, retrieved_output_response.resource)

    def test_delete_akamai_net_storage_output(self):
        sample_output = self._get_sample_akamai_net_storage_output()
        created_output_response = self.bitmovin.outputs.AkamaiNetStorage.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_akamai_net_storage_outputs(sample_output, created_output_response.resource)

        deleted_minimal_resource = self.bitmovin.outputs.AkamaiNetStorage.delete(created_output_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.outputs.AkamaiNetStorage.retrieve(created_output_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving output after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_akamai_net_storage_outputs(self):
        sample_output = self._get_sample_akamai_net_storage_output()
        created_output_response = self.bitmovin.outputs.AkamaiNetStorage.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_akamai_net_storage_outputs(sample_output, created_output_response.resource)

        outputs = self.bitmovin.outputs.AkamaiNetStorage.list()
        self.assertIsNotNone(outputs)
        self.assertIsNotNone(outputs.resource)
        self.assertIsNotNone(outputs.response)
        self.assertIsInstance(outputs.resource, list)
        self.assertIsInstance(outputs.response, Response)
        self.assertGreater(outputs.resource.__sizeof__(), 1)

    def test_retrieve_akamai_net_storage_output_custom_data(self):
        sample_output = self._get_sample_akamai_net_storage_output()
        sample_output.customData = '<pre>my custom data</pre>'
        created_output_response = self.bitmovin.outputs.AkamaiNetStorage.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_akamai_net_storage_outputs(sample_output, created_output_response.resource)

        custom_data_response = self.bitmovin.outputs.AkamaiNetStorage.retrieve_custom_data(
            created_output_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_output.customData, json.loads(custom_data.customData))

    def _compare_akamai_net_storage_outputs(self, first: AkamaiNetStorageOutput, second: AkamaiNetStorageOutput):
        """

        :param first: AkamaiNetStorageOutput
        :param second: AkamaiNetStorageOutput
        :return: bool
        """
        self.assertEqual(first.host, second.host)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)

    def _get_sample_akamai_net_storage_output(self):
        output_settings = self.settings.get('sampleObjects').get('outputs')\
            .get('akamai-net-storage').get('ba3bf270-de04-415a-ba65-fd6e6bfc9789')
        sample_output = AkamaiNetStorageOutput(
            host=output_settings.get('host'),
            username=output_settings.get('username'),
            password=output_settings.get('password'),
            name='Sample Akamai NetStorage Output'
        )
        self.assertIsNotNone(sample_output.host)
        self.assertIsNotNone(sample_output.username)
        self.assertIsNotNone(sample_output.password)
        return sample_output


if __name__ == '__main__':
    unittest.main()
