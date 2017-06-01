from bitmovin.resources.models import ProgressiveTSMuxing as ProgressiveTSMuxingResource
from .generic_muxing_service import GenericMuxingService
from .progressive_ts_id3_service import ProgressiveTSID3Service


class ProgressiveTSMuxing(GenericMuxingService):

    def __init__(self, http_client):
        super().__init__(http_client=http_client, type_url='progressive-ts', resource_class=ProgressiveTSMuxingResource)
        self.ID3Tags = ProgressiveTSID3Service(http_client=http_client)
