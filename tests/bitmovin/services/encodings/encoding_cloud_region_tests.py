import unittest

from bitmovin import Bitmovin, Encoding, CloudRegion
from tests.bitmovin import BitmovinTestCase


class EncodingCloudRegionTests(BitmovinTestCase):

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

    def test_create_encoding_cloud_region_auto(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AUTO)

    def test_create_encoding_cloud_region_azure_europe_west(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AZURE_EUROPE_WEST)

    def test_create_encoding_cloud_region_aws_ap_northeast_1(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AWS_AP_NORTHEAST_1)

    def test_create_encoding_cloud_region_aws_ap_northeast_2(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AWS_AP_NORTHEAST_2)

    def test_create_encoding_cloud_region_aws_ap_southeast_1(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AWS_AP_SOUTHEAST_1)

    def test_create_encoding_cloud_region_aws_ap_southeast_2(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AWS_AP_SOUTHEAST_2)

    def test_create_encoding_cloud_region_aws_ap_south_1(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AWS_AP_SOUTH_1)

    def test_create_encoding_cloud_region_aws_eu_central_1(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AWS_EU_CENTRAL_1)

    def test_create_encoding_cloud_region_aws_eu_west_1(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AWS_EU_WEST_1)

    def test_create_encoding_cloud_region_aws_sa_east_1(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AWS_SA_EAST_1)

    def test_create_encoding_cloud_region_aws_us_east_1(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AWS_US_EAST_1)

    def test_create_encoding_cloud_region_aws_us_west_1(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AWS_US_WEST_1)

    def test_create_encoding_cloud_region_aws_us_west_2(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AWS_US_WEST_2)

    def test_create_encoding_cloud_region_google_asia_east_1(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.GOOGLE_ASIA_EAST_1)

    def test_create_encoding_cloud_region_google_europe_west_1(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)

    def test_create_encoding_cloud_region_google_us_central_1(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.GOOGLE_US_CENTRAL_1)

    def test_create_encoding_cloud_region_google_us_west_1(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.GOOGLE_US_WEST_1)

    def test_create_encoding_cloud_region_google_us_east_1(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.GOOGLE_US_EAST_1)

    def test_create_encoding_cloud_region_north_america(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.NORTH_AMERICA)

    def test_create_encoding_cloud_region_south_america(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.SOUTH_AMERICA)

    def test_create_encoding_cloud_region_europe(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.EUROPE)

    def test_create_encoding_cloud_region_africa(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AFRICA)

    def test_create_encoding_cloud_region_asia(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.ASIA)

    def test_create_encoding_cloud_region_australia(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AUSTRALIA)

    def test_create_encoding_cloud_region_aws(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.AWS)

    def test_create_encoding_cloud_region_google(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.GOOGLE)

    def test_create_encoding_cloud_region_kubernetes(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.KUBERNETES)

    def test_create_encoding_cloud_region_external(self):
        self._test_create_encoding_cloud_region(cloud_region=CloudRegion.EXTERNAL)

    def _test_create_encoding_cloud_region(self, cloud_region):
        self.assertIsNotNone(cloud_region)
        sample_encoding = self._get_sample_encoding()
        sample_encoding.cloudRegion = cloud_region
        encoding_resource_response = self.bitmovin.encodings.Encoding.create(sample_encoding)
        self._verify_response_is_not_empty(response=encoding_resource_response)
        self.assertEqual(first=cloud_region.value, second=encoding_resource_response.resource.cloudRegion)

    def _verify_response_is_not_empty(self, response):
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.resource)
        self.assertIsNotNone(response.resource.id)
        self.assertIsNotNone(response.resource.cloudRegion)

    def _get_sample_encoding(self):
        encoding = Encoding(name='Sample Encoding bitmovin-python',
                            description='Sample encoding used in bitmovin-python API client tests',
                            cloud_region=CloudRegion.GOOGLE_EUROPE_WEST_1)
        self.assertIsNotNone(encoding.name)
        self.assertIsNotNone(encoding.description)
        self.assertIsNotNone(encoding.cloudRegion)
        return encoding


if __name__ == '__main__':
    unittest.main()
