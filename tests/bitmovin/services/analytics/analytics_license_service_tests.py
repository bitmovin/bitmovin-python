from bitmovin import Bitmovin
from bitmovin.resources.models import AnalyticsDomain, AnalyticsLicense
from tests.bitmovin import BitmovinTestCase


class AnalyticsLicenseServiceTests(BitmovinTestCase):

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

    def test_list_licenses(self):
        licenses_response = self.bitmovin.analytics.Licenses.list()
        licenses = licenses_response.resource
        self.assertIsInstance(licenses, list)
        self.assertGreater(len(licenses), 0)
        self.assertIsInstance(licenses[0], AnalyticsLicense)
        self.assertIsNotNone(licenses[0].licenseKey)
        self.assertIsNotNone(licenses[0].id)
        self.assertIsInstance(licenses[0].licenseKey, str)
        self.assertIsInstance(licenses[0].id, str)

    def test_get_license(self):
        first_analytics_license_id = self.settings.get('sampleObjects').get('analyticsLicenses')[0]
        license_response = self.bitmovin.analytics.Licenses.retrieve(id_=first_analytics_license_id)
        license_ = license_response.resource
        self.assertIsNotNone(license_)
        self.assertIsNotNone(license_.id)
        self.assertIsInstance(license_.id, str)
        self.assertIsNotNone(license_.licenseKey)
        self.assertIsNotNone(license_.datapoints)
        self.assertIsNotNone(license_.maxDatapoints)
        self.assertIsNotNone(license_.domains)
        self.assertIsInstance(license_.domains, list)
        self.assertGreater(len(license_.domains), 0)
        self.assertIsInstance(license_.domains[0], AnalyticsDomain)
        self.assertIsNotNone(license_.domains[0].id)
        self.assertIsNotNone(license_.domains[0].url)
        self.assertIsInstance(license_.domains[0].id, str)
        self.assertIsInstance(license_.domains[0].url, str)
