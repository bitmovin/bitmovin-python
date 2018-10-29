import unittest
import uuid
from bitmovin import Bitmovin, ACLEntry, ACLPermission, EncodingOutput, Encoding, \
    Stream, StreamInput, MuxingStream, MP4Muxing, AbstractMP4Representation, SmoothManifest, MP4Representation
from tests.bitmovin import BitmovinTestCase


class MP4RepresentationTests(BitmovinTestCase):
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

    def tearDown(self):
        super().tearDown()

    def test_add_mp4_representation(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.Smooth.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_mp4_representation = self._get_sample_mp4_representation()
        mp4_representation_response = self.bitmovin.manifests.Smooth.MP4Representation.create(
            object_=sample_mp4_representation, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(mp4_representation_response)
        self.assertIsNotNone(mp4_representation_response.resource)
        self.assertIsNotNone(mp4_representation_response.resource.id)
        self._compare_mp4_representations(sample_mp4_representation, mp4_representation_response.resource)

    def test_list_mp4_representation(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.Smooth.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_mp4_representation = self._get_sample_mp4_representation()
        mp4_representation_response = self.bitmovin.manifests.Smooth.MP4Representation.create(
            object_=sample_mp4_representation, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(mp4_representation_response)
        self.assertIsNotNone(mp4_representation_response.resource)
        self.assertIsNotNone(mp4_representation_response.resource.id)
        self._compare_mp4_representations(sample_mp4_representation, mp4_representation_response.resource)

        list_representation_resource_response = self.bitmovin.manifests.Smooth.MP4Representation.list(
            manifest_id=manifest_resource_response.resource.id,
            limit=1
        )
        self.assertIsNotNone(list_representation_resource_response)
        self.assertTrue(isinstance(list_representation_resource_response.resource, list))
        self.assertEqual(1, len(list_representation_resource_response.resource))

    def test_retrieve_mp4_representation(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.Smooth.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_mp4_representation = self._get_sample_mp4_representation()
        mp4_representation_response = self.bitmovin.manifests.Smooth.MP4Representation.create(
            object_=sample_mp4_representation, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(mp4_representation_response)
        self.assertIsNotNone(mp4_representation_response.resource)
        self.assertIsNotNone(mp4_representation_response.resource.id)
        self._compare_mp4_representations(sample_mp4_representation, mp4_representation_response.resource)

        retrieve_representation_resource_response = self.bitmovin.manifests.Smooth.MP4Representation.retrieve(
            manifest_id=manifest_resource_response.resource.id, representation_id=mp4_representation_response.resource.id)

        self.assertIsNotNone(retrieve_representation_resource_response)
        self.assertTrue(isinstance(retrieve_representation_resource_response.resource, MP4Representation))
        self._compare_mp4_representations(sample_mp4_representation, retrieve_representation_resource_response.resource)

    def test_delete_mp4_representation(self):
        sample_manifest = self._get_sample_manifest()
        manifest_resource_response = self.bitmovin.manifests.Smooth.create(sample_manifest)
        self.assertIsNotNone(manifest_resource_response)
        self.assertIsNotNone(manifest_resource_response.resource)
        self.assertIsNotNone(manifest_resource_response.resource.id)
        self._compare_manifests(sample_manifest, manifest_resource_response.resource)

        sample_mp4_representation = self._get_sample_mp4_representation()
        mp4_representation_response = self.bitmovin.manifests.Smooth.MP4Representation.create(
            object_=sample_mp4_representation, manifest_id=manifest_resource_response.resource.id)

        self.assertIsNotNone(mp4_representation_response)
        self.assertIsNotNone(mp4_representation_response.resource)
        self.assertIsNotNone(mp4_representation_response.resource.id)
        self._compare_mp4_representations(sample_mp4_representation, mp4_representation_response.resource)

        delete_sample_mp4_representation_resource_response = self.bitmovin.manifests.Smooth.MP4Representation.delete(
            manifest_id=manifest_resource_response.resource.id, representation_id=mp4_representation_response.resource.id)

        self.assertIsNotNone(delete_sample_mp4_representation_resource_response)
        self.assertIsNotNone(delete_sample_mp4_representation_resource_response.resource)
        self.assertIsNotNone(delete_sample_mp4_representation_resource_response.resource.id)
        self.assertEqual(mp4_representation_response.resource.id,
                         delete_sample_mp4_representation_resource_response.resource.id)

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

    def _compare_mp4_representations(self, first: AbstractMP4Representation, second: AbstractMP4Representation):
        self.assertEqual(first.encodingId, second.encodingId)
        self.assertEqual(first.muxingId, second.muxingId)
        self.assertEqual(first.mediaFile, second.mediaFile)
        self.assertEqual(first.language, second.language)
        self.assertEqual(first.trackName, second.trackName)
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

    def _get_sample_mp4_representation(self):
        encoding_id = self.sampleEncoding.id
        muxing_id = self.sampleMuxing.id

        mp4_representation = MP4Representation(encoding_id=encoding_id,
                                               muxing_id=muxing_id,
                                               media_file='myrendition.ismv')
        return mp4_representation

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
        muxing_resource_response = self.bitmovin.encodings.Muxing.MP4.create(object_=sample_muxing,
                                                                              encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(muxing_resource_response)
        self.assertIsNotNone(muxing_resource_response.resource)
        self.assertIsNotNone(muxing_resource_response.resource.id)
        self._compare_muxings(sample_muxing, muxing_resource_response.resource)
        return (muxing_resource_response.resource, created_stream)


if __name__ == '__main__':
    unittest.main()
