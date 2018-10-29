import unittest
import uuid
from bitmovin import Bitmovin, DashManifest, ACLEntry, ACLPermission, EncodingOutput, Period, CustomXMLElement
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
        sample_period = Period()
        period_resource_response = self.bitmovin.manifests.DASH.add_period(
            object_=sample_period, manifest_id=manifest_resource_response.resource.id)
        self.assertIsNotNone(period_resource_response)
        self.assertIsNotNone(period_resource_response.resource)
        self.assertIsNotNone(period_resource_response.resource.id)
        self._compare_periods(sample_period, period_resource_response.resource)
        
    def test_add_custom_xml_to_period(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.DASH.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)
        sample_period = Period()
        period_resource_response = self.bitmovin.manifests.DASH.add_period(
            object_=sample_period, manifest_id=manifest_resource_response.resource.id)
        self.assertIsNotNone(period_resource_response)
        self.assertIsNotNone(period_resource_response.resource)
        self.assertIsNotNone(period_resource_response.resource.id)
        self._compare_periods(sample_period, period_resource_response.resource)
        custom_xml_element = CustomXMLElement(data='<xml>content goes here</xml>')

        custom_xml_element_response = self.bitmovin.manifests.DASH.add_custom_xml_element_to_period(
            period_id=period_resource_response.resource.id,
            object_=custom_xml_element,
            manifest_id=manifest_resource_response.resource.id
        )
        self.assertIsNotNone(custom_xml_element_response)
        self.assertIsNotNone(custom_xml_element_response.resource)
        self.assertIsNotNone(custom_xml_element_response.resource.id)
        self._compare_custom_xml_elements(first=custom_xml_element, second=custom_xml_element_response.resource)

    def _compare_manifests(self, first: DashManifest, second: DashManifest):
        self.assertEqual(first.manifestName, second.manifestName)
        self.assertEqual(first.description, second.description)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _compare_periods(self, first: Period, second: Period):
        self.assertEqual(first.start, second.start)
        self.assertEqual(first.duration, second.duration)
        return True

    def _get_sample_manifest(self):

        encoding_output = self._get_sample_encoding_output()
        manifest = DashManifest(manifest_name='bitmovin-python_Sample_DASH_Manifest.mpd', outputs=[encoding_output],
                                name='Sample DASH Manifest')

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

    def _compare_custom_xml_elements(self, first: CustomXMLElement, second: CustomXMLElement):
        self.assertEqual(first.data, second.data)


if __name__ == '__main__':
    unittest.main()
