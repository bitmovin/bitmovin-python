import json
import unittest

from bitmovin import Bitmovin, Response, TextFilter, Font
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase


class TextFilterTests(BitmovinTestCase):

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

    def test_create_text_filter(self):
        sample_filter = self._get_sample_text_filter()
        filter_resource_response = self.bitmovin.filters.Text.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_text_filters(sample_filter, filter_resource_response.resource)

    def test_create_text_filter_without_name(self):
        sample_filter = self._get_sample_text_filter()
        sample_filter.name = None
        filter_resource_response = self.bitmovin.filters.Text.create(sample_filter)
        self.assertIsNotNone(filter_resource_response)
        self.assertIsNotNone(filter_resource_response.resource)
        self.assertIsNotNone(filter_resource_response.resource.id)
        self._compare_text_filters(sample_filter, filter_resource_response.resource)

    def test_retrieve_text_filter(self):
        sample_filter = self._get_sample_text_filter()
        created_filter_response = self.bitmovin.filters.Text.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_text_filters(sample_filter, created_filter_response.resource)

        retrieved_filter_response = self.bitmovin.filters.Text.retrieve(created_filter_response.resource.id)
        self.assertIsNotNone(retrieved_filter_response)
        self.assertIsNotNone(retrieved_filter_response.resource)
        self._compare_text_filters(created_filter_response.resource, retrieved_filter_response.resource)

    def test_delete_text_filter(self):
        sample_filter = self._get_sample_text_filter()
        created_filter_response = self.bitmovin.filters.Text.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_text_filters(sample_filter, created_filter_response.resource)

        deleted_minimal_resource = self.bitmovin.filters.Text.delete(created_filter_response.resource.id)
        self.assertIsNotNone(deleted_minimal_resource)
        self.assertIsNotNone(deleted_minimal_resource.resource)
        self.assertIsNotNone(deleted_minimal_resource.resource.id)

        try:
            self.bitmovin.filters.Text.retrieve(created_filter_response.resource.id)
            self.fail(
                'Previous statement should have thrown an exception. ' +
                'Retrieving filter after deleting it shouldn\'t be possible.'
            )
        except BitmovinApiError:
            pass

    def test_list_text_filters(self):
        sample_filter = self._get_sample_text_filter()
        created_filter_response = self.bitmovin.filters.Text.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_text_filters(sample_filter, created_filter_response.resource)

        filters = self.bitmovin.filters.Text.list()
        self.assertIsNotNone(filters)
        self.assertIsNotNone(filters.resource)
        self.assertIsNotNone(filters.response)
        self.assertIsInstance(filters.resource, list)
        self.assertIsInstance(filters.response, Response)
        self.assertGreater(filters.resource.__sizeof__(), 1)

    def test_retrieve_text_filter_custom_data(self):
        sample_filter = self._get_sample_text_filter()
        sample_filter.customData = '<pre>my custom data</pre>'
        created_filter_response = self.bitmovin.filters.Text.create(sample_filter)
        self.assertIsNotNone(created_filter_response)
        self.assertIsNotNone(created_filter_response.resource)
        self.assertIsNotNone(created_filter_response.resource.id)
        self._compare_text_filters(sample_filter, created_filter_response.resource)

        custom_data_response = self.bitmovin.filters.Text.retrieve_custom_data(
            created_filter_response.resource.id)
        custom_data = custom_data_response.resource
        self.assertEqual(sample_filter.customData, json.loads(custom_data.customData))

    def _compare_text_filters(self, first: TextFilter, second: TextFilter):
        """

        :param first: TextFilter
        :param second: TextFilter
        :return: bool
        """
        self.assertEqual(str(first.x), str(second.x))
        self.assertEqual(str(first.y), str(second.y))
        self.assertEqual(first.text, second.text)
        self.assertEqual(first.timecode, second.timecode)
        self.assertEqual(first.shadowY, second.shadowX)
        self.assertEqual(first.shadowX, second.shadowX)
        self.assertEqual(first.shadowColor, second.shadowColor)
        self.assertEqual(first.alpha, second.alpha)
        self.assertEqual(first.fontSize, second.fontSize)
        self.assertEqual(first.font, second.font)
        self.assertEqual(first.fontColor, second.fontColor)
        self.assertEqual(first.fixBounds, second.fixBounds)
        self.assertEqual(first.borderWidth, second.borderWidth)
        self.assertEqual(first.lineSpacing, second.lineSpacing)
        self.assertEqual(first.boxColor, second.boxColor)
        self.assertEqual(first.boxBorderWidth, second.boxBorderWidth)
        self.assertEqual(first.box, second.box)
        self.assertEqual(first.description, second.description)
        self.assertEqual(first.name, second.name)
        return True

    def _get_sample_text_filter(self):
        text_filter = TextFilter(name='Sample Text Filter',
                                 x='10',
                                 y='10',
                                 text='ThisIsATest',
                                 font=Font.DEJAVUSANS)

        self.assertIsNotNone(text_filter.x)
        self.assertIsNotNone(text_filter.y)
        self.assertIsNotNone(text_filter.name)
        self.assertIsNotNone(text_filter.font)
        return text_filter


if __name__ == '__main__':
    unittest.main()
