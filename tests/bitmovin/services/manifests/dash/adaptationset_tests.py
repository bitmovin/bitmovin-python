import unittest
import uuid
from bitmovin import Bitmovin, DashManifest, ACLEntry, ACLPermission, EncodingOutput, Period, AudioAdaptationSet, \
    VideoAdaptationSet, SubtitleAdaptationSet, AbstractAdaptationSet
from tests.bitmovin import BitmovinTestCase


class AdaptationSetTests(BitmovinTestCase):

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

    def test_add_audio_adaptationset(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.DASH.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)
        sample_period = self._get_sample_period_default()
        period_resource_response = self.bitmovin.manifests.DASH.add_period(
            object_=sample_period, manifest_id=manifest_resource_response.resource.id)
        self.assertIsNotNone(period_resource_response)
        self.assertIsNotNone(period_resource_response.resource)
        self.assertIsNotNone(period_resource_response.resource.id)
        self._compare_periods(sample_period, period_resource_response.resource)
        sample_audio_adaptationset = self._get_sample_audio_adaptationset()
        adaptationset_resource_response = self.bitmovin.manifests.DASH.add_audio_adaptation_set(
            object_=sample_audio_adaptationset, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id
        )
        self.assertIsNotNone(adaptationset_resource_response)
        self.assertIsNotNone(adaptationset_resource_response.resource)
        self.assertIsNotNone(adaptationset_resource_response.resource.id)
        self._compare_audio_adaptationsets(sample_audio_adaptationset, adaptationset_resource_response.resource)

    def test_add_video_adaptationset(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.DASH.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)
        sample_period = self._get_sample_period_default()
        period_resource_response = self.bitmovin.manifests.DASH.add_period(
            object_=sample_period, manifest_id=manifest_resource_response.resource.id)
        self.assertIsNotNone(period_resource_response)
        self.assertIsNotNone(period_resource_response.resource)
        self.assertIsNotNone(period_resource_response.resource.id)
        self._compare_periods(sample_period, period_resource_response.resource)
        sample_video_adaptationset = self._get_sample_video_adaptationset()
        adaptationset_resource_response = self.bitmovin.manifests.DASH.add_video_adaptation_set(
            object_=sample_video_adaptationset, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id
        )
        self.assertIsNotNone(adaptationset_resource_response)
        self.assertIsNotNone(adaptationset_resource_response.resource)
        self.assertIsNotNone(adaptationset_resource_response.resource.id)
        self._compare_video_adaptationsets(sample_video_adaptationset, adaptationset_resource_response.resource)
            
    def test_add_subtitle_adaptationset(self):
            sample_manifest = self._get_sample_manifest()
            manifest_resource_response = self.bitmovin.manifests.DASH.create(sample_manifest)
            self.assertIsNotNone(manifest_resource_response)
            self.assertIsNotNone(manifest_resource_response.resource)
            self.assertIsNotNone(manifest_resource_response.resource.id)
            self._compare_manifests(sample_manifest, manifest_resource_response.resource)
            sample_period = self._get_sample_period_default()
            period_resource_response = self.bitmovin.manifests.DASH.add_period(
                object_=sample_period, manifest_id=manifest_resource_response.resource.id)
            self.assertIsNotNone(period_resource_response)
            self.assertIsNotNone(period_resource_response.resource)
            self.assertIsNotNone(period_resource_response.resource.id)
            self._compare_periods(sample_period, period_resource_response.resource)
            sample_subtitle_adaptationset = self._get_sample_subtitle_adaptationset()
            adaptationset_resource_response = self.bitmovin.manifests.DASH.add_subtitle_adaptation_set(
                object_=sample_subtitle_adaptationset, manifest_id=manifest_resource_response.resource.id,
                period_id=period_resource_response.resource.id
            )
            self.assertIsNotNone(adaptationset_resource_response)
            self.assertIsNotNone(adaptationset_resource_response.resource)
            self.assertIsNotNone(adaptationset_resource_response.resource.id)
            self._compare_subtitle_adaptationsets(sample_subtitle_adaptationset, adaptationset_resource_response.resource)

    def _compare_manifests(self, first: DashManifest, second: DashManifest):
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(len(first.outputs), len(second.outputs))
        return True

    def _compare_periods(self, first: Period, second: Period):
        self.assertEqual(first.start, second.start)
        self.assertEqual(first.duration, second.duration)
        return True

    def _compare_adaptationsets(self, first: AbstractAdaptationSet, second: AbstractAdaptationSet):
        return True

    def _compare_audio_adaptationsets(self, first: AudioAdaptationSet, second: AudioAdaptationSet):
        self._compare_adaptationsets(first, second)
        self.assertEqual(first.lang, second.lang)
        return True

    def _compare_video_adaptationsets(self, first: VideoAdaptationSet, second: VideoAdaptationSet):
        self._compare_adaptationsets(first, second)
        return True

    def _compare_subtitle_adaptationsets(self, first: SubtitleAdaptationSet, second: SubtitleAdaptationSet):
        self._compare_adaptationsets(first, second)
        self.assertEqual(first.lang, second.lang)
        return True

    def _get_sample_manifest(self):

        encoding_output = self._get_sample_encoding_output()
        manifest = DashManifest(name='bitmovin-python Sample DASH Manifest', outputs=[encoding_output])

        self.assertIsNotNone(manifest)
        self.assertIsNotNone(manifest.name)
        self.assertIsNotNone(manifest.outputs)
        return manifest

    def _get_sample_encoding_output(self):
        acl_entry = ACLEntry(scope='string', permission=ACLPermission.PUBLIC_READ)

        sample_output = self.utils.get_sample_s3_output()
        s3_output = self.bitmovin.outputs.S3.create(sample_output)
        encoding_output = EncodingOutput(output_id=s3_output.resource.id,
                                         output_path='/bitmovin-python/StreamTests/'+str(uuid.uuid4()),
                                         acl=[acl_entry])

        return encoding_output

    def _get_sample_period_default(self):
        period = Period()
        return period

    def _get_special_period(self):
        period = self._get_sample_period_default()
        period.start = 1.33
        period.duration = 67.3
        return period

    def _get_sample_audio_adaptationset(self):
        audio_adaptationset = AudioAdaptationSet(lang='en')
        return audio_adaptationset

    def _get_sample_video_adaptationset(self):
        video_adaptationset = VideoAdaptationSet()
        return video_adaptationset

    def _get_sample_subtitle_adaptationset(self):
        subtitle_adaptationset = SubtitleAdaptationSet(lang='en')
        return subtitle_adaptationset

if __name__ == '__main__':
    unittest.main()
