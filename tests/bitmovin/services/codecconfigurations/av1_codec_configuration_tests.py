import json
import unittest

from bitmovin import Bitmovin, Response, ChromaLocation, ColorSpace, ColorPrimaries, ColorRange, ColorTransfer, \
    InputColorSpace, InputColorRange, ColorConfig, AV1CodecConfiguration, AV1KeyPlacementMode, \
    AV1RateControlMode, AV1AdaptiveQuantMode
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class AV1CodecConfigurationTests(BitmovinTestCase):

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

    def test_create_h265_codec_configuration(self):
        sample_codec_configuration = self._get_sample_codec_configuration()
        codec_configuration_resource_response = self.bitmovin.codecConfigurations.AV1.create(
            sample_codec_configuration)
        self.assertIsNotNone(codec_configuration_resource_response)
        self.assertIsNotNone(codec_configuration_resource_response.resource)
        self.assertIsNotNone(codec_configuration_resource_response.resource.id)
        self._compare_codec_configurations(sample_codec_configuration,
                                           codec_configuration_resource_response.resource)

    def test_retrieve_codec_configuration(self):
        sample_codec_configuration = self._get_sample_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.AV1.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_codec_configurations(sample_codec_configuration,
                                           created_codec_configuration_response.resource)

        retrieved_codec_configuration_response = self.bitmovin.codecConfigurations.AV1.retrieve(
            created_codec_configuration_response.resource.id)
        self.assertIsNotNone(retrieved_codec_configuration_response)
        self.assertIsNotNone(retrieved_codec_configuration_response.resource)
        self._compare_codec_configurations(created_codec_configuration_response.resource,
                                           retrieved_codec_configuration_response.resource)

    def test_delete_codec_configuration(self):
        sample_codec_configuration = self._get_sample_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.AV1.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_codec_configurations(sample_codec_configuration,
                                           created_codec_configuration_response.resource)

        deleted_minimal_resource = self.bitmovin.codecConfigurations.AV1.delete(
            created_codec_configuration_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.codecConfigurations.AV1.retrieve(created_codec_configuration_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving codec_configuration after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_codec_configurations(self):
        sample_codec_configuration = self._get_sample_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.AV1.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_codec_configurations(sample_codec_configuration,
                                           created_codec_configuration_response.resource)

        codec_configurations = self.bitmovin.codecConfigurations.AV1.list()
        self.assertIsNotNone(codec_configurations)
        self.assertIsNotNone(codec_configurations.resource)
        self.assertIsNotNone(codec_configurations.response)
        self.assertIsInstance(codec_configurations.resource, list)
        self.assertIsInstance(codec_configurations.response, Response)
        self.assertGreater(codec_configurations.resource.__sizeof__(), 1)

    def test_retrieve_codec_configuration_custom_data(self):
        sample_codec_configuration = self._get_sample_codec_configuration()
        sample_codec_configuration.customData = '<pre>my custom data</pre>'
        created_codec_configuration_response = self.bitmovin.codecConfigurations.AV1.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_codec_configurations(sample_codec_configuration,
                                           created_codec_configuration_response.resource)

        custom_data_response = self.bitmovin.codecConfigurations.AV1.retrieve_custom_data(
            created_codec_configuration_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_codec_configuration.customData, json.loads(custom_data.customData))

    def test_create_codec_config_with_bitrate_and_crf(self):
        sample_codec_configuration = self._get_sample_codec_configuration()
        self.assertIsNotNone(sample_codec_configuration.bitrate)

        sample_codec_configuration.crf = 51.0
        self.assertEqual(sample_codec_configuration.crf, 51.0)
        try:
            self.bitmovin.codecConfigurations.AV1.create(sample_codec_configuration)

        except BitmovinApiError as error:
            self.assertEqual(error.response.status, 'ERROR')
            self.assertEqual(error.response.data.code, 1001)

    def test_create_codec_configuration_with_av1_enums(self):
        sample_codec_configuration = self._get_sample_codec_configuration()
        sample_codec_configuration.keyPlacementMode = AV1KeyPlacementMode.FIXED
        sample_codec_configuration.adaptiveQuantMode = AV1AdaptiveQuantMode.CYCLIC_REFRESH
        sample_codec_configuration.rateControlMode = AV1RateControlMode.CONSTANT_QUALITY

        codec_configuration_resource_response = self.bitmovin.codecConfigurations.AV1.create(
            sample_codec_configuration)

        self.assertIsNotNone(codec_configuration_resource_response)
        self.assertIsNotNone(codec_configuration_resource_response.resource)
        self.assertIsNotNone(codec_configuration_resource_response.resource.id)
        self._compare_codec_configurations(sample_codec_configuration,
                                           codec_configuration_resource_response.resource)

    def _compare_codec_configurations(self, first: AV1CodecConfiguration, second: AV1CodecConfiguration):
        """

        :param first: AV1CodecConfiguration
        :param second: AV1CodecConfiguration
        :return: bool
        """
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.bitrate, second.bitrate)
        self.assertEqual(first.rate, second.rate)
        self.assertEqual(first.width, second.width)
        self.assertEqual(first.height, second.height)
        self.assertEqual(first.keyPlacementMode, second.keyPlacementMode)
        self.assertEqual(first.rateControlMode, second.rateControlMode)
        self.assertEqual(first.sampleAspectRatioNumerator, second.sampleAspectRatioNumerator)
        self.assertEqual(first.sampleAspectRatioDenominator, second.sampleAspectRatioDenominator)
        self.assertEqual(first.adaptiveQuantMode, second.adaptiveQuantMode)
        self.assertEqual(first.lagInFrames, second.lagInFrames)
        self.assertEqual(first.minQ, second.minQ)
        self.assertEqual(first.maxQ, second.maxQ)
        self.assertEqual(first.undershootPct, second.undershootPct)
        self.assertEqual(first.overshootPct, second.overshootPct)
        self.assertEqual(first.clientBufferSize, second.clientBufferSize)
        self.assertEqual(first.clientInitialBufferSize, second.clientInitialBufferSize)
        self.assertEqual(first.clientOptimalBufferSize, second.clientOptimalBufferSize)
        self.assertEqual(first.tileColumns, second.tileColumns)
        self.assertEqual(first.tileRows, second.tileRows)
        self.assertEqual(first.automaticAltRefFramesEnabled, second.automaticAltRefFramesEnabled)
        self.assertEqual(first.arnrMaxFrames, second.arnrMaxFrames)
        self.assertEqual(first.arnrStrength, second.arnrStrength)
        self.assertEqual(first.cqLevel, second.cqLevel)
        self.assertEqual(first.maxIntraRate, second.maxIntraRate)
        self.assertEqual(first.maxInterRate, second.maxInterRate)
        self.assertEqual(first.gfCbrBoost, second.gfCbrBoost)
        self.assertEqual(first.lossless, second.lossless)
        self.assertEqual(first.frameParallel, second.frameParallel)
        self.assertEqual(first.sharpness, second.sharpness)
        self.assertEqual(first.frameBoostEnabled, second.frameBoostEnabled)
        self.assertEqual(first.noiseSensitivity, second.noiseSensitivity)
        self.assertEqual(first.minGfInterval, second.minGfInterval)
        self.assertEqual(first.maxGfInterval, second.maxGfInterval)
        self.assertEqual(first.numTileGroups, second.numTileGroups)
        self.assertEqual(first.mtuSize, second.mtuSize)
        self.assertTrue(self._compare_color_configs(first.colorConfig, second.colorConfig))

        return True

    def _compare_color_configs(self, first: ColorConfig, second: ColorConfig):
        """

        :param first: ColorConfig
        :param second: ColorConfig
        :return: bool
        """
        self.assertEqual(first.inputColorSpace, second.inputColorSpace)
        self.assertEqual(first.colorTransfer, second.colorTransfer)
        self.assertEqual(first.colorRange, second.colorRange)
        self.assertEqual(first.colorPrimaries, second.colorPrimaries)
        self.assertEqual(first.colorSpace, second.colorSpace)
        self.assertEqual(first.chromaLocation, second.chromaLocation)
        self.assertEqual(first.copyChromaLocationFlag, second.copyChromaLocationFlag)
        self.assertEqual(first.copyColorPrimariesFlag, second.copyColorPrimariesFlag)
        self.assertEqual(first.copyColorRangeFlag, second.copyColorRangeFlag)
        self.assertEqual(first.copyColorSpaceFlag, second.copyColorSpaceFlag)
        self.assertEqual(first.copyColorTransferFlag, second.copyColorTransferFlag)
        return True

    def _get_sample_codec_configuration(self):
        codec_configuration = AV1CodecConfiguration(name='AV1 Sample Codec Config',
                                                    description='Long description for AV1 Codec Config',
                                                    bitrate=10000000,
                                                    rate=23.97,
                                                    width=1920,
                                                    height=1080,
                                                    pixel_format=None,
                                                    sample_aspect_ratio_numerator=2.0,
                                                    sample_aspect_ratio_denominator=3.0,
                                                    key_placement_mode=AV1KeyPlacementMode.FIXED,
                                                    rate_control_mode=AV1RateControlMode.CONSTRAINED_QUALITY,
                                                    adaptive_quant_mode=AV1AdaptiveQuantMode.COMPLEXITY,
                                                    lag_in_frames=0,
                                                    min_q=0,
                                                    max_q=63,
                                                    undershoot_pct=500,
                                                    overshoot_pct=500,
                                                    client_buffer_size=2000,
                                                    client_initial_buffer_size=2000,
                                                    client_optimal_buffer_size=2000,
                                                    tile_columns=1,
                                                    tile_rows=1,
                                                    automatic_alt_ref_frames_enabled=False,
                                                    arnr_max_frames=10,
                                                    arnr_strength=10,
                                                    cq_level=0,
                                                    max_intra_rate=0,
                                                    max_inter_rate=0,
                                                    gf_cbr_boost=0,
                                                    lossless=False,
                                                    frame_parallel=False,
                                                    sharpness=50,
                                                    frame_boost_enabled=True,
                                                    noise_sensitivity=0,
                                                    min_gf_interval=4,
                                                    max_gf_interval=16,
                                                    num_tile_groups=1,
                                                    mtu_size=4096,
                                                    color_config=ColorConfig(
                                                        copy_chroma_location_flag=True,
                                                        copy_color_space_flag=True,
                                                        copy_color_primaries_flag=True,
                                                        copy_color_range_flag=True,
                                                        copy_color_transfer_flag=True,
                                                        chroma_location=ChromaLocation.BOTTOM,
                                                        color_space=ColorSpace.BT2020_CL,
                                                        color_primaries=ColorPrimaries.BT709,
                                                        color_range=ColorRange.MPEG,
                                                        color_transfer=ColorTransfer.BT2020_10,
                                                        input_color_space=InputColorSpace.BT470BG,
                                                        input_color_range=InputColorRange.JPEG)

                                                    )

        self.assertIsNotNone(codec_configuration.colorConfig)
        self.assertIsNotNone(codec_configuration.keyPlacementMode)
        self.assertIsNotNone(codec_configuration.rateControlMode)
        self.assertIsNotNone(codec_configuration.sampleAspectRatioNumerator)
        self.assertIsNotNone(codec_configuration.sampleAspectRatioDenominator)
        self.assertIsNotNone(codec_configuration.adaptiveQuantMode)
        self.assertIsNotNone(codec_configuration.lagInFrames)
        self.assertIsNotNone(codec_configuration.minQ)
        self.assertIsNotNone(codec_configuration.maxQ)
        self.assertIsNotNone(codec_configuration.undershootPct)
        self.assertIsNotNone(codec_configuration.overshootPct)
        self.assertIsNotNone(codec_configuration.clientBufferSize)
        self.assertIsNotNone(codec_configuration.clientInitialBufferSize)
        self.assertIsNotNone(codec_configuration.clientOptimalBufferSize)
        self.assertIsNotNone(codec_configuration.tileColumns)
        self.assertIsNotNone(codec_configuration.tileRows)
        self.assertIsNotNone(codec_configuration.automaticAltRefFramesEnabled)
        self.assertIsNotNone(codec_configuration.arnrMaxFrames)
        self.assertIsNotNone(codec_configuration.arnrStrength)
        self.assertIsNotNone(codec_configuration.cqLevel)
        self.assertIsNotNone(codec_configuration.maxIntraRate)
        self.assertIsNotNone(codec_configuration.maxInterRate)
        self.assertIsNotNone(codec_configuration.gfCbrBoost)
        self.assertIsNotNone(codec_configuration.lossless)
        self.assertIsNotNone(codec_configuration.frameParallel)
        self.assertIsNotNone(codec_configuration.sharpness)
        self.assertIsNotNone(codec_configuration.frameBoostEnabled)
        self.assertIsNotNone(codec_configuration.noiseSensitivity)
        self.assertIsNotNone(codec_configuration.minGfInterval)
        self.assertIsNotNone(codec_configuration.maxGfInterval)
        self.assertIsNotNone(codec_configuration.numTileGroups)
        self.assertIsNotNone(codec_configuration.mtuSize)

        return codec_configuration


if __name__ == '__main__':
    unittest.main()
