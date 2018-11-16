import unittest
import uuid
from bitmovin import Bitmovin, Response, DashManifest, ACLEntry, ACLPermission, EncodingOutput, \
    DashManifestProfile, DASHNamespace, Stream, StreamInput, FMP4Muxing, MuxingStream, DashMP4Representation, Period, \
    VideoAdaptationSet
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
        self.sampleEncoding = self._create_sample_encoding()  # type: Encoding
        self.sampleMuxing = self._create_sample_muxing()  # type: FMP4Muxing

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
        self._compare_namespaces(first=custom_namespace, second=manifest_resource_response.resource.namespaces[0])

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

    def test_list_manifests_by_encoding_id(self):
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
        sample_adaptationset = self._get_sample_adaptationset()
        adaptationset_resource_response = self.bitmovin.manifests.DASH.add_video_adaptation_set(
            object_=sample_adaptationset, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id
        )
        self.assertIsNotNone(adaptationset_resource_response)
        self.assertIsNotNone(adaptationset_resource_response.resource)
        self.assertIsNotNone(adaptationset_resource_response.resource.id)
        sample_representation = self._get_sample_mp4_representation()
        representation_resource_response = self.bitmovin.manifests.DASH.add_mp4_representation(
            object_=sample_representation, manifest_id=manifest_resource_response.resource.id,
            period_id=period_resource_response.resource.id, adaptationset_id=adaptationset_resource_response.resource.id
        )

        manifests = self.bitmovin.manifests.DASH.filter_by_encoding_id(encoding_id=self.sampleEncoding.id)

        self.assertIsNotNone(manifests)
        self.assertIsNotNone(manifests.resource)
        self.assertIsNotNone(manifests.response)
        self.assertIsInstance(manifests.resource, list)
        self.assertIsInstance(manifests.response, Response)
        self.assertEqual(manifests.resource[0].id, manifest_resource_response.resource.id)
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

        if first.profile is not None:
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

    def _get_sample_period_default(self):
        period = Period()
        return period

    def _get_sample_adaptationset(self):
        video_adaptationset = VideoAdaptationSet()
        return video_adaptationset

    def _get_sample_mp4_representation(self):
        encoding_id = self.sampleEncoding.id
        muxing_id = self.sampleMuxing.id
        mp4_representation = DashMP4Representation(encoding_id=encoding_id,
                                                   muxing_id=muxing_id,
                                                   file_path='/path/to/file.mp4')

        return mp4_representation

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
        return encoding_resource_response.resource

    def _create_sample_muxing(self):
        sample_muxing = self._get_sample_muxing()
        muxing_resource_response = self.bitmovin.encodings.Muxing.FMP4.create(object_=sample_muxing,
                                                                              encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(muxing_resource_response)
        self.assertIsNotNone(muxing_resource_response.resource)
        self.assertIsNotNone(muxing_resource_response.resource.id)
        return muxing_resource_response.resource


if __name__ == '__main__':
    unittest.main()
