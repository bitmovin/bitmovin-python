import uuid
from bitmovin import Bitmovin
from tests.bitmovin import BitmovinTestCase
from bitmovin.resources.models.analytics import AnalyticsDomain


class AnalyticsDomainServiceTests(BitmovinTestCase):

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

    def test_add_domain_to_license(self):
        first_analytics_license_id = self.settings.get('sampleObjects').get('analyticsLicenses')[0]
        license_response = self.bitmovin.analytics.Licenses.retrieve(id_=first_analytics_license_id)
        analytics_license = license_response.resource
        domains = self.bitmovin.analytics.Licenses.Domains.list(license_id=first_analytics_license_id)
        self.assertIsNotNone(domains.resource)
        new_domain_name = 'test' + str(len(analytics_license.domains)) + '.com'
        new_domain = self.bitmovin.analytics.Licenses.Domains.create(
            object_=AnalyticsDomain(url=new_domain_name),
            license_id=first_analytics_license_id
        ).resource
        self.assertIsInstance(new_domain, AnalyticsDomain)
        retrieved_license = self.bitmovin.analytics.Licenses.retrieve(id_=first_analytics_license_id).resource
        self.assertGreater(len(retrieved_license.domains), len(analytics_license.domains))

    def test_delete_domain_from_license(self):
        first_analytics_license_id = self.settings.get('sampleObjects').get('analyticsLicenses')[0]
        analytics_license = self.bitmovin.analytics.Licenses.retrieve(id_=first_analytics_license_id).resource
        analytics_domain = AnalyticsDomain(url='to-be-deleted2-{}.com'.format(uuid.uuid4()))
        added_domain = self.bitmovin.analytics.Licenses.Domains.create(license_id=first_analytics_license_id,
                                                                       object_=analytics_domain).resource
        self.bitmovin.analytics.Licenses.Domains.delete(license_id=first_analytics_license_id,
                                                        domain_id=added_domain.id)
        retrieved_license = self.bitmovin.analytics.Licenses.retrieve(id_=first_analytics_license_id).resource
        self.assertEqual(len(analytics_license.domains), len(retrieved_license.domains))

    def test_list_domains(self):
        first_analytics_license_id = self.settings.get('sampleObjects').get('analyticsLicenses')[0]
        analytics_license = self.bitmovin.analytics.Licenses.retrieve(id_=first_analytics_license_id).resource
        analytics_license_domains = self.bitmovin.analytics.Licenses.Domains.list(
            license_id=first_analytics_license_id).resource
        self.assertEqual(len(analytics_license.domains), len(analytics_license_domains))
        analytics_domain = AnalyticsDomain(url='to-be-deleted2-{}.com'.format(uuid.uuid4()))
        added_domain = self.bitmovin.analytics.Licenses.Domains.create(license_id=first_analytics_license_id,
                                                                       object_=analytics_domain).resource
        listed_domains = self.bitmovin.analytics.Licenses.Domains.list(
            license_id=first_analytics_license_id).resource
        self.assertEquals(len(listed_domains) - len(analytics_license_domains), 1)
