import unittest
import uuid
from bitmovin import Bitmovin, Response, Stream, StreamInput, EncodingOutput, ACLEntry, Encoding, \
    FMP4Muxing, MuxingStream, ClearKeyDRM, DRMStatus, SelectionMode, ACLPermission
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class ClearKeyDRMTests(BitmovinTestCase):

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
        sample_drm = self._get_sample_drm_clearkey()
        sample_drm.outputs = fmp4_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: ClearKeyDRM
        self._compare_drms(sample_drm, drm_resource)

    def test_create_drm_without_name(self):
        fmp4_muxing = self._create_muxing()  # type: FMP4Muxing
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_clearkey()
        sample_drm.name = None
        sample_drm.outputs = fmp4_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: ClearKeyDRM
        self._compare_drms(sample_drm, drm_resource)

    def test_retrieve_drm(self):
        fmp4_muxing = self._create_muxing()
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_clearkey()
        sample_drm.outputs = fmp4_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: ClearKeyDRM
        self._compare_drms(sample_drm, drm_resource)

        retrieved_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.retrieve(
            encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id, drm_id=drm_resource.id)

        self.assertIsNotNone(retrieved_drm_response)
        self.assertIsNotNone(retrieved_drm_response.resource)
        self._compare_drms(retrieved_drm_response.resource, created_drm_response.resource)

    def test_retrieve_drm_sample_clearkey(self):
        fmp4_muxing = self._create_muxing()
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_clearkey()
        sample_drm.outputs = fmp4_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: ClearKeyDRM
        self._compare_drms(sample_drm, drm_resource)

        retrieved_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.retrieve(
            encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id, drm_id=drm_resource.id)

        self.assertIsNotNone(retrieved_drm_response)
        self.assertIsNotNone(retrieved_drm_response.resource)
        self._compare_drms(retrieved_drm_response.resource, created_drm_response.resource)

    def test_delete_drm(self):
        fmp4_muxing = self._create_muxing()
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_clearkey()
        sample_drm.outputs = fmp4_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: ClearKeyDRM
        self._compare_drms(sample_drm, drm_resource)

        deleted_minimal_resource = self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.delete(
            muxing_id=fmp4_muxing.id, encoding_id=self.sampleEncoding.id, drm_id=drm_resource.id)

        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.retrieve(encoding_id=self.sampleEncoding.id,
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
        sample_drm = self._get_sample_drm_clearkey()
        sample_drm.outputs = fmp4_muxing.outputs

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: ClearKeyDRM
        self._compare_drms(sample_drm, drm_resource)

        drms = self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.list(encoding_id=self.sampleEncoding.id,
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
        sample_drm = self._get_sample_drm_clearkey()
        sample_drm.outputs = fmp4_muxing.outputs
        sample_drm.customData = 'my_fancy_awesome_custom_data'

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: ClearKeyDRM
        self._compare_drms(sample_drm, drm_resource)

        custom_data_response = self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.retrieve_custom_data(
            muxing_id=fmp4_muxing.id,
            encoding_id=self.sampleEncoding.id,
            drm_id=drm_resource.id
        )

        custom_data = custom_data_response.resource
        self.assertEqual(sample_drm.customData, custom_data.customData)

    def test_retrieve_drm_status(self):
        fmp4_muxing = self._create_muxing()
        self.assertIsNotNone(fmp4_muxing.id)
        sample_drm = self._get_sample_drm_clearkey()
        sample_drm.outputs = fmp4_muxing.outputs
        sample_drm.customData = 'my_fancy_awesome_custom_data'

        created_drm_response = self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.create(
            object_=sample_drm, encoding_id=self.sampleEncoding.id, muxing_id=fmp4_muxing.id)

        self.assertIsNotNone(created_drm_response)
        self.assertIsNotNone(created_drm_response.resource)
        self.assertIsNotNone(created_drm_response.resource.id)
        drm_resource = created_drm_response.resource  # type: ClearKeyDRM
        self._compare_drms(sample_drm, drm_resource)

        drm_status_response = self.bitmovin.encodings.Muxing.FMP4.DRM.ClearKey.retrieve_status(
            muxing_id=fmp4_muxing.id,
            encoding_id=self.sampleEncoding.id,
            drm_id=drm_resource.id
        )

        self.assertIsNotNone(drm_status_response)
        self.assertIsNotNone(drm_status_response.resource)
        resource = drm_status_response.resource  # type: DRMStatus
        self.assertIsNotNone(resource.status)
        self.assertEqual('CREATED', resource.status)

    def _create_muxing(self):
        sample_muxing = self._get_sample_muxing()
        created_muxing_response = self.bitmovin.encodings.Muxing.FMP4.create(object_=sample_muxing,
                                                                             encoding_id=self.sampleEncoding.id)
        self.assertIsNotNone(created_muxing_response)
        self.assertIsNotNone(created_muxing_response.resource)
        self.assertIsNotNone(created_muxing_response.resource.id)
        self._compare_muxings(sample_muxing, created_muxing_response.resource)
        return created_muxing_response.resource

    def _compare_drms(self, first: ClearKeyDRM, second: ClearKeyDRM):
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
        return True

    def _compare_muxings(self, first: FMP4Muxing, second: FMP4Muxing):
        """

        :param first: Stream
        :param second: Stream
        :return: bool
        """

        self.assertEqual(first.segmentLength, second.segmentLength)
        self.assertEqual(first.segmentNaming, second.segmentNaming)
        self.assertEqual(len(first.outputs), len(second.outputs))
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _get_sample_drm_clearkey(self):
        clearkey_drm_settings = self.settings.get('sampleObjects').get('drmConfigurations').get('ClearKey')

        drm = ClearKeyDRM(key=clearkey_drm_settings[0].get('key'),
                          kid=clearkey_drm_settings[0].get('kid'),
                          name='Sample ClearKey DRM')

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
