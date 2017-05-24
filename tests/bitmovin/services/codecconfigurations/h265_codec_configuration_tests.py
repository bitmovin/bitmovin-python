import unittest
import json
from bitmovin import Bitmovin, Response, H265CodecConfiguration, H265Profile, H265Level, BAdapt, MaxCTUSize, \
    TUIntraDepth, TUInterDepth, MotionSearch
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
            self.assertEqual(error.response.data.message,
                             '400 Both bitrate and crf are set. Only one of them is allowed.')

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
        return True

    def _get_sample_h265_codec_configuration(self):
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
                                                          sao=True)

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

        return h265_codec_configuration


if __name__ == '__main__':
    unittest.main()
