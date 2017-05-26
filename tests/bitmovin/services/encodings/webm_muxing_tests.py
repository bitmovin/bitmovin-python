import unittest
import uuid
import json
from bitmovin import Bitmovin, Response, Stream, StreamInput, EncodingOutput, ACLEntry, ACLPermission, Encoding, \
    EncodingStatus, WebMMuxing, MuxingStream, SelectionMode
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class EncodingWebMMuxingTests(BitmovinTestCase):

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

    def test_create_muxing(self):
        sample_muxing = self._get_sample_muxing()
        muxing_resource_response = self.bitmovin.encodings.Muxing.WebM.create(object_=sample_muxing,
                                                                              encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(muxing_resource_response)
        self.assertIsNotNone(muxing_resource_response.resource)
        self.assertIsNotNone(muxing_resource_response.resource.id)
        self._compare_muxings(sample_muxing, muxing_resource_response.resource)

    def test_create_muxing_without_name(self):
        sample_muxing = self._get_sample_muxing()
        sample_muxing.name = None
        muxing_resource_response = self.bitmovin.encodings.Muxing.WebM.create(object_=sample_muxing,
                                                                              encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(muxing_resource_response)
        self.assertIsNotNone(muxing_resource_response.resource)
        self.assertIsNotNone(muxing_resource_response.resource.id)
        self._compare_muxings(sample_muxing, muxing_resource_response.resource)

    def test_retrieve_muxing(self):
        sample_muxing = self._get_sample_muxing()
        created_muxing_response = self.bitmovin.encodings.Muxing.WebM.create(object_=sample_muxing,
                                                                             encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_muxing_response)
        self.assertIsNotNone(created_muxing_response.resource)
        self.assertIsNotNone(created_muxing_response.resource.id)
        self._compare_muxings(sample_muxing, created_muxing_response.resource)

        retrieved_muxing_response = self.bitmovin.encodings.Muxing.WebM.retrieve(
            muxing_id=created_muxing_response.resource.id, encoding_id=self.sampleEncoding.id)

        self.assertIsNotNone(retrieved_muxing_response)
        self.assertIsNotNone(retrieved_muxing_response.resource)
        self._compare_muxings(created_muxing_response.resource, retrieved_muxing_response.resource)

    @unittest.skip('DELETE route not available yet.')  # TODO: implement delete route in service
    def test_delete_muxing(self):
        sample_muxing = self._get_sample_muxing()
        created_muxing_response = self.bitmovin.encodings.Muxing.WebM.create(object_=sample_muxing,
                                                                             encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_muxing_response)
        self.assertIsNotNone(created_muxing_response.resource)
        self.assertIsNotNone(created_muxing_response.resource.id)
        self._compare_muxings(sample_muxing, created_muxing_response.resource)

        deleted_minimal_resource = self.bitmovin.encodings.Muxing.WebM.delete(
            muxing_id=created_muxing_response.resource.id,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.encodings.Muxing.WebM.retrieve(created_muxing_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving muxing after deleting it should not be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_muxings(self):
        sample_muxing = self._get_sample_muxing()
        created_muxing_response = self.bitmovin.encodings.Muxing.WebM.create(object_=sample_muxing,
                                                                             encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_muxing_response)
        self.assertIsNotNone(created_muxing_response.resource)
        self.assertIsNotNone(created_muxing_response.resource.id)
        self._compare_muxings(sample_muxing, created_muxing_response.resource)

        muxings = self.bitmovin.encodings.Muxing.WebM.list(encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(muxings)
        self.assertIsNotNone(muxings.resource)
        self.assertIsNotNone(muxings.response)
        self.assertIsInstance(muxings.resource, list)
        self.assertIsInstance(muxings.response, Response)
        self.assertGreater(muxings.resource.__sizeof__(), 1)

    def test_retrieve_stream_custom_data(self):
        sample_muxing = self._get_sample_muxing()
        sample_muxing.customData = '<pre>my custom data</pre>'
        created_muxing_response = self.bitmovin.encodings.Muxing.WebM.create(object_=sample_muxing,
                                                                        encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_muxing_response)
        self.assertIsNotNone(created_muxing_response.resource)
        self.assertIsNotNone(created_muxing_response.resource.id)
        self._compare_muxings(sample_muxing, created_muxing_response.resource)

        custom_data_response = self.bitmovin.encodings.Muxing.WebM.retrieve_custom_data(
            muxing_id=created_muxing_response.resource.id,
            encoding_id=self.sampleEncoding.id)

        custom_data = custom_data_response.resource
        self.assertEqual(sample_muxing.customData, json.loads(custom_data.customData))

    def _compare_muxings(self, first: WebMMuxing, second: WebMMuxing):
        """

        :param first: Stream
        :param second: Stream
        :return: bool
        """

        self.assertEqual(first.initSegmentName, second.initSegmentName)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.segmentLength, second.segmentLength)
        self.assertEqual(first.segmentNaming, second.segmentNaming)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _get_sample_muxing(self):
        stream = self._get_sample_stream()

        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)

        muxing_stream = MuxingStream(stream_id=create_stream_response.resource.id)

        muxing = WebMMuxing(streams=[muxing_stream],
                            segment_length=4,
                            segment_naming='seg_%number%.chk',
                            init_segment_name='init.hdr',
                            outputs=stream.outputs,
                            name='Sample WebM Muxing')
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
