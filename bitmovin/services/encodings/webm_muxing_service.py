from bitmovin.resources.models import WebMMuxing as WebMMuxingResource
from .generic_muxing_service import GenericMuxingService
from .webm_drm_service import WebMDRMService


class WebMMuxing(GenericMuxingService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client, type_url='webm', resource_class=WebMMuxingResource)
        self.DRM = WebMDRMService(http_client=http_client)
