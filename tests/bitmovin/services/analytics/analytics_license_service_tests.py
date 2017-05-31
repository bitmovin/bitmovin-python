import unittest
import json
from bitmovin import Bitmovin
from bitmovin.errors import BitmovinApiError
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

    def test_get_licenses(self):
        licenses = self.bitmovin.analytics.list()
        self.assertIsInstance(licenses.resource, list)
        self.assertIsInstance(licenses.resource[0].domains, list)
        self.assertIsInstance(licenses.resource[0].id, str)

    def test_get_license(self):
        license = self.bitmovin.analytics.retrieve("7353eef2-ca20-4593-b4c1-8dd81033229f")
        self.assertIsInstance(license.resource.id, str)

    def test_get_domains_from_license(self):
        license = self.bitmovin.analytics.retrieve("7353eef2-ca20-4593-b4c1-8dd81033229f")
        domains = license.resource.domains
        self.assertIsInstance(domains, list)
