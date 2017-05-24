import unittest
import json
from bitmovin import Bitmovin, Response, LocalInput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class LocalInputTest(BitmovinTestCase):

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

    def test_create_local_input(self):
        sample_input = self._get_sample_local_input()
        input_resource_response = self.bitmovin.inputs.Local.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_local_inputs(sample_input, input_resource_response.resource)

    def test_create_local_input_without_name(self):
        sample_input = self._get_sample_local_input()
        sample_input.name = None
        input_resource_response = self.bitmovin.inputs.Local.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_local_inputs(sample_input, input_resource_response.resource)

    def test_retrieve_local_input(self):
        sample_input= self._get_sample_local_input()
        created_input_response = self.bitmovin.inputs.Local.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_local_inputs(sample_input, created_input_response.resource)

        retrieved_input_response = self.bitmovin.inputs.Local.retrieve(created_input_response.resource.id)
        self.assertIsNotNone(retrieved_input_response)
        self.assertIsNotNone(retrieved_input_response.resource)
        self._compare_local_inputs(created_input_response.resource, retrieved_input_response.resource)

    def test_delete_local_input(self):
        sample_input = self._get_sample_local_input()
        created_input_response = self.bitmovin.inputs.Local.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_local_inputs(sample_input, created_input_response.resource)

        deleted_minimal_resource = self.bitmovin.inputs.Local.delete(created_input_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.inputs.Local.retrieve(created_input_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving input after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_local_inputs(self):
        sample_input = self._get_sample_local_input()
        created_input_response = self.bitmovin.inputs.Local.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_local_inputs(sample_input, created_input_response.resource)

        inputs = self.bitmovin.inputs.Local.list()
        self.assertIsNotNone(inputs)
        self.assertIsNotNone(inputs.resource)
        self.assertIsNotNone(inputs.response)
        self.assertIsInstance(inputs.resource, list)
        self.assertIsInstance(inputs.response, Response)
        self.assertGreater(inputs.resource.__sizeof__(), 1)

    def test_retrieve_local_input_custom_data(self):
        sample_input = self._get_sample_local_input()
        sample_input.customData = '<pre>my custom data</pre>'
        created_input_response = self.bitmovin.inputs.Local.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_local_inputs(sample_input, created_input_response.resource)

        custom_data_response = self.bitmovin.inputs.Local.retrieve_custom_data(created_input_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_input.customData, json.loads(custom_data.customData))

    def _compare_local_inputs(self, first: LocalInput, second: LocalInput):
        """

        :param first: LocalInput
        :param second: LocalInput
        :return: bool
        """
        self.assertEqual(first.path, second.path)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)

    def _get_sample_local_input(self):
        local_input_settings = self.settings.get('sampleObjects').get('inputs').get('local')\
            .get('3d61877c-f8ea-427c-b73f-4259befb3907')
        path = local_input_settings.get('path')
        local_input = LocalInput(
            name='Sample Local input',
            path=path
        )
        self.assertIsNotNone(local_input.path)
        return local_input


if __name__ == '__main__':
    unittest.main()
