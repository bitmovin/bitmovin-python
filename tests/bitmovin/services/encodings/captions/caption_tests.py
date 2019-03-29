import uuid

from bitmovin import Bitmovin, Response, Encoding, EncodingInput, Stream, StreamInput, SelectionMode, \
    BurnInSrtSubtitle, ACLEntry, ACLPermission, EncodingOutput, CaptionCharacterEncoding
from tests.bitmovin import BitmovinTestCase


class EncodingCaptionTests(BitmovinTestCase):
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
        self.sample_encoding = self._create_sample_encoding()  # type: Encoding

    def tearDown(self):
        super().tearDown()

    def test_create_burn_in_srt_subtitle(self):
        sample_subtitle = self._get_sample_burn_in_subtitle()
        sample_stream = self._get_sample_stream()

        burnin_subtitle_resource_response = self.bitmovin.encodings.Stream.BurnInSrtSubtitle.create(
            object_=sample_subtitle,
            encoding_id=self.sample_encoding.id,
            stream_id=sample_stream.id)
        self.assertIsNotNone(burnin_subtitle_resource_response)
        self.assertIsNotNone(burnin_subtitle_resource_response.resource)
        self.assertIsNotNone(burnin_subtitle_resource_response.resource.id)
        self._compare_subtitles(sample_subtitle, burnin_subtitle_resource_response.resource)

    def test_retrieve_burn_in_srt_subtitle(self):
        sample_subtitle = self._get_sample_burn_in_subtitle()
        sample_stream = self._get_sample_stream()

        created_burnin_subtitle_resource_response = self.bitmovin.encodings.Stream.BurnInSrtSubtitle.create(
            object_=sample_subtitle,
            encoding_id=self.sample_encoding.id,
            stream_id=sample_stream.id)

        retrieved_burnin_subtitle_response = self.bitmovin.encodings.Stream.BurnInSrtSubtitle.retrieve(
            burn_in_subtitle_id=created_burnin_subtitle_resource_response.resource.id,
            encoding_id=self.sample_encoding.id,
            stream_id=sample_stream.id
        )

        self.assertIsNotNone(retrieved_burnin_subtitle_response)
        self.assertIsNotNone(retrieved_burnin_subtitle_response.resource)
        self._compare_subtitles(created_burnin_subtitle_resource_response.resource,
                                retrieved_burnin_subtitle_response.resource)

    def test_list_burn_in_srt_subtitles(self):
        sample_subtitle = self._get_sample_burn_in_subtitle()
        sample_stream = self._get_sample_stream()

        created_burnin_subtitle_resource_response = self.bitmovin.encodings.Stream.BurnInSrtSubtitle.create(
            object_=sample_subtitle,
            encoding_id=self.sample_encoding.id,
            stream_id=sample_stream.id)

        burnin_subtitles = self.bitmovin.encodings.Stream.BurnInSrtSubtitle.list(
            encoding_id=self.sample_encoding.id,
            stream_id=sample_stream.id)
        self.assertIsNotNone(burnin_subtitles)
        self.assertIsNotNone(burnin_subtitles.resource)
        self.assertIsNotNone(burnin_subtitles.response)
        self.assertIsInstance(burnin_subtitles.resource, list)
        self.assertIsInstance(burnin_subtitles.response, Response)
        self.assertEqual(len(burnin_subtitles.resource), 1)

    def _compare_subtitles(self, first: BurnInSrtSubtitle, second: BurnInSrtSubtitle):
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.input.inputId, second.input.inputId)
        self.assertEqual(first.input.inputPath, second.input.inputPath)
        self.assertEqual(first.characterEncoding, second.characterEncoding)
        return True

    def _get_sample_burn_in_subtitle(self):
        (sample_input, sample_files) = self.utils.get_sample_s3_input()
        s3_input = self.bitmovin.inputs.S3.create(sample_input)

        encoding_input = EncodingInput(input_id=s3_input.resource.id,
                                       input_path="path/to/srt/file")
        self.assertIsNotNone(encoding_input.inputId)
        self.assertIsNotNone(encoding_input.inputPath)
        self.assertEqual(encoding_input.inputPath, "path/to/srt/file")

        subtitle = BurnInSrtSubtitle(name="Sample Subtitle for Burn-in",
                                     input=encoding_input,
                                     character_encoding=CaptionCharacterEncoding.UTF_8)
        self.assertIsNotNone(subtitle.input)
        self.assertIsNotNone(subtitle.name)
        return subtitle

    def _get_sample_stream(self):
        sample_codec_configuration = self.utils.get_sample_h264_codec_configuration()
        h264_codec_configuration = self.bitmovin.codecConfigurations.H264.create(sample_codec_configuration)

        (sample_input, sample_files) = self.utils.get_sample_s3_input()
        s3_input = self.bitmovin.inputs.S3.create(sample_input)
        stream_input = StreamInput(input_id=s3_input.resource.id,
                                   input_path=sample_files.get('854b9c98-17b9-49ed-b75c-3b912730bfd1'),
                                   selection_mode=SelectionMode.AUTO)

        encoding_outputs = self._get_sample_outputs()

        stream = Stream(codec_configuration_id=h264_codec_configuration.resource.id,
                        input_streams=[stream_input],
                        outputs=encoding_outputs,
                        name='Sample Stream')
        stream = self.bitmovin.encodings.Stream.create(stream, encoding_id=self.sample_encoding.id).resource
        return stream

    def _get_sample_outputs(self):
        acl_entry = ACLEntry(scope='string', permission=ACLPermission.PUBLIC_READ)

        sample_output = self.utils.get_sample_s3_output()
        s3_output = self.bitmovin.outputs.S3.create(sample_output)
        encoding_output = EncodingOutput(output_id=s3_output.resource.id,
                                         output_path='/bitmovin-python/StreamTests/'+str(uuid.uuid4()),
                                         acl=[acl_entry])
        return [encoding_output]

    def _create_sample_encoding(self):
        sample_encoding = self.utils.get_sample_encoding()
        resource_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        return resource_response.resource
