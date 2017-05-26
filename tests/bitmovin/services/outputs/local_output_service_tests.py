import unittest
import json
from bitmovin import Bitmovin, Response, LocalOutput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class LocalOutputTest(BitmovinTestCase):

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

    def test_create_local_output(self):
        sample_output = self._get_sample_local_output()
        output_resource_response = self.bitmovin.outputs.Local.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_local_outputs(sample_output, output_resource_response.resource)

    def test_create_local_output_without_name(self):
        sample_output = self._get_sample_local_output()
        sample_output.name = None
        output_resource_response = self.bitmovin.outputs.Local.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_local_outputs(sample_output, output_resource_response.resource)

    def test_retrieve_local_output(self):
        sample_output= self._get_sample_local_output()
        created_output_response = self.bitmovin.outputs.Local.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_local_outputs(sample_output, created_output_response.resource)

        retrieved_output_response = self.bitmovin.outputs.Local.retrieve(created_output_response.resource.id)
        self.assertIsNotNone(retrieved_output_response)
        self.assertIsNotNone(retrieved_output_response.resource)
        self._compare_local_outputs(created_output_response.resource, retrieved_output_response.resource)

    def test_delete_local_output(self):
        sample_output = self._get_sample_local_output()
        created_output_response = self.bitmovin.outputs.Local.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_local_outputs(sample_output, created_output_response.resource)

        deleted_minimal_resource = self.bitmovin.outputs.Local.delete(created_output_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.outputs.Local.retrieve(created_output_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving output after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_local_outputs(self):
        sample_output = self._get_sample_local_output()
        created_output_response = self.bitmovin.outputs.Local.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_local_outputs(sample_output, created_output_response.resource)

        outputs = self.bitmovin.outputs.Local.list()
        self.assertIsNotNone(outputs)
        self.assertIsNotNone(outputs.resource)
        self.assertIsNotNone(outputs.response)
        self.assertIsInstance(outputs.resource, list)
        self.assertIsInstance(outputs.response, Response)
        self.assertGreater(outputs.resource.__sizeof__(), 1)

    def test_retrieve_local_output_custom_data(self):
        sample_output = self._get_sample_local_output()
        sample_output.customData = '<pre>my custom data</pre>'
        created_output_response = self.bitmovin.outputs.Local.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_local_outputs(sample_output, created_output_response.resource)

        custom_data_response = self.bitmovin.outputs.Local.retrieve_custom_data(created_output_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_output.customData, json.loads(custom_data.customData))

    def _compare_local_outputs(self, first: LocalOutput, second: LocalOutput):
        """

        :param first: LocalOutput
        :param second: LocalOutput
        :return: bool
        """
        self.assertEqual(first.path, second.path)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)

    def _get_sample_local_output(self):
        local_output_settings = self.settings.get('sampleObjects').get('outputs').get('local')\
            .get('689ad35b-9774-41f5-ac7f-390a5e7b9de1')
        path = local_output_settings.get('path')
        local_output = LocalOutput(
            name='Sample Local output',
            path=path
        )
        self.assertIsNotNone(local_output.path)
        return local_output


if __name__ == '__main__':
    unittest.main()
