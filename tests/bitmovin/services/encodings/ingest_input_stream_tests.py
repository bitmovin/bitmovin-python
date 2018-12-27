import unittest
from bitmovin import Bitmovin, Response, IngestInputStream, Encoding, SelectionMode
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class EncodingIngestInputStreamTests(BitmovinTestCase):

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

    def test_create_ingest_input_stream(self):
        sample_ingest_input_stream = self._get_sample_ingest_input_stream()

        ingest_input_stream_resource_response = self.bitmovin.encodings.IngestInputStream.create(
            object_=sample_ingest_input_stream,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(ingest_input_stream_resource_response)
        self.assertIsNotNone(ingest_input_stream_resource_response.resource)
        self.assertIsNotNone(ingest_input_stream_resource_response.resource.id)

        self._compare_ingest_input_streams(
            first=sample_ingest_input_stream,
            second=ingest_input_stream_resource_response.resource
        )

    def test_retrieve_ingest_input_stream(self):
        sample_ingest_input_stream = self._get_sample_ingest_input_stream()

        created_ingest_input_stream_response = self.bitmovin.encodings.IngestInputStream.create(
            object_=sample_ingest_input_stream,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(created_ingest_input_stream_response)
        self.assertIsNotNone(created_ingest_input_stream_response.resource)
        self.assertIsNotNone(created_ingest_input_stream_response.resource.id)

        self._compare_ingest_input_streams(
            first=sample_ingest_input_stream,
            second=created_ingest_input_stream_response.resource
        )

        retrieved_ingest_input_stream_response = self.bitmovin.encodings.IngestInputStream.retrieve(
            encoding_id=self.sampleEncoding.id,
            input_stream_id=created_ingest_input_stream_response.resource.id
        )

        self.assertIsNotNone(retrieved_ingest_input_stream_response)
        self.assertIsNotNone(retrieved_ingest_input_stream_response.resource)
        self.assertIsNotNone(retrieved_ingest_input_stream_response.resource.id)

        self._compare_ingest_input_streams(
            first=created_ingest_input_stream_response.resource,
            second=retrieved_ingest_input_stream_response.resource
        )

    def test_delete_stream(self):
        sample_ingest_input_stream = self._get_sample_ingest_input_stream()

        created_ingest_input_stream_response = self.bitmovin.encodings.IngestInputStream.create(
            object_=sample_ingest_input_stream,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(created_ingest_input_stream_response)
        self.assertIsNotNone(created_ingest_input_stream_response.resource)
        self.assertIsNotNone(created_ingest_input_stream_response.resource.id)

        self._compare_ingest_input_streams(
            first=sample_ingest_input_stream,
            second=created_ingest_input_stream_response.resource
        )

        deleted_minimal_resource = self.bitmovin.encodings.IngestInputStream.delete(
            encoding_id=self.sampleEncoding.id,
            input_stream_id=created_ingest_input_stream_response.resource.id
        )

        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)
        self.assertEqual(deleted_minimal_resource.resource.id, created_ingest_input_stream_response.resource.id)

        with self.assertRaises(BitmovinApiError):
            self.bitmovin.encodings.IngestInputStream.retrieve(
                encoding_id=self.sampleEncoding.id,
                input_stream_id=created_ingest_input_stream_response.resource.id
            )

    def test_list_streams(self):
        sample_ingest_input_stream = self._get_sample_ingest_input_stream()

        created_ingest_input_stream_response = self.bitmovin.encodings.IngestInputStream.create(
            object_=sample_ingest_input_stream,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(created_ingest_input_stream_response)
        self.assertIsNotNone(created_ingest_input_stream_response.resource)
        self.assertIsNotNone(created_ingest_input_stream_response.resource.id)

        self._compare_ingest_input_streams(
            first=sample_ingest_input_stream,
            second=created_ingest_input_stream_response.resource
        )

        ingest_input_streams = self.bitmovin.encodings.IngestInputStream.list(encoding_id=self.sampleEncoding.id)

        self.assertIsNotNone(ingest_input_streams)
        self.assertIsNotNone(ingest_input_streams.resource)
        self.assertIsNotNone(ingest_input_streams.response)
        self.assertIsInstance(ingest_input_streams.resource, list)
        self.assertIsInstance(ingest_input_streams.response, Response)
        self.assertGreater(ingest_input_streams.resource.__sizeof__(), 1)

    def _compare_ingest_input_streams(self, first: IngestInputStream, second: IngestInputStream):
        """

        :param first: IngestInputStream
        :param second: IngestInputStream
        :return: bool
        """
        self.assertEqual(first.inputId, second.inputId)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.inputPath, second.inputPath)
        self.assertEqual(first.selectionMode, second.selectionMode)

        if first.position:
            self.assertEqual(first.position, second.position)

        return True

    def _get_sample_ingest_input_stream(self):
        (sample_input, sample_files) = self.utils.get_sample_s3_input()
        s3_input = self.bitmovin.inputs.S3.create(sample_input)
        ingest_input_stream = IngestInputStream(input_id=s3_input.resource.id,
                                                input_path=sample_files.get('854b9c98-17b9-49ed-b75c-3b912730bfd1'),
                                                selection_mode=SelectionMode.AUTO,
                                                position=0)

        return ingest_input_stream

    def _create_sample_encoding(self):
        sample_encoding = self.utils.get_sample_encoding()
        resource_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        return resource_response.resource


if __name__ == '__main__':
    unittest.main()
