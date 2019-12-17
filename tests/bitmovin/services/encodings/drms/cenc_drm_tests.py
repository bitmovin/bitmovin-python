import unittest
import json
import uuid
from bitmovin import Bitmovin, Response, Stream, StreamInput, EncodingOutput, ACLEntry, Encoding, \
    FMP4Muxing, MuxingStream, CENCDRM, CENCPlayReadyEntry, CENCWidevineEntry, SelectionMode, ACLPermission, \
    IvSize, WebMMuxing, CENCMarlinEntry, CENCFairPlayEntry, PlayReadyDRMAdditionalInformation
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class CENCDRMTests(BitmovinTestCase):

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

    def test_create_drm(self):
        fmp4_muxing = self._create_muxing()  # type: FMP4Muxing
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_cenc()
        sample_drm.outputs = fmp4_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: CENCDRM
        self._compare_drms(sample_drm, drm_resource)

    def test_create_drm_with_additional_playready_information(self):
        fmp4_muxing = self._create_muxing()  # type: FMP4Muxing
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_cenc_playready_with_additional_information()
        sample_drm.outputs = fmp4_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: CENCDRM
        self.assertIsNotNone(drm_resource.playReady.additionalInformation)
        self._compare_drms(sample_drm, drm_resource)

    def test_create_drm_with_marlin(self):
        fmp4_muxing = self._create_muxing()  # type: FMP4Muxing
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_cenc_with_marlin()
        sample_drm.outputs = fmp4_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: CENCDRM
        self._compare_drms(sample_drm, drm_resource)

    def test_create_drm_with_8Byte_IV(self):
        fmp4_muxing = self._create_muxing()  # type: FMP4Muxing
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_cenc()
        sample_drm.outputs = fmp4_muxing.outputs
        sample_drm.ivSize = IvSize.EIGHT_BYTES

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: CENCDRM
        self._compare_drms(sample_drm, drm_resource)

    def test_create_drm_with_16Byte_IV(self):
        fmp4_muxing = self._create_muxing()  # type: FMP4Muxing
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_cenc()
        sample_drm.outputs = fmp4_muxing.outputs
        sample_drm.ivSize = IvSize.SIXTEEN_BYTES

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: CENCDRM
        self._compare_drms(sample_drm, drm_resource)

    def test_create_drm_with_piff_compatibility(self):
        fmp4_muxing = self._create_muxing()  # type: FMP4Muxing
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_cenc()
        sample_drm.outputs = fmp4_muxing.outputs
        sample_drm.enablePiffCompatibility = True

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: CENCDRM
        self._compare_drms(sample_drm, drm_resource)

    def test_create_drm_without_name(self):
        fmp4_muxing = self._create_muxing()  # type: FMP4Muxing
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_cenc()
        sample_drm.name = None
        sample_drm.outputs = fmp4_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: CENCDRM
        self._compare_drms(sample_drm, drm_resource)

    def test_create_cenc_drm_fairplay(self):
        fmp4_muxing = self._create_muxing()  # type: FMP4Muxing
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_cenc_with_fairplay()
        sample_drm.name = None
        sample_drm.outputs = fmp4_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: CENCDRM
        self._compare_drms(sample_drm, drm_resource)

    def test_create_cenc_drm_webm(self):
        webm_muxing = self._create_webm_muxing()  # type: WebMMuxing
        self.assertIsNotNone(webm_muxing.id)
        sample_drm = self._get_sample_drm_cenc()
        sample_drm.playReady = None
        sample_drm.outputs = webm_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.WebM.DRM.CENC.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=webm_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: CENCDRM
        self._compare_drms(sample_drm, drm_resource)

    def test_retrieve_drm(self):
        fmp4_muxing = self._create_muxing()
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_cenc()
        sample_drm.outputs = fmp4_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: CENCDRM
        self._compare_drms(sample_drm, drm_resource)

        retrieved_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.retrieve(
            encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id, drm_id=drm_resource.id)

        self.assertIsNotNone(retrieved_drm_response)
        self.assertIsNotNone(retrieved_drm_response.resource)
        self._compare_drms(retrieved_drm_response.resource, created_drm_response.resource)

    def test_delete_drm(self):
        fmp4_muxing = self._create_muxing()
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_cenc()
        sample_drm.outputs = fmp4_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: CENCDRM
        self._compare_drms(sample_drm, drm_resource)

        deleted_minimal_resource = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.delete(
            muxing_id=fmp4_muxing.id, encoding_id=self.sampleEncoding.id, drm_id=drm_resource.id)

        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.retrieve(encoding_id=self.sampleEncoding.id,
                                                                  muxing_id=fmp4_muxing.id, drm_id=drm_resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving muxing after deleting it should not be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_drms(self):
        fmp4_muxing = self._create_muxing()
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_cenc()
        sample_drm.outputs = fmp4_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: CENCDRM
        self._compare_drms(sample_drm, drm_resource)

        drms = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.list(encoding_id=self.sampleEncoding.id,
                                                                 muxing_id=fmp4_muxing.id)
        self.assertIsNotNone(drms)
        self.assertIsNotNone(drms.resource)
        self.assertIsNotNone(drms.response)
        self.assertIsInstance(drms.resource, list)
        self.assertIsInstance(drms.response, Response)
        self.assertGreater(drms.resource.__sizeof__(), 1)

    def test_retrieve_stream_custom_data(self):
        fmp4_muxing = self._create_muxing()
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_cenc()
        sample_drm.outputs = fmp4_muxing.outputs
        sample_drm.customData = 'my_fancy_awesome_custom_data'

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: CENCDRM
        self._compare_drms(sample_drm, drm_resource)

        custom_data_response = self.bitmovin.encodings.Muxing.FMP4.DRM.CENC.retrieve_custom_data(
            muxing_id=fmp4_muxing.id,
            encoding_id=self.sampleEncoding.id,
            drm_id=drm_resource.id
        )

        custom_data = custom_data_response.resource
        self.assertEqual(sample_drm.customData, json.loads(custom_data.customData))

    def _create_muxing(self):
        sample_muxing = self._get_sample_muxing()
        created_muxing_response = self.bitmovin.encodings.Muxing.FMP4.create(object_=sample_muxing,
                                                                             encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_muxing_response)
        self.assertIsNotNone(created_muxing_response.resource)
        self.assertIsNotNone(created_muxing_response.resource.id)
        self._compare_muxings(sample_muxing, created_muxing_response.resource)
        return created_muxing_response.resource

    def _create_webm_muxing(self):
        sample_muxing = self._get_sample_webm_muxing()
        created_muxing_response = self.bitmovin.encodings.Muxing.WebM.create(object_=sample_muxing,
                                                                             encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_muxing_response)
        self.assertIsNotNone(created_muxing_response.resource)
        self.assertIsNotNone(created_muxing_response.resource.id)
        self._compare_webm_muxings(sample_muxing, created_muxing_response.resource)
        return created_muxing_response.resource

    def _compare_drms(self, first: CENCDRM, second: CENCDRM):
        """

        :param first:
        :param second:
        :return: bool
        """

        self.assertEqual(first.kid, second.kid)
        self.assertEqual(first.key, second.key)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertTrue(self._compare_widevine_drm(first.widevine, second.widevine))
        self.assertTrue(self._compare_playready_drm(first.playReady, second.playReady))
        self.assertTrue(self._compare_marlin_drm(first.marlin, second.marlin))
        self.assertTrue(self._compare_fairplay_drm(first.fairPlay, second.fairPlay))
        self.assertEqual(first.enablePiffCompatibility, second.enablePiffCompatibility)
        self.assertEqual(first.ivSize, second.ivSize)

        return True

    def _compare_fairplay_drm(self, first: CENCFairPlayEntry, second: CENCFairPlayEntry):
        if first is None and second is None:
            return True

        self.assertEqual(first.iv, second.iv)
        self.assertEqual(first.uri, second.uri)

        return True

    def _compare_widevine_drm(self, first: CENCWidevineEntry, second: CENCWidevineEntry):
        if first is None and second is None:
            return True

        self.assertEqual(first.pssh, second.pssh)

        return True

    def _compare_playready_drm(self, first: CENCPlayReadyEntry, second: CENCPlayReadyEntry):
        if first is None and second is None:
            return True

        self.assertEqual(first.pssh, second.pssh)
        self.assertEqual(first.laUrl, second.laUrl)

        if first.additionalInformation is None and second.additionalInformation is None:
            return True

        self.assertEqual(first.additionalInformation.wrm_header_custom_attributes,
                         second.additionalInformation.wrm_header_custom_attributes)

        return True

    def _compare_marlin_drm(self, first: CENCMarlinEntry, second: CENCMarlinEntry):
        if first is None and second is None:
            return True

        return True

    def _compare_muxings(self, first: FMP4Muxing, second: FMP4Muxing):
        """

        :param first: FMP4Muxing
        :param second: FMP4Muxing
        :return: bool
        """

        self.assertEqual(first.segmentLength, second.segmentLength)
        self.assertEqual(first.segmentNaming, second.segmentNaming)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _compare_webm_muxings(self, first: WebMMuxing, second: WebMMuxing):
        """

        :param first: WebMMuxing
        :param second: WebMMuxing
        :return: bool
        """

        self.assertEqual(first.segmentLength, second.segmentLength)
        self.assertEqual(first.segmentNaming, second.segmentNaming)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _get_sample_drm_cenc(self):
        cenc_drm_settings = self.settings.get('sampleObjects').get('drmConfigurations').get('Cenc')
        widevine = CENCWidevineEntry(pssh=cenc_drm_settings[0].get('widevine').get('pssh'))
        play_ready = CENCPlayReadyEntry(la_url=cenc_drm_settings[0].get('playReady').get('laUrl'))

        drm = CENCDRM(key=cenc_drm_settings[0].get('key'),
                      kid=cenc_drm_settings[0].get('kid'),
                      widevine=widevine,
                      playReady=play_ready,
                      name='Sample CENC DRM')

        return drm

    def _get_sample_drm_cenc_playready_with_additional_information(self):
        cenc_drm_settings = self.settings.get('sampleObjects').get('drmConfigurations').get('Cenc')
        widevine = CENCWidevineEntry(pssh=cenc_drm_settings[0].get('widevine').get('pssh'))
        additional_information = PlayReadyDRMAdditionalInformation(
            wrm_header_custom_attributes="<custom><tag1>text</tag1></custom>")
        play_ready = CENCPlayReadyEntry(la_url=cenc_drm_settings[0].get('playReady').get('laUrl'),
                                        additional_information=additional_information)

        drm = CENCDRM(key=cenc_drm_settings[0].get('key'),
                      kid=cenc_drm_settings[0].get('kid'),
                      widevine=widevine,
                      playReady=play_ready,
                      name='Sample CENC DRM')

        return drm

    def _get_sample_drm_cenc_with_marlin(self):
        cenc_drm_settings = self.settings.get('sampleObjects').get('drmConfigurations').get('Cenc')
        widevine = CENCWidevineEntry(pssh=cenc_drm_settings[0].get('widevine').get('pssh'))
        play_ready = CENCPlayReadyEntry(la_url=cenc_drm_settings[0].get('playReady').get('laUrl'))
        marlin = {}

        drm = CENCDRM(key=cenc_drm_settings[0].get('key'),
                      kid=cenc_drm_settings[0].get('kid'),
                      widevine=widevine,
                      playReady=play_ready,
                      marlin=marlin,
                      name='Sample CENC DRM')

        return drm

    def _get_sample_drm_cenc_with_fairplay(self):
        cenc_drm_settings = self.settings.get('sampleObjects').get('drmConfigurations').get('Cenc')
        fairplay = CENCFairPlayEntry(
            iv=cenc_drm_settings[0].get('fairPlay').get('iv'),
            uri=cenc_drm_settings[0].get('fairPlay').get('uri')
        )

        drm = CENCDRM(key=cenc_drm_settings[0].get('key'),
                      kid=cenc_drm_settings[0].get('kid'),
                      fairplay=fairplay,
                      name='Sample CENC DRM with FairPlay')

        return drm

    def _get_sample_muxing(self):
        stream = self._get_sample_stream()

        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)

        muxing_stream = MuxingStream(stream_id=create_stream_response.resource.id)

        muxing = FMP4Muxing(streams=[muxing_stream], segment_length=4, segment_naming='seg_%number%.ts',
                            outputs=stream.outputs, name='Sample FMP4 Muxing')
        return muxing

    def _get_sample_webm_muxing(self):
        stream = self._get_sample_stream()

        create_stream_response = self.bitmovin.encodings.Stream.create(object_=stream,
                                                                       encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(create_stream_response)
        self.assertIsNotNone(create_stream_response.resource)
        self.assertIsNotNone(create_stream_response.resource.id)

        muxing_stream = MuxingStream(stream_id=create_stream_response.resource.id)

        muxing = WebMMuxing(streams=[muxing_stream], segment_length=4, segment_naming='seg_%number%.chk',
                            outputs=stream.outputs, name='Sample WebM Muxing')
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
