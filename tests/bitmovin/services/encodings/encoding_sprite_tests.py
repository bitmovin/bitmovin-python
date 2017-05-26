import unittest
import uuid
import json
from bitmovin import Bitmovin, Response, Stream, StreamInput, EncodingOutput, ACLEntry, ACLPermission, Encoding, \
    SelectionMode, Sprite
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class EncodingSpriteTests(BitmovinTestCase):

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

    def test_create_sprite(self):
        stream = self._get_sample_stream()
        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)
        stream_id = create_stream_response.resource.id

        sample_sprite = self._get_sample_sprite()
        sprite_resource_response = self.bitmovin.encodings.Stream.Sprite.create(object_=sample_sprite,
                                                                                encoding_id=self.sampleEncoding.id,
                                                                                stream_id=stream_id)

        self.assertIsNotNone(sprite_resource_response)
        self.assertIsNotNone(sprite_resource_response.resource)
        self.assertIsNotNone(sprite_resource_response.resource.id)
        self._compare_sprites(sample_sprite, sprite_resource_response.resource)

    def test_create_sprite_without_name(self):
        stream = self._get_sample_stream()
        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)
        stream_id = create_stream_response.resource.id

        sample_sprite = self._get_sample_sprite()
        sample_sprite.name = None
        sprite_resource_response = self.bitmovin.encodings.Stream.Sprite.create(object_=sample_sprite,
                                                                                encoding_id=self.sampleEncoding.id,
                                                                                stream_id=stream_id)

        self.assertIsNotNone(sprite_resource_response)
        self.assertIsNotNone(sprite_resource_response.resource)
        self.assertIsNotNone(sprite_resource_response.resource.id)
        self._compare_sprites(sample_sprite, sprite_resource_response.resource)

    def test_retrieve_sprite(self):
        stream = self._get_sample_stream()
        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)
        stream_id = create_stream_response.resource.id

        sample_sprite = self._get_sample_sprite()
        sample_sprite.name = None
        sprite_resource_response = self.bitmovin.encodings.Stream.Sprite.create(object_=sample_sprite,
                                                                                encoding_id=self.sampleEncoding.id,
                                                                                stream_id=stream_id)

        self.assertIsNotNone(sprite_resource_response)
        self.assertIsNotNone(sprite_resource_response.resource)
        self.assertIsNotNone(sprite_resource_response.resource.id)
        self._compare_sprites(sample_sprite, sprite_resource_response.resource)

        retrieved_sprite_response = self.bitmovin.encodings.Stream.Sprite.retrieve(
            stream_id=stream_id, encoding_id=self.sampleEncoding.id, sprite_id=sprite_resource_response.resource.id)

        self.assertIsNotNone(retrieved_sprite_response)
        self.assertIsNotNone(retrieved_sprite_response.resource)
        self._compare_sprites(retrieved_sprite_response.resource, sprite_resource_response.resource)

    def test_delete_sprite(self):
        stream = self._get_sample_stream()
        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)
        stream_id = create_stream_response.resource.id

        sample_sprite = self._get_sample_sprite()
        sprite_resource_response = self.bitmovin.encodings.Stream.Sprite.create(object_=sample_sprite,
                                                                                encoding_id=self.sampleEncoding.id,
                                                                                stream_id=stream_id)

        self.assertIsNotNone(sprite_resource_response)
        self.assertIsNotNone(sprite_resource_response.resource)
        self.assertIsNotNone(sprite_resource_response.resource.id)
        self._compare_sprites(sample_sprite, sprite_resource_response.resource)

        deleted_minimal_resource = self.bitmovin.encodings.Stream.Sprite.delete(
            stream_id=stream_id,
            encoding_id=self.sampleEncoding.id,
            sprite_id=sprite_resource_response.resource.id
        )

        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.encodings.Stream.Sprite.retrieve(encoding_id=self.sampleEncoding.id,
                                                           stream_id=stream_id,
                                                           sprite_id=sprite_resource_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving muxing after deleting it should not be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_sprites(self):
        stream = self._get_sample_stream()
        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)
        stream_id = create_stream_response.resource.id

        sample_sprite = self._get_sample_sprite()
        sprite_resource_response = self.bitmovin.encodings.Stream.Sprite.create(object_=sample_sprite,
                                                                                encoding_id=self.sampleEncoding.id,
                                                                                stream_id=stream_id)

        self.assertIsNotNone(sprite_resource_response)
        self.assertIsNotNone(sprite_resource_response.resource)
        self.assertIsNotNone(sprite_resource_response.resource.id)
        self._compare_sprites(sample_sprite, sprite_resource_response.resource)

        sprites = self.bitmovin.encodings.Stream.Sprite.list(encoding_id=self.sampleEncoding.id,
                                                             stream_id=stream_id)
        self.assertIsNotNone(sprites)
        self.assertIsNotNone(sprites.resource)
        self.assertIsNotNone(sprites.response)
        self.assertIsInstance(sprites.resource, list)
        self.assertIsInstance(sprites.response, Response)
        self.assertGreater(sprites.resource.__sizeof__(), 1)

    def test_retrieve_sprite_custom_data(self):
        stream = self._get_sample_stream()
        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)
        stream_id = create_stream_response.resource.id

        sample_sprite = self._get_sample_sprite()
        sample_sprite.customData = '{"myKey": "myValue", "My2ndKey": "my2ndValue", "my3RdKey": 234}'
        sprite_resource_response = self.bitmovin.encodings.Stream.Sprite.create(object_=sample_sprite,
                                                                                encoding_id=self.sampleEncoding.id,
                                                                                stream_id=stream_id)

        self.assertIsNotNone(sprite_resource_response)
        self.assertIsNotNone(sprite_resource_response.resource)
        self.assertIsNotNone(sprite_resource_response.resource.id)
        self._compare_sprites(sample_sprite, sprite_resource_response.resource)

        custom_data_response = self.bitmovin.encodings.Stream.Sprite.retrieve_custom_data(
            stream_id=stream_id,
            encoding_id=self.sampleEncoding.id,
            sprite_id=sprite_resource_response.resource.id
        )

        custom_data = custom_data_response.resource
        self.assertEqual(sample_sprite.customData, json.loads(custom_data.customData))

    def _compare_sprites(self, first: Sprite, second: Sprite):
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.height, second.height)
        self.assertEqual(first.width, second.width)
        self.assertEqual(first.spriteName, second.spriteName)
        self.assertEqual(first.vttName, second.vttName)
        self.assertEqual(first.distance, second.distance)
        return True

    def _get_sample_sprite(self):
        outputs = self._get_sample_outputs()
        sprite = Sprite(name='Sample Sprite Python',
                        description='Sample Sprite created using python tests',
                        height=480,
                        width=360,
                        sprite_name='myAwesomeSprite.jpg',
                        vtt_name='myAwesomeSpriteVtt.vtt',
                        distance=10,
                        outputs=outputs)
        return sprite

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
                                         output_path='/bitmovin-python/StreamTests/'+str(uuid.uuid4()),
                                         acl=[acl_entry])
        return [encoding_output]

    def _create_sample_encoding(self):
        sample_encoding = self.utils.get_sample_encoding()
        resource_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        return resource_response.resource


if __name__ == '__main__':
    unittest.main()
