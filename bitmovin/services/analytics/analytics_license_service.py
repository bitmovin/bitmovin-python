from bitmovin.resources.models import AnalyticsLicense
from bitmovin.errors import FunctionalityNotAvailableError
from .analytics_domain_service import AnalyticsDomainService
from ..rest_service import RestService


class AnalyticsLicenseService(RestService):
    BASE_ENDPOINT_URL = 'analytics/licenses'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=AnalyticsLicense)
        self.Domains = AnalyticsDomainService(http_client=self.http_client)

    def create(self, object_, license_id):
        raise FunctionalityNotAvailableError()

    def delete(self, license_id, domain_id):
        raise FunctionalityNotAvailableError()

    def retrieve_custom_data(self, license_id, domain_id):
        raise FunctionalityNotAvailableError()
