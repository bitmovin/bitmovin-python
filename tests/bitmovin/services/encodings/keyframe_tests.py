import unittest
from bitmovin import Bitmovin, Response, Encoding, Keyframe
from tests.bitmovin import BitmovinTestCase


class EncodingKeyframeTests(BitmovinTestCase):
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
        self.sample_encoding = self._create_sample_encoding()  # type: Encoding

    def tearDown(self):
        super().tearDown()

    def test_create_keyframe(self):
        sample_keyframe = self._get_sample_keyframe()
        keyframe_resource_response = self.bitmovin.encodings.Keyframe.create(object_=sample_keyframe,
                                                                             encoding_id=self.sample_encoding.id)
        self.assertIsNotNone(keyframe_resource_response)
        self.assertIsNotNone(keyframe_resource_response.resource)
        self.assertIsNotNone(keyframe_resource_response.resource.id)
        self._compare_keyframes(sample_keyframe, keyframe_resource_response.resource)

    def test_retrieve_keyframe(self):
        sample_keyframe = self._get_sample_keyframe()
        created_keyframe_response = self.bitmovin.encodings.Keyframe.create(object_=sample_keyframe,
                                                                            encoding_id=self.sample_encoding.id)
        self.assertIsNotNone(created_keyframe_response)
        self.assertIsNotNone(created_keyframe_response.resource)
        self.assertIsNotNone(created_keyframe_response.resource.id)
        self._compare_keyframes(sample_keyframe, created_keyframe_response.resource)

        retrieved_keyframe_response = self.bitmovin.encodings.Keyframe.retrieve(
            keyframe_id=created_keyframe_response.resource.id,
            encoding_id=self.sample_encoding.id
        )

        self.assertIsNotNone(retrieved_keyframe_response)
        self.assertIsNotNone(retrieved_keyframe_response.resource)
        self._compare_keyframes(created_keyframe_response.resource, retrieved_keyframe_response.resource)

    def test_list_keyframes(self):
        sample_keyframe = self._get_sample_keyframe()
        created_keyframe_response = self.bitmovin.encodings.Keyframe.create(object_=sample_keyframe,
                                                                            encoding_id=self.sample_encoding.id)
        self.assertIsNotNone(created_keyframe_response)
        self.assertIsNotNone(created_keyframe_response.resource)
        self.assertIsNotNone(created_keyframe_response.resource.id)
        self._compare_keyframes(sample_keyframe, created_keyframe_response.resource)

        keyframes = self.bitmovin.encodings.Keyframe.list(encoding_id=self.sample_encoding.id)
        self.assertIsNotNone(keyframes)
        self.assertIsNotNone(keyframes.resource)
        self.assertIsNotNone(keyframes.response)
        self.assertIsInstance(keyframes.resource, list)
        self.assertIsInstance(keyframes.response, Response)
        self.assertGreater(keyframes.resource.__sizeof__(), 1)

    def _compare_keyframes(self, first: Keyframe, second: Keyframe):
        self.assertEqual(first.time, second.time)
        self.assertEqual(first.segmentCut, second.segmentCut)
        return True

    def _get_sample_keyframe(self):
        keyframe = Keyframe(time=3.2, segment_cut=True)
        self.assertIsNotNone(keyframe.time)
        self.assertIsNotNone(keyframe.segmentCut)
        return keyframe

    def _create_sample_encoding(self):
        sample_encoding = self.utils.get_sample_encoding()
        resource_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        return resource_response.resource


if __name__ == '__main__':
    unittest.main()
