from bitmovin.resources.models import TSMuxing as TSMuxingResource
from .generic_muxing_service import GenericMuxingService
from .ts_drm_service import TSDRMService


class TSMuxing(GenericMuxingService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client, type_url='ts', resource_class=TSMuxingResource)
        self.DRM = TSDRMService(http_client=http_client)
