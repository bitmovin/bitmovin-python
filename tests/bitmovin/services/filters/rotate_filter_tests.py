import unittest
from bitmovin import Bitmovin, Response, RotateFilter
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class RotateFilterTests(BitmovinTestCase):

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

    def test_create_rotate_filter(self):
        sample_filter = self._get_sample_rotate_filter()
        filter_resource_response = self.bitmovin.filters.Rotate.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_rotate_filters(sample_filter, filter_resource_response.resource)

    def test_retrieve_rotate_filter(self):
        sample_filter = self._get_sample_rotate_filter()
        created_filter_response = self.bitmovin.filters.Rotate.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_rotate_filters(sample_filter, created_filter_response.resource)

        retrieved_filter_response = self.bitmovin.filters.Rotate.retrieve(created_filter_response.resource.id)
        self.assertIsNotNone(retrieved_filter_response)
        self.assertIsNotNone(retrieved_filter_response.resource)
        self._compare_rotate_filters(created_filter_response.resource, retrieved_filter_response.resource)

    def test_delete_rotate_filter(self):
        sample_filter = self._get_sample_rotate_filter()
        created_filter_response = self.bitmovin.filters.Rotate.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_rotate_filters(sample_filter, created_filter_response.resource)

        deleted_minimal_resource = self.bitmovin.filters.Rotate.delete(created_filter_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.filters.Rotate.retrieve(created_filter_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving filter after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_rotate_filters(self):
        sample_filter = self._get_sample_rotate_filter()
        created_filter_response = self.bitmovin.filters.Rotate.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_rotate_filters(sample_filter, created_filter_response.resource)

        filters = self.bitmovin.filters.Rotate.list()
        self.assertIsNotNone(filters)
        self.assertIsNotNone(filters.resource)
        self.assertIsNotNone(filters.response)
        self.assertIsInstance(filters.resource, list)
        self.assertIsInstance(filters.response, Response)
        self.assertGreater(filters.resource.__sizeof__(), 1)

    def test_retrieve_rotate_filter_custom_data(self):
        sample_filter = self._get_sample_rotate_filter()
        sample_filter.customData = '<pre>my custom data</pre>'
        created_filter_response = self.bitmovin.filters.Rotate.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_rotate_filters(sample_filter, created_filter_response.resource)

        custom_data_response = self.bitmovin.filters.Rotate.retrieve_custom_data(created_filter_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_filter.customData, custom_data.customData)

    def _compare_rotate_filters(self, first: RotateFilter, second: RotateFilter):
        """

        :param first: RotateFilter
        :param second: RotateFilter
        :return: bool
        """
        self.assertEqual(first.rotation, second.rotation)
        return True

    def _get_sample_rotate_filter(self):
        rotate_filter = RotateFilter(rotation=90)
        self.assertIsNotNone(rotate_filter.rotation)
        return rotate_filter


if __name__ == '__main__':
    unittest.main()
