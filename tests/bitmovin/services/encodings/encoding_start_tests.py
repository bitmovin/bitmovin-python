import unittest
import json
from bitmovin import Bitmovin, StartEncodingRequest, Scheduling, Tweaks, AudioVideoSyncMode, PerTitle, \
    H264PerTitleConfiguration, AutoRepresentation
from tests.bitmovin import BitmovinTestCase
from bitmovin.utils import BitmovinJSONEncoder


class EncodingStartTests(BitmovinTestCase):

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

    def test_encoding_start_request_serialization_with_prewarmed_instance_ids(self):
        prewarmed_instance_pool_ids = ['4a67260e-2fd3-4e9e-9829-651280ea8f06', '4b67260e-2fd3-4e9e-9829-651280ea8f07']
        scheduling = Scheduling(prewarmed_instance_pool_ids=prewarmed_instance_pool_ids)

        scheduling_serialized = json.dumps(obj=scheduling, cls=BitmovinJSONEncoder)
        self.assertEqual(first=scheduling_serialized, second='{"prewarmedInstancePoolIds": ["4a67260e-2fd3-4e9e-9829-651280ea8f06", "4b67260e-2fd3-4e9e-9829-651280ea8f07"]}')

        start_encoding_request = StartEncodingRequest(scheduling=scheduling)
        start_encoding_request_serialized = json.dumps(obj=start_encoding_request, cls=BitmovinJSONEncoder)
        self.assertEqual(first=start_encoding_request_serialized, second='{"scheduling": {"prewarmedInstancePoolIds": ["4a67260e-2fd3-4e9e-9829-651280ea8f06", "4b67260e-2fd3-4e9e-9829-651280ea8f07"]}}')

    def test_encoding_start_request_serialization_with_tweaks(self):
        tweaks = Tweaks(audio_video_sync_mode=AudioVideoSyncMode.RESYNC_AT_START)

        tweaks_serialized = json.dumps(obj=tweaks, cls=BitmovinJSONEncoder)
        self.assertEqual(first=tweaks_serialized, second='{"audioVideoSyncMode": "RESYNC_AT_START"}')

        start_encoding_request = StartEncodingRequest(tweaks=tweaks)
        start_encoding_request_serialized = json.dumps(obj=start_encoding_request, cls=BitmovinJSONEncoder)
        self.assertEqual(first=start_encoding_request_serialized, second='{"tweaks": {"audioVideoSyncMode": "RESYNC_AT_START"}}')

    def test_encoding_start_request_with_per_title_configuration(self):
        auto_representation = AutoRepresentation(adopt_configuration_threshold=1.5)
        h264_configuration = H264PerTitleConfiguration(auto_representations=auto_representation,
                                                       min_bitrate_step_size=15000, max_bitrate_step_size=20000,
                                                       min_bitrate=500000, max_bitrate=8000000, target_quality_crf=0.5)
        per_title = PerTitle(h264_configuration=h264_configuration)
        per_title_serialized = json.dumps(per_title, cls=BitmovinJSONEncoder)
        self.assertEqual(first=per_title_serialized, second='{"h264Configuration": {"min_bitrate": 500000, '
                                                            '"max_bitrate": 8000000, "min_bitrate_step_size": 15000, '
                                                            '"max_bitrate_step_size": 20000, "targetQualityCrf": 0.5, '
                                                            '"autoRepresentations": {"adoptConfigurationThreshold": '
                                                            '1.5}}}')

        start_encoding_request = StartEncodingRequest(per_title=per_title)
        start_encoding_request_serialized = json.dumps(obj=start_encoding_request, cls=BitmovinJSONEncoder)
        self.assertEqual(first=start_encoding_request_serialized, second='{"perTitle": {"h264Configuration": {'
                                                                         '"min_bitrate": 500000, "max_bitrate": '
                                                                         '8000000, "min_bitrate_step_size": 15000, '
                                                                         '"max_bitrate_step_size": 20000, '
                                                                         '"targetQualityCrf": 0.5, '
                                                                         '"autoRepresentations": {'
                                                                         '"adoptConfigurationThreshold": 1.5}}}}')


if __name__ == '__main__':
    unittest.main()
