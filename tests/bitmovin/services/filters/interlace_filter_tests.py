import json
import unittest

from bitmovin import Bitmovin, Response, InterlaceFilter, InterlaceMode, VerticalLowPassFilteringMode
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class InterlaceFilterTests(BitmovinTestCase):

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

    def test_create_interlace_filter(self):
        sample_filter = self._get_sample_interlace_filter()
        filter_resource_response = self.bitmovin.filters.Interlace.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_interlace_filters(sample_filter, filter_resource_response.resource)

    def test_create_interlace_filter_without_name(self):
        sample_filter = self._get_sample_interlace_filter()
        sample_filter.name = None
        filter_resource_response = self.bitmovin.filters.Interlace.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_interlace_filters(sample_filter, filter_resource_response.resource)

    def test_retrieve_interlace_filter(self):
        sample_filter = self._get_sample_interlace_filter()
        created_filter_response = self.bitmovin.filters.Interlace.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_interlace_filters(sample_filter, created_filter_response.resource)

        retrieved_filter_response = self.bitmovin.filters.Interlace.retrieve(created_filter_response.resource.id)
        self.assertIsNotNone(retrieved_filter_response)
        self.assertIsNotNone(retrieved_filter_response.resource)
        self._compare_interlace_filters(created_filter_response.resource, retrieved_filter_response.resource)

    def test_delete_interlace_filter(self):
        sample_filter = self._get_sample_interlace_filter()
        created_filter_response = self.bitmovin.filters.Interlace.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_interlace_filters(sample_filter, created_filter_response.resource)

        deleted_minimal_resource = self.bitmovin.filters.Interlace.delete(created_filter_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.filters.Interlace.retrieve(created_filter_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving filter after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_interlace_filters(self):
        sample_filter = self._get_sample_interlace_filter()
        created_filter_response = self.bitmovin.filters.Interlace.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_interlace_filters(sample_filter, created_filter_response.resource)

        filters = self.bitmovin.filters.Interlace.list()
        self.assertIsNotNone(filters)
        self.assertIsNotNone(filters.resource)
        self.assertIsNotNone(filters.response)
        self.assertIsInstance(filters.resource, list)
        self.assertIsInstance(filters.response, Response)
        self.assertGreater(filters.resource.__sizeof__(), 1)

    def test_retrieve_interlace_filter_custom_data(self):
        sample_filter = self._get_sample_interlace_filter()
        sample_filter.customData = '<pre>my custom data</pre>'
        created_filter_response = self.bitmovin.filters.Interlace.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_interlace_filters(sample_filter, created_filter_response.resource)

        custom_data_response = self.bitmovin.filters.Interlace.retrieve_custom_data(created_filter_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_filter.customData, json.loads(custom_data.customData))

    def _compare_interlace_filters(self, first: InterlaceFilter, second: InterlaceFilter):
        """

        :param first: InterlaceFilter
        :param second: InterlaceFilter
        :return: bool
        """
        self.assertEqual(first.mode, second.mode)
        self.assertEqual(first.verticalLowPassFilteringMode, second.verticalLowPassFilteringMode)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _get_sample_interlace_filter(self):
        interlace_filter = InterlaceFilter(name='Sample Interlace Filter py',
                                           mode=InterlaceMode.INTERLACE_X2,
                                           vertical_low_pass_filtering_mode=VerticalLowPassFilteringMode.COMPLEX)
        return interlace_filter


if __name__ == '__main__':
    unittest.main()
