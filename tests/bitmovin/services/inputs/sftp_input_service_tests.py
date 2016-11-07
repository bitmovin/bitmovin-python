import unittest
from bitmovin import Bitmovin, Response, SFTPInput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class SFTPInputTests(BitmovinTestCase):

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

    def test_create_sftp_input(self):
        (sample_input, sample_files) = self._get_sample_sftp_input()
        input_resource_response = self.bitmovin.inputs.SFTP.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_sftp_inputs(sample_input, input_resource_response.resource)

    def test_create_sftp_input_custom(self):
        (sample_input, sample_files) = self._get_sample_sftp_input()
        sample_input.port = 9921
        input_resource_response = self.bitmovin.inputs.SFTP.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_sftp_inputs(sample_input, input_resource_response.resource)
        self.assertEqual(sample_input.port, input_resource_response.resource.port)

    def test_retrieve_sftp_input(self):
        (sample_input, sample_files) = self._get_sample_sftp_input()
        created_input_response = self.bitmovin.inputs.SFTP.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_sftp_inputs(sample_input, created_input_response.resource)

        retrieved_input_response = self.bitmovin.inputs.SFTP.retrieve(created_input_response.resource.id)
        self.assertIsNotNone(retrieved_input_response)
        self.assertIsNotNone(retrieved_input_response.resource)
        self._compare_sftp_inputs(created_input_response.resource, retrieved_input_response.resource)

    def test_delete_sftp_input(self):
        (sample_input, sample_files) = self._get_sample_sftp_input()
        created_input_response = self.bitmovin.inputs.SFTP.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_sftp_inputs(sample_input, created_input_response.resource)

        deleted_minimal_resource = self.bitmovin.inputs.SFTP.delete(created_input_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.inputs.SFTP.retrieve(created_input_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving input after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_sftp_inputs(self):
        (sample_input, sample_files) = self._get_sample_sftp_input()
        created_input_response = self.bitmovin.inputs.SFTP.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_sftp_inputs(sample_input, created_input_response.resource)

        inputs = self.bitmovin.inputs.SFTP.list()
        self.assertIsNotNone(inputs)
        self.assertIsNotNone(inputs.resource)
        self.assertIsNotNone(inputs.response)
        self.assertIsInstance(inputs.resource, list)
        self.assertIsInstance(inputs.response, Response)
        self.assertGreater(inputs.resource.__sizeof__(), 1)

    def test_retrieve_sftp_input_custom_data(self):
        (sample_input, sample_files) = self._get_sample_sftp_input()
        sample_input.customData = '<pre>my custom data</pre>'
        created_input_response = self.bitmovin.inputs.SFTP.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_sftp_inputs(sample_input, created_input_response.resource)

        custom_data_response = self.bitmovin.inputs.SFTP.retrieve_custom_data(created_input_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_input.customData, custom_data.customData)

    def _compare_sftp_inputs(self, first: SFTPInput, second: SFTPInput):
        """

        :param first: SFTPInput
        :param second: SFTPInput
        :return: bool
        """
        self.assertEqual(first.host, second.host)
        #self.assertEqual(first.username, second.username)  # issue 574

    def _get_sample_sftp_input(self):
        sftp_input_settings = self.settings.get('sampleObjects').get('inputs').get('sftp')\
            .get('3945fee9-5e0f-48ce-8f3d-d451c0bf1071')
        files = sftp_input_settings.get('files')
        sftp_input = SFTPInput(
            host=sftp_input_settings.get('host'),
            username=sftp_input_settings.get('username'),
            password=sftp_input_settings.get('password')
        )
        self.assertIsNotNone(sftp_input.host)
        self.assertIsNotNone(sftp_input.username)
        self.assertIsNotNone(sftp_input.password)
        return sftp_input, files


if __name__ == '__main__':
    unittest.main()
