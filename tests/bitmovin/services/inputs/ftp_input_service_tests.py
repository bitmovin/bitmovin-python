import unittest
from bitmovin import Bitmovin, Response, FTPInput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class FTPInputTests(BitmovinTestCase):

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

    def test_create_ftp_input(self):
        (sample_input, sample_files) = self._get_sample_ftp_input()
        input_resource_response = self.bitmovin.inputs.FTP.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_ftp_inputs(sample_input, input_resource_response.resource)

    def test_create_ftp_input_without_name(self):
        (sample_input, sample_files) = self._get_sample_ftp_input()
        sample_input.name = None
        input_resource_response = self.bitmovin.inputs.FTP.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_ftp_inputs(sample_input, input_resource_response.resource)

    def test_create_ftp_input_custom(self):
        (sample_input, sample_files) = self._get_sample_ftp_input()
        sample_input.port = 9921
        sample_input.passive = False
        input_resource_response = self.bitmovin.inputs.FTP.create(sample_input)
        self.assertIsNotNone(input_resource_response)
        self.assertIsNotNone(input_resource_response.resource)
        self.assertIsNotNone(input_resource_response.resource.id)
        self._compare_ftp_inputs(sample_input, input_resource_response.resource)
        self.assertEqual(sample_input.port, input_resource_response.resource.port)
        self.assertNotEqual(True, input_resource_response.resource.passive)

    def test_retrieve_ftp_input(self):
        (sample_input, sample_files) = self._get_sample_ftp_input()
        created_input_response = self.bitmovin.inputs.FTP.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_ftp_inputs(sample_input, created_input_response.resource)

        retrieved_input_response = self.bitmovin.inputs.FTP.retrieve(created_input_response.resource.id)
        self.assertIsNotNone(retrieved_input_response)
        self.assertIsNotNone(retrieved_input_response.resource)
        self._compare_ftp_inputs(created_input_response.resource, retrieved_input_response.resource)

    def test_delete_ftp_input(self):
        (sample_input, sample_files) = self._get_sample_ftp_input()
        created_input_response = self.bitmovin.inputs.FTP.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_ftp_inputs(sample_input, created_input_response.resource)

        deleted_minimal_resource = self.bitmovin.inputs.FTP.delete(created_input_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.inputs.FTP.retrieve(created_input_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving input after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_ftp_inputs(self):
        (sample_input, sample_files) = self._get_sample_ftp_input()
        created_input_response = self.bitmovin.inputs.FTP.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_ftp_inputs(sample_input, created_input_response.resource)

        inputs = self.bitmovin.inputs.FTP.list()
        self.assertIsNotNone(inputs)
        self.assertIsNotNone(inputs.resource)
        self.assertIsNotNone(inputs.response)
        self.assertIsInstance(inputs.resource, list)
        self.assertIsInstance(inputs.response, Response)
        self.assertGreater(inputs.resource.__sizeof__(), 1)

    def test_retrieve_ftp_input_custom_data(self):
        (sample_input, sample_files) = self._get_sample_ftp_input()
        sample_input.customData = '<pre>my custom data</pre>'
        created_input_response = self.bitmovin.inputs.FTP.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_ftp_inputs(sample_input, created_input_response.resource)

        custom_data_response = self.bitmovin.inputs.FTP.retrieve_custom_data(created_input_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_input.customData, custom_data.customData)

    def _compare_ftp_inputs(self, first: FTPInput, second: FTPInput):
        """

        :param first: FTPInput
        :param second: FTPInput
        :return: bool
        """
        self.assertEqual(first.host, second.host)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)

    def _get_sample_ftp_input(self):
        ftp_input_settings = self.settings.get('sampleObjects').get('inputs').get('ftp')\
            .get('13bcc79f-f554-482c-bd12-041391df63f8')
        files = ftp_input_settings.get('files')
        ftp_input = FTPInput(
            host=ftp_input_settings.get('host'),
            username=ftp_input_settings.get('username'),
            password=ftp_input_settings.get('password'),
            name='Sample FTP input'
        )
        self.assertIsNotNone(ftp_input.host)
        self.assertIsNotNone(ftp_input.username)
        self.assertIsNotNone(ftp_input.password)
        return ftp_input, files


if __name__ == '__main__':
    unittest.main()
