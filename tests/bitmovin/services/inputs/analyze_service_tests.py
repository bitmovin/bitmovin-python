import json
import time
import unittest
from bitmovin import Bitmovin, HTTPSInput, CustomData, Analysis, AnalysisStatus, AnalysisDetails, AnalysisVideoStream, \
    AnalysisStreamDetails, CloudRegion
from bitmovin.errors import BitmovinError
from bitmovin.utils import BitmovinJSONEncoder
from tests.bitmovin import BitmovinTestCase


class AnalyzeServiceTests(BitmovinTestCase):

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

    def tearDown(self):
        super().tearDown()

    def test_start_analyse_https_input(self):
        (sample_input, sample_file) = self._get_https_input_multiple_audio_tracks()
        created_input_response = self.bitmovin.inputs.HTTPS.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_https_inputs(sample_input, created_input_response.resource)
        analyze_request = Analysis(path=sample_file, cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)
        analyze_response = self.bitmovin.inputs.HTTPS.analyze(
            created_input_response.resource.id, analysis_object=analyze_request)
        self.assertIsNotNone(analyze_response)
        self.assertIsNotNone(analyze_response.resource)
        self.assertIsNotNone(analyze_response.resource.id)

    def test_list_analyses(self):
        (sample_input, sample_file) = self._get_https_input_multiple_audio_tracks()
        created_input_response = self.bitmovin.inputs.HTTPS.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_https_inputs(sample_input, created_input_response.resource)
        analyze_request = Analysis(path=sample_file, cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)
        analyze_response = self.bitmovin.inputs.HTTPS.analyze(
            created_input_response.resource.id, analysis_object=analyze_request)
        self.assertIsNotNone(analyze_response)
        self.assertIsNotNone(analyze_response.resource)
        self.assertIsNotNone(analyze_response.resource.id)

        analyses_list = self.bitmovin.inputs.S3.list_analyses(input_id=created_input_response.resource.id)
        self.assertIsNotNone(analyses_list)
        self.assertIsNotNone(analyses_list.resource)
        self.assertIsInstance(analyses_list.resource, list)
        self.assertIs(len(analyses_list.resource), 1)

    @unittest.skip('GET customData route not available yet.')  # TODO: implement get customdata route in service
    def test_start_analyse_with_custom_data(self):
        (sample_input, sample_file) = self._get_https_input_multiple_audio_tracks()
        created_input_response = self.bitmovin.inputs.HTTPS.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_https_inputs(sample_input, created_input_response.resource)
        analyze_request = Analysis(path=sample_file, cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1, custom_data='mycustomdata')
        analyze_response = self.bitmovin.inputs.HTTPS.analyze(
            created_input_response.resource.id, analysis_object=analyze_request)
        self.assertIsNotNone(analyze_response)
        self.assertIsNotNone(analyze_response.resource)
        self.assertIsNotNone(analyze_response.resource.id)

        custom_data_response = self.bitmovin.inputs.S3.retrieve_analysis_custom_data(
            input_id=created_input_response.resource.id, analysis_id=analyze_response.resource.id)

        custom_data = custom_data_response.resource  # type: CustomData
        self.assertEqual(analyze_request.customData, custom_data.customData)

    def test_retrieve_analysis_status_wait_until_finished(self):
        (sample_input, sample_file) = self._get_https_input_multiple_audio_tracks()
        created_input_response = self.bitmovin.inputs.HTTPS.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_https_inputs(sample_input, created_input_response.resource)
        analyze_request = Analysis(path=sample_file, cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)
        analyze_response = self.bitmovin.inputs.HTTPS.analyze(
            created_input_response.resource.id, analysis_object=analyze_request)
        self.assertIsNotNone(analyze_response)
        self.assertIsNotNone(analyze_response.resource)
        self.assertIsNotNone(analyze_response.resource.id)

        started_at = time.time()

        analysis_status = None

        while analysis_status != 'FINISHED' and analysis_status != 'ERROR':
            time.sleep(5)
            analysis_status = self.bitmovin.inputs.HTTPS.retrieve_analysis_status(
                input_id=created_input_response.resource.id,
                analysis_id=analyze_response.resource.id
            )
            analysis_status_resource = analysis_status.resource  # type: AnalysisStatus
            self.logger.info('Analysis Status: {}'.format(json.dumps(analysis_status_resource,
                                                                     cls=BitmovinJSONEncoder)))
            analysis_status = analysis_status_resource.status

        finished_at = time.time()
        difference = int(finished_at - started_at)
        self.logger.info('Analysis took {} seconds.'.format(difference))

        if analysis_status == 'ERROR':
            self.fail('Analysis FAILED!')

    def test_retrieve_analysis_details_multiple_audio(self):
        (sample_input, sample_file) = self._get_https_input_multiple_audio_tracks()
        analysis_details = self._retrieve_analysis_details_https_input(sample_input, sample_file)
        self.assertEqual(2, len(analysis_details.audioStreams))

        first = None
        second = None
        for audio_stream in analysis_details.audioStreams:
            if audio_stream.position == 0:
                first = audio_stream
            elif audio_stream.position == 1:
                second = audio_stream
            else:
                raise BitmovinError('Got unexpected audio stream position: {}'.format(audio_stream.position))

        self.assertEqual('swe', first.language)
        self.assertEqual('nor', second.language)

    def test_retrieve_analysis_details_multiple_audio_second(self):
        (sample_input, sample_file) = self._get_https_input_multiple_audio_tracks_second()
        analysis_details = self._retrieve_analysis_details_https_input(sample_input, sample_file)
        self.assertEqual(2, len(analysis_details.audioStreams))

        first = None
        second = None
        for audio_stream in analysis_details.audioStreams:
            if audio_stream.position == 0:
                first = audio_stream
            elif audio_stream.position == 1:
                second = audio_stream
            else:
                raise BitmovinError('Got unexpected audio stream position: {}'.format(audio_stream.position))

        self.assertIsNotNone(first)
        self.assertIsNotNone(second)

        self.assertEqual('nor', first.language)
        self.assertEqual('nor', second.language)
        self.assertEqual('ac3', first.codec)
        self.assertEqual('aac_latm', second.codec)

    def test_retrieve_analysis_details_multiple_audio_third(self):
        (sample_input, sample_file) = self._get_https_input_multiple_audio_tracks_second()
        analysis_details = self._retrieve_analysis_details_https_input(sample_input, sample_file)
        self.assertEqual(2, len(analysis_details.audioStreams))

        first = None
        second = None
        third = None
        for subtitle_stream in analysis_details.subtitleStreams:
            if subtitle_stream.position == 3:
                first = subtitle_stream
            elif subtitle_stream.position == 4:
                second = subtitle_stream
            elif subtitle_stream.position == 5:
                third = subtitle_stream
            else:
                raise BitmovinError('Got unexpected audio stream position: {}'.format(subtitle_stream.position))

        self.assertIsNotNone(first)
        self.assertIsNotNone(second)
        self.assertIsNotNone(third)
        self.assertIsNotNone(first.id)
        self.assertIsNotNone(second.id)
        self.assertIsNotNone(third.id)
        # self.assertIsNotNone(first.codec) see issue #643
        self.assertIsNotNone(second.codec)
        self.assertIsNotNone(third.codec)
        self.assertIsNotNone(first.language)
        self.assertIsNotNone(second.language)
        self.assertIsNotNone(third.language)

        self.assertEqual('nor', first.language)
        self.assertEqual('nor', second.language)
        self.assertEqual('nor', third.language)
        # self.assertEqual('???', first.codec) # see issue #643
        self.assertEqual('dvbsub', second.codec)
        self.assertEqual('dvbsub', third.codec)
        self.assertFalse(first.hearingImpaired)
        self.assertFalse(second.hearingImpaired)
        self.assertTrue(third.hearingImpaired)

    def _retrieve_analysis_details_https_input(self, sample_input, sample_file):
        created_input_response = self.bitmovin.inputs.HTTPS.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_https_inputs(sample_input, created_input_response.resource)
        analyze_request = Analysis(path=sample_file, cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)
        analyze_response = self.bitmovin.inputs.HTTPS.analyze(
            created_input_response.resource.id, analysis_object=analyze_request)
        self.assertIsNotNone(analyze_response)
        self.assertIsNotNone(analyze_response.resource)
        self.assertIsNotNone(analyze_response.resource.id)

        started_at = time.time()

        analysis_status = None

        while analysis_status != 'FINISHED' and analysis_status != 'ERROR':
            time.sleep(5)
            analysis_status = self.bitmovin.inputs.HTTPS.retrieve_analysis_status(
                input_id=created_input_response.resource.id,
                analysis_id=analyze_response.resource.id
            )
            analysis_status_resource = analysis_status.resource  # type: AnalysisStatus
            self.logger.info('Analysis Status: {}'.format(json.dumps(analysis_status_resource,
                                                                     cls=BitmovinJSONEncoder)))
            analysis_status = analysis_status_resource.status

        finished_at = time.time()
        difference = int(finished_at - started_at)
        self.logger.info('Analysis took {} seconds.'.format(difference))

        if analysis_status == 'ERROR':
            self.fail('Analysis FAILED!')

        analysis_details_response = self.bitmovin.inputs.HTTPS.retrieve_analysis_details(
            input_id=created_input_response.resource.id,
            analysis_id=analyze_response.resource.id
        )

        self.assertIsNotNone(analysis_details_response)
        self.assertIsNotNone(analysis_details_response.resource)
        analysis_details = analysis_details_response.resource  # type: AnalysisDetails
        self.assertIsNotNone(analysis_details.id)

        return analysis_details

    @unittest.skip('feature with more object not deployed yet')
    def test_retrieve_analysis_stream_details_multiple_audio(self):
        (sample_input, sample_file) = self._get_https_input_multiple_audio_tracks()
        self._retrieve_analysis_stream_details_https_input(sample_input, sample_file)

    def _retrieve_analysis_stream_details_https_input(self, sample_input, sample_file):
        created_input_response = self.bitmovin.inputs.HTTPS.create(sample_input)
        self.assertIsNotNone(created_input_response)
        self.assertIsNotNone(created_input_response.resource)
        self.assertIsNotNone(created_input_response.resource.id)
        self._compare_https_inputs(sample_input, created_input_response.resource)
        analyze_request = Analysis(path=sample_file, cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)
        analyze_response = self.bitmovin.inputs.HTTPS.analyze(
            created_input_response.resource.id, analysis_object=analyze_request)
        self.assertIsNotNone(analyze_response)
        self.assertIsNotNone(analyze_response.resource)
        self.assertIsNotNone(analyze_response.resource.id)

        started_at = time.time()

        analysis_status = None

        while analysis_status != 'FINISHED' and analysis_status != 'ERROR':
            time.sleep(5)
            analysis_status = self.bitmovin.inputs.HTTPS.retrieve_analysis_status(
                input_id=created_input_response.resource.id,
                analysis_id=analyze_response.resource.id
            )
            analysis_status_resource = analysis_status.resource  # type: AnalysisStatus
            self.logger.info('Analysis Status: {}'.format(json.dumps(analysis_status_resource,
                                                                     cls=BitmovinJSONEncoder)))
            analysis_status = analysis_status_resource.status

        finished_at = time.time()
        difference = int(finished_at - started_at)
        self.logger.info('Analysis took {} seconds.'.format(difference))

        if analysis_status == 'ERROR':
            self.fail('Analysis FAILED!')

        analysis_details_response = self.bitmovin.inputs.HTTPS.retrieve_analysis_details(
            input_id=created_input_response.resource.id,
            analysis_id=analyze_response.resource.id
        )

        self.assertIsNotNone(analysis_details_response)
        self.assertIsNotNone(analysis_details_response.resource)
        analysis_details = analysis_details_response.resource  # type: AnalysisDetails
        self.assertIsNotNone(analysis_details.id)

        video_stream = analysis_details.videoStreams[0]  # type: AnalysisVideoStream
        analysis_stream_details_response = self.bitmovin.inputs.HTTPS.retrieve_analysis_stream_details(
            input_id=created_input_response.resource.id,
            analysis_id=analyze_response.resource.id,
            stream_id=video_stream.id
        )
        self.assertIsNotNone(analysis_stream_details_response)
        self.assertIsNotNone(analysis_stream_details_response.resource)
        analysis_stream_details = analysis_stream_details_response.resource  # type: AnalysisStreamDetails
        self.assertIsNotNone(analysis_stream_details.more)

    def _compare_https_inputs(self, first: HTTPSInput, second: HTTPSInput):
        """

        :param first: HTTPSInput
        :param second: HTTPSInput
        :return: bool
        """
        self.assertEqual(first.host, second.host)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)

    def _get_https_input_multiple_audio_tracks(self):
        http_input_settings = self.settings.get('sampleObjects').get('inputs').get('http')\
            .get('4fa9fec1-b75e-4e2c-a01b-6e0cb7e3cf3e')
        input_file = http_input_settings.get('files').get('1c08c700-abcb-41f8-9cb7-3387503c1e50')
        self.assertIsNotNone(input_file)
        https_input = HTTPSInput(host=http_input_settings.get('host'), name='Sample HTTPS input multiple audio tracks')
        return https_input, input_file

    def _get_https_input_multiple_audio_tracks_second(self):
        http_input_settings = self.settings.get('sampleObjects').get('inputs').get('http')\
            .get('4fa9fec1-b75e-4e2c-a01b-6e0cb7e3cf3e')
        input_file = http_input_settings.get('files').get('7fd49d67-562b-4027-8e94-59b125bb2ef7')
        self.assertIsNotNone(input_file)
        https_input = HTTPSInput(host=http_input_settings.get('host'),
                                 name='Sample HTTPS input multiple audio tracks 2')
        return https_input, input_file

if __name__ == '__main__':
    unittest.main()
