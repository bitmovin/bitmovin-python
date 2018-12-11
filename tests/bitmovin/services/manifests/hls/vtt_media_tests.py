import unittest
import uuid
from bitmovin import Bitmovin, ACLEntry, ACLPermission, EncodingOutput, HlsManifest, VttMedia
from tests.bitmovin import BitmovinTestCase


class VttMediaTests(BitmovinTestCase):
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

    def test_add_vtt_media(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_vtt_media = self._get_sample_vtt_media()
        vtt_media_resource_response = self.bitmovin.manifests.HLS.VttMedia.create(
            object_=sample_vtt_media, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(vtt_media_resource_response)
        self.assertIsNotNone(vtt_media_resource_response.resource)
        self.assertIsNotNone(vtt_media_resource_response.resource.id)
        self._compare_vtt_medias(sample_vtt_media, vtt_media_resource_response.resource)

    def test_list_vtt_media(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_vtt_media = self._get_sample_vtt_media()
        vtt_media_resource_response = self.bitmovin.manifests.HLS.VttMedia.create(
            object_=sample_vtt_media, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(vtt_media_resource_response)
        self.assertIsNotNone(vtt_media_resource_response.resource)
        self.assertIsNotNone(vtt_media_resource_response.resource.id)
        self._compare_vtt_medias(sample_vtt_media, vtt_media_resource_response.resource)

        manifests_resource_response = self.bitmovin.manifests.HLS.VttMedia.list(
            manifest_id=manifest_resource_response.resource.id,
            limit=1
        )

        self.assertIsNotNone(manifests_resource_response)
        self.assertTrue(isinstance(manifests_resource_response.resource, list))
        self.assertEqual(1, len(manifests_resource_response.resource))

    def test_retrieve_vtt_media(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_vtt_media = self._get_sample_vtt_media()
        vtt_media_resource_response = self.bitmovin.manifests.HLS.VttMedia.create(
            object_=sample_vtt_media, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(vtt_media_resource_response)
        self.assertIsNotNone(vtt_media_resource_response.resource)
        self.assertIsNotNone(vtt_media_resource_response.resource.id)
        self._compare_vtt_medias(sample_vtt_media, vtt_media_resource_response.resource)

        retrieve_manifest_resource_response = self.bitmovin.manifests.HLS.VttMedia.retrieve(
            manifest_id=manifest_resource_response.resource.id, media_id=vtt_media_resource_response.resource.id)

        self.assertIsNotNone(retrieve_manifest_resource_response)
        self.assertTrue(isinstance(retrieve_manifest_resource_response.resource, VttMedia))
        self._compare_vtt_medias(sample_vtt_media, retrieve_manifest_resource_response.resource)

    def test_delete_vtt_media(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_vtt_media = self._get_sample_vtt_media()
        vtt_media_resource_response = self.bitmovin.manifests.HLS.VttMedia.create(
            object_=sample_vtt_media, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(vtt_media_resource_response)
        self.assertIsNotNone(vtt_media_resource_response.resource)
        self.assertIsNotNone(vtt_media_resource_response.resource.id)
        self._compare_vtt_medias(sample_vtt_media, vtt_media_resource_response.resource)

        delete_sample_vtt_media_resource_response = self.bitmovin.manifests.HLS.VttMedia.delete(
            manifest_id=manifest_resource_response.resource.id, media_id=vtt_media_resource_response.resource.id)

        self.assertIsNotNone(delete_sample_vtt_media_resource_response)
        self.assertIsNotNone(delete_sample_vtt_media_resource_response.resource)
        self.assertIsNotNone(delete_sample_vtt_media_resource_response.resource.id)
        self.assertEqual(vtt_media_resource_response.resource.id,
                         delete_sample_vtt_media_resource_response.resource.id)

    def _compare_manifests(self, first: HlsManifest, second: HlsManifest):
        self.assertEqual(first.manifestName, second.manifestName)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _compare_vtt_medias(self, first: VttMedia, second: VttMedia):
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.groupId, second.groupId)
        self.assertEqual(first.language, second.language)
        self.assertEqual(first.assocLanguage, second.assocLanguage)
        self.assertEqual(first.autoselect, second.autoselect)
        self.assertEqual(first.characteristics, second.characteristics)
        self.assertEqual(first.vttUrl, second.vttUrl)
        self.assertEqual(first.uri, second.uri)

    def _get_sample_manifest(self):
        encoding_output = self._get_sample_encoding_output()
        manifest = HlsManifest(manifest_name='bitmovin-python_Sample_HLS_Manifest.m3u8', outputs=[encoding_output],
                               name='Sample HLS Manifest')

        self.assertIsNotNone(manifest)
        self.assertIsNotNone(manifest.manifestName)
        self.assertIsNotNone(manifest.outputs)
        return manifest

    def _get_sample_vtt_media(self):
        vtt_media = VttMedia(group_id='subs_group_1', language='en', assoc_language='en', name='Subs Media Test',
                             is_default=False, autoselect=False,
                             vtt_url='https://host.com/mysubs.vtt', uri='subtitle_en.m3u8')

        return vtt_media

    def _get_sample_encoding_output(self):
        acl_entry = ACLEntry(scope='string', permission=ACLPermission.PUBLIC_READ)

        sample_output = self.utils.get_sample_s3_output()
        s3_output = self.bitmovin.outputs.S3.create(sample_output)
        encoding_output = EncodingOutput(output_id=s3_output.resource.id,
                                         output_path='/bitmovin-python/StreamTests/' + str(uuid.uuid4()),
                                         acl=[acl_entry])

        return encoding_output


if __name__ == '__main__':
    unittest.main()
