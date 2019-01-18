import unittest
import json
from bitmovin import Bitmovin, Response, VP9CodecConfiguration, VP9Quality, VP9AQMode, VP9ARNRType
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class VP9CodecConfigurationTests(BitmovinTestCase):

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

    def test_create_vp9_codec_configuration(self):
        sample_codec_configuration = self._get_sample_vp9_codec_configuration()
        codec_configuration_resource_response = self.bitmovin.codecConfigurations.VP9.create(
            sample_codec_configuration)
        self.assertIsNotNone(codec_configuration_resource_response)
        self.assertIsNotNone(codec_configuration_resource_response.resource)
        self.assertIsNotNone(codec_configuration_resource_response.resource.id)
        self._compare_vp9_codec_configurations(sample_codec_configuration,
                                               codec_configuration_resource_response.resource)

    def test_create_vp9_codec_configuration_keyframe_interval(self):
        sample_codec_configuration = self._get_sample_vp9_codec_configuration()
        sample_codec_configuration.minGop = None
        sample_codec_configuration.maxGop = None
        sample_codec_configuration.minKeyframeInterval = 10.12
        sample_codec_configuration.maxKeyframeInterval = 20.34
        codec_configuration_resource_response = self.bitmovin.codecConfigurations.VP9.create(
            sample_codec_configuration)
        self.assertIsNotNone(codec_configuration_resource_response)
        self.assertIsNotNone(codec_configuration_resource_response.resource)
        self.assertIsNotNone(codec_configuration_resource_response.resource.id)
        self._compare_vp9_codec_configurations(sample_codec_configuration,
                                               codec_configuration_resource_response.resource)

    def test_retrieve_vp9_codec_configuration(self):
        sample_codec_configuration = self._get_sample_vp9_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.VP9.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_vp9_codec_configurations(sample_codec_configuration,
                                               created_codec_configuration_response.resource)

        retrieved_codec_configuration_response = self.bitmovin.codecConfigurations.VP9.retrieve(
            created_codec_configuration_response.resource.id)
        self.assertIsNotNone(retrieved_codec_configuration_response)
        self.assertIsNotNone(retrieved_codec_configuration_response.resource)
        self._compare_vp9_codec_configurations(created_codec_configuration_response.resource,
                                               retrieved_codec_configuration_response.resource)

    def test_delete_vp9_codec_configuration(self):
        sample_codec_configuration = self._get_sample_vp9_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.VP9.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_vp9_codec_configurations(sample_codec_configuration,
                                               created_codec_configuration_response.resource)

        deleted_minimal_resource = self.bitmovin.codecConfigurations.VP9.delete(
            created_codec_configuration_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.codecConfigurations.VP9.retrieve(created_codec_configuration_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving codec_configuration after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_vp9_codec_configurations(self):
        sample_codec_configuration = self._get_sample_vp9_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.VP9.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_vp9_codec_configurations(sample_codec_configuration,
                                               created_codec_configuration_response.resource)

        codec_configurations = self.bitmovin.codecConfigurations.VP9.list()
        self.assertIsNotNone(codec_configurations)
        self.assertIsNotNone(codec_configurations.resource)
        self.assertIsNotNone(codec_configurations.response)
        self.assertIsInstance(codec_configurations.resource, list)
        self.assertIsInstance(codec_configurations.response, Response)
        self.assertGreater(codec_configurations.resource.__sizeof__(), 1)

    def test_retrieve_vp9_codec_configuration_custom_data(self):
        sample_codec_configuration = self._get_sample_vp9_codec_configuration()
        sample_codec_configuration.customData = '<pre>my custom data</pre>'
        created_codec_configuration_response = self.bitmovin.codecConfigurations.VP9.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_vp9_codec_configurations(sample_codec_configuration,
                                               created_codec_configuration_response.resource)

        custom_data_response = self.bitmovin.codecConfigurations.VP9.retrieve_custom_data(
            created_codec_configuration_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_codec_configuration.customData, json.loads(custom_data.customData))

    def _compare_vp9_codec_configurations(self, first: VP9CodecConfiguration, second: VP9CodecConfiguration):
        """

        :param first: VP9CodecConfiguration
        :param second: VP9CodecConfiguration
        :return: bool
        """
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.bitrate, second.bitrate)
        self.assertEqual(first.rate, second.rate)
        self.assertEqual(first.width, second.width)
        self.assertEqual(first.height, second.height)
        self.assertEqual(first.lagInFrames, second.lagInFrames)
        self.assertEqual(first.tileColumns, second.tileColumns)
        self.assertEqual(first.tileRows, second.tileRows)
        self.assertEqual(first.frameParallel, second.frameParallel)
        self.assertEqual(first.maxIntraRate, second.maxIntraRate)
        self.assertEqual(first.qpMin, second.qpMin)
        self.assertEqual(first.qpMax, second.qpMax)
        self.assertEqual(first.crf, second.crf)
        self.assertEqual(first.rateUndershootPct, second.rateUndershootPct)
        self.assertEqual(first.rateOvershootPct, second.rateOvershootPct)
        self.assertEqual(first.cpuUsed, second.cpuUsed)
        self.assertEqual(first.noiseSensitivity, second.noiseSensitivity)
        self.assertEqual(first.quality, second.quality)
        self.assertEqual(first.lossless, second.lossless)
        self.assertEqual(first.staticThresh, second.staticThresh)
        self.assertEqual(first.aqMode, second.aqMode)
        self.assertEqual(first.arnrMaxFrames, second.arnrMaxFrames)
        self.assertEqual(first.arnrStrength, second.arnrStrength)
        self.assertEqual(first.arnrType, second.arnrType)
        self.assertEqual(first.minGop, second.minGop)
        self.assertEqual(first.maxGop, second.maxGop)
        self.assertEqual(first.minKeyframeInterval, second.minKeyframeInterval)
        self.assertEqual(first.maxKeyframeInterval, second.maxKeyframeInterval)

        return True

    def _get_sample_vp9_codec_configuration(self):
        vp9_codec_configuration = VP9CodecConfiguration(name='VP9 Sample Codec Config',
                                                        description='Long description for VP9 Codec Config',
                                                        bitrate=10000000,
                                                        rate=23.97,
                                                        width=1920,
                                                        height=1080,
                                                        lag_in_frames=5,
                                                        tile_columns=0,
                                                        tile_rows=0,
                                                        frame_parallel=False,
                                                        max_intra_rate=0,
                                                        qp_min=0,
                                                        qp_max=63,
                                                        rate_undershoot_pct=25,
                                                        rate_overshoot_pct=25,
                                                        cpu_used=1,
                                                        noise_sensitivity=False,
                                                        quality=VP9Quality.GOOD,
                                                        lossless=False,
                                                        static_thresh=0,
                                                        aq_mode=VP9AQMode.NONE,
                                                        arnr_max_frames=0,
                                                        arnr_strength=3,
                                                        arnr_type=VP9ARNRType.CENTERED,
                                                        min_gop=30,
                                                        max_gop=120)

        self.assertIsNotNone(vp9_codec_configuration.name)
        self.assertIsNotNone(vp9_codec_configuration.description)
        self.assertIsNotNone(vp9_codec_configuration.bitrate)
        self.assertIsNotNone(vp9_codec_configuration.rate)
        self.assertIsNotNone(vp9_codec_configuration.width)
        self.assertIsNotNone(vp9_codec_configuration.height)
        self.assertIsNotNone(vp9_codec_configuration.lagInFrames)
        self.assertIsNotNone(vp9_codec_configuration.tileColumns)
        self.assertIsNotNone(vp9_codec_configuration.tileRows)
        self.assertIsNotNone(vp9_codec_configuration.frameParallel)
        self.assertIsNotNone(vp9_codec_configuration.maxIntraRate)
        self.assertIsNotNone(vp9_codec_configuration.qpMin)
        self.assertIsNotNone(vp9_codec_configuration.qpMax)
        self.assertIsNotNone(vp9_codec_configuration.rateUndershootPct)
        self.assertIsNotNone(vp9_codec_configuration.rateOvershootPct)
        self.assertIsNotNone(vp9_codec_configuration.cpuUsed)
        self.assertIsNotNone(vp9_codec_configuration.noiseSensitivity)
        self.assertIsNotNone(vp9_codec_configuration.quality)
        self.assertIsNotNone(vp9_codec_configuration.lossless)
        self.assertIsNotNone(vp9_codec_configuration.staticThresh)
        self.assertIsNotNone(vp9_codec_configuration.aqMode)
        self.assertIsNotNone(vp9_codec_configuration.arnrMaxFrames)
        self.assertIsNotNone(vp9_codec_configuration.arnrStrength)
        self.assertIsNotNone(vp9_codec_configuration.arnrType)
        self.assertIsNotNone(vp9_codec_configuration.minGop)
        self.assertIsNotNone(vp9_codec_configuration.maxGop)

        return vp9_codec_configuration


if __name__ == '__main__':
    unittest.main()
