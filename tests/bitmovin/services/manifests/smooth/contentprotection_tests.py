import unittest
import uuid
from bitmovin import Bitmovin, ACLEntry, ACLPermission, EncodingOutput, Encoding, \
    Stream, StreamInput, MuxingStream, MP4Muxing, SmoothManifest, SmoothContentProtection, PlayReadyDRM
from tests.bitmovin import BitmovinTestCase


class SmoothContentProtectionTests(BitmovinTestCase):
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
        self.sampleEncoding = self._create_sample_encoding()  # type: Encoding
        (self.sampleMuxing, self.sampleStream) = self._create_sample_muxing()  # type: MP4Muxing
        self.sampleDrm = self._create_sample_drm()  # type: PlayReadyDRM

    def tearDown(self):
        super().tearDown()

    def test_add_content_protection(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.Smooth.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_content_protection = self._get_sample_content_protection()
        content_protection_response = self.bitmovin.manifests.Smooth.ContentProtection.create(
            object_=sample_content_protection, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(content_protection_response)
        self.assertIsNotNone(content_protection_response.resource)
        self.assertIsNotNone(content_protection_response.resource.id)
        self._compare_content_protections(sample_content_protection, content_protection_response.resource)

    def test_list_content_protection(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.Smooth.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_content_protection = self._get_sample_content_protection()
        content_protection_response = self.bitmovin.manifests.Smooth.ContentProtection.create(
            object_=sample_content_protection, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(content_protection_response)
        self.assertIsNotNone(content_protection_response.resource)
        self.assertIsNotNone(content_protection_response.resource.id)
        self._compare_content_protections(sample_content_protection, content_protection_response.resource)

        list_content_protection_resource_response = self.bitmovin.manifests.Smooth.ContentProtection.list(
            manifest_id=manifest_resource_response.resource.id, limit=1)

        self.assertIsNotNone(list_content_protection_resource_response)
        self.assertTrue(isinstance(list_content_protection_resource_response.resource, list))
        self.assertEqual(1, len(list_content_protection_resource_response.resource))

    def test_retrieve_content_protection(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.Smooth.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_content_protection = self._get_sample_content_protection()
        content_protection_response = self.bitmovin.manifests.Smooth.ContentProtection.create(
            object_=sample_content_protection, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(content_protection_response)
        self.assertIsNotNone(content_protection_response.resource)
        self.assertIsNotNone(content_protection_response.resource.id)
        self._compare_content_protections(sample_content_protection, content_protection_response.resource)

        retrieve_content_protection_resource_response = self.bitmovin.manifests.Smooth.ContentProtection.retrieve(
            manifest_id=manifest_resource_response.resource.id, protection_id=content_protection_response.resource.id)

        self.assertIsNotNone(retrieve_content_protection_resource_response)
        self.assertTrue(isinstance(retrieve_content_protection_resource_response.resource, SmoothContentProtection))

        self._compare_content_protections(
            sample_content_protection,
            retrieve_content_protection_resource_response.resource
        )

    def test_delete_content_protection(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.Smooth.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_content_protection = self._get_sample_content_protection()
        content_protection_response = self.bitmovin.manifests.Smooth.ContentProtection.create(
            object_=sample_content_protection, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(content_protection_response)
        self.assertIsNotNone(content_protection_response.resource)
        self.assertIsNotNone(content_protection_response.resource.id)
        self._compare_content_protections(sample_content_protection, content_protection_response.resource)

        delete_content_protection_resource_response = self.bitmovin.manifests.Smooth.ContentProtection.delete(
            manifest_id=manifest_resource_response.resource.id, protection_id=content_protection_response.resource.id)

        self.assertIsNotNone(delete_content_protection_resource_response)
        self.assertIsNotNone(delete_content_protection_resource_response.resource)
        self.assertIsNotNone(delete_content_protection_resource_response.resource.id)
        self.assertEqual(content_protection_response.resource.id, delete_content_protection_resource_response.resource.id)

    def _compare_manifests(self, first: SmoothManifest, second: SmoothManifest):
        self.assertEqual(first.serverManifestName, second.serverManifestName)
        self.assertEqual(first.clientManifestName, second.clientManifestName)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _compare_encodings(self, first: Encoding, second: Encoding):
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.encoderVersion, second.encoderVersion)
        self.assertEqual(first.cloudRegion, second.cloudRegion)
        return True

    def _compare_muxings(self, first: MP4Muxing, second: MP4Muxing):
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.fragmentDuration, second.fragmentDuration)
        self.assertEqual(first.filename, second.filename)
        self.assertEqual(first.name, second.name)
        self.assertEqual(second.description, second.description)
        return True

    def _compare_content_protections(self, first: SmoothContentProtection, second: SmoothContentProtection):
        self.assertEqual(first.encodingId, second.encodingId)
        self.assertEqual(first.muxingId, second.muxingId)
        self.assertEqual(first.drmId, second.drmId)
        return True

    def _compare_drms(self, first: PlayReadyDRM, second: PlayReadyDRM):
        self.assertEqual(first.kid, second.kid)
        self.assertEqual(first.keySeed, second.keySeed)
        self.assertEqual(first.method, second.method)
        self.assertEqual(first.laUrl, second.laUrl)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _get_sample_manifest(self):
        encoding_output = self._get_sample_encoding_output()
        manifest = SmoothManifest(server_manifest_name='bitmovin-python_Sample_Smooth_Manifest.ism',
                                  client_manifest_name='bitmovin-python_Sample_Smooth_Manifest.ismc',
                                  outputs=[encoding_output],
                                  name='Sample Smooth Manifest')

        self.assertIsNotNone(manifest)
        self.assertIsNotNone(manifest.serverManifestName)
        self.assertIsNotNone(manifest.clientManifestName)
        self.assertIsNotNone(manifest.outputs)
        return manifest

    def _get_sample_content_protection(self):
        encoding_id = self.sampleEncoding.id
        muxing_id = self.sampleMuxing.id
        drm_id = self.sampleDrm.id

        content_protection = SmoothContentProtection(encoding_id=encoding_id,
                                                     muxing_id=muxing_id,
                                                     drm_id=drm_id)
        return content_protection

    def _get_sample_encoding_output(self):
        acl_entry = ACLEntry(scope='string', permission=ACLPermission.PUBLIC_READ)

        sample_output = self.utils.get_sample_s3_output()
        s3_output = self.bitmovin.outputs.S3.create(sample_output)
        encoding_output = EncodingOutput(output_id=s3_output.resource.id,
                                         output_path='/bitmovin-python/StreamTests/' + str(uuid.uuid4()),
                                         acl=[acl_entry])

        return encoding_output

    def _get_sample_muxing(self):
        stream = self._get_sample_stream()

        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)

        muxing_stream = MuxingStream(stream_id=create_stream_response.resource.id)

        muxing = MP4Muxing(streams=[muxing_stream],
                           filename="myrendition.ismv",
                           fragment_duration=4000,
                           outputs=stream.outputs,
                           name='Sample MP4 Muxing')

        return muxing, create_stream_response.resource

    def _get_sample_stream(self):
        sample_codec_configuration = self.utils.get_sample_h264_codec_configuration()
        h264_codec_configuration = self.bitmovin.codecConfigurations.H264.create(sample_codec_configuration)

        (sample_input, sample_files) = self.utils.get_sample_s3_input()
        s3_input = self.bitmovin.inputs.S3.create(sample_input)
        stream_input = StreamInput(input_id=s3_input.resource.id,
                                   input_path=sample_files.get('854b9c98-17b9-49ed-b75c-3b912730bfd1'),
                                   selection_mode='AUTO')

        acl_entry = ACLEntry(scope='string', permission=ACLPermission.PUBLIC_READ)

        sample_output = self.utils.get_sample_s3_output()
        s3_output = self.bitmovin.outputs.S3.create(sample_output)
        encoding_output = EncodingOutput(output_id=s3_output.resource.id,
                                         output_path='/bitmovin-python/StreamTests/'+str(uuid.uuid4()),
                                         acl=[acl_entry])

        stream = Stream(codec_configuration_id=h264_codec_configuration.resource.id,
                        input_streams=[stream_input],
                        outputs=[encoding_output],
                        name='Sample Stream')

        self.assertIsNotNone(stream.codecConfigId)
        self.assertIsNotNone(stream.inputStreams)
        self.assertIsNotNone(stream.outputs)

        return stream

    def _create_sample_encoding(self):
        sample_encoding = self.utils.get_sample_encoding()
        encoding_resource_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        self.assertIsNotNone(encoding_resource_response)
        self.assertIsNotNone(encoding_resource_response.resource)
        self.assertIsNotNone(encoding_resource_response.resource.id)
        self._compare_encodings(sample_encoding, encoding_resource_response.resource)
        return encoding_resource_response.resource

    def _create_sample_muxing(self):
        (sample_muxing, created_stream) = self._get_sample_muxing()
        muxing_resource_response = self.bitmovin.encodings.Muxing.MP4.create(object_=sample_muxing,
                                                                             encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(muxing_resource_response)
        self.assertIsNotNone(muxing_resource_response.resource)
        self.assertIsNotNone(muxing_resource_response.resource.id)
        self._compare_muxings(sample_muxing, muxing_resource_response.resource)
        return muxing_resource_response.resource, created_stream

    def _create_sample_drm(self):
        sample_drm = self._get_sample_drm_playready()
        drm_resource_response = self.bitmovin.encodings.Muxing.MP4.DRM.PlayReady.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=self.sampleMuxing.id)
        self.assertIsNotNone(drm_resource_response)
        self.assertIsNotNone(drm_resource_response.resource)
        self.assertIsNotNone(drm_resource_response.resource.id)
        self._compare_drms(sample_drm, drm_resource_response.resource)
        return drm_resource_response.resource

    def _get_sample_drm_playready(self):
        sample_output = self._get_sample_encoding_output()
        sample_output.outputPath += '/drm'

        playready_drm_settings = self.settings.get('sampleObjects').get('drmConfigurations').get('PlayReady')

        drm = PlayReadyDRM(key_seed=playready_drm_settings[0].get('keySeed'),
                           kid=playready_drm_settings[0].get('kid'),
                           method=playready_drm_settings[0].get('method'),
                           la_url=playready_drm_settings[0].get('laUrl'),
                           name='Sample PlayReady DRM',
                           outputs=[sample_output])
        return drm


if __name__ == '__main__':
    unittest.main()
