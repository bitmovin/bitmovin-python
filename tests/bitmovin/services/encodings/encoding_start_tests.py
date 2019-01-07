import unittest
import json
from bitmovin import Bitmovin, StartEncodingRequest, Scheduling, Tweaks, AudioVideoSyncMode, PerTitle, \
    H264PerTitleConfiguration, AutoRepresentation, H265PerTitleConfiguration, VP9PerTitleConfiguration, \
    VodDashStartManifest, VodHlsStartManifest
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
        self.assertEqual(first=scheduling_serialized, second='{"prewarmedInstancePoolIds": '
                                                             '["4a67260e-2fd3-4e9e-9829-651280ea8f06", '
                                                             '"4b67260e-2fd3-4e9e-9829-651280ea8f07"]}')

        start_encoding_request = StartEncodingRequest(scheduling=scheduling)
        start_encoding_request_serialized = json.dumps(obj=start_encoding_request, cls=BitmovinJSONEncoder)
        self.assertEqual(first=start_encoding_request_serialized, second='{"scheduling": {"prewarmedInstancePoolIds": '
                                                                         '["4a67260e-2fd3-4e9e-9829-651280ea8f06", '
                                                                         '"4b67260e-2fd3-4e9e-9829-651280ea8f07"]}}')

    def test_encoding_start_request_serialization_with_tweaks(self):
        tweaks = Tweaks(audio_video_sync_mode=AudioVideoSyncMode.RESYNC_AT_START)

        tweaks_serialized = json.dumps(obj=tweaks, cls=BitmovinJSONEncoder)
        self.assertEqual(first=tweaks_serialized, second='{"audioVideoSyncMode": "RESYNC_AT_START"}')

        start_encoding_request = StartEncodingRequest(tweaks=tweaks)
        start_encoding_request_serialized = json.dumps(obj=start_encoding_request, cls=BitmovinJSONEncoder)
        self.assertEqual(
            first=start_encoding_request_serialized,
            second='{"tweaks": {"audioVideoSyncMode": "RESYNC_AT_START"}}'
        )

    def test_encoding_start_request_with_h264_per_title_configuration(self):
        auto_representation = AutoRepresentation(adopt_configuration_threshold=1.5)
        h264_configuration = H264PerTitleConfiguration(auto_representations=auto_representation,
                                                       min_bitrate_step_size=15000, max_bitrate_step_size=20000,
                                                       min_bitrate=500000, max_bitrate=8000000, target_quality_crf=0.5,
                                                       codec_min_bitrate_factor=1, codec_max_bitrate_factor=1,
                                                       codec_bufsize_factor=2, complexity_factor=1.7)

        per_title = PerTitle(h264_configuration=h264_configuration)
        per_title_serialized = json.dumps(per_title, cls=BitmovinJSONEncoder)

        self.assertEqual(first=per_title_serialized, second='{"h264Configuration": {"minBitrate": 500000, '
                                                            '"maxBitrate": 8000000, "minBitrateStepSize": 15000, '
                                                            '"maxBitrateStepSize": 20000, "complexityFactor": 1.7, '
                                                            '"targetQualityCrf": 0.5, "codecMinBitrateFactor": 1, '
                                                            '"codecMaxBitrateFactor": 1, "codecBufsizeFactor": 2, '
                                                            '"autoRepresentations": '
                                                            '{"adoptConfigurationThreshold": 1.5}}}')

        start_encoding_request = StartEncodingRequest(per_title=per_title)
        start_encoding_request_serialized = json.dumps(obj=start_encoding_request, cls=BitmovinJSONEncoder)
        self.assertEqual(
            first=start_encoding_request_serialized,
            second='{"perTitle": {"h264Configuration": {"minBitrate": 500000, '
                   '"maxBitrate": 8000000, "minBitrateStepSize": 15000, '
                   '"maxBitrateStepSize": 20000, "complexityFactor": 1.7, '
                   '"targetQualityCrf": 0.5, "codecMinBitrateFactor": 1, '
                   '"codecMaxBitrateFactor": 1, "codecBufsizeFactor": 2, '
                   '"autoRepresentations": {"adoptConfigurationThreshold": 1.5}}}}'
        )

    def test_encoding_start_request_with_h265_per_title_configuration(self):
        auto_representation = AutoRepresentation(adopt_configuration_threshold=1.5)
        h265_configuration = H265PerTitleConfiguration(auto_representations=auto_representation,
                                                       min_bitrate_step_size=15000, max_bitrate_step_size=20000,
                                                       min_bitrate=500000, max_bitrate=8000000, target_quality_crf=0.5,
                                                       codec_min_bitrate_factor=1, codec_max_bitrate_factor=1,
                                                       codec_bufsize_factor=2, complexity_factor=1.7)
        per_title = PerTitle(h265_configuration=h265_configuration)
        per_title_serialized = json.dumps(per_title, cls=BitmovinJSONEncoder)
        self.assertEqual(
            first=per_title_serialized,
            second='{"h265Configuration": {"minBitrate": 500000, '
                   '"maxBitrate": 8000000, "minBitrateStepSize": 15000, '
                   '"maxBitrateStepSize": 20000, "complexityFactor": 1.7, '
                   '"targetQualityCrf": 0.5, "codecMinBitrateFactor": 1, '
                   '"codecMaxBitrateFactor": 1, "codecBufsizeFactor": 2, '
                   '"autoRepresentations": {"adoptConfigurationThreshold": 1.5}}}'
        )

        start_encoding_request = StartEncodingRequest(per_title=per_title)
        start_encoding_request_serialized = json.dumps(obj=start_encoding_request, cls=BitmovinJSONEncoder)
        self.assertEqual(
            first=start_encoding_request_serialized,
            second='{"perTitle": {"h265Configuration": {"minBitrate": 500000, '
                   '"maxBitrate": 8000000, "minBitrateStepSize": 15000, '
                   '"maxBitrateStepSize": 20000, "complexityFactor": 1.7, '
                   '"targetQualityCrf": 0.5, "codecMinBitrateFactor": 1, '
                   '"codecMaxBitrateFactor": 1, "codecBufsizeFactor": 2, '
                   '"autoRepresentations": {"adoptConfigurationThreshold": 1.5}}}}'
        )

    def test_encoding_start_request_with_vp9_per_title_configuration(self):
        auto_representation = AutoRepresentation(adopt_configuration_threshold=1.5)
        vp9_configuration = VP9PerTitleConfiguration(auto_representations=auto_representation,
                                                     min_bitrate_step_size=15000, max_bitrate_step_size=20000,
                                                     min_bitrate=500000, max_bitrate=8000000, target_quality_crf=0.5,
                                                     complexity_factor=1.7)
        per_title = PerTitle(vp9_configuration=vp9_configuration)
        per_title_serialized = json.dumps(per_title, cls=BitmovinJSONEncoder)
        self.assertEqual(first=per_title_serialized, second='{"vp9Configuration": {"minBitrate": 500000, '
                                                            '"maxBitrate": 8000000, "minBitrateStepSize": 15000, '
                                                            '"maxBitrateStepSize": 20000, "complexityFactor": 1.7, '
                                                            '"targetQualityCrf": 0.5, "autoRepresentations": '
                                                            '{"adoptConfigurationThreshold": 1.5}}}')

        start_encoding_request = StartEncodingRequest(per_title=per_title)
        start_encoding_request_serialized = json.dumps(obj=start_encoding_request, cls=BitmovinJSONEncoder)
        self.assertEqual(first=start_encoding_request_serialized, second='{"perTitle": {"vp9Configuration": {'
                                                                         '"minBitrate": 500000, "maxBitrate": '
                                                                         '8000000, "minBitrateStepSize": 15000, '
                                                                         '"maxBitrateStepSize": 20000, '
                                                                         '"complexityFactor": 1.7, '
                                                                         '"targetQualityCrf": 0.5, '
                                                                         '"autoRepresentations": {'
                                                                         '"adoptConfigurationThreshold": 1.5}}}}')

    def test_encoding_start_request_with_dash_vod_manifest(self):
        uuid_1 = '731ec108-c5fb-4f31-ac42-823428e295f8'
        uuid_2 = 'a38ead99-e24a-4130-80fd-95502eb388f9'

        vod_dash_manifest_1 = VodDashStartManifest(manifest_id=uuid_1)
        vod_dash_manifest_2 = VodDashStartManifest(manifest_id=uuid_2)

        vod_dash_manifests = [vod_dash_manifest_1, vod_dash_manifest_2]

        start_encoding_request = StartEncodingRequest(vod_dash_manifests=vod_dash_manifests)
        start_encoding_request_serialized = json.dumps(obj=start_encoding_request, cls=BitmovinJSONEncoder)

        expected_start_manifest_payload = '{"vodDashManifests": [' + \
                                          '{"manifestId": "731ec108-c5fb-4f31-ac42-823428e295f8"}' + \
                                          ', ' + \
                                          '{"manifestId": "a38ead99-e24a-4130-80fd-95502eb388f9"}' + \
                                          ']}'

        self.assertEqual(first=start_encoding_request_serialized, second=expected_start_manifest_payload)

    def test_encoding_start_request_with_hls_vod_manifest(self):
        uuid_1 = 'b252e1d0-a252-4c7b-a99b-340c14d15bbb'
        uuid_2 = '90aba55c-b449-4a7e-b691-5607c7ac971b'

        vod_hls_manifest_1 = VodHlsStartManifest(manifest_id=uuid_1)
        vod_hls_manifest_2 = VodHlsStartManifest(manifest_id=uuid_2)

        vod_hls_manifests = [vod_hls_manifest_1, vod_hls_manifest_2]

        start_encoding_request = StartEncodingRequest(vod_hls_manifests=vod_hls_manifests)
        start_encoding_request_serialized = json.dumps(obj=start_encoding_request, cls=BitmovinJSONEncoder)

        expected_start_manifest_payload = '{"vodHlsManifests": [' + \
                                          '{"manifestId": "b252e1d0-a252-4c7b-a99b-340c14d15bbb"}' + \
                                          ', ' + \
                                          '{"manifestId": "90aba55c-b449-4a7e-b691-5607c7ac971b"}' + \
                                          ']}'

        self.assertEqual(first=start_encoding_request_serialized, second=expected_start_manifest_payload)

    def test_encoding_start_request_with_dash_and_hls_vod_manifest(self):
        uuid_1 = '731ec108-c5fb-4f31-ac42-823428e295f8'
        uuid_2 = 'a38ead99-e24a-4130-80fd-95502eb388f9'
        uuid_3 = 'b252e1d0-a252-4c7b-a99b-340c14d15bbb'
        uuid_4 = '90aba55c-b449-4a7e-b691-5607c7ac971b'

        vod_dash_manifest_1 = VodDashStartManifest(manifest_id=uuid_1)
        vod_dash_manifest_2 = VodDashStartManifest(manifest_id=uuid_2)

        vod_dash_manifests = [vod_dash_manifest_1, vod_dash_manifest_2]

        vod_hls_manifest_1 = VodHlsStartManifest(manifest_id=uuid_3)
        vod_hls_manifest_2 = VodHlsStartManifest(manifest_id=uuid_4)

        vod_hls_manifests = [vod_hls_manifest_1, vod_hls_manifest_2]

        start_encoding_request = StartEncodingRequest(vod_dash_manifests=vod_dash_manifests,
                                                      vod_hls_manifests=vod_hls_manifests)

        start_encoding_request_serialized = json.dumps(obj=start_encoding_request, cls=BitmovinJSONEncoder)

        expected_start_manifest_payload = '{"vodDashManifests": [' + \
                                          '{"manifestId": "731ec108-c5fb-4f31-ac42-823428e295f8"}' + \
                                          ', ' + \
                                          '{"manifestId": "a38ead99-e24a-4130-80fd-95502eb388f9"}' + \
                                          '], ' + \
                                          '"vodHlsManifests": [' + \
                                          '{"manifestId": "b252e1d0-a252-4c7b-a99b-340c14d15bbb"}' + \
                                          ', ' + \
                                          '{"manifestId": "90aba55c-b449-4a7e-b691-5607c7ac971b"}' + \
                                          ']}'

        self.assertEqual(first=start_encoding_request_serialized, second=expected_start_manifest_payload)


if __name__ == '__main__':
    unittest.main()
