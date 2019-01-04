from bitmovin.resources.models import SegmentedRawMuxing as SegmentedRawMuxingResource
from .generic_muxing_service import GenericMuxingService


class SegmentedRawMuxing(GenericMuxingService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client, type_url='segmented-raw', resource_class=SegmentedRawMuxingResource)
