from bitmovin.resources.models import MP4Muxing as MP4MuxingResource
from .generic_muxing_service import GenericMuxingService


class MP4Muxing(GenericMuxingService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client, type_url='mp4', resource_class=MP4MuxingResource)
