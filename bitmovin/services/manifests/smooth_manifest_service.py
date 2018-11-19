from bitmovin.resources import SmoothManifest
from bitmovin.services.manifests.generic_manifest_service import GenericManifestService
from .manifest_control_service import ManifestControlService
from .smooth_representation_service import MP4RepresentationService
from .smooth_content_protection_service import SmoothContentProtectionService


class Smooth(GenericManifestService, ManifestControlService):
    manifest_type = 'smooth'

    def __init__(self, http_client):
        super().__init__(http_client=http_client, manifest_type=self.manifest_type, resource_class=SmoothManifest)

        self.MP4Representation = MP4RepresentationService(http_client=http_client)
        self.ContentProtection = SmoothContentProtectionService(http_client=http_client)
