import unittest
from bitmovin import Bitmovin, Response, HTTPSInput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class HTTPSInputTests(BitmovinTestCase):

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

    def test_create_https_input(self):
        (sample_input, sample_files) = self._get_sample_https_input()
        input_resource_response = self.bitmovin.inputs.HTTPS.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_https_inputs(sample_input, input_resource_response.resource)

    @unittest.skip('not ready - see issue 574')
    def test_create_https_input_credentials(self):
        (sample_input, sample_files) = self._get_sample_https_input()
        sample_input.username = 'bitmovin-testuser-python'
        sample_input.password = 'bitmovin-testuser-python'
        input_resource_response = self.bitmovin.inputs.HTTPS.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_https_inputs(sample_input, input_resource_response.resource)
        # self.assertIsNotNone(input_resource_response.resource.username)  # issue 574
        # self.assertEqual(sample_input.username, input_resource_response.resource.username)  # issue 574

    def test_retrieve_https_input(self):
        (sample_input, sample_files) = self._get_sample_https_input()
        created_input_response = self.bitmovin.inputs.HTTPS.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_https_inputs(sample_input, created_input_response.resource)

        retrieved_input_response = self.bitmovin.inputs.HTTPS.retrieve(created_input_response.resource.id)
        self.assertIsNotNone(retrieved_input_response)
        self.assertIsNotNone(retrieved_input_response.resource)
        self._compare_https_inputs(created_input_response.resource, retrieved_input_response.resource)

    def test_delete_https_input(self):
        (sample_input, sample_files) = self._get_sample_https_input()
        created_input_response = self.bitmovin.inputs.HTTPS.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_https_inputs(sample_input, created_input_response.resource)

        deleted_minimal_resource = self.bitmovin.inputs.HTTPS.delete(created_input_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.inputs.HTTPS.retrieve(created_input_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving input after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_https_inputs(self):
        (sample_input, sample_files) = self._get_sample_https_input()
        created_input_response = self.bitmovin.inputs.HTTPS.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_https_inputs(sample_input, created_input_response.resource)

        inputs = self.bitmovin.inputs.HTTPS.list()
        self.assertIsNotNone(inputs)
        self.assertIsNotNone(inputs.resource)
        self.assertIsNotNone(inputs.response)
        self.assertIsInstance(inputs.resource, list)
        self.assertIsInstance(inputs.response, Response)
        self.assertGreater(inputs.resource.__sizeof__(), 1)

    def test_retrieve_https_input_custom_data(self):
        (sample_input, sample_files) = self._get_sample_https_input()
        sample_input.customData = '<pre>my custom data</pre>'
        created_input_response = self.bitmovin.inputs.HTTPS.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_https_inputs(sample_input, created_input_response.resource)

        custom_data_response = self.bitmovin.inputs.HTTPS.retrieve_custom_data(created_input_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_input.customData, custom_data.customData)

    def _compare_https_inputs(self, first: HTTPSInput, second: HTTPSInput):
        """

        :param first: HTTPSInput
        :param second: HTTPSInput
        :return: bool
        """
        self.assertEqual(first.host, second.host)
        #self.assertEqual(first.username, second.username)  # issue 574

    def _get_sample_https_input(self):
        https_input_settings = self.settings.get('sampleObjects').get('inputs').get('https')\
            .get('cdd1cb62-592a-40b5-8288-cda378cd1aa8')
        files = https_input_settings.get('files')
        https_input = HTTPSInput(
            host=https_input_settings.get('host')
        )
        self.assertIsNotNone(https_input.host)
        return https_input, files


if __name__ == '__main__':
    unittest.main()
