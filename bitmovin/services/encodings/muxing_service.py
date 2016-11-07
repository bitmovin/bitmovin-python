from bitmovin.bitmovin_object import BitmovinObject
from .fmp4_muxing_service import FMP4Muxing
from .ts_muxing_service import TSMuxing
from .mp4_muxing_service import MP4Muxing


class MuxingService(BitmovinObject):
    def __init__(self, http_client):
        super().__init__()
        self.http_client = http_client
        self.FMP4 = FMP4Muxing(http_client=self.http_client)
        self.MP4 = MP4Muxing(http_client=self.http_client)
        self.TS = TSMuxing(http_client=self.http_client)
