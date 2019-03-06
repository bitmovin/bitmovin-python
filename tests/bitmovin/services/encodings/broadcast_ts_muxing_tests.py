import json
import unittest
import uuid

from bitmovin import Bitmovin, Response, Stream, StreamInput, EncodingOutput, ACLEntry, ACLPermission, Encoding, \
    MuxingStream, SelectionMode, BroadcastTsMuxing, BroadcastTsMuxingConfiguration, BroadcastTsTransportConfiguration, \
    BroadcastTsProgramConfiguration, BroadcastTsVideoStreamConfiguration, BroadcastTsAudioStreamConfiguration, \
    SetRaiOnAu, InternalChunkLengthMode, InternalChunkLength
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class BroadcastTsMuxingTests(BitmovinTestCase):

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
        muxing_resource_response = self.bitmovin.encodings.Muxing.BroadcastTS.create(object_=sample_muxing,
                                                                                     encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(muxing_resource_response)
        self.assertIsNotNone(muxing_resource_response.resource)
        self.assertIsNotNone(muxing_resource_response.resource.id)
        self._compare_muxings(sample_muxing, muxing_resource_response.resource)

    def test_create_muxing_without_name(self):
        sample_muxing = self._get_sample_muxing()
        sample_muxing.name = None
        muxing_resource_response = self.bitmovin.encodings.Muxing.BroadcastTS.create(object_=sample_muxing,
                                                                                     encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(muxing_resource_response)
        self.assertIsNotNone(muxing_resource_response.resource)
        self.assertIsNotNone(muxing_resource_response.resource.id)
        self._compare_muxings(sample_muxing, muxing_resource_response.resource)

    def test_retrieve_muxing(self):
        sample_muxing = self._get_sample_muxing()
        created_muxing_response = self.bitmovin.encodings.Muxing.BroadcastTS.create(object_=sample_muxing,
                                                                                    encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_muxing_response)
        self.assertIsNotNone(created_muxing_response.resource)
        self.assertIsNotNone(created_muxing_response.resource.id)
        self._compare_muxings(sample_muxing, created_muxing_response.resource)

        retrieved_muxing_response = self.bitmovin.encodings.Muxing.BroadcastTS.retrieve(
            muxing_id=created_muxing_response.resource.id, encoding_id=self.sampleEncoding.id)

        self.assertIsNotNone(retrieved_muxing_response)
        self.assertIsNotNone(retrieved_muxing_response.resource)
        self._compare_muxings(created_muxing_response.resource, retrieved_muxing_response.resource)

    def test_delete_muxing(self):
        sample_muxing = self._get_sample_muxing()
        created_muxing_response = self.bitmovin.encodings.Muxing.BroadcastTS.create(object_=sample_muxing,
                                                                                    encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_muxing_response)
        self.assertIsNotNone(created_muxing_response.resource)
        self.assertIsNotNone(created_muxing_response.resource.id)
        self._compare_muxings(sample_muxing, created_muxing_response.resource)

        deleted_minimal_resource = self.bitmovin.encodings.Muxing.BroadcastTS.delete(
            muxing_id=created_muxing_response.resource.id,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.encodings.Muxing.BroadcastTS.retrieve(encoding_id=self.sampleEncoding.id,
                                                                muxing_id=created_muxing_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving muxing after deleting it should not be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_muxings(self):
        sample_muxing = self._get_sample_muxing()
        created_muxing_response = self.bitmovin.encodings.Muxing.BroadcastTS.create(object_=sample_muxing,
                                                                                    encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_muxing_response)
        self.assertIsNotNone(created_muxing_response.resource)
        self.assertIsNotNone(created_muxing_response.resource.id)
        self._compare_muxings(sample_muxing, created_muxing_response.resource)

        muxings = self.bitmovin.encodings.Muxing.BroadcastTS.list(encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(muxings)
        self.assertIsNotNone(muxings.resource)
        self.assertIsNotNone(muxings.response)
        self.assertIsInstance(muxings.resource, list)
        self.assertIsInstance(muxings.response, Response)
        self.assertGreater(muxings.resource.__sizeof__(), 1)

    @unittest.skip('CUSTOM DATA route is not available yet')
    def test_retrieve_muxing_custom_data(self):
        sample_muxing = self._get_sample_muxing()
        sample_muxing.customData = '<pre>my custom data</pre>'
        created_muxing_response = self.bitmovin.encodings.Muxing.BroadcastTS.create(object_=sample_muxing,
                                                                                    encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_muxing_response)
        self.assertIsNotNone(created_muxing_response.resource)
        self.assertIsNotNone(created_muxing_response.resource.id)
        self._compare_muxings(sample_muxing, created_muxing_response.resource)

        custom_data_response = self.bitmovin.encodings.Muxing.BroadcastTS.retrieve_custom_data(
            muxing_id=created_muxing_response.resource.id,
            encoding_id=self.sampleEncoding.id)

        custom_data = custom_data_response.resource
        self.assertEqual(sample_muxing.customData, json.loads(custom_data.customData))

    def test_create_muxing_with_internal_chunk_length(self):
        sample_muxing = self._get_sample_muxing()

        internal_chunk_length = InternalChunkLength(mode=InternalChunkLengthMode.CUSTOM,
                                                    custom_chunk_length=12.345)

        sample_muxing.internal_chunk_length = internal_chunk_length

        muxing_resource_response = self.bitmovin.encodings.Muxing.BroadcastTS.create(
            object_=sample_muxing,
            encoding_id=self.sampleEncoding.id
        )

        self.assertIsNotNone(muxing_resource_response)
        self.assertIsNotNone(muxing_resource_response.resource)
        self.assertIsNotNone(muxing_resource_response.resource.id)
        self.assertIsNotNone(muxing_resource_response.resource.internal_chunk_length)
        self._compare_muxings(sample_muxing, muxing_resource_response.resource)

    def _compare_internal_chunk_length(self, first: InternalChunkLength, second: InternalChunkLength):
        """

        :param first: InternalChunkLength
        :param second: InternalChunkLength
        :return: bool
        """
        if first is None and second is None:
            return True

        self.assertEqual(first.mode, second.mode)
        self.assertEqual(first.customChunkLength, second.customChunkLength)
        return True

    def _compare_muxings(self, first: BroadcastTsMuxing, second: BroadcastTsMuxing):
        """

        :param first: BroadcastTsMuxing
        :param second: BroadcastTsMuxing
        :return: bool
        """

        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.segmentLength, second.segmentLength)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.filename, second.filename)
        self.assertEqual(True,
                         self._compare_broadcast_ts_muxing_configuration(first.configuration, second.configuration))
        self.assertTrue(self._compare_internal_chunk_length(first.internal_chunk_length, second.internal_chunk_length))
        return True

    def _compare_broadcast_ts_muxing_configuration(self, first: BroadcastTsMuxingConfiguration,
                                                   second: BroadcastTsMuxingConfiguration):
        """

        :param first: BroadcastTsMuxingConfiguration
        :param second: BroadcastTsMuxingConfiguration
        :return: bool
        """

        if first is None and second is None:
            return True

        self.assertEqual(True, self._compare_broadcast_ts_transport_configuration(
            first.transport, second.transport
        ))
        self.assertEqual(True, self._compare_broadcast_ts_program_configuration(
            first.program, second.program
        ))
        self.assertEqual(1, len(first.videoStreams))
        self.assertEqual(1, len(second.videoStreams))
        self.assertEqual(True, self._compare_broadcast_ts_video_stream_configuration(
            first.videoStreams[0], second.videoStreams[0]
        ))
        self.assertEqual(1, len(first.audioStreams))
        self.assertEqual(1, len(second.audioStreams))
        self.assertEqual(True, self._compare_broadcast_ts_audio_stream_configuration(
            first.audioStreams[0], second.audioStreams[0]
        ))
        return True

    def _compare_broadcast_ts_transport_configuration(self, first: BroadcastTsTransportConfiguration,
                                                      second: BroadcastTsTransportConfiguration):
        """

        :param first: BroadcastTsTransportConfiguration
        :param second: BroadcastTsTransportConfiguration
        :return: bool
        """

        if first is None and second is None:
            return True

        self.assertEqual(first.muxrate, second.muxrate)
        self.assertEqual(first.patRepetitionRatePerSec, second.patRepetitionRatePerSec)
        self.assertEqual(first.pmtRepetitionRatePerSec, second.pmtRepetitionRatePerSec)
        self.assertEqual(first.preventEmptyAdaptionFieldsInVideo, second.preventEmptyAdaptionFieldsInVideo)
        self.assertEqual(first.stopOnError, second.stopOnError)
        return True

    def _compare_broadcast_ts_program_configuration(self, first: BroadcastTsProgramConfiguration,
                                                    second: BroadcastTsProgramConfiguration):
        """

        :param first: BroadcastTsProgramConfiguration
        :param second: BroadcastTsProgramConfiguration
        :return: bool
        """

        if first is None and second is None:
            return True

        self.assertEqual(first.insertProgramClockRefOnPes, second.insertProgramClockRefOnPes)
        self.assertEqual(first.pidForPMT, second.pidForPMT)
        self.assertEqual(first.programNumber, second.programNumber)
        return True

    def _compare_broadcast_ts_video_stream_configuration(self, first: BroadcastTsVideoStreamConfiguration,
                                                         second: BroadcastTsVideoStreamConfiguration):
        """

        :param first: BroadcastTsVideoStreamConfiguration
        :param second:  BroadcastTsVideoStreamConfiguration
        :return: bool
        """

        if first is None and second is None:
            return True

        self.assertEqual(first.alignPes, second.alignPes)
        self.assertEqual(first.startWithDiscontinuityIndicator, second.startWithDiscontinuityIndicator)
        self.assertEqual(first.packetIdentifier, second.packetIdentifier)
        self.assertEqual(first.streamId, second.streamId)
        self.assertEqual(first.insertAccessUnitDelimiterinAvc, second.insertAccessUnitDelimiterinAvc)
        self.assertEqual(first.maxDecodeDelay, second.maxDecodeDelay)
        self.assertEqual(first.setRaiOnAu, second.setRaiOnAu)
        return True

    def _compare_broadcast_ts_audio_stream_configuration(self, first: BroadcastTsAudioStreamConfiguration,
                                                         second: BroadcastTsAudioStreamConfiguration):
        """

        :param first: BroadcastTsAudioStreamConfiguration
        :param second: BroadcastTsAudioStreamConfiguration
        :return: bool
        """

        if first is None and second is None:
            return True

        self.assertEqual(first.streamId, second.streamId)
        self.assertEqual(first.packetIdentifier, second.packetIdentifier)
        self.assertEqual(first.startWithDiscontinuityIndicator, second.startWithDiscontinuityIndicator)
        self.assertEqual(first.alignPes, second.alignPes)
        self.assertEqual(first.language, second.language)
        self.assertEqual(first.useATSCBufferModel, second.useATSCBufferModel)
        self.assertEqual(first.setRaiOnAu, second.setRaiOnAu)
        return True

    def _get_sample_muxing(self):
        video_stream = self._get_sample_video_stream()

        video_stream_response = self.bitmovin.encodings.Stream.create(object_=video_stream,
                                                                      encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(video_stream_response)
        self.assertIsNotNone(video_stream_response.resource)
        self.assertIsNotNone(video_stream_response.resource.id)

        audio_stream = self._get_sample_audio_stream()
        audio_stream_response = self.bitmovin.encodings.Stream.create(object_=audio_stream,
                                                                      encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(audio_stream_response)
        self.assertIsNotNone(audio_stream_response.resource)
        self.assertIsNotNone(audio_stream_response.resource.id)

        muxing_video_stream = MuxingStream(stream_id=video_stream_response.resource.id)
        muxing_audio_stream = MuxingStream(stream_id=audio_stream_response.resource.id)

        broadcast_ts_muxing_configuration = self._get_sample_broadcast_ts_muxing_configuration(
            video_stream_id=video_stream_response.resource.id,
            audio_stream_id=audio_stream_response.resource.id
        )

        return BroadcastTsMuxing(streams=[muxing_video_stream, muxing_audio_stream],
                                 segment_length=4,
                                 outputs=video_stream.outputs,
                                 name='Sample BroadcastTS Muxing',
                                 filename='pythontest.ts',
                                 configuration=broadcast_ts_muxing_configuration)

    def _get_sample_broadcast_ts_muxing_configuration(self, video_stream_id, audio_stream_id):
        broadcast_ts_transport_configuration = BroadcastTsTransportConfiguration(
            muxrate=0,
            stop_on_error=True,
            prevent_empty_adaptation_fields_in_video=True,
            pat_repetition_rate_per_sec=10,
            pmt_repetition_rate_per_sec=10
        )

        broadcast_ts_program_configuration = BroadcastTsProgramConfiguration(
            program_number=32,
            pid_for_pmt=64,
            insert_program_clock_ref_on_pes=True
        )

        broadcast_ts_video_stream_configuration = BroadcastTsVideoStreamConfiguration(
            stream_id=video_stream_id,
            packet_identifier=32,
            start_with_discontinuity_indicator=True,
            align_pes=True,
            set_rai_on_au=SetRaiOnAu.ACCORDING_TO_INPUT,
            insert_access_unit_delimiter_in_avc=True,
            max_decode_delay=500000
        )

        broadcast_ts_audio_stream_configuration = BroadcastTsAudioStreamConfiguration(
            stream_id=audio_stream_id,
            packet_identifier=32,
            start_with_discontinuity_indicator=True,
            align_pes=True,
            set_rai_on_au=SetRaiOnAu.ACCORDING_TO_INPUT,
            use_atsc_buffer_model=True,
            language='de'
        )

        return BroadcastTsMuxingConfiguration(
            transport=broadcast_ts_transport_configuration,
            program=broadcast_ts_program_configuration,
            video_streams=[broadcast_ts_video_stream_configuration],
            audio_streams=[broadcast_ts_audio_stream_configuration]
        )

    def _get_sample_audio_stream(self):
        aac_codec_configuration = self.utils.get_sample_aac_codec_configuration()
        aac_codec_configuration = self.bitmovin.codecConfigurations.AAC.create(aac_codec_configuration)

        (sample_input, sample_files) = self.utils.get_sample_s3_input()
        s3_input = self.bitmovin.inputs.S3.create(sample_input)

        stream_input = StreamInput(input_id=s3_input.resource.id,
                                   input_path=sample_files.get('854b9c98-17b9-49ed-b75c-3b912730bfd1'),
                                   selection_mode=SelectionMode.AUTO)

        acl_entry = ACLEntry(scope='string', permission=ACLPermission.PUBLIC_READ)

        sample_output = self.utils.get_sample_s3_output()
        s3_output = self.bitmovin.outputs.S3.create(sample_output)
        encoding_output = EncodingOutput(output_id=s3_output.resource.id,
                                         output_path='/bitmovin-python/StreamTests/' + str(uuid.uuid4()),
                                         acl=[acl_entry])

        stream = Stream(codec_configuration_id=aac_codec_configuration.resource.id,
                        input_streams=[stream_input],
                        outputs=[encoding_output],
                        name='Sample Audio Stream')

        self.assertIsNotNone(stream.codecConfigId)
        self.assertIsNotNone(stream.inputStreams)
        self.assertIsNotNone(stream.outputs)
        return stream

    def _get_sample_video_stream(self):
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
                                         output_path='/bitmovin-python/StreamTests/' + str(uuid.uuid4()),
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
