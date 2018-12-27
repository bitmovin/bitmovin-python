import unittest
from bitmovin import Bitmovin, Response, IngestInputStream, Encoding, SelectionMode, \
    ConcatenationInputStreamConfiguration, ConcatenationInputStream
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class EncodingConcatenationInputStreamTests(BitmovinTestCase):

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

    def test_create_concatenation_input_stream(self):
        sample_concatenation_input_stream = self._get_sample_concatenation_input_stream()

        concatenation_input_stream_resource_response = self.bitmovin.encodings.ConcatenationInputStream.create(
            object_=sample_concatenation_input_stream,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(concatenation_input_stream_resource_response)
        self.assertIsNotNone(concatenation_input_stream_resource_response.resource)
        self.assertIsNotNone(concatenation_input_stream_resource_response.resource.id)

        self._compare_concatenation_input_streams(
            first=sample_concatenation_input_stream,
            second=concatenation_input_stream_resource_response.resource
        )

    def test_retrieve_concatenation_input_stream(self):
        sample_concatenation_input_stream = self._get_sample_concatenation_input_stream()

        created_concatenation_input_stream_response = self.bitmovin.encodings.ConcatenationInputStream.create(
            object_=sample_concatenation_input_stream,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(created_concatenation_input_stream_response)
        self.assertIsNotNone(created_concatenation_input_stream_response.resource)
        self.assertIsNotNone(created_concatenation_input_stream_response.resource.id)

        self._compare_concatenation_input_streams(
            first=sample_concatenation_input_stream,
            second=created_concatenation_input_stream_response.resource
        )

        retrieved_concatenation_input_stream_response = self.bitmovin.encodings.ConcatenationInputStream.retrieve(
            input_stream_id=created_concatenation_input_stream_response.resource.id,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(retrieved_concatenation_input_stream_response)
        self.assertIsNotNone(retrieved_concatenation_input_stream_response.resource)
        self.assertIsNotNone(retrieved_concatenation_input_stream_response.resource.id)

        self._compare_concatenation_input_streams(
            first=created_concatenation_input_stream_response.resource,
            second=retrieved_concatenation_input_stream_response.resource
        )

    def test_delete_concatenation_input_stream(self):
        sample_concatenation_input_stream = self._get_sample_concatenation_input_stream()

        created_concatenation_input_stream_response = self.bitmovin.encodings.ConcatenationInputStream.create(
            object_=sample_concatenation_input_stream,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(created_concatenation_input_stream_response)
        self.assertIsNotNone(created_concatenation_input_stream_response.resource)
        self.assertIsNotNone(created_concatenation_input_stream_response.resource.id)

        self._compare_concatenation_input_streams(
            first=sample_concatenation_input_stream,
            second=created_concatenation_input_stream_response.resource
        )

        deleted_minimal_resource = self.bitmovin.encodings.ConcatenationInputStream.delete(
            input_stream_id=created_concatenation_input_stream_response.resource.id,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)
        self.assertEqual(deleted_minimal_resource.resource.id, created_concatenation_input_stream_response.resource.id)

        with self.assertRaises(BitmovinApiError):
            self.bitmovin.encodings.ConcatenationInputStream.retrieve(
                encoding_id=self.sampleEncoding.id,
                input_stream_id=created_concatenation_input_stream_response.resource.id
            )

    def test_list_streams(self):
        sample_concatenation_input_stream = self._get_sample_concatenation_input_stream()

        created_concatenation_input_stream_response = self.bitmovin.encodings.ConcatenationInputStream.create(
            object_=sample_concatenation_input_stream,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(created_concatenation_input_stream_response)
        self.assertIsNotNone(created_concatenation_input_stream_response.resource)
        self.assertIsNotNone(created_concatenation_input_stream_response.resource.id)

        self._compare_concatenation_input_streams(
            first=sample_concatenation_input_stream,
            second=created_concatenation_input_stream_response.resource
        )

        concatenation_input_streams = self.bitmovin.encodings.ConcatenationInputStream.list(
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(concatenation_input_streams)
        self.assertIsNotNone(concatenation_input_streams.resource)
        self.assertIsNotNone(concatenation_input_streams.response)
        self.assertIsInstance(concatenation_input_streams.resource, list)
        self.assertIsInstance(concatenation_input_streams.response, Response)
        self.assertGreater(concatenation_input_streams.resource.__sizeof__(), 1)

        retrieved_input_stream = concatenation_input_streams.resource[0]

        self.assertIsNotNone(retrieved_input_stream)
        self.assertIsInstance(retrieved_input_stream, ConcatenationInputStream)
        self._compare_concatenation_input_streams(
            first=retrieved_input_stream,
            second=created_concatenation_input_stream_response.resource
        )

    def _compare_concatenation_input_streams(self, first: ConcatenationInputStream, second: ConcatenationInputStream):
        """

        :param first: ConcatenationInputStream
        :param second: ConcatenationInputStream
        :return: bool
        """

        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(len(first.concatenation), len(second.concatenation))

        for i in range(len(first.concatenation)):
            self._compare_concatenation_input_stream_configuration(first.concatenation[i], second.concatenation[i])

        return True

    def _compare_concatenation_input_stream_configuration(self,
                                                          first: ConcatenationInputStreamConfiguration,
                                                          second: ConcatenationInputStreamConfiguration):
        """

        :param first: ConcatenationInputStreamConfiguration
        :param second: ConcatenationInputStreamConfiguration
        :return: bool
        """
        self.assertEqual(first.inputStreamId, second.inputStreamId)
        self.assertEqual(first.isMain, second.isMain)
        self.assertEqual(first.position, second.position)

        return True

    def _get_sample_concatenation_input_stream(self):
        (sample_input, sample_files) = self.utils.get_sample_s3_input()
        s3_input = self.bitmovin.inputs.S3.create(sample_input)

        bumper_ingest_input_stream = IngestInputStream(
            input_id=s3_input.resource.id,
            input_path=sample_files.get('854b9c98-17b9-49ed-b75c-3b912730bfd1'),
            selection_mode=SelectionMode.AUTO,
            position=0
        )

        bumper_ingest_input_stream_resource_response = self.bitmovin.encodings.IngestInputStream.create(
            object_=bumper_ingest_input_stream,
            encoding_id=self.sampleEncoding.id
        )

        main_ingest_input_stream = IngestInputStream(
            input_id=s3_input.resource.id,
            input_path=sample_files.get('b373572e-ad12-4206-8e51-650a9c53b577'),
            selection_mode=SelectionMode.AUTO,
            position=0
        )

        main_ingest_input_stream_resource_response = self.bitmovin.encodings.IngestInputStream.create(
            object_=main_ingest_input_stream,
            encoding_id=self.sampleEncoding.id
        )

        bumper_concatenation_input_stream_config = ConcatenationInputStreamConfiguration(
            input_stream_id=bumper_ingest_input_stream_resource_response.resource.id,
            is_main=False,
            position=0
        )

        main_concatenation_input_stream_config = ConcatenationInputStreamConfiguration(
            input_stream_id=main_ingest_input_stream_resource_response.resource.id,
            is_main=True,
            position=0
        )

        concatenation_input_stream = ConcatenationInputStream(
            concatenation=[bumper_concatenation_input_stream_config, main_concatenation_input_stream_config]
        )

        return concatenation_input_stream

    def _create_sample_encoding(self):
        sample_encoding = self.utils.get_sample_encoding()
        resource_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        return resource_response.resource


if __name__ == '__main__':
    unittest.main()
