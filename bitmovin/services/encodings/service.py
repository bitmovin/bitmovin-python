from bitmovin.bitmovin_object import BitmovinObject
from .encoding_service import Encoding
from .stream_service import Stream
from .muxing_service import MuxingService
from .keyframe_service import KeyframeService
from .input_analysis_service import InputAnalysisService


class EncodingService(BitmovinObject):
    def __init__(self, http_client):
        super().__init__()
        self.http_client = http_client
        self.Encoding = Encoding(http_client=self.http_client)
        self.Stream = Stream(http_client=self.http_client)
        self.Muxing = MuxingService(http_client=self.http_client)
        self.Keyframe = KeyframeService(http_client=self.http_client)
        self.InputAnalysis = InputAnalysisService(http_client=self.http_client)
