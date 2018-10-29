import unittest
import uuid
from bitmovin import Bitmovin, Response, DashManifest, ACLEntry, ACLPermission, EncodingOutput, \
    DashManifestProfile, DASHNamespace
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class DashManifestTests(BitmovinTestCase):

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

    def test_create_manifest(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.DASH.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

    def test_create_manifest_without_name(self):
        sample_manifest = self._get_sample_manifest()
        sample_manifest.name = None
        manifest_resource_response = self.bitmovin.manifests.DASH.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

    def test_create_manifest_live(self):
        sample_manifest = self._get_sample_manifest()
        sample_manifest.profile = DashManifestProfile.LIVE
        manifest_resource_response = self.bitmovin.manifests.DASH.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)
        self.assertEqual(sample_manifest.profile, manifest_resource_response.resource.profile)
        
    def test_create_manifest_ondemand(self):
        sample_manifest = self._get_sample_manifest()
        sample_manifest.profile = DashManifestProfile.ON_DEMAND
        manifest_resource_response = self.bitmovin.manifests.DASH.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)
        self.assertEqual(sample_manifest.profile, manifest_resource_response.resource.profile)
        
    def test_create_manifest_custom_namespace(self):
        sample_manifest = self._get_sample_manifest()
        custom_namespace = DASHNamespace(prefix='scte35', uri='urn:scte:scte35:2014:xml+bin')
        sample_manifest.namespaces = [custom_namespace]
        manifest_resource_response = self.bitmovin.manifests.DASH.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)
        self.assertEqual(len(sample_manifest.namespaces), len(manifest_resource_response.resource.namespaces))
        self._compare_namespaces(first=custom_namespace, second=manifest_resource_response.response.namespaces[0])

    def test_retrieve_manifest(self):
        sample_manifest = self._get_sample_manifest()
        created_manifest_response = self.bitmovin.manifests.DASH.create(sample_manifest)
        self.assertIsNotNone(created_manifest_response)
        self.assertIsNotNone(created_manifest_response.resource)
        self.assertIsNotNone(created_manifest_response.resource.id)
        self._compare_manifests(sample_manifest, created_manifest_response.resource)

        retrieved_manifest_response = self.bitmovin.manifests.DASH.retrieve(created_manifest_response.resource.id)
        self.assertIsNotNone(retrieved_manifest_response)
        self.assertIsNotNone(retrieved_manifest_response.resource)
        self._compare_manifests(created_manifest_response.resource, retrieved_manifest_response.resource)

    def test_delete_manifest(self):
        sample_manifest = self._get_sample_manifest()
        created_manifest_response = self.bitmovin.manifests.DASH.create(sample_manifest)
        self.assertIsNotNone(created_manifest_response)
        self.assertIsNotNone(created_manifest_response.resource)
        self.assertIsNotNone(created_manifest_response.resource.id)
        self._compare_manifests(sample_manifest, created_manifest_response.resource)

        deleted_minimal_resource = self.bitmovin.manifests.DASH.delete(created_manifest_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.manifests.DASH.retrieve(created_manifest_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving manifest after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_manifests(self):
        sample_manifest = self._get_sample_manifest()
        created_manifest_response = self.bitmovin.manifests.DASH.create(sample_manifest)
        self.assertIsNotNone(created_manifest_response)
        self.assertIsNotNone(created_manifest_response.resource)
        self.assertIsNotNone(created_manifest_response.resource.id)
        self._compare_manifests(sample_manifest, created_manifest_response.resource)

        manifests = self.bitmovin.manifests.DASH.list()
        self.assertIsNotNone(manifests)
        self.assertIsNotNone(manifests.resource)
        self.assertIsNotNone(manifests.response)
        self.assertIsInstance(manifests.resource, list)
        self.assertIsInstance(manifests.response, Response)
        self.assertGreater(manifests.resource.__sizeof__(), 1)

    def _compare_manifests(self, first: DashManifest, second: DashManifest):
        """

        :param first: Manifest
        :param second: Manifest
        :return: bool
        """
        self.assertEqual(first.manifestName, second.manifestName)
        self.assertEqual(first.description, second.description)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.profile, second.profile)

        return True

    def _compare_namespaces(self, first: DASHNamespace, second: DASHNamespace):
        """

        :param first: DASHNamespace
        :param second: DASHNamespace
        :return: bool
        """
        self.assertEqual(first.prefix, second.prefix)
        self.assertEqual(first.uri, second.uri)

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


if __name__ == '__main__':
    unittest.main()
