import json
import unittest

from bitmovin import Bitmovin, Response, HeAACv1CodecConfiguration, AACChannelLayout, HeAacCodecConfigSignaling
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class AACCodecConfigurationTests(BitmovinTestCase):

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

    def test_create_he_aac_v1_codec_configuration(self):
        sample_codec_configuration = self._get_sample_he_aac_v1_codec_configuration()
        codec_configuration_resource_response = self.bitmovin.codecConfigurations.HeAACv1.create(
            sample_codec_configuration)
        self.assertIsNotNone(codec_configuration_resource_response)
        self.assertIsNotNone(codec_configuration_resource_response.resource)
        self.assertIsNotNone(codec_configuration_resource_response.resource.id)
        self._compare_he_aac_v1_codec_configurations(sample_codec_configuration,
                                                     codec_configuration_resource_response.resource)

    def test_retrieve_he_aac_v1_codec_configuration(self):
        sample_codec_configuration = self._get_sample_he_aac_v1_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.HeAACv1.create(
            sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_he_aac_v1_codec_configurations(sample_codec_configuration,
                                                     created_codec_configuration_response.resource)

        retrieved_codec_configuration_response = self.bitmovin.codecConfigurations.HeAACv1.retrieve(
            created_codec_configuration_response.resource.id)
        self.assertIsNotNone(retrieved_codec_configuration_response)
        self.assertIsNotNone(retrieved_codec_configuration_response.resource)
        self._compare_he_aac_v1_codec_configurations(created_codec_configuration_response.resource,
                                                     retrieved_codec_configuration_response.resource)

    def test_delete_he_aac_v1_codec_configuration(self):
        sample_codec_configuration = self._get_sample_he_aac_v1_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.HeAACv1.create(
            sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_he_aac_v1_codec_configurations(sample_codec_configuration,
                                                     created_codec_configuration_response.resource)

        deleted_minimal_resource = self.bitmovin.codecConfigurations.HeAACv1.delete(
            created_codec_configuration_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.codecConfigurations.HeAACv1.retrieve(created_codec_configuration_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving codec_configuration after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_he_aac_v1_codec_configurations(self):
        sample_codec_configuration = self._get_sample_he_aac_v1_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.HeAACv1.create(
            sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_he_aac_v1_codec_configurations(sample_codec_configuration,
                                                     created_codec_configuration_response.resource)

        codec_configurations = self.bitmovin.codecConfigurations.HeAACv1.list()
        self.assertIsNotNone(codec_configurations)
        self.assertIsNotNone(codec_configurations.resource)
        self.assertIsNotNone(codec_configurations.response)
        self.assertIsInstance(codec_configurations.resource, list)
        self.assertIsInstance(codec_configurations.response, Response)
        self.assertGreater(codec_configurations.resource.__sizeof__(), 1)

    def test_retrieve_he_aac_v1_codec_configuration_custom_data(self):
        sample_codec_configuration = self._get_sample_he_aac_v1_codec_configuration()
        sample_codec_configuration.customData = '<pre>my custom data</pre>'
        created_codec_configuration_response = self.bitmovin.codecConfigurations.HeAACv1.create(
            sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_he_aac_v1_codec_configurations(sample_codec_configuration,
                                                     created_codec_configuration_response.resource)

        custom_data_response = self.bitmovin.codecConfigurations.HeAACv1.retrieve_custom_data(
            created_codec_configuration_response.resource.id)
        custom_data = custom_data_response.resource

        self.assertEqual(sample_codec_configuration.customData, json.loads(custom_data.customData))

    def _compare_he_aac_v1_codec_configurations(self, first: HeAACv1CodecConfiguration,
                                                second: HeAACv1CodecConfiguration):
        """

        :param first: HeAACv1CodecConfiguration
        :param second: HeAACv1CodecConfiguration
        :return: bool
        """
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.bitrate, second.bitrate)
        self.assertEqual(first.rate, second.rate)
        self.assertEqual(first.channelLayout, second.channelLayout)
        self.assertEqual(first.volumeAdjust, second.volumeAdjust)
        self.assertEqual(first.normalize, second.normalize)
        self.assertEqual(first.signaling, second.signaling)
        return True

    def _get_sample_he_aac_v1_codec_configuration(self):
        he_aac_v1_codec_configuration = HeAACv1CodecConfiguration(
            name='Python - Sample HeAACv1 Codec Configuration',
            description='More declarative description for CodecConfig',
            bitrate=128000,
            rate=48000,
            volume_adjust=None,
            normalize=None,
            channel_layout=AACChannelLayout.CL_2_1,
            signaling=HeAacCodecConfigSignaling.EXPLICIT_SBR)

        self.assertIsNotNone(he_aac_v1_codec_configuration.name)
        self.assertIsNotNone(he_aac_v1_codec_configuration.description)
        self.assertIsNotNone(he_aac_v1_codec_configuration.bitrate)
        self.assertIsNotNone(he_aac_v1_codec_configuration.rate)
        self.assertIsNotNone(he_aac_v1_codec_configuration.channelLayout)
        self.assertIsNotNone(he_aac_v1_codec_configuration.signaling)
        return he_aac_v1_codec_configuration


if __name__ == '__main__':
    unittest.main()
