import unittest
import uuid
import json
from bitmovin import Bitmovin, Response, Stream, StreamInput, EncodingOutput, ACLEntry, ACLPermission, Encoding, \
    SelectionMode, Thumbnail
from bitmovin.errors import BitmovinApiError
from bitmovin.resources.enums.thumbnail_unit import ThumbnailUnit
from tests.bitmovin import BitmovinTestCase


class EncodingThumbnailTests(BitmovinTestCase):
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

    def test_create_thumbnail(self):
        stream = self._get_sample_stream()
        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)
        stream_id = create_stream_response.resource.id

        sample_thumbnail = self._get_sample_thumbnail()
        thumbnail_resource_response = self.bitmovin.encodings.Stream.Thumbnail.create(object_=sample_thumbnail,
                                                                                      encoding_id=self.sampleEncoding.id,
                                                                                      stream_id=stream_id)

        self.assertIsNotNone(thumbnail_resource_response)
        self.assertIsNotNone(thumbnail_resource_response.resource)
        self.assertIsNotNone(thumbnail_resource_response.resource.id)
        self._compare_thumbnails(sample_thumbnail, thumbnail_resource_response.resource)

    def test_create_thumbnail_without_name(self):
        stream = self._get_sample_stream()
        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)
        stream_id = create_stream_response.resource.id

        sample_thumbnail = self._get_sample_thumbnail()
        sample_thumbnail.name = None
        thumbnail_resource_response = self.bitmovin.encodings.Stream.Thumbnail.create(object_=sample_thumbnail,
                                                                                      encoding_id=self.sampleEncoding.id,
                                                                                      stream_id=stream_id)

        self.assertIsNotNone(thumbnail_resource_response)
        self.assertIsNotNone(thumbnail_resource_response.resource)
        self.assertIsNotNone(thumbnail_resource_response.resource.id)
        self._compare_thumbnails(sample_thumbnail, thumbnail_resource_response.resource)

    def test_retrieve_thumbnail(self):
        stream = self._get_sample_stream()
        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)
        stream_id = create_stream_response.resource.id

        sample_thumbnail = self._get_sample_thumbnail()
        sample_thumbnail.name = None
        thumbnail_resource_response = self.bitmovin.encodings.Stream.Thumbnail.create(object_=sample_thumbnail,
                                                                                      encoding_id=self.sampleEncoding.id,
                                                                                      stream_id=stream_id)

        self.assertIsNotNone(thumbnail_resource_response)
        self.assertIsNotNone(thumbnail_resource_response.resource)
        self.assertIsNotNone(thumbnail_resource_response.resource.id)
        self._compare_thumbnails(sample_thumbnail, thumbnail_resource_response.resource)

        retrieved_thumbnail_response = self.bitmovin.encodings.Stream.Thumbnail.retrieve(
            stream_id=stream_id, encoding_id=self.sampleEncoding.id,
            thumbnail_id=thumbnail_resource_response.resource.id)

        self.assertIsNotNone(retrieved_thumbnail_response)
        self.assertIsNotNone(retrieved_thumbnail_response.resource)
        self._compare_thumbnails(retrieved_thumbnail_response.resource, thumbnail_resource_response.resource)

    def test_delete_thumbnail(self):
        stream = self._get_sample_stream()
        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)
        stream_id = create_stream_response.resource.id

        sample_thumbnail = self._get_sample_thumbnail()
        thumbnail_resource_response = self.bitmovin.encodings.Stream.Thumbnail.create(object_=sample_thumbnail,
                                                                                      encoding_id=self.sampleEncoding.id,
                                                                                      stream_id=stream_id)

        self.assertIsNotNone(thumbnail_resource_response)
        self.assertIsNotNone(thumbnail_resource_response.resource)
        self.assertIsNotNone(thumbnail_resource_response.resource.id)
        self._compare_thumbnails(sample_thumbnail, thumbnail_resource_response.resource)

        deleted_minimal_resource = self.bitmovin.encodings.Stream.Thumbnail.delete(
            stream_id=stream_id,
            encoding_id=self.sampleEncoding.id,
            thumbnail_id=thumbnail_resource_response.resource.id
        )

        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.encodings.Stream.Thumbnail.retrieve(encoding_id=self.sampleEncoding.id,
                                                              stream_id=stream_id,
                                                              thumbnail_id=thumbnail_resource_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving muxing after deleting it should not be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_thumbnails(self):
        stream = self._get_sample_stream()
        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)
        stream_id = create_stream_response.resource.id

        sample_thumbnail = self._get_sample_thumbnail()
        thumbnail_resource_response = self.bitmovin.encodings.Stream.Thumbnail.create(object_=sample_thumbnail,
                                                                                      encoding_id=self.sampleEncoding.id,
                                                                                      stream_id=stream_id)

        self.assertIsNotNone(thumbnail_resource_response)
        self.assertIsNotNone(thumbnail_resource_response.resource)
        self.assertIsNotNone(thumbnail_resource_response.resource.id)
        self._compare_thumbnails(sample_thumbnail, thumbnail_resource_response.resource)

        thumbnails = self.bitmovin.encodings.Stream.Thumbnail.list(encoding_id=self.sampleEncoding.id,
                                                                   stream_id=stream_id)
        self.assertIsNotNone(thumbnails)
        self.assertIsNotNone(thumbnails.resource)
        self.assertIsNotNone(thumbnails.response)
        self.assertIsInstance(thumbnails.resource, list)
        self.assertIsInstance(thumbnails.response, Response)
        self.assertGreater(thumbnails.resource.__sizeof__(), 1)

    def test_retrieve_thumbnail_custom_data(self):
        stream = self._get_sample_stream()
        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)
        stream_id = create_stream_response.resource.id

        sample_thumbnail = self._get_sample_thumbnail()
        sample_thumbnail.customData = '{"myKey": "myValue", "My2ndKey": "my2ndValue", "my3RdKey": 234}'
        thumbnail_resource_response = self.bitmovin.encodings.Stream.Thumbnail.create(object_=sample_thumbnail,
                                                                                      encoding_id=self.sampleEncoding.id,
                                                                                      stream_id=stream_id)

        self.assertIsNotNone(thumbnail_resource_response)
        self.assertIsNotNone(thumbnail_resource_response.resource)
        self.assertIsNotNone(thumbnail_resource_response.resource.id)
        self._compare_thumbnails(sample_thumbnail, thumbnail_resource_response.resource)

        custom_data_response = self.bitmovin.encodings.Stream.Thumbnail.retrieve_custom_data(
            stream_id=stream_id,
            encoding_id=self.sampleEncoding.id,
            thumbnail_id=thumbnail_resource_response.resource.id
        )

        custom_data = custom_data_response.resource
        self.assertEqual(sample_thumbnail.customData, json.loads(custom_data.customData))

    def _compare_thumbnails(self, first: Thumbnail, second: Thumbnail):
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.height, second.height)
        self.assertEqual(first.unit, second.unit)
        return True

    def _get_sample_thumbnail(self):
        outputs = self._get_sample_outputs()
        thumbnail = Thumbnail(name='Sample Thumbnail Python',
                              description='Sample Thumbnail created using python tests',
                              height=460,
                              pattern="thumbnail_%number%.png",
                              unit=ThumbnailUnit.PERCENTS,
                              positions=[1, 2.5, 5],
                              outputs=outputs)
        return thumbnail

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

        self.assertIsNotNone(stream.codecConfigId)
        self.assertIsNotNone(stream.inputStreams)
        self.assertIsNotNone(stream.outputs)
        return stream

    def _get_sample_outputs(self):
        acl_entry = ACLEntry(scope='string', permission=ACLPermission.PUBLIC_READ)

        sample_output = self.utils.get_sample_s3_output()
        s3_output = self.bitmovin.outputs.S3.create(sample_output)
        encoding_output = EncodingOutput(output_id=s3_output.resource.id,
                                         output_path='/bitmovin-python/StreamTests/' + str(uuid.uuid4()),
                                         acl=[acl_entry])
        return [encoding_output]

    def _create_sample_encoding(self):
        sample_encoding = self.utils.get_sample_encoding()
        resource_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        return resource_response.resource


if __name__ == '__main__':
    unittest.main()
