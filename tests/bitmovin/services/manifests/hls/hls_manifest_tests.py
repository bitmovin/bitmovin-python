import unittest
import uuid
from bitmovin import Bitmovin, Response, ACLEntry, ACLPermission, EncodingOutput, HlsManifest, MuxingStream, FMP4Muxing, \
    StreamInput, Stream, VariantStream, HlsVersion
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class HlsManifestTests(BitmovinTestCase):

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
        (self.sampleMuxing, self.sampleStream) = self._create_sample_muxing()  # type: FMP4Muxing

    def tearDown(self):
        super().tearDown()

    def test_create_manifest(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

    def test_create_manifest_without_name(self):
        sample_manifest = self._get_sample_manifest()
        sample_manifest.name = None
        manifest_resource_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

    def test_create_manifest_custom_versions(self):
        sample_manifest = self._get_sample_manifest()
        sample_manifest.hlsMediaPlaylistVersion = HlsVersion.HLS_VERSION_7
        sample_manifest.hlsMasterPlaylistVersion = HlsVersion.HLS_VERSION_7
        manifest_resource_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

    def test_retrieve_manifest(self):
        sample_manifest = self._get_sample_manifest()
        created_manifest_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(created_manifest_response)
        self.assertIsNotNone(created_manifest_response.resource)
        self.assertIsNotNone(created_manifest_response.resource.id)
        self._compare_manifests(sample_manifest, created_manifest_response.resource)

        retrieved_manifest_response = self.bitmovin.manifests.HLS.retrieve(created_manifest_response.resource.id)
        self.assertIsNotNone(retrieved_manifest_response)
        self.assertIsNotNone(retrieved_manifest_response.resource)
        self._compare_manifests(created_manifest_response.resource, retrieved_manifest_response.resource)

    def test_delete_manifest(self):
        sample_manifest = self._get_sample_manifest()
        created_manifest_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(created_manifest_response)
        self.assertIsNotNone(created_manifest_response.resource)
        self.assertIsNotNone(created_manifest_response.resource.id)
        self._compare_manifests(sample_manifest, created_manifest_response.resource)

        deleted_minimal_resource = self.bitmovin.manifests.HLS.delete(created_manifest_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.manifests.HLS.retrieve(created_manifest_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving manifest after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_manifests(self):
        sample_manifest = self._get_sample_manifest()
        created_manifest_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(created_manifest_response)
        self.assertIsNotNone(created_manifest_response.resource)
        self.assertIsNotNone(created_manifest_response.resource.id)
        self._compare_manifests(sample_manifest, created_manifest_response.resource)

        manifests = self.bitmovin.manifests.HLS.list()
        self.assertIsNotNone(manifests)
        self.assertIsNotNone(manifests.resource)
        self.assertIsNotNone(manifests.response)
        self.assertIsInstance(manifests.resource, list)
        self.assertIsInstance(manifests.response, Response)
        self.assertGreater(manifests.resource.__sizeof__(), 1)

    def test_list_manifests_by_encoding_id(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_variant_stream = self._get_sample_variant_stream()
        variant_stream_resource_response = self.bitmovin.manifests.HLS.VariantStream.create(
            object_=sample_variant_stream, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(variant_stream_resource_response)
        self.assertIsNotNone(variant_stream_resource_response.resource)
        self.assertIsNotNone(variant_stream_resource_response.resource.id)

        manifests = self.bitmovin.manifests.HLS.filter_by_encoding_id(encoding_id=self.sampleEncoding.id)

        self.assertIsNotNone(manifests)
        self.assertIsNotNone(manifests.resource)
        self.assertIsNotNone(manifests.response)
        self.assertIsInstance(manifests.resource, list)
        self.assertIsInstance(manifests.response, Response)
        self.assertEqual(manifests.resource[0].id, manifest_resource_response.resource.id)
        self.assertEqual(len(manifests.resource), 1)

    def _compare_manifests(self, first: HlsManifest, second: HlsManifest):
        self.assertEqual(first.manifestName, second.manifestName)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.hlsMediaPlaylistVersion, second.hlsMediaPlaylistVersion)
        self.assertEqual(first.hlsMasterPlaylistVersion, second.hlsMasterPlaylistVersion)
        return True

    def _get_sample_manifest(self):

        encoding_output = self._get_sample_encoding_output()
        manifest = HlsManifest(manifest_name='bitmovin-python_Sample_HLS_Manifest.m3u8', outputs=[encoding_output],
                               name='Sample HLS Manifest')

        self.assertIsNotNone(manifest)
        self.assertIsNotNone(manifest.manifestName)
        self.assertIsNotNone(manifest.outputs)
        return manifest

    def _get_sample_variant_stream(self):
        encoding_id = self.sampleEncoding.id
        stream_id = self.sampleStream.id
        muxing_id = self.sampleMuxing.id

        variant_stream = VariantStream(audio='audio_grp', video='video_grp', subtitles='subtitles_grp',
                                       closed_captions='NONE', segment_path='/path/to/segs', uri='playlist.m3u8',
                                       encoding_id=encoding_id, stream_id=stream_id, muxing_id=muxing_id,
                                       start_segment_number=0)

        return variant_stream

    def _get_sample_encoding_output(self):
        acl_entry = ACLEntry(scope='string', permission=ACLPermission.PUBLIC_READ)

        sample_output = self.utils.get_sample_s3_output()
        s3_output = self.bitmovin.outputs.S3.create(sample_output)
        encoding_output = EncodingOutput(output_id=s3_output.resource.id,
                                         output_path='/bitmovin-python/StreamTests/'+str(uuid.uuid4()),
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

        muxing = FMP4Muxing(streams=[muxing_stream],
                            segment_length=4,
                            segment_naming='seg_%number%.m4s',
                            init_segment_name='init.mp4',
                            outputs=stream.outputs,
                            name='Sample FMP4 Muxing')
        return (muxing, create_stream_response.resource)

    def _get_sample_stream(self):
        sample_codec_configuration = self.utils.get_sample_h264_codec_configuration()
        h264_codec_configuration = self.bitmovin.codecConfigurations.H264.create(sample_codec_configuration)

        (sample_input, sample_files) = self.utils.get_sample_s3_input()
        s3_input = self.bitmovin.inputs.S3.create(sample_input)
        stream_input = StreamInput(input_id=s3_input.resource.id, input_path=sample_files.get('854b9c98-17b9-49ed-b75c-3b912730bfd1'), selection_mode='AUTO')

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
        return encoding_resource_response.resource

    def _create_sample_muxing(self):
        (sample_muxing, created_stream) = self._get_sample_muxing()
        muxing_resource_response = self.bitmovin.encodings.Muxing.FMP4.create(object_=sample_muxing,
                                                                              encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(muxing_resource_response)
        self.assertIsNotNone(muxing_resource_response.resource)
        self.assertIsNotNone(muxing_resource_response.resource.id)
        return (muxing_resource_response.resource, created_stream)


if __name__ == '__main__':
    unittest.main()
