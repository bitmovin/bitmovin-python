import json
import unittest

from bitmovin import Bitmovin, Response, DenoiseHqdn3dFilter, PictureFieldParity
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class DenoiseHqdn3dFilterTestTests(BitmovinTestCase):

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

    def test_create_denoise_hqdn3d_filter(self):
        sample_filter = self._get_sample_denoise_hqdn3d_filter()
        filter_resource_response = self.bitmovin.filters.DenoiseHqdn3d.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_denoise_hqdn3d_filters(sample_filter, filter_resource_response.resource)

    def test_create_denoise_hqdn3d_filter_without_name(self):
        sample_filter = self._get_sample_denoise_hqdn3d_filter()
        sample_filter.name = None
        filter_resource_response = self.bitmovin.filters.DenoiseHqdn3d.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_denoise_hqdn3d_filters(sample_filter, filter_resource_response.resource)

    def test_retrieve_denoise_hqdn3d_filter(self):
        sample_filter = self._get_sample_denoise_hqdn3d_filter()
        created_filter_response = self.bitmovin.filters.DenoiseHqdn3d.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_denoise_hqdn3d_filters(sample_filter, created_filter_response.resource)

        retrieved_filter_response = self.bitmovin.filters.DenoiseHqdn3d.retrieve(created_filter_response.resource.id)
        self.assertIsNotNone(retrieved_filter_response)
        self.assertIsNotNone(retrieved_filter_response.resource)
        self._compare_denoise_hqdn3d_filters(created_filter_response.resource, retrieved_filter_response.resource)

    def test_delete_denoise_hqdn3d_filter(self):
        sample_filter = self._get_sample_denoise_hqdn3d_filter()
        created_filter_response = self.bitmovin.filters.DenoiseHqdn3d.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_denoise_hqdn3d_filters(sample_filter, created_filter_response.resource)

        deleted_minimal_resource = self.bitmovin.filters.DenoiseHqdn3d.delete(created_filter_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.filters.DenoiseHqdn3d.retrieve(created_filter_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving filter after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_denoise_hqdn3d_filters(self):
        sample_filter = self._get_sample_denoise_hqdn3d_filter()
        created_filter_response = self.bitmovin.filters.DenoiseHqdn3d.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_denoise_hqdn3d_filters(sample_filter, created_filter_response.resource)

        filters = self.bitmovin.filters.DenoiseHqdn3d.list()
        self.assertIsNotNone(filters)
        self.assertIsNotNone(filters.resource)
        self.assertIsNotNone(filters.response)
        self.assertIsInstance(filters.resource, list)
        self.assertIsInstance(filters.response, Response)
        self.assertGreater(filters.resource.__sizeof__(), 1)

    def test_retrieve_denoise_hqdn3d_filter_custom_data(self):
        sample_filter = self._get_sample_denoise_hqdn3d_filter()
        sample_filter.customData = '<pre>my custom data</pre>'
        created_filter_response = self.bitmovin.filters.DenoiseHqdn3d.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_denoise_hqdn3d_filters(sample_filter, created_filter_response.resource)

        custom_data_response = self.bitmovin.filters.DenoiseHqdn3d.retrieve_custom_data(created_filter_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_filter.customData, json.loads(custom_data.customData))

    def _compare_denoise_hqdn3d_filters(self, first: DenoiseHqdn3dFilter, second: DenoiseHqdn3dFilter):
        """

        :param first: DenoiseHqdn3dFilter
        :param second: DenoiseHqdn3dFilter
        :return: bool
        """
        self.assertEqual(first.lumaSpatial, second.lumaSpatial)
        self.assertEqual(first.chromaSpatial, second.chromaSpatial)
        self.assertEqual(first.lumaTmp, second.lumaTmp)
        self.assertEqual(first.chromaTmp, second.chromaTmp)
        self.assertEqual(first.name, second.name)
        self.assertEqual(first.description, second.description)
        return True

    def _get_sample_denoise_hqdn3d_filter(self):
        denoise_hqdn3d_filter = DenoiseHqdn3dFilter(name='Sample DenoiseHqdn3d Filter 1 2 3 4',
                                                    luma_spatial=1.0, chroma_spatial=2.0,
                                                    luma_tmp=3.0, chroma_tmp=4.0)
        self.assertIsNotNone(denoise_hqdn3d_filter.lumaSpatial)
        self.assertIsNotNone(denoise_hqdn3d_filter.chromaSpatial)
        self.assertIsNotNone(denoise_hqdn3d_filter.lumaTmp)
        self.assertIsNotNone(denoise_hqdn3d_filter.chromaTmp)
        return denoise_hqdn3d_filter


if __name__ == '__main__':
    unittest.main()
