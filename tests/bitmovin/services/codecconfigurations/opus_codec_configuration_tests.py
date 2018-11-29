import unittest
import json
from bitmovin import Bitmovin, Response, OpusCodecConfiguration, ChannelLayout
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class OpusCodecConfigurationTests(BitmovinTestCase):

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

    def test_create_codec_configuration(self):
        sample_codec_configuration = self._get_sample_codec_configuration()
        codec_configuration_resource_response = self.bitmovin.codecConfigurations.Opus.create(sample_codec_configuration)
        self.assertIsNotNone(codec_configuration_resource_response)
        self.assertIsNotNone(codec_configuration_resource_response.resource)
        self.assertIsNotNone(codec_configuration_resource_response.resource.id)
        self._compare_codec_configurations(sample_codec_configuration,
                                           codec_configuration_resource_response.resource)

    def test_retrieve_codec_configuration(self):
        sample_codec_configuration = self._get_sample_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.Opus.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_codec_configurations(sample_codec_configuration, created_codec_configuration_response.resource)

        retrieved_codec_configuration_response = self.bitmovin.codecConfigurations.Opus.retrieve(
            created_codec_configuration_response.resource.id)
        self.assertIsNotNone(retrieved_codec_configuration_response)
        self.assertIsNotNone(retrieved_codec_configuration_response.resource)
        self._compare_codec_configurations(created_codec_configuration_response.resource,
                                           retrieved_codec_configuration_response.resource)

    def test_retrieve_codec_configuration_channel_layout_none(self):
        sample_codec_configuration = self._get_sample_codec_configuration()
        sample_codec_configuration.channelLayout = None
        created_codec_configuration_response = self.bitmovin.codecConfigurations.Opus.create(
            sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        default_channel_layout = ChannelLayout.NONE
        sample_codec_configuration.channelLayout = default_channel_layout
        self._compare_codec_configurations(sample_codec_configuration,
                                           created_codec_configuration_response.resource)

        retrieved_codec_configuration_response = self.bitmovin.codecConfigurations.Opus.retrieve(
            created_codec_configuration_response.resource.id)
        self.assertIsNotNone(retrieved_codec_configuration_response)
        self.assertIsNotNone(retrieved_codec_configuration_response.resource)
        self._compare_codec_configurations(created_codec_configuration_response.resource,
                                           retrieved_codec_configuration_response.resource)

    def test_delete_codec_configuration(self):
        sample_codec_configuration = self._get_sample_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.Opus.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_codec_configurations(sample_codec_configuration, created_codec_configuration_response.resource)

        deleted_minimal_resource = self.bitmovin.codecConfigurations.Opus.delete(
            created_codec_configuration_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.codecConfigurations.Opus.retrieve(created_codec_configuration_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving codec_configuration after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_codec_configurations(self):
        sample_codec_configuration = self._get_sample_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.Opus.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_codec_configurations(sample_codec_configuration,
                                           created_codec_configuration_response.resource)

        codec_configurations = self.bitmovin.codecConfigurations.Opus.list()
        self.assertIsNotNone(codec_configurations)
        self.assertIsNotNone(codec_configurations.resource)
        self.assertIsNotNone(codec_configurations.response)
        self.assertIsInstance(codec_configurations.resource, list)
        self.assertIsInstance(codec_configurations.response, Response)
        self.assertGreater(codec_configurations.resource.__sizeof__(), 1)

    def test_retrieve_codec_configuration_custom_data(self):
        sample_codec_configuration = self._get_sample_codec_configuration()
        sample_codec_configuration.customData = '<pre>my custom data</pre>'
        created_codec_configuration_response = self.bitmovin.codecConfigurations.Opus.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_codec_configurations(sample_codec_configuration, created_codec_configuration_response.resource)

        custom_data_response = self.bitmovin.codecConfigurations.Opus.retrieve_custom_data(
            created_codec_configuration_response.resource.id)
        custom_data = custom_data_response.resource

        self.assertEqual(sample_codec_configuration.customData, json.loads(custom_data.customData))

    def _compare_codec_configurations(self, first: OpusCodecConfiguration, second: OpusCodecConfiguration):
        """

        :param first: OpusCodecConfiguration
        :param second: OpusCodecConfiguration
        :return: bool
        """
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.bitrate, second.bitrate)
        self.assertEqual(first.rate, second.rate)
        self.assertEqual(first.channelLayout, second.channelLayout)
        return True

    def _get_sample_codec_configuration(self):
        codec_configuration = OpusCodecConfiguration(name='Python - Test Opus Codec Configuration',
                                                     description='More declarative description for CodecConfig',
                                                     bitrate=128000,
                                                     rate=48000,
                                                     channel_layout=ChannelLayout.NONE)

        self.assertIsNotNone(codec_configuration.name)
        self.assertIsNotNone(codec_configuration.description)
        self.assertIsNotNone(codec_configuration.bitrate)
        self.assertIsNotNone(codec_configuration.rate)
        self.assertIsNotNone(codec_configuration.channelLayout)
        return codec_configuration


if __name__ == '__main__':
    unittest.main()
