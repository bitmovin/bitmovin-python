from bitmovin.resources.models import BroadcastTsMuxing as BroadcastTsMuxingResource
from .generic_muxing_service import GenericMuxingService


class BroadcastTsMuxing(GenericMuxingService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client, type_url='broadcast-ts', resource_class=BroadcastTsMuxingResource)
