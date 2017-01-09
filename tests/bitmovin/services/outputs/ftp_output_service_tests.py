import unittest
import json
from bitmovin import Bitmovin, Response, FTPOutput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class FTPOutputTests(BitmovinTestCase):

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

    def test_create_ftp_output(self):
        sample_output = self._get_sample_ftp_output()
        output_resource_response = self.bitmovin.outputs.FTP.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_ftp_outputs(sample_output, output_resource_response.resource)

    def test_create_ftp_output_without_name(self):
        sample_output = self._get_sample_ftp_output()
        sample_output.name = None
        output_resource_response = self.bitmovin.outputs.FTP.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_ftp_outputs(sample_output, output_resource_response.resource)

    def test_create_ftp_output_custom(self):
        sample_output = self._get_sample_ftp_output()
        sample_output.port = 9921
        sample_output.passive = False
        output_resource_response = self.bitmovin.outputs.FTP.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_ftp_outputs(sample_output, output_resource_response.resource)
        self.assertEqual(sample_output.port, output_resource_response.resource.port)
        self.assertNotEqual(True, output_resource_response.resource.passive)

    def test_retrieve_ftp_output(self):
        sample_output = self._get_sample_ftp_output()
        created_output_response = self.bitmovin.outputs.FTP.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_ftp_outputs(sample_output, created_output_response.resource)

        retrieved_output_response = self.bitmovin.outputs.FTP.retrieve(created_output_response.resource.id)
        self.assertIsNotNone(retrieved_output_response)
        self.assertIsNotNone(retrieved_output_response.resource)
        self._compare_ftp_outputs(created_output_response.resource, retrieved_output_response.resource)

    def test_delete_ftp_output(self):
        sample_output = self._get_sample_ftp_output()
        created_output_response = self.bitmovin.outputs.FTP.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_ftp_outputs(sample_output, created_output_response.resource)

        deleted_minimal_resource = self.bitmovin.outputs.FTP.delete(created_output_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.outputs.FTP.retrieve(created_output_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving output after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_ftp_outputs(self):
        sample_output = self._get_sample_ftp_output()
        created_output_response = self.bitmovin.outputs.FTP.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_ftp_outputs(sample_output, created_output_response.resource)

        outputs = self.bitmovin.outputs.FTP.list()
        self.assertIsNotNone(outputs)
        self.assertIsNotNone(outputs.resource)
        self.assertIsNotNone(outputs.response)
        self.assertIsInstance(outputs.resource, list)
        self.assertIsInstance(outputs.response, Response)
        self.assertGreater(outputs.resource.__sizeof__(), 1)

    def test_retrieve_ftp_output_custom_data(self):
        sample_output = self._get_sample_ftp_output()
        sample_output.customData = '<pre>my custom data</pre>'
        created_output_response = self.bitmovin.outputs.FTP.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_ftp_outputs(sample_output, created_output_response.resource)

        custom_data_response = self.bitmovin.outputs.FTP.retrieve_custom_data(created_output_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_output.customData, json.loads(custom_data.customData))

    def _compare_ftp_outputs(self, first: FTPOutput, second: FTPOutput):
        """

        :param first: FTPOutput
        :param second: FTPOutput
        :return: bool
        """
        self.assertEqual(first.host, second.host)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)

    def _get_sample_ftp_output(self):
        ftp_output_settings = self.settings.get('sampleObjects').get('outputs').get('ftp')\
            .get('e55925d9-f50a-4f68-bb07-5454345ced26')
        ftp_output = FTPOutput(
            host=ftp_output_settings.get('host'),
            username=ftp_output_settings.get('username'),
            password=ftp_output_settings.get('password'),
            name='Sample FTP Output'
        )
        self.assertIsNotNone(ftp_output.host)
        self.assertIsNotNone(ftp_output.username)
        self.assertIsNotNone(ftp_output.password)
        return ftp_output


if __name__ == '__main__':
    unittest.main()
