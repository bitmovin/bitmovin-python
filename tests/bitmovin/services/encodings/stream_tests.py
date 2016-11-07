import unittest
import uuid
from bitmovin import Bitmovin, Response, Stream, StreamInput, EncodingOutput, ACLEntry, Encoding, EncodingStatus, \
    ACLPermission, SelectionMode
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class EncodingStreamTests(BitmovinTestCase):

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

    def test_create_stream(self):
        sample_stream = self._get_sample_stream()
        stream_resource_response = self.bitmovin.encodings.Stream.create(object_=sample_stream,
                                                                         encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(stream_resource_response)
        self.assertIsNotNone(stream_resource_response.resource)
        self.assertIsNotNone(stream_resource_response.resource.id)
        self._compare_streams(sample_stream, stream_resource_response.resource)

    def test_retrieve_stream(self):
        sample_stream = self._get_sample_stream()
        created_stream_response = self.bitmovin.encodings.Stream.create(object_=sample_stream,
                                                                        encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_stream_response)
        self.assertIsNotNone(created_stream_response.resource)
        self.assertIsNotNone(created_stream_response.resource.id)
        self._compare_streams(sample_stream, created_stream_response.resource)

        retrieved_stream_response = self.bitmovin.encodings.Stream.retrieve(
            stream_id=created_stream_response.resource.id,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(retrieved_stream_response)
        self.assertIsNotNone(retrieved_stream_response.resource)
        self._compare_streams(created_stream_response.resource, retrieved_stream_response.resource)

    @unittest.skip("Currently there's no route for stream deletion")
    def test_delete_stream(self):
        sample_stream = self._get_sample_stream()
        created_stream_response = self.bitmovin.encodings.Stream.create(object_=sample_stream,
                                                                        encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_stream_response)
        self.assertIsNotNone(created_stream_response.resource)
        self.assertIsNotNone(created_stream_response.resource.id)
        self._compare_streams(sample_stream, created_stream_response.resource)

        deleted_minimal_resource = self.bitmovin.encodings.Stream.delete(stream_id=created_stream_response.resource.id,
                                                                         encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.encodings.Stream.retrieve(created_stream_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving stream after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_streams(self):
        sample_stream = self._get_sample_stream()
        created_stream_response = self.bitmovin.encodings.Stream.create(object_=sample_stream,
                                                                        encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_stream_response)
        self.assertIsNotNone(created_stream_response.resource)
        self.assertIsNotNone(created_stream_response.resource.id)
        self._compare_streams(sample_stream, created_stream_response.resource)

        streams = self.bitmovin.encodings.Stream.list(encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(streams)
        self.assertIsNotNone(streams.resource)
        self.assertIsNotNone(streams.response)
        self.assertIsInstance(streams.resource, list)
        self.assertIsInstance(streams.response, Response)
        self.assertGreater(streams.resource.__sizeof__(), 1)

    def test_retrieve_stream_custom_data(self):
        sample_stream = self._get_sample_stream()
        sample_stream.customData = '<pre>my custom data</pre>'
        created_stream_response = self.bitmovin.encodings.Stream.create(object_=sample_stream,
                                                                        encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_stream_response)
        self.assertIsNotNone(created_stream_response.resource)
        self.assertIsNotNone(created_stream_response.resource.id)
        self._compare_streams(sample_stream, created_stream_response.resource)

        custom_data_response = self.bitmovin.encodings.Stream.retrieve_custom_data(
            stream_id=created_stream_response.resource.id,
            encoding_id=self.sampleEncoding.id)

        custom_data = custom_data_response.resource
        self.assertEqual(sample_stream.customData, custom_data.customData)

    def test_retrieve_stream_status(self):
        sample_stream = self._get_sample_stream()
        created_stream_response = self.bitmovin.encodings.Stream.create(object_=sample_stream,
                                                                        encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_stream_response)
        self.assertIsNotNone(created_stream_response.resource)
        self.assertIsNotNone(created_stream_response.resource.id)
        self._compare_streams(sample_stream, created_stream_response.resource)

        stream_status_response = self.bitmovin.encodings.Stream.retrieve_status(
            stream_id=created_stream_response.resource.id,
            encoding_id=self.sampleEncoding.id)

        self.assertIsNotNone(stream_status_response)
        self.assertIsNotNone(stream_status_response.resource)
        resource = stream_status_response.resource  # type: EncodingStatus
        self.assertIsNotNone(resource.status)
        self.assertEqual('CREATED', resource.status)

    def _compare_streams(self, first: Stream, second: Stream):
        """

        :param first: Stream
        :param second: Stream
        :return: bool
        """
        self.assertEqual(first.codecConfigId, second.codecConfigId)
        if first.inputStreams:
            self.assertEqual(len(first.inputStreams), len(second.inputStreams))
        if first.outputs:
            self.assertEqual(len(first.outputs), len(second.outputs))
        return True

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
                        outputs=[encoding_output])

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
