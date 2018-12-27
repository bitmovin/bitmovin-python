import unittest
from bitmovin import Bitmovin, Response, IngestInputStream, TimeCodeTrackTrimmingInputStream, Encoding, SelectionMode
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class EncodingTimeCodeTrackTrimmingInputStreamTests(BitmovinTestCase):

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
        self.sampleIngestInputStream = self._create_sample_ingest_input_stream(encoding_id=self.sampleEncoding.id)

    def tearDown(self):
        super().tearDown()

    def test_create_time_code_track_trimming_input_stream(self):
        sample_trimming_input_stream = self._get_sample_time_code_track_trimming_input_stream(
            input_stream_id=self.sampleIngestInputStream.id
        )

        trimming_input_stream_resource_response = self.bitmovin.encodings.TimeCodeTrackTrimmingInputStream.create(
            object_=sample_trimming_input_stream,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(trimming_input_stream_resource_response)
        self.assertIsNotNone(trimming_input_stream_resource_response.resource)
        self.assertIsNotNone(trimming_input_stream_resource_response.resource.id)

        self._compare_time_code_track_trimming_input_streams(
            first=sample_trimming_input_stream,
            second=trimming_input_stream_resource_response.resource
        )

    def test_retrieve_time_code_track_trimming_input_stream(self):
        sample_trimming_input_stream = self._get_sample_time_code_track_trimming_input_stream(
            input_stream_id=self.sampleIngestInputStream.id
        )

        trimming_input_stream_resource_response = self.bitmovin.encodings.TimeCodeTrackTrimmingInputStream.create(
            object_=sample_trimming_input_stream,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(trimming_input_stream_resource_response)
        self.assertIsNotNone(trimming_input_stream_resource_response.resource)
        self.assertIsNotNone(trimming_input_stream_resource_response.resource.id)

        self._compare_time_code_track_trimming_input_streams(
            first=sample_trimming_input_stream,
            second=trimming_input_stream_resource_response.resource
        )

        retrieved_trimming_input_stream_response = self.bitmovin.encodings.TimeCodeTrackTrimmingInputStream.retrieve(
            encoding_id=self.sampleEncoding.id,
            input_stream_id=trimming_input_stream_resource_response.resource.id
        )

        self.assertIsNotNone(retrieved_trimming_input_stream_response)
        self.assertIsNotNone(retrieved_trimming_input_stream_response.resource)
        self.assertIsNotNone(retrieved_trimming_input_stream_response.resource.id)

        self._compare_time_code_track_trimming_input_streams(
            first=trimming_input_stream_resource_response.resource,
            second=retrieved_trimming_input_stream_response.resource
        )

    def test_delete_time_code_track_trimming_input_stream(self):
        sample_trimming_input_stream = self._get_sample_time_code_track_trimming_input_stream(
            input_stream_id=self.sampleIngestInputStream.id
        )

        trimming_input_stream_resource_response = self.bitmovin.encodings.TimeCodeTrackTrimmingInputStream.create(
            object_=sample_trimming_input_stream,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(trimming_input_stream_resource_response)
        self.assertIsNotNone(trimming_input_stream_resource_response.resource)
        self.assertIsNotNone(trimming_input_stream_resource_response.resource.id)

        self._compare_time_code_track_trimming_input_streams(
            first=sample_trimming_input_stream,
            second=trimming_input_stream_resource_response.resource
        )

        deleted_minimal_resource = self.bitmovin.encodings.TimeCodeTrackTrimmingInputStream.delete(
            encoding_id=self.sampleEncoding.id,
            input_stream_id=trimming_input_stream_resource_response.resource.id
        )

        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)
        self.assertEqual(deleted_minimal_resource.resource.id, trimming_input_stream_resource_response.resource.id)

        with self.assertRaises(BitmovinApiError):
            self.bitmovin.encodings.TimeCodeTrackTrimmingInputStream.retrieve(
                encoding_id=self.sampleEncoding.id,
                input_stream_id=trimming_input_stream_resource_response.resource.id
            )

    def test_list_time_code_track_trimming_input_streams(self):
        sample_trimming_input_stream = self._get_sample_time_code_track_trimming_input_stream(
            input_stream_id=self.sampleIngestInputStream.id
        )

        trimming_input_stream_resource_response = self.bitmovin.encodings.TimeCodeTrackTrimmingInputStream.create(
            object_=sample_trimming_input_stream,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(trimming_input_stream_resource_response)
        self.assertIsNotNone(trimming_input_stream_resource_response.resource)
        self.assertIsNotNone(trimming_input_stream_resource_response.resource.id)

        self._compare_time_code_track_trimming_input_streams(
            first=sample_trimming_input_stream,
            second=trimming_input_stream_resource_response.resource
        )

        trimming_input_streams = self.bitmovin.encodings.TimeCodeTrackTrimmingInputStream.list(
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(trimming_input_streams)
        self.assertIsNotNone(trimming_input_streams.resource)
        self.assertIsNotNone(trimming_input_streams.response)
        self.assertIsInstance(trimming_input_streams.resource, list)
        self.assertIsInstance(trimming_input_streams.response, Response)
        self.assertGreater(trimming_input_streams.resource.__sizeof__(), 1)

        retrieved_input_stream = trimming_input_streams.resource[0]

        self.assertIsNotNone(retrieved_input_stream)
        self.assertIsInstance(retrieved_input_stream, TimeCodeTrackTrimmingInputStream)
        self._compare_time_code_track_trimming_input_streams(
            first=retrieved_input_stream,
            second=trimming_input_stream_resource_response.resource
        )

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

    def _compare_time_code_track_trimming_input_streams(self,
                                                        first: TimeCodeTrackTrimmingInputStream,
                                                        second: TimeCodeTrackTrimmingInputStream):
        """

        :param first: TimeCodeTrackTrimmingInputStream
        :param second: TimeCodeTrackTrimmingInputStream
        :return: bool
        """
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.inputStreamId, second.inputStreamId)
        self.assertEqual(first.startTimeCode, second.startTimeCode)
        self.assertEqual(first.endTimeCode, second.endTimeCode)

        return True

    def _get_sample_time_code_track_trimming_input_stream(self, input_stream_id):
        input_stream = TimeCodeTrackTrimmingInputStream(input_stream_id=input_stream_id,
                                                        start_time_code='09:36:14:01',
                                                        end_time_code='09:40:12:01',
                                                        name='Sample TimeCode Track Trimming Input Stream',
                                                        description='TCTTIS Python IT')

        return input_stream

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

    def _create_sample_ingest_input_stream(self, encoding_id):
        sample_ingest_input_stream = self._get_sample_ingest_input_stream()
        resource_response = self.bitmovin.encodings.IngestInputStream.create(
            object_=sample_ingest_input_stream,
            encoding_id=encoding_id
        )

        self.assertIsNotNone(resource_response)
        self.assertIsNotNone(resource_response.resource)
        self.assertIsNotNone(resource_response.resource.id)
        self._compare_ingest_input_streams(first=sample_ingest_input_stream, second=resource_response.resource)

        return resource_response.resource


if __name__ == '__main__':
    unittest.main()
