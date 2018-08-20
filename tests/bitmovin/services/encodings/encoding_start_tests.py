import unittest
import json
from bitmovin import Bitmovin, StartEncodingRequest, Scheduling
from tests.bitmovin import BitmovinTestCase
from bitmovin.utils import BitmovinJSONEncoder


class EncodingStartTests(BitmovinTestCase):

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

    def test_encoding_start_request_serialization_with_prewarmed_instance_ids(self):
        prewarmed_instance_pool_ids = ['4a67260e-2fd3-4e9e-9829-651280ea8f06', '4b67260e-2fd3-4e9e-9829-651280ea8f07']
        scheduling = Scheduling(prewarmed_instance_pool_ids=prewarmed_instance_pool_ids)

        scheduling_serialized = json.dumps(obj=scheduling, cls=BitmovinJSONEncoder)
        self.assertEqual(first=scheduling_serialized, second='{"prewarmedInstancePoolIds": ["4a67260e-2fd3-4e9e-9829-651280ea8f06", "4b67260e-2fd3-4e9e-9829-651280ea8f07"]}')

        start_encoding_request = StartEncodingRequest(scheduling=scheduling)
        start_encoding_request_serialized = json.dumps(obj=start_encoding_request, cls=BitmovinJSONEncoder)
        self.assertEqual(first=start_encoding_request_serialized, second='{"scheduling": {"prewarmedInstancePoolIds": ["4a67260e-2fd3-4e9e-9829-651280ea8f06", "4b67260e-2fd3-4e9e-9829-651280ea8f07"]}}')


if __name__ == '__main__':
    unittest.main()
