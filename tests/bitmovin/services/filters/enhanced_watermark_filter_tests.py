import json
import unittest

from bitmovin import Bitmovin, Response, WatermarkFilter, WatermarkUnit
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class EnhancedWatermarkFilterTests(BitmovinTestCase):

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

    def test_create_enchanced_watermark_filter(self):
        sample_filter = self._get_sample_enchanced_watermark_filter()
        filter_resource_response = self.bitmovin.filters.Watermark.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_enchanced_watermark_filters(sample_filter, filter_resource_response.resource)

    def test_create_enchanced_watermark_filter_without_name(self):
        sample_filter = self._get_sample_enchanced_watermark_filter()
        sample_filter.name = None
        filter_resource_response = self.bitmovin.filters.Watermark.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_enchanced_watermark_filters(sample_filter, filter_resource_response.resource)

    def test_retrieve_enchanced_watermark_filter(self):
        sample_filter = self._get_sample_enchanced_watermark_filter()
        created_filter_response = self.bitmovin.filters.Watermark.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_enchanced_watermark_filters(sample_filter, created_filter_response.resource)

        retrieved_filter_response = self.bitmovin.filters.Watermark.retrieve(created_filter_response.resource.id)
        self.assertIsNotNone(retrieved_filter_response)
        self.assertIsNotNone(retrieved_filter_response.resource)
        self._compare_enchanced_watermark_filters(created_filter_response.resource, retrieved_filter_response.resource)

    def test_delete_enchanced_watermark_filter(self):
        sample_filter = self._get_sample_enchanced_watermark_filter()
        created_filter_response = self.bitmovin.filters.Watermark.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_enchanced_watermark_filters(sample_filter, created_filter_response.resource)

        deleted_minimal_resource = self.bitmovin.filters.Watermark.delete(created_filter_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.filters.Watermark.retrieve(created_filter_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving filter after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_enchanced_watermark_filters(self):
        sample_filter = self._get_sample_enchanced_watermark_filter()
        created_filter_response = self.bitmovin.filters.Watermark.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_enchanced_watermark_filters(sample_filter, created_filter_response.resource)

        filters = self.bitmovin.filters.Watermark.list()
        self.assertIsNotNone(filters)
        self.assertIsNotNone(filters.resource)
        self.assertIsNotNone(filters.response)
        self.assertIsInstance(filters.resource, list)
        self.assertIsInstance(filters.response, Response)
        self.assertGreater(filters.resource.__sizeof__(), 1)

    def test_retrieve_enchanced_watermark_filter_custom_data(self):
        sample_filter = self._get_sample_enchanced_watermark_filter()
        sample_filter.customData = '<pre>my custom data</pre>'
        created_filter_response = self.bitmovin.filters.Watermark.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_enchanced_watermark_filters(sample_filter, created_filter_response.resource)

        custom_data_response = self.bitmovin.filters.Watermark.retrieve_custom_data(created_filter_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_filter.customData, json.loads(custom_data.customData))

    def _compare_enchanced_watermark_filters(self, first: WatermarkFilter, second: WatermarkFilter):
        """

        :param first: WatermarkFilter
        :param second: WatermarkFilter
        :return: bool
        """
        self.assertEqual(first.image, second.image)
        self.assertEqual(first.top, second.top)
        self.assertEqual(first.bottom, second.bottom)
        self.assertEqual(first.left, second.left)
        self.assertEqual(first.right, second.right)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.unit, second.unit)
        return True

    def _get_sample_enchanced_watermark_filter(self):
        enchanced_watermark_filter = WatermarkFilter(image='http://www.bitmovin.com/favicon.ico', right=10, top=10,
                                                     name='Sample Watermark Filter bitmovin icon',
                                                     unit=WatermarkUnit.PERCENTS)
        self.assertIsNotNone(enchanced_watermark_filter.image)
        self.assertIsNotNone(enchanced_watermark_filter.right)
        self.assertIsNotNone(enchanced_watermark_filter.top)
        self.assertIsNotNone(enchanced_watermark_filter.unit)
        return enchanced_watermark_filter


if __name__ == '__main__':
    unittest.main()
