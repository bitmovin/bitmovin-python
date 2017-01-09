import unittest
import json
from bitmovin import Bitmovin, Response, CropFilter
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class CropFilterTests(BitmovinTestCase):

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

    def test_create_crop_filter(self):
        sample_filter = self._get_sample_crop_filter()
        filter_resource_response = self.bitmovin.filters.Crop.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_crop_filters(sample_filter, filter_resource_response.resource)

    def test_create_crop_filter_without_name(self):
        sample_filter = self._get_sample_crop_filter()
        sample_filter.name = None
        filter_resource_response = self.bitmovin.filters.Crop.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_crop_filters(sample_filter, filter_resource_response.resource)

    def test_retrieve_crop_filter(self):
        sample_filter = self._get_sample_crop_filter()
        created_filter_response = self.bitmovin.filters.Crop.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_crop_filters(sample_filter, created_filter_response.resource)

        retrieved_filter_response = self.bitmovin.filters.Crop.retrieve(created_filter_response.resource.id)
        self.assertIsNotNone(retrieved_filter_response)
        self.assertIsNotNone(retrieved_filter_response.resource)
        self._compare_crop_filters(created_filter_response.resource, retrieved_filter_response.resource)

    def test_delete_crop_filter(self):
        sample_filter = self._get_sample_crop_filter()
        created_filter_response = self.bitmovin.filters.Crop.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_crop_filters(sample_filter, created_filter_response.resource)

        deleted_minimal_resource = self.bitmovin.filters.Crop.delete(created_filter_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.filters.Crop.retrieve(created_filter_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving filter after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_crop_filters(self):
        sample_filter = self._get_sample_crop_filter()
        created_filter_response = self.bitmovin.filters.Crop.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_crop_filters(sample_filter, created_filter_response.resource)

        filters = self.bitmovin.filters.Crop.list()
        self.assertIsNotNone(filters)
        self.assertIsNotNone(filters.resource)
        self.assertIsNotNone(filters.response)
        self.assertIsInstance(filters.resource, list)
        self.assertIsInstance(filters.response, Response)
        self.assertGreater(filters.resource.__sizeof__(), 1)

    def test_retrieve_crop_filter_custom_data(self):
        sample_filter = self._get_sample_crop_filter()
        sample_filter.customData = '<pre>my custom data</pre>'
        created_filter_response = self.bitmovin.filters.Crop.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_crop_filters(sample_filter, created_filter_response.resource)

        custom_data_response = self.bitmovin.filters.Crop.retrieve_custom_data(created_filter_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_filter.customData, json.loads(custom_data.customData))

    def _compare_crop_filters(self, first: CropFilter, second: CropFilter):
        """

        :param first: CropFilter
        :param second: CropFilter
        :return: bool
        """
        self.assertEqual(first.top, second.top)
        self.assertEqual(first.bottom, second.bottom)
        self.assertEqual(first.left, second.left)
        self.assertEqual(first.right, second.right)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _get_sample_crop_filter(self):
        crop_filter = CropFilter(right=10, top=11, name='Sample Crop Filter 10 11')
        self.assertIsNotNone(crop_filter.right)
        self.assertIsNotNone(crop_filter.top)
        return crop_filter


if __name__ == '__main__':
    unittest.main()
