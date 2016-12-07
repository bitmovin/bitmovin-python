import unittest
import uuid
from bitmovin import Bitmovin, DashManifest, ACLEntry, ACLPermission, EncodingOutput, Period
from tests.bitmovin import BitmovinTestCase


class PeriodTests(BitmovinTestCase):

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

    def test_add_period(self):
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

    def _compare_manifests(self, first: DashManifest, second: DashManifest):
        self.assertEqual(first.manifestName, second.manifestName)
        self.assertEqual(first.description, second.description)
        self.assertEqual(len(first.outputs), len(second.outputs))
        return True

    def _compare_periods(self, first: Period, second: Period):
        self.assertEqual(first.start, second.start)
        self.assertEqual(first.duration, second.duration)
        return True

    def _get_sample_manifest(self):

        encoding_output = self._get_sample_encoding_output()
        manifest = DashManifest(manifest_name='bitmovin-python_Sample_DASH_Manifest.mpd', outputs=[encoding_output])

        self.assertIsNotNone(manifest)
        self.assertIsNotNone(manifest.manifestName)
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


if __name__ == '__main__':
    unittest.main()
