import unittest
import uuid
from bitmovin import Bitmovin, DashManifest, ACLEntry, ACLPermission, EncodingOutput, Period, VideoAdaptationSet, \
    AbstractAdaptationSet, FMP4Representation, FMP4RepresentationType, DRMFMP4Representation, Encoding, \
    Stream, StreamInput, MuxingStream, FMP4Muxing, MarlinDRM, AbstractFMP4Representation, WebMRepresentation, \
    WebMRepresentationType, DashMP4Representation, SubtitleAdaptationSet, VttRepresentation
from tests.bitmovin import BitmovinTestCase


class RepresentationTests(BitmovinTestCase):
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
        self.sampleMuxing = self._create_sample_muxing()  # type: FMP4Muxing
        self.sampleDrm = self._create_sample_drm()  # type: MarlinDRM

    def tearDown(self):
        super().tearDown()

    def test_add_fmp4_representation(self):
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
        sample_adaptationset = self._get_sample_adaptationset()
        adaptationset_resource_response = self.bitmovin.manifests.DASH.add_video_adaptation_set(
            object_=sample_adaptationset, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id
        )
        self.assertIsNotNone(adaptationset_resource_response)
        self.assertIsNotNone(adaptationset_resource_response.resource)
        self.assertIsNotNone(adaptationset_resource_response.resource.id)
        self._compare_video_adaptationsets(sample_adaptationset, adaptationset_resource_response.resource)
        sample_representation = self._get_sample_fmp4_representation()
        representation_resource_response = self.bitmovin.manifests.DASH.add_fmp4_representation(
            object_=sample_representation, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id, adaptationset_id=adaptationset_resource_response.resource.id
        )
        self.assertIsNotNone(representation_resource_response)
        self.assertIsNotNone(representation_resource_response.resource)
        self.assertIsNotNone(representation_resource_response.resource.id)
        self._compare_fmp4_representations(sample_representation, representation_resource_response.resource)

    def test_add_fmp4_representation_with_keyframes(self):
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
        sample_adaptationset = self._get_sample_adaptationset()
        adaptationset_resource_response = self.bitmovin.manifests.DASH.add_video_adaptation_set(
            object_=sample_adaptationset, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id
        )
        self.assertIsNotNone(adaptationset_resource_response)
        self.assertIsNotNone(adaptationset_resource_response.resource)
        self.assertIsNotNone(adaptationset_resource_response.resource.id)
        self._compare_video_adaptationsets(sample_adaptationset, adaptationset_resource_response.resource)
        sample_representation = self._get_sample_fmp4_representation_with_keyframes()
        representation_resource_response = self.bitmovin.manifests.DASH.add_fmp4_representation(
            object_=sample_representation, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id, adaptationset_id=adaptationset_resource_response.resource.id
        )
        self.assertIsNotNone(representation_resource_response)
        self.assertIsNotNone(representation_resource_response.resource)
        self.assertIsNotNone(representation_resource_response.resource.id)
        self._compare_fmp4_representations(sample_representation, representation_resource_response.resource)

    def test_add_drm_fmp4_representation(self):
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
        sample_adaptationset = self._get_sample_adaptationset()
        adaptationset_resource_response = self.bitmovin.manifests.DASH.add_video_adaptation_set(
            object_=sample_adaptationset, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id
        )
        self.assertIsNotNone(adaptationset_resource_response)
        self.assertIsNotNone(adaptationset_resource_response.resource)
        self.assertIsNotNone(adaptationset_resource_response.resource.id)
        self._compare_video_adaptationsets(sample_adaptationset, adaptationset_resource_response.resource)
        sample_representation = self._get_sample_drm_fmp4_representation()
        representation_resource_response = self.bitmovin.manifests.DASH.add_drm_fmp4_representation(
            object_=sample_representation, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id, adaptationset_id=adaptationset_resource_response.resource.id
        )
        self.assertIsNotNone(representation_resource_response)
        self.assertIsNotNone(representation_resource_response.resource)
        self.assertIsNotNone(representation_resource_response.resource.id)
        self._compare_drm_fmp4_representations(sample_representation, representation_resource_response.resource)

    def test_add_webm_representation(self):
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
        sample_adaptationset = self._get_sample_adaptationset()
        adaptationset_resource_response = self.bitmovin.manifests.DASH.add_video_adaptation_set(
            object_=sample_adaptationset, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id
        )
        self.assertIsNotNone(adaptationset_resource_response)
        self.assertIsNotNone(adaptationset_resource_response.resource)
        self.assertIsNotNone(adaptationset_resource_response.resource.id)
        self._compare_video_adaptationsets(sample_adaptationset, adaptationset_resource_response.resource)
        sample_representation = self._get_sample_webm_representation()
        representation_resource_response = self.bitmovin.manifests.DASH.add_webm_representation(
            object_=sample_representation, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id, adaptationset_id=adaptationset_resource_response.resource.id
        )
        self.assertIsNotNone(representation_resource_response)
        self.assertIsNotNone(representation_resource_response.resource)
        self.assertIsNotNone(representation_resource_response.resource.id)
        self._compare_webm_representations(sample_representation, representation_resource_response.resource)

    def test_add_mp4_representation(self):
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
        sample_adaptationset = self._get_sample_adaptationset()
        adaptationset_resource_response = self.bitmovin.manifests.DASH.add_video_adaptation_set(
            object_=sample_adaptationset, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id
        )
        self.assertIsNotNone(adaptationset_resource_response)
        self.assertIsNotNone(adaptationset_resource_response.resource)
        self.assertIsNotNone(adaptationset_resource_response.resource.id)
        self._compare_video_adaptationsets(sample_adaptationset, adaptationset_resource_response.resource)
        sample_representation = self._get_sample_mp4_representation()
        representation_resource_response = self.bitmovin.manifests.DASH.add_mp4_representation(
            object_=sample_representation, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id, adaptationset_id=adaptationset_resource_response.resource.id
        )
        self.assertIsNotNone(representation_resource_response)
        self.assertIsNotNone(representation_resource_response.resource)
        self.assertIsNotNone(representation_resource_response.resource.id)
        self._compare_mp4_representations(sample_representation, representation_resource_response.resource)

    def test_add_vtt_representation(self):
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
        sample_adaptationset = self._get_sample_subtitle_adaptationset()
        adaptationset_resource_response = self.bitmovin.manifests.DASH.add_subtitle_adaptation_set(
            object_=sample_adaptationset, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id
        )
        self.assertIsNotNone(adaptationset_resource_response)
        self.assertIsNotNone(adaptationset_resource_response.resource)
        self.assertIsNotNone(adaptationset_resource_response.resource.id)
        self._compare_subtitle_adaptationsets(sample_adaptationset, adaptationset_resource_response.resource)
        sample_representation = self._get_sample_vtt_representation()
        representation_resource_response = self.bitmovin.manifests.DASH.add_vtt_representation(
            object_=sample_representation, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id, adaptationset_id=adaptationset_resource_response.resource.id
        )
        self.assertIsNotNone(representation_resource_response)
        self.assertIsNotNone(representation_resource_response.resource)
        self.assertIsNotNone(representation_resource_response.resource.id)
        self._compare_vtt_representations(sample_representation, representation_resource_response.resource)

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

    def _compare_adaptationsets(self, first: AbstractAdaptationSet, second: AbstractAdaptationSet):
        return True

    def _compare_video_adaptationsets(self, first: VideoAdaptationSet, second: VideoAdaptationSet):
        self._compare_adaptationsets(first, second)
        return True

    def _compare_subtitle_adaptationsets(self, first: SubtitleAdaptationSet, second: SubtitleAdaptationSet):
        self._compare_adaptationsets(first, second)
        return True

    def _compare_fmp4_representations(self, first: AbstractFMP4Representation, second: AbstractFMP4Representation):
        self.assertEqual(first.type, second.type)
        self.assertEqual(first.encodingId, second.encodingId)
        self.assertEqual(first.muxingId, second.muxingId)
        self.assertEqual(first.segmentPath, second.segmentPath)
        self.assertEqual(first.startSegmentNumber, second.startSegmentNumber)
        self.assertEqual(first.endSegmentNumber, second.endSegmentNumber)
        self.assertEqual(first.startKeyframeId, second.startKeyframeId)
        self.assertEqual(first.endKeyframeId, second.endKeyframeId)
        return True

    def _compare_drm_fmp4_representations(self, first: DRMFMP4Representation, second: DRMFMP4Representation):
        self._compare_fmp4_representations(first, second)
        self.assertEqual(first.drmId, second.drmId)
        return True

    def _compare_webm_representations(self, first: WebMRepresentation, second: WebMRepresentation):
        self.assertEqual(first.type, second.type)
        self.assertEqual(first.encodingId, second.encodingId)
        self.assertEqual(first.muxingId, second.muxingId)
        self.assertEqual(first.segmentPath, second.segmentPath)
        self.assertEqual(first.startSegmentNumber, second.startSegmentNumber)
        return True

    def _compare_vtt_representations(self, first: VttRepresentation, second: VttRepresentation):
        self.assertEqual(first.vttUrl, second.vttUrl)
        return True
    
    def _compare_mp4_representations(self, first: DashMP4Representation, second: DashMP4Representation):
        self.assertEqual(first.encodingId, second.encodingId)
        self.assertEqual(first.muxingId, second.muxingId)
        self.assertEqual(first.filePath, second.filePath)
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

    def _get_sample_adaptationset(self):
        video_adaptationset = VideoAdaptationSet()
        return video_adaptationset

    def _get_sample_subtitle_adaptationset(self):
        subtitle_adaptationset = SubtitleAdaptationSet(lang='eng')
        return subtitle_adaptationset

    def _get_sample_fmp4_representation(self):
        encoding_id = self.sampleEncoding.id
        muxing_id = self.sampleMuxing.id
        fmp4_representation = FMP4Representation(type=FMP4RepresentationType.TEMPLATE,
                                                 encoding_id=encoding_id,
                                                 muxing_id=muxing_id,
                                                 segment_path='/path/to/segments/',
                                                 start_segment_number=1,
                                                 end_segment_number=2)

        return fmp4_representation

    def _get_sample_fmp4_representation_with_keyframes(self):
        encoding_id = self.sampleEncoding.id
        muxing_id = self.sampleMuxing.id
        fmp4_representation = FMP4Representation(type=FMP4RepresentationType.TEMPLATE,
                                                 encoding_id=encoding_id,
                                                 muxing_id=muxing_id,
                                                 segment_path='/path/to/segments/',
                                                 start_keyframe_id='345678987654345678',
                                                 end_keyframe_id='3453453454')

        return fmp4_representation


    def _get_sample_drm_fmp4_representation(self):
        encoding_id = self.sampleEncoding.id
        muxing_id = self.sampleMuxing.id
        drm_id = self.sampleDrm.id
        fmp4_representation = DRMFMP4Representation(type=FMP4RepresentationType.TEMPLATE,
                                                    encoding_id=encoding_id,
                                                    muxing_id=muxing_id,
                                                    segment_path='/path/to/segments/',
                                                    start_segment_number=1,
                                                    end_segment_number=2,
                                                    drm_id=drm_id)

        return fmp4_representation

    def _get_sample_webm_representation(self):
        encoding_id = self.sampleEncoding.id
        muxing_id = self.sampleMuxing.id
        webm_representation = WebMRepresentation(type=WebMRepresentationType.TEMPLATE,
                                                 encoding_id=encoding_id,
                                                 muxing_id=muxing_id,
                                                 segment_path='/path/to/segments/',
                                                 start_segment_number=1)

        return webm_representation
    
    def _get_sample_mp4_representation(self):
        encoding_id = self.sampleEncoding.id
        muxing_id = self.sampleMuxing.id
        mp4_representation = DashMP4Representation(encoding_id=encoding_id,
                                                   muxing_id=muxing_id,
                                                   file_path='/path/to/file.mp4')

        return mp4_representation

    def _get_sample_vtt_representation(self):
        webm_representation = VttRepresentation(vtt_url='https://yourhost.com/path/mysubtitles.vtt')

        return webm_representation

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
        return muxing

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
        sample_muxing = self._get_sample_muxing()
        muxing_resource_response = self.bitmovin.encodings.Muxing.FMP4.create(object_=sample_muxing,
                                                                              encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(muxing_resource_response)
        self.assertIsNotNone(muxing_resource_response.resource)
        self.assertIsNotNone(muxing_resource_response.resource.id)
        self._compare_muxings(sample_muxing, muxing_resource_response.resource)
        return muxing_resource_response.resource

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
