import json
import unittest

from bitmovin import Bitmovin, Response, UnsharpFilter
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class UnsharpFilterTests(BitmovinTestCase):

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

    def test_create_unsharp_filter(self):
        sample_filter = self._get_sample_unsharp_filter()
        filter_resource_response = self.bitmovin.filters.Unsharp.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_unsharp_filters(sample_filter, filter_resource_response.resource)

    def test_create_unsharp_filter_without_name(self):
        sample_filter = self._get_sample_unsharp_filter()
        sample_filter.name = None
        filter_resource_response = self.bitmovin.filters.Unsharp.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_unsharp_filters(sample_filter, filter_resource_response.resource)

    def test_retrieve_unsharp_filter(self):
        sample_filter = self._get_sample_unsharp_filter()
        created_filter_response = self.bitmovin.filters.Unsharp.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_unsharp_filters(sample_filter, created_filter_response.resource)

        retrieved_filter_response = self.bitmovin.filters.Unsharp.retrieve(created_filter_response.resource.id)
        self.assertIsNotNone(retrieved_filter_response)
        self.assertIsNotNone(retrieved_filter_response.resource)
        self._compare_unsharp_filters(created_filter_response.resource, retrieved_filter_response.resource)

    def test_delete_unsharp_filter(self):
        sample_filter = self._get_sample_unsharp_filter()
        created_filter_response = self.bitmovin.filters.Unsharp.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_unsharp_filters(sample_filter, created_filter_response.resource)

        deleted_minimal_resource = self.bitmovin.filters.Unsharp.delete(created_filter_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.filters.Unsharp.retrieve(created_filter_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving filter after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_unsharp_filters(self):
        sample_filter = self._get_sample_unsharp_filter()
        created_filter_response = self.bitmovin.filters.Unsharp.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_unsharp_filters(sample_filter, created_filter_response.resource)

        filters = self.bitmovin.filters.Unsharp.list()
        self.assertIsNotNone(filters)
        self.assertIsNotNone(filters.resource)
        self.assertIsNotNone(filters.response)
        self.assertIsInstance(filters.resource, list)
        self.assertIsInstance(filters.response, Response)
        self.assertGreater(filters.resource.__sizeof__(), 1)

    def test_retrieve_unsharp_filter_custom_data(self):
        sample_filter = self._get_sample_unsharp_filter()
        sample_filter.customData = '<pre>my custom data</pre>'
        created_filter_response = self.bitmovin.filters.Unsharp.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_unsharp_filters(sample_filter, created_filter_response.resource)

        custom_data_response = self.bitmovin.filters.Unsharp.retrieve_custom_data(created_filter_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_filter.customData, json.loads(custom_data.customData))

    def _compare_unsharp_filters(self, first: UnsharpFilter, second: UnsharpFilter):
        """

        :param first: UnsharpFilter
        :param second: UnsharpFilter
        :return: bool
        """
        self.assertEqual(first.lumaMatrixHorizontalSize, second.lumaMatrixHorizontalSize)
        self.assertEqual(first.lumaMatrixVerticalSize, second.lumaMatrixVerticalSize)
        self.assertEqual(first.lumaEffectStrength, second.lumaEffectStrength)
        self.assertEqual(first.chromaMatrixHorizontalSize, second.chromaMatrixHorizontalSize)
        self.assertEqual(first.chromaMatrixVerticalSize, second.chromaMatrixVerticalSize)
        self.assertEqual(first.chromaEffectStrength, second.chromaEffectStrength)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _get_sample_unsharp_filter(self):
        unsharp_filter = UnsharpFilter(name='Sample Unsharp Filter py',
                                       description='sample py unsharp filter',
                                       luma_matrix_horizontal_size=5,
                                       luma_matrix_vertical_size=7,
                                       luma_effect_strength=1.3,
                                       chroma_matrix_horizontal_size=9,
                                       chroma_matrix_vertical_size=11,
                                       chroma_effect_strength=1.01)
        return unsharp_filter


if __name__ == '__main__':
    unittest.main()
