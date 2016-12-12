import unittest
from bitmovin import Bitmovin, Response, SFTPOutput
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class SFTPOutputTests(BitmovinTestCase):

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

    def test_create_sftp_output(self):
        sample_output = self._get_sample_sftp_output()
        output_resource_response = self.bitmovin.outputs.SFTP.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_sftp_outputs(sample_output, output_resource_response.resource)

    def test_create_sftp_output_without_name(self):
        sample_output = self._get_sample_sftp_output()
        sample_output.name = None
        output_resource_response = self.bitmovin.outputs.SFTP.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_sftp_outputs(sample_output, output_resource_response.resource)

    def test_create_sftp_output_custom(self):
        sample_output = self._get_sample_sftp_output()
        sample_output.port = 9921
        output_resource_response = self.bitmovin.outputs.SFTP.create(sample_output)
        self.assertIsNotNone(output_resource_response)
        self.assertIsNotNone(output_resource_response.resource)
        self.assertIsNotNone(output_resource_response.resource.id)
        self._compare_sftp_outputs(sample_output, output_resource_response.resource)
        self.assertEqual(sample_output.port, output_resource_response.resource.port)

    def test_retrieve_sftp_output(self):
        sample_output = self._get_sample_sftp_output()
        created_output_response = self.bitmovin.outputs.SFTP.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_sftp_outputs(sample_output, created_output_response.resource)

        retrieved_output_response = self.bitmovin.outputs.SFTP.retrieve(created_output_response.resource.id)
        self.assertIsNotNone(retrieved_output_response)
        self.assertIsNotNone(retrieved_output_response.resource)
        self._compare_sftp_outputs(created_output_response.resource, retrieved_output_response.resource)

    def test_delete_sftp_output(self):
        sample_output = self._get_sample_sftp_output()
        created_output_response = self.bitmovin.outputs.SFTP.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_sftp_outputs(sample_output, created_output_response.resource)

        deleted_minimal_resource = self.bitmovin.outputs.SFTP.delete(created_output_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.outputs.SFTP.retrieve(created_output_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving output after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_sftp_outputs(self):
        sample_output = self._get_sample_sftp_output()
        created_output_response = self.bitmovin.outputs.SFTP.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_sftp_outputs(sample_output, created_output_response.resource)

        outputs = self.bitmovin.outputs.SFTP.list()
        self.assertIsNotNone(outputs)
        self.assertIsNotNone(outputs.resource)
        self.assertIsNotNone(outputs.response)
        self.assertIsInstance(outputs.resource, list)
        self.assertIsInstance(outputs.response, Response)
        self.assertGreater(outputs.resource.__sizeof__(), 1)

    def test_retrieve_sftp_output_custom_data(self):
        sample_output = self._get_sample_sftp_output()
        sample_output.customData = '<pre>my custom data</pre>'
        created_output_response = self.bitmovin.outputs.SFTP.create(sample_output)
        self.assertIsNotNone(created_output_response)
        self.assertIsNotNone(created_output_response.resource)
        self.assertIsNotNone(created_output_response.resource.id)
        self._compare_sftp_outputs(sample_output, created_output_response.resource)

        custom_data_response = self.bitmovin.outputs.SFTP.retrieve_custom_data(created_output_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_output.customData, custom_data.customData)

    def _compare_sftp_outputs(self, first: SFTPOutput, second: SFTPOutput):
        """

        :param first: SFTPOutput
        :param second: SFTPOutput
        :return: bool
        """
        self.assertEqual(first.host, second.host)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)

    def _get_sample_sftp_output(self):
        sftp_output_settings = self.settings.get('sampleObjects').get('outputs').get('sftp')\
            .get('1b5110d3-8ed3-438d-a8cb-b12cb8b142ca')
        sftp_output = SFTPOutput(
            host=sftp_output_settings.get('host'),
            username=sftp_output_settings.get('username'),
            password=sftp_output_settings.get('password'),
            name='Sample SFTP Output'
        )
        self.assertIsNotNone(sftp_output.host)
        self.assertIsNotNone(sftp_output.username)
        self.assertIsNotNone(sftp_output.password)
        return sftp_output


if __name__ == '__main__':
    unittest.main()
