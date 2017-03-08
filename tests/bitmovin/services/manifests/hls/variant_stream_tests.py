import unittest
import uuid
from bitmovin import Bitmovin, ACLEntry, ACLPermission, EncodingOutput, VideoAdaptationSet, \
    AbstractAdaptationSet, Encoding, \
    Stream, StreamInput, MuxingStream, FMP4Muxing, MarlinDRM, HlsManifest, VariantStream
from tests.bitmovin import BitmovinTestCase


class VariantStreamTests(BitmovinTestCase):
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
        self.sampleDrm = self._create_sample_drm()  # type: MarlinDRM

    def tearDown(self):
        super().tearDown()

    def test_add_variant_stream(self):
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
        self._compare_variant_streams(sample_variant_stream, variant_stream_resource_response.resource)

    def test_list_variant_stream(self):
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
        self._compare_variant_streams(sample_variant_stream, variant_stream_resource_response.resource)

        manifests_resource_response = self.bitmovin.manifests.HLS.VariantStream.list(manifest_id=manifest_resource_response.resource.id, limit=1)
        self.assertIsNotNone(manifests_resource_response)
        self.assertTrue(isinstance(manifests_resource_response.resource, list))
        self.assertEqual(1, len(manifests_resource_response.resource))

    def test_retrieve_variant_stream(self):
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
        self._compare_variant_streams(sample_variant_stream, variant_stream_resource_response.resource)

        retrieve_manifest_resource_response = self.bitmovin.manifests.HLS.VariantStream.retrieve(
            manifest_id=manifest_resource_response.resource.id, stream_id=variant_stream_resource_response.resource.id)

        self.assertIsNotNone(retrieve_manifest_resource_response)
        self.assertTrue(isinstance(retrieve_manifest_resource_response.resource, VariantStream))
        self._compare_variant_streams(sample_variant_stream, retrieve_manifest_resource_response.resource)

    def test_delete_variant_stream(self):
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
        self._compare_variant_streams(sample_variant_stream, variant_stream_resource_response.resource)

        delete_sample_variant_stream_resource_response = self.bitmovin.manifests.HLS.VariantStream.delete(
            manifest_id=manifest_resource_response.resource.id, stream_id=variant_stream_resource_response.resource.id)

        self.assertIsNotNone(delete_sample_variant_stream_resource_response)
        self.assertIsNotNone(delete_sample_variant_stream_resource_response.resource)
        self.assertIsNotNone(delete_sample_variant_stream_resource_response.resource.id)
        self.assertEqual(variant_stream_resource_response.resource.id,
                         delete_sample_variant_stream_resource_response.resource.id)

    def _compare_manifests(self, first: HlsManifest, second: HlsManifest):
        self.assertEqual(first.manifestName, second.manifestName)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _compare_adaptationsets(self, first: AbstractAdaptationSet, second: AbstractAdaptationSet):
        return True

    def _compare_video_adaptationsets(self, first: VideoAdaptationSet, second: VideoAdaptationSet):
        self._compare_adaptationsets(first, second)
        return True

    def _compare_encodings(self, first: Encoding, second: Encoding):
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.encoderVersion, second.encoderVersion)
        self.assertEqual(first.cloudRegion, second.cloudRegion)
        return True

    def _compare_muxings(self, first: FMP4Muxing, second: FMP4Muxing):
        self.assertEqual(first.initSegmentName, second.initSegmentName)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.segmentLength, second.segmentLength)
        self.assertEqual(first.segmentNaming, second.segmentNaming)
        self.assertEqual(first.name, second.name)
        self.assertEqual(second.description, second.description)
        return True

    def _compare_drms(self, first: MarlinDRM, second: MarlinDRM):
        self.assertEqual(first.kid, second.kid)
        self.assertEqual(first.key, second.key)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _compare_variant_streams(self, first: VariantStream, second: VariantStream):
        self.assertEqual(first.audio, second.audio)
        self.assertEqual(first.video, second.video)
        self.assertEqual(first.subtitles, second.subtitles)
        self.assertEqual(first.closedCaptions, second.closedCaptions)
        self.assertEqual(first.segmentPath, second.segmentPath)
        self.assertEqual(first.encodingId, second.encodingId)
        self.assertEqual(first.streamId, second.streamId)
        self.assertEqual(first.muxingId, second.muxingId)
        self.assertEqual(first.drmId, second.drmId)
        self.assertEqual(first.startSegmentNumber, second.startSegmentNumber)
        self.assertEqual(first.endSegmentNumber, second.endSegmentNumber)
        self.assertEqual(first.uri, second.uri)

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
        drm_id = self.sampleDrm.id

        variant_stream = VariantStream(audio='audio_grp', video='video_grp', subtitles='subtitles_grp',
                                       closed_captions='NONE', segment_path='/path/to/segs', uri='playlist.m3u8',
                                       encoding_id=encoding_id, stream_id=stream_id, muxing_id=muxing_id, drm_id=drm_id,
                                       start_segment_number=0)

        return variant_stream

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
        self._compare_encodings(sample_encoding, encoding_resource_response.resource)
        return encoding_resource_response.resource

    def _create_sample_muxing(self):
        (sample_muxing, created_stream) = self._get_sample_muxing()
        muxing_resource_response = self.bitmovin.encodings.Muxing.FMP4.create(object_=sample_muxing,
                                                                              encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(muxing_resource_response)
        self.assertIsNotNone(muxing_resource_response.resource)
        self.assertIsNotNone(muxing_resource_response.resource.id)
        self._compare_muxings(sample_muxing, muxing_resource_response.resource)
        return (muxing_resource_response.resource, created_stream)

    def _create_sample_drm(self):
        sample_drm = self._get_sample_drm_marlin()
        drm_resource_response = self.bitmovin.encodings.Muxing.FMP4.DRM.Marlin.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=self.sampleMuxing.id)
        self.assertIsNotNone(drm_resource_response)
        self.assertIsNotNone(drm_resource_response.resource)
        self.assertIsNotNone(drm_resource_response.resource.id)
        self._compare_drms(sample_drm, drm_resource_response.resource)
        return drm_resource_response.resource

    def _get_sample_drm_marlin(self):
        sample_output = self._get_sample_encoding_output()
        sample_output.outputPath += '/drm'
        marlin_drm_settings = self.settings.get('sampleObjects').get('drmConfigurations').get('Marlin')
        drm = MarlinDRM(key=marlin_drm_settings[0].get('key'),
                        kid=marlin_drm_settings[0].get('kid'),
                        outputs=[sample_output],
                        name='Sample Marlin DRM')
        return drm


if __name__ == '__main__':
    unittest.main()
