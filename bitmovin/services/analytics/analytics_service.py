from bitmovin.bitmovin_object import BitmovinObject
from .analytics_license_service import AnalyticsLicenseService


class AnalyticsService(BitmovinObject):
    def __init__(self, http_client):
        super().__init__()
        self.http_client = http_client
        self.Licenses = AnalyticsLicenseService(http_client=self.http_client)
