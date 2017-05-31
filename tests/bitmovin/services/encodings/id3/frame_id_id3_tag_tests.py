import unittest
import base64
import uuid
import json
from bitmovin import Bitmovin, Response, Stream, StreamInput, EncodingOutput, ACLEntry, Encoding, \
    ProgressiveTSMuxing, MuxingStream, SelectionMode, ACLPermission, FrameIdID3Tag, ID3TagPositionMode
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class FrameIdID3TagTests(BitmovinTestCase):

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

    def tearDown(self):
        super().tearDown()

    def test_create_id3_frame_id(self):
        ts_muxing = self._create_muxing()  # type: ProgressiveTSMuxing
        self.assertIsNotNone(ts_muxing.id)
        frame_id_id3_tag = self._get_sample_id3_frame_id_time()
        created_id3_response = self.bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.create(
            object_=frame_id_id3_tag,
            encoding_id=self.sampleEncoding.id,
            muxing_id=ts_muxing.id
        )
        self.assertIsNotNone(created_id3_response)
        self.assertIsNotNone(created_id3_response.resource)
        self.assertIsNotNone(created_id3_response.resource.id)
        id3_resource = created_id3_response.resource  # type: FrameIdID3Tag
        self._compare_frame_id_id3_tags(frame_id_id3_tag, id3_resource)

    @unittest.skip("Not implemented yet")
    def test_create_id3_frame_id_frame(self):
        ts_muxing = self._create_muxing()  # type: ProgressiveTSMuxing
        self.assertIsNotNone(ts_muxing.id)
        frame_id_id3_tag = self._get_sample_id3_frame_id_frame()
        created_id3_response = self.bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.create(
            object_=frame_id_id3_tag,
            encoding_id=self.sampleEncoding.id,
            muxing_id=ts_muxing.id
        )
        self.assertIsNotNone(created_id3_response)
        self.assertIsNotNone(created_id3_response.resource)
        self.assertIsNotNone(created_id3_response.resource.id)
        id3_resource = created_id3_response.resource  # type: FrameIdID3Tag
        self._compare_frame_id_id3_tags(frame_id_id3_tag, id3_resource)

    def test_create_id3_frame_id_without_name(self):
        ts_muxing = self._create_muxing()  # type: ProgressiveTSMuxing
        self.assertIsNotNone(ts_muxing.id)
        frame_id_id3_tag = self._get_sample_id3_frame_id_time()
        frame_id_id3_tag.name = None
        created_id3_response = self.bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.create(
            object_=frame_id_id3_tag,
            encoding_id=self.sampleEncoding.id,
            muxing_id=ts_muxing.id
        )
        self.assertIsNotNone(created_id3_response)
        self.assertIsNotNone(created_id3_response.resource)
        self.assertIsNotNone(created_id3_response.resource.id)
        id3_resource = created_id3_response.resource  # type: FrameIdID3Tag
        self._compare_frame_id_id3_tags(frame_id_id3_tag, id3_resource)

    def test_retrieve_frame_id_id3(self):
        ts_muxing = self._create_muxing()  # type: ProgressiveTSMuxing
        self.assertIsNotNone(ts_muxing.id)
        frame_id_id3_tag = self._get_sample_id3_frame_id_time()
        created_id3_response = self.bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.create(
            object_=frame_id_id3_tag,
            encoding_id=self.sampleEncoding.id,
            muxing_id=ts_muxing.id
        )
        self.assertIsNotNone(created_id3_response)
        self.assertIsNotNone(created_id3_response.resource)
        self.assertIsNotNone(created_id3_response.resource.id)
        id3_resource = created_id3_response.resource  # type: FrameIdID3Tag
        self._compare_frame_id_id3_tags(frame_id_id3_tag, id3_resource)

        retrieved_id3_response = self.bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.retrieve(
            encoding_id=self.sampleEncoding.id,
            muxing_id=ts_muxing.id,
            id3_id=id3_resource.id
        )

        self.assertIsNotNone(retrieved_id3_response)
        self.assertIsNotNone(retrieved_id3_response.resource)
        self._compare_frame_id_id3_tags(retrieved_id3_response.resource, created_id3_response.resource)

    @unittest.skip("Not implemented yet")
    def test_retrieve_frame_id_id3_frame(self):
        ts_muxing = self._create_muxing()  # type: ProgressiveTSMuxing
        self.assertIsNotNone(ts_muxing.id)
        frame_id_id3_tag = self._get_sample_id3_frame_id_frame()
        created_id3_response = self.bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.create(
            object_=frame_id_id3_tag,
            encoding_id=self.sampleEncoding.id,
            muxing_id=ts_muxing.id
        )
        self.assertIsNotNone(created_id3_response)
        self.assertIsNotNone(created_id3_response.resource)
        self.assertIsNotNone(created_id3_response.resource.id)
        id3_resource = created_id3_response.resource  # type: FrameIdID3Tag
        self._compare_frame_id_id3_tags(frame_id_id3_tag, id3_resource)

        retrieved_id3_response = self.bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.retrieve(
            encoding_id=self.sampleEncoding.id,
            muxing_id=ts_muxing.id,
            id3_id=id3_resource.id
        )

        self.assertIsNotNone(retrieved_id3_response)
        self.assertIsNotNone(retrieved_id3_response.resource)
        self._compare_frame_id_id3_tags(retrieved_id3_response.resource, created_id3_response.resource)

    def test_delete_frame_id_id3(self):
        ts_muxing = self._create_muxing()  # type: ProgressiveTSMuxing
        self.assertIsNotNone(ts_muxing.id)
        frame_id_id3_tag = self._get_sample_id3_frame_id_time()
        created_id3_response = self.bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.create(
            object_=frame_id_id3_tag,
            encoding_id=self.sampleEncoding.id,
            muxing_id=ts_muxing.id
        )
        self.assertIsNotNone(created_id3_response)
        self.assertIsNotNone(created_id3_response.resource)
        self.assertIsNotNone(created_id3_response.resource.id)
        id3_resource = created_id3_response.resource  # type: FrameIdID3Tag
        self._compare_frame_id_id3_tags(frame_id_id3_tag, id3_resource)

        deleted_minimal_resource = self.bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.delete(
            muxing_id=ts_muxing.id,
            encoding_id=self.sampleEncoding.id,
            id3_id=id3_resource.id
        )

        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.retrieve(encoding_id=self.sampleEncoding.id,
                                                                              muxing_id=ts_muxing.id,
                                                                              id3_id=id3_resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving id3 tag after deleting it should not be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_frame_id_id3_tags(self):
        ts_muxing = self._create_muxing()  # type: ProgressiveTSMuxing
        self.assertIsNotNone(ts_muxing.id)
        frame_id_id3_tag = self._get_sample_id3_frame_id_time()
        created_id3_response = self.bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.create(
            object_=frame_id_id3_tag,
            encoding_id=self.sampleEncoding.id,
            muxing_id=ts_muxing.id
        )
        self.assertIsNotNone(created_id3_response)
        self.assertIsNotNone(created_id3_response.resource)
        self.assertIsNotNone(created_id3_response.resource.id)
        id3_resource = created_id3_response.resource  # type: FrameIdID3Tag
        self._compare_frame_id_id3_tags(frame_id_id3_tag, id3_resource)

        frame_id_id3_tags = self.bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.list(encoding_id=self.sampleEncoding.id,
                                                                                     muxing_id=ts_muxing.id)
        self.assertIsNotNone(frame_id_id3_tags)
        self.assertIsNotNone(frame_id_id3_tags.resource)
        self.assertIsNotNone(frame_id_id3_tags.response)
        self.assertIsInstance(frame_id_id3_tags.resource, list)
        self.assertIsInstance(frame_id_id3_tags.response, Response)
        self.assertGreater(frame_id_id3_tags.resource.__sizeof__(), 1)

    def test_retrieve_id3_custom_data(self):
        ts_muxing = self._create_muxing()  # type: ProgressiveTSMuxing
        self.assertIsNotNone(ts_muxing.id)
        frame_id_id3_tag = self._get_sample_id3_frame_id_time()
        frame_id_id3_tag.customData = {
            "myKey": "MY_VALUE"
        }
        created_id3_response = self.bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.create(
            object_=frame_id_id3_tag,
            encoding_id=self.sampleEncoding.id,
            muxing_id=ts_muxing.id
        )
        self.assertIsNotNone(created_id3_response)
        self.assertIsNotNone(created_id3_response.resource)
        self.assertIsNotNone(created_id3_response.resource.id)
        id3_resource = created_id3_response.resource  # type: FrameIdID3Tag
        self._compare_frame_id_id3_tags(frame_id_id3_tag, id3_resource)

        custom_data_response = self.bitmovin.encodings.Muxing.ProgressiveTS.ID3Tags.FrameId.retrieve_custom_data(
            muxing_id=ts_muxing.id,
            encoding_id=self.sampleEncoding.id,
            id3_id=id3_resource.id
        )

        custom_data = custom_data_response.resource
        self.assertEqual(frame_id_id3_tag.customData, json.loads(custom_data.customData))

    def _create_muxing(self):
        sample_muxing = self._get_sample_muxing()
        created_muxing_response = self.bitmovin.encodings.Muxing.ProgressiveTS.create(
            object_=sample_muxing,
            encoding_id=self.sampleEncoding.id
        )
        self.assertIsNotNone(created_muxing_response)
        self.assertIsNotNone(created_muxing_response.resource)
        self.assertIsNotNone(created_muxing_response.resource.id)
        self._compare_muxings(sample_muxing, created_muxing_response.resource)
        return created_muxing_response.resource

    def _compare_frame_id_id3_tags(self, first: FrameIdID3Tag, second: FrameIdID3Tag):
        self.assertEqual(first.bytes, second.bytes)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.positionMode, second.positionMode)
        self.assertEqual(first.time, second.time)
        self.assertEqual(first.frame, second.frame)
        return True

    def _compare_muxings(self, first: ProgressiveTSMuxing, second: ProgressiveTSMuxing):
        self.assertEqual(first.segmentLength, second.segmentLength)
        self.assertEqual(first.filename, second.filename)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _get_sample_id3_frame_id_frame(self):

        id3 = FrameIdID3Tag(position_mode=ID3TagPositionMode.FRAME, frame=1234,
                            bytes_=base64.b64encode(b'MyTag Python TeSt').decode('utf-8'), frame_id='ASIK',
                            name='FrameIdID3 Frame', description='no descr')

        return id3

    def _get_sample_id3_frame_id_time(self):

        id3 = FrameIdID3Tag(position_mode=ID3TagPositionMode.TIME, time=12.34,
                            bytes_=base64.b64encode(b'MyTag Python TeSt').decode('utf-8'), frame_id='OAYN',
                            name='FrameIdID3 Time', description='n')

        return id3

    def _get_sample_muxing(self):
        stream = self._get_sample_stream()

        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)

        muxing_stream = MuxingStream(stream_id=create_stream_response.resource.id)

        muxing = ProgressiveTSMuxing(
            streams=[muxing_stream],
            segment_length=4,
            filename='myprogressive.ts',
            outputs=stream.outputs,
            name='Sample TSMuxing'
        )
        return muxing

    def _get_sample_stream(self):
        sample_codec_configuration = self.utils.get_sample_h264_codec_configuration()
        h264_codec_configuration = self.bitmovin.codecConfigurations.H264.create(sample_codec_configuration)

        (sample_input, sample_files) = self.utils.get_sample_s3_input()
        s3_input = self.bitmovin.inputs.S3.create(sample_input)
        stream_input = StreamInput(input_id=s3_input.resource.id,
                                   input_path=sample_files.get('854b9c98-17b9-49ed-b75c-3b912730bfd1'),
                                   selection_mode=SelectionMode.AUTO)

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
        resource_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        return resource_response.resource


if __name__ == '__main__':
    unittest.main()
