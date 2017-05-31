from .bitmovin_object import BitmovinObject
from .rest import BitmovinHttpClient
from .services import InputService, OutputService, FilterService, CodecConfigurationService, EncodingService, \
    ManifestService, InfrastructureService, AnalyticsLicenseService


class Bitmovin(BitmovinObject):
    def __init__(self, api_key, api_base_url=None):
        super().__init__()
        self._api_key = api_key
        self._api_base_url = api_base_url
        self._http_client = BitmovinHttpClient(api_key=self._api_key, base_url=self._api_base_url)
        self.inputs = InputService(http_client=self._http_client)
        self.outputs = OutputService(http_client=self._http_client)
        self.filters = FilterService(http_client=self._http_client)
        self.codecConfigurations = CodecConfigurationService(http_client=self._http_client)
        self.encodings = EncodingService(http_client=self._http_client)
        self.manifests = ManifestService(http_client=self._http_client)
        self.infrastructures = InfrastructureService(http_client=self._http_client)
        self.analytics = AnalyticsLicenseService(http_client=self._http_client)
