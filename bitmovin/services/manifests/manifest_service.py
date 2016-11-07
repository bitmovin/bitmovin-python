from bitmovin.bitmovin_object import BitmovinObject
from .dash_manifest_service import DASH


class ManifestService(BitmovinObject):
    def __init__(self, http_client):
        super().__init__()
        self.http_client = http_client
        self.DASH = DASH(http_client=self.http_client)
