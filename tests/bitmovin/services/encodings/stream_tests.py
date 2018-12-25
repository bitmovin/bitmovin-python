import unittest
import uuid
import json
from bitmovin import Bitmovin, Response, Stream, StreamInput, StreamMetadata, EncodingOutput, ACLEntry, Encoding, \
    ACLPermission, SelectionMode, StreamMode, StreamDecodingErrorMode
from bitmovin.errors import BitmovinApiError
from bitmovin.resources.models.encodings.conditions import AndConjunction, OrConjunction, Condition
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

    def test_create_stream_without_name(self):
        sample_stream = self._get_sample_stream()
        sample_stream.name = None
        stream_resource_response = self.bitmovin.encodings.Stream.create(object_=sample_stream,
                                                                         encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(stream_resource_response)
        self.assertIsNotNone(stream_resource_response.resource)
        self.assertIsNotNone(stream_resource_response.resource.id)
        self._compare_streams(sample_stream, stream_resource_response.resource)

    def test_create_stream_with_metadata(self):
        sample_stream = self._get_sample_stream()
        sample_stream.name = None
        stream_metadata = StreamMetadata(language='eng')
        sample_stream.metadata = stream_metadata

        self.assertIsNotNone(sample_stream.metadata)

        stream_resource_response = self.bitmovin.encodings.Stream.create(object_=sample_stream,
                                                                         encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(stream_resource_response)
        self.assertIsNotNone(stream_resource_response.resource)
        self.assertIsNotNone(stream_resource_response.resource.id)
        self._compare_streams(sample_stream, stream_resource_response.resource)

    def test_create_stream_per_title_fixed_resolution(self):
        sample_stream = self._get_sample_stream()
        sample_stream.mode = StreamMode.PER_TITLE_TEMPLATE_FIXED_RESOLUTION
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

    @unittest.skip('Currently there is no route for stream deletion')
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
        self.assertEqual(sample_stream.customData, json.loads(custom_data.customData))

    def _compare_streams(self, first: Stream, second: Stream):
        """

        :param first: Stream
        :param second: Stream
        :return: bool
        """
        self.assertEqual(first.codecConfigId, second.codecConfigId)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.mode, second.mode)
        if first.inputStreams:
            self.assertEqual(len(first.inputStreams), len(second.inputStreams))
        if first.outputs:
            self.assertEqual(len(first.outputs), len(second.outputs))
        if first.conditions:
            self._assertEqualConditions(first.conditions, second.conditions)
        if first.metadata:
            self._assertEqualConditions(first.metadata, second.metadata)
        return True

    def _get_sample_stream(self):
        sample_codec_configuration = self.utils.get_sample_h264_codec_configuration()
        h264_codec_configuration = self.bitmovin.codecConfigurations.H264.create(sample_codec_configuration)
        conditions = self._get_sample_conditions()

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
                        name='Sample Stream',
                        conditions=conditions,
                        mode=StreamMode.PER_TITLE_TEMPLATE,
                        decoding_error_mode=StreamDecodingErrorMode.FAIL_ON_ERROR)

        self.assertEqual(stream.codecConfigId, h264_codec_configuration.resource.id)
        self.assertEqual(stream.inputStreams, [stream_input])
        self.assertEqual(stream.outputs, [encoding_output])
        self.assertEqual(stream.conditions, conditions)
        self.assertEqual(stream.mode, StreamMode.PER_TITLE_TEMPLATE.value)
        self.assertEqual(stream.decodingErrorMode, StreamDecodingErrorMode.FAIL_ON_ERROR.value)

        return stream

    def _get_sample_conditions(self):
        bitrate_condition = Condition(attribute='BITRATE', operator='!=', value='2000000')
        fps_condition = Condition(attribute='FPS', operator='==', value='24')

        or_conjunctions = [bitrate_condition, fps_condition]
        sub_condition_or = OrConjunction(conditions=or_conjunctions)

        height_condition_condition = Condition(attribute='HEIGHT', operator='<=', value='400')
        and_conditions = [sub_condition_or, height_condition_condition]

        and_conjunction = AndConjunction(conditions=and_conditions)
        return and_conjunction

    def _create_sample_encoding(self):
        sample_encoding = self.utils.get_sample_encoding()
        resource_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        return resource_response.resource

    def _assertEqualConditions(self, first, second):
        if first is None and second is None:
            return True

        if first is not None and second is None:
            raise self.failureException('second condition is none but not first')

        if first is None and second is not None:
            raise self.failureException('first condition is none but not second')

        if isinstance(first, Condition):
            if isinstance(second, Condition):
                if first.attribute != second.attribute:
                    raise self.failureException('first.attribute is {}, second.attribute is {}'.format(
                        first.attribute, second.attribute))
                if first.operator != second.operator:
                    raise self.failureException('first.operator is {}, second.operator is {}'.format(
                        first.operator, second.operator))
                if first.value != second.value:
                    raise self.failureException('first.value is {}, second.value is {}'.format(
                        first.value, second.value))
            else:
                raise self.failureException('first is {}, second is {}'.format(type(first), type(second)))

        if isinstance(first, OrConjunction):
            if isinstance(second, OrConjunction):
                self.assertEqual(len(first.conditions), len(second.conditions))
            else:
                raise self.failureException('first is {}, second is {}'.format(type(first), type(second)))

        if isinstance(first, StreamMetadata):
            if isinstance(second, StreamMetadata):
                self.assertEqual(first.language, second.language)
            else:
                raise self.failureException('first is {}, second is {}'.format(type(first), type(second)))


if __name__ == '__main__':
    unittest.main()
