import unittest
import json
from bitmovin import Bitmovin, Response, H265CodecConfiguration, H265Profile, H265Level, BAdapt, MaxCTUSize, \
    TUIntraDepth, TUInterDepth, MotionSearch, ChromaLocation, ColorSpace, ColorPrimaries, ColorRange, ColorTransfer, \
    InputColorSpace, InputColorRange, ColorConfig, VideoFormat, H265AdaptiveQuantizationMode
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class H265CodecConfigurationTests(BitmovinTestCase):

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
        sample_codec_configuration = self._get_sample_h265_codec_configuration()
        codec_configuration_resource_response = self.bitmovin.codecConfigurations.H265.create(
            sample_codec_configuration)
        self.assertIsNotNone(codec_configuration_resource_response)
        self.assertIsNotNone(codec_configuration_resource_response.resource)
        self.assertIsNotNone(codec_configuration_resource_response.resource.id)
        self._compare_h265_codec_configurations(sample_codec_configuration,
                                                codec_configuration_resource_response.resource)

    def test_retrieve_h265_codec_configuration(self):
        sample_codec_configuration = self._get_sample_h265_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.H265.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_h265_codec_configurations(sample_codec_configuration,
                                                created_codec_configuration_response.resource)

        retrieved_codec_configuration_response = self.bitmovin.codecConfigurations.H265.retrieve(
            created_codec_configuration_response.resource.id)
        self.assertIsNotNone(retrieved_codec_configuration_response)
        self.assertIsNotNone(retrieved_codec_configuration_response.resource)
        self._compare_h265_codec_configurations(created_codec_configuration_response.resource,
                                                retrieved_codec_configuration_response.resource)

    def test_delete_h265_codec_configuration(self):
        sample_codec_configuration = self._get_sample_h265_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.H265.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_h265_codec_configurations(sample_codec_configuration,
                                                created_codec_configuration_response.resource)

        deleted_minimal_resource = self.bitmovin.codecConfigurations.H265.delete(
            created_codec_configuration_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.codecConfigurations.H265.retrieve(created_codec_configuration_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving codec_configuration after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_h265_codec_configurations(self):
        sample_codec_configuration = self._get_sample_h265_codec_configuration()
        created_codec_configuration_response = self.bitmovin.codecConfigurations.H265.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_h265_codec_configurations(sample_codec_configuration,
                                                created_codec_configuration_response.resource)

        codec_configurations = self.bitmovin.codecConfigurations.H265.list()
        self.assertIsNotNone(codec_configurations)
        self.assertIsNotNone(codec_configurations.resource)
        self.assertIsNotNone(codec_configurations.response)
        self.assertIsInstance(codec_configurations.resource, list)
        self.assertIsInstance(codec_configurations.response, Response)
        self.assertGreater(codec_configurations.resource.__sizeof__(), 1)

    def test_retrieve_h265_codec_configuration_custom_data(self):
        sample_codec_configuration = self._get_sample_h265_codec_configuration()
        sample_codec_configuration.customData = '<pre>my custom data</pre>'
        created_codec_configuration_response = self.bitmovin.codecConfigurations.H265.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_h265_codec_configurations(sample_codec_configuration,
                                                created_codec_configuration_response.resource)

        custom_data_response = self.bitmovin.codecConfigurations.H265.retrieve_custom_data(
            created_codec_configuration_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_codec_configuration.customData, json.loads(custom_data.customData))

    def test_create_h265_codec_config_with_bitrate_and_crf(self):
        sample_codec_configuration = self._get_sample_h265_codec_configuration()
        self.assertIsNotNone(sample_codec_configuration.bitrate)

        sample_codec_configuration.crf = 51.0
        self.assertEqual(sample_codec_configuration.crf, 51.0)
        try:
            self.bitmovin.codecConfigurations.H265.create(sample_codec_configuration)

        except BitmovinApiError as error:
            self.assertEqual(error.response.status, 'ERROR')
            self.assertEqual(error.response.data.code, 1001)

    def test_create_h265_codec_configuration_with_crf(self):
            sample_codec_configuration = self._get_sample_h265_codec_configuration()
            sample_codec_configuration.bitrate = None
            sample_codec_configuration.crf = 51.0

            codec_configuration_resource_response = self.bitmovin.codecConfigurations.H265.create(
                sample_codec_configuration)

            self.assertIsNotNone(codec_configuration_resource_response)
            self.assertIsNotNone(codec_configuration_resource_response.resource)
            self.assertIsNotNone(codec_configuration_resource_response.resource.id)
            self._compare_h265_codec_configurations(sample_codec_configuration,
                                                    codec_configuration_resource_response.resource)

    def test_create_h265_codec_configuration_with_hlg_signaling_activated(self):
            sample_codec_configuration = self._get_sample_h265_codec_configuration()
            sample_codec_configuration.enableHlgSignaling = True

            codec_configuration_resource_response = self.bitmovin.codecConfigurations.H265.create(
                sample_codec_configuration)

            self.assertIsNotNone(codec_configuration_resource_response)
            self.assertIsNotNone(codec_configuration_resource_response.resource)
            self.assertIsNotNone(codec_configuration_resource_response.resource.id)
            self._compare_h265_codec_configurations(sample_codec_configuration,
                                                    codec_configuration_resource_response.resource)

    def test_create_h265_codec_configuration_with_hlg_signaling_disabled(self):
            sample_codec_configuration = self._get_sample_h265_codec_configuration()
            sample_codec_configuration.enableHlgSignaling = False

            codec_configuration_resource_response = self.bitmovin.codecConfigurations.H265.create(
                sample_codec_configuration)

            self.assertIsNotNone(codec_configuration_resource_response)
            self.assertIsNotNone(codec_configuration_resource_response.resource)
            self.assertIsNotNone(codec_configuration_resource_response.resource.id)
            self._compare_h265_codec_configurations(sample_codec_configuration,
                                                    codec_configuration_resource_response.resource)

    def test_create_h265_codec_configuration_with_video_format_secam(self):
        sample_codec_configuration = self._get_sample_h265_codec_configuration()
        sample_codec_configuration.videoFormat = VideoFormat.SECAM

        codec_configuration_resource_response = self.bitmovin.codecConfigurations.H265.create(
            sample_codec_configuration)

        self.assertIsNotNone(codec_configuration_resource_response)
        self.assertIsNotNone(codec_configuration_resource_response.resource)
        self.assertIsNotNone(codec_configuration_resource_response.resource.id)
        self._compare_h265_codec_configurations(sample_codec_configuration,
                                                codec_configuration_resource_response.resource)

    def test_create_h265_codec_configuration_with_qpMin_qpMax(self):
        sample_codec_configuration = self._get_sample_h265_codec_configuration()

        sample_codec_configuration.qp = None
        sample_codec_configuration.qpMin = 1
        sample_codec_configuration.qpMax = 2

        codec_configuration_resource_response = self.bitmovin.codecConfigurations.H265.create(
            sample_codec_configuration)

        self.assertIsNotNone(codec_configuration_resource_response)
        self.assertIsNotNone(codec_configuration_resource_response.resource)
        self.assertIsNotNone(codec_configuration_resource_response.resource.id)
        self._compare_h265_codec_configurations(sample_codec_configuration,
                                                codec_configuration_resource_response.resource)

        pass

    def _compare_h265_codec_configurations(self, first: H265CodecConfiguration, second: H265CodecConfiguration):
        """

        :param first: H265CodecConfiguration
        :param second: H265CodecConfiguration
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
        self.assertEqual(first.qp, second.qp)
        self.assertEqual(first.maxBitrate, second.maxBitrate)
        self.assertEqual(first.minBitrate, second.minBitrate)
        self.assertEqual(first.bufsize, second.bufsize)
        self.assertEqual(first.minGop, second.minGop)
        self.assertEqual(first.maxGop, second.maxGop)
        self.assertEqual(first.level, second.level)
        self.assertEqual(first.rcLookahead, second.rcLookahead)
        self.assertEqual(first.bAdapt, second.bAdapt)
        self.assertEqual(first.maxCTUSize, second.maxCTUSize)
        self.assertEqual(first.tuIntraDepth, second.tuIntraDepth)
        self.assertEqual(first.tuInterDepth, second.tuInterDepth)
        self.assertEqual(first.motionSearch, second.motionSearch)
        self.assertEqual(first.subMe, second.subMe)
        self.assertEqual(first.motionSearchRange, second.motionSearchRange)
        self.assertEqual(first.weightPredictionOnBSlice, second.weightPredictionOnBSlice)
        self.assertEqual(first.weightPredictionOnPSlice, second.weightPredictionOnPSlice)
        self.assertEqual(first.sao, second.sao)
        self.assertEqual(first.crf, second.crf)
        self.assertEqual(first.maxKeyframeInterval, second.maxKeyframeInterval)
        self.assertEqual(first.minKeyframeInterval, second.minKeyframeInterval)
        self.assertEqual(first.sceneCutThreshold, second.sceneCutThreshold)
        self.assertEqual(first.enableHlgSignaling, second.enableHlgSignaling)
        self.assertEqual(first.videoFormat, second.videoFormat)
        self.assertEqual(first.hdr, second.hdr)
        self.assertEqual(first.masterDisplay, second.masterDisplay)
        self.assertEqual(first.maxContentLightLevel, second.maxContentLightLevel)
        self.assertEqual(first.maxPictureAverageLightLevel, second.maxPictureAverageLightLevel)
        self.assertEqual(first.sampleAspectRatioNumerator, second.sampleAspectRatioNumerator)
        self.assertEqual(first.sampleAspectRatioDenominator, second.sampleAspectRatioDenominator)
        self.assertEqual(first.adaptiveQuantizationMode, second.adaptiveQuantizationMode)
        self.assertEqual(first.psyRateDistortionOptimization, second.psyRateDistortionOptimization)
        self.assertEqual(first.psyRateDistortionOptimizedQuantization, second.psyRateDistortionOptimizedQuantization)
        self.assertEqual(first.cutree, second.cutree)
        self.assertEqual(first.qpMin, second.qpMin)
        self.assertEqual(first.qpMax, second.qpMax)
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

    def _get_sample_h265_codec_configuration(self):
        master_display_sample = 'G(13250,34500)B(7500,3000)R(34000,16000)WP(15635,16450)L(10000000,10)'

        h265_codec_configuration = H265CodecConfiguration(name='H265 Sample Codec Config',
                                                          description='Long description for H265 Codec Config',
                                                          bitrate=10000000,
                                                          rate=23.97,
                                                          profile=H265Profile.main,
                                                          width=1920,
                                                          height=1080,
                                                          bframes=3,
                                                          ref_frames=5,
                                                          qp=10,
                                                          max_bitrate=10000000,
                                                          min_bitrate=5000000,
                                                          level=H265Level.L5_1,
                                                          bufsize=10000000,
                                                          min_gop=None,
                                                          max_gop=None,
                                                          rc_lookahead=20,
                                                          b_adapt=BAdapt.FULL,
                                                          max_ctu_size=MaxCTUSize.S64,
                                                          tu_intra_depth=TUIntraDepth.D1,
                                                          tu_inter_depth=TUInterDepth.D1,
                                                          motion_search=MotionSearch.HEX,
                                                          sub_me=2,
                                                          motion_search_range=57,
                                                          weight_prediction_on_b_slice=False,
                                                          weight_prediction_on_p_slice=True,
                                                          sao=True,
                                                          crf=None,
                                                          pixel_format=None,
                                                          scene_cut_threshold=30,
                                                          max_keyframe_interval=5,
                                                          min_keyframe_interval=3,
                                                          hdr=True,
                                                          master_display=master_display_sample,
                                                          max_content_light_level=800,
                                                          max_picture_average_light_level=400,
                                                          sample_aspect_ratio_numerator=2.0,
                                                          sample_aspect_ratio_denominator=3.0,
                                                          adaptive_quantization_mode=H265AdaptiveQuantizationMode.AUTO_VARIANCE,
                                                          psy_rate_distortion_optimization=0,
                                                          psy_rate_distortion_optimization_quantization=0,
                                                          cutree=False,
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
                                                              input_color_range=InputColorRange.JPEG
                                                          ))

        self.assertIsNotNone(h265_codec_configuration.name)
        self.assertIsNotNone(h265_codec_configuration.description)
        self.assertIsNotNone(h265_codec_configuration.bitrate)
        self.assertIsNotNone(h265_codec_configuration.rate)
        self.assertIsNotNone(h265_codec_configuration.profile)
        self.assertIsNotNone(h265_codec_configuration.width)
        self.assertIsNotNone(h265_codec_configuration.height)
        self.assertIsNotNone(h265_codec_configuration.bframes)
        self.assertIsNotNone(h265_codec_configuration.refFrames)
        self.assertIsNotNone(h265_codec_configuration.qp)
        self.assertIsNotNone(h265_codec_configuration.maxBitrate)
        self.assertIsNotNone(h265_codec_configuration.minBitrate)
        self.assertIsNotNone(h265_codec_configuration.level)
        self.assertIsNotNone(h265_codec_configuration.bufsize)
        self.assertIsNotNone(h265_codec_configuration.rcLookahead)
        self.assertIsNotNone(h265_codec_configuration.bAdapt)
        self.assertIsNotNone(h265_codec_configuration.maxCTUSize)
        self.assertIsNotNone(h265_codec_configuration.tuIntraDepth)
        self.assertIsNotNone(h265_codec_configuration.tuInterDepth)
        self.assertIsNotNone(h265_codec_configuration.motionSearch)
        self.assertIsNotNone(h265_codec_configuration.subMe)
        self.assertIsNotNone(h265_codec_configuration.motionSearchRange)
        self.assertIsNotNone(h265_codec_configuration.weightPredictionOnPSlice)
        self.assertIsNotNone(h265_codec_configuration.weightPredictionOnBSlice)
        self.assertIsNotNone(h265_codec_configuration.sao)
        self.assertIsNotNone(h265_codec_configuration.hdr)
        self.assertIsNotNone(h265_codec_configuration.masterDisplay)
        self.assertIsNotNone(h265_codec_configuration.maxContentLightLevel)
        self.assertIsNotNone(h265_codec_configuration.maxPictureAverageLightLevel)
        self.assertIsNotNone(h265_codec_configuration.sampleAspectRatioNumerator)
        self.assertIsNotNone(h265_codec_configuration.sampleAspectRatioDenominator)
        self.assertIsNotNone(h265_codec_configuration.adaptiveQuantizationMode)
        self.assertIsNotNone(h265_codec_configuration.psyRateDistortionOptimization)
        self.assertIsNotNone(h265_codec_configuration.psyRateDistortionOptimizedQuantization)
        self.assertIsNotNone(h265_codec_configuration.cutree)

        return h265_codec_configuration


if __name__ == '__main__':
    unittest.main()
