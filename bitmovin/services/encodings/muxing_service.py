from bitmovin.bitmovin_object import BitmovinObject
from .fmp4_muxing_service import FMP4Muxing
from .ts_muxing_service import TSMuxing
from .mp4_muxing_service import MP4Muxing
from .webm_muxing_service import WebMMuxing
from .progressive_ts_muxing_service import ProgressiveTSMuxing
from .progressive_mov_muxing_service import ProgressiveMOVMuxing
from .broadcast_ts_muxing_service import BroadcastTsMuxing
from .progressive_webm_muxing_service import ProgressiveWebMMuxing
from .segmented_raw_muxing_service import SegmentedRawMuxing


class MuxingService(BitmovinObject):
    def __init__(self, http_client):
        super().__init__()
        self.http_client = http_client
        self.FMP4 = FMP4Muxing(http_client=self.http_client)
        self.MP4 = MP4Muxing(http_client=self.http_client)
        self.TS = TSMuxing(http_client=self.http_client)
        self.WebM = WebMMuxing(http_client=self.http_client)
        self.ProgressiveTS = ProgressiveTSMuxing(http_client=self.http_client)
        self.ProgressiveMOV = ProgressiveMOVMuxing(http_client=self.http_client)
        self.BroadcastTS = BroadcastTsMuxing(http_client=self.http_client)
        self.ProgressiveWebM = ProgressiveWebMMuxing(http_client=self.http_client)
        self.SegmentedRaw = SegmentedRawMuxing(http_client=self.http_client)
