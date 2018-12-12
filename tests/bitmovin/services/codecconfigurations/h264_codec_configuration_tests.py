import unittest
from bitmovin import Bitmovin, Response, H264CodecConfiguration, H264Profile, MVPredictionMode, H264Level, BAdapt, \
    ChromaLocation, ColorSpace, ColorPrimaries, ColorRange, ColorTransfer, InputColorSpace, InputColorRange, \
    ColorConfig, H264BPyramid, H264NalHrd, Cea608708SubtitleConfig
from bitmovin.errors import BitmovinApiError
from bitmovin.resources.enums.h264_interlace_mode import H264InterlaceMode
from bitmovin.resources.enums.h264_motion_estimation_method import H264MotionEstimationMethod
from bitmovin.resources.enums.h264_partition import H264Partition
from bitmovin.resources.enums.h264_sub_me import H264SubMe
from bitmovin.resources.enums.h264_trellis import H264Trellis
from bitmovin.resources.enums.pixel_format import PixelFormat
from bitmovin.resources.enums.h264_adaptive_quantization_mode import H264AdaptiveQuantizationMode
from tests.bitmovin import BitmovinTestCase


class MyAwesomeClass:
    def __init__(self, name, description, value_a, value_b, value_c):
        self.name = name
        self.description = description
        self.value_a = value_a
        self.value_b = value_b
        self.value_c = value_c


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

        my_custom_data = dict()
        my_custom_data['data'] = '<pre>my custom data</pre>'

        sample_codec_configuration = self._get_sample_h264_codec_configuration()
        sample_codec_configuration.customData = my_custom_data
        created_codec_configuration_response = self.bitmovin.codecConfigurations.H264.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_h264_codec_configurations(sample_codec_configuration,
                                                created_codec_configuration_response.resource)

        custom_data_response = self.bitmovin.codecConfigurations.H264.retrieve_custom_data(
            created_codec_configuration_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_codec_configuration.customData['data'], custom_data.customData['data'])

    def test_retrieve_h264_codec_configuration_custom_data_object(self):
        myobject_1 = MyAwesomeClass('mystring', 12, 34, True, None)
        myobject_2 = MyAwesomeClass('mystring', 1234, 1234.0, myobject_1, "@@@漢漢%$%$")

        sample_codec_configuration = self._get_sample_h264_codec_configuration()
        sample_codec_configuration.customData = myobject_2
        created_codec_configuration_response = self.bitmovin.codecConfigurations.H264.create(sample_codec_configuration)
        self.assertIsNotNone(created_codec_configuration_response)
        self.assertIsNotNone(created_codec_configuration_response.resource)
        self.assertIsNotNone(created_codec_configuration_response.resource.id)
        self._compare_h264_codec_configurations(sample_codec_configuration,
                                                created_codec_configuration_response.resource)

        custom_data_response = self.bitmovin.codecConfigurations.H264.retrieve_custom_data(
            created_codec_configuration_response.resource.id)
        custom_data = custom_data_response.resource

        self.assertIsNotNone(custom_data.customData)
        self.assertEqual(sample_codec_configuration.customData.name, custom_data.customData['name'])
        self.assertEqual(sample_codec_configuration.customData.description, custom_data.customData['description'])
        self.assertEqual(sample_codec_configuration.customData.value_a, custom_data.customData['value_a'])
        self.assertEqual(sample_codec_configuration.customData.value_c, custom_data.customData['value_c'])
        self.assertEqual(sample_codec_configuration.customData.value_b.name, custom_data.customData['value_b']['name'])
        self.assertEqual(sample_codec_configuration.customData.value_b.description,
                         custom_data.customData['value_b']['description'])
        self.assertEqual(sample_codec_configuration.customData.value_b.value_a,
                         custom_data.customData['value_b']['value_a'])
        self.assertEqual(sample_codec_configuration.customData.value_b.value_b,
                         custom_data.customData['value_b']['value_b'])
        self.assertEqual(sample_codec_configuration.customData.value_b.value_c,
                         custom_data.customData['value_b']['value_c'])

    def test_create_h264_codec_config_with_bitrate_and_crf(self):
        sample_codec_configuration = self._get_sample_h264_codec_configuration()
        self.assertIsNotNone(sample_codec_configuration.bitrate)

        sample_codec_configuration.crf = 51.0
        self.assertEqual(sample_codec_configuration.crf, 51.0)
        try:
            self.bitmovin.codecConfigurations.H264.create(sample_codec_configuration)

        except BitmovinApiError as error:
            self.assertEqual(error.response.status, 'ERROR')
            self.assertEqual(error.response.data.code, 1001)

    def test_create_h264_codec_configuration_with_crf(self):
            sample_codec_configuration = self._get_sample_h264_codec_configuration()
            sample_codec_configuration.bitrate = None
            sample_codec_configuration.crf = 51.0

            codec_configuration_resource_response = self.bitmovin.codecConfigurations.H264.create(
                sample_codec_configuration)

            self.assertIsNotNone(codec_configuration_resource_response)
            self.assertIsNotNone(codec_configuration_resource_response.resource)
            self.assertIsNotNone(codec_configuration_resource_response.resource.id)
            self._compare_h264_codec_configurations(sample_codec_configuration,
                                                    codec_configuration_resource_response.resource)

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
        self.assertEqual(first.rc_lookahead, second.rc_lookahead)
        self.assertEqual(first.sub_me, second.sub_me)
        self.assertEqual(first.motion_estimation_method, second.motion_estimation_method)
        self.assertEqual(first.b_adapt, second.b_adapt)
        self.assertEqual(first.partitions, second.partitions)
        self.assertEqual(first.trellis, second.trellis)
        self.assertEqual(first.slices, second.slices)
        self.assertEqual(first.interlaceMode, second.interlaceMode)
        self.assertEqual(first.crf, second.crf)
        self.assertEqual(first.minKeyframeInterval, second.minKeyframeInterval)
        self.assertEqual(first.maxKeyframeInterval, second.maxKeyframeInterval)
        self.assertEqual(first.pixelFormat, second.pixelFormat)
        self.assertEqual(first.sampleAspectRatioNumerator, second.sampleAspectRatioNumerator)
        self.assertEqual(first.sampleAspectRatioDenominator, second.sampleAspectRatioDenominator)
        self.assertEqual(first.sceneCutThreshold, second.sceneCutThreshold)
        self.assertEqual(first.bPyramid, second.bPyramid)
        self.assertEqual(first.nalHrd, second.nalHrd)
        self.assertEqual(first.openGop, second.openGop)
        self.assertTrue(self._compare_color_configs(first.colorConfig, second.colorConfig))
        self.assertTrue(self._compare_cea_608_708_subtitle_configs(first.cea608708SubtitleConfig,
                                                                   second.cea608708SubtitleConfig))
        self.assertEqual(first.adaptiveQuantizationMode, second.adaptiveQuantizationMode)
        self.assertEqual(first.adaptiveQuantizationStrength, second.adaptiveQuantizationStrength)
        self.assertEqual(first.psyRateDistortionOptimization, second.psyRateDistortionOptimization)
        self.assertEqual(first.psyTrellis, second.psyTrellis)
        self.assertEqual(first.deblockAlpha, second.deblockAlpha)
        self.assertEqual(first.deblockBeta, second.deblockBeta)
        
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

    def _compare_cea_608_708_subtitle_configs(self, first: Cea608708SubtitleConfig, second: Cea608708SubtitleConfig):
        """

        :param first: Cea608708SubtitleConfig
        :param second: Cea608708SubtitleConfig
        :return: bool
        """
        self.assertEqual(first.passthroughActivated, second.passthroughActivated)
        return True

    def _get_sample_h264_codec_configuration(self):
        h264_codec_configuration = H264CodecConfiguration(
            name='Python - H264 Sample Codec Config',
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
            level=H264Level.L5_1,
            rc_lookahead=30,
            sub_me=H264SubMe.RD_IP,
            motion_estimation_method=H264MotionEstimationMethod.HEX,
            b_adapt=BAdapt.FAST,
            partitions=[H264Partition.I4X4, H264Partition.I8X8, H264Partition.P8X8, H264Partition.B8X8],
            trellis=H264Trellis.ENABLED_FINAL_MB,
            slices=5,
            interlaceMode=H264InterlaceMode.BOTTOM_FIELD_FIRST,
            min_keyframe_interval=10.23,
            max_keyframe_interval=20.91,
            pixel_format=PixelFormat.YUV440P10BE,
            sample_aspect_ratio_numerator=2.0,
            sample_aspect_ratio_denominator=3.0,
            scene_cut_threshold=30,
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
            ),
            nal_hrd=H264NalHrd.VBR,
            b_pyramid=H264BPyramid.NONE,
            open_gop=True,
            cea_608_708_subtitle_config=Cea608708SubtitleConfig(
                passthrough_activated=True
            ),
            adaptive_quantization_mode=H264AdaptiveQuantizationMode.AUTO_VARIANCE_DARK_SCENES,
            adaptive_quantization_strength=0.5,
            psy_rate_distortion_optimization=1.0,
            psy_trellis=0.25,
            deblock_alpha=1,
            deblock_beta=1
        )

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
        self.assertIsNotNone(h264_codec_configuration.rc_lookahead)
        self.assertIsNotNone(h264_codec_configuration.sub_me)
        self.assertIsNotNone(h264_codec_configuration.motion_estimation_method)
        self.assertIsNotNone(h264_codec_configuration.b_adapt)
        self.assertIsNotNone(h264_codec_configuration.partitions)
        self.assertIsNotNone(h264_codec_configuration.trellis)
        self.assertIsNotNone(h264_codec_configuration.slices)
        self.assertIsNotNone(h264_codec_configuration.interlaceMode)
        self.assertIsNotNone(h264_codec_configuration.minKeyframeInterval)
        self.assertIsNotNone(h264_codec_configuration.maxKeyframeInterval)
        self.assertIsNotNone(h264_codec_configuration.pixelFormat)
        self.assertIsNotNone(h264_codec_configuration.colorConfig)
        self.assertIsNotNone(h264_codec_configuration.nalHrd)
        self.assertIsNotNone(h264_codec_configuration.bPyramid)
        self.assertIsNotNone(h264_codec_configuration.openGop)
        self.assertIsNotNone(h264_codec_configuration.cea608708SubtitleConfig)
        self.assertIsNotNone(h264_codec_configuration.adaptiveQuantizationMode)
        self.assertIsNotNone(h264_codec_configuration.adaptiveQuantizationStrength)
        self.assertIsNotNone(h264_codec_configuration.psyRateDistortionOptimization)
        self.assertIsNotNone(h264_codec_configuration.psyTrellis)
        self.assertIsNotNone(h264_codec_configuration.deblockAlpha)
        self.assertIsNotNone(h264_codec_configuration.deblockBeta)

        return h264_codec_configuration


if __name__ == '__main__':
    unittest.main()
