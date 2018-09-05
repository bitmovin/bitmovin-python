from bitmovin.resources import SmoothManifest
from .manifest_control_service import ManifestControlService
from ..rest_service import RestService
from .smooth_representation_service import MP4RepresentationService
from .smooth_content_protection_service import SmoothContentProtectionService


class Smooth(RestService, ManifestControlService):
    BASE_ENDPOINT_URL = 'encoding/manifests/smooth'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, relative_url=self.BASE_ENDPOINT_URL, class_=SmoothManifest)

        self.MP4Representation = MP4RepresentationService(http_client=http_client)
        self.ContentProtection = SmoothContentProtectionService(http_client=http_client)
