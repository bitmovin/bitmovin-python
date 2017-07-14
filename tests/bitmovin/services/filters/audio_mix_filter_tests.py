import json
import unittest

from bitmovin import Bitmovin, Response, AudioMixFilter, AudioMixFilterChannelLayout, \
    AudioMixChannel, AudioMixSourceChannel, AudioMixFilterChannelType
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class AudioMixFilterTests(BitmovinTestCase):

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

    def test_create_audio_mix_filter(self):
        sample_filter = self._get_sample_audio_mix_filter()
        filter_resource_response = self.bitmovin.filters.AudioMix.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_audio_mix_filters(sample_filter, filter_resource_response.resource)

    def test_create_audio_mix_filter_without_name(self):
        sample_filter = self._get_sample_audio_mix_filter()
        sample_filter.name = None
        filter_resource_response = self.bitmovin.filters.AudioMix.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_audio_mix_filters(sample_filter, filter_resource_response.resource)

    def test_retrieve_audio_mix_filter(self):
        sample_filter = self._get_sample_audio_mix_filter()
        created_filter_response = self.bitmovin.filters.AudioMix.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_audio_mix_filters(sample_filter, created_filter_response.resource)

        retrieved_filter_response = self.bitmovin.filters.AudioMix.retrieve(created_filter_response.resource.id)
        self.assertIsNotNone(retrieved_filter_response)
        self.assertIsNotNone(retrieved_filter_response.resource)
        self._compare_audio_mix_filters(created_filter_response.resource, retrieved_filter_response.resource)

    def test_delete_audio_mix_filter(self):
        sample_filter = self._get_sample_audio_mix_filter()
        created_filter_response = self.bitmovin.filters.AudioMix.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_audio_mix_filters(sample_filter, created_filter_response.resource)

        deleted_minimal_resource = self.bitmovin.filters.AudioMix.delete(created_filter_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.filters.AudioMix.retrieve(created_filter_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving filter after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_audio_mix_filters(self):
        sample_filter = self._get_sample_audio_mix_filter()
        created_filter_response = self.bitmovin.filters.AudioMix.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_audio_mix_filters(sample_filter, created_filter_response.resource)

        filters = self.bitmovin.filters.AudioMix.list()
        self.assertIsNotNone(filters)
        self.assertIsNotNone(filters.resource)
        self.assertIsNotNone(filters.response)
        self.assertIsInstance(filters.resource, list)
        self.assertIsInstance(filters.response, Response)
        self.assertGreater(filters.resource.__sizeof__(), 1)

    def test_retrieve_audio_mix_filter_custom_data(self):
        sample_filter = self._get_sample_audio_mix_filter()
        sample_filter.customData = '<pre>my custom data</pre>'
        created_filter_response = self.bitmovin.filters.AudioMix.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_audio_mix_filters(sample_filter, created_filter_response.resource)

        custom_data_response = self.bitmovin.filters.AudioMix.retrieve_custom_data(created_filter_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_filter.customData, json.loads(custom_data.customData))

    def _compare_audio_mix_filters(self, first: AudioMixFilter, second: AudioMixFilter):
        """
        :param first: AudioMixFilter
        :param second: AudioMixFilter
        :return: bool
        """
        self.assertEqual(first.channel_layout, second.channel_layout)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _get_sample_audio_mix_filter(self):
        source_channels = [AudioMixSourceChannel(channel_type=AudioMixFilterChannelType.CHANNEL_NUMBER,
                                                 channel_number=0,
                                                 gain=1.0)]
        audio_mix_channels = [AudioMixChannel(channel_number=0, source_channels=source_channels)]
        audio_mix_filter = AudioMixFilter(name="Audio Mix Channel",
                                          channel_layout=AudioMixFilterChannelLayout.CL_MONO,
                                          audio_mix_channels=audio_mix_channels)
        self.assertIsNotNone(audio_mix_filter.channel_layout)
        self.assertIsNotNone(audio_mix_filter.audio_mix_channels)
        return audio_mix_filter


if __name__ == '__main__':
    unittest.main()
