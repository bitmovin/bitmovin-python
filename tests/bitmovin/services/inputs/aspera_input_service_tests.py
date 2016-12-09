import unittest
from bitmovin import Bitmovin, Response, AsperaInput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class AsperaInputTests(BitmovinTestCase):

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

    def test_create_aspera_input(self):
        (sample_input, sample_file) = self._get_sample_aspera_input()
        input_resource_response = self.bitmovin.inputs.Aspera.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_aspera_inputs(sample_input, input_resource_response.resource)

    def test_create_aspera_input_custom(self):
        (sample_input, sample_file) = self._get_sample_aspera_input()
        sample_input.minBandwidth = '100m'
        sample_input.maxBandwidth = '100g'
        input_resource_response = self.bitmovin.inputs.Aspera.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_aspera_inputs(sample_input, input_resource_response.resource)
        self.assertEqual(sample_input.minBandwidth, input_resource_response.resource.minBandwidth)
        self.assertEqual(sample_input.maxBandwidth, input_resource_response.resource.maxBandwidth)

    def test_retrieve_aspera_input(self):
        (sample_input, sample_file) = self._get_sample_aspera_input()
        created_input_response = self.bitmovin.inputs.Aspera.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_aspera_inputs(sample_input, created_input_response.resource)

        retrieved_input_response = self.bitmovin.inputs.Aspera.retrieve(created_input_response.resource.id)
        self.assertIsNotNone(retrieved_input_response)
        self.assertIsNotNone(retrieved_input_response.resource)
        self._compare_aspera_inputs(created_input_response.resource, retrieved_input_response.resource)

    def test_delete_aspera_input(self):
        (sample_input, sample_file) = self._get_sample_aspera_input()
        created_input_response = self.bitmovin.inputs.Aspera.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_aspera_inputs(sample_input, created_input_response.resource)

        deleted_minimal_resource = self.bitmovin.inputs.Aspera.delete(created_input_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.inputs.Aspera.retrieve(created_input_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving input after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_aspera_inputs(self):
        (sample_input, sample_file) = self._get_sample_aspera_input()
        created_input_response = self.bitmovin.inputs.Aspera.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_aspera_inputs(sample_input, created_input_response.resource)

        inputs = self.bitmovin.inputs.Aspera.list()
        self.assertIsNotNone(inputs)
        self.assertIsNotNone(inputs.resource)
        self.assertIsNotNone(inputs.response)
        self.assertIsInstance(inputs.resource, list)
        self.assertIsInstance(inputs.response, Response)
        self.assertGreater(inputs.resource.__sizeof__(), 1)

    def test_retrieve_aspera_input_custom_data(self):
        (sample_input, sample_file) = self._get_sample_aspera_input()
        sample_input.customData = '<pre>my custom data</pre>'
        created_input_response = self.bitmovin.inputs.Aspera.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_aspera_inputs(sample_input, created_input_response.resource)

        custom_data_response = self.bitmovin.inputs.Aspera.retrieve_custom_data(created_input_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_input.customData, custom_data.customData)

    def _compare_aspera_inputs(self, first: AsperaInput, second: AsperaInput):
        """

        :param first: AsperaInput
        :param second: AsperaInput
        :return: bool
        """
        self.assertEqual(first.host, second.host)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)

    def _get_sample_aspera_input(self):
        aspera_input_settings = self.settings.get('sampleObjects').get('inputs').get('aspera')\
            .get('cfa45808-9c5d-4c04-ba8c-8d6cfc16271b')
        file = aspera_input_settings.get('files').get('3b9be60e-1a31-42c3-ae80-c4a0bc9300b9')
        aspera_input = AsperaInput(
            host=aspera_input_settings.get('host'),
            username=aspera_input_settings.get('username'),
            password=aspera_input_settings.get('password'),
            name='Sample Aspera Input',
            description='Descriptive words'
        )
        self.assertIsNotNone(aspera_input.host)
        self.assertIsNotNone(aspera_input.username)
        self.assertIsNotNone(aspera_input.password)
        return aspera_input, file


if __name__ == '__main__':
    unittest.main()
