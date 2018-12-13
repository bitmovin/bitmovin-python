import unittest
import uuid

from bitmovin.errors import BitmovinApiError

from bitmovin import Bitmovin, ACLEntry, ACLPermission, EncodingOutput, Period, VideoAdaptationSet, \
    AbstractAdaptationSet, DRMFMP4Representation, Encoding, \
    Stream, StreamInput, MuxingStream, FMP4Muxing, MarlinDRM, AbstractFMP4Representation, HlsManifest, AudioMedia, \
    CustomTag, PositionMode
from tests.bitmovin import BitmovinTestCase


class AudioMediaTests(BitmovinTestCase):
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

    def test_add_audio_media(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_audio_media = self._get_sample_audio_media()
        audio_media_resource_response = self.bitmovin.manifests.HLS.AudioMedia.create(
            object_=sample_audio_media, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(audio_media_resource_response)
        self.assertIsNotNone(audio_media_resource_response.resource)
        self.assertIsNotNone(audio_media_resource_response.resource.id)
        self._compare_audio_medias(sample_audio_media, audio_media_resource_response.resource)

    def test_list_audio_media(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_audio_media = self._get_sample_audio_media()
        audio_media_resource_response = self.bitmovin.manifests.HLS.AudioMedia.create(
            object_=sample_audio_media, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(audio_media_resource_response)
        self.assertIsNotNone(audio_media_resource_response.resource)
        self.assertIsNotNone(audio_media_resource_response.resource.id)
        self._compare_audio_medias(sample_audio_media, audio_media_resource_response.resource)

        manifests_resource_response = self.bitmovin.manifests.HLS.AudioMedia.list(manifest_id=manifest_resource_response.resource.id, limit=1)
        self.assertIsNotNone(manifests_resource_response)
        self.assertTrue(isinstance(manifests_resource_response.resource, list))
        self.assertEqual(1, len(manifests_resource_response.resource))

    def test_retrieve_audio_media(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_audio_media = self._get_sample_audio_media()
        audio_media_resource_response = self.bitmovin.manifests.HLS.AudioMedia.create(
            object_=sample_audio_media, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(audio_media_resource_response)
        self.assertIsNotNone(audio_media_resource_response.resource)
        self.assertIsNotNone(audio_media_resource_response.resource.id)
        self._compare_audio_medias(sample_audio_media, audio_media_resource_response.resource)

        retrieve_manifest_resource_response = self.bitmovin.manifests.HLS.AudioMedia.retrieve(
            manifest_id=manifest_resource_response.resource.id, media_id=audio_media_resource_response.resource.id)

        self.assertIsNotNone(retrieve_manifest_resource_response)
        self.assertTrue(isinstance(retrieve_manifest_resource_response.resource, AudioMedia))
        self._compare_audio_medias(sample_audio_media, retrieve_manifest_resource_response.resource)

    def test_delete_audio_media(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_audio_media = self._get_sample_audio_media()
        audio_media_resource_response = self.bitmovin.manifests.HLS.AudioMedia.create(
            object_=sample_audio_media, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(audio_media_resource_response)
        self.assertIsNotNone(audio_media_resource_response.resource)
        self.assertIsNotNone(audio_media_resource_response.resource.id)
        self._compare_audio_medias(sample_audio_media, audio_media_resource_response.resource)

        delete_sample_audio_media_resource_response = self.bitmovin.manifests.HLS.AudioMedia.delete(
            manifest_id=manifest_resource_response.resource.id, media_id=audio_media_resource_response.resource.id)

        self.assertIsNotNone(delete_sample_audio_media_resource_response)
        self.assertIsNotNone(delete_sample_audio_media_resource_response.resource)
        self.assertIsNotNone(delete_sample_audio_media_resource_response.resource.id)
        self.assertEqual(audio_media_resource_response.resource.id,
                         delete_sample_audio_media_resource_response.resource.id)

    def test_custom_tags(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.HLS.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_audio_media = self._get_sample_audio_media()
        audio_media_resource_response = self.bitmovin.manifests.HLS.AudioMedia.create(
            object_=sample_audio_media, manifest_id=manifest_resource_response.resource.id)

        custom_tag = self._create_sample_custom_tag()

        custom_tag_resource_response = self.bitmovin.manifests.HLS.AudioMedia.CustomTag.create(
            object_=custom_tag, manifest_id=manifest_resource_response.resource.id,
            media_id=audio_media_resource_response.resource.id)

        tags = self.bitmovin.manifests.HLS.AudioMedia.CustomTag.list(
            manifest_id=manifest_resource_response.resource.id,
            media_id=audio_media_resource_response.resource.id)

        custom_tag_retrieve = self.bitmovin.manifests.HLS.AudioMedia.CustomTag.retrieve(
            manifest_id=manifest_resource_response.resource.id,
            media_id=audio_media_resource_response.resource.id,
            custom_tag_id=custom_tag_resource_response.resource.id)

        self.assertIsNotNone(audio_media_resource_response)
        self.assertIsNotNone(audio_media_resource_response.resource)
        self.assertIsNotNone(audio_media_resource_response.resource.id)
        self._compare_audio_medias(sample_audio_media, audio_media_resource_response.resource)
        self._compare_custom_tags(custom_tag, custom_tag_resource_response.resource)
        self._compare_custom_tags(custom_tag_resource_response.resource, custom_tag_retrieve.resource)
        self.assertTrue(len(tags.resource), 1)

        self.bitmovin.manifests.HLS.AudioMedia.CustomTag.delete(
            manifest_id=manifest_resource_response.resource.id,
            media_id=audio_media_resource_response.resource.id,
            custom_tag_id=custom_tag_resource_response.resource.id)

        with self.assertRaises(BitmovinApiError):
            self.bitmovin.manifests.HLS.AudioMedia.CustomTag.retrieve(
                manifest_id=manifest_resource_response.resource.id,
                media_id=audio_media_resource_response.resource.id,
                custom_tag_id=custom_tag_resource_response.resource.id)

    def _compare_manifests(self, first: HlsManifest, second: HlsManifest):
        self.assertEqual(first.manifestName, second.manifestName)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _compare_periods(self, first: Period, second: Period):
        self.assertEqual(first.start, second.start)
        self.assertEqual(first.duration, second.duration)
        return True

    def _compare_adaptationsets(self, first: AbstractAdaptationSet, second: AbstractAdaptationSet):
        return True

    def _compare_video_adaptationsets(self, first: VideoAdaptationSet, second: VideoAdaptationSet):
        self._compare_adaptationsets(first, second)
        return True

    def _compare_fmp4_representations(self, first: AbstractFMP4Representation, second: AbstractFMP4Representation):
        self.assertEqual(first.type, second.type)
        self.assertEqual(first.encodingId, second.encodingId)
        self.assertEqual(first.muxingId, second.muxingId)
        self.assertEqual(first.segmentPath, second.segmentPath)
        self.assertEqual(first.startSegmentNumber, second.startSegmentNumber)
        return True

    def _compare_drm_fmp4_representations(self, first: DRMFMP4Representation, second: DRMFMP4Representation):
        self._compare_fmp4_representations(first, second)
        self.assertEqual(first.drmId, second.drmId)
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

    def _compare_audio_medias(self, first: AudioMedia, second: AudioMedia):
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.groupId, second.groupId)
        self.assertEqual(first.language, second.language)
        self.assertEqual(first.assocLanguage, second.assocLanguage)
        self.assertEqual(first.autoselect, second.autoselect)
        self.assertEqual(first.characteristics, second.characteristics)
        self.assertEqual(first.segmentPath, second.segmentPath)
        self.assertEqual(first.encodingId, second.encodingId)
        self.assertEqual(first.streamId, second.streamId)
        self.assertEqual(first.muxingId, second.muxingId)
        self.assertEqual(first.drmId, second.drmId)
        self.assertEqual(first.startSegmentNumber, second.startSegmentNumber)
        self.assertEqual(first.endSegmentNumber, second.endSegmentNumber)
        self.assertEqual(first.uri, second.uri)

    def _compare_custom_tags(self, first: CustomTag, second: CustomTag):
        self.assertEqual(first.positionMode, second.positionMode)
        self.assertEqual(first.time, second.time)
        self.assertEqual(first.segment, second.segment)
        self.assertEqual(first.data, second.data)

    def _get_sample_manifest(self):
        encoding_output = self._get_sample_encoding_output()
        manifest = HlsManifest(manifest_name='bitmovin-python_Sample_HLS_Manifest.m3u8', outputs=[encoding_output],
                                name='Sample HLS Manifest')

        self.assertIsNotNone(manifest)
        self.assertIsNotNone(manifest.manifestName)
        self.assertIsNotNone(manifest.outputs)
        return manifest

    def _get_sample_audio_media(self):
        encoding_id = self.sampleEncoding.id
        stream_id = self.sampleStream.id
        muxing_id = self.sampleMuxing.id
        drm_id = self.sampleDrm.id

        audio_media = AudioMedia(group_id='audio_group_1', language='en', assoc_language='en', name='Audio Media Test',
                                 is_default=False, autoselect=False, segment_path='/path/to/segs',
                                 encoding_id=encoding_id, stream_id=stream_id, muxing_id=muxing_id, drm_id=drm_id,
                                 start_segment_number=0, uri='myrendition.m3u8')

        return audio_media

    def _get_sample_encoding_output(self):
        acl_entry = ACLEntry(scope='string', permission=ACLPermission.PUBLIC_READ)

        sample_output = self.utils.get_sample_s3_output()
        s3_output = self.bitmovin.outputs.S3.create(sample_output)
        encoding_output = EncodingOutput(output_id=s3_output.resource.id,
                                         output_path='/bitmovin-python/StreamTests/' + str(uuid.uuid4()),
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

    def _create_sample_custom_tag(self):
        custom_tag = CustomTag(position_mode=PositionMode.SEGMENT, segment=1, data="#X-CUSTOM-TAG")

        return custom_tag

if __name__ == '__main__':
    unittest.main()
