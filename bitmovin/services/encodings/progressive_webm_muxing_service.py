from bitmovin.resources.models import ProgressiveWebMMuxing as ProgressiveWebMMuxingResource
from .generic_muxing_service import GenericMuxingService


class ProgressiveWebMMuxing(GenericMuxingService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client, type_url='progressive-webm',
                         resource_class=ProgressiveWebMMuxingResource)
