from bitmovin.resources.models import FMP4Muxing as FMP4MuxingResource
from .generic_muxing_service import GenericMuxingService
from .fmp4_drm_service import FMP4DRMService


class FMP4Muxing(GenericMuxingService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client, type_url='fmp4', resource_class=FMP4MuxingResource)
        self.DRM = FMP4DRMService(http_client=http_client)
