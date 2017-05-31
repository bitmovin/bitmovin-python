import unittest
import json
from bitmovin import Bitmovin
from bitmovin.errors import BitmovinApiError
from tests.bitmovin import BitmovinTestCase
from bitmovin.resources.models.analytics import AnalyticsLicense, AnalyticsDomain

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

    def test_get_licenses(self):
        licenses = self.bitmovin.analytics.licenses.list()
        self.assertIsInstance(licenses.resource, list)
        self.assertIsInstance(licenses.resource[0].domains, list)
        self.assertIsInstance(licenses.resource[0].id, str)

    def test_get_license(self):
        license = self.bitmovin.analytics.licenses.retrieve("7353eef2-ca20-4593-b4c1-8dd81033229f")
        self.assertIsInstance(license.resource.id, str)

    def test_get_domains_from_license(self):
        license = self.bitmovin.analytics.licenses.retrieve("7353eef2-ca20-4593-b4c1-8dd81033229f")
        domains = license.resource.domains
        self.assertIsInstance(domains, list)
        self.assertIsInstance(domains[0].id, str)
        self.assertIsInstance(domains[0].url, str)

    def test_add_domain_for_license(self):
        license = self.bitmovin.analytics.licenses.retrieve("7353eef2-ca20-4593-b4c1-8dd81033229f")
        domains = license.resource.domains
        
        new_domain = self.bitmovin.analytics.licenses.add_domain(license, 'test' + str(len(domains)) + '.com').resource

        self.assertIsInstance(new_domain, AnalyticsDomain)

        license2 = self.bitmovin.analytics.licenses.retrieve("7353eef2-ca20-4593-b4c1-8dd81033229f")
        self.assertGreater(len(license2.resource.domains), len(license.resource.domains))

    def test_add_domain_with_string(self):
        license = self.bitmovin.analytics.licenses.retrieve("7353eef2-ca20-4593-b4c1-8dd81033229f")
        domains = license.resource.domains
        url = 'test' + str(len(domains)) + '.com'
        new_domain = self.bitmovin.analytics.licenses.add_domain("7353eef2-ca20-4593-b4c1-8dd81033229f", url).resource
        self.assertIsInstance(new_domain, AnalyticsDomain)
        self.assertEqual(new_domain.url, url)

    def test_delete_domain_from_license(self):
        license = self.bitmovin.analytics.licenses.retrieve("7353eef2-ca20-4593-b4c1-8dd81033229f").resource
        added_domain = self.bitmovin.analytics.licenses.add_domain("7353eef2-ca20-4593-b4c1-8dd81033229f", "to-be-deleted2.com").resource
        self.bitmovin.analytics.licenses.remove_domain("7353eef2-ca20-4593-b4c1-8dd81033229f", added_domain.id)
        license2 = self.bitmovin.analytics.licenses.retrieve("7353eef2-ca20-4593-b4c1-8dd81033229f").resource

        self.assertEqual(len(license.domains), len(license2.domains))
