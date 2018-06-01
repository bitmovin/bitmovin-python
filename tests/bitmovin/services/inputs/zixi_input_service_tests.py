import unittest
import json
from bitmovin import Bitmovin, Response, ZixiInput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class ZixiInputTests(BitmovinTestCase):

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

    def test_create_zixi_input(self):
        (sample_input, sample_files) = self._get_sample_zixi_input()
        input_resource_response = self.bitmovin.inputs.Zixi.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_zixi_inputs(sample_input, input_resource_response.resource)

    def test_create_zixi_input_without_name(self):
        (sample_input, sample_files) = self._get_sample_zixi_input()
        sample_input.name = None
        input_resource_response = self.bitmovin.inputs.Zixi.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_zixi_inputs(sample_input, input_resource_response.resource)

    def test_retrieve_zixi_input(self):
        (sample_input, sample_files) = self._get_sample_zixi_input()
        created_input_response = self.bitmovin.inputs.Zixi.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_zixi_inputs(sample_input, created_input_response.resource)

        retrieved_input_response = self.bitmovin.inputs.Zixi.retrieve(created_input_response.resource.id)
        self.assertIsNotNone(retrieved_input_response)
        self.assertIsNotNone(retrieved_input_response.resource)
        self._compare_zixi_inputs(created_input_response.resource, retrieved_input_response.resource)

    def test_delete_zixi_input(self):
        (sample_input, sample_files) = self._get_sample_zixi_input()
        created_input_response = self.bitmovin.inputs.Zixi.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_zixi_inputs(sample_input, created_input_response.resource)

        deleted_minimal_resource = self.bitmovin.inputs.Zixi.delete(created_input_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.inputs.Zixi.retrieve(created_input_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving input after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_zixi_inputs(self):
        (sample_input, sample_files) = self._get_sample_zixi_input()
        created_input_response = self.bitmovin.inputs.Zixi.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_zixi_inputs(sample_input, created_input_response.resource)

        inputs = self.bitmovin.inputs.Zixi.list()
        self.assertIsNotNone(inputs)
        self.assertIsNotNone(inputs.resource)
        self.assertIsNotNone(inputs.response)
        self.assertIsInstance(inputs.resource, list)
        self.assertIsInstance(inputs.response, Response)
        self.assertGreater(inputs.resource.__sizeof__(), 1)

    def test_retrieve_zixi_input_custom_data(self):
        (sample_input, sample_files) = self._get_sample_zixi_input()
        sample_input.customData = '<pre>my custom data</pre>'
        created_input_response = self.bitmovin.inputs.Zixi.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_zixi_inputs(sample_input, created_input_response.resource)

        custom_data_response = self.bitmovin.inputs.Zixi.retrieve_custom_data(created_input_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_input.customData, json.loads(custom_data.customData))

    def _compare_zixi_inputs(self, first: ZixiInput, second: ZixiInput):
        """

        :param first: ZixiInput
        :param second: ZixiInput
        :return: bool
        """
        self.assertEqual(first.host, second.host)
        self.assertEqual(first.port, second.port)
        self.assertEqual(first.stream, second.stream)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)

    def _get_sample_zixi_input(self):
        zixi_input_settings = self.settings.get('sampleObjects').get('inputs').get('zixi')\
            .get('36b848e3-b9e9-49ba-9c56-62d67fb5bcb2')
        files = zixi_input_settings.get('files')
        zixi_input = ZixiInput(
            host=zixi_input_settings.get('host'),
            port=zixi_input_settings.get('port'),
            stream=zixi_input_settings.get('stream'),
            password=zixi_input_settings.get('password'),
            latency=zixi_input_settings.get('latency'),
            min_bitrate=zixi_input_settings.get('minBitrate'),
            decryption_type=zixi_input_settings.get('decryptionType'),
            decryption_key=zixi_input_settings.get('decryptionKey'),
            name='Sample Zixi input'
        )
        self.assertIsNotNone(zixi_input.host)
        self.assertIsNotNone(zixi_input.port)
        self.assertIsNotNone(zixi_input.stream)
        return zixi_input, files


if __name__ == '__main__':
    unittest.main()
