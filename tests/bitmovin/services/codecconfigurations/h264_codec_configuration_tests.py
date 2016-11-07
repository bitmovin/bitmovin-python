import unittest
from bitmovin import Bitmovin, Response, H264CodecConfiguration, H264Profile, MVPredictionMode, H264Level
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class H264CodecConfigurationTests(BitmovinTestCase):

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

    def test_create_h264_codec_configuration(self):
        sample_codec_configuration = self._get_sample_h264_codec_configuration()
        codec_configuration_resource_response = self.bitmovin.codecConfigurations.H264.create(
            sample_codec_configuration)
        self.assertIsNotNone(codec_configuration_resource_response)
        self.assertIsNotNone(codec_configuration_resource_response.resource)
        self.assertIsNotNone(codec_configuration_resource_response.resource.id)
        self._compare_h264_codec_configurations(sample_codec_configuration,
                                                codec_configuration_resource_response.resource)

    def test_retrieve_h264_codec_configuration(self):
        sample_codec_configuration = self._get_sample_h264_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.H264.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_h264_codec_configurations(sample_codec_configuration,
                                                created_codec_configuration_response.resource)

        retrieved_codec_configuration_response = self.bitmovin.codecConfigurations.H264.retrieve(
            created_codec_configuration_response.resource.id)
        self.assertIsNotNone(retrieved_codec_configuration_response)
        self.assertIsNotNone(retrieved_codec_configuration_response.resource)
        self._compare_h264_codec_configurations(created_codec_configuration_response.resource,
                                                retrieved_codec_configuration_response.resource)

    def test_delete_h264_codec_configuration(self):
        sample_codec_configuration = self._get_sample_h264_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.H264.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_h264_codec_configurations(sample_codec_configuration,
                                                created_codec_configuration_response.resource)

        deleted_minimal_resource = self.bitmovin.codecConfigurations.H264.delete(
            created_codec_configuration_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.codecConfigurations.H264.retrieve(created_codec_configuration_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving codec_configuration after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_h264_codec_configurations(self):
        sample_codec_configuration = self._get_sample_h264_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.H264.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_h264_codec_configurations(sample_codec_configuration,
                                                created_codec_configuration_response.resource)

        codec_configurations = self.bitmovin.codecConfigurations.H264.list()
        self.assertIsNotNone(codec_configurations)
        self.assertIsNotNone(codec_configurations.resource)
        self.assertIsNotNone(codec_configurations.response)
        self.assertIsInstance(codec_configurations.resource, list)
        self.assertIsInstance(codec_configurations.response, Response)
        self.assertGreater(codec_configurations.resource.__sizeof__(), 1)

    def test_retrieve_h264_codec_configuration_custom_data(self):
        sample_codec_configuration = self._get_sample_h264_codec_configuration()
        sample_codec_configuration.customData = '<pre>my custom data</pre>'
        created_codec_configuration_response = self.bitmovin.codecConfigurations.H264.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_h264_codec_configurations(sample_codec_configuration,
                                                created_codec_configuration_response.resource)

        custom_data_response = self.bitmovin.codecConfigurations.H264.retrieve_custom_data(
            created_codec_configuration_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_codec_configuration.customData, custom_data.customData)

    def _compare_h264_codec_configurations(self, first: H264CodecConfiguration, second: H264CodecConfiguration):
        """

        :param first: H264CodecConfiguration
        :param second: H264CodecConfiguration
        :return: bool
        """
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.bitrate, second.bitrate)
        self.assertEqual(first.rate, second.rate)
        self.assertEqual(first.width, second.width)
        self.assertEqual(first.height, second.height)
        self.assertEqual(first.profile, second.profile)
        self.assertEqual(first.bframes, second.bframes)
        self.assertEqual(first.refFrames, second.refFrames)
        self.assertEqual(first.qpMin, second.qpMin)
        self.assertEqual(first.qpMax, second.qpMax)
        self.assertEqual(first.mvPredictionMode, second.mvPredictionMode)
        self.assertEqual(first.mvSearchRangeMax, second.mvSearchRangeMax)
        self.assertEqual(first.cabac, second.cabac)
        self.assertEqual(first.maxBitrate, second.maxBitrate)
        self.assertEqual(first.minBitrate, second.minBitrate)
        self.assertEqual(first.bufsize, second.bufsize)
        self.assertEqual(first.minGop, second.minGop)
        self.assertEqual(first.maxGop, second.maxGop)
        self.assertEqual(first.level, second.level)
        return True

    def _get_sample_h264_codec_configuration(self):
        h264_codec_configuration = H264CodecConfiguration(name='Python - H264 Sample Codec Config',
                                                          description='Long description for H264 Codec Config',
                                                          bitrate=10000000,
                                                          rate=23.97,
                                                          profile=H264Profile.MAIN,
                                                          width=1920,
                                                          height=1080,
                                                          bframes=3,
                                                          ref_frames=5,
                                                          qp_min=1,
                                                          qp_max=69,
                                                          mv_prediction_mode=MVPredictionMode.SPATIAL,
                                                          mv_search_range_max=16,
                                                          cabac=True,
                                                          max_bitrate=10000000,
                                                          min_bitrate=5000000,
                                                          bufsize=10000000,
                                                          min_gop=None,
                                                          max_gop=None,
                                                          level=H264Level.L5_1)

        self.assertIsNotNone(h264_codec_configuration.name)
        self.assertIsNotNone(h264_codec_configuration.description)
        self.assertIsNotNone(h264_codec_configuration.bitrate)
        self.assertIsNotNone(h264_codec_configuration.rate)
        self.assertIsNotNone(h264_codec_configuration.profile)
        self.assertIsNotNone(h264_codec_configuration.width)
        self.assertIsNotNone(h264_codec_configuration.height)
        self.assertIsNotNone(h264_codec_configuration.bframes)
        self.assertIsNotNone(h264_codec_configuration.refFrames)
        self.assertIsNotNone(h264_codec_configuration.qpMin)
        self.assertIsNotNone(h264_codec_configuration.qpMax)
        self.assertIsNotNone(h264_codec_configuration.mvPredictionMode)
        self.assertIsNotNone(h264_codec_configuration.mvSearchRangeMax)
        self.assertIsNotNone(h264_codec_configuration.cabac)
        self.assertIsNotNone(h264_codec_configuration.maxBitrate)
        self.assertIsNotNone(h264_codec_configuration.minBitrate)
        self.assertIsNotNone(h264_codec_configuration.level)

        return h264_codec_configuration


if __name__ == '__main__':
    unittest.main()
